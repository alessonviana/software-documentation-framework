# ADR 0001: Keep project truth with project code

- Status: Accepted

## Context

A centralized documentation repository can standardize templates, but separating
project-specific documentation from implementation increases drift and makes it
harder for developers and AI agents to find current context.

## Decision

Store reusable standards, templates, and skill logic in this framework. Store each
software project's specifications, architecture, setup, deployment, operations,
and user documentation in that project's own repository.

## Alternatives considered

- Store all project documentation in one central repository.
- Generate every document from source code.
- Keep documentation only in tickets or chat history.

## Consequences

### Positive

- Documentation can change with code and be reviewed in the same pull request.
- Repository-local AI agents receive the relevant context.
- Ownership and version history remain close to the system.

### Negative

- Standards must be distributed and updated across projects.
- Teams need a lightweight adoption and update process.

### Risks and mitigations

- Template drift is mitigated by keeping the framework canonical and target
  project truth local.
- Inconsistent adoption is mitigated through validation guidance and examples.
