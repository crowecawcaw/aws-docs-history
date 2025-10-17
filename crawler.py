"""AWS documentation crawler focused on selected services.

This module implements a multi-threaded crawler that downloads AWS
documentation pages and converts the main content of each page to Markdown.
While it currently focuses on a curated list of services, the building blocks
are intentionally generic so the crawl scope can be expanded in the future.
"""

from __future__ import annotations

import argparse
import logging
import os
import queue
import threading
import time
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import posixpath
from typing import Optional
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup, Tag
import markdownify

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

IMAGE_HOST = "docs.aws.amazon.com"
IMAGE_PATH_PREFIX = "/images/"
ALLOWED_IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg"}
MAX_IMAGE_BYTES = 10 * 1024 * 1024  # 10 MiB safeguard for very large assets


@dataclass(frozen=True)
class ServiceScope:
    """Describe the default crawl scope for a single AWS service."""

    start_urls: tuple[str, ...]
    allowed_prefixes: tuple[str, ...]


DEFAULT_SERVICE_SCOPES: dict[str, ServiceScope] = {
    "deadline-cloud": ServiceScope(
        start_urls=(
            "https://docs.aws.amazon.com/deadline-cloud/latest/userguide/what-is-deadline-cloud.html",
            "https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/what-is-deadline-cloud.html",
            "https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/Welcome.html",
        ),
        allowed_prefixes=(
            "/deadline-cloud/latest/userguide/",
            "/deadline-cloud/latest/developerguide/",
            "/deadline-cloud/latest/APIReference/",
        ),
    ),
}


def _collect_start_urls(scopes: Iterable[ServiceScope]) -> list[str]:
    start_urls: list[str] = []
    for scope in scopes:
        start_urls.extend(scope.start_urls)
    return start_urls


def _collect_allowed_prefixes(scopes: Iterable[ServiceScope]) -> list[str]:
    prefixes: list[str] = []
    for scope in scopes:
        prefixes.extend(scope.allowed_prefixes)
    return prefixes


DEFAULT_START_URLS = _collect_start_urls(DEFAULT_SERVICE_SCOPES.values())
DEFAULT_ALLOWED_PREFIXES = _collect_allowed_prefixes(DEFAULT_SERVICE_SCOPES.values())


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


def build_link_checker(
    allowed_prefixes: Optional[Sequence[str]] = None,
) -> Callable[[str], bool]:
    """Return a predicate that determines whether a link should be crawled.

    The checker enforces that links:
    * Stay on the ``docs.aws.amazon.com`` host.
    * Reside under one of the configured path prefixes so that the crawler can
      focus on specific services.
    * Resolve to HTML documents (i.e., ignore in-page anchors, mailto links,
      etc.).

    The function is intentionally self-contained and easy to modify as new
    services are added or the crawl scope changes.
    """

    allowed_host = "docs.aws.amazon.com"
    raw_prefixes = (
        list(allowed_prefixes) if allowed_prefixes is not None else DEFAULT_ALLOWED_PREFIXES
    )
    prefixes: list[str] = []
    for prefix in raw_prefixes:
        if not prefix:
            continue
        normalised = prefix if prefix.startswith("/") else f"/{prefix.lstrip('/')}"
        prefixes.append(normalised)

    def should_visit(url: str) -> bool:
        parsed = urlparse(url)

        # Reject links without a network location or supported scheme.
        if parsed.scheme == "mailto":
            return False

        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            return False

        if parsed.netloc != allowed_host:
            return False

        if prefixes and not any(parsed.path.startswith(prefix) for prefix in prefixes):
            return False

        # Skip assets that clearly are not HTML documents and enforce an HTML suffix.
        lower_path = parsed.path.lower()
        if lower_path.endswith(
            (".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".svg", ".xml")
        ):
            return False

        if lower_path and not lower_path.endswith("/"):
            if not lower_path.endswith((".html", ".htm")):
                return False

        # Allow the service root (no explicit path) and directory listings.
        if not lower_path and parsed.path == "":
            return True

        return True

    return should_visit


def extract_main_content(soup: BeautifulSoup) -> Tag:
    """Extract the main documentation content from the parsed HTML page."""

    main: Tag | None = None
    for selector in CONTENT_SELECTORS:
        candidate = soup.select_one(selector)
        if candidate is not None:
            main = candidate
            break

    if main is None:
        main = soup.body or soup

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

    return (content.strip() + "\n") if content else ""


def _default_link_checker(base_url: str) -> Callable[[str], bool]:
    """Provide a conservative default link checker for standalone conversion."""

    base_host = urlparse(base_url).netloc

    def checker(candidate: str) -> bool:
        return urlparse(candidate).netloc == base_host

    return checker


def normalise_url(url: str) -> str:
    """Normalise a URL by removing fragments and redundant path segments."""

    parsed = urlparse(url)
    cleaned_path = posixpath.normpath(parsed.path or "/")
    if parsed.path.endswith("/") and not cleaned_path.endswith("/"):
        cleaned_path += "/"

    cleaned = parsed._replace(path=cleaned_path, fragment="", query="")
    return urlunparse(cleaned)


def url_to_output_path(url: str, output_root: Path) -> Path:
    """Translate a documentation URL into a Markdown output path."""

    return output_root / url_to_relative_output_path(url)


def url_to_relative_output_path(url: str) -> Path:
    """Translate a documentation URL into a relative Markdown output path."""

    parsed = urlparse(url)
    path = parsed.path.lstrip("/")

    if path.endswith("/"):
        path = path[:-1]
    if not path:
        path = "index"
    if path.endswith(".html"):
        path = path[:-5]

    parts = [part for part in path.split("/") if part]
    if not parts:
        parts = ["index"]

    return Path(*parts).with_suffix(".md")


def convert_tag_to_markdown(
    url: str,
    main: Tag,
    *,
    output_root: Path,
    link_checker: Callable[[str], bool],
) -> tuple[Path, str]:
    """Convert an extracted HTML fragment into Markdown."""

    _strip_code_block_links(main)
    rewrite_doc_links(main, url, output_root, link_checker)
    markdown = convert_html_to_markdown(str(main))
    output_path = url_to_output_path(url, output_root)
    return output_path, markdown


def _strip_code_block_links(container: Tag) -> None:
    """Remove hyperlinks that appear within code or preformatted blocks."""

    for anchor in container.find_all("a"):
        if anchor.find_parent(["code", "pre"]):
            anchor.replace_with(anchor.get_text())


def convert_page(
    url: str,
    html: str,
    *,
    output_root: Path | None = None,
    link_checker: Callable[[str], bool] | None = None,
) -> tuple[Path, str]:
    """Convert a documentation page to Markdown without writing to disk."""

    if output_root is None:
        output_root = Path(".")
    if link_checker is None:
        link_checker = _default_link_checker(url)

    soup = BeautifulSoup(html, "html.parser")
    main = extract_main_content(soup)
    return convert_tag_to_markdown(
        url,
        main,
        output_root=output_root,
        link_checker=link_checker,
    )


def rewrite_doc_links(
    container: Tag,
    base_url: str,
    output_root: Path,
    link_checker: Callable[[str], bool],
) -> None:
    """Rewrite internal documentation links so they point at local Markdown files."""

    base_output = url_to_output_path(base_url, output_root)

    for anchor in container.find_all("a", href=True):
        href = anchor["href"].strip()

        if not href or href.startswith("#") or href.startswith("mailto:"):
            continue

        absolute = urljoin(base_url, href)
        parsed = urlparse(absolute)
        fragment = parsed.fragment
        cleaned = urlunparse(parsed._replace(fragment="", query=""))
        cleaned = normalise_url(cleaned)

        if not link_checker(cleaned):
            continue

        target_output = url_to_output_path(cleaned, output_root)
        relative_path = os.path.relpath(target_output, start=base_output.parent)
        relative_href = Path(relative_path).as_posix()

        if fragment:
            relative_href = f"{relative_href}#{fragment}"

        anchor["href"] = relative_href


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
            self.link_checker = build_link_checker(allowed_prefixes)

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
        self._workers: list[threading.Thread] = []
        self._downloaded_images: set[str] = set()
        self._downloaded_images_lock = threading.Lock()
        self._toc_entries: dict[str, dict] = {}
        self._toc_entries_lock = threading.Lock()

        self.images_root = self.output_dir / "images"
        self._rate_limiter = RequestRateLimiter(requests_per_second)

    @property
    def visited_urls(self) -> list[str]:
        return list(self._visited_urls)

    def crawl(self) -> None:
        LOGGER.info("Starting crawl at %s", ", ".join(self.start_urls))
        self.output_dir.mkdir(parents=True, exist_ok=True)

        with self._known_urls_lock:
            self._known_urls.update(self.start_urls)

        for _ in range(self.max_workers):
            worker = threading.Thread(target=self._worker, daemon=True)
            worker.start()
            self._workers.append(worker)

        for url in self.start_urls:
            self._url_queue.put(url)
        self._url_queue.join()

        for _ in range(self.max_workers):
            self._url_queue.put(None)

        for worker in self._workers:
            worker.join()
        self._workers.clear()

        self._write_toc_documents()

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
        self._download_and_rewrite_images(main, url, output_path)
        output_path, markdown = convert_tag_to_markdown(
            url,
            main,
            output_root=self.output_dir,
            link_checker=self.link_checker,
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
        LOGGER.info("Wrote %s", output_path)

        with self._known_urls_lock:
            self._visited_urls.append(url)

        self._enqueue_links(soup, url)

    def _enqueue_links(self, soup: Tag, base_url: str) -> None:
        for link in soup.find_all("a", href=True):
            href = link["href"].strip()
            if not href:
                continue

            absolute_url = urljoin(base_url, href)
            absolute_url = normalise_url(absolute_url)

            if not self.link_checker(absolute_url):
                continue

            with self._known_urls_lock:
                if absolute_url in self._known_urls:
                    continue
                self._known_urls.add(absolute_url)
            self._url_queue.put(absolute_url)

        self._enqueue_toc_links(soup, base_url)

    def _enqueue_toc_links(self, soup: Tag, base_url: str) -> None:
        for meta in soup.find_all("meta", attrs={"name": "tocs"}):
            raw_content = meta.get("content", "")
            if not raw_content:
                continue

            for toc_entry in (part.strip() for part in raw_content.split(",")):
                if not toc_entry:
                    continue

                toc_url = normalise_url(urljoin(base_url, toc_entry))

                with self._known_urls_lock:
                    if toc_url in self._known_tocs:
                        continue
                    self._known_tocs.add(toc_url)

                self._process_toc(toc_url)

    def _process_toc(self, toc_url: str) -> None:
        LOGGER.debug("Fetching TOC %s", toc_url)

        try:
            self._rate_limiter.acquire()
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

            if not self.link_checker(candidate_url):
                continue

            with self._known_urls_lock:
                if candidate_url in self._known_urls:
                    continue
                self._known_urls.add(candidate_url)

            self._url_queue.put(candidate_url)

        with self._toc_entries_lock:
            self._toc_entries[toc_url] = toc_data

    @staticmethod
    def _iter_toc_hrefs(node: object) -> list[str]:
        hrefs: list[str] = []

        def _walk(value: object) -> None:
            if isinstance(value, dict):
                href = value.get("href")
                if isinstance(href, str):
                    hrefs.append(href)
                contents = value.get("contents")
                if isinstance(contents, list):
                    for item in contents:
                        _walk(item)
            elif isinstance(value, list):
                for item in value:
                    _walk(item)

        _walk(node)
        return hrefs

    def _download_and_rewrite_images(self, container: Tag, page_url: str, page_output: Path) -> None:
        for image in container.find_all("img"):
            source_attr, raw_src = self._select_image_source(image)
            if not raw_src:
                continue

            rewritten = self._rewrite_single_image(raw_src, page_url, page_output)
            if not rewritten:
                continue

            # Always ensure the ``src`` attribute is updated even if a data attribute
            # provided the original path so that the Markdown conversion references
            # the downloaded asset.
            image["src"] = rewritten
            if source_attr and source_attr != "src":
                image[source_attr] = rewritten

            self._rewrite_srcsets(image, page_url, page_output)

    def _select_image_source(self, image: Tag) -> tuple[Optional[str], str]:
        """Determine the most useful source attribute for an ``img`` tag."""

        for attr in ("src", "data-src", "data-awsdocs-src"):
            value = image.get(attr)
            if isinstance(value, str):
                stripped = value.strip()
                if stripped:
                    return attr, stripped
        return None, ""

    def _rewrite_single_image(self, raw_src: str, page_url: str, page_output: Path) -> Optional[str]:
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

            for part in value.split(","):
                piece = part.strip()
                if not piece:
                    continue

                if " " in piece:
                    url_token, descriptor = piece.split(" ", 1)
                else:
                    url_token, descriptor = piece, ""

                new_url = self._rewrite_single_image(url_token, page_url, page_output)
                if new_url:
                    url_token = new_url
                    modified = True

                if descriptor:
                    rewritten_parts.append(f"{url_token} {descriptor}")
                else:
                    rewritten_parts.append(url_token)

            if modified:
                image[attr] = ", ".join(rewritten_parts)

    def _image_output_path(self, image_path: str) -> Path:
        relative_path = image_path[len(IMAGE_PATH_PREFIX) :]
        safe_parts = [part for part in PurePosixPath(relative_path).parts if part not in {"..", "."}]
        local_path = self.images_root.joinpath(*safe_parts)
        return local_path

    def _download_image(self, image_url: str, destination: Path) -> bool:
        destination.parent.mkdir(parents=True, exist_ok=True)

        if destination.exists():
            return True

        with self._downloaded_images_lock:
            if image_url in self._downloaded_images:
                return destination.exists()
            self._downloaded_images.add(image_url)

        try:
            self._rate_limiter.acquire()
            response = self.session.get(image_url, stream=True, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            LOGGER.warning("Failed to download image %s: %s", image_url, exc)
            with self._downloaded_images_lock:
                self._downloaded_images.discard(image_url)
            return False

        content_length = response.headers.get("Content-Length")
        if content_length:
            try:
                if int(content_length) > MAX_IMAGE_BYTES:
                    LOGGER.warning(
                        "Skipping image %s because it exceeds the %d byte limit", image_url, MAX_IMAGE_BYTES
                    )
                    with self._downloaded_images_lock:
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
                        with self._downloaded_images_lock:
                            self._downloaded_images.discard(image_url)
                        return False
                    handle.write(chunk)
        finally:
            response.close()

        return True

    def _write_toc_documents(self) -> None:
        with self._toc_entries_lock:
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
                self._render_toc_markdown(
                    toc_url,
                    readme_path,
                    contents,
                )
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
        index_path = self.output_dir / "README.md"

        guide_order = {"User Guide": 0, "Developer Guide": 1, "Administrator Guide": 2, "API Reference": 3}

        lines = ["# AWS Documentation Archive", "", "Browse the available service documentation using the links below.", ""]

        for (_, service_display), guides in sorted(service_guides.items(), key=lambda item: item[0][1]):
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
        "--log-level",
        default="INFO",
        help="Python logging level (e.g. INFO, DEBUG).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level.upper(), logging.INFO))

    start_urls = args.start_urls or DEFAULT_START_URLS
    allowed_prefixes = args.allowed_prefixes or DEFAULT_ALLOWED_PREFIXES

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
