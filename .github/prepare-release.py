"""Get the repository ready for a release: pick the next version number, set it in
tools/countertop.py, and gather the notes in changes/ into that version's section of CHANGELOG.md.

    python3 .github/prepare-release.py fix        # 0.3.1 -> 0.3.2
    python3 .github/prepare-release.py feature    # 0.3.1 -> 0.4.0
    python3 .github/prepare-release.py 1.0.0      # an exact version

Prints the new tag (e.g. v0.3.2) and removes the note files it used. Stops with an error, and
changes nothing, if there are no notes or the version would not go up.
"""
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVER = ROOT / "tools" / "countertop.py"
CHANGELOG = ROOT / "CHANGELOG.md"
CHANGES = ROOT / "changes"
KINDS = [("new", "New"), ("changed", "Changed"), ("fixed", "Fixed")]

how = sys.argv[1] if len(sys.argv) > 1 else ""
code = SERVER.read_text()
cur = re.search(r'^VERSION = "(\d+)\.(\d+)\.(\d+)"', code, re.M)
if not cur:
    sys.exit("Couldn't find VERSION in tools/countertop.py")
major, minor, patch = map(int, cur.groups())
if how == "fix":
    new = (major, minor, patch + 1)
elif how == "feature":
    new = (major, minor + 1, 0)
elif re.fullmatch(r"v?\d+\.\d+\.\d+", how):
    new = tuple(map(int, how.lstrip("v").split(".")))
else:
    sys.exit("usage: prepare-release.py fix | feature | X.Y.Z")
if new <= (major, minor, patch):
    sys.exit("v%d.%d.%d isn't newer than the current version v%d.%d.%d" % (new + (major, minor, patch)))
ver = "%d.%d.%d" % new

text = CHANGELOG.read_text()
# notes written straight into an "## Unreleased" section (the older way) still count
old = re.search(r"^## Unreleased[ \t]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
old_notes = old.group(1).strip() if old else ""
if old:
    text = text[:old.start()] + text[old.end():]

used, parts = [], []
for folder, heading in KINDS:
    lines = []
    for f in sorted((CHANGES / folder).glob("*.md")):
        body = f.read_text().strip()
        if body:
            lines.append(body if body.startswith("- ") else "- " + body)
        used.append(f)
    if lines:
        parts.append("### %s\n%s" % (heading, "\n".join(lines)))
notes = "\n\n".join(p for p in [old_notes] + parts if p)
if not notes:
    sys.exit("There are no notes for this release. Add a file under changes/new, changes/changed or changes/fixed "
             "(see changes/README.md), then try again.")

today = datetime.date.today().isoformat()
first = re.search(r"^## ", text, re.M)
at = first.start() if first else len(text)
text = text[:at] + "## v%s (%s)\n\n%s\n\n" % (ver, today, notes) + text[at:]
CHANGELOG.write_text(text)
SERVER.write_text(code[:cur.start()] + 'VERSION = "%s"' % ver + code[cur.end():])
for f in used:
    f.unlink()
print("v" + ver)
