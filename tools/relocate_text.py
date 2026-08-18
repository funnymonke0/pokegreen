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
LOCAL_LABEL_RE = re.compile(r"^\s*\.[A-Za-z_][A-Za-z0-9_]*:\s*(?:;.*)?$")
RELOCATED_LINE_RE = re.compile(r"^\s*ld\s+hl\s*,\s*(RelocatedText_[A-Za-z0-9_]+)\s*$")
STRING_RE = re.compile(r'"([^"]*)"')

ALLOWED_TEXT_MACROS = (
    "text ",
    "line ",
    "cont ",
    "para ",
    "next ",
    "_cnt ",
    "scrl ",
    "done",
    "prompt",
    "text_end",
    "text_waitbutton",
    "text_scroll",
    "text_pause",
    "text_dots ",
)


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


def strip_comment(line: str) -> str:
    if ";" in line:
        return line.split(";", 1)[0].rstrip()
    return line.rstrip()


def first_meaningful_line(lines: list[str]) -> str | None:
    for line in lines:
        stripped = strip_comment(line).strip()
        if stripped:
            return stripped
    return None


def is_already_relocated_stub(block: Block) -> str | None:
    for line in block.lines[1:]:
        m = RELOCATED_LINE_RE.match(strip_comment(line).strip())
        if m:
            return m.group(1)
    return None


def text_payload_char_count(block: Block) -> int:
    total = 0
    for line in block.lines[1:]:
        for m in STRING_RE.finditer(line):
            total += len(m.group(1))
    return total


def is_relocatable_text_block(block: Block) -> bool:
    body = block.lines[1:]
    if not body:
        return False

    first = first_meaningful_line(body)
    if first is None or not first.startswith("text "):
        return False

    for line in body:
        code = strip_comment(line).strip()
        if not code:
            continue
        if LOCAL_LABEL_RE.match(code):
            return False
        if code.startswith("text_asm") or code.startswith("script_"):
            return False
        if not code.startswith(ALLOWED_TEXT_MACROS):
            return False

    return True


def make_stub(label: str, relocated_label: str) -> list[str]:
    return [
        f"{label}:",
        "\ttext_asm",
        f"\tld hl, {relocated_label}",
        f"\tld a, BANK({relocated_label})",
        "\tldh [hLoadedROMBank], a",
        "\tld [rROMB], a",
        "\tcall PrintText",
        "\tld a, [wCurMap]",
        "\tcall SwitchToMapRomBank",
        "\tjp TextScriptEnd",
        "",
    ]


def process_script(
    path: Path, min_chars: int, apply: bool
) -> tuple[bool, list[tuple[str, list[str]]], set[str], int]:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    table = find_table(lines)
    if table is None:
        return False, [], set(), 0

    _, _, entries = table
    labels = find_global_labels(lines)

    unique_labels: list[str] = []
    seen: set[str] = set()
    for _, label in entries:
        if label in seen:
            continue
        seen.add(label)
        unique_labels.append(label)

    blocks: dict[str, Block] = {}
    for label in unique_labels:
        block = block_for_label(lines, labels, label)
        if block is not None:
            blocks[label] = block

    relocations: list[tuple[str, str, Block]] = []
    referenced_relocated_labels: set[str] = set()
    for label in unique_labels:
        block = blocks.get(label)
        if block is None:
            continue

        already = is_already_relocated_stub(block)
        if already is not None:
            referenced_relocated_labels.add(already)
            continue

        if not is_relocatable_text_block(block):
            continue

        if text_payload_char_count(block) < min_chars:
            continue

        relocated_label = f"RelocatedText_{label}"
        relocations.append((label, relocated_label, block))

    if not relocations:
        return False, [], referenced_relocated_labels, 0

    new_lines = lines[:]
    for label, relocated_label, block in sorted(relocations, key=lambda x: x[2].start, reverse=True):
        stub = make_stub(label, relocated_label)
        new_lines[block.start:block.end] = stub

    updated = "\n".join(new_lines) + "\n"
    changed = updated != original
    if changed and apply:
        path.write_text(updated, encoding="utf-8")

    relocated_blocks = []
    for _, relocated_label, block in relocations:
        relocated_blocks.append((relocated_label, block.lines))

    return changed, relocated_blocks, referenced_relocated_labels, len(relocations)


def build_relocation_file(relocated_blocks: list[tuple[str, list[str]]]) -> str:
    lines = [
        '; Auto-generated by tools/relocate_text.py.',
        '; Do not edit by hand; re-run the tool.',
        "",
    ]
    for relocated_label, original_block in relocated_blocks:
        lines.append(f"{relocated_label}:")
        lines.extend(original_block[1:])
        if lines[-1] != "":
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def parse_relocation_file(path: Path) -> dict[str, list[str]]:
    if not path.exists():
        return {}

    lines = path.read_text(encoding="utf-8").splitlines()
    labels = find_global_labels(lines)
    blocks: dict[str, list[str]] = {}
    for label, start in sorted(labels.items(), key=lambda x: x[1]):
        if not label.startswith("RelocatedText_"):
            continue
        block = block_for_label(lines, labels, label)
        if block is not None:
            blocks[label] = block.lines
    return blocks


def write_relocation_file(path: Path, content: str, apply: bool) -> bool:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    changed = existing != content
    if apply and changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Relocate eligible map text blocks into a generated overflow file and "
            "replace original labels with bank-switching text stubs."
        )
    )
    parser.add_argument("--apply", action="store_true", help="Write changes to files")
    parser.add_argument(
        "--scripts-dir",
        default="scripts",
        help="Directory containing map script asm files (default: scripts)",
    )
    parser.add_argument(
        "--relocation-file",
        default="scripts/text_relocations.asm",
        help="Generated relocation text file path (default: scripts/text_relocations.asm)",
    )
    parser.add_argument(
        "--min-chars",
        type=int,
        default=60,
        help="Minimum quoted character count to relocate a text block (default: 60)",
    )
    args = parser.parse_args()

    scripts_dir = Path(args.scripts_dir)
    relocation_file = Path(args.relocation_file)

    files = sorted(scripts_dir.glob("*.asm"))
    changed_files = 0
    total_relocated = 0
    relocated_blocks: list[tuple[str, list[str]]] = []
    referenced_relocated_labels: set[str] = set()
    existing_blocks = parse_relocation_file(relocation_file)

    for file in files:
        changed, blocks, referenced_labels, relocated_count = process_script(
            file, min_chars=args.min_chars, apply=args.apply
        )
        changed_files += int(changed)
        total_relocated += relocated_count
        relocated_blocks.extend(blocks)
        referenced_relocated_labels.update(referenced_labels)
        if changed:
            action = "updated" if args.apply else "would update"
            print(f"{action} {file} ({relocated_count} relocations)")

    merged_blocks: list[tuple[str, list[str]]] = []
    for label in sorted(referenced_relocated_labels):
        existing = existing_blocks.get(label)
        if existing is None:
            raise SystemExit(
                f"error: missing relocated block definition for {label} in {relocation_file}"
            )
        merged_blocks.append((label, existing))

    new_labels = {label for label, _ in merged_blocks}
    for label, block in relocated_blocks:
        if label in new_labels:
            continue
        merged_blocks.append((label, block))
        new_labels.add(label)

    relocation_content = build_relocation_file(merged_blocks)
    relocation_changed = write_relocation_file(
        relocation_file, relocation_content, apply=args.apply
    )
    if relocation_changed:
        action = "updated" if args.apply else "would update"
        print(f"{action} {relocation_file}")

    mode = "applied" if args.apply else "dry-run"
    print(
        f"{mode}: scanned {len(files)} files, "
        f"updated={changed_files}, relocated={total_relocated}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
