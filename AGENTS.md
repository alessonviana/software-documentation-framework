# Repository instructions

## Project map

- Start with [README.md](README.md).
- Read [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) before changing structure.
- Read [docs/METHODOLOGY.md](docs/METHODOLOGY.md) before changing documentation
  principles.
- Treat `.agents/skills/document-software-project/` as the canonical skill source.
- Read [docs/PUBLIC-REPOSITORY-SAFETY.md](docs/PUBLIC-REPOSITORY-SAFETY.md) before
  publishing source-derived material.

## Required workflow

1. Inspect current instructions and affected files.
2. Preserve evidence-first behavior and framework neutrality.
3. Update the skill, references, assets, tests, and user guides together when their
   contract changes.
4. Run all repository validation before committing.
5. Review the final diff for unsupported claims, sensitive data, and source text.

## Safe commands

| Task | Command |
| --- | --- |
| Validate repository structure and public safety | `python3 scripts/validate_repository.py` |
| Run automated tests | `python3 -m unittest discover -s tests -v` |
| Inspect the framework itself | `python3 .agents/skills/document-software-project/scripts/collect_project_evidence.py --root . --format markdown` |

## Change constraints

- Never add source PDFs, ebooks, book chapters, or extensive copied passages.
- Never add credentials, actual `.env` files, private keys, customer data, or
  internal runtime artifacts.
- Never include local workspace paths, Library identifiers, or tool-call tokens.
- Do not select or change the project license without the repository owner's
  explicit approval.
- Use ASCII hyphens. Do not use Unicode dash characters.
- Keep examples obviously fictional and non-secret.
- Do not duplicate project truth across the skill, guides, and templates. Link to
  the canonical source where practical.

## Documentation impact

Update documentation in the same change when behavior, templates, skill triggers,
validation rules, installation steps, source methodology, or public-safety policy
changes.

## Definition of done

- The skill remains structurally valid.
- Tests and repository validation pass.
- Every local Markdown link resolves.
- No prohibited public content is present.
- User-facing usage instructions match the implemented paths and commands.
