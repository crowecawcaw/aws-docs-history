# AWS Docs History Automation

## Overview
This repository will host the automation for capturing, converting, and archiving
AWS documentation on a daily schedule. A GitHub Actions workflow will
orchestrate crawling the latest AWS documentation pages, converting the raw
content to Markdown, and committing the results back into the repository.

## High-Level Workflow
1. **Schedule trigger** &mdash; A GitHub Actions workflow runs once per day.
2. **Documentation crawl** &mdash; The workflow executes a crawler that pulls the
   desired set of AWS documentation pages (HTML or JSON sources).
3. **Conversion to Markdown** &mdash; Retrieved documents are converted to Markdown
   using the conversion utilities derived from the
   [`aws_documentation_mcp_server` utility module](https://github.com/awslabs/mcp/blob/main/src/aws-documentation-mcp-server/awslabs/aws_documentation_mcp_server/util.py).
4. **Archiving** &mdash; The Markdown output is organized to mirror the AWS
   documentation URL paths and checked into the repository.
5. **Change tracking** &mdash; The workflow commits the day's updates and pushes them
   to the repository, providing an auditable history of documentation changes.

## Architecture Components
- **Crawler**
  - Responsible for downloading the target AWS documentation pages.
  - Accepts CLI flags for start URLs and allowed path prefixes so additional
    services can be added without modifying the code.
  - Outputs raw HTML (or intermediate JSON) to a staging directory for
    conversion.
- **Markdown Conversion Utility**
  - Imports or vendored copy of the `convert_html_to_markdown` logic from the
    MCP utility module to ensure consistent formatting.
  - Applies post-processing (front matter, metadata, link normalization) to make
    generated Markdown easy to diff.
- **Repository Storage Layout**
  - Mirror the AWS documentation URL hierarchy when writing Markdown
    (e.g., `service/latest/userguide/topic.html` becomes
    `service/latest/userguide/topic.md`).
  - Avoid encoding timestamps in filenames; rely on Git history for temporal
    diffs.
  - Maintain manifests (e.g., `index.json`) describing the pages captured each
    run for quick lookups.
- **GitHub Actions Workflow**
  - Scheduled via cron expression (e.g., `0 2 * * *`).
  - Sets up dependencies (Python, requests/beautifulsoup/markdown-it, etc.).
  - Runs crawler, conversion, and git commit/push steps with an automation token.
  - Optionally opens issues or sends alerts if crawl fails or produces large diffs.
- **Observability & Reliability**
  - Log key events (start/end times, counts of pages fetched, failures).
  - Store crawl artifacts to ease debugging (e.g., upload raw HTML as workflow
    artifacts for failed runs).
  - Add basic retry/backoff logic around network requests.

## Manually triggering the GitHub Actions workflow

The documentation crawler workflow can be triggered manually from the GitHub Actions UI:

1. Go to the "Actions" tab in the repository
2. Select the "Docs crawler" workflow
3. Click "Run workflow"
4. Optionally specify a service ID to crawl only that service (e.g., `a2c`, `account`, `s3`)
5. Leave the service field empty to crawl all services

When a specific service ID is provided, the workflow will only crawl documentation for that service. When left empty, it will crawl all services defined in the manifest.

The daily scheduled crawler will always crawl all services regardless of this setting.

## Running the crawler locally

Install the Python dependencies listed in `requirements.txt` and then execute
the crawler. The defaults will start at representative entry points for the
Deadline Cloud, Amazon S3, and AWS CloudFormation developer guides and API
references while restricting the crawl to the corresponding documentation
trees:

```bash
python crawler.py
```

You can provide your own seed URLs or limit the crawl scope by supplying one or
more `--start-url` and `--allowed-prefix` arguments:

```bash
python crawler.py \
  --start-url https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/Welcome.html \
  --allowed-prefix /deadline-cloud/latest/APIReference/
```

Only Markdown output should be committed back to the repository once the crawl
has completed and the generated docs have been reviewed.

The default crawl scope is defined in `crawler.py` under
`DEFAULT_SERVICE_SCOPES`. Each entry lists the seed URLs and allowed path
prefixes for a given service so new services can be added by updating that
mapping instead of modifying the crawler logic.

## Running the test suite

Install the project dependencies and then execute `pytest` from the repository
root to run the automated tests:

```bash
python -m pip install -r requirements.txt
pytest
```

All pull requests run the test suite automatically through a GitHub Actions
workflow to prevent regressions.

