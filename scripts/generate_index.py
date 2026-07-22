#!/usr/bin/env python3
"""
Regenerates index.md from the live git-tracked repo state.

Run manually: python3 scripts/generate_index.py
Also run automatically by .github/workflows/regenerate-index.yml on every
push to main.
"""
import re
import subprocess
import datetime
import os
from collections import defaultdict, Counter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git_ls_files(pattern):
    result = subprocess.run(
        ["git", "ls-files", pattern],
        capture_output=True, text=True, cwd=REPO_ROOT,
    )
    return [l for l in result.stdout.splitlines() if l]


def get_field(frontmatter, field, default="—"):
    m = re.search(rf"^{field}:\s*(.+)$", frontmatter, re.MULTILINE)
    return m.group(1).strip() if m else default


def main():
    all_md = git_ls_files("*.md")
    files = [
        f for f in all_md
        if "/archive/" not in f
        and f not in ("index.md", "log.md", "schema.md", "RESOLVER.md")
        and not f.endswith("README.md")
    ]
    files.sort()

    by_folder = defaultdict(list)
    status_counter = Counter()
    doc_type_counter = Counter()
    confidentiality_counter = Counter()
    missing_metadata = []

    for path in files:
        full_path = os.path.join(REPO_ROOT, path)
        with open(full_path, encoding="utf-8") as f:
            content = f.read()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
        if not m:
            missing_metadata.append(path)
            continue
        fm, body = m.group(1), m.group(2)

        doc_type = get_field(fm, "doc_type", "sop")
        status = get_field(fm, "status", "Unknown")
        confidentiality = get_field(fm, "confidentiality", "Internal")

        summary_m = re.search(r"^>\s*(.+)$", body, re.MULTILINE)
        summary = summary_m.group(1).strip() if summary_m else ""
        if len(summary) > 140:
            summary = summary[:137] + "..."

        folder = os.path.dirname(path) + "/"
        by_folder[folder].append(
            (os.path.basename(path), path, doc_type, status, confidentiality, summary)
        )
        status_counter[status] += 1
        doc_type_counter[doc_type] += 1
        confidentiality_counter[confidentiality] += 1

    archive_count = len(git_ls_files("**/archive/*.md"))
    today = datetime.date.today().isoformat()

    lines = []
    lines.append("# Musti Musik Brain — Index")
    lines.append("")
    lines.append(
        f"_Auto-regenerated {today} by `.github/workflows/regenerate-index.yml` "
        f"from `git ls-files` (live tracked repo state) on every push to `main`. "
        f"Never edit this file by hand — it will be overwritten on the next push. "
        f"To regenerate manually: `python3 scripts/generate_index.py`._"
    )
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(
        f"- **Total embeddable files:** {len(files)} (excludes `archive/` "
        f"subfolders — {archive_count} files there, human-reference only, "
        f"never embedded per RESOLVER ETL Skip Rules)"
    )
    if missing_metadata:
        lines.append(
            f"- **⚠ Missing frontmatter (skipped by ETL, needs fixing):** "
            f"{len(missing_metadata)} — {', '.join(missing_metadata)}"
        )
    lines.append("")
    lines.append(
        "**By status** (how much content is human-verified vs not):"
    )
    lines.append("")
    lines.append("| Status | Count | % |")
    lines.append("| --- | --- | --- |")
    total = sum(status_counter.values())
    for s in ["Approve", "Draft", "Unknown", "Archive"]:
        c = status_counter.get(s, 0)
        pct = round(100 * c / total) if total else 0
        lines.append(f"| {s} | {c} | {pct}% |")
    lines.append("")
    lines.append("**By doc_type:**")
    lines.append("")
    lines.append("| doc_type | Count |")
    lines.append("| --- | --- |")
    for dt, c in sorted(doc_type_counter.items(), key=lambda x: -x[1]):
        lines.append(f"| {dt} | {c} |")
    lines.append("")
    lines.append("**By confidentiality:**")
    lines.append("")
    lines.append("| Tier | Count |")
    lines.append("| --- | --- |")
    for cf, c in sorted(confidentiality_counter.items(), key=lambda x: -x[1]):
        lines.append(f"| {cf} | {c} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    for folder in sorted(by_folder.keys()):
        entries = sorted(by_folder[folder])
        lines.append(f"## {folder}")
        lines.append("")
        lines.append("| File | doc_type | status | confidentiality | Summary |")
        lines.append("| --- | --- | --- | --- | --- |")
        for fname, path, doc_type, status, confidentiality, summary in entries:
            lines.append(
                f"| [{fname}]({path}) | {doc_type} | {status} | "
                f"{confidentiality} | {summary} |"
            )
        lines.append("")

    out_path = os.path.join(REPO_ROOT, "index.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Indexed {len(files)} files ({archive_count} archived, excluded)")
    print(f"Missing frontmatter: {missing_metadata}")
    print(f"Status breakdown: {dict(status_counter)}")


if __name__ == "__main__":
    main()
