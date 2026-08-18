#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

LABEL_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*::?\s*(?:;.*)?$")
AUDIO_ENG_CHANNEL_RE = re.compile(
    r"^\s*audio_eng_channel\s+([A-Za-z_][A-Za-z0-9_]*)\s*,\s*([0-9]+)\s*(?:;.*)?$"
)

MUSIC1_FILES = [
    "audio/music/pkmn_healed.asm",
    "audio/music/routes_1.asm",
    "audio/music/routes_2.asm",
    "audio/music/routes_3.asm",
    "audio/music/routes_4.asm",
    "audio/music/indigo_plateau.asm",
    "audio/music/pallet_town.asm",
    "audio/music/unused_song.asm",
    "audio/music/cities_1.asm",
    "audio/music/museum_guy.asm",
    "audio/music/meet_prof_oak.asm",
    "audio/music/meet_rival.asm",
    "audio/music/ss_anne.asm",
    "audio/music/cities_2.asm",
    "audio/music/celadon.asm",
    "audio/music/cinnabar.asm",
    "audio/music/vermilion.asm",
    "audio/music/lavender.asm",
    "audio/music/safari_zone.asm",
    "audio/music/gym.asm",
    "audio/music/pokecenter.asm",
]

MUSIC3_FILES = [
    "audio/music/bike_riding.asm",
    "audio/music/dungeon_1.asm",
    "audio/music/game_corner.asm",
    "audio/music/title_screen.asm",
    "audio/music/dungeon_2.asm",
    "audio/music/dungeon_3.asm",
    "audio/music/cinnabar_mansion.asm",
    "audio/music/oaks_lab.asm",
    "audio/music/pokemon_tower.asm",
    "audio/music/silph_co.asm",
    "audio/music/meet_evil_trainer.asm",
    "audio/music/meet_female_trainer.asm",
    "audio/music/meet_male_trainer.asm",
    "audio/music/intro_battle.asm",
    "audio/music/surfing.asm",
    "audio/music/jigglypuff_song.asm",
    "audio/music/hall_of_fame.asm",
]

AUDIO3_FILES = [
    "audio/music/credits.asm",
]

MUSIC2_FILES = [
    "audio/music/gym_leader_battle.asm",
    "audio/music/trainer_battle.asm",
    "audio/music/wild_battle.asm",
    "audio/music/final_battle.asm",
    "audio/music/defeated_trainer.asm",
    "audio/music/defeated_wild_mon.asm",
    "audio/music/defeated_gym_leader.asm",
]

SFX2_FILES = [
    "audio/sfx/press_ab.asm",
    "audio/sfx/start_menu.asm",
    "audio/sfx/tink.asm",
    "audio/sfx/heal_hp.asm",
    "audio/sfx/heal_ailment.asm",
    "audio/sfx/trainer_appeared.asm",
    "audio/sfx/ball_toss.asm",
    "audio/sfx/ball_poof.asm",
    "audio/sfx/faint_thud.asm",
    "audio/sfx/run.asm",
    "audio/sfx/dex_page_added.asm",
    "audio/sfx/pokeflute_ch7.asm",
    "audio/sfx/peck.asm",
    "audio/sfx/faint_fall.asm",
    "audio/sfx/battle_09.asm",
    "audio/sfx/pound.asm",
    "audio/sfx/battle_0b.asm",
    "audio/sfx/battle_0c.asm",
    "audio/sfx/battle_0d.asm",
    "audio/sfx/battle_0e.asm",
    "audio/sfx/battle_0f.asm",
    "audio/sfx/damage.asm",
    "audio/sfx/not_very_effective.asm",
    "audio/sfx/battle_12.asm",
    "audio/sfx/battle_13.asm",
    "audio/sfx/battle_14.asm",
    "audio/sfx/vine_whip.asm",
    "audio/sfx/battle_16.asm",
    "audio/sfx/battle_17.asm",
    "audio/sfx/battle_18.asm",
    "audio/sfx/battle_19.asm",
    "audio/sfx/super_effective.asm",
    "audio/sfx/battle_1b.asm",
    "audio/sfx/battle_1c.asm",
    "audio/sfx/doubleslap.asm",
    "audio/sfx/battle_1e.asm",
    "audio/sfx/horn_drill.asm",
    "audio/sfx/battle_20.asm",
    "audio/sfx/battle_21.asm",
    "audio/sfx/battle_22.asm",
    "audio/sfx/battle_23.asm",
    "audio/sfx/battle_24.asm",
    "audio/sfx/battle_25.asm",
    "audio/sfx/battle_26.asm",
    "audio/sfx/battle_27.asm",
    "audio/sfx/battle_28.asm",
    "audio/sfx/battle_29.asm",
    "audio/sfx/battle_2a.asm",
    "audio/sfx/battle_2b.asm",
    "audio/sfx/battle_2c.asm",
    "audio/sfx/psybeam.asm",
    "audio/sfx/battle_2e.asm",
    "audio/sfx/battle_2f.asm",
    "audio/sfx/psychic_m.asm",
    "audio/sfx/battle_31.asm",
    "audio/sfx/battle_32.asm",
    "audio/sfx/battle_33.asm",
    "audio/sfx/battle_34.asm",
    "audio/sfx/battle_35.asm",
    "audio/sfx/battle_36.asm",
]

SFX3_FILES = [
    "audio/sfx/start_menu.asm",
    "audio/sfx/cut.asm",
    "audio/sfx/go_inside.asm",
    "audio/sfx/swap.asm",
    "audio/sfx/tink.asm",
    "audio/sfx/59.asm",
    "audio/sfx/purchase.asm",
    "audio/sfx/collision.asm",
    "audio/sfx/go_outside.asm",
    "audio/sfx/press_ab.asm",
    "audio/sfx/save.asm",
    "audio/sfx/heal_hp.asm",
    "audio/sfx/poisoned.asm",
    "audio/sfx/heal_ailment.asm",
    "audio/sfx/trade_machine.asm",
    "audio/sfx/turn_on_pc.asm",
    "audio/sfx/turn_off_pc.asm",
    "audio/sfx/enter_pc.asm",
    "audio/sfx/shrink.asm",
    "audio/sfx/switch.asm",
    "audio/sfx/healing_machine.asm",
    "audio/sfx/teleport_exit1.asm",
    "audio/sfx/teleport_enter1.asm",
    "audio/sfx/teleport_exit2.asm",
    "audio/sfx/ledge.asm",
    "audio/sfx/teleport_enter2.asm",
    "audio/sfx/fly.asm",
    "audio/sfx/denied.asm",
    "audio/sfx/arrow_tiles.asm",
    "audio/sfx/push_boulder.asm",
    "audio/sfx/ss_anne_horn.asm",
    "audio/sfx/withdraw_deposit.asm",
    "audio/sfx/intro_lunge.asm",
    "audio/sfx/intro_hip.asm",
    "audio/sfx/intro_hop.asm",
    "audio/sfx/intro_raise.asm",
    "audio/sfx/intro_crash.asm",
    "audio/sfx/intro_whoosh.asm",
    "audio/sfx/slots_stop_wheel.asm",
    "audio/sfx/slots_reward.asm",
    "audio/sfx/slots_new_spin.asm",
    "audio/sfx/shooting_star.asm",
]

SFX1_FILES = [
    "audio/sfx/start_menu.asm",
    "audio/sfx/pokeflute.asm",
    "audio/sfx/cut.asm",
    "audio/sfx/go_inside.asm",
    "audio/sfx/swap.asm",
    "audio/sfx/tink.asm",
    "audio/sfx/59.asm",
    "audio/sfx/purchase.asm",
    "audio/sfx/collision.asm",
    "audio/sfx/go_outside.asm",
    "audio/sfx/press_ab.asm",
    "audio/sfx/save.asm",
    "audio/sfx/heal_hp.asm",
    "audio/sfx/poisoned.asm",
    "audio/sfx/heal_ailment.asm",
    "audio/sfx/trade_machine.asm",
    "audio/sfx/turn_on_pc.asm",
    "audio/sfx/turn_off_pc.asm",
    "audio/sfx/enter_pc.asm",
    "audio/sfx/shrink.asm",
    "audio/sfx/switch.asm",
    "audio/sfx/healing_machine.asm",
    "audio/sfx/teleport_exit1.asm",
    "audio/sfx/teleport_enter1.asm",
    "audio/sfx/teleport_exit2.asm",
    "audio/sfx/ledge.asm",
    "audio/sfx/teleport_enter2.asm",
    "audio/sfx/fly.asm",
    "audio/sfx/denied.asm",
    "audio/sfx/arrow_tiles.asm",
    "audio/sfx/push_boulder.asm",
    "audio/sfx/ss_anne_horn.asm",
    "audio/sfx/withdraw_deposit.asm",
    "audio/sfx/safari_zone_pa.asm",
]

MUSIC1_SFX_FILES = [
    "audio/sfx/get_item1.asm",
    "audio/sfx/pokedex_rating.asm",
    "audio/sfx/get_item2.asm",
    "audio/sfx/get_key_item.asm",
]

MUSIC2_SFX_FILES = [
    "audio/sfx/pokeflute_ch5_ch6.asm",
    "audio/sfx/unused_fanfare.asm",
    "audio/sfx/level_up.asm",
    "audio/sfx/get_item2.asm",
    "audio/sfx/caught_mon.asm",
]

MUSIC3_SFX_FILES = [
    "audio/sfx/get_item1.asm",
    "audio/sfx/pokedex_rating.asm",
    "audio/sfx/get_item2.asm",
    "audio/sfx/get_key_item.asm",
]

OUT_DIR = Path("audio/headroom")


def labels_and_channels_from_file(path: Path) -> tuple[list[str], list[tuple[str, int]]]:
    text = path.read_text(encoding="utf-8")
    labels: list[str] = []
    channels: list[tuple[str, int]] = []
    for line in text.splitlines():
        cm = AUDIO_ENG_CHANNEL_RE.match(line)
        if cm:
            channels.append((cm.group(1), int(cm.group(2))))
            continue
        m = LABEL_RE.match(line)
        if not m:
            continue
        label = m.group(1)
        if label.startswith("."):
            continue
        labels.append(label)
    return labels, channels


def write_stub(out_path: Path, source_files: list[str]) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        "; Auto-generated by tools/generate_audio_headroom_stubs.py",
        "; Emits silent stubs that preserve global labels/pointers.",
        "",
    ]
    seen_labels: set[str] = set()
    seen_channels: set[tuple[str, int]] = set()
    for rel in source_files:
        labels, channels = labels_and_channels_from_file(Path(rel))
        if not labels and not channels:
            continue
        lines.append(f"; from {rel}")
        for label in labels:
            if label in seen_labels:
                continue
            seen_labels.add(label)
            lines.append(f"{label}::")
            lines.append("\tsound_ret")
        for base, channel in channels:
            key = (base, channel)
            if key in seen_channels:
                continue
            seen_channels.add(key)
            lines.append(f"\taudio_eng_channel {base}, {channel}")
            lines.append("\tsound_ret")
        lines.append("")
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def cry_files() -> list[str]:
    files = sorted(Path("audio/sfx").glob("cry*.asm"))
    result = [str(path) for path in files]
    result.append("audio/sfx/unused_cry.asm")
    return result


def main() -> int:
    all_sfx1 = SFX1_FILES + cry_files()
    all_sfx2 = SFX2_FILES + cry_files()
    all_sfx3 = SFX3_FILES + cry_files()

    write_stub(OUT_DIR / "music1_stubs.asm", MUSIC1_FILES)
    write_stub(OUT_DIR / "music2_stubs.asm", MUSIC2_FILES)
    write_stub(OUT_DIR / "music3_stubs.asm", MUSIC3_FILES)
    write_stub(OUT_DIR / "audio3_stubs.asm", AUDIO3_FILES)
    write_stub(OUT_DIR / "sfx1_stubs.asm", all_sfx1)
    write_stub(OUT_DIR / "sfx2_stubs.asm", all_sfx2)
    write_stub(OUT_DIR / "sfx3_stubs.asm", all_sfx3)
    write_stub(OUT_DIR / "music1_sfx_stubs.asm", MUSIC1_SFX_FILES)
    write_stub(OUT_DIR / "music2_sfx_stubs.asm", MUSIC2_SFX_FILES)
    write_stub(OUT_DIR / "music3_sfx_stubs.asm", MUSIC3_SFX_FILES)
    print("wrote audio/headroom/music1_stubs.asm")
    print("wrote audio/headroom/music2_stubs.asm")
    print("wrote audio/headroom/music3_stubs.asm")
    print("wrote audio/headroom/audio3_stubs.asm")
    print("wrote audio/headroom/sfx1_stubs.asm")
    print("wrote audio/headroom/sfx2_stubs.asm")
    print("wrote audio/headroom/sfx3_stubs.asm")
    print("wrote audio/headroom/music1_sfx_stubs.asm")
    print("wrote audio/headroom/music2_sfx_stubs.asm")
    print("wrote audio/headroom/music3_sfx_stubs.asm")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
