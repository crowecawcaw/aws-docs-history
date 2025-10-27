"""Service discovery functions for AWS documentation.

This module contains legacy functions used by tests to parse AWS landing pages
and manifests.
"""

from __future__ import annotations

from typing import Optional
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from aws_docs import (
    DOCS_BASE_URL,
    DOCS_NETLOC,
    ServiceGuide,
    derive_allowed_prefix,
    normalise_url,
)


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
    """Check if a guide looks like an API reference."""
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
