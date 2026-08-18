#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


TABLE_LABEL_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)_TextPointers:\s*$")
DW_CONST_RE = re.compile(
    r"^(\s*dw_const\s+)([A-Za-z_][A-Za-z0-9_]*)(\s*,\s*[A-Za-z0-9_]+\s*(?:;.*)?)$"
)
GLOBAL_LABEL_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(?:;.*)?$")


@dataclass
class Block:
    start: int
    end: int
    lines: list[str]


def find_table(lines: list[str]) -> tuple[int, int, list[tuple[int, str]]] | None:
    for i, line in enumerate(lines):
        if not TABLE_LABEL_RE.match(line):
            continue
        j = i + 1
        entries: list[tuple[int, str]] = []
        while j < len(lines):
            cur = lines[j]
            if not cur.strip() or cur.lstrip().startswith(";") or cur.strip() == "def_text_pointers":
                j += 1
                continue
            m = DW_CONST_RE.match(cur)
            if not m:
                break
            entries.append((j, m.group(2)))
            j += 1
        if entries:
            return i, j, entries
    return None


def find_global_labels(lines: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for i, line in enumerate(lines):
        m = GLOBAL_LABEL_RE.match(line)
        if m:
            result[m.group(1)] = i
    return result


def block_for_label(lines: list[str], labels: dict[str, int], label: str) -> Block | None:
    if label not in labels:
        return None
    start = labels[label]
    next_global = len(lines)
    for i in range(start + 1, len(lines)):
        if GLOBAL_LABEL_RE.match(lines[i]):
            next_global = i
            break
    return Block(start=start, end=next_global, lines=lines[start:next_global])


def token_count(lines: list[str], token: str) -> int:
    pat = re.compile(rf"(?<![A-Za-z0-9_]){re.escape(token)}(?![A-Za-z0-9_])")
    return sum(len(pat.findall(line)) for line in lines)


def rewrite_dw_const(line: str, new_label: str) -> str:
    m = DW_CONST_RE.match(line)
    if not m:
        return line
    return f"{m.group(1)}{new_label}{m.group(3)}"


def process_script(path: Path, apply: bool) -> tuple[int, int]:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    table = find_table(lines)
    if table is None:
        return 0, 0

    table_start, table_end, entries = table
    labels = find_global_labels(lines)

    refs_in_table: dict[str, int] = {}
    for _, lbl in entries:
        refs_in_table[lbl] = refs_in_table.get(lbl, 0) + 1

    candidate_labels = [lbl for _, lbl in entries]
    blocks: dict[str, Block] = {}
    for label in set(candidate_labels):
        block = block_for_label(lines, labels, label)
        if block is None:
            continue
        blocks[label] = block

    external_use: dict[str, bool] = {}
    for label, table_refs in refs_in_table.items():
        # One occurrence in definition + N in this table.
        expected = 1 + table_refs
        external_use[label] = token_count(lines, label) > expected

    canonical_for_text: dict[str, str] = {}
    remap: dict[str, str] = {}
    for label in candidate_labels:
        block = blocks.get(label)
        if block is None or external_use.get(label, True):
            continue
        block_text = "\n".join(block.lines[1:]).strip()
        if not block_text:
            continue
        canonical = canonical_for_text.get(block_text)
        if canonical is None:
            canonical_for_text[block_text] = label
            continue
        if canonical != label:
            remap[label] = canonical

    if not remap:
        return 0, 0

    new_lines = lines[:]
    for idx, old_label in entries:
        new_label = remap.get(old_label)
        if new_label is None:
            continue
        new_lines[idx] = rewrite_dw_const(new_lines[idx], new_label)

    # Delete now-unreferenced duplicate text blocks.
    delete_ranges: list[tuple[int, int]] = []
    for duplicate_label in sorted(remap):
        block = blocks[duplicate_label]
        # If this label still has references, keep it.
        if token_count(new_lines, duplicate_label) > 1:
            continue
        delete_ranges.append((block.start, block.end))

    for start, end in sorted(delete_ranges, reverse=True):
        del new_lines[start:end]

    updated = "\n".join(new_lines) + "\n"
    changed = 1 if updated != original else 0

    if apply and changed:
        path.write_text(updated, encoding="utf-8")

    return changed, len(remap)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Deduplicate identical map text blocks by repointing *_TextPointers "
            "dw_const entries and removing unreferenced duplicates."
        )
    )
    parser.add_argument("--apply", action="store_true", help="Write changes to files")
    parser.add_argument(
        "--scripts-dir",
        default="scripts",
        help="Directory containing map script asm files (default: scripts)",
    )
    args = parser.parse_args()

    scripts_dir = Path(args.scripts_dir)
    files = sorted(scripts_dir.glob("*.asm"))

    changed_files = 0
    total_repoints = 0
    for file in files:
        changed, repoints = process_script(file, apply=args.apply)
        changed_files += changed
        total_repoints += repoints
        if changed:
            print(f"updated {file} ({repoints} repoints)")

    mode = "applied" if args.apply else "dry-run"
    print(
        f"{mode}: scanned {len(files)} files, "
        f"would_update={changed_files}, repoints={total_repoints}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
