# Spec-driven documentation alignment

## Contents

1. Purpose
2. Detect the project's framework
3. Artifact dependency model
4. Change-impact decision
5. Brownfield drift workflow
6. Traceability
7. Quality gates
8. Prohibited shortcuts

## 1. Purpose

Use this guide to keep specifications, plans, tasks, implementation, tests, and
documentation aligned. Specifications express intended outcomes. Implementation
shows current behavior. Neither should silently overwrite the other.

## 2. Detect the project's framework

Search project instructions and common locations, including:

- `.specify/`, `specs/`, and `memory/constitution.md`
- `openspec/` or project-specific OpenSpec locations
- `.kiro/specs/`
- `requirements/`, `features/`, `docs/specs/`, RFCs, or design documents
- issue templates, task definitions, BDD features, or acceptance-test conventions

Read the framework's local instructions and templates. Preserve its filenames,
identifiers, statuses, phase order, and vocabulary. Do not install, migrate, or
normalize a framework unless requested.

If no framework exists, use the generic model below only when the task is complex
enough to benefit from durable specifications. A minor internal refactor does not
need a new specification system.

## 3. Artifact dependency model

The generic dependency order is:

1. governing principles or constitution
2. specification of what and why
3. clarification of material ambiguity
4. technical plan for how
5. contracts, data changes, and architecture decisions
6. small, independently verifiable tasks
7. implementation and tests
8. analysis and convergence against the specification
9. developer, operator, API, release, and user documentation

For GitHub Spec Kit, respect the repository's adopted sequence. Current official
guidance may include constitution, specify, clarify, plan, checklist, tasks,
analyze, implement, and converge. Do not invent absent commands or regenerate
artifacts blindly.

## 4. Change-impact decision

Update the specification when a change alters:

- user scenario, workflow, permission, rule, outcome, or error behavior
- functional requirement, non-functional target, acceptance criterion, or scope
- compliance, privacy, security, retention, or accessibility intent
- public API, event, CLI, file format, or integration behavior

Update the technical plan or design when a change alters:

- component boundaries or dependencies
- storage, migrations, data lifecycle, or consistency model
- infrastructure, deployment topology, availability, or recovery
- important technology choice or constraint
- security boundary, authentication, authorization, or secrets handling

Update tasks when work sequencing, completion status, or verification changes.
Update downstream documentation whenever its reader-visible facts change.

Do not update normative intent for:

- formatting-only edits
- implementation refactors that preserve every relevant contract
- generated-file changes with no source change

Record that no documentation change is required when review policy expects an
explicit impact decision.

## 5. Brownfield drift workflow

When implementation and specifications differ:

1. freeze assumptions and avoid editing the normative spec
2. identify the exact requirement, plan section, task, test, and code paths
3. describe the observed behavior and expected behavior separately
4. determine whether the difference is an accepted change, defect, stale spec, or
   unresolved decision
5. ask the product or technical authority when evidence is insufficient
6. update the authoritative artifact first
7. propagate the decision through dependent artifacts
8. verify code and tests against the resolved intent

Use a compact drift table:

| Item | Intended evidence | Observed evidence | Impact | Decision needed |
| --- | --- | --- | --- | --- |
| Identifier or behavior | Spec path and section | Test, code, or runtime path | User or technical effect | Concrete question |

## 6. Traceability

Reuse existing identifiers. Never renumber stable requirements simply to improve
appearance.

When the project has no convention and traceability is valuable, use:

- `FR-###` for functional requirements
- `NFR-###` for non-functional requirements
- `AC-###` for acceptance criteria
- existing issue or task IDs for implementation work

Trace only relationships that help review or maintenance:

```text
Requirement -> acceptance criterion -> plan or contract -> task -> test -> release
```

A small feature can use links or a table. Avoid a large matrix that no one will
maintain.

## 7. Quality gates

Before declaring alignment:

- every in-scope scenario has observable acceptance criteria
- exclusions and edge cases are explicit
- non-functional requirements are measurable or transparently qualitative
- the technical plan respects constraints and governing principles
- tasks cover the plan without mixing unrelated changes
- tests or other verification map to the important acceptance criteria
- current implementation has no unexplained drift
- user, API, operational, and release documentation reflect the resolved outcome

Pause for clarification when ambiguity can change architecture, data handling,
security, cost, or user-visible behavior.

## 8. Prohibited shortcuts

Never:

- infer desired requirements solely from existing code
- change a specification to make a failing implementation appear compliant
- mark tasks complete based only on file existence
- use tests as proof that all business intent is represented
- overwrite an accepted ADR instead of superseding it
- create duplicate sources of truth for an API or schema
- add fictional metrics, targets, owners, dates, or approvals
