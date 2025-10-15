# Image support plan

## Observed image usage in existing Markdown

* `using-usage-explorer.md` embeds two illustrative charts stored under `/images/deadline-cloud/latest/userguide/images/`, indicating that rich screenshots live alongside the guide hierarchy in the upstream docs, while a generic warning icon is loaded from a CloudFront CDN URL.【F:docs/deadline-cloud/latest/userguide/using-usage-explorer.md†L76-L110】
* `build-job-bundle.md` contains a submitter UI screenshot referenced from `/images/deadline-cloud/latest/developerguide/images/`, showing that developer guide content follows the same structure.【F:docs/deadline-cloud/latest/developerguide/build-job-bundle.md†L27-L43】
* `storage-virtual.md` includes a workflow screenshot located beneath the `userguide/images/` directory, reinforcing that substantive imagery is hosted at service-scoped paths under `/images/...` while note and warning callouts use shared CDN assets.【F:docs/deadline-cloud/latest/userguide/storage-virtual.md†L1-L44】

These examples suggest a consistent pattern: primary documentation images live on the `docs.aws.amazon.com` origin under a service-specific `/images/<service>/<version>/<guide>/images/` prefix, whereas ancillary icons are loaded from `https://d1ge0kk1l5kms0.cloudfront.net/`.

## Proposed crawling workflow changes

1. **Collect candidate images from the main content**
   * After locating the `<main>` element (or fallback container), enumerate descendant `<img>` tags before Markdown conversion.
   * Normalize each `src` against the page URL to obtain an absolute URL so we can evaluate host and path unambiguously.

2. **Filter to "main" documentation images**
   * Retain only images hosted on `docs.aws.amazon.com` whose paths start with `/images/`. This keeps the charts and screenshots shown in the guides while excluding header/nav artwork and the CDN-hosted alert icons observed above.
   * Optionally enforce common raster extensions (`.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`) to avoid other asset types.
   * Skip anything larger than a reasonable size limit (for example 10 MB) to prevent pathological downloads.

3. **Download and persist images**
   * Mirror the remote folder structure underneath a new `docs/images/` root (for example `docs/images/deadline-cloud/latest/userguide/images/cost-explorer-graph.png`). This mirrors the upstream hierarchy, avoids filename collisions, and keeps screenshots co-located by guide and version.
   * Ensure directories are created before writing, and reuse cached files when a subsequent crawl encounters the same image URL (skip download if the file already exists and matches the expected checksum/size).

4. **Rewrite Markdown to reference local assets**
   * Before running `markdownify`, mutate qualifying `<img>` tags so that `src` points to the relative path from the Markdown file to the stored image (for example `images/cost-explorer-graph.png` for files inside `docs/deadline-cloud/latest/userguide/`).
   * Let `markdownify` convert the updated HTML, producing Markdown that references the local copies. Alt text supplied by AWS Docs will be preserved automatically.

5. **Track downloaded images**
   * Record image URLs in the crawl manifest used for HTML pages so we avoid duplicate fetches and have provenance data for debugging.

## Future considerations

* Some guides may embed diagrams hosted outside the `/images/` prefix. We can expand the allowlist incrementally as we encounter legitimate examples.
* If other services are added, their screenshots should naturally fall under `docs/images/<service>/...`, keeping the storage layout consistent across products.
