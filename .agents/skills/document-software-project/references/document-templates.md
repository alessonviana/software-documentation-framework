# Adaptable documentation templates

Use templates as starting structures, not forms that must always be completed.
Copy only the documents supported by the project's evidence, audiences, and risk.
Remove unused headings rather than publishing empty sections.

## Template catalog

| Reader need | Template |
| --- | --- |
| Project entry point | `assets/templates/README.template.md` |
| Product purpose and boundaries | `assets/templates/PROJECT-OVERVIEW.template.md` |
| Feature requirements and acceptance | `assets/templates/FEATURE-SPEC.template.md` |
| System structure and quality attributes | `assets/templates/ARCHITECTURE.template.md` |
| Consequential technical decision | `assets/templates/ADR.template.md` |
| Contributor setup and workflow | `assets/templates/DEVELOPMENT.template.md` |
| Release, verification, and rollback | `assets/templates/DEPLOYMENT.template.md` |
| Operational diagnosis and recovery | `assets/templates/RUNBOOK.template.md` |
| Durable repository instructions for agents | `assets/templates/AGENTS.template.md` |

Resolve these paths relative to the skill directory.

## Selection rules

- Always use the existing project convention when one exists.
- Keep the root README as a concise entry point and navigation layer.
- Create a feature specification only when durable requirements add value.
- Create an ADR only for a decision with meaningful alternatives or consequences.
- Separate deployment procedures from incident runbooks.
- Keep agent instructions operational and link to durable documentation.
- Never add owners, dates, service targets, environments, or commands without
  evidence.
- Never retain angle-bracket placeholders in a finished document. Ask, omit the
  section, or use an approved confirmation marker.

## Adaptation checklist

Before saving a document:

1. Name its audience and task.
2. Confirm its authoritative sources.
3. Remove irrelevant headings.
4. Replace placeholders only with verified facts.
5. Link it from the README or existing documentation index.
6. Validate commands, paths, links, examples, and diagrams.
