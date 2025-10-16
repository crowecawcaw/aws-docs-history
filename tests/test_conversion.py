from pathlib import Path
import sys
from typing import Iterable, Tuple

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from crawler import convert_page, url_to_relative_output_path


DATA_DIR = Path(__file__).parent / "data"


def _iter_conversion_cases() -> Iterable[Tuple[str, Path, Path]]:
    for url_file in sorted(DATA_DIR.glob("*.url")):
        url = url_file.read_text(encoding="utf-8").strip()
        stem = url_file.stem
        html_path = DATA_DIR / f"{stem}.html"
        markdown_path = DATA_DIR / f"{stem}.md"

        if not html_path.exists() or not markdown_path.exists():
            raise FileNotFoundError(
                f"Missing HTML/Markdown partner for fixture '{stem}'"
            )

        yield url, html_path, markdown_path


CONVERSION_CASES = list(_iter_conversion_cases())

if not CONVERSION_CASES:
    raise ValueError("No conversion fixtures discovered in tests/data")


@pytest.mark.parametrize(
    "url, html_path, markdown_path",
    CONVERSION_CASES,
    ids=[html_path.stem for _, html_path, _ in CONVERSION_CASES],
)
def test_conversion_cases(url: str, html_path: Path, markdown_path: Path) -> None:
    html = html_path.read_text(encoding="utf-8")
    expected_markdown = markdown_path.read_text(encoding="utf-8")

    output_path, markdown = convert_page(url, html)

    assert output_path == url_to_relative_output_path(url)
    assert markdown == expected_markdown
