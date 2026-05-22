from __future__ import annotations

import argparse
import pathlib
import shutil

SKILLS = [
    "literature-review",
    "hypothesis-generation",
    "scientific-critical-thinking",
    "peer-review",
    "statistical-analysis",
    "scientific-visualization",
    "scientific-writing",
]


def copy_skill(source_root: pathlib.Path, target_root: pathlib.Path, skill_name: str, force: bool) -> None:
    source = source_root / skill_name
    target = target_root / skill_name
    if not source.exists():
        raise FileNotFoundError(f"missing source skill: {source}")
    if target.exists():
        if not force:
            raise FileExistsError(f"target already exists: {target}; pass --force to overwrite")
        shutil.rmtree(target)
    target_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install selected scientific-thinking skills into a target skills directory."
    )
    parser.add_argument(
        "--source",
        type=pathlib.Path,
        required=True,
        help="Source directory that contains scientific-thinking skill folders.",
    )
    parser.add_argument(
        "--target",
        type=pathlib.Path,
        required=True,
        help="Target skills directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing target skill directories.",
    )
    args = parser.parse_args()

    source_root = args.source.expanduser().resolve()
    target_root = args.target.expanduser().resolve()

    for skill_name in SKILLS:
        copy_skill(source_root, target_root, skill_name, args.force)
        print(f"installed {skill_name} -> {target_root / skill_name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
