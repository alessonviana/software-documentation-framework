# Software documentation standard

## Contents

1. Purpose and source basis
2. Common principles
3. Evidence and source-of-truth policy
4. Audience and documentation map
5. Document selection
6. Writing and information architecture
7. Technical content
8. Review and validation
9. Maintenance and governance
10. Lightweight adoption

## 1. Purpose and source basis

Use this standard to plan, create, audit, and maintain documentation for software
products and the teams or AI agents that work on them. Adapt it to the project's
size, risk, audience, and established conventions.

This standard synthesizes:

- legacy academic and sprint-oriented software documentation templates reviewed
  during the framework's design, including project purpose, scope, stakeholders,
  business rules, functional and non-functional requirements, architecture, data,
  testing, deployment, user guidance, change impact, scenarios, and screens
- Google Technical Writing, "Organizing large documents", which emphasizes
  outlining, introductions that state coverage and prerequisites, task-oriented
  headings, navigation, and progressive disclosure:
  https://developers.google.com/tech-writing/two/large-docs
- Write the Docs, which emphasizes early and participatory documentation,
  docs-as-code, content close to code, clear ownership, consistent style,
  accessible content, and automated quality checks:
  https://www.writethedocs.org/guide/
- *Docs for Developers: An Engineer's Field Guide to Technical Writing*, whose
  published framework moves from audience research and planning through drafting,
  editing, examples, visuals, publishing, feedback, measurement, organization, and
  maintenance:
  https://link.springer.com/book/10.1007/979-8-8688-2509-5
- GitHub Spec Kit's official spec-driven flow and quality gates, used only when a
  repository adopts that workflow:
  https://github.github.com/spec-kit/

The legacy academic template is broad and useful as a coverage inventory, not as
a mandatory monolithic document. Modern projects benefit from modular,
version-controlled documentation selected by audience and task. The source PDFs
and book text are not redistributed by this project.

## 2. Common principles

The sources converge on these principles:

1. Start with the audience, their task, and the problem being solved.
2. Define scope and exclusions before adding detail.
3. Plan the information architecture before drafting.
4. Treat documentation as part of product and engineering work, not an afterthought.
5. Keep documentation reviewable, versioned, and close to the implementation.
6. Organize content for findability with clear entry points, headings, and links.
7. Reveal complexity progressively and use examples or visuals only when useful.
8. Separate intent, explanation, procedures, reference, and operational guidance.
9. Review and test documentation for accuracy, usability, accessibility, and drift.
10. Maintain it through ownership, change triggers, feedback, and measurable checks.

## 3. Evidence and source-of-truth policy

### 3.1 Source categories

Use each source for what it can authoritatively establish:

| Source | Strong evidence for | Not sufficient by itself for |
| --- | --- | --- |
| Explicit user or stakeholder decision | Desired outcomes, priorities, scope | Current implementation |
| Product or feature specification | Normative behavior and acceptance | Proof that behavior exists |
| API contract or schema | Interface shape and constraints | Business rationale |
| ADR or approved design | Decision, alternatives, consequences | Current deployment state |
| Tests | Verified examples and expected behavior | Complete product intent |
| Implementation | Current mechanics and observable behavior | Why the behavior is correct |
| Deployment and IaC configuration | Defined infrastructure and workflow | Runtime health or manual exceptions |
| Logs or runtime inspection | Observed state at a point in time | Desired long-term behavior |
| Existing prose | Prior understanding | Accuracy without corroboration |

Freshness alone does not resolve conflicts. A recent workaround can be less
authoritative than an approved specification, while an old specification can have
failed to incorporate an accepted change.

### 3.2 Fact handling

- State confirmed information directly.
- Label current-state reconstruction from code as "Observed implementation" when
  product intent is unknown.
- Label proposals as proposals.
- Preserve open questions as a short list with a responsible decision-maker when
  known.
- Never add invented owners, dates, service-level targets, user roles, data
  retention periods, costs, URLs, ports, or environment behavior.
- Never document sample credentials that resemble real secrets.

### 3.3 Conflict handling

When sources disagree:

1. quote or summarize each conflicting claim
2. cite its path, section, or source
3. explain the practical impact
4. ask which intent is authoritative
5. avoid destructive consolidation until resolved

## 4. Audience and documentation map

| Audience | Primary questions | Likely documents |
| --- | --- | --- |
| Evaluator or stakeholder | What is this, for whom, why, and what is in scope? | README, product overview, feature specs |
| New developer or AI agent | How is the project organized and how do I work safely? | README, contributor guide, development guide, architecture, concise agent instructions when used |
| Maintainer | Why was it built this way and what changes are risky? | architecture, ADRs, data and integration docs |
| API or platform consumer | How do I integrate and recover from errors? | API reference, quickstart, examples, troubleshooting |
| Operator or on-call engineer | How do I deploy, observe, roll back, and recover? | deployment guide, runbooks, observability, backup and recovery |
| End user or support | How do I accomplish a task or solve a problem? | tutorials, how-to guides, reference, troubleshooting |
| Security or compliance reviewer | What data, controls, boundaries, and assumptions exist? | security model, data flows, retention and access docs |

One person can occupy several audiences. Separate documents when their tasks,
permissions, terminology, or update cycles differ.

## 5. Document selection

### 5.1 Baseline entry point

Keep a root README that answers:

- what the project does and what problem it solves
- current status when known
- primary audience
- fastest verified path to run or use it
- prerequisites
- links to deeper documentation
- where to get support or contribute, when applicable
- license only when confirmed

The README is a map, not the entire documentation body.

### 5.2 Select by evidence and risk

Create these only when the project needs them:

- product overview for goals, scope, users, business rules, and success
- feature specs for scenarios, requirements, exclusions, acceptance, and edge cases
- experience or UI guidance for important screens, navigation, states, validation,
  accessibility, and design sources
- architecture for boundaries, components, data flow, dependencies, and quality
  attributes
- ADRs for consequential decisions and tradeoffs
- development guide for setup, commands, conventions, and repository workflow
- testing guide for strategy, levels, fixtures, environments, and verification
- API or event reference for public or internal contracts
- data model for entities, relationships, migrations, classification, and lifecycle
- deployment guide for environments, configuration, release, and rollback
- runbooks for detection, diagnosis, mitigation, recovery, and escalation
- security documentation for trust boundaries, authentication, authorization,
  secrets, sensitive data, abuse cases, and safe defaults
- user documentation for task guidance and troubleshooting
- release notes for user-relevant changes and required actions
- `AGENTS.md` or an established equivalent for repository-specific agent commands,
  constraints, validation, and definition of done

Keep agent instructions short and operational. Link to durable project
documentation instead of duplicating architecture, requirements, or runbooks.

### 5.3 Avoid document inflation

Do not create:

- empty files that only contain headings
- duplicate explanations across multiple sources
- diagrams that restate a simple paragraph
- generated reference copied into manually maintained prose
- speculative roadmaps or requirements inferred from code
- a single giant document when audiences need different entry points

## 6. Writing and information architecture

### 6.1 Introductions

Open substantial documents with:

- purpose
- audience
- prerequisites
- included topics
- explicit exclusions

Keep background only when it helps the reader complete the intended task.

### 6.2 Structure

- Organize procedures by reader goal.
- Put prerequisite concepts before dependent concepts.
- Use descriptive headings that make sense in search results.
- Add brief context under a heading before lower-level subsections.
- Start with the common path, then add variations and advanced cases.
- Break long procedures into independently verifiable sub-tasks.
- Provide "next" and related links when navigation is not obvious.
- Add a table of contents to long reference documents.

### 6.3 Style

- Prefer plain, direct language and concrete nouns.
- Use consistent product names, UI labels, commands, and terminology.
- Define necessary terms near first use and maintain a glossary only when terms are
  numerous or domain-specific.
- Use active voice when it clarifies responsibility.
- Avoid filler, marketing claims, idioms, unexplained acronyms, and vague words such
  as "simple", "obvious", or "just".
- Write link text that describes the destination.
- Make lists parallel and procedures sequential.
- Use accessible headings, table headers, alt text, contrast, and non-color cues.

## 7. Technical content

### 7.1 Requirements

Keep functional and non-functional requirements distinct. A requirement should be:

- uniquely identifiable when traceability matters
- observable or verifiable
- free of hidden implementation detail unless it is a genuine constraint
- linked to acceptance criteria, tests, or tasks when the workflow supports it

Record out-of-scope behavior to prevent accidental expansion.

### 7.2 Examples and commands

- Prefer the smallest realistic example that proves the common task.
- State prerequisites and expected output.
- Use placeholders that are unmistakably non-secret.
- Include meaningful failure handling.
- Execute samples where safe and compare their output with the documentation.
- Generate repetitive API or schema reference from authoritative contracts when
  possible, but keep explanation and task guidance human-written.

### 7.3 Diagrams

Use diagrams for:

- system context and component boundaries
- three or more meaningful interactions
- state transitions
- data relationships
- deployment topology
- ownership or dependency relationships that are hard to explain linearly

Name every boundary and important arrow. Accompany the diagram with a short
interpretation, assumptions, and links to relevant contracts or ADRs. Keep the
source editable and versioned.

### 7.4 Decisions

An ADR records one decision with status, context, decision, alternatives, and
consequences. Do not rewrite an accepted historical ADR to make a new decision look
old. Supersede it with a new ADR and link both.

## 8. Review and validation

Apply the strongest relevant checks:

| Check | Purpose |
| --- | --- |
| Subject-matter review | Verify intent, constraints, and domain language |
| Reader or friction review | Confirm a target reader can complete the task |
| Command and sample execution | Prevent stale procedures and examples |
| Link and anchor validation | Preserve navigation and findability |
| Docs build | Catch syntax, rendering, and navigation defects |
| Style and terminology lint | Maintain consistency and accessibility |
| Contract or schema comparison | Detect API and data drift |
| Diff review | Catch accidental deletion, scope creep, and unsupported claims |

For high-risk operational instructions, test in a safe environment and include
preconditions, impact, rollback, and a stopping condition.

## 9. Maintenance and governance

### 9.1 Keep docs in the delivery workflow

- Review documentation in the same change as affected code when practical.
- Add a documentation-impact check to change templates or review criteria.
- Require documentation updates for changes listed in the skill's impact rules.
- Keep named ownership at document area or subsystem level when the organization
  can support it.
- Archive or remove obsolete content deliberately, repairing inbound links.
- Version user-facing docs when supported versions materially differ.

### 9.2 Feedback and measurement

Use a lightweight combination of:

- reader feedback and recurring support questions
- search terms that fail to produce useful results
- task completion or friction observations
- stale or broken-link counts
- documentation build and lint failures
- time-to-first-success for onboarding
- change coverage for releases

Metrics guide improvement; they do not replace qualitative review.

## 10. Lightweight adoption

For an MVP or small team:

1. keep docs in the application repository
2. use Markdown and the existing review workflow
3. maintain a strong README plus only the high-value detail pages
4. record consequential decisions as ADRs
5. add link checking and one documentation-impact question to CI or reviews
6. expand tooling only when real reader or maintenance pain justifies it

A separate centralized repository can hold organization-wide templates, terminology,
or policy. Project-specific truth should remain near the project it describes.
