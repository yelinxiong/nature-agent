# Nature Agent

Nature Agent is a Codex-compatible multi-agent workflow pack for scientific research writing. It provides a reusable research team for paper reading, evidence mapping, citation management, manuscript drafting, language polishing, figure planning, data availability checks, reviewer responses, and paper-to-PPT workflows.

The project is designed as a public GitHub repository that can be adapted for Codex plugin workflows while keeping the individual agent role definitions readable and reusable.

## What It Does

- Deep paper reading and structured Markdown reports
- Literature search planning and evidence mapping
- Claim-level citation management
- Nature-style manuscript drafting and restructuring
- Scientific English polishing with overclaim control
- Scientific figure and multi-panel layout planning
- Data Availability and FAIR metadata checks
- Point-by-point reviewer response drafting
- Journal club, lab meeting, and paper-to-PPT planning
- Scientific quality review before final delivery

## Repository Layout

```text
nature-agent/
|-- .codex-plugin/plugin.json
|-- agents/
|-- assets/
|-- avatars/
|-- docs/
|-- legacy/
|-- rules/
|-- scripts/
|-- skills/nature-analysis/SKILL.md
|-- LICENSE
`-- README.md
```

## Main Entry Points

- `.codex-plugin/plugin.json`: Codex-compatible plugin manifest.
- `skills/nature-analysis/SKILL.md`: main orchestration skill and workflow SOP.
- `agents/nature-team-lead.md`: team lead role and collaboration rules.
- `agents/*.md`: specialist role definitions.
- `rules/nature-agent_rules.md`: trigger guidance and safety reminders.
- `scripts/validate_nature_agent.py`: repository structure and content validation.
- `legacy/codebuddy-plugin.json`: legacy WorkBuddy/CodeBuddy-style manifest kept for reference only.

## Team Roles

| Agent | Purpose |
|---|---|
| `nature-team-lead` | Workflow coordinator and final compiler |
| `paper-reader` | Paper deep reading and figure grounding |
| `literature-searcher` | Literature search planning and evidence maps |
| `citation-manager` | Claim-level citation matching and formatting |
| `manuscript-writer` | Manuscript section drafting and restructuring |
| `language-polisher` | Nature-style scientific English polishing |
| `figure-designer` | Scientific figure planning and plotting guidance |
| `data-availability-checker` | Data Availability and FAIR checks |
| `reviewer-response-writer` | Reviewer comment maps and response letters |
| `ppt-builder` | Paper-to-PPT and journal club slide planning |
| `quality-editor` | Scientific quality gate and editorial decision |

## Workflows

### Workflow A: Paper Reading

```text
paper-reader -> optional literature-searcher -> quality-editor -> final report
```

### Workflow B: Manuscript Writing

```text
literature-searcher + citation-manager + data-availability-checker -> manuscript-writer -> language-polisher -> quality-editor -> final text
```

### Workflow C: Scientific Figure

```text
figure-designer -> quality-editor -> figure-designer -> final figure plan/code/assets
```

### Workflow D: Reviewer Response

```text
reviewer-response-writer -> citation-manager + manuscript-writer -> quality-editor -> final response letter
```

### Workflow E: Paper to PPT

```text
paper-reader -> quality-editor -> ppt-builder -> final PPT or slide outline
```

## Required Output Markers

- `[PAPER_READING_REPORT]`
- `[LITERATURE_SEARCH_REPORT]`
- `[CITATION_MANAGEMENT_REPORT]`
- `[MANUSCRIPT_DRAFT]`
- `[LANGUAGE_POLISHING_DRAFT]`
- `[SCIENTIFIC_FIGURE_PLAN]`
- `[DATA_AVAILABILITY_REPORT]`
- `[REVIEWER_RESPONSE_DRAFT]`
- `[PAPER_PRESENTATION_PPT]`
- `[SCIENTIFIC_EDITOR_DECISION]`

## Installation

Clone the repository:

```bash
git clone https://github.com/yelinxiong/nature-agent.git
cd nature-agent
```

Validate the structure:

```bash
python scripts/validate_nature_agent.py
```

If you use Codex plugin marketplaces, point your marketplace entry at this repository or local checkout and use `.codex-plugin/plugin.json` as the manifest.

## Optional Scientific Thinking Skills

This repository can coordinate with external scientific-thinking skills when they are installed. The helper script can copy a selected scientific-thinking skills directory into a target skills directory:

```bash
python scripts/install_nature_skills.py --source /path/to/scientific-thinking --target /path/to/skills
```

The script does not assume local machine paths. Both `--source` and `--target` should be provided explicitly for reproducible installs.

## Legacy Compatibility

The previous CodeBuddy/WorkBuddy-style manifest has been moved to:

```text
legacy/codebuddy-plugin.json
```

It is retained for reference and migration only. The canonical public manifest is:

```text
.codex-plugin/plugin.json
```

## Validation Checklist

- `.codex-plugin/plugin.json` is valid JSON.
- The plugin manifest includes public repository metadata.
- `skills/nature-analysis/SKILL.md` defines explicit workflows and failure recovery.
- All agent files include `name` and `description` frontmatter.
- Required output markers are present across the workflow docs.
- Text files are ASCII-only unless intentionally changed.
- No local absolute paths are required for validation.

## Safety Rules

- Do not fabricate data, experiments, citations, DOI, PMID, arXiv IDs, line numbers, figures, or reviewer comments.
- Ask for missing source materials before producing final scientific content.
- Prefer primary sources and verified metadata for literature or citation work.
- Important deliverables should pass through `quality-editor` before final response.

## License

MIT. See [LICENSE](LICENSE).
