---
name: document-software-project
description: Create, audit, reorganize, or update evidence-based documentation for software projects, SaaS products, websites, APIs, infrastructure, and AI-assisted codebases. Use when documenting a project from zero, improving an existing README or docs tree, reconciling documentation with code, preparing context for developers or AI agents, documenting architecture, setup, APIs, data, testing, deployment, operations, or decisions, and keeping spec-driven development artifacts aligned with implementation changes.
---

# Document Software Project

Produce documentation that helps a reader understand, use, change, and operate a
software project without inventing product intent or technical facts. Keep
documentation close to the code and compatible with the project's established
workflow.

## Non-negotiable rules

1. Treat explicit user statements and repository evidence as the basis for facts.
2. Distinguish current behavior, intended behavior, historical decisions,
   assumptions, and unknowns.
3. Never convert an inference into a fact. Use
   `[NEEDS CONFIRMATION: <specific question>]` only when a visible placeholder is
   useful and the user permits it. Otherwise ask before writing.
4. Ask concise, grouped questions when missing information would materially alter
   scope, architecture, requirements, security, operations, or user instructions.
5. Do not expose secrets. Never copy secret values from local files, environment
   variables, CI settings, logs, or credentials. Document variable names and
   purpose only when supported by safe evidence.
6. Do not modify application code, infrastructure, or product behavior unless the
   user separately authorizes those changes.
7. Preserve project instructions, terminology, language, identifiers, and existing
   documentation architecture unless a change is justified and approved.
8. Prefer a small complete documentation set over many empty or speculative files.
9. Treat incorrect documentation as a defect. Verify commands, links, examples,
   paths, contracts, and diagrams before delivery.
10. Keep specifications and implementation aligned, but never silently rewrite
    desired behavior to match accidental implementation.

## Load the references

- Read [documentation-standard.md](references/documentation-standard.md) before
  planning a new documentation set or performing a full audit.
- Read [spec-driven-development.md](references/spec-driven-development.md) whenever
  the project contains specifications or the request affects requirements,
  acceptance criteria, plans, tasks, contracts, or architectural intent.
- Read [document-templates.md](references/document-templates.md) only for the
  document types selected for the task. Copy only the relevant starting files
  from `assets/templates/` and remove every unsupported or unnecessary section.

## Workflow

### 1. Establish authority and scope

Read applicable project instructions before changing files:

- `AGENTS.md`, `CONTRIBUTING*`, repository policies, and local instruction files
- root `README*` and existing documentation indexes
- specs, plans, task files, ADRs, API contracts, schemas, migrations, tests, CI,
  deployment configuration, and representative implementation
- user-provided requirements, tickets, designs, and source material

Record the requested outcome, audiences, project phase, expected deliverables,
language, and any explicit exclusions. Infer none of these when the choice would
materially change the result.

### 2. Inventory before drafting

Run the bundled evidence collector from the skill directory:

```bash
python3 scripts/collect_project_evidence.py --root <project-root> --format markdown
```

Use its output as an inventory, not as proof of product intent. Follow with
targeted `rg`, file reads, safe build metadata inspection, and relevant tests.
Do not read dependency trees, generated output, vendored code, or actual secret
files unless the task specifically requires a safe review of them.

Classify the task:

- greenfield documentation for a new project
- brownfield documentation reconstructed from an existing project
- focused update caused by a code or product change
- documentation audit without edits
- reorganization or consolidation

### 3. Build an evidence map

For every material claim, identify the supporting source. Use this classification:

| Class | Meaning | Allowed treatment |
| --- | --- | --- |
| Confirmed | Directly supported by the user or current authoritative artifact | State as fact |
| Inferred | Strongly suggested by implementation or configuration | Label as inference and verify before making normative |
| Conflicted | Authoritative artifacts disagree | Report the conflict and ask which intent wins |
| Unknown | No reliable evidence | Ask, omit, or use an approved confirmation marker |

When code, tests, contracts, and prose disagree, describe the mismatch precisely.
Do not choose a winner only because one source is newer.

### 4. Select the smallest sufficient document set

Choose documents from the audience and change-impact analysis. Do not create every
possible file. Normally:

- keep the root README as the entry point and navigation layer
- place durable detail under the project's existing docs location
- separate product intent, architecture, contributor guidance, operations, and
  user guidance when their audiences or maintenance cycles differ
- use ADRs for decisions whose alternatives and consequences matter
- use machine-readable contracts as the reference layer for APIs or schemas when
  the project already supports them

For a full project baseline, prepare a proposed documentation map before writing.
For a focused update, change only the affected documents and their navigation.

### 5. Reconcile spec-driven artifacts first

If the project uses a spec-driven workflow, follow its existing framework and
templates. Detect, do not assume, systems such as `.specify/`, `specs/`,
`openspec/`, `.kiro/specs/`, or a project-specific convention.

Update artifacts in dependency order:

1. intent, constitution, or governing principles when truly affected
2. feature or product specification, including scope and acceptance criteria
3. technical plan, architecture decisions, and contracts
4. implementation tasks and traceability
5. implementation-facing and user-facing documentation

If implementation already drifted from the specification, produce a drift report
before changing normative intent. Ask whether the code or the specification should
change when the answer is not explicit.

### 6. Draft for the reader's task

Apply the selected templates as adaptable structures, not forms that must all be
filled. Write:

- an opening that states audience, purpose, prerequisites, coverage, and exclusions
- task-oriented headings and progressive disclosure
- short, verifiable steps with expected results where useful
- examples for common paths and failure handling for risky paths
- diagrams only when they clarify relationships, sequence, state, ownership, or
  topology better than prose
- links between intent, design, code-facing guidance, and operations

Match the repository's language. If multiple languages coexist without a clear
primary language, ask which language is authoritative and whether translations are
required.

### 7. Validate documentation as code

Perform checks appropriate to the project:

- run every safe setup command or code sample that can be verified locally
- build or preview the documentation when tooling exists
- validate relative links, anchors, referenced paths, image paths, and navigation
- compare API examples with current contracts and handlers
- compare schema documentation with migrations or schema sources
- compare deployment and runbook steps with current configuration
- verify Mermaid syntax or render diagrams when a renderer is available
- run existing documentation lint, spell, style, and link checks
- inspect the final diff for accidental rewrites and unsupported claims

If a command cannot be run, state exactly what was not verified and why. Never say
that documentation is verified when only its prose was reviewed.

### 8. Report the result

Summarize:

- documents created, updated, moved, or intentionally left unchanged
- specification changes and detected drift
- validation performed and any limitations
- unresolved questions, owners, or follow-up work

Do not claim full documentation coverage when important audiences or systems remain
outside the reviewed scope.

## Change-impact rules

Review documentation impact when a change affects any of these:

- user-visible behavior, workflow, permissions, or error handling
- functional requirements, acceptance criteria, or non-functional requirements
- API, event, CLI, schema, migration, or integration contracts
- architecture, dependencies, boundaries, or important decisions
- configuration variables, prerequisites, local setup, or developer workflow
- deployment, rollback, observability, alerting, backup, recovery, or support
- security, privacy, compliance, data retention, or threat assumptions

Purely internal refactors with no changed contract may require only an ADR, design
note, or no documentation update. Make that determination explicit.

## Completion standard

Finish only when the resulting documentation is:

- accurate enough to trace material claims to evidence
- findable from the README or existing documentation index
- scoped to named audiences and tasks
- consistent with current specifications or transparent about drift
- concise enough to maintain
- validated with the strongest checks available in the project
