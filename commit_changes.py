#!/usr/bin/env python3
"""Commit documentation changes grouped by service and guide."""
from __future__ import annotations

import os
import re
import subprocess
import sys
from collections import OrderedDict
from typing import Iterable, List, Optional, Sequence, Set, Tuple


SPECIAL_SLUGS = {
    "apireference": "API reference",
    "api-reference": "API reference",
    "apireferences": "API references",
    "userguide": "user guide",
    "user-guide": "user guide",
    "developerguide": "developer guide",
    "developer-guide": "developer guide",
    "gettingstarted": "getting started",
    "getting-started": "getting started",
    "faqs": "FAQs",
    "faq": "FAQ",
    "cli": "CLI",
}

VERSION_MARKERS = {
    "latest",
    "current",
    "preview",
    "prerelease",
    "prod",
}


def run_git(args: Sequence[str], *, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], check=check, text=True)


def prettify_slug(slug: Optional[str]) -> str:
    if not slug:
        return ""

    lower = slug.lower()
    if lower in SPECIAL_SLUGS:
        return SPECIAL_SLUGS[lower]

    text = slug.replace("-", " ").replace("_", " ")
    text = re.sub(r"(?<=[a-z0-9])([A-Z])", r" \1", text)
    text = re.sub(r"(?<=[A-Z])([A-Z][a-z])", r" \1", text)
    text = re.sub(r"\s+", " ", text).strip()

    words: List[str] = []
    for word in text.split(" "):
        if not word:
            continue
        if re.fullmatch(r"[A-Z0-9]+", word):
            words.append(word)
        else:
            words.append(word[0].upper() + word[1:].lower())
    return " ".join(words)


def format_guide(slug: Optional[str]) -> str:
    pretty = prettify_slug(slug)
    if not pretty:
        return ""
    words = []
    for word in pretty.split():
        if re.fullmatch(r"[A-Z0-9]+", word):
            words.append(word)
        else:
            words.append(word.lower())
    return " ".join(words)


def determine_group(path: str) -> Tuple[Optional[str], Optional[str]]:
    if not path.startswith("docs/"):
        return (None, None)

    parts = path.split("/")
    if len(parts) < 2:
        return (None, None)

    service = parts[1]
    guide: Optional[str] = None

    if len(parts) > 2:
        candidate = parts[2]
        candidate_lower = candidate.lower()
        if (
            candidate_lower in VERSION_MARKERS
            or bool(re.search(r"\d", candidate_lower))
            or candidate_lower.startswith("v")
        ):
            if len(parts) > 3:
                guide = parts[3]
        else:
            guide = candidate
    return (service, guide)


def parse_status() -> List[Tuple[str, str, Optional[str]]]:
    result = subprocess.check_output(["git", "status", "--porcelain=1", "-z"])
    if not result:
        return []

    entries = iter(result.split(b"\0"))
    changes: List[Tuple[str, str, Optional[str]]] = []

    for entry in entries:
        if not entry:
            break

        status = entry[:2].decode()
        path = entry[3:].decode()
        new_path: Optional[str] = None

        # Renamed or copied files have the new path in the next entry
        if status and status[0] in {"R", "C"}:
            try:
                new_path = next(entries).decode()
            except StopIteration:
                pass

        changes.append((status, path, new_path))

    return changes


def is_tracked(path: str) -> bool:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def run_prettier(_: Iterable[str]) -> None:
    command = [
        "npx",
        "--yes",
        "prettier",
        "--write",
        "docs/**/*.md",
    ]

    subprocess.run(command, check=True)


def stage_paths(paths: Iterable[str]) -> None:
    run_prettier(paths)

    for path in sorted(set(paths)):
        if not path:
            continue
        try:
            run_git(["add", "--", path])
            continue
        except subprocess.CalledProcessError:
            pass

        tracked = is_tracked(path)
        exists = os.path.lexists(path)

        if tracked and not exists:
            run_git(["rm", "--cached", "--", path])
            continue

        if exists or tracked:
            run_git(["add", "-f", "--", path])
            continue

        run_git(["add", "--", path])


def has_staged_changes() -> bool:
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return diff.returncode == 1


def set_output(changes: bool) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as handle:
            handle.write(f"changes={'true' if changes else 'false'}\n")


def main() -> int:
    changes = parse_status()
    if not changes:
        print("No changes detected.")
        set_output(False)
        return 0

    run_git(["reset", "HEAD"])

    grouped: OrderedDict[Tuple[Optional[str], Optional[str]], Set[str]] = OrderedDict()
    for status, original_path, new_path in changes:
        reference_path = new_path or original_path
        group_key = determine_group(reference_path)
        if group_key not in grouped:
            grouped[group_key] = set()
        grouped[group_key].add(original_path)
        if new_path:
            grouped[group_key].add(new_path)

    total_commits = 0
    deferred: List[Tuple[Tuple[Optional[str], Optional[str]], Set[str]]] = []

    for key, paths in grouped.items():
        if key == (None, None):
            deferred.append((key, paths))
            continue
        service_slug, guide_slug = key
        stage_paths(paths)
        if not has_staged_changes():
            run_git(["reset", "HEAD"])
            continue
        service = prettify_slug(service_slug)
        guide = format_guide(guide_slug)
        if service and guide:
            message = f"Update to {service} {guide}"
        elif service:
            message = f"Update to {service} docs"
        else:
            message = "Update documentation"
        run_git(["commit", "-m", message])
        total_commits += 1

    for key, paths in deferred:
        stage_paths(paths)
        if not has_staged_changes():
            run_git(["reset", "HEAD"])
            continue
        run_git(["commit", "-m", "Update repository files"])
        total_commits += 1

    if total_commits == 0:
        print("No commits created.")
        set_output(False)
        return 0

    print(f"Created {total_commits} commit(s).")
    set_output(True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
