from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Iterable

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from crawler import convert_page, url_to_relative_output_path


DATA_DIR = Path(__file__).parent / "data"


@dataclass(frozen=True)
class ConversionCase:
    url: str
    html_path: Path
    markdown_path: Path
    id: str


def _read_url(url_path: Path) -> str:
    for line in url_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    raise ValueError(f"No URL found in {url_path.relative_to(DATA_DIR)}")


def _iter_conversion_cases() -> Iterable[ConversionCase]:
    for url_file in sorted(DATA_DIR.rglob("*.url")):
        url = _read_url(url_file)
        html_path = url_file.with_suffix(".html")
        markdown_path = url_file.with_suffix(".md")

        missing = [
            str(path.relative_to(DATA_DIR))
            for path in (html_path, markdown_path)
            if not path.exists()
        ]
        if missing:
            raise FileNotFoundError(
                f"Missing partner files for fixture '{url_file.relative_to(DATA_DIR)}':"
                f" {', '.join(missing)}"
            )

        case_id = str(url_file.relative_to(DATA_DIR).with_suffix(""))
        yield ConversionCase(url, html_path, markdown_path, case_id)


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    if {"url", "html_path", "markdown_path"} <= set(metafunc.fixturenames):
        params = [
            pytest.param(case.url, case.html_path, case.markdown_path, id=case.id)
            for case in _iter_conversion_cases()
        ]

        if not params:
            pytest.fail(
                "No conversion fixtures discovered in tests/data", pytrace=False
            )

        metafunc.parametrize(("url", "html_path", "markdown_path"), params)


def test_conversion_cases(url: str, html_path: Path, markdown_path: Path) -> None:
    html = html_path.read_text(encoding="utf-8")
    expected_markdown = markdown_path.read_text(encoding="utf-8")

    output_path, markdown = convert_page(url, html)

    assert output_path == url_to_relative_output_path(url)
    assert markdown == expected_markdown
