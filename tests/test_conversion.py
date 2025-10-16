from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from crawler import convert_page, url_to_relative_output_path


DATA_DIR = Path(__file__).parent / "data"
SAMPLE_URL = "https://docs.aws.amazon.com/deadline-cloud/latest/userguide/what-is-deadline-cloud.html"
SAMPLE_HTML = DATA_DIR / "sample.html"
SAMPLE_MARKDOWN = DATA_DIR / "sample.md"

IMAGE_URL = "https://docs.aws.amazon.com/eks/latest/userguide/eks-compute.html"
IMAGE_HTML = DATA_DIR / "eks_compute.html"
IMAGE_MARKDOWN = DATA_DIR / "eks_compute.md"

API_URL = "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html"
API_HTML = DATA_DIR / "ec2_run_instances.html"
API_MARKDOWN = DATA_DIR / "ec2_run_instances.md"


def _run_conversion_test(url: str, html_path: Path, markdown_path: Path) -> None:
    html = html_path.read_text(encoding="utf-8")
    expected_markdown = markdown_path.read_text(encoding="utf-8")

    output_path, markdown = convert_page(url, html)

    assert output_path == url_to_relative_output_path(url)
    assert markdown == expected_markdown


def test_sample_page_conversion() -> None:
    _run_conversion_test(SAMPLE_URL, SAMPLE_HTML, SAMPLE_MARKDOWN)


def test_image_page_conversion() -> None:
    _run_conversion_test(IMAGE_URL, IMAGE_HTML, IMAGE_MARKDOWN)


def test_api_reference_conversion() -> None:
    _run_conversion_test(API_URL, API_HTML, API_MARKDOWN)
