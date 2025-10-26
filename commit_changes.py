#!/usr/bin/env python3
"""Commit documentation changes grouped by service and guide."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Sequence


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


def stage_service_by_pattern(service_id: str) -> None:
    """Stage all changes for a service using a file pattern."""
    pattern = f"docs/{service_id}/**"
    run_git(["add", "-A", "--", pattern])


def has_staged_changes() -> bool:
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return diff.returncode == 1


def set_output(changes: bool) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a", encoding="utf-8") as handle:
            handle.write(f"changes={'true' if changes else 'false'}\n")


def load_service_ids(manifest_path: Path) -> List[str]:
    """Load service IDs from the service manifest."""
    if not manifest_path.exists():
        print(f"Warning: Service manifest not found at {manifest_path}")
        return []

    with open(manifest_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    services = data.get("services", [])
    service_ids = [s.get("id") for s in services if s.get("id")]
    return service_ids


def main() -> int:
    manifest_path = Path("docs/service-manifest.json")

    # Reset any staged changes
    run_git(["reset", "HEAD"], check=False)

    # Run prettier once on all markdown files
    run_prettier_once()

    # Load service IDs from manifest
    service_ids = load_service_ids(manifest_path)
    if not service_ids:
        print("No services found in manifest.")
        set_output(False)
        return 0

    print(f"Processing {len(service_ids)} services...")
    total_commits = 0

    # Process each service
    for service_id in service_ids:
        # Stage all changes for this service
        stage_service_by_pattern(service_id)

        # Check if there are changes to commit
        if not has_staged_changes():
            continue

        # Create commit message
        service_name = prettify_slug(service_id)
        message = f"Update to {service_name} docs"

        try:
            run_git(["commit", "-m", message])
            total_commits += 1
            print(f"Committed changes for {service_name}")
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
