

# Performance and latency best practices

`StartDocumentInsights` is asynchronous. End-to-end time is the time from submitting a job until it reaches `SUCCEEDED`, not a single synchronous call. Latency scales with how much work the job configuration asks for. This page explains what drives latency and how to reduce it.

## What affects latency
<a name="insights-performance-factors"></a>

The following factors increase the time a job takes to reach `SUCCEEDED`.
+ **Document size (pages).** Processing time grows with page count. A large multi-page file, or a large segment after splitting, takes proportionally longer because inference runs across the pages.
+ **Number of capabilities enabled.** Each capability you turn on adds work: extraction, custom extraction against a blueprint, document splitting, blueprint matching across several blueprints, and PII detection and redaction each add processing. A project with all of them enabled is slower than an extraction-only project on the same document.
+ **Extraction granularity and output formats.** Requesting more `Granularity.Types` (adding `LINE`, `WORD`, and `ELEMENT` on top of `PAGE` and `DOCUMENT`) and enabling additional `OutputFormat` types (Markdown, HTML, CSV) produces more output and increases processing time.
+ **Blueprint matching.** Attaching multiple blueprints requires the service to classify each document before extraction, which adds a step compared with a single known blueprint.
+ **Cross-Region routing under load.** During peak demand, cross-Region inference routes work to the most available AWS Region for resilience. This improves overall throughput, but an individual job can see variable latency. See [Cross-Region inference](insights-cross-region.md) for more information on where your inference can be routed based on source AWS Region.

## Reducing latency
<a name="insights-performance-reducing"></a>

To reduce latency, apply the following practices.
+ **Enable only the capabilities you need.** If you only need custom extraction, keep the extraction configuration minimal (for example, `BoundingBox` disabled with `PAGE` granularity) rather than enabling every granularity and output format.
+ **Keep granularity and output formats minimal.** Add `LINE`, `WORD`, or `ELEMENT` granularity and extra text formats only when a downstream consumer uses them.
+ **Use a single known blueprint when the document type is fixed.** Reserve multi-blueprint matching for mixed document types. One blueprint per project avoids the classification step.
+ **Split large files into smaller inputs** where practical, so individual jobs process fewer pages.

## When a job is slower than expected
<a name="insights-performance-slow"></a>

First check the page count and the number of capabilities enabled. Then reduce granularity and output formats, or split large files into smaller inputs. Because jobs are asynchronous, design your client to poll with a backoff rather than blocking, and remember that each job type has an open-job quota (see [Limits and quotas](insights-quotas.md)).