"""AWS documentation crawler using sitemap-based discovery.

This crawler downloads AWS documentation pages and converts them to Markdown.
It uses AWS's sitemap.xml files to discover all services and pages.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import logging
import os
import posixpath
import queue
import re
import shutil
import subprocess
import sys
import threading
import time
import xml.etree.ElementTree as ET
from pathlib import Path, PurePosixPath
from typing import Optional
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup, Tag
import markdownify

from aws_docs import (
    DOCS_BASE_URL,
    DOCS_NETLOC,
    derive_allowed_prefix,
    normalise_url,
)

CONTENT_SELECTORS = [
    "main",
    "article",
    "#main-content",
    ".main-content",
    "#content",
    ".content",
    "div[role='main']",
    "#awsdocs-content",
    ".awsui-article",
]

NAVIGATION_SELECTORS = [
    "noscript",
    ".prev-next",
    "#main-col-footer",
    ".awsdocs-page-utilities",
    "#quick-feedback-yes",
    "#quick-feedback-no",
    ".page-loading-indicator",
    "#tools-panel",
    ".doc-cookie-banner",
    "awsdocs-copyright",
    "awsdocs-thumb-feedback",
]

TAGS_TO_STRIP = [
    "script",
    "style",
    "noscript",
    "meta",
    "link",
    "footer",
    "nav",
    "aside",
    "header",
    "awsdocs-cookie-consent-container",
    "awsdocs-feedback-container",
    "awsdocs-page-header",
    "awsdocs-page-header-container",
    "awsdocs-filter-selector",
    "awsdocs-breadcrumb-container",
    "awsdocs-page-footer",
    "awsdocs-page-footer-container",
    "awsdocs-footer",
    "awsdocs-cookie-banner",
    "js-show-more-buttons",
    "js-show-more-text",
    "feedback-container",
    "feedback-section",
    "doc-feedback-container",
    "doc-feedback-section",
    "warning-container",
    "warning-section",
    "cookie-banner",
    "cookie-notice",
    "copyright-section",
    "legal-section",
    "terms-section",
]

LOGGER = logging.getLogger(__name__)

MODULE_ROOT = Path(__file__).resolve().parent

IMAGE_HOST = "docs.aws.amazon.com"
IMAGE_PATH_PREFIX = "/images/"
ALLOWED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg"}
MAX_IMAGE_BYTES = 10 * 1024 * 1024  # 10 MiB safeguard

SITEMAP_INDEX_URL = f"{DOCS_BASE_URL}/sitemap_index.xml"

# Patterns to exclude
NON_SERVICE_PATTERNS = {
    "identifiers": {
        "abap-sdk", "cli", "cpp", "go", "java", "net", "php", "powershell",
        "python3", "pythonsdk", "ruby", "sdk-for-cpp", "sdk-for-go",
        "sdk-for-java", "sdk-for-javascript", "sdk-for-kotlin", "sdk-for-net",
        "sdk-for-php", "sdk-for-ruby", "sdk-for-rust", "sdk-for-sapabap",
        "sdk-for-swift", "sdk-for-unity", "sdkforkotlin",
        # Additional SDK-related services
        "awsjavasdk", "xray-sdk-for-java", "cdi-sdk", "database-encryption-sdk",
        "encryption-sdk", "embedded-csdk", "amazon-s3-encryption-client",
        "cloudformation-cli", "sdkref",
        # Toolkits
        "toolkit-for-jetbrains", "toolkit-for-visual-studio", "toolkit-for-vscode",
        "tk-dotnet-refactoring",
        # CLI tools
        "cli", "aws-cli",
        # Non-service documentation types
        "prescriptive-guidance", "solutions", "whitepapers", "decision-guides",
        # Code examples and reference implementations (high volume, low value)
        "freertos", "code-library",
    },
    "prefixes": ("sdk-for-", "aws-sdk-", "tk-", "toolkit-"),
    "substrings": ("toolkit", "-sdk", "-cli"),
}


def build_local_image_path(image_path: str, output_root: Path) -> Path:
    """Translate an AWS Docs image path into a local filesystem destination."""
    if not image_path.startswith(IMAGE_PATH_PREFIX):
        raise ValueError(f"Image path must start with {IMAGE_PATH_PREFIX!r}: {image_path!r}")

    relative_path = image_path[len(IMAGE_PATH_PREFIX):]
    safe_parts = [
        part for part in PurePosixPath(relative_path).parts
        if part not in {"..", "."}
    ]

    if not safe_parts:
        raise ValueError(f"Image path did not contain any usable segments: {image_path!r}")

    return output_root.joinpath(*safe_parts)


def looks_like_non_service(identifier: str) -> bool:
    """Return True when the identifier is not an AWS service."""
    normalised = identifier.strip().lower()
    if not normalised:
        return False

    return (
        normalised in NON_SERVICE_PATTERNS["identifiers"]
        or any(normalised.startswith(p) for p in NON_SERVICE_PATTERNS["prefixes"])
        or any(s in normalised for s in NON_SERVICE_PATTERNS["substrings"])
    )


def looks_like_api_doc(guide_segment: str) -> bool:
    """Check if a guide segment looks like an API reference."""
    guide_lower = guide_segment.lower()
    api_markers = ("apireference", "api-reference", "apiref", "api")
    return any(marker in guide_lower for marker in api_markers)


def looks_like_unwanted_guide(guide_segment: str) -> bool:
    """Check if a guide segment is an unwanted/autogenerated type."""
    guide_lower = guide_segment.lower()
    unwanted_guides = (
        "javadoc",       # Java API documentation
        "site_map",      # CloudFormation autogenerated resource docs
        "cli",           # CLI documentation
        "sdk",           # SDK documentation
    )
    return any(unwanted in guide_lower for unwanted in unwanted_guides)


class RequestRateLimiter:
    """Coordinate request throttling across multiple worker threads."""

    def __init__(self, requests_per_second: Optional[float]) -> None:
        if requests_per_second is None or requests_per_second <= 0:
            self._min_interval = None
        else:
            self._min_interval = 1.0 / requests_per_second
        self._lock = threading.Lock()
        self._next_allowed = time.monotonic()

    def acquire(self) -> None:
        if self._min_interval is None:
            return

        while True:
            with self._lock:
                now = time.monotonic()
                if now >= self._next_allowed:
                    self._next_allowed = now + self._min_interval
                    return
                delay = self._next_allowed - now
            time.sleep(delay)


class LinkChecker:
    """Determine whether a link should be crawled."""

    def __init__(self, allowed_prefixes: Optional[list[str]] = None) -> None:
        self.allowed_schemes = {"http", "https"}
        self.disallowed_suffixes = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".svg", ".xml"}
        self.html_suffixes = ("/", ".html", ".htm")
        raw_prefixes = list(allowed_prefixes or [])
        self.prefixes = [
            prefix if prefix.startswith("/") else f"/{prefix.lstrip('/')}"
            for prefix in raw_prefixes if prefix
        ]

    def __call__(self, url: str) -> bool:
        """Check if the URL should be visited."""
        parsed = urlparse(url)
        if parsed.scheme not in self.allowed_schemes:
            return False
        if not parsed.netloc or parsed.netloc != DOCS_NETLOC:
            return False
        if self.prefixes and not any(parsed.path.startswith(prefix) for prefix in self.prefixes):
            return False
        lower_path = parsed.path.lower()
        if any(lower_path.endswith(suffix) for suffix in self.disallowed_suffixes):
            return False
        if lower_path and not lower_path.endswith(self.html_suffixes):
            return False
        return True


def extract_main_content(soup: BeautifulSoup) -> Tag:
    """Extract the main documentation content from the parsed HTML page."""
    main = (
        next(
            (
                candidate
                for selector in CONTENT_SELECTORS
                if (candidate := soup.select_one(selector))
            ),
            None,
        )
        or soup.body
        or soup
    )

    for selector in NAVIGATION_SELECTORS:
        for element in main.select(selector):
            element.decompose()

    return main


class AwsDocsMarkdownConverter(markdownify.MarkdownConverter):
    """Custom markdownify converter that handles complex table cells.

    AWS documentation tables often contain multi-paragraph content and lists
    within cells. The default markdownify converter breaks these across
    multiple lines, creating invalid markdown tables. This custom converter
    keeps all cell content on a single line by:
    1. Removing newlines from cell content
    2. Converting list markers (* -) to <br>• for readability
    3. Separating paragraphs with <br> to maintain visual structure
    """

    def convert_td(self, el, text, convert_as_inline):
        """Convert table data cell, cleaning multi-line content."""
        text = self._clean_cell_text(text)
        return ' ' + text + ' |'

    def convert_th(self, el, text, convert_as_inline):
        """Convert table header cell, cleaning multi-line content."""
        text = self._clean_cell_text(text)
        return ' ' + text + ' |'

    def _clean_cell_text(self, text):
        """Clean cell text, using <br> to separate paragraphs and list items."""
        if not text:
            return ''

        # First split by newlines, then handle lines that have list markers mid-line
        lines = text.split('\n')
        result_parts = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Check if line starts with a list marker
            if line.startswith('* ') or line.startswith('- '):
                item_text = line[2:].strip()
                if result_parts:
                    result_parts.append('<br>• ' + item_text)
                else:
                    result_parts.append('• ' + item_text)
            # Check if line contains list markers mid-line (markdownify sometimes does this)
            elif '* ' in line or '- ' in line:
                # Split on list markers and process each part
                import re
                # Split on * or - followed by space, keeping the delimiter pattern
                parts = re.split(r'(\* |- )', line)
                for i, part in enumerate(parts):
                    if not part or part in ('* ', '- '):
                        continue
                    if i > 0 and parts[i-1] in ('* ', '- '):
                        # This is a list item
                        if result_parts:
                            result_parts.append('<br>• ' + part.strip())
                        else:
                            result_parts.append('• ' + part.strip())
                    else:
                        # Regular text
                        if result_parts:
                            result_parts.append('<br>' + part.strip())
                        else:
                            result_parts.append(part.strip())
            else:
                # Regular paragraph - use <br> separator if not first
                if result_parts:
                    result_parts.append('<br>' + line)
                else:
                    result_parts.append(line)

        # Join without spaces since <br> handles separation
        return ''.join(result_parts)


def convert_html_to_markdown(html: str) -> str:
    """Convert HTML content to Markdown using custom AWS docs converter."""
    content = AwsDocsMarkdownConverter(
        heading_style=markdownify.ATX,
        autolinks=True,
        default_title=True,
        escape_asterisks=True,
        escape_underscores=True,
        newline_style="SPACES",
        strip=TAGS_TO_STRIP,
    ).convert(html)

    if not content:
        return ""

    return content.strip() + "\n"


def url_to_output_path(url: str, output_root: Optional[Path] = None) -> Path:
    """Translate a documentation URL into a Markdown output path."""
    parsed = urlparse(url)
    path = parsed.path.lstrip("/").rstrip("/")

    if not path:
        path = "index"
    if path.endswith(".html"):
        path = path[:-5]

    parts = [part for part in path.split("/") if part]
    if not parts:
        parts = ["index"]

    relative_path = Path(*parts).with_suffix(".md")
    return output_root / relative_path if output_root else relative_path


def convert_tag_to_markdown(
    url: str,
    main: Tag,
    *,
    output_path: Path,
    output_root: Path,
) -> str:
    """Convert an extracted HTML fragment into Markdown."""
    for anchor in main.find_all("a"):
        if anchor.find_parent(["code", "pre"]):
            anchor.replace_with(anchor.get_text())

    rewrite_doc_links(main, url, base_output=output_path, output_root=output_root)
    markdown = convert_html_to_markdown(str(main))
    return markdown


def rewrite_doc_links(
    container: Tag,
    base_url: str,
    *,
    base_output: Path,
    output_root: Path,
) -> None:
    """Rewrite internal documentation links to point at local Markdown files."""
    base_host = urlparse(base_url).netloc

    for anchor in container.find_all("a", href=True):
        href = anchor["href"].strip()

        if not href or href.startswith("#") or href.startswith("mailto:"):
            continue

        absolute = urljoin(base_url, href)
        parsed = urlparse(absolute)

        if parsed.netloc != base_host:
            continue

        fragment = parsed.fragment
        cleaned = urlunparse(parsed._replace(fragment="", query=""))
        cleaned = normalise_url(cleaned)

        target_output = url_to_output_path(cleaned, output_root)
        relative_path = os.path.relpath(target_output, start=base_output.parent)
        relative_href = Path(relative_path).as_posix()

        if fragment:
            relative_href = f"{relative_href}#{fragment}"

        anchor["href"] = relative_href


class ImageHandler:
    """Handle image downloading and rewriting for documentation pages."""

    def __init__(
        self,
        output_dir: Path,
        session: requests.Session,
        rate_limiter: RequestRateLimiter,
    ) -> None:
        self.output_dir = output_dir
        self.session = session
        self.rate_limiter = rate_limiter
        self._downloaded_images: set[str] = set()
        self._lock = threading.Lock()

    def download_and_rewrite_images(
        self, container: Tag, page_url: str, page_output: Path
    ) -> None:
        """Download images and rewrite their references in the HTML container."""
        for image in container.find_all("img"):
            sources: list[str] = []
            raw_src = ""
            for attr in ("src", "data-src", "data-awsdocs-src"):
                value = image.get(attr)
                if isinstance(value, str):
                    stripped = value.strip()
                    if stripped:
                        raw_src = raw_src or stripped
                        sources.append(attr)

            if not raw_src:
                continue

            rewritten = self._rewrite_single_image(raw_src, page_url, page_output)
            if rewritten:
                for attr in sources or ["src"]:
                    image[attr] = rewritten

    def _rewrite_single_image(
        self, raw_src: str, page_url: str, page_output: Path
    ) -> Optional[str]:
        """Download an image and return the rewritten relative path."""
        absolute_url = normalise_url(urljoin(page_url, raw_src))
        parsed = urlparse(absolute_url)

        if parsed.scheme not in {"http", "https"}:
            return None
        if parsed.netloc != IMAGE_HOST:
            return None
        if not parsed.path.startswith(IMAGE_PATH_PREFIX):
            return None

        extension = Path(parsed.path).suffix.lower()
        if extension not in ALLOWED_IMAGE_EXTENSIONS:
            return None

        local_path = build_local_image_path(parsed.path, self.output_dir)
        if not self._download_image(absolute_url, local_path):
            return None

        relative_path = os.path.relpath(local_path, start=page_output.parent)
        return Path(relative_path).as_posix()

    def _download_image(self, image_url: str, destination: Path) -> bool:
        destination.parent.mkdir(parents=True, exist_ok=True)

        if destination.exists():
            return True

        with self._lock:
            if image_url in self._downloaded_images:
                return destination.exists()
            self._downloaded_images.add(image_url)

        try:
            self.rate_limiter.acquire()
            response = self.session.get(image_url, stream=True, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            LOGGER.warning("Failed to download image %s: %s", image_url, exc)
            with self._lock:
                self._downloaded_images.discard(image_url)
            return False

        content_length = response.headers.get("Content-Length")
        if content_length:
            try:
                if int(content_length) > MAX_IMAGE_BYTES:
                    LOGGER.warning(
                        "Skipping image %s because it exceeds the %d byte limit",
                        image_url,
                        MAX_IMAGE_BYTES,
                    )
                    with self._lock:
                        self._downloaded_images.discard(image_url)
                    response.close()
                    return False
            except ValueError:
                pass

        bytes_written = 0
        try:
            with destination.open("wb") as handle:
                for chunk in response.iter_content(chunk_size=8192):
                    if not chunk:
                        continue
                    bytes_written += len(chunk)
                    if bytes_written > MAX_IMAGE_BYTES:
                        LOGGER.warning(
                            "Skipping image %s because it exceeded the %d byte limit while downloading",
                            image_url,
                            MAX_IMAGE_BYTES,
                        )
                        response.close()
                        handle.close()
                        destination.unlink(missing_ok=True)
                        with self._lock:
                            self._downloaded_images.discard(image_url)
                        return False
                    handle.write(chunk)
        finally:
            response.close()

        return True


class AwsDocsCrawler:
    """Multi-threaded crawler for AWS documentation using sitemaps."""

    def __init__(
        self,
        output_dir: Path,
        max_workers: int = 8,
        session: Optional[requests.Session] = None,
        requests_per_second: Optional[float] = 10.0,
    ) -> None:
        self.output_dir = output_dir
        self.max_workers = max_workers
        self.session = session or requests.Session()

        self.session.headers.setdefault(
            "User-Agent",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/121.0 Safari/537.36",
        )

        self._url_queue: queue.Queue[str | None] = queue.Queue()
        self._known_urls: set[str] = set()
        self._known_urls_lock = threading.Lock()
        self._visited_urls: set[str] = set()

        self._rate_limiter = RequestRateLimiter(requests_per_second)
        self._image_handler = ImageHandler(output_dir, self.session, self._rate_limiter)

        # Link checker and service URL filter (set per-guide during processing)
        self._link_checker: Optional[LinkChecker] = None
        self._service_url_prefix: Optional[str] = None

    @property
    def visited_urls(self) -> list[str]:
        with self._known_urls_lock:
            return list(self._visited_urls)

    def discover_services(self) -> list[dict]:
        """Discover all services from sitemap index and return metadata."""
        LOGGER.info("Fetching sitemap index from %s", SITEMAP_INDEX_URL)

        try:
            self._rate_limiter.acquire()
            response = self.session.get(SITEMAP_INDEX_URL, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            LOGGER.error("Failed to fetch sitemap index: %s", exc)
            return []

        try:
            root = ET.fromstring(response.text)
        except ET.ParseError as exc:
            LOGGER.error("Failed to parse sitemap index XML: %s", exc)
            return []

        # Extract all sitemap URLs
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = root.findall(".//sm:loc", ns)
        if not locs:
            locs = root.findall(".//loc")

        services = []
        for loc in locs:
            sitemap_url = (loc.text or "").strip()
            if not sitemap_url:
                continue

            # Parse the sitemap URL to filter services
            if not self._should_include_sitemap(sitemap_url):
                continue

            # Extract service path from sitemap URL
            # e.g., /AmazonS3/latest/userguide/sitemap.xml -> /AmazonS3/latest/userguide/
            parsed = urlparse(sitemap_url)
            path = parsed.path.rstrip("/")
            if path.endswith("/sitemap.xml"):
                service_path = path[:-len("/sitemap.xml")]
            else:
                service_path = path.rstrip("/")

            service_url = "/" + service_path.lstrip("/") + "/"

            # Extract service name (first path component)
            parts = [p for p in service_path.split("/") if p]
            service_name = parts[0] if parts else "unknown"

            # Count pages in this sitemap
            page_count = self._count_sitemap_pages(sitemap_url)

            services.append({
                "url": service_url,
                "name": service_name,
                "page_count": page_count,
                "last_discovered": datetime.now(timezone.utc).isoformat(),
            })

        LOGGER.info("Discovered %d services", len(services))
        return services

    def _count_sitemap_pages(self, sitemap_url: str) -> int:
        """Count the number of pages in a sitemap by fetching and parsing it."""
        try:
            self._rate_limiter.acquire()
            response = self.session.get(sitemap_url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            LOGGER.warning("Failed to fetch sitemap %s: %s", sitemap_url, exc)
            return 0

        try:
            root = ET.fromstring(response.text)
        except ET.ParseError as exc:
            LOGGER.warning("Failed to parse sitemap XML from %s: %s", sitemap_url, exc)
            return 0

        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = root.findall(".//sm:loc", ns)
        if not locs:
            locs = root.findall(".//loc")

        # Count valid URLs (we can't use link_checker here as it's not set up yet)
        count = 0
        for loc in locs:
            url = (loc.text or "").strip()
            if url:
                count += 1

        return count

    def _discover_from_sitemap_index(self) -> None:
        """Fetch the sitemap index and discover all service sitemaps."""
        LOGGER.info("Fetching sitemap index from %s", SITEMAP_INDEX_URL)

        try:
            self._rate_limiter.acquire()
            response = self.session.get(SITEMAP_INDEX_URL, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            LOGGER.error("Failed to fetch sitemap index: %s", exc)
            return

        try:
            root = ET.fromstring(response.text)
        except ET.ParseError as exc:
            LOGGER.error("Failed to parse sitemap index XML: %s", exc)
            return

        # Extract all sitemap URLs and process them
        # Sitemap namespace
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        sitemap_urls: list[str] = []

        # Try with namespace first, then without
        locs = root.findall(".//sm:loc", ns)
        if not locs:
            locs = root.findall(".//loc")

        for loc in locs:
            sitemap_url = (loc.text or "").strip()
            if not sitemap_url:
                continue

            # Parse the sitemap URL to filter services
            if not self._should_include_sitemap(sitemap_url):
                continue

            sitemap_urls.append(sitemap_url)

        LOGGER.info("Found %d service sitemaps to process", len(sitemap_urls))

        # Process each service sitemap
        for sitemap_url in sitemap_urls:
            self._process_sitemap(sitemap_url)

    def _should_include_sitemap(self, sitemap_url: str) -> bool:
        """Determine if a sitemap should be processed."""
        parsed = urlparse(sitemap_url)
        if parsed.netloc != DOCS_NETLOC:
            return False

        # Expected pattern: /service/version/guide-type/sitemap.xml
        parts = [p for p in parsed.path.strip("/").split("/") if p]

        if len(parts) < 4 or parts[-1] != "sitemap.xml":
            return False

        service_segment = parts[0]
        version = parts[1]
        guide_segment = parts[2]

        # Only include "latest" versions
        if version.lower() != "latest":
            return False

        # Filter out API references
        if looks_like_api_doc(guide_segment):
            return False

        # Filter out unwanted guide types (javadoc, site_map, etc.)
        if looks_like_unwanted_guide(guide_segment):
            return False

        # Filter out SDKs and toolkits
        if looks_like_non_service(service_segment):
            return False

        # Apply service URL filter if specified
        if self._service_url_prefix:
            # Extract the path up to and including the guide segment
            # e.g., /AmazonS3/latest/userguide/sitemap.xml -> /AmazonS3/latest/userguide/
            sitemap_path = parsed.path.rstrip("/")
            if sitemap_path.endswith("/sitemap.xml"):
                sitemap_path = sitemap_path[:-len("/sitemap.xml")]

            sitemap_prefix = sitemap_path + "/"

            # Check if the sitemap path starts with the filter prefix
            if not sitemap_prefix.startswith(self._service_url_prefix):
                return False

        return True

    def _process_sitemap(self, sitemap_url: str) -> None:
        """Fetch and process a service sitemap XML file to discover all pages."""
        LOGGER.debug("Fetching sitemap %s", sitemap_url)

        try:
            self._rate_limiter.acquire()
            response = self.session.get(sitemap_url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            LOGGER.warning("Failed to fetch sitemap %s: %s", sitemap_url, exc)
            return

        try:
            root = ET.fromstring(response.text)
        except ET.ParseError as exc:
            LOGGER.warning("Failed to parse sitemap XML from %s: %s", sitemap_url, exc)
            return

        # Extract all <loc> URLs from the sitemap
        # Sitemap namespace
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

        # Try with namespace first, then without
        locs = root.findall(".//sm:loc", ns)
        if not locs:
            locs = root.findall(".//loc")

        page_count = 0
        for loc in locs:
            url = (loc.text or "").strip()
            if not url:
                continue

            # Normalize and validate the URL
            candidate_url = normalise_url(url)

            # Check if it's an HTML page we should crawl
            if self._link_checker and self._link_checker(candidate_url):
                self._add_url_to_known(candidate_url)
                page_count += 1

        LOGGER.debug("Found %d pages in sitemap %s", page_count, sitemap_url)

    def _add_url_to_known(self, url: str) -> bool:
        """Add URL to known set for later processing."""
        with self._known_urls_lock:
            if url in self._known_urls:
                return False
            self._known_urls.add(url)
        return True

    def _worker(self) -> None:
        """Worker thread that processes URLs from the queue."""
        while True:
            try:
                url = self._url_queue.get(timeout=1.0)
            except queue.Empty:
                continue

            if url is None:
                self._url_queue.task_done()
                break

            try:
                self._process_url(url)
            except Exception as exc:
                LOGGER.exception("Unhandled error processing %s: %s", url, exc)
            finally:
                self._url_queue.task_done()

    def _process_url(self, url: str) -> None:
        """Process a single URL: fetch, convert, and save."""
        # Check if already visited
        with self._known_urls_lock:
            if url in self._visited_urls:
                LOGGER.debug("Skipping already visited URL: %s", url)
                return

        LOGGER.debug("Fetching %s", url)

        if not self._link_checker or not self._link_checker(url):
            LOGGER.debug("Skipping %s because it does not look like an HTML page", url)
            return

        try:
            self._rate_limiter.acquire()
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            LOGGER.warning("Failed to fetch %s: %s", url, exc)
            return

        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            LOGGER.debug("Skipping %s due to non-HTML content type %s", url, content_type)
            return

        if "charset=" not in content_type.lower():
            apparent = response.apparent_encoding
            if apparent:
                response.encoding = apparent

        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        main = extract_main_content(soup)
        output_path = url_to_output_path(url, self.output_dir)
        self._image_handler.download_and_rewrite_images(main, url, output_path)
        markdown = convert_tag_to_markdown(
            url,
            main,
            output_path=output_path,
            output_root=self.output_dir,
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")

        with self._known_urls_lock:
            self._visited_urls.add(url)
            crawled = len(self._visited_urls)
            total = len(self._known_urls)
            LOGGER.info("Wrote [%d/%d] %s", crawled, total, output_path)

    def _extract_url_prefix(self, url_or_path: str) -> str:
        """Extract the path prefix from a URL or path string."""
        # Handle full URLs
        if url_or_path.startswith(("http://", "https://")):
            parsed = urlparse(url_or_path)
            path = parsed.path
        else:
            # Treat as a path
            path = url_or_path

        # Normalize the path
        path = path.strip()
        if not path.startswith("/"):
            path = "/" + path

        # Remove trailing filename if present (e.g., /path/to/page.html -> /path/to/)
        if path.endswith((".html", ".htm")):
            path = posixpath.dirname(path)

        # Ensure it ends with / for prefix matching
        if not path.endswith("/"):
            path = path + "/"

        return path

    def process_single_guide(
        self,
        service_url: str,
        *,
        enable_commit: bool = False,
    ) -> tuple[int, bool]:
        """Process a single service guide: crawl, format, and optionally commit.

        Returns:
            Tuple of (pages_crawled, commit_success)
        """
        LOGGER.info("=" * 80)
        LOGGER.info("Processing guide: %s", service_url)
        LOGGER.info("=" * 80)

        # Step 1: Delete previous guide directory
        clean_guide_directory(self.output_dir, service_url)

        # Step 2: Set up link checker and URL filter for this guide
        self._service_url_prefix = self._extract_url_prefix(service_url)
        allowed_prefix = self._service_url_prefix.rstrip("/")
        self._link_checker = LinkChecker([allowed_prefix])

        # Step 3: Discover pages from sitemap and crawl
        LOGGER.info("Phase 1: Discovering pages for %s", service_url)
        self._discover_from_sitemap_index()

        with self._known_urls_lock:
            page_count = len(self._known_urls)

        if page_count == 0:
            LOGGER.warning("No pages discovered for %s", service_url)
            return 0, False

        LOGGER.info("Phase 2: Crawling %d pages for %s", page_count, service_url)

        # Step 4: Crawl all pages using thread pool (pages processed in parallel within guide)
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for _ in range(self.max_workers):
                executor.submit(self._worker)

            # Enqueue all discovered URLs
            with self._known_urls_lock:
                for url in self._known_urls:
                    if url not in self._visited_urls:
                        self._url_queue.put(url)

            self._url_queue.join()

            for _ in range(self.max_workers):
                self._url_queue.put(None)

        pages_crawled = len(self.visited_urls)
        LOGGER.info("Crawled %d pages for %s", pages_crawled, service_url)

        # Step 5: Get guide directory path
        parsed = urlparse(service_url) if service_url.startswith(("http://", "https://")) else None
        path = parsed.path if parsed else service_url
        path = path.strip().strip("/")
        guide_dir = self.output_dir / path

        # Step 6: Run prettier on the guide
        LOGGER.info("Formatting markdown files with prettier...")
        run_prettier_on_guide(guide_dir)

        # Step 7: Commit if enabled
        commit_success = False
        if enable_commit:
            LOGGER.info("Committing changes for %s...", service_url)
            commit_success = commit_guide_directory(guide_dir, service_url)
        else:
            LOGGER.info("Skipping commit (--commit not specified)")

        return pages_crawled, commit_success

    def process_all_guides(
        self,
        *,
        enable_commit: bool = False,
        single_guide_url: Optional[str] = None,
        start_from_guide: Optional[str] = None,
    ) -> None:
        """Process all service guides sequentially.

        Args:
            enable_commit: If True, commit each guide after processing
            single_guide_url: If provided, process only this guide
            start_from_guide: If provided, start from this guide (for resuming)
        """
        # Discover all service guides
        LOGGER.info("Discovering service guides from sitemap index...")
        services = self.discover_services()

        if not services:
            LOGGER.error("No services discovered")
            sys.exit(1)

        # Sort services by name for deterministic processing order
        services.sort(key=lambda s: s["name"].lower())

        # Filter to single guide if specified
        if single_guide_url:
            # Normalize the URL for comparison
            if single_guide_url.startswith(("http://", "https://")):
                parsed = urlparse(single_guide_url)
                single_guide_path = "/" + parsed.path.strip("/") + "/"
            else:
                single_guide_path = "/" + single_guide_url.strip("/") + "/"

            services = [s for s in services if s["url"] == single_guide_path]
            if not services:
                LOGGER.error("Guide not found: %s", single_guide_url)
                sys.exit(1)
            LOGGER.info("Processing single guide: %s", single_guide_url)

        # Find start index if resuming
        start_index = 0
        if start_from_guide and not single_guide_url:
            # Normalize the start URL for comparison
            if start_from_guide.startswith(("http://", "https://")):
                parsed = urlparse(start_from_guide)
                start_guide_path = "/" + parsed.path.strip("/") + "/"
            else:
                start_guide_path = "/" + start_from_guide.strip("/") + "/"

            for i, service in enumerate(services):
                if service["url"] == start_guide_path:
                    start_index = i
                    break

            if start_index == 0 and services[0]["url"] != start_guide_path:
                LOGGER.error("Start guide not found: %s", start_from_guide)
                sys.exit(1)

            LOGGER.info("Resuming from guide %d/%d: %s", start_index + 1, len(services), start_from_guide)

        # Process each guide
        total_pages = 0
        total_commits = 0
        failed_guides = []

        for idx, service in enumerate(services[start_index:], start=start_index + 1):
            service_url = service["url"]
            expected_pages = service.get("page_count", 0)

            LOGGER.info("")
            LOGGER.info("=" * 80)
            LOGGER.info("Guide %d/%d: %s (expected %d pages)", idx, len(services), service_url, expected_pages)
            LOGGER.info("=" * 80)

            try:
                # Reset state for this guide
                with self._known_urls_lock:
                    self._known_urls.clear()
                    self._visited_urls.clear()

                # Process the guide
                pages_crawled, committed = self.process_single_guide(
                    service_url,
                    enable_commit=enable_commit,
                )

                total_pages += pages_crawled
                if committed:
                    total_commits += 1

                if pages_crawled == 0:
                    LOGGER.warning("No pages crawled for %s", service_url)
                    failed_guides.append(service_url)

            except Exception as exc:
                LOGGER.error("Failed to process guide %s: %s", service_url, exc, exc_info=True)
                failed_guides.append(service_url)

        # Final summary
        LOGGER.info("")
        LOGGER.info("=" * 80)
        LOGGER.info("FINAL SUMMARY")
        LOGGER.info("=" * 80)
        LOGGER.info("Total guides processed: %d", len(services) - start_index)
        LOGGER.info("Total pages crawled: %d", total_pages)
        LOGGER.info("Total commits: %d", total_commits)
        LOGGER.info("Failed guides: %d", len(failed_guides))
        if failed_guides:
            LOGGER.info("Failed guide URLs:")
            for guide_url in failed_guides:
                LOGGER.info("  - %s", guide_url)
        LOGGER.info("=" * 80)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Crawl AWS documentation using sitemaps.")

    # Global arguments
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Python logging level (e.g. INFO, DEBUG).",
    )

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", required=True, help="Command to run")

    # Discover command
    discover_parser = subparsers.add_parser("discover", help="Discover services from sitemap and save to JSON")
    discover_parser.add_argument(
        "--output",
        type=Path,
        default="services.json",
        help="Output JSON file path (default: services.json)",
    )
    discover_parser.add_argument(
        "--requests-per-second",
        type=float,
        default=10.0,
        help="Maximum number of HTTP requests per second. Set to 0 to disable throttling.",
    )

    # Process-guides command (new simplified workflow)
    process_guides_parser = subparsers.add_parser(
        "process-guides",
        help="Process all service guides sequentially (simplified workflow)"
    )
    process_guides_parser.add_argument(
        "--output-dir",
        default="docs",
        type=Path,
        help="Directory where Markdown files should be written.",
    )
    process_guides_parser.add_argument(
        "--max-workers",
        type=int,
        default=8,
        help="Number of worker threads to use for crawling each guide.",
    )
    process_guides_parser.add_argument(
        "--requests-per-second",
        type=float,
        default=10.0,
        help="Maximum number of HTTP requests per second. Set to 0 to disable throttling.",
    )
    process_guides_parser.add_argument(
        "--commit",
        action="store_true",
        help="Enable git commits after processing each guide. Without this flag, changes are only local.",
    )
    process_guides_parser.add_argument(
        "--service-guide-url",
        type=str,
        help="Process only this specific guide (for testing). E.g., '/AmazonS3/latest/userguide/'",
    )
    process_guides_parser.add_argument(
        "--service-guides-start",
        type=str,
        help="Start processing from this guide (for resuming failed runs). E.g., '/AmazonS3/latest/userguide/'",
    )

    return parser.parse_args()


def clean_guide_directory(output_dir: Path, service_url: str) -> None:
    """Delete existing documentation directory for a specific guide."""
    # Extract the path from the URL
    if service_url.startswith(("http://", "https://")):
        parsed = urlparse(service_url)
        path = parsed.path
    else:
        path = service_url

    # Normalize the path
    path = path.strip().strip("/")

    if not path:
        LOGGER.warning("Cannot clean directory: empty path from URL %s", service_url)
        return

    # Construct the guide directory path
    guide_dir = output_dir / path

    if guide_dir.exists() and guide_dir.is_dir():
        try:
            LOGGER.info("Cleaning directory %s for recrawl", guide_dir)
            shutil.rmtree(guide_dir)
        except Exception as exc:
            LOGGER.warning("Failed to clean directory %s: %s", guide_dir, exc)


def run_prettier_on_guide(guide_dir: Path) -> bool:
    """Run prettier on all markdown files in a guide directory."""
    if not guide_dir.exists() or not guide_dir.is_dir():
        LOGGER.warning("Guide directory does not exist: %s", guide_dir)
        return False

    try:
        LOGGER.info("Running prettier on %s", guide_dir)
        # Use glob pattern relative to the guide directory
        pattern = f"{guide_dir}/**/*.md"
        subprocess.run(
            ["npx", "--yes", "prettier", "--write", pattern],
            check=True,
            capture_output=True,
            text=True,
        )
        return True
    except subprocess.CalledProcessError as exc:
        LOGGER.warning("Prettier failed for %s: %s", guide_dir, exc)
        return False
    except FileNotFoundError:
        LOGGER.warning("npx/prettier not found. Skipping prettier formatting.")
        return False


def prettify_slug(slug: str | None) -> str:
    """Convert a slug into a human-readable name."""
    if not slug:
        return ""

    # Special cases
    special_slugs = {
        "apireference": "API reference",
        "api-reference": "API reference",
        "userguide": "user guide",
        "user-guide": "user guide",
        "developerguide": "developer guide",
        "developer-guide": "developer guide",
        "gettingstarted": "getting started",
        "getting-started": "getting started",
    }

    lower = slug.lower()
    if lower in special_slugs:
        return special_slugs[lower]

    # Convert to title case
    text = slug.replace("-", " ").replace("_", " ")
    text = re.sub(r"(?<=[a-z0-9])([A-Z])", r" \1", text)
    text = re.sub(r"(?<=[A-Z])([A-Z][a-z])", r" \1", text)
    text = re.sub(r"\s+", " ", text).strip()

    words = []
    for word in text.split(" "):
        if not word:
            continue
        if re.fullmatch(r"[A-Z0-9]+", word):
            words.append(word)
        else:
            words.append(word[0].upper() + word[1:].lower())
    return " ".join(words)


def commit_guide_directory(guide_dir: Path, service_url: str) -> bool:
    """Commit changes for a specific guide directory and push to remote."""
    if not guide_dir.exists():
        LOGGER.warning("Cannot commit: guide directory does not exist: %s", guide_dir)
        return False

    try:
        # Stage all changes in the guide directory
        subprocess.run(
            ["git", "add", "-A", "--", str(guide_dir)],
            check=True,
            capture_output=True,
            text=True,
        )

        # Check if there are staged changes
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            capture_output=True,
        )

        if result.returncode == 0:
            # No changes to commit
            LOGGER.info("No changes to commit for %s", guide_dir)
            return False

        # Extract service name from URL for commit message
        parsed = urlparse(service_url) if service_url.startswith(("http://", "https://")) else None
        path = parsed.path if parsed else service_url
        path_parts = [p for p in path.strip("/").split("/") if p]

        # Generate commit message
        service_name = prettify_slug(path_parts[0]) if path_parts else "unknown"
        guide_type = prettify_slug(path_parts[2]) if len(path_parts) > 2 else ""

        if guide_type:
            message = f"Add {service_name} {guide_type}"
        else:
            message = f"Add {service_name} documentation"

        # Create commit
        subprocess.run(
            ["git", "commit", "-m", message],
            check=True,
            capture_output=True,
            text=True,
        )

        LOGGER.info("Committed changes for %s: %s", guide_dir, message)

        # Push to remote with retry logic (exponential backoff)
        # Get current branch
        branch_result = subprocess.run(
            ["git", "branch", "--show-current"],
            check=True,
            capture_output=True,
            text=True,
        )
        branch = branch_result.stdout.strip()

        if not branch:
            LOGGER.warning("Could not determine current branch, skipping push")
            return True

        LOGGER.info("Pushing commit to remote branch %s...", branch)

        # Retry push up to 4 times with exponential backoff
        max_retries = 4
        retry_delays = [2, 4, 8, 16]  # seconds

        for attempt in range(max_retries):
            try:
                subprocess.run(
                    ["git", "push", "-u", "origin", branch],
                    check=True,
                    capture_output=True,
                    text=True,
                    timeout=60,
                )
                LOGGER.info("Successfully pushed commit for %s", guide_dir)
                return True
            except subprocess.CalledProcessError as push_exc:
                if attempt < max_retries - 1:
                    delay = retry_delays[attempt]
                    LOGGER.warning(
                        "Push failed (attempt %d/%d): %s. Retrying in %ds...",
                        attempt + 1,
                        max_retries,
                        push_exc,
                        delay,
                    )
                    time.sleep(delay)
                else:
                    LOGGER.error("Push failed after %d attempts: %s", max_retries, push_exc)
                    return False
            except subprocess.TimeoutExpired:
                if attempt < max_retries - 1:
                    delay = retry_delays[attempt]
                    LOGGER.warning(
                        "Push timed out (attempt %d/%d). Retrying in %ds...",
                        attempt + 1,
                        max_retries,
                        delay,
                    )
                    time.sleep(delay)
                else:
                    LOGGER.error("Push timed out after %d attempts", max_retries)
                    return False

        return False

    except subprocess.CalledProcessError as exc:
        LOGGER.warning("Failed to commit %s: %s", guide_dir, exc)
        # Reset any staged changes
        subprocess.run(["git", "reset", "HEAD"], check=False, capture_output=True)
        return False


def cmd_discover(args: argparse.Namespace) -> None:
    """Discover services from sitemap and save to JSON."""
    # Create a crawler just for discovery (no output dir needed)
    crawler = AwsDocsCrawler(
        output_dir=Path("tmp"),  # Not used for discovery
        max_workers=1,  # Single thread for discovery
        requests_per_second=args.requests_per_second,
    )

    # Discover services
    services = crawler.discover_services()

    if not services:
        LOGGER.error("No services discovered")
        sys.exit(1)

    # Create output structure
    output_data = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "services": services,
    }

    # Write to file
    args.output.write_text(json.dumps(output_data, indent=2), encoding="utf-8")
    LOGGER.info("Discovered %d services, saved to %s", len(services), args.output)


def cmd_process_guides(args: argparse.Namespace) -> None:
    """Process all service guides sequentially (simplified workflow)."""
    args.output_dir.mkdir(parents=True, exist_ok=True)

    crawler = AwsDocsCrawler(
        output_dir=args.output_dir,
        max_workers=args.max_workers,
        requests_per_second=args.requests_per_second,
    )

    crawler.process_all_guides(
        enable_commit=args.commit,
        single_guide_url=args.service_guide_url,
        start_from_guide=args.service_guides_start,
    )


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level.upper(), logging.INFO))

    # Route to appropriate command handler
    if args.command == "discover":
        cmd_discover(args)
    elif args.command == "process-guides":
        cmd_process_guides(args)
    else:
        LOGGER.error("Unknown command: %s", args.command)
        sys.exit(1)


if __name__ == "__main__":
    main()
