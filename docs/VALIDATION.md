# Validation

## Local checks

Run:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

## Repository validation

`scripts/validate_repository.py` checks:

- required framework files
- `SKILL.md` frontmatter
- local Markdown links
- prohibited public file types
- sensitive filenames
- internal local paths and attachment identifiers
- prohibited Unicode dash characters
- template and skill path consistency

## Automated tests

The test suite verifies that the evidence collector:

- excludes actual `.env` files and their values
- reads only variable names from example environment files
- detects documentation, specification, API, CI, container, and manifest signals
- avoids following symlinked files
- produces valid JSON and readable Markdown

## Continuous integration

`.github/workflows/validate.yml` runs validation and tests on:

- pushes to `main`
- pull requests targeting `main`

CI uses only the Python standard library. The framework has no runtime package
dependency.

## Manual review

Automation cannot verify product intent, copyright ownership, or whether a
paraphrase is sufficiently original. Every public change still requires a manual
diff review using [the public-repository safety checklist](PUBLIC-REPOSITORY-SAFETY.md).
