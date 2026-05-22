from __future__ import annotations

import json
import pathlib
from typing import Iterable, List

BASE = pathlib.Path(__file__).resolve().parents[1]
PLUGIN = BASE / ".codex-plugin" / "plugin.json"
LEGACY_PLUGIN = BASE / "legacy" / "codebuddy-plugin.json"
RULES = BASE / "rules" / "nature-agent_rules.md"
SKILL = BASE / "skills" / "nature-analysis" / "SKILL.md"
README = BASE / "README.md"

REQUIRED_AGENTS = [
    "nature-team-lead",
    "paper-reader",
    "literature-searcher",
    "citation-manager",
    "manuscript-writer",
    "language-polisher",
    "figure-designer",
    "data-availability-checker",
    "reviewer-response-writer",
    "ppt-builder",
    "quality-editor",
]

REQUIRED_MARKERS = [
    "[PAPER_READING_REPORT]",
    "[LITERATURE_SEARCH_REPORT]",
    "[CITATION_MANAGEMENT_REPORT]",
    "[MANUSCRIPT_DRAFT]",
    "[LANGUAGE_POLISHING_DRAFT]",
    "[SCIENTIFIC_FIGURE_PLAN]",
    "[DATA_AVAILABILITY_REPORT]",
    "[REVIEWER_RESPONSE_DRAFT]",
    "[PAPER_PRESENTATION_PPT]",
    "[SCIENTIFIC_EDITOR_DECISION]",
]


def load_json(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check_paths(paths: Iterable[pathlib.Path]) -> List[str]:
    errors: List[str] = []
    for path in paths:
        if not path.exists():
            errors.append(f"missing required path: {path.relative_to(BASE)}")
    return errors


def check_plugin_manifest(plugin: dict) -> List[str]:
    errors: List[str] = []
    if plugin.get("name") != "nature-agent":
        errors.append("plugin name must be nature-agent")
    if plugin.get("license") != "MIT":
        errors.append("plugin license must be MIT")
    if plugin.get("skills") != "./skills/":
        errors.append("plugin skills path must be ./skills/")
    if "interface" not in plugin:
        errors.append("plugin manifest missing interface block")
    for field in ["homepage", "repository", "description", "author"]:
        if field not in plugin:
            errors.append(f"plugin manifest missing {field}")

    interface = plugin.get("interface", {})
    for field in ["displayName", "shortDescription", "longDescription", "category"]:
        if field not in interface:
            errors.append(f"plugin interface missing {field}")
    for rel in [interface.get("logo"), *(interface.get("screenshots", []) or [])]:
        if rel and not (BASE / rel).exists():
            errors.append(f"plugin asset path does not exist: {rel}")
    return errors


def check_agent_files() -> List[str]:
    errors: List[str] = []
    for agent_id in REQUIRED_AGENTS:
        path = BASE / "agents" / f"{agent_id}.md"
        if not path.exists():
            errors.append(f"missing agent file: agents/{agent_id}.md")
            continue
        text = path.read_text(encoding="utf-8")
        if "name:" not in text:
            errors.append(f"missing frontmatter name: agents/{agent_id}.md")
        if "description:" not in text:
            errors.append(f"missing frontmatter description: agents/{agent_id}.md")
    return errors


def check_docs() -> List[str]:
    errors: List[str] = []
    rules = RULES.read_text(encoding="utf-8")
    skill = SKILL.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")

    if "alwaysApply: false" not in rules:
        errors.append("rules should use alwaysApply: false for narrower trigger")

    required_skill_phrases = [
        "Workflow A",
        "Workflow B",
        "Workflow C",
        "Workflow D",
        "Workflow E",
        "Failure Recovery",
        "scientific-thinking",
        "quality-editor",
        "paper-reader",
        "literature-searcher",
    ]
    for phrase in required_skill_phrases:
        if phrase not in skill:
            errors.append(f"SKILL.md missing required concept: {phrase}")

    required_readme_phrases = [
        ".codex-plugin/plugin.json",
        "Legacy Compatibility",
        "Validation Checklist",
        "MIT",
    ]
    for phrase in required_readme_phrases:
        if phrase not in readme:
            errors.append(f"README missing required concept: {phrase}")

    combined = "\n".join([rules, skill, readme])
    for marker in REQUIRED_MARKERS:
        if marker not in combined:
            errors.append(f"missing required output marker: {marker}")
    return errors


def check_text_is_ascii() -> List[str]:
    errors: List[str] = []
    for path in BASE.rglob("*"):
        if path.is_dir() or path.suffix.lower() not in {".md", ".json", ".py", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8")
        if any(ord(ch) > 127 for ch in text):
            errors.append(f"non-ASCII text remains in {path.relative_to(BASE)}")
    return errors


def main() -> int:
    errors: List[str] = []
    errors.extend(
        check_paths(
            [
                PLUGIN,
                LEGACY_PLUGIN,
                RULES,
                SKILL,
                README,
                BASE / "LICENSE",
                BASE / ".gitignore",
            ]
        )
    )

    if PLUGIN.exists():
        errors.extend(check_plugin_manifest(load_json(PLUGIN)))
    if LEGACY_PLUGIN.exists():
        load_json(LEGACY_PLUGIN)

    errors.extend(check_agent_files())
    if RULES.exists() and SKILL.exists() and README.exists():
        errors.extend(check_docs())
    errors.extend(check_text_is_ascii())

    if errors:
        print("nature-agent validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("nature-agent validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
