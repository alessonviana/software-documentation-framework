# ADR 0002: Publish synthesis, not source material

- Status: Accepted

## Context

The framework was informed by public courses, community guides, a published book,
and legacy documentation templates. A public repository must not redistribute
copyrighted source files, private attachments, or extensive copied passages.

## Decision

Publish original synthesis, reusable templates, source links, and independent
scripts. Do not publish source PDFs, ebook files, book chapters, screenshots of
protected text, or internal attachment identifiers.

## Alternatives considered

- Commit every source file for convenience.
- Copy long excerpts into the methodology guide.
- Omit sources entirely.

## Consequences

### Positive

- The public repository remains focused and safer to share.
- Readers can inspect the methodology and follow direct public references.
- The framework does not depend on private attachments.

### Negative

- Some legacy source material cannot be independently inspected from this
  repository.
- Maintainers must preserve citations while paraphrasing concepts.

### Risks and mitigations

- Unsupported attribution is mitigated by linking to official public pages.
- Accidental source publication is mitigated by repository validation and review
  rules.
