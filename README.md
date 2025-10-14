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
  - Accepts a configuration file (list of URLs, services, or sitemaps) to allow
    new sources to be added without code changes.
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

## Daily Run Sequence
1. Workflow triggers and installs runtime dependencies.
2. Crawler ingests configured AWS documentation endpoints.
3. Conversion utility transforms each document into Markdown files.
4. Markdown files saved under directories that mirror the source URL paths and
   validated (lint, front-matter checks).
5. Git status inspected; if changes exist, commit with message
   `chore: update aws docs`.
6. Push commit to the repository, allowing downstream consumers to track changes.

## Task Breakdown
1. **Repository setup**
   - Define directory structure for raw downloads and Markdown archives.
   - Add `.gitignore`, linting config, and dependency pinning (`requirements.txt`).
2. **Crawler implementation**
   - Determine list of documentation sources (manual list or sitemap discovery).
   - Build downloader with concurrency, error handling, and caching/etag support.
   - Write tests or scripts to validate fetching logic.
3. **Markdown conversion pipeline**
   - Copy or import the `util.py` conversion helpers into the repo.
   - Wrap conversion in a CLI (e.g., `python -m aws_docs.convert`) for reuse.
   - Add formatting rules, metadata enrichment, and unit tests for conversions.
4. **Archival and metadata management**
   - Implement deterministic file naming and directory structure.
   - Generate daily manifest/index files summarizing captured pages.
   - Provide scripts to diff historical Markdown outputs.
5. **Automation workflow**
   - Create GitHub Actions YAML with scheduled trigger, dependency setup, and
     secrets management (PAT or GitHub token for pushing).
   - Add steps to upload workflow logs/artifacts and notify on failure.
6. **Documentation**
   - Expand this README with configuration instructions and troubleshooting tips.
   - Document process for adding new pages/services and testing locally.
7. **Future enhancements** (optional backlog)
   - Add change detection heuristics to avoid committing identical content.
   - Integrate with issue tracking or Slack notifications.
   - Build dashboard summarizing documentation change history.

