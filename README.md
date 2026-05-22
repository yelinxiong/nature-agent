# Nature Agent

![Nature Agent technical roadmap](assets/screenshot-roadmap.png)

Nature Agent is a multi-agent workflow pack for scientific research writing. It provides a reusable research team for paper reading, evidence mapping, citation management, manuscript drafting, language polishing, figure planning, data availability checks, reviewer responses, and paper-to-PPT workflows.

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

## Optional Scientific Thinking Skills

This repository can coordinate with external scientific-thinking skills when they are installed. The helper script can copy a selected scientific-thinking skills directory into a target skills directory:

```bash
python scripts/install_nature_skills.py --source /path/to/scientific-thinking --target /path/to/skills
```

The script does not assume local machine paths. Both `--source` and `--target` should be provided explicitly for reproducible installs.

## License

MIT. See [LICENSE](LICENSE).
