import pytest

from pathlib import Path

from crawler import build_local_image_path, IMAGE_PATH_PREFIX


def test_build_local_image_path_places_asset_within_output(tmp_path: Path) -> None:
    output_root = tmp_path / "docs"
    image_path = "/images/deadline-cloud/latest/userguide/images/monitor-job-status.png"

    local_path = build_local_image_path(image_path, output_root)

    assert local_path == output_root / "deadline-cloud/latest/userguide/images/monitor-job-status.png"


def test_build_local_image_path_rejects_missing_prefix(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        build_local_image_path("/assets/example.png", tmp_path)


def test_build_local_image_path_ignores_traversal(tmp_path: Path) -> None:
    image_path = f"{IMAGE_PATH_PREFIX}../deadline-cloud/./latest/userguide/images/example.png"

    local_path = build_local_image_path(image_path, tmp_path)

    assert local_path == tmp_path / "deadline-cloud/latest/userguide/images/example.png"
