#!/usr/bin/env python3
"""Commit documentation changes grouped by service and guide."""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Sequence


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


def run_git(args: Sequence[str], *, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], check=check, text=True)


def prettify_slug(slug: str | None) -> str:
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


def run_prettier_once() -> None:
    """Run prettier once on all markdown files in docs/."""
    command = [
        "npx",
        "--yes",
        "prettier",
        "--write",
        "docs/**/*.md",
    ]
    print("Running Prettier on all documentation files...")
    subprocess.run(command, check=True)


def has_staged_changes() -> bool:
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return diff.returncode == 1


def set_output(changes: bool) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as handle:
            handle.write(f"changes={'true' if changes else 'false'}\n")


def discover_service_directories(docs_path: Path) -> List[str]:
    """Discover service directories by scanning the docs/ folder.

    Returns:
        List of service directory names (relative to docs/)
    """
    if not docs_path.exists() or not docs_path.is_dir():
        return []

    services = []
    for item in docs_path.iterdir():
        if item.is_dir() and item.name != "." and not item.name.startswith("."):
            # Skip README.md and other files
            if item.name not in ["README.md", "service-manifest.json"]:
                services.append(item.name)

    return sorted(services)


def main() -> int:
    docs_path = Path("docs")

    # Reset any staged changes
    run_git(["reset", "HEAD"], check=False)

    # Run prettier once on all markdown files
    run_prettier_once()

    # Discover service directories
    services = discover_service_directories(docs_path)
    if not services:
        print("No service directories found in docs/.")
    else:
        print(f"Found {len(services)} service directories: {', '.join(services)}")

    total_commits = 0

    # Process each service directory
    for service_dir in services:
        # Stage all changes for this service directory
        service_path = docs_path / service_dir
        pattern = f"docs/{service_dir}/**"

        # Stage the service directory
        run_git(["add", "-A", "--", pattern], check=False)

        # Check if there are changes to commit
        if not has_staged_changes():
            print(f"No changes for {service_dir}, skipping...")
            continue

        # Create commit message
        service_name = prettify_slug(service_dir)
        message = f"Add {service_name} documentation"

        try:
            run_git(["commit", "-m", message])
            total_commits += 1
            print(f"Committed changes for {service_name}")
        except subprocess.CalledProcessError:
            # No changes to commit or commit failed
            run_git(["reset", "HEAD"], check=False)
            continue

    # Commit any non-docs repository files (code, config, etc.)
    # Stage everything except docs/
    run_git(["add", "-A", "."], check=False)
    run_git(["reset", "HEAD", "docs/"], check=False)

    if has_staged_changes():
        try:
            run_git(["commit", "-m", "Update repository files"])
            total_commits += 1
            print("Committed non-documentation files")
        except subprocess.CalledProcessError:
            run_git(["reset", "HEAD"], check=False)

    if total_commits == 0:
        print("No commits created.")
        set_output(False)
        return 0

    print(f"Created {total_commits} commit(s).")
    set_output(True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
