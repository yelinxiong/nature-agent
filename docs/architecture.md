# Architecture

Nature Agent is organized as a workflow pack rather than a monolithic tool. The Codex plugin manifest points to the skills directory, while the agent role definitions document the specialist behavior expected in each phase.

## Layers

```text
User request
  -> nature-analysis skill
  -> nature-team-lead role
  -> specialist agent role definitions
  -> quality-editor gate
  -> final deliverable
```

## Components

- `.codex-plugin/plugin.json`: public plugin metadata and UI-facing information.
- `skills/nature-analysis/SKILL.md`: workflow router and operational SOP.
- `agents/*.md`: reusable role definitions for specialist research tasks.
- `rules/nature-agent_rules.md`: trigger guidance and safety constraints.
- `scripts/*.py`: validation and optional helper scripts.
- `legacy/codebuddy-plugin.json`: previous WorkBuddy/CodeBuddy-style manifest retained for migration.

## Design Principles

- Keep scientific claims traceable to source materials or verified references.
- Route specialist work to the matching role.
- Require a quality review gate for important deliverables.
- Make dependency gaps explicit instead of pretending external tools or skills were used.
