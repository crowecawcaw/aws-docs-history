from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest

from crawler import convert_page, url_to_relative_output_path


DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture(scope="module")
def sample_page_data() -> dict[str, str]:
    """Load the sample conversion fixture from disk once per test module."""

    url = "https://docs.aws.amazon.com/deadline-cloud/latest/userguide/what-is-deadline-cloud.html"
    html = (DATA_DIR / "sample.html").read_text(encoding="utf-8")
    expected_markdown = (DATA_DIR / "sample.md").read_text(encoding="utf-8")

    return {
        "url": url,
        "html": html,
        "expected_markdown": expected_markdown,
    }


def test_sample_page_conversion(sample_page_data: dict[str, str]) -> None:
    output_path, markdown = convert_page(sample_page_data["url"], sample_page_data["html"])

    assert output_path == url_to_relative_output_path(sample_page_data["url"])
    assert markdown == sample_page_data["expected_markdown"]
