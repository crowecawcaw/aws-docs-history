"""AWS documentation crawler using sitemap-based discovery.

This crawler downloads AWS documentation pages and converts them to Markdown.
It uses AWS's sitemap.xml files to discover all services and pages.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import logging
import os
import queue
import shutil
import threading
import time
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
    },
    "prefixes": ("sdk-for-", "aws-sdk-", "tk-"),
    "substrings": ("toolkit",),
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


def convert_html_to_markdown(html: str) -> str:
    """Convert the relevant HTML content to Markdown using markdownify."""
    content = markdownify.markdownify(
        html,
        heading_style=markdownify.ATX,
        autolinks=True,
        default_title=True,
        escape_asterisks=True,
        escape_underscores=True,
        newline_style="SPACES",
        strip=TAGS_TO_STRIP,
    )

    if not content:
        return ""

    cleaned = _reflow_markdown_tables(content)
    return cleaned.strip() + "\n"


def _reflow_markdown_tables(markdown: str) -> str:
    """Join wrapped table rows produced by markdownify."""
    lines = markdown.splitlines()
    result: list[str] = []
    pending_row: str | None = None
    in_table = False
    expected_pipe_count: int | None = None

    def flush_row() -> None:
        nonlocal pending_row
        if pending_row is not None:
            result.append(pending_row.rstrip())
            pending_row = None

    for line in lines:
        stripped_leading = line.lstrip()

        if stripped_leading.startswith("|"):
            pipe_count = stripped_leading.count("|")

            if (
                in_table
                and pending_row is not None
                and expected_pipe_count
                and pipe_count < expected_pipe_count
                and pending_row.count("|") < expected_pipe_count
            ):
                pending_row += " " + stripped_leading.strip()
                continue

            if in_table:
                flush_row()
            else:
                in_table = True

            pending_row = stripped_leading.rstrip()
            if expected_pipe_count is None or pipe_count > expected_pipe_count:
                expected_pipe_count = pipe_count
            continue

        if in_table and pending_row is not None:
            stripped = line.strip()
            if not stripped:
                continue

            if stripped.startswith("* "):
                addition = f" <br>• {stripped[2:].strip()}"
            elif stripped.startswith("- "):
                addition = f" <br>• {stripped[2:].strip()}"
            else:
                addition = " " + stripped

            pending_row += addition
            continue

        if in_table:
            flush_row()
            in_table = False
            expected_pipe_count = None

        result.append(line)

    if in_table:
        flush_row()

    return "\n".join(result)


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
        allowed_prefixes: Optional[list[str]] = None,
        requests_per_second: Optional[float] = 10.0,
        service_filter: Optional[str] = None,
    ) -> None:
        self.output_dir = output_dir
        self.max_workers = max_workers
        self.session = session or requests.Session()
        self.link_checker = LinkChecker(allowed_prefixes)
        self.service_filter = service_filter

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

    @property
    def visited_urls(self) -> list[str]:
        with self._known_urls_lock:
            return list(self._visited_urls)

    def crawl(self) -> None:
        """Main crawl entry point."""
        LOGGER.info("Starting crawl")
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Phase 1: Discover all pages from sitemap index
        LOGGER.info("Phase 1: Discovering pages from AWS sitemap index")
        self._discover_from_sitemap_index()

        # Phase 2: Crawl all discovered pages
        with self._known_urls_lock:
            page_count = len(self._known_urls)
        LOGGER.info("Phase 2: Crawling %d discovered pages", page_count)

        if page_count == 0:
            LOGGER.warning("No pages discovered to crawl")
            return

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
            soup = BeautifulSoup(response.text, "xml")
        except Exception as exc:
            LOGGER.error("Failed to parse sitemap index XML: %s", exc)
            return

        # Extract all sitemap URLs and process them
        sitemap_urls: list[str] = []
        for loc in soup.find_all("loc"):
            sitemap_url = loc.get_text().strip()
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

        # Filter out SDKs and toolkits
        if looks_like_non_service(service_segment):
            return False

        # Apply service filter if specified
        if self.service_filter:
            service_id = service_segment.lower().replace("_", "-")
            if service_id != self.service_filter.lower():
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
            soup = BeautifulSoup(response.text, "xml")
        except Exception as exc:
            LOGGER.warning("Failed to parse sitemap XML from %s: %s", sitemap_url, exc)
            return

        # Extract all <loc> URLs from the sitemap
        for loc in soup.find_all("loc"):
            url = loc.get_text().strip()
            if not url:
                continue

            # Normalize and validate the URL
            candidate_url = normalise_url(url)

            # Check if it's an HTML page we should crawl
            if self.link_checker(candidate_url):
                self._add_url_to_known(candidate_url)

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

        if not self.link_checker(url):
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Crawl AWS documentation using sitemaps.")
    parser.add_argument(
        "--output-dir",
        default="docs",
        type=Path,
        help="Directory where Markdown files should be written.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=8,
        help="Number of worker threads to use for crawling.",
    )
    parser.add_argument(
        "--requests-per-second",
        type=float,
        default=10.0,
        help="Maximum number of HTTP requests per second. Set to 0 to disable throttling.",
    )
    parser.add_argument(
        "--service",
        type=str,
        help="Service ID to crawl (e.g., 'deadline-cloud', 's3'). If not provided, all services will be crawled.",
    )
    parser.add_argument(
        "--allowed-prefix",
        dest="allowed_prefixes",
        action="append",
        metavar="PATH",
        help="Restrict crawling to URLs with this path prefix. Can be provided multiple times.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Python logging level (e.g. INFO, DEBUG).",
    )
    return parser.parse_args()


def clean_service_directories(output_dir: Path, service_id: str) -> None:
    """Delete existing documentation directories for a specific service."""
    # Construct the service directory path
    service_dir = output_dir / service_id

    if service_dir.exists() and service_dir.is_dir():
        try:
            LOGGER.info("Cleaning directory %s for recrawl", service_dir)
            shutil.rmtree(service_dir)
        except Exception as exc:
            LOGGER.warning("Failed to clean directory %s: %s", service_dir, exc)


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level.upper(), logging.INFO))

    # Clean service directories if crawling a specific service
    if args.service:
        clean_service_directories(args.output_dir, args.service)

    crawler = AwsDocsCrawler(
        output_dir=args.output_dir,
        max_workers=args.max_workers,
        allowed_prefixes=args.allowed_prefixes,
        requests_per_second=args.requests_per_second,
        service_filter=args.service,
    )
    crawler.crawl()

    LOGGER.info("Crawled %d pages", len(crawler.visited_urls))


if __name__ == "__main__":
    main()
