# Testing Standards

- Tests live next to the code they test or in a `tests/` mirror structure.
- Use `pytest`. No other test runner.
- Every public function has at least one test covering the happy path.
- Test names describe the scenario: `test_user_login_returns_token_on_success`.

## What to test

- Unit tests for pure functions.
- Integration tests for anything touching a database, API, or file system.
- Do not mock internals — only mock at system boundaries.
