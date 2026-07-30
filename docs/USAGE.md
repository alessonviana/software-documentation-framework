# Usage guide

## Audience

This guide is for developers, product engineers, platform teams, technical writers,
and AI-assisted development teams that need accurate, maintainable project
documentation.

## Agent compatibility

This is a portable Agent Skill, not a Codex-only instruction set. The canonical
package is stored in `.agents/skills`, which Codex, Gemini CLI, and GitHub Copilot
can discover at project scope. Claude Code supports the same skill format but
expects project skills under `.claude/skills`.

| Agent host | Project path | Invocation |
| --- | --- | --- |
| Codex | `.agents/skills/document-software-project/` | `$document-software-project` |
| Gemini CLI | `.agents/skills/document-software-project/` | Ask Gemini to use the skill |
| GitHub Copilot | `.agents/skills/document-software-project/` | Use `/document-software-project` in the prompt |
| Claude Code | `.claude/skills/document-software-project/` | `/document-software-project` |

Read [Agent compatibility](COMPATIBILITY.md) for complete installation,
verification, and fallback instructions.

## Choose an adoption mode

### Repository scope for Codex, Gemini CLI, or GitHub Copilot

Use repository scope when the workflow should apply only to one project or should
be shared with every contributor to that project.

Place the skill at:

```text
<target-project>/.agents/skills/document-software-project/
```

From a clone of this framework:

```bash
mkdir -p /path/to/target-project/.agents/skills
cp -R .agents/skills/document-software-project \
  /path/to/target-project/.agents/skills/
```

Commit the skill with the target repository only when its license and team policy
permit that use.

### Repository scope for Claude Code

Claude Code uses the same files from a different discovery location:

```bash
mkdir -p /path/to/target-project/.claude/skills
cp -R .agents/skills/document-software-project \
  /path/to/target-project/.claude/skills/
```

### User scope for Codex, Gemini CLI, or GitHub Copilot

Use user scope when the same workflow should be available across local repositories:

```text
$HOME/.agents/skills/document-software-project/
```

Install by copying:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R .agents/skills/document-software-project "$HOME/.agents/skills/"
```

Or create a symlink:

```bash
ln -s "$(pwd)/.agents/skills/document-software-project" \
  "$HOME/.agents/skills/document-software-project"
```

Codex supports symlinked skill directories.

### User scope for Claude Code

```bash
mkdir -p "$HOME/.claude/skills"
cp -R .agents/skills/document-software-project "$HOME/.claude/skills/"
```

Claude Code also supports symlinked skill directories in current versions.

### Codex skill installer

Ask the built-in installer to retrieve the skill from the repository:

```text
$skill-installer
Install the document-software-project skill from
https://github.com/alessonviana/software-documentation-framework/tree/main/.agents/skills/document-software-project
```

## Invoke the skill

In Codex:

```text
$document-software-project
<Your documentation request>
```

In Claude Code:

```text
/document-software-project
<Your documentation request>
```

In GitHub Copilot:

```text
Use the /document-software-project skill.
<Your documentation request>
```

In Gemini CLI:

```text
Use the document-software-project skill.
<Your documentation request>
```

Compatible agents may also activate the skill implicitly when a task matches its
description.

## Recommended workflows

### Audit without edits

Use this before deciding what to create:

```text
$document-software-project
Audit this repository's documentation without modifying files. Identify the current
documentation map, unsupported claims, missing reader journeys, specification
drift, and the smallest recommended improvement plan.
```

Expected result:

- evidence reviewed
- current documentation map
- prioritized findings
- specification drift
- unresolved questions
- proposed document set
- validation limitations

### Create documentation from zero

```text
$document-software-project
Inspect this project and create its documentation from zero. Keep the root README
concise, place durable detail under the existing documentation location, and ask
before writing facts that cannot be proven from project evidence.
```

The skill should:

1. read repository instructions and existing artifacts
2. inventory the project
3. classify evidence
4. ask material questions
5. propose the smallest sufficient document set
6. reconcile specifications first
7. draft selected documents
8. validate commands, links, examples, contracts, and diagrams
9. report changes and limitations

### Update after a feature

```text
$document-software-project
Review the current feature changes and update every affected specification and
document. Do not change application behavior. Show the traceability from
requirements to acceptance criteria, implementation tasks, tests, and release
documentation.
```

### Reconcile specification drift

```text
$document-software-project
Compare the feature specification, plan, tasks, tests, and implementation. Produce
a drift report before editing normative intent. Ask whether the specification or
implementation should change when the evidence is inconclusive.
```

### Prepare a repository for AI agents

```text
$document-software-project
Improve this repository's context for developers and AI agents. Create or update a
concise AGENTS.md that links to authoritative project documentation instead of
duplicating it. Verify every command in the definition of done.
```

### Review public-repository safety

```text
$document-software-project
Audit this repository for public release. Check for credentials, private paths,
personal or customer data, internal attachments, unsupported claims, and
copyrighted source material. Do not publish or delete anything.
```

## Evidence model

The skill classifies material claims:

| Class | Meaning | Action |
| --- | --- | --- |
| Confirmed | Supported directly by an authoritative source | State as fact |
| Inferred | Suggested by implementation or configuration | Label and verify |
| Conflicted | Authoritative sources disagree | Report and ask |
| Unknown | No reliable evidence exists | Ask, omit, or mark with approval |

This prevents a common documentation failure: treating implementation as proof that
the current behavior is the intended product behavior.

## What the skill reads

Depending on the task, the skill may inspect:

- `AGENTS.md`, `CONTRIBUTING*`, and repository policies
- READMEs and documentation indexes
- specifications, plans, tasks, RFCs, ADRs, and BDD features
- API contracts, schemas, migrations, and integration definitions
- representative implementation and tests
- CI, deployment, infrastructure, and configuration examples
- user-provided requirements, tickets, designs, and source material

It should avoid generated output, vendored dependencies, actual secret files, and
unnecessary broad reads.

## Use the evidence collector directly

### Markdown output

```bash
python3 .agents/skills/document-software-project/scripts/collect_project_evidence.py \
  --root /path/to/project \
  --format markdown
```

### JSON output

```bash
python3 .agents/skills/document-software-project/scripts/collect_project_evidence.py \
  --root /path/to/project \
  --format json
```

### Limit path discovery

```bash
python3 .agents/skills/document-software-project/scripts/collect_project_evidence.py \
  --root /path/to/project \
  --format json \
  --max-files 5000
```

The collector reports whether the inventory was truncated.

## Use templates manually

Templates live at:

```text
.agents/skills/document-software-project/assets/templates/
```

Choose only the required type. For example:

```bash
cp .agents/skills/document-software-project/assets/templates/ARCHITECTURE.template.md \
  /path/to/target-project/docs/ARCHITECTURE.md
```

Then:

1. identify the audience and purpose
2. remove irrelevant headings
3. replace placeholders only with verified facts
4. link authoritative sources
5. validate paths, commands, links, examples, and diagrams
6. link the finished document from the README or docs index

Do not keep empty template sections in published documentation.

## Spec-driven development

The skill does not require one SDD product. It detects and preserves existing
conventions such as:

- GitHub Spec Kit
- OpenSpec
- Kiro Specs
- BDD features
- RFCs and ADRs
- project-specific `specs/` or `requirements/`

When a change affects intent, update artifacts in dependency order:

1. governing principles
2. specification
3. clarification
4. technical plan and decisions
5. contracts and data changes
6. tasks
7. implementation and tests
8. user, developer, API, deployment, and operational documentation

For small internal changes with no contract impact, record the documentation-impact
decision without creating unnecessary specification files.

## Integrate with review

Add a documentation-impact question to the target repository's pull request
template:

```markdown
## Documentation impact

- [ ] No documentation change is required, with reason below.
- [ ] Specifications were updated.
- [ ] Developer or operator documentation was updated.
- [ ] API, data, release, or user documentation was updated.

Reason or links:
```

Use target-project CI to validate its own documentation toolchain. This framework
does not impose a static-site generator.

## Expected clarification questions

The skill should pause when answers materially affect:

- product scope or desired behavior
- users, roles, permissions, or business rules
- architecture, data, APIs, or integrations
- security, privacy, compliance, or retention
- deployment, recovery, availability, or cost
- documentation audience, language, or public visibility

A good question identifies the missing decision and its impact. It should not ask
for facts already available in the repository.

## Validation expectations

The skill should run the strongest relevant checks:

- setup and usage commands
- code samples
- local Markdown links and anchors
- API examples against contracts
- data documentation against schema or migrations
- deployment and rollback steps against configuration
- Mermaid syntax or rendering
- existing documentation build, style, spell, and link checks
- final diff review

When a check cannot be run, the final report must say what remains unverified and
why.

## Limitations

- Static inspection cannot recover original business rationale.
- Passing tests do not prove that all product intent is represented.
- A generated API reference does not replace conceptual or task guidance.
- Documentation cannot repair a poorly designed interface.
- The framework cannot select a license or organizational policy without authority.

## Update the framework

After changing the skill or scripts, run:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

Read [CONTRIBUTING.md](../CONTRIBUTING.md) before opening a pull request.
