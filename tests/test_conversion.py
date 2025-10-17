from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pytest

from crawler import convert_page, url_to_relative_output_path


DATA_DIR = Path(__file__).parent / "data"


PAGE_FIXTURES: dict[str, dict[str, str]] = {
    "sample": {
        "url": "https://docs.aws.amazon.com/deadline-cloud/latest/userguide/what-is-deadline-cloud.html",
    },
    "auto_scaling_image": {
        "url": "https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html",
    },
}


@pytest.fixture(scope="module", params=sorted(PAGE_FIXTURES), ids=lambda name: name)
def page_data(request: pytest.FixtureRequest) -> dict[str, str]:
    """Load a conversion fixture from disk once per parametrized test."""

    name: str = request.param
    config = PAGE_FIXTURES[name]
    html = (DATA_DIR / f"{name}.html").read_text(encoding="utf-8")
    expected_markdown = (DATA_DIR / f"{name}.md").read_text(encoding="utf-8")

    return {
        "url": config["url"],
        "html": html,
        "expected_markdown": expected_markdown,
    }


def test_page_conversion(page_data: dict[str, str]) -> None:
    output_path, markdown = convert_page(page_data["url"], page_data["html"])

    assert output_path == url_to_relative_output_path(page_data["url"])
    assert markdown == page_data["expected_markdown"]
