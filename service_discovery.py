"""Generate the service manifest consumed by the documentation crawler."""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Sequence

from crawler import ServiceGuide, discover_service_guides


LOGGER = logging.getLogger(__name__)


def _format_timestamp(timestamp: datetime) -> str:
    return timestamp.astimezone(timezone.utc).replace(tzinfo=timezone.utc).isoformat().replace(
        "+00:00", "Z"
    )


def _guide_to_dict(guide: ServiceGuide) -> dict[str, str]:
    return {
        "title": guide.title,
        "url": guide.url,
        "allowed_prefix": guide.allowed_prefix,
    }


def _build_manifest(
    guides_by_service: Mapping[str, Sequence[ServiceGuide]],
) -> dict[str, object]:
    services: list[dict[str, object]] = []

    for service_id, guides in sorted(guides_by_service.items()):
        serialised_guides = [
            _guide_to_dict(guide) for guide in sorted(guides, key=lambda guide: guide.url)
        ]
        services.append({"id": service_id, "guides": serialised_guides})

    manifest = {
        "generated_at": _format_timestamp(datetime.now(timezone.utc)),
        "services": services,
    }

    return manifest


def _ensure_manifest_written(path: Path, manifest: dict[str, object]) -> bool:
    """Write ``manifest`` to ``path`` if it has changed."""

    rendered = json.dumps(manifest, indent=2, sort_keys=False) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)

    existing = None
    if path.exists():
        existing = path.read_text(encoding="utf-8")

    if existing == rendered:
        LOGGER.info("Service manifest is already up to date at %s", path)
        return False

    path.write_text(rendered, encoding="utf-8")
    LOGGER.info("Wrote updated service manifest to %s", path)
    return True


def _commit_manifest(path: Path) -> bool:
    """Commit the manifest file if staged changes are present."""

    subprocess.run(["git", "add", "--", str(path)], check=True)
    status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if status.returncode == 0:
        LOGGER.info("No staged manifest changes detected; skipping commit.")
        subprocess.run(["git", "reset", "HEAD", "--", str(path)], check=True)
        return False

    subprocess.run(["git", "commit", "-m", "Update service manifest"], check=True)
    LOGGER.info("Committed service manifest changes.")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Discover AWS documentation services and write a manifest."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/service-manifest.json"),
        help="Where the manifest JSON file should be written.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Python logging level (e.g. INFO, DEBUG).",
    )
    parser.add_argument(
        "--no-commit",
        action="store_true",
        help="Write the manifest without creating a Git commit.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level.upper(), logging.INFO))

    LOGGER.info("Discovering AWS documentation services...")
    guides = discover_service_guides()
    LOGGER.info("Discovered %d services", len(guides))

    manifest = _build_manifest(guides)
    changed = _ensure_manifest_written(args.output, manifest)

    if not changed:
        LOGGER.info("Manifest unchanged; nothing to do.")
        return

    if args.no_commit:
        LOGGER.info("Manifest updated without committing per --no-commit flag.")
        return

    try:
        committed = _commit_manifest(args.output)
    except subprocess.CalledProcessError as exc:  # pragma: no cover - defensive logging
        LOGGER.error("Failed to commit manifest changes: %s", exc)
        raise

    if committed:
        LOGGER.info("Service manifest changes committed successfully.")


if __name__ == "__main__":
    main()
