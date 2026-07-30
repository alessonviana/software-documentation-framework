# Public-repository safety

## Purpose

Use this policy before publishing any change. The goal is to keep the repository
useful without exposing private data, credentials, internal artifacts, or protected
source material.

## Allowed content

- original framework instructions
- original templates
- fictional examples
- scripts that operate on user-selected local projects
- public source links and short paraphrased summaries
- tests generated specifically for this repository
- repository-specific architecture and decisions

## Prohibited content

- actual `.env` files or secret values
- API tokens, passwords, private keys, certificates, or credential stores
- customer, employee, student, or patient data
- private repository content
- internal workspace paths or local tool identifiers
- source PDFs, ebooks, book chapters, or extensive copied passages
- screenshots containing private information
- production logs, database dumps, backups, or runtime exports
- a license selected without the repository owner's explicit approval

## Source-material rule

When a source informs the framework:

1. identify the principle in your own words
2. link to an authoritative public page when available
3. quote only when necessary and keep quotations short
4. do not commit the source file unless redistribution rights are confirmed
5. do not expose internal attachment names or identifiers

## Secret-handling rule

Examples may use names such as `API_TOKEN`, but values must be obvious placeholders.
Never use values copied from a real environment.

The evidence collector may read variable names from `.env.example`,
`.env.sample`, or another recognized example file. It must exclude actual `.env`
files and values.

## Pre-publication checklist

- [ ] Repository validation passes.
- [ ] Automated tests pass.
- [ ] No source PDFs, ebooks, archives, or office documents are present.
- [ ] No local workspace paths or attachment identifiers are present.
- [ ] No real credentials or personal information are present.
- [ ] Examples are fictional and non-secret.
- [ ] Source-derived prose is original and linked.
- [ ] The license status is represented accurately.
- [ ] The final diff contains only intended files.

## If sensitive content is found

Stop publication. Remove the content from the proposed change and determine whether
it exists in published history. If it does, rotate any exposed credential first,
then follow GitHub guidance for removing sensitive data from repository history.
