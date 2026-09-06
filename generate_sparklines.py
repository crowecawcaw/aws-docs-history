#!/usr/bin/env python3
"""Generate an SVG sparkline chart showing weekly lines added/removed per AWS service.

Usage:
    python generate_sparklines.py [--months N] [--cache FILE] [--output FILE]

The script runs `git log --numstat` to collect per-file change stats, groups them
by service and ISO week, then renders a compact SVG with stacked green/red bars
(log scale) for each service.

Options:
    --months N     Number of months of history to include (default: 6)
    --cache FILE   Path to a cached numstat dump. If the file doesn't exist, it
                   will be created. Reuse it to skip the slow git-log step.
    --output FILE  SVG output path (default: docs_activity.svg)
"""

import argparse
import math
import os
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from xml.sax.saxutils import escape


def get_git_numstat(since_date: str, cache_path: str | None = None) -> str:
    """Run git log --numstat and return raw output, optionally caching to disk."""
    if cache_path and os.path.exists(cache_path):
        print(f"Reading cached numstat from {cache_path}")
        with open(cache_path) as f:
            return f.read()

    print(f"Running git log --numstat --since={since_date} (this can take minutes on a partial clone)...")
    cmd = [
        "git", "-c", "core.commitGraph=false",
        "log", "--numstat",
        "-w", "--ignore-blank-lines",
        "--format=COMMIT %H %ad",
        "--date=short",
        f"--since={since_date}",
        "--", "docs/",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    if result.returncode != 0:
        # Allow partial output if it ends with a fetch error (disk-space issue on blobless clones)
        if result.stdout and "fatal:" in result.stderr:
            print(f"Warning: git log had errors but produced partial output: {result.stderr.splitlines()[-1]}",
                  file=sys.stderr)
        else:
            print(f"git log failed: {result.stderr}", file=sys.stderr)
            sys.exit(1)

    raw = result.stdout
    if cache_path:
        with open(cache_path, "w") as f:
            f.write(raw)
        print(f"Cached numstat to {cache_path}")
    return raw


def parse_numstat(raw: str) -> dict:
    """Parse numstat output, excluding each service's initial snapshot commit.

    The first commit for a service establishes its baseline.  In particular, it
    may contain a one-time formatting diff when the archive changes how it
    obtains Markdown, so counting it as documentation activity would add noise
    to the chart.
    """
    data = defaultdict(lambda: defaultdict(lambda: {"added": 0, "deleted": 0}))
    current_date = None
    current_commit = None
    commits = []
    commit_stats = None

    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("COMMIT "):
            parts = line.split()
            current_commit = parts[1]
            current_date = parts[2]  # YYYY-MM-DD
            commit_stats = defaultdict(lambda: {"added": 0, "deleted": 0})
            commits.append((current_commit, current_date, commit_stats))
            continue
        if line.startswith("fatal:"):
            continue
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        added_str, deleted_str, path = parts
        if added_str == "-" or deleted_str == "-":
            continue  # binary file
        if not path.startswith("docs/"):
            continue
        service = path.split("/")[1]
        commit_stats[service]["added"] += int(added_str)
        commit_stats[service]["deleted"] += int(deleted_str)

    # `git log` emits newest commits first, so the last commit encountered for
    # each service is its initial snapshot. Keep the service in the result (and
    # therefore in the chart), but do not count that baseline's line changes.
    initial_commits = {}
    for commit, _date, stats in commits:
        for service in stats:
            initial_commits[service] = commit
            data[service]

    for commit, commit_date, stats in commits:
        dt = datetime.strptime(commit_date, "%Y-%m-%d")
        week_start = dt - timedelta(days=dt.weekday())
        week_key = week_start.strftime("%Y-%m-%d")
        for service, changes in stats.items():
            if commit == initial_commits[service]:
                continue
            data[service][week_key]["added"] += changes["added"]
            data[service][week_key]["deleted"] += changes["deleted"]

    return data


def generate_svg(data: dict, weeks: list, output_path: str):
    """Generate the SVG sparkline chart."""
    services = sorted(data.keys(), key=str.lower)
    num_services = len(services)
    num_weeks = len(weeks)

    # Layout
    label_width = 160
    bar_width = 8
    bar_gap = 2
    chart_width = num_weeks * (bar_width + bar_gap)
    row_height = 22
    header_height = 16
    padding_x = 6
    padding_y = 4

    total_width = label_width + chart_width + padding_x * 2
    total_height = header_height + num_services * row_height + padding_y * 2

    # Compute net change (added - deleted) per service per week
    # Positive = net growth (green), negative = net shrink (red)
    nets = {}
    global_max = 1
    for service in services:
        nets[service] = {}
        for week in weeks:
            e = data[service].get(week, {"added": 0, "deleted": 0})
            net = e["added"] - e["deleted"]
            nets[service][week] = net
            global_max = max(global_max, abs(net))
    log_max = math.log1p(global_max)
    max_bar_h = row_height / 2 - 1  # max height per half-bar

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="{total_height}">')
    svg.append('<style>')
    svg.append('  text { font-family: ui-monospace, "Cascadia Mono", "Segoe UI Mono", "Liberation Mono", Menlo, Monaco, Consolas, monospace; }')
    svg.append('  .svc { font-size: 7px; fill: #555; }')
    svg.append('  .month { font-size: 7px; fill: #999; }')
    svg.append('  .bar-add { fill: #3fb950; }')
    svg.append('  .bar-del { fill: #f85149; }')
    svg.append('  .row-even { fill: #f6f8fa; }')
    svg.append('</style>')
    svg.append(f'<rect width="{total_width}" height="{total_height}" fill="white"/>')

    # Month headers
    chart_x = padding_x + label_width
    prev_month = None
    for i, week in enumerate(weeks):
        dt = datetime.strptime(week, "%Y-%m-%d")
        month_label = dt.strftime("%b")
        if month_label != prev_month:
            x = chart_x + i * (bar_width + bar_gap)
            svg.append(f'<text x="{x}" y="{padding_y + 10}" class="month">{month_label}</text>')
            prev_month = month_label

    # Service rows
    for row_idx, service in enumerate(services):
        y_base = padding_y + header_height + row_idx * row_height
        y_mid = y_base + row_height / 2

        if row_idx % 2 == 0:
            svg.append(f'<rect x="0" y="{y_base}" width="{total_width}" height="{row_height}" class="row-even"/>')

        display = escape(service if len(service) <= 24 else service[:22] + "..")
        svg.append(f'<text x="{padding_x}" y="{y_mid + 2.5}" class="svc">{display}</text>')

        for i, week in enumerate(weeks):
            net = nets[service].get(week, 0)
            if net == 0:
                continue
            x = chart_x + i * (bar_width + bar_gap)
            h = max(0.5, (math.log1p(abs(net)) / log_max) * max_bar_h)
            if net > 0:
                svg.append(f'<rect x="{x}" y="{y_mid - h:.1f}" width="{bar_width}" height="{h:.1f}" class="bar-add"/>')
            else:
                svg.append(f'<rect x="{x}" y="{y_mid:.1f}" width="{bar_width}" height="{h:.1f}" class="bar-del"/>')

    svg.append('</svg>')

    with open(output_path, "w") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path} ({num_services} services, {num_weeks} weeks, {total_width}x{total_height}px)")


SVG_MARKER_START = "<!-- sparkline-start -->"
SVG_MARKER_END = "<!-- sparkline-end -->"


def update_readme(svg_path: str, readme_path: str = "README.md"):
    """Embed the SVG in the README between marker comments."""
    with open(readme_path) as f:
        readme = f.read()

    section = f"""{SVG_MARKER_START}
## Documentation activity

Net lines changed per service per week over the last 6 months, excluding each
service's initial snapshot. Bar heights use a log scale. Green = net lines
added, red = net lines removed.

![Documentation activity](docs_activity.svg)
{SVG_MARKER_END}"""

    if SVG_MARKER_START in readme:
        import re
        readme = re.sub(
            rf"{re.escape(SVG_MARKER_START)}.*?{re.escape(SVG_MARKER_END)}",
            section,
            readme,
            flags=re.DOTALL,
        )
    else:
        # Insert before the licensing section
        insert_before = "## Licensing"
        if insert_before in readme:
            readme = readme.replace(insert_before, section + "\n\n" + insert_before)
        else:
            readme += "\n\n" + section

    with open(readme_path, "w") as f:
        f.write(readme)
    print(f"Updated {readme_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate SVG sparkline chart of AWS docs changes")
    parser.add_argument("--months", type=int, default=6, help="Months of history (default: 6)")
    parser.add_argument("--cache", type=str, default=None, help="Path to cache numstat output")
    parser.add_argument("--output", type=str, default="docs_activity.svg", help="SVG output path")
    parser.add_argument("--update-readme", action="store_true", help="Embed SVG in README.md")
    args = parser.parse_args()

    # Use the later of N months ago or 2025-12-01 (before that is bulk initial imports)
    earliest = "2025-12-01"
    months_ago = (datetime.now() - timedelta(days=args.months * 30)).strftime("%Y-%m-%d")
    since = max(earliest, months_ago)
    raw = get_git_numstat(since, args.cache)

    print("Parsing...")
    data = parse_numstat(raw)

    all_weeks = set()
    for service_data in data.values():
        all_weeks.update(service_data.keys())
    weeks = sorted(all_weeks)

    generate_svg(data, weeks, args.output)

    if args.update_readme:
        update_readme(args.output)


if __name__ == "__main__":
    main()
