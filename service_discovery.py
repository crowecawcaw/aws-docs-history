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
    DEFAULT_LOCALE,
    ServiceGuide,
    derive_allowed_prefix,
    normalise_url,
)


LOGGER = logging.getLogger(__name__)
MODULE_ROOT = Path(__file__).resolve().parent

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


def _normalise_service_href(raw_href: str) -> Optional[str]:
    """Normalise the ``href`` from the main landing page to a service root."""

    if not raw_href:
        return None

    parsed = urlparse(urljoin(DOCS_BASE_URL, raw_href))
    if parsed.scheme not in {"http", "https"} or (
        parsed.netloc and parsed.netloc != DOCS_NETLOC
    ):
        return None

    service_segment = parsed.path.strip("/").split("/", 1)[0].strip("/")
    return f"/{service_segment}/" if service_segment else None


def parse_main_landing_page(xml_text: str) -> dict[str, str]:
    """Parse the AWS docs main landing XML into service roots."""

    soup = BeautifulSoup(xml_text, "html.parser")
    services: dict[str, str] = {}

    for item in soup.find_all("list-card-item"):
        if not (
            service_root := _normalise_service_href((item.get("href") or "").strip())
        ):
            continue

        identifier = (item.get("id") or service_root.strip("/")).strip().lower()
        if not identifier or _looks_like_non_service(identifier):
            continue

        services.setdefault(identifier, service_root)

    return services


def _looks_like_api_doc(title: str, href: str) -> bool:
    title_lower = title.lower()
    href_lower = href.lower()

    api_title_markers = (
        "api reference",
        "rest api reference",
        "http api reference",
        "websocket api reference",
        "sdk api reference",
    )

    if any(marker in title_lower for marker in api_title_markers):
        return True

    if any(token in href_lower for token in ("apireference", "api-reference", "/api/")):
        return True

    return False


def parse_service_landing_page(xml_text: str) -> list[ServiceGuide]:
    """Extract discoverable guides from a service landing page XML."""

    soup = BeautifulSoup(xml_text, "html.parser")
    guides: dict[str, ServiceGuide] = {}

    for element in soup.find_all(
        lambda tag: (tag.get("guide") or "").lower() == "true"
    ):
        if not (href := (element.get("href") or "").strip()):
            continue

        title_tag = element.find("title")
        title_text = title_tag.get_text(strip=True) if title_tag else href

        if _looks_like_api_doc(title_text, href):
            continue

        absolute_url = normalise_url(urljoin(DOCS_BASE_URL, href))
        if urlparse(absolute_url).netloc != DOCS_NETLOC:
            continue

        guides.setdefault(
            absolute_url,
            ServiceGuide(
                title=title_text,
                url=absolute_url,
                allowed_prefix=derive_allowed_prefix(absolute_url),
            ),
        )

    return sorted(guides.values(), key=lambda guide: guide.url)


def discover_service_guides(
    *,
    session: Optional[requests.Session] = None,
    main_landing_url: str = f"{DOCS_BASE_URL}/{DEFAULT_LOCALE}/main-landing-page.xml",
) -> dict[str, tuple[ServiceGuide, ...]]:
    """Discover documentation guides for all AWS services."""

    owns_session = session is None
    http = session or requests.Session()

    response = http.get(main_landing_url, timeout=30)
    response.raise_for_status()

    services = parse_main_landing_page(response.text)
    guides_by_service: dict[str, tuple[ServiceGuide, ...]] = {}

    for service_id, service_root in sorted(services.items()):
        landing_url = urljoin(DOCS_BASE_URL, f"{service_root}{DEFAULT_LOCALE}/landing-page.xml")

        landing_response = http.get(landing_url, timeout=30)
        if landing_response.status_code == 404:
            LOGGER.debug("Skipping %s because %s returned 404", service_id, landing_url)
            continue
        landing_response.raise_for_status()

        guides = parse_service_landing_page(landing_response.text)
        if not guides:
            LOGGER.debug("No guides discovered for %s", service_id)
            continue

        guides_by_service[service_id] = tuple(guides)

    if owns_session:
        http.close()

    return guides_by_service


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


def _extract_service_segment(url: str) -> Optional[str]:
    """Extract the service segment from a documentation URL."""
    path = urlparse(url).path.strip("/")
    parts = path.split("/")
    return parts[0] if parts else None


def _derive_service_name(service_id: str, guides: Sequence[ServiceGuide]) -> str:
    """Derive a display name for the service from guide titles."""
    import re
    from collections import Counter

    titles = [guide.title for guide in guides]
    service_names = []

    # Try to find AWS/Amazon service name in titles
    for title in titles:
        # Remove common suffixes that aren't part of the service name
        clean_title = re.sub(
            r'\s+(User Guide|Developer Guide|Reference Guide|API Reference|section of.*|in the.*|for.*)$',
            '',
            title,
            flags=re.IGNORECASE
        )

        # Match patterns like "AWS X" or "Amazon X"
        match = re.search(
            r'\b(AWS|Amazon)\s+([A-Z][A-Za-z0-9]+(?:\s+[A-Z][A-Za-z0-9]+)*)',
            clean_title
        )
        if match:
            service_names.append(f"{match.group(1)} {match.group(2)}")

    # Use the most common service name
    if service_names:
        return Counter(service_names).most_common(1)[0][0]

    # Fallback: derive from the primary service segment
    segments = [_extract_service_segment(guide.url) for guide in guides]

    # Skip generic segments that don't represent the service
    preferred_segments = [
        seg for seg in segments
        if seg and seg not in {'cli'}
    ]

    if preferred_segments:
        segment = sorted(preferred_segments)[0]

        # Handle camelCase segments (e.g., "AmazonS3" -> "Amazon S3", "AWSCloudFormation" -> "AWS CloudFormation")
        if not re.search(r'[-_]', segment):
            # First, handle the AWS/Amazon prefix
            if segment.startswith('AWS'):
                # Extract "AWS" and process the rest
                rest = segment[3:]
                if rest:
                    # Insert spaces before capital letters in the rest
                    rest_spaced = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', rest)
                    return f'AWS {rest_spaced}'
                return 'AWS'
            elif segment.startswith('Amazon'):
                # Extract "Amazon" and process the rest
                rest = segment[6:]
                if rest:
                    # Insert spaces before capital letters in the rest
                    rest_spaced = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', rest)
                    return f'Amazon {rest_spaced}'
                return 'Amazon'
            else:
                # General case: insert spaces before capital letters
                return re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', segment)

        # Handle hyphenated/underscored segments (e.g., "deadline-cloud" -> "Deadline Cloud")
        return segment.replace("-", " ").replace("_", " ").title()

    # Final fallback: capitalize the service ID
    return service_id.replace("-", " ").replace("_", " ").title()


def _build_manifest(
    guides_by_service: Mapping[str, Sequence[ServiceGuide]],
) -> dict[str, object]:
    services: list[dict[str, object]] = []

    for service_id, guides in sorted(guides_by_service.items()):
        serialised_guides = [
            _guide_to_dict(guide) for guide in sorted(guides, key=lambda guide: guide.url)
        ]

        # Extract service name and segments
        service_name = _derive_service_name(service_id, guides)
        segments = sorted(set(
            seg for guide in guides
            if (seg := _extract_service_segment(guide.url)) is not None
        ))

        services.append({
            "id": service_id,
            "name": service_name,
            "segments": segments,
            "guides": serialised_guides,
        })

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
