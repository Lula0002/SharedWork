# Security Standards

## Hard rules

- **No secrets in code.** No API keys, passwords, tokens, or credentials — ever. Use environment variables or a secrets manager.
- **No secrets in commit history.** If a secret is committed, rotate it immediately — deleting the file is not enough.
- **Dependencies must be pinned.** Lock files (`requirements.txt`, `poetry.lock`, etc.) are committed and kept up to date.
- **No `eval`, `exec`, or `subprocess` with unsanitized input.** Treat all external input as untrusted.

## Before opening a PR

- Check your diff for anything that looks like a key, token, or password.
- If you added a new dependency, verify it is actively maintained and has no known critical CVEs.

## If you find a vulnerability

1. Do not open a public issue.
2. Report it directly to the team lead via a private channel.
3. Agree on a fix timeline before disclosing publicly.

## Dependency scanning

CI runs dependency checks on every push. A failing scan blocks merge — do not bypass it.
If a flagged dependency has no fix yet, document it in `processes/decision-log.md` with a review date.
