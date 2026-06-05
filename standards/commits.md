# Commit Messages

## Format

```text
<type>: <short summary>

[optional body — wrap at 72 characters]
```

The summary line must be under 72 characters. Use the imperative mood: "add feature" not "added feature" or "adds feature".

## Types

| Type | Use for |
|---|---|
| `feat` | New content, feature, or capability |
| `fix` | Correcting something that was wrong |
| `docs` | Changes to documentation only |
| `chore` | Tooling, CI, dependencies, repo maintenance |
| `refactor` | Restructuring without changing meaning |

## Examples

```text
feat: add RFC template for async decisions

fix: remove duplicate bullet in sbar-template

chore: add trailing newline to pass MD047
```

## Rules

- One logical change per commit. If you need "and" in the summary, split it.
- The summary says *what* changed. The body (if needed) says *why*.
- Never commit secrets, credentials, or generated files.
