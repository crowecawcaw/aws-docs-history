"""AWS documentation crawler tailored for Deadline Cloud content.

This module implements a multi-threaded crawler that downloads AWS Deadline
Cloud documentation pages and converts the main content of each page to
Markdown. The crawler is intentionally focused on a single service while the
project is bootstrapped, but the core pieces (link checker, crawling logic,
conversion) are written so that the scope can be expanded in the future.
"""

from __future__ import annotations

import argparse
import logging
import os
import queue
import threading
from collections.abc import Callable
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


def build_deadline_cloud_link_checker() -> Callable[[str], bool]:
    """Return a predicate that determines whether a link should be crawled.

    The checker enforces that links:
    * Stay on the ``docs.aws.amazon.com`` host.
    * Are scoped to the ``/deadline-cloud/`` prefix while we bootstrap the
      crawler.
    * Avoid obvious API reference documentation which lives under the
      ``APIReference`` path segment.
    * Resolve to HTML documents (i.e., ignore in-page anchors, mailto links,
      etc.).

    The function is intentionally self-contained and easy to modify as new
    services are added or the crawl scope changes.
    """

    allowed_host = "docs.aws.amazon.com"
    required_prefix = "/deadline-cloud/"

    def should_visit(url: str) -> bool:
        parsed = urlparse(url)

        # Reject links without a network location or supported scheme.
        if parsed.scheme == "mailto":
            return False

        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            return False

        if parsed.netloc != allowed_host:
            return False

        if not parsed.path.startswith(required_prefix):
            return False

        # Ignore API reference sections to focus on guides.
        if "apireference" in parsed.path.lower():
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

    parsed = urlparse(url)
    path = parsed.path.lstrip("/")

    if path.endswith("/"):
        path = path[:-1]
    if not path:
        path = "index"
    if path.endswith(".html"):
        path = path[:-5]

    output_path = output_root.joinpath(*path.split("/"))
    return output_path.with_suffix(".md")


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


class DeadlineCloudCrawler:
    """Multi-threaded crawler for AWS Deadline Cloud documentation."""

    def __init__(
        self,
        start_url: str,
        output_dir: Path,
        max_workers: int = 8,
        session: Optional[requests.Session] = None,
        link_checker: Optional[Callable[[str], bool]] = None,
    ) -> None:
        self.start_url = start_url
        self.output_dir = output_dir
        self.max_workers = max_workers
        self.session = session or requests.Session()
        self.link_checker = link_checker or build_deadline_cloud_link_checker()

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

        self.images_root = self.output_dir / "images"

    @property
    def visited_urls(self) -> list[str]:
        return list(self._visited_urls)

    def crawl(self) -> None:
        LOGGER.info("Starting crawl at %s", self.start_url)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        with self._known_urls_lock:
            self._known_urls.add(self.start_url)

        for _ in range(self.max_workers):
            worker = threading.Thread(target=self._worker, daemon=True)
            worker.start()
            self._workers.append(worker)

        self._url_queue.put(self.start_url)
        self._url_queue.join()

        for _ in range(self.max_workers):
            self._url_queue.put(None)

        for worker in self._workers:
            worker.join()
        self._workers.clear()

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
        rewrite_doc_links(main, url, self.output_dir, self.link_checker)
        markdown = convert_html_to_markdown(str(main))

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
        for image in container.find_all("img", src=True):
            raw_src = image.get("src", "").strip()
            if not raw_src:
                continue

            absolute_url = normalise_url(urljoin(page_url, raw_src))
            parsed = urlparse(absolute_url)

            if parsed.scheme not in {"http", "https"}:
                continue

            if parsed.netloc != IMAGE_HOST:
                continue

            if not parsed.path.startswith(IMAGE_PATH_PREFIX):
                continue

            extension = Path(parsed.path).suffix.lower()
            if extension not in ALLOWED_IMAGE_EXTENSIONS:
                continue

            local_path = self._image_output_path(parsed.path)
            if not self._download_image(absolute_url, local_path):
                continue

            relative_path = os.path.relpath(local_path, start=page_output.parent)
            image["src"] = Path(relative_path).as_posix()

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Crawl AWS Deadline Cloud documentation.")
    parser.add_argument(
        "--start-url",
        default="https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/what-is-deadline-cloud.html",
        help="Root documentation URL to start crawling from.",
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
        "--log-level",
        default="INFO",
        help="Python logging level (e.g. INFO, DEBUG).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level.upper(), logging.INFO))

    crawler = DeadlineCloudCrawler(
        start_url=args.start_url,
        output_dir=args.output_dir,
        max_workers=args.max_workers,
    )
    crawler.crawl()

    LOGGER.info("Crawled %d pages", len(crawler.visited_urls))


if __name__ == "__main__":
    main()
