"""Shared AWS documentation utilities used by the crawler and discovery tools."""

from __future__ import annotations

from dataclasses import dataclass
import posixpath
from urllib.parse import urlparse, urlunparse


DOCS_BASE_URL = "https://docs.aws.amazon.com"
DEFAULT_LOCALE = "en_us"
DOCS_NETLOC = urlparse(DOCS_BASE_URL).netloc


@dataclass(frozen=True)
class ServiceGuide:
    """Represent a single documentation guide for a service."""

    title: str
    url: str
    allowed_prefix: str


@dataclass(frozen=True)
class ServiceScope:
    """Describe the default crawl scope for a single AWS service."""

    guides: tuple[ServiceGuide, ...]

    @property
    def start_urls(self) -> tuple[str, ...]:
        return tuple(guide.url for guide in self.guides)

    @property
    def allowed_prefixes(self) -> tuple[str, ...]:
        return tuple(sorted({guide.allowed_prefix for guide in self.guides}))


def normalise_url(url: str) -> str:
    """Normalise a URL by removing fragments and redundant path segments."""

    parsed = urlparse(url)
    cleaned_path = posixpath.normpath(parsed.path or "/")
    if parsed.path.endswith("/") and not cleaned_path.endswith("/"):
        cleaned_path += "/"

    cleaned = parsed._replace(path=cleaned_path, fragment="", query="")
    return urlunparse(cleaned)


def derive_allowed_prefix(url: str) -> str:
    """Derive the crawl prefix for ``url`` by trimming to the containing folder."""

    path = urlparse(url).path or "/"
    normalized = "/" + path.lstrip("/")
    directory = normalized if normalized.endswith("/") else posixpath.dirname(normalized)
    directory = directory or "/"

    if directory != "/" and not directory.endswith("/"):
        directory = directory.rstrip("/") + "/"

    return directory

