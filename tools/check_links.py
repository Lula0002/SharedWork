"""Check that all internal markdown links in the repo resolve to real files."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
LINK_RE = re.compile(r"\[.*?\]\(([^)]+)\)")


def check() -> list[str]:
    errors = []
    for md_file in ROOT.rglob("*.md"):
        text = md_file.read_text()
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if target.startswith("http"):
                continue
            resolved = (md_file.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{md_file.relative_to(ROOT)}: broken link → {target}")
    return errors


if __name__ == "__main__":
    errors = check()
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print("All internal links OK.")
