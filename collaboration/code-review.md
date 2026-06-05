# Code Review

## As an author

- Keep PRs small and focused. One change per PR.
- Write a clear description explaining *why*, not just *what*.
- Self-review your diff before requesting a review.

## As a reviewer

- Aim to review within one working day.
- Distinguish blockers from suggestions: prefix suggestions with `nit:` or `optional:`.
- Approve when you'd be comfortable shipping it — not when it's perfect.
- Practice Radical Candor: challenge directly but care personally. Keep feedback focused on the code, not the author.

## Merging

- At least one approval required before merging.
- The author merges (not the reviewer), once CI passes.
- Squash merge to keep `main` history clean.
