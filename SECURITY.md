# Security policy

## Scope

Security reports may concern:

- the evidence collector reading excluded secret files or values
- repository validation failing to detect sensitive public content
- unsafe commands in templates or guides
- path traversal, symlink traversal, or unintended filesystem access
- examples that could expose or normalize insecure practices

## Reporting

Do not open a public issue containing credentials, private repository content,
customer data, or a working exploit with sensitive impact.

Use GitHub private vulnerability reporting if it is enabled for this repository.
If it is not enabled, contact the repository owner through a private channel listed
on the owner's GitHub profile before sharing sensitive details.

## Safe report contents

Include:

- the affected file and behavior
- a minimal reproduction using fictional data
- the expected safe behavior
- the potential impact
- a suggested mitigation when available

Do not include real tokens, passwords, private keys, or third-party confidential
material.
