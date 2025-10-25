#!/usr/bin/env python3
"""Commit documentation changes grouped by service and guide."""
from __future__ import annotations

import os
import re
import subprocess
import sys
from collections import OrderedDict
from typing import Iterable, List, Optional, Set, Tuple

from git import Repo
from git.exc import GitCommandError


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


def parse_status(repo: Repo) -> List[Tuple[str, str, Optional[str]]]:
    """Parse git status using GitPython."""
    # Use git status --porcelain=1 -z for consistent output
    result = repo.git.status(porcelain=True, z=True)
    if not result:
        return []

    entries = result.encode().split(b"\0")
    changes: List[Tuple[str, str, Optional[str]]] = []
    i = 0
    while i < len(entries):
        entry = entries[i]
        if not entry:
            break
        status = entry[:2].decode()
        path = entry[3:].decode()
        new_path: Optional[str] = None
        if status and status[0] in {"R", "C"}:
            i += 1
            if i < len(entries):
                new_entry = entries[i]
                new_path = new_entry.decode()
        changes.append((status, path, new_path))
        i += 1
    return changes


def is_tracked(repo: Repo, path: str) -> bool:
    """Check if a path is tracked by git."""
    try:
        repo.git.ls_files(path, error_unmatch=True)
        return True
    except GitCommandError:
        return False


def run_prettier(_: Iterable[str]) -> None:
    command = [
        "npx",
        "--yes",
        "prettier",
        "--write",
        "docs/**/*.md",
    ]

    subprocess.run(command, check=True)


def stage_paths(repo: Repo, paths: Iterable[str]) -> None:
    """Stage paths for commit using GitPython."""
    run_prettier(paths)

    for path in sorted(set(paths)):
        if not path:
            continue
        try:
            repo.index.add([path])
            continue
        except GitCommandError:
            pass

        tracked = is_tracked(repo, path)
        exists = os.path.lexists(path)

        if tracked and not exists:
            repo.index.remove([path], cached=True)
            continue

        if exists or tracked:
            repo.index.add([path], force=True)
            continue

        repo.index.add([path])


def has_staged_changes(repo: Repo) -> bool:
    """Check if there are staged changes."""
    return len(repo.index.diff("HEAD")) > 0


def set_output(changes: bool) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as handle:
            handle.write(f"changes={'true' if changes else 'false'}\n")


def main() -> int:
    """Main function to process and commit documentation changes."""
    repo = Repo(".")

    changes = parse_status(repo)
    if not changes:
        print("No changes detected.")
        set_output(False)
        return 0

    repo.index.reset()

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
        stage_paths(repo, paths)
        if not has_staged_changes(repo):
            repo.index.reset()
            continue
        service = prettify_slug(service_slug)
        guide = format_guide(guide_slug)
        if service and guide:
            message = f"Update to {service} {guide}"
        elif service:
            message = f"Update to {service} docs"
        else:
            message = "Update documentation"
        repo.index.commit(message)
        total_commits += 1

    for key, paths in deferred:
        stage_paths(repo, paths)
        if not has_staged_changes(repo):
            repo.index.reset()
            continue
        repo.index.commit("Update repository files")
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
