"""AWS documentation crawler focused on selected services.

This module implements a multi-threaded crawler that downloads AWS
documentation pages and converts the main content of each page to Markdown.
While it currently focuses on a curated list of services, the building blocks
are intentionally generic so the crawl scope can be expanded in the future.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import logging
import os
import queue
import threading
import time
from collections.abc import Callable, Iterable, Sequence
from pathlib import Path, PurePosixPath
import posixpath
from typing import Optional
from urllib.parse import ParseResult, urljoin, urlparse, urlunparse

import requests

from bs4 import BeautifulSoup, Tag
import markdownify

from aws_docs import (
    DOCS_BASE_URL,
    DOCS_NETLOC,
    ServiceGuide,
    ServiceScope,
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
MAX_IMAGE_BYTES = 10 * 1024 * 1024  # 10 MiB safeguard for very large assets


def build_local_image_path(image_path: str, output_root: Path) -> Path:
    """Translate an AWS Docs image path into a local filesystem destination."""

    if not image_path.startswith(IMAGE_PATH_PREFIX):
        raise ValueError(f"Image path must start with {IMAGE_PATH_PREFIX!r}: {image_path!r}")

    relative_path = image_path[len(IMAGE_PATH_PREFIX) :]
    safe_parts = [
        part
        for part in PurePosixPath(relative_path).parts
        if part not in {"..", "."}
    ]

    if not safe_parts:
        raise ValueError(f"Image path did not contain any usable segments: {image_path!r}")

    return output_root.joinpath(*safe_parts)


def _collect_scope_values(scopes: Iterable[ServiceScope], attribute: str) -> list[str]:
    return [value for scope in scopes for value in getattr(scope, attribute)]


def load_service_manifest(path: Path) -> dict[str, ServiceScope]:
    """Load a previously generated service manifest."""

    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    services_raw = data.get("services", [])
    scopes: dict[str, ServiceScope] = {}

    for entry in services_raw:
        service_id = (entry.get("id") or "").strip()
        if not service_id:
            continue

        guides_raw = entry.get("guides", [])
        guides: list[ServiceGuide] = []

        for guide_data in guides_raw:
            url = (guide_data.get("url") or "").strip()
            if not url:
                continue

            title = (guide_data.get("title") or "").strip() or url
            allowed_prefix = (
                (guide_data.get("allowed_prefix") or "").strip()
                or derive_allowed_prefix(url)
            )

            guides.append(
                ServiceGuide(title=title, url=normalise_url(url), allowed_prefix=allowed_prefix)
            )

        if not guides:
            continue

        scopes[service_id] = ServiceScope(
            guides=tuple(sorted(guides, key=lambda guide: guide.url))
        )

    return scopes


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

    def __init__(self, allowed_prefixes: Optional[Sequence[str]] = None) -> None:
        self.allowed_schemes = {"http", "https"}
        self.disallowed_suffixes = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".svg", ".xml"}
        self.html_suffixes = ("/", ".html", ".htm")
        raw_prefixes = list(allowed_prefixes or [])
        self.prefixes = [
            prefix if prefix.startswith("/") else f"/{prefix.lstrip('/')}"
            for prefix in raw_prefixes
            if prefix
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
    """Convert the relevant HTML content to Markdown using ``markdownify``."""

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
    """Join wrapped table rows produced by ``markdownify``.

    The AWS documentation frequently includes multi-paragraph or list content
    inside table cells. ``markdownify`` represents these structures using
    normal Markdown constructs, which introduces newline characters that break
    the table layout. This helper collapses continuation lines back into the
    table row and inserts HTML ``<br>`` elements for list items so that the
    rendered tables remain readable.
    """

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
    """Translate a documentation URL into a Markdown output path.

    Args:
        url: The URL to convert
        output_root: Optional root directory. If provided, returns absolute path,
                     otherwise returns relative path.

    Returns:
        Path object pointing to the Markdown file
    """
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
    link_checker: Callable[[str], bool] | None = None,
) -> str:
    """Convert an extracted HTML fragment into Markdown."""

    for anchor in main.find_all("a"):
        if anchor.find_parent(["code", "pre"]):
            anchor.replace_with(anchor.get_text())
    rewrite_doc_links(
        main,
        url,
        base_output=output_path,
        output_root=output_root,
        link_checker=link_checker,
    )
    markdown = convert_html_to_markdown(str(main))
    return markdown


def convert_page(
    url: str,
    html: str,
    *,
    output_root: Path | None = None,
) -> tuple[Path, str]:
    """Convert a documentation page to Markdown without writing to disk."""

    if output_root is None:
        output_root = Path(".")

    soup = BeautifulSoup(html, "html.parser")
    main = extract_main_content(soup)
    output_path = url_to_output_path(url, output_root)
    markdown = convert_tag_to_markdown(
        url,
        main,
        output_path=output_path,
        output_root=output_root,
    )
    return output_path, markdown


def rewrite_doc_links(
    container: Tag,
    base_url: str,
    *,
    base_output: Path,
    output_root: Path,
    link_checker: Callable[[str], bool] | None = None,
) -> None:
    """Rewrite internal documentation links so they point at local Markdown files."""

    if link_checker is None:
        base_host = urlparse(base_url).netloc

        def should_rewrite(candidate: str) -> bool:
            return urlparse(candidate).netloc == base_host
    else:
        should_rewrite: Callable[[str], bool] = link_checker

    for anchor in container.find_all("a", href=True):
        href = anchor["href"].strip()

        if not href or href.startswith("#") or href.startswith("mailto:"):
            continue

        absolute = urljoin(base_url, href)
        parsed = urlparse(absolute)
        fragment = parsed.fragment
        cleaned = urlunparse(parsed._replace(fragment="", query=""))
        cleaned = normalise_url(cleaned)

        if not should_rewrite(cleaned):
            continue

        target_output = url_to_output_path(cleaned, output_root)
        relative_path = os.path.relpath(target_output, start=base_output.parent)
        relative_href = Path(relative_path).as_posix()

        if fragment:
            relative_href = f"{relative_href}#{fragment}"

        anchor["href"] = relative_href


class TocManager:
    """Handle table of contents processing and document generation."""

    def __init__(
        self,
        output_dir: Path,
        session: requests.Session,
        rate_limiter: RequestRateLimiter,
        link_checker: Callable[[str], bool],
        enqueue_callback: Callable[[str], bool],
    ) -> None:
        self.output_dir = output_dir
        self.session = session
        self.rate_limiter = rate_limiter
        self.link_checker = link_checker
        self.enqueue_callback = enqueue_callback
        self._toc_entries: dict[str, dict] = {}
        self._lock = threading.Lock()

    def process_toc(self, toc_url: str) -> None:
        """Fetch and process a table of contents JSON file."""
        LOGGER.debug("Fetching TOC %s", toc_url)

        try:
            self.rate_limiter.acquire()
            response = self.session.get(toc_url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            LOGGER.warning("Failed to fetch TOC %s: %s", toc_url, exc)
            return

        try:
            toc_data = response.json()
        except ValueError as exc:  # pragma: no cover - defensive logging
            LOGGER.warning("Failed to parse TOC JSON from %s: %s", toc_url, exc)
            return

        for href in self._iter_toc_hrefs(toc_data):
            candidate_url = normalise_url(urljoin(toc_url, href))
            if self.link_checker(candidate_url):
                self.enqueue_callback(candidate_url)

        with self._lock:
            self._toc_entries[toc_url] = toc_data

    @staticmethod
    def _iter_toc_hrefs(node: object) -> Iterable[str]:
        """Recursively extract href values from TOC JSON structure."""
        if isinstance(node, dict):
            href = node.get("href")
            if isinstance(href, str) and href:
                yield href

            contents = node.get("contents")
            if isinstance(contents, list):
                for item in contents:
                    yield from TocManager._iter_toc_hrefs(item)
            return

        if isinstance(node, list):
            for item in node:
                yield from TocManager._iter_toc_hrefs(item)

    def write_toc_documents(self) -> None:
        """Generate README files for each TOC and a main index."""
        with self._lock:
            toc_items = list(self._toc_entries.items())

        if not toc_items:
            return

        service_guides: dict[tuple[str, str], list[tuple[str, str]]] = {}

        for toc_url, toc_data in toc_items:
            metadata = self._parse_toc_metadata(toc_url)
            if metadata is None:
                continue

            service_slug, service_display, guide_display, readme_path = metadata

            contents = toc_data.get("contents") if isinstance(toc_data, dict) else None
            if not isinstance(contents, list):
                continue

            readme_lines = [f"# {service_display} {guide_display} Table of Contents", ""]
            readme_lines.extend(
                self._render_toc_markdown(toc_url, readme_path, contents)
            )

            readme_text = "\n".join(readme_lines).rstrip() + "\n"
            readme_path.parent.mkdir(parents=True, exist_ok=True)
            readme_path.write_text(readme_text, encoding="utf-8")
            LOGGER.info("Wrote TOC %s", readme_path)

            relative_path = readme_path.relative_to(self.output_dir).as_posix()
            service_guides.setdefault((service_slug, service_display), []).append(
                (guide_display, relative_path)
            )

        if service_guides:
            self._write_docs_index(service_guides)

    def _render_toc_markdown(
        self,
        toc_url: str,
        readme_path: Path,
        contents: list[dict],
        depth: int = 0,
    ) -> list[str]:
        """Render TOC entries as Markdown list items."""
        lines: list[str] = []

        def _walk(nodes: list[dict], level: int) -> None:
            for node in nodes:
                if not isinstance(node, dict):
                    continue

                title = str(node.get("title", "")).strip()
                href = node.get("href")
                indent = "  " * level

                link: Optional[str] = None
                if isinstance(href, str) and href:
                    target_url = normalise_url(urljoin(toc_url, href))
                    target_path = url_to_output_path(target_url, self.output_dir)
                    relative = os.path.relpath(target_path, start=readme_path.parent)
                    link = Path(relative).as_posix()

                if title and link:
                    lines.append(f"{indent}- [{title}]({link})")
                elif title:
                    lines.append(f"{indent}- {title}")

                children = node.get("contents")
                if isinstance(children, list) and children:
                    _walk(children, level + 1)

        _walk(contents, depth)
        return lines

    def _parse_toc_metadata(
        self, toc_url: str
    ) -> Optional[tuple[str, str, str, Path]]:
        """Extract service and guide information from TOC URL."""
        parsed = urlparse(toc_url)
        parts = PurePosixPath(parsed.path.lstrip("/")).parts

        if len(parts) < 4 or parts[-1] != "toc-contents.json":
            return None

        service_segment, version_segment, guide_segment = parts[0], parts[1], parts[2]

        if version_segment.lower() != "latest":
            return None

        service_slug, service_display = self._service_display(service_segment)
        guide_display = self._guide_display(guide_segment)
        readme_path = self.output_dir.joinpath(*parts[:-1], "README.md")

        return service_slug, service_display, guide_display, readme_path

    @staticmethod
    def _service_display(service_segment: str) -> tuple[str, str]:
        """Convert service segment to slug and display name."""
        mapping = {
            "deadline-cloud": ("deadline-cloud", "Deadline Cloud"),
            "AmazonS3": ("amazon-s3", "Amazon S3"),
            "AWSCloudFormation": ("aws-cloudformation", "AWS CloudFormation"),
        }

        if service_segment in mapping:
            return mapping[service_segment]

        slug = service_segment.lower().replace("_", "-")
        display = slug.replace("-", " ").title()
        return slug, display

    @staticmethod
    def _guide_display(guide_segment: str) -> str:
        """Convert guide segment to display name."""
        mapping = {
            "userguide": "User Guide",
            "developerguide": "Developer Guide",
            "apireference": "API Reference",
            "api": "API Reference",
        }

        key = guide_segment.lower()
        return mapping.get(key, guide_segment.replace("-", " ").title())

    def _write_docs_index(
        self,
        service_guides: dict[tuple[str, str], list[tuple[str, str]]],
    ) -> None:
        """Write the main documentation index README."""
        index_path = self.output_dir / "README.md"

        guide_order = {
            "User Guide": 0,
            "Developer Guide": 1,
            "Administrator Guide": 2,
            "API Reference": 3,
        }

        lines = [
            "# AWS Documentation Archive",
            "",
            "Browse the available service documentation using the links below.",
            "",
        ]

        for (_, service_display), guides in sorted(
            service_guides.items(), key=lambda item: item[0][1]
        ):
            lines.append(f"- **{service_display}**")
            for guide_display, relative_path in sorted(
                guides,
                key=lambda item: (guide_order.get(item[0], 99), item[0]),
            ):
                lines.append(f"  - [{guide_display}]({relative_path})")

        lines.append("")
        index_text = "\n".join(lines).rstrip() + "\n"
        index_path.write_text(index_text, encoding="utf-8")
        LOGGER.info("Wrote documentation index %s", index_path)


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

            rewritten = next(
                (
                    rewritten
                    for _, rewritten, _ in self._iter_image_rewrites(
                        raw_src, page_url, page_output
                    )
                    if rewritten
                ),
                None,
            )
            if not rewritten:
                continue

            for attr in sources or ["src"]:
                image[attr] = rewritten

            self._rewrite_srcsets(image, page_url, page_output)

    def _iter_image_rewrites(
        self, raw_value: str, page_url: str, page_output: Path
    ) -> Iterable[tuple[str, Optional[str], str]]:
        for part in raw_value.split(","):
            piece = part.strip()
            if not piece:
                continue

            if " " in piece:
                url_token, descriptor = piece.split(None, 1)
                descriptor = descriptor.strip()
            else:
                url_token, descriptor = piece, ""

            rewritten = self._rewrite_single_image(url_token, page_url, page_output)
            yield piece, rewritten, descriptor

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

        local_path = self._image_output_path(parsed.path)
        if not self._download_image(absolute_url, local_path):
            return None

        relative_path = os.path.relpath(local_path, start=page_output.parent)
        return Path(relative_path).as_posix()

    def _rewrite_srcsets(self, image: Tag, page_url: str, page_output: Path) -> None:
        """Rewrite image ``srcset`` style attributes to point at local assets."""
        for attr in ("srcset", "data-srcset", "data-awsdocs-srcset"):
            value = image.get(attr)
            if not value or not isinstance(value, str):
                continue

            rewritten_parts: list[str] = []
            modified = False

            for piece, rewritten, descriptor in self._iter_image_rewrites(
                value, page_url, page_output
            ):
                if rewritten:
                    modified = True
                    token = f"{rewritten} {descriptor}" if descriptor else rewritten
                else:
                    token = piece
                rewritten_parts.append(token)

            if modified:
                image[attr] = ", ".join(rewritten_parts)

    def _image_output_path(self, image_path: str) -> Path:
        return build_local_image_path(image_path, self.output_dir)

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
    """Multi-threaded crawler for curated AWS documentation sections."""

    def __init__(
        self,
        start_urls: Sequence[str],
        output_dir: Path,
        max_workers: int = 8,
        session: Optional[requests.Session] = None,
        link_checker: Optional[Callable[[str], bool]] = None,
        allowed_prefixes: Optional[Sequence[str]] = None,
        requests_per_second: Optional[float] = 10.0,
    ) -> None:
        self.start_urls = [normalise_url(url) for url in start_urls]
        self.output_dir = output_dir
        self.max_workers = max_workers
        self.session = session or requests.Session()
        if link_checker and allowed_prefixes is not None:
            raise ValueError("Provide either link_checker or allowed_prefixes, not both")

        if link_checker is not None:
            self.link_checker = link_checker
        else:
            self.link_checker = LinkChecker(allowed_prefixes)

        self.session.headers.setdefault(
            "User-Agent",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/121.0 Safari/537.36",
        )

        self._url_queue: queue.Queue[str | None] = queue.Queue()
        self._known_urls: set[str] = set()
        self._known_urls_lock = threading.Lock()
        self._known_tocs: set[str] = set()
        self._visited_urls: list[str] = []

        self._rate_limiter = RequestRateLimiter(requests_per_second)
        self._image_handler = ImageHandler(output_dir, self.session, self._rate_limiter)
        self._toc_manager = TocManager(
            output_dir, self.session, self._rate_limiter, self.link_checker, self._enqueue_url_if_new
        )

    @property
    def visited_urls(self) -> list[str]:
        return list(self._visited_urls)

    def crawl(self) -> None:
        LOGGER.info("Starting crawl at %s", ", ".join(self.start_urls))
        self.output_dir.mkdir(parents=True, exist_ok=True)

        with self._known_urls_lock:
            self._known_urls.update(self.start_urls)

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for _ in range(self.max_workers):
                executor.submit(self._worker)

            for url in self.start_urls:
                self._url_queue.put(url)
            self._url_queue.join()

            for _ in range(self.max_workers):
                self._url_queue.put(None)

        self._toc_manager.write_toc_documents()

    def _worker(self) -> None:
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
            except Exception as exc:  # pragma: no cover - defensive logging
                LOGGER.exception("Unhandled error processing %s: %s", url, exc)
            finally:
                self._url_queue.task_done()

    def _process_url(self, url: str) -> None:
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
            link_checker=self.link_checker,
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")

        with self._known_urls_lock:
            crawled = len(self._visited_urls) + 1
            total = len(self._known_urls)
            LOGGER.info("Wrote [%d/%d] %s", crawled, total, output_path)
            self._visited_urls.append(url)

        self._enqueue_links(soup, url)

    def _enqueue_links(self, soup: Tag, base_url: str) -> None:
        def handle_candidate(raw_value: str, *, is_toc: bool = False) -> None:
            candidate = raw_value.strip()
            if not candidate:
                return

            absolute_url = normalise_url(urljoin(base_url, candidate))

            if is_toc:
                with self._known_urls_lock:
                    if absolute_url in self._known_tocs:
                        return
                    self._known_tocs.add(absolute_url)

                self._toc_manager.process_toc(absolute_url)
                return

            if self.link_checker(absolute_url):
                self._enqueue_url_if_new(absolute_url)

        for link in soup.find_all("a", href=True):
            handle_candidate(link["href"])

        for meta in soup.find_all("meta", attrs={"name": "tocs"}):
            raw_content = meta.get("content", "")
            for toc_entry in raw_content.split(","):
                handle_candidate(toc_entry, is_toc=True)

    def _enqueue_url_if_new(self, url: str) -> bool:
        with self._known_urls_lock:
            if url in self._known_urls:
                return False
            self._known_urls.add(url)

        self._url_queue.put(url)
        return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Crawl selected AWS documentation.")
    parser.add_argument(
        "--start-url",
        dest="start_urls",
        action="append",
        metavar="URL",
        help=(
            "Root documentation URLs to start crawling from. "
            "Can be provided multiple times."
        ),
    )
    parser.add_argument(
        "--allowed-prefix",
        dest="allowed_prefixes",
        action="append",
        metavar="PATH",
        help=(
            "Restrict crawling to URLs whose path starts with the provided prefix. "
            "If omitted, a curated set for Deadline Cloud, Amazon S3, and "
            "AWS CloudFormation is used."
        ),
    )
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
        help=(
            "Maximum number of HTTP requests to perform per second. "
            "Set to 0 or a negative value to disable throttling."
        ),
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=MODULE_ROOT / "docs/service-manifest.json",
        help=(
            "Path to the service manifest JSON file generated by the discovery "
            "workflow. The manifest must exist unless explicit start URLs are "
            "provided."
        ),
    )
    parser.add_argument(
        "--service",
        type=str,
        help=(
            "Service ID to crawl from the manifest (e.g., 'a2c', 's3'). "
            "If provided, only this service will be crawled. "
            "Cannot be used with --start-url or --allowed-prefix."
        ),
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Python logging level (e.g. INFO, DEBUG).",
    )
    return parser.parse_args()


def _resolve_cli_scope(args: argparse.Namespace) -> tuple[list[str], list[str]]:
    # Check for conflicting arguments
    if args.service and (args.start_urls or args.allowed_prefixes):
        raise ValueError(
            "--service cannot be used with --start-url or --allowed-prefix"
        )

    if args.start_urls or args.allowed_prefixes:
        start_urls = [normalise_url(url) for url in args.start_urls or []]
        allowed_prefixes = list(args.allowed_prefixes or [])
        if not allowed_prefixes and start_urls:
            allowed_prefixes = [derive_allowed_prefix(url) for url in start_urls]
        return start_urls, allowed_prefixes

    manifest_path = args.manifest
    if not manifest_path:
        raise ValueError("Manifest path must be provided when no start URLs are supplied")

    manifest_path = Path(manifest_path)

    try:
        manifest_scopes = load_service_manifest(manifest_path)
    except FileNotFoundError as exc:
        LOGGER.error("Manifest %s not found", manifest_path)
        raise
    except ValueError as exc:
        LOGGER.error("Failed to load manifest %s (%s)", manifest_path, exc)
        raise

    # If a specific service is requested, filter to just that service
    if args.service:
        service_id = args.service
        if service_id not in manifest_scopes:
            available_services = ", ".join(sorted(manifest_scopes.keys()))
            LOGGER.error(
                "Service '%s' not found in manifest. Available services: %s",
                service_id,
                available_services,
            )
            raise ValueError(f"Service '{service_id}' not found in manifest")

        scope = manifest_scopes[service_id]
        start_urls = scope.start_urls
        allowed_prefixes = scope.allowed_prefixes
        LOGGER.info(
            "Loaded service '%s' with %d guides from manifest %s",
            service_id,
            len(start_urls),
            manifest_path,
        )
        return start_urls, allowed_prefixes

    # No service specified, load all services
    start_urls = _collect_scope_values(manifest_scopes.values(), "start_urls")
    allowed_prefixes = _collect_scope_values(
        manifest_scopes.values(), "allowed_prefixes"
    )
    LOGGER.info(
        "Loaded %d services spanning %d guides from manifest %s",
        len(manifest_scopes),
        len(start_urls),
        manifest_path,
    )
    return start_urls, allowed_prefixes


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level.upper(), logging.INFO))

    start_urls, allowed_prefixes = _resolve_cli_scope(args)

    crawler = AwsDocsCrawler(
        start_urls=start_urls,
        output_dir=args.output_dir,
        max_workers=args.max_workers,
        allowed_prefixes=allowed_prefixes,
        requests_per_second=args.requests_per_second,
    )
    crawler.crawl()

    LOGGER.info("Crawled %d pages", len(crawler.visited_urls))


if __name__ == "__main__":
    main()
