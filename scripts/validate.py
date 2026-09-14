#!/usr/bin/env python3
"""Check the curated catalog, documentation links, and arXiv-only paper policy."""

import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "applications.json"
SURVEY_URL = "https://arxiv.org/abs/2609.07254"
PARADIGM_COUNTS = {
    "linear-programming": 2,
    "quadratic-programming": 1,
    "binary-and-mixed-integer-programming": 12,
    "conic-programming": 2,
    "bilevel-programming": 5,
    "multi-objective-optimization": 1,
    "inverse-optimization": 1,
    "distributionally-robust-optimization": 2,
    "submodular-optimization": 3,
    "min-max-optimization": 1,
}


def anchors(text):
    """Collect explicit HTML IDs and the heading slugs used by these documents."""
    found = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    counts = {}
    # Code snippets are not headings in GitHub's rendered document.
    without_code = re.sub(r"(?ms)^```.*?^```\s*$", "", text)
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)(?:\s+#+)?$", without_code):
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        slug = "".join(c for c in heading.lower() if c.isalnum() or c in " -_").replace(" ", "-")
        occurrence = counts.get(slug, 0)
        counts[slug] = occurrence + 1
        found.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    return found


def normalize_url(url):
    return unquote(url).replace("/paper_files/paper/", "/paper/").rstrip("/")


def validate():
    errors = []
    catalog = json.loads(OUTPUT.read_text(encoding="utf-8"))
    apps = catalog["applications"]
    if catalog.get("schema_version") != 3 or catalog.get("survey_url") != SURVEY_URL:
        errors.append("Expected catalog schema version 3 and the survey's arXiv link")
    if [app["id"] for app in apps] != list(range(1, 31)):
        errors.append("Expected applications 1 through 30 exactly once, in order")
    if [app["anchor"] for app in apps] != [f"app-{i:02d}" for i in range(1, 31)]:
        errors.append("Catalog application anchors must agree with their internal IDs")
    counts = Counter(app["paradigm_id"] for app in apps)
    paradigms = catalog["paradigms"]
    if counts != PARADIGM_COUNTS or len(paradigms) != 10:
        errors.append("Expected the survey's 10 paradigms and application counts")
    if {p["id"]: p["application_count"] for p in paradigms} != PARADIGM_COUNTS:
        errors.append("Paradigm metadata does not match the application counts")
    if next((a for a in apps if a["id"] == 2), {}).get("paradigm_id") != "linear-programming":
        errors.append("Network-flow tracking must be inside Linear Programming")
    refs = catalog["references"]
    for app in apps:
        cited = set(app["citation_keys"])
        if not cited or not cited <= refs.keys():
            errors.append(f"Application {app['id']} has missing or inconsistent citation keys")
    for key, record in refs.items():
        if record["key"] != key or not all(record.get(field) for field in ["title", "authors", "venue", "year", "url"]):
            errors.append(f"Reference {key} lacks required metadata")
        if urlsplit(record["url"]).scheme not in {"http", "https"}:
            errors.append(f"Reference {key} lacks a web URL")
    expected_ids = [f"app-{number:02d}" for number in range(1, 31)]
    for relative in ["README.md"]:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"Missing {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        if SURVEY_URL not in text:
            errors.append(f"{relative}: missing survey arXiv link")
        if re.search(r"(?m)^#{3,6}\s+\d+[.)]\s", text):
            errors.append(f"{relative}: application headings must not be numbered")
        matches = list(re.finditer(r'<a\s+(?:id|name)=["\'](app-\d{2})["\'][^>]*>', text))
        if [match.group(1) for match in matches] != expected_ids:
            errors.append(f"{relative}: expected application anchors app-01 through app-30 exactly once, in order")
            continue
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            block = text[match.end():end]
            if index == 1:
                sections = re.findall(r"(?m)^## (.+)$", text[:match.start()])
                subsections = re.findall(r"(?m)^### (.+)$", text[:match.start()])
                if not sections or sections[-1].lower() != "linear programming" or not subsections or subsections[-1] != "LP with Network-Flow Structure":
                    errors.append(f"{relative}: tracking is not nested under the LP network-flow subsection")
            heading = re.search(r"(?m)^#{3,6} .+$", block)
            if not heading:
                errors.append(f"{relative}: {match.group(1)} lacks an application heading")
                continue
            # Stop before the next paradigm or other section, including HTML anchors.
            citations = re.split(r"(?m)^(?:#{1,6}\s|<a\s)", block[heading.end():], maxsplit=1)[0]
            lines = [line.strip() for line in citations.splitlines() if line.strip()]
            if not lines or any(not line.startswith("- ") or not re.search(r"\[[^\]]+\]\(https?://", line) for line in lines):
                errors.append(f"{relative}: {match.group(1)} must contain citation bullets only")
            links = {normalize_url(url) for url in re.findall(r"https?://[^\s)>\"]+", citations)}
            for key in apps[index]["citation_keys"]:
                if key in refs and normalize_url(refs[key]["url"]) not in links:
                    errors.append(f"{relative}: {match.group(1)} lacks its cited paper {key}")
        if relative == "README.md":
            links = {normalize_url(url) for url in re.findall(r"https?://[^\s)>\"]+", text)}
            for key, record in refs.items():
                if normalize_url(record["url"]) not in links:
                    errors.append(f"README.md: bibliography record {key} has no matching paper link")
    local_links = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts or "build" in path.relative_to(ROOT).parts:
            continue
        text = path.read_text(encoding="utf-8")
        links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
        links += re.findall(r'(?:href|src)=["\']([^"\']+)["\']', text)
        for link in links:
            # Optional Markdown link titles are not used in this repository.
            parsed = urlsplit(link.strip("<>"))
            if parsed.scheme or parsed.netloc:
                continue
            if not parsed.path and not parsed.fragment:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {link}")
                continue
            local_links += 1
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local target: {link}")
            elif parsed.fragment and target.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(target.read_text(encoding="utf-8")):
                    errors.append(f"{path.relative_to(ROOT)}: missing Markdown anchor: {link}")
            elif parsed.fragment and target.suffix in {".tex", ".bib", ".py"}:
                line = re.fullmatch(r"L(\d+)(?:-L(\d+))?", parsed.fragment)
                if line and int(line.group(1)) > len(target.read_text(encoding="utf-8").splitlines()):
                    errors.append(f"{path.relative_to(ROOT)}: source line outside file: {link}")
    tracked = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.split("\0")
    for name in filter(None, tracked):
        path = Path(name)
        if path.parts[0] == "paper" or path.suffix.lower() in {".tex", ".bib", ".pdf"}:
            errors.append(f"Bundled manuscript material is forbidden; link to arXiv instead: {name}")
    if errors:
        raise SystemExit("Validation failed:\n" + "\n".join(f"- {error}" for error in errors))
    print(f"PASS: 30 applications, 10 paradigms, {len(refs)} reference records; all citation keys resolve.")
    print(f"PASS: 30 unnumbered application headings with citation bullets only, all primary-paper links, {local_links} local links/anchors.")
    print("PASS: network-flow placement and arXiv-only manuscript links; no bundled source, bibliography, or PDF.")
    print("These structural checks do not independently verify bibliographic accuracy or external URL availability.")


if __name__ == "__main__":
    validate()
