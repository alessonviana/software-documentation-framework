# Contributing

Thank you for helping improve the Software Documentation Framework.

## Contribution scope

Useful contributions include:

- clearer evidence and uncertainty handling
- additional documentation templates with distinct reader needs
- safer project inspection
- better validation and drift detection
- corrections to installation or usage instructions
- tests for realistic documentation failure modes

Do not submit source PDFs, book content, customer documentation, secrets, private
project artifacts, or copied proprietary templates.

## Development workflow

1. Create a focused branch.
2. Make the smallest coherent change.
3. Update documentation and tests affected by the change.
4. Run:

   ```bash
   python3 scripts/validate_repository.py
   python3 -m unittest discover -s tests -v
   ```

5. Review the diff for unsupported claims and sensitive information.
6. Open a pull request using the repository template.

## Skill changes

When changing `.agents/skills/document-software-project/`:

- keep `SKILL.md` focused on the workflow
- place detailed policy in `references/`
- place output starting files in `assets/templates/`
- use `scripts/` only for deterministic operations
- update activation, incomplete-input, non-activation, and safety tests when needed
- preserve the rule that the skill asks instead of inventing material facts

## Documentation style

- Write direct, task-oriented prose.
- Name the audience, prerequisites, scope, and exclusions.
- Use consistent terms and descriptive links.
- Use ASCII hyphens.
- Verify commands and examples.
- Cite public sources with direct links.
- Prefer paraphrase over quotation.

## License notice

No open-source license has been selected yet. Contributions should not be submitted
until the contributor understands that no reuse license is currently granted.
