from generate_sparklines import parse_numstat


def test_parse_numstat_excludes_initial_commit_for_each_service():
    raw = """COMMIT newest 2026-09-13
3\t1\tdocs/s3/latest/page.md
5\t2\tdocs/ec2/latest/page.md
COMMIT s3-baseline 2026-09-06
100\t0\tdocs/s3/latest/page.md
COMMIT ec2-baseline 2026-08-30
200\t0\tdocs/ec2/latest/page.md
"""

    data = parse_numstat(raw)

    assert data["s3"]["2026-09-07"] == {"added": 3, "deleted": 1}
    assert data["ec2"]["2026-09-07"] == {"added": 5, "deleted": 2}
    assert "2026-08-31" not in data["s3"]
    assert "2026-08-24" not in data["ec2"]


def test_parse_numstat_retains_service_with_only_baseline_commit():
    raw = """COMMIT baseline 2026-09-06
100\t0\tdocs/s3/latest/page.md
"""

    data = parse_numstat(raw)

    assert "s3" in data
    assert not data["s3"]
