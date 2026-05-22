# Architecture

Nature Agent is organized as a scientific workflow pack rather than a monolithic tool. The core skill defines the routing logic, while the agent role definitions document the specialist behavior expected in each phase.

## Layers

```text
User request
  -> skills/SKILL.md
  -> nature-team-lead role
  -> specialist agent role definitions
  -> quality-editor gate
  -> final deliverable
```

## Components

- `skills/SKILL.md`: workflow router and operational SOP.
- `agents/*.md`: reusable role definitions for specialist research tasks.
- `rules/nature-agent_rules.md`: trigger guidance and safety constraints.
- `scripts/*.py`: validation and optional helper scripts.
- `assets/screenshot-roadmap.png`: technical roadmap shown on the project page.

## Design Principles

- Keep scientific claims traceable to source materials or verified references.
- Route specialist work to the matching role.
- Require a quality review gate for important deliverables.
- Make dependency gaps explicit instead of pretending external tools or skills were used.
