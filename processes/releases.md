# Releases

1. Confirm `main` is green (CI passing).
2. Update the version in `pyproject.toml` following [semver](https://semver.org/).
3. Tag the commit: `git tag vX.Y.Z && git push origin vX.Y.Z`.
4. CI publishes automatically on a version tag.
5. Announce in the team channel with a one-line summary of what changed.

## Versioning rules

| Change | Version bump |
|---|---|
| Breaking change | Major (`X`) |
| New content or feature | Minor (`Y`) |
| Fix or small clarification | Patch (`Z`) |
