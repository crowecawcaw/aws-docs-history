"""Generate the service manifest consumed by the documentation crawler."""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Optional, Sequence
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from aws_docs import (
    DOCS_BASE_URL,
    DOCS_NETLOC,
    ServiceGuide,
    derive_allowed_prefix,
    normalise_url,
)


LOGGER = logging.getLogger(__name__)
MODULE_ROOT = Path(__file__).resolve().parent

# Sitemap URLs
SITEMAP_INDEX_URL = f"{DOCS_BASE_URL}/sitemap_index.xml"

_NON_SERVICE_PATTERNS = {
    "identifiers": {
        "abap-sdk",
        "cli",
        "cpp",
        "go",
        "java",
        "net",
        "php",
        "powershell",
        "python3",
        "pythonsdk",
        "ruby",
        "sdk-for-cpp",
        "sdk-for-go",
        "sdk-for-java",
        "sdk-for-javascript",
        "sdk-for-kotlin",
        "sdk-for-net",
        "sdk-for-php",
        "sdk-for-ruby",
        "sdk-for-rust",
        "sdk-for-sapabap",
        "sdk-for-swift",
        "sdk-for-unity",
        "sdkforkotlin",
    },
    "prefixes": ("sdk-for-", "aws-sdk-", "tk-"),
    "substrings": ("toolkit",),
}

# Guide types we want to include (excluding API references)
_INCLUDED_GUIDE_TYPES = {
    "userguide",
    "developerguide",
    "adminguide",
    "dg",
    "ug",
}


def _looks_like_non_service(identifier: str) -> bool:
    """Return ``True`` when the manifest identifier is not an AWS service."""
    normalised = identifier.strip().lower()
    if not normalised:
        return False

    return (
        normalised in _NON_SERVICE_PATTERNS["identifiers"]
        or any(normalised.startswith(p) for p in _NON_SERVICE_PATTERNS["prefixes"])
        or any(s in normalised for s in _NON_SERVICE_PATTERNS["substrings"])
    )


def _looks_like_api_doc(guide_segment: str) -> bool:
    """Check if a guide segment looks like an API reference."""
    guide_lower = guide_segment.lower()

    api_markers = (
        "apireference",
        "api-reference",
        "apiref",
        "api",
    )

    return any(marker in guide_lower for marker in api_markers)


def _parse_sitemap_url(sitemap_url: str) -> Optional[tuple[str, str, str, str]]:
    """Parse a sitemap URL to extract service, version, guide type.

    Returns: (service_id, version, guide_type, base_url) or None
    """
    parsed = urlparse(sitemap_url)
    if parsed.netloc != DOCS_NETLOC:
        return None

    # Expected pattern: /service/version/guide-type/sitemap.xml
    parts = [p for p in parsed.path.strip("/").split("/") if p]

    if len(parts) < 4 or parts[-1] != "sitemap.xml":
        return None

    service_segment = parts[0]
    version = parts[1]
    guide_segment = parts[2]

    # Only include "latest" versions for now
    if version.lower() != "latest":
        return None

    # Filter out API references
    if _looks_like_api_doc(guide_segment):
        return None

    # Filter out SDKs and toolkits
    if _looks_like_non_service(service_segment):
        return None

    # Build the base URL for this guide
    base_url = f"{DOCS_BASE_URL}/{service_segment}/{version}/{guide_segment}/"

    # Normalize service ID
    service_id = service_segment.lower().replace("_", "-")

    return service_id, version, guide_segment, base_url


def _derive_guide_title(service_id: str, guide_segment: str) -> str:
    """Generate a human-readable guide title."""
    guide_type_map = {
        "userguide": "User Guide",
        "developerguide": "Developer Guide",
        "adminguide": "Administrator Guide",
        "dg": "Developer Guide",
        "ug": "User Guide",
    }

    guide_type = guide_type_map.get(guide_segment.lower(), guide_segment.title())
    service_name = service_id.replace("-", " ").title()

    return f"{service_name} {guide_type}"


def discover_service_guides_from_sitemap(
    *,
    session: Optional[requests.Session] = None,
    sitemap_index_url: str = SITEMAP_INDEX_URL,
) -> dict[str, tuple[ServiceGuide, ...]]:
    """Discover documentation guides for all AWS services from sitemap index."""

    owns_session = session is None
    http = session or requests.Session()

    try:
        LOGGER.info("Fetching sitemap index from %s", sitemap_index_url)
        response = http.get(sitemap_index_url, timeout=30)
        response.raise_for_status()

        # Parse sitemap index XML
        soup = BeautifulSoup(response.text, "xml")

        guides_by_service: dict[str, list[ServiceGuide]] = {}

        # Extract all sitemap URLs
        for loc in soup.find_all("loc"):
            sitemap_url = loc.get_text().strip()

            parsed = _parse_sitemap_url(sitemap_url)
            if not parsed:
                continue

            service_id, version, guide_segment, base_url = parsed

            # Create a ServiceGuide for this guide
            guide = ServiceGuide(
                title=_derive_guide_title(service_id, guide_segment),
                url=normalise_url(base_url),
                allowed_prefix=derive_allowed_prefix(base_url),
            )

            guides_by_service.setdefault(service_id, []).append(guide)

        # Convert lists to sorted tuples
        result: dict[str, tuple[ServiceGuide, ...]] = {}
        for service_id, guides in guides_by_service.items():
            result[service_id] = tuple(sorted(guides, key=lambda g: g.url))

        LOGGER.info("Discovered %d services with %d total guides",
                   len(result), sum(len(guides) for guides in result.values()))

        return result

    finally:
        if owns_session:
            http.close()


def discover_pages_from_sitemap(
    sitemap_url: str,
    *,
    session: Optional[requests.Session] = None,
) -> list[str]:
    """Discover all HTML page URLs from a service sitemap.

    Args:
        sitemap_url: URL to the sitemap.xml file for a service guide
        session: Optional requests session to reuse

    Returns:
        List of normalized HTML page URLs
    """
    owns_session = session is None
    http = session or requests.Session()

    try:
        LOGGER.debug("Fetching sitemap from %s", sitemap_url)
        response = http.get(sitemap_url, timeout=30)
        response.raise_for_status()

        # Parse sitemap XML
        soup = BeautifulSoup(response.text, "xml")

        pages: list[str] = []

        # Extract all URLs from <loc> tags
        for loc in soup.find_all("loc"):
            url = loc.get_text().strip()
            if not url:
                continue

            # Validate and normalize the URL
            parsed = urlparse(url)
            if parsed.netloc != DOCS_NETLOC:
                continue

            # Only include HTML pages
            if url.endswith((".html", ".htm")) or url.endswith("/"):
                pages.append(normalise_url(url))

        LOGGER.info("Discovered %d pages from %s", len(pages), sitemap_url)
        return pages

    except requests.RequestException as exc:
        LOGGER.warning("Failed to fetch sitemap %s: %s", sitemap_url, exc)
        return []

    finally:
        if owns_session:
            http.close()


def build_sitemap_url_from_guide(guide_url: str) -> str:
    """Build the sitemap URL from a guide's base URL.

    Args:
        guide_url: Base URL of a guide (e.g., https://docs.aws.amazon.com/service/latest/userguide/)

    Returns:
        URL to the guide's sitemap.xml
    """
    parsed = urlparse(guide_url)
    path = parsed.path.rstrip("/")
    sitemap_path = f"{path}/sitemap.xml"

    return urlunparse(parsed._replace(path=sitemap_path))


# Keep the old function for backward compatibility but mark as deprecated
def discover_service_guides(
    *,
    session: Optional[requests.Session] = None,
    main_landing_url: str = None,
) -> dict[str, tuple[ServiceGuide, ...]]:
    """Discover documentation guides for all AWS services.

    DEPRECATED: Use discover_service_guides_from_sitemap() instead.
    This function is maintained for backward compatibility only.
    """
    LOGGER.warning("discover_service_guides() is deprecated, use discover_service_guides_from_sitemap()")
    return discover_service_guides_from_sitemap(session=session)


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
        default=MODULE_ROOT / "docs/service-manifest.json",
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

    LOGGER.info("Discovering AWS documentation services from sitemap...")
    guides = discover_service_guides_from_sitemap()
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
