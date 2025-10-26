#!/usr/bin/env python3
"""Commit documentation changes grouped by service and guide."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Sequence, Tuple


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


def stage_service_by_pattern(directories: List[str]) -> None:
    """Stage all changes for a service's directories using file patterns."""
    for directory in directories:
        dir_path = Path(f"docs/{directory}")
        if not dir_path.exists():
            # Skip directories that don't exist (e.g., when crawling single service)
            continue
        pattern = f"docs/{directory}/**"
        run_git(["add", "-A", "--", pattern])


def has_staged_changes() -> bool:
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return diff.returncode == 1


def set_output(changes: bool) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as handle:
            handle.write(f"changes={'true' if changes else 'false'}\n")


def load_services(manifest_path: Path) -> List[Tuple[str, List[str]]]:
    """Load services with their directory paths from the manifest.

    Returns:
        List of tuples (service_id, [directory_names])
    """
    if not manifest_path.exists():
        print(f"Warning: Service manifest not found at {manifest_path}")
        return []

    with open(manifest_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    services = data.get("services", [])
    result = []

    for service in services:
        service_id = service.get("id")
        if not service_id:
            continue

        # Extract unique directory names from guide paths
        directories = set()
        for guide in service.get("guides", []):
            prefix = guide.get("allowed_prefix", "")
            if prefix and prefix.startswith("/"):
                # Get first segment: /app2container/... -> app2container
                parts = prefix.lstrip("/").split("/")
                if parts and parts[0]:
                    directories.add(parts[0])

        if directories:
            result.append((service_id, sorted(directories)))

    return result


def main() -> int:
    manifest_path = Path("docs/service-manifest.json")

    # Reset any staged changes
    run_git(["reset", "HEAD"], check=False)

    # Run prettier once on all markdown files
    run_prettier_once()

    # Load services and their directories from manifest
    services = load_services(manifest_path)
    if not services:
        print("No services found in manifest.")
        set_output(False)
        return 0

    print(f"Processing {len(services)} services...")
    total_commits = 0

    # Process each service
    for service_id, directories in services:
        # Stage all changes for this service's directories
        stage_service_by_pattern(directories)

        # Check if there are changes to commit
        if not has_staged_changes():
            continue

        # Create commit message
        service_name = prettify_slug(service_id)
        message = f"Update to {service_name} docs"

        try:
            run_git(["commit", "-m", message])
            total_commits += 1
            print(f"Committed changes for {service_name} ({', '.join(directories)})")
        except subprocess.CalledProcessError:
            # No changes to commit or commit failed
            run_git(["reset", "HEAD"], check=False)
            continue

    # Commit any remaining non-docs files
    run_git(["add", "-A", "."], check=False)
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
