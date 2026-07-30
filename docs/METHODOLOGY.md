# Methodology and sources

## Purpose

The framework combines software-documentation coverage with modern technical
writing, docs-as-code, evidence handling, and spec-driven alignment.

## Source foundation

### Google Technical Writing

[Organizing large documents](https://developers.google.com/tech-writing/two/large-docs)
contributes:

- outline-first organization
- introductions that define audience, prerequisites, coverage, and exclusions
- task-oriented headings
- clear navigation
- progressive disclosure

### Write the Docs

The [Software Documentation Guide](https://www.writethedocs.org/guide/) and
[Docs as Code](https://www.writethedocs.org/guide/docs-as-code/) contribute:

- documentation in version control
- review and automation in the engineering workflow
- content close to the code it describes
- shared ownership
- consistency, accessibility, findability, and maintenance

### Docs for Developers

The public description and chapter structure of
[*Docs for Developers: An Engineer's Field Guide to Technical Writing*](https://link.springer.com/book/10.1007/979-8-8688-2509-5)
contribute the lifecycle:

1. understand the audience
2. plan
3. draft
4. edit
5. integrate code samples and visuals
6. publish
7. collect feedback
8. measure quality
9. organize
10. maintain

The complete book text is not included or reproduced.

### GitHub Spec Kit

[GitHub Spec Kit](https://github.github.com/spec-kit/) contributes the explicit
relationship among specification, technical plan, tasks, implementation, and
quality gates. The framework uses this as one supported convention, not a mandatory
dependency.

### OpenAI agent skills

[OpenAI guidance for building skills](https://learn.chatgpt.com/docs/build-skills)
contributes:

- a focused `SKILL.md` workflow
- progressive disclosure through references and assets
- deterministic scripts only where needed
- explicit and implicit skill activation
- repository and user skill scopes

### Legacy documentation templates

Legacy academic and sprint-oriented templates reviewed during design contributed
coverage for:

- problem, purpose, scope, stakeholders, and business rules
- functional and non-functional requirements
- scenarios, screens, architecture, components, and interactions
- data models, integrations, testing, deployment, and user guidance
- explicit impact and out-of-scope analysis

Those source files are not redistributed.

## Common synthesis

The sources converge on ten operating principles:

1. Start with the reader and task.
2. Define scope and exclusions.
3. Plan information architecture before drafting.
4. Treat documentation as part of product and engineering work.
5. Keep documentation versioned and reviewable.
6. Organize for findability and progressive disclosure.
7. Use examples and visuals when they materially help.
8. Separate intent, procedures, explanation, reference, and operations.
9. Test accuracy, usability, accessibility, and drift.
10. Maintain through ownership, change triggers, feedback, and metrics.

## Evidence policy

The framework adds an explicit evidence model:

| Class | Treatment |
| --- | --- |
| Confirmed | State as fact |
| Inferred | Label and verify before making normative |
| Conflicted | Report the disagreement and request a decision |
| Unknown | Ask, omit, or use an approved confirmation marker |

Implementation proves current mechanics, not necessarily desired product intent.
Specifications express intent, not proof of implementation. Alignment requires
reviewing both.

## Copyright boundary

This repository contains original synthesis and templates. It does not contain the
reviewed PDFs, ebook files, book chapters, or extensive quotations. Source links
are provided so readers can consult the public materials directly.
