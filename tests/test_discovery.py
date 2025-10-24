from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from crawler import (
    load_service_manifest,
    parse_main_landing_page,
    parse_service_landing_page,
)

DATA_DIR = Path(__file__).parent / "data"


def test_parse_main_landing_page_extracts_service_roots() -> None:
    xml_text = (DATA_DIR / "main_landing_sample.xml").read_text(encoding="utf-8")

    services = parse_main_landing_page(xml_text)

    assert services["cloudfront"] == "/cloudfront/"
    assert services["glue"] == "/glue/"
    assert services["signin"] == "/signin/"
    assert "whitepapers" not in services


def test_parse_service_landing_page_filters_api_docs() -> None:
    xml_text = (DATA_DIR / "glue_landing_sample.xml").read_text(encoding="utf-8")

    guides = parse_service_landing_page(xml_text)
    urls = [guide.url for guide in guides]

    assert "https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html" in urls
    assert "https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html" in urls
    assert all("APIReference" not in url for url in urls)

    prefixes = {guide.allowed_prefix for guide in guides}
    assert "/glue/latest/dg/" in prefixes


def test_parse_service_landing_page_keeps_api_gateway_developer_guide() -> None:
    xml_text = (DATA_DIR / "apigateway_landing_sample.xml").read_text(encoding="utf-8")

    guides = parse_service_landing_page(xml_text)
    urls = [guide.url for guide in guides]

    assert "https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html" in urls
    assert all("apireference" not in url.lower() for url in urls)

    prefixes = {guide.allowed_prefix for guide in guides}
    assert "/apigateway/latest/developerguide/" in prefixes


def test_load_service_manifest_produces_expected_scopes() -> None:
    manifest_path = DATA_DIR / "sample_manifest.json"

    scopes = load_service_manifest(manifest_path)

    assert set(scopes) == {"cloudfront", "glue"}

    glue_scope = scopes["glue"]
    assert sorted(glue_scope.start_urls) == [
        "https://docs.aws.amazon.com/glue/latest/developerguide/index.html",
        "https://docs.aws.amazon.com/glue/latest/userguide/what-is-glue.html",
    ]
    assert set(glue_scope.allowed_prefixes) == {
        "/glue/latest/developerguide/",
        "/glue/latest/userguide/",
    }
