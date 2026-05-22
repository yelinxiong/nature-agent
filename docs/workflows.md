# Workflows

Nature Agent defines five primary workflows. Each workflow is intentionally explicit so it can be audited, adapted, or run manually by another agent system.

## Workflow A: Paper Reading

```text
paper-reader -> optional literature-searcher -> quality-editor -> final report
```

Use for paper deep reading, bilingual Markdown reports, figure-by-figure grounding, and journal club preparation.

## Workflow B: Manuscript Writing

```text
literature-searcher + citation-manager + data-availability-checker -> manuscript-writer -> language-polisher -> quality-editor -> final text
```

Use for abstracts, introductions, results, discussions, methods, cover letters, and manuscript restructuring.

## Workflow C: Scientific Figure

```text
figure-designer -> quality-editor -> figure-designer -> final figure plan/code/assets
```

Use for multi-panel scientific figures, figure legends, plotting plans, and graphical abstract structures.

## Workflow D: Reviewer Response

```text
reviewer-response-writer -> citation-manager + manuscript-writer -> quality-editor -> final response letter
```

Use for reviewer comment maps, action tables, rebuttal letters, and revision checklists.

## Workflow E: Paper to PPT

```text
paper-reader -> quality-editor -> ppt-builder -> final PPT or slide outline
```

Use for journal club, lab meeting, thesis seminar, and paper-sharing presentations.

## Quality Gate

Important deliverables should pass through `quality-editor`, which returns `PASS`, `REVISE`, or `RETURN` and highlights evidence, citation, figure, data, and author-input risks.
