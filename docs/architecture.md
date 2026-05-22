# Architecture

Nature Agent is organized as a scientific workflow pack rather than a monolithic tool. The agent role definitions document the specialist behavior expected in each phase.

## Layers

```text
User request
  -> agents/
  -> nature-team-lead role
  -> specialist agent role definitions
  -> quality-editor gate
  -> final deliverable
```

## Components

- `agents/*.md`: reusable role definitions for specialist research tasks.
- `docs/screenshot-roadmap.png`: technical roadmap shown on the project page.

## Design Principles

- Keep scientific claims traceable to source materials or verified references.
- Route specialist work to the matching role.
- Require a quality review gate for important deliverables.
- Make dependency gaps explicit instead of pretending external tools or skills were used.
