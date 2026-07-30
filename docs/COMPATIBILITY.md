# Agent compatibility

## Compatibility statement

`document-software-project` follows the open
[Agent Skills specification](https://agentskills.io/specification). Its core
package is portable: `SKILL.md`, references, templates, and scripts do not depend
on one language model vendor.

Compatibility depends on the agent host, not only on the underlying LLM. A host
must be able to discover or read the skill directory, load referenced files, and,
for the complete workflow, access the project filesystem and run Python 3.

The locations and commands below were verified against official documentation on
July 30, 2026.

## Support matrix

| Agent host | Native Agent Skills support | Project scope | User scope | Explicit use |
| --- | --- | --- | --- | --- |
| Codex | Yes | `.agents/skills/` | `~/.agents/skills/` | `$document-software-project` |
| Gemini CLI | Yes | `.agents/skills/` or `.gemini/skills/` | `~/.agents/skills/` or `~/.gemini/skills/` | Ask Gemini to use the named skill |
| GitHub Copilot | Yes | `.agents/skills/`, `.github/skills/`, or `.claude/skills/` | `~/.agents/skills/` or `~/.copilot/skills/` | Include `/document-software-project` in the prompt |
| Claude Code | Yes | `.claude/skills/` | `~/.claude/skills/` | `/document-software-project` |
| Other coding agents | Varies | Product-specific | Product-specific | Follow the product's Agent Skills documentation |
| Chat-only LLMs | Usually no automatic discovery | Not applicable | Not applicable | Attach or paste files manually, with reduced capability |

## Install for Codex

### Repository scope

```bash
mkdir -p /path/to/project/.agents/skills
cp -R .agents/skills/document-software-project \
  /path/to/project/.agents/skills/
```

Invoke:

```text
$document-software-project
Audit this repository's documentation without editing files.
```

### User scope

```bash
mkdir -p "$HOME/.agents/skills"
cp -R .agents/skills/document-software-project "$HOME/.agents/skills/"
```

Codex can also install the skill from this repository through `$skill-installer`.
See the [official Codex skill guidance](https://learn.chatgpt.com/docs/build-skills).

## Install for Claude Code

Claude Code uses the same Agent Skills format but discovers project skills under
`.claude/skills` and personal skills under `~/.claude/skills`.

### Repository scope

```bash
mkdir -p /path/to/project/.claude/skills
cp -R .agents/skills/document-software-project \
  /path/to/project/.claude/skills/
```

Start Claude Code from the target project and invoke:

```text
/document-software-project
Inspect this project and create the smallest sufficient documentation baseline.
Do not invent missing product or technical facts.
```

### User scope

```bash
mkdir -p "$HOME/.claude/skills"
cp -R .agents/skills/document-software-project "$HOME/.claude/skills/"
```

Claude Code can invoke a matching skill automatically or through
`/document-software-project`. Claude Code also supports symlinked skill
directories in current versions. See the
[official Claude Code skills documentation](https://code.claude.com/docs/en/skills).

## Install for Gemini CLI

Google documents `.agents/skills` as a project discovery location for Gemini CLI.

```bash
mkdir -p /path/to/project/.agents/skills
cp -R .agents/skills/document-software-project \
  /path/to/project/.agents/skills/
```

Start Gemini CLI from the project, then verify discovery:

```text
/skills list
```

Request the workflow explicitly:

```text
Use the document-software-project skill to audit this repository.
Do not modify files. Report unsupported claims, documentation gaps, specification
drift, and questions that require confirmation.
```

See Google's
[Gemini CLI Agent Skills documentation](https://geminicli.com/docs/cli/skills/).

## Install for GitHub Copilot

GitHub Copilot recognizes project skills in `.agents/skills`, `.github/skills`, or
`.claude/skills`. This repository uses `.agents/skills` as its canonical location.

```bash
mkdir -p /path/to/project/.agents/skills
cp -R .agents/skills/document-software-project \
  /path/to/project/.agents/skills/
```

For personal use:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R .agents/skills/document-software-project "$HOME/.agents/skills/"
```

In Copilot CLI, reload and inspect the skill when necessary:

```text
/skills reload
/skills info document-software-project
```

Invoke it in a prompt:

```text
Use the /document-software-project skill to review this repository and update only
the documentation affected by the current feature.
```

See GitHub's
[agent skills documentation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## Use with another coding agent

Before installation, verify that the product supports the Agent Skills open
standard and identify its project and user discovery directories.

If it supports Agent Skills:

1. copy the entire `document-software-project` directory
2. preserve `SKILL.md`, `references/`, `assets/`, and `scripts/`
3. place it in the product's documented skills directory
4. restart or reload the agent if required
5. ask the agent to list or inspect installed skills
6. invoke the skill by name with an audit-only request first

Do not copy only `SKILL.md`. The workflow depends on its references, templates,
and evidence collector.

## Use without native Agent Skills support

An agent with filesystem access can use the framework manually:

```text
Read .agents/skills/document-software-project/SKILL.md completely and follow it
for this task. Load referenced files only when the SKILL.md instructions require
them. Do not invent information. Ask before writing unsupported claims.
```

This is a fallback, not full native integration. The agent may not:

- discover or activate the skill automatically
- preserve progressive loading of references
- resolve relative skill paths correctly
- run the evidence collector
- validate project files or commands

For a chat-only LLM without repository access, attach the required files and ask
for an audit or draft. Treat its output as unverified until a filesystem-capable
agent or a person checks it against the actual project.

## Portability boundaries

The skill provides a workflow and reusable resources. It does not provide the
agent host with permissions or tools it does not already have.

Results can differ when an agent lacks:

- project filesystem access
- shell or Python 3 execution
- Git history
- access to referenced specifications or tickets
- permission to edit or validate files

An agent must report these limitations instead of claiming that the documentation
was fully verified.
