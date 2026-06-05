# Python Standards

- **Formatter:** `ruff format` — no manual style debates.
- **Linter:** `ruff check` — fix all warnings before merging.
- **Type hints:** required on all public functions and methods.
- **Python version:** 3.11+.

## Naming

- Functions and variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`

## Dependencies

- Declared in `pyproject.toml`. No loose `requirements.txt`.
- Pin direct dependencies; let the lock file handle transitive ones.
