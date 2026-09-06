# CloudWatch OpenTelemetry Metrics

OpenTelemetry metrics in CloudWatch use the OpenTelemetry Protocol (OTLP) for ingestion
and PromQL for querying. This model supports open-source metric names, up to 150 labels
per data point, and includes 15 months of storage with no per-metric charges.

Use OpenTelemetry metrics when:

- You are starting new workloads and want the recommended path
- You need high-cardinality labels (pod names, custom tags, OTel semantic
  conventions)
- You want to query with PromQL (industry-standard, compatible with existing
  Grafana dashboards)
- You use Container Insights OTel, Application Signals, or AWS vended OTel
  metrics

## In this section

| Page                                                                                                      | Description                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Publish custom metrics with OpenTelemetry](metrics-otel-send.md "metrics-otel-send.md")                  | Publish custom metrics through the OTLP endpoint using OTel<br>SDKs or collectors                                                                                                                                                                                                                 |
| [AWS vended metrics in OpenTelemetry format](CloudWatch-OTelEnrichment.md "CloudWatch-OTelEnrichment.md") | Enable AWS services to publish metrics as OTel data<br>points with resource tags. Uses OTel Vended Metric Enrichment to<br>convert existing AWS service metrics (Amazon EC2, Amazon RDS, ELB, and so on)<br>into the OTel path with full label enrichment — no agent or<br>code changes required. |
| [Query metrics with PromQL](CloudWatch-PromQL.md "CloudWatch-PromQL.md")                                  | Query, aggregate, and filter OTel metrics using the<br>Prometheus Query Language                                                                                                                                                                                                                  |
| [OTel metrics pricing and storage](metrics-otel-pricing.md "metrics-otel-pricing.md")                     | Per-GB ingestion pricing, included 15-month retention, no<br>per-metric or API charges                                                                                                                                                                                                            |
| [Migrate from Classic to OTel metrics](metrics-otel-migrate.md "metrics-otel-migrate.md")                 | Incremental migration from PutMetricData/EMF to<br>OTLP                                                                                                                                                                                                                                           |
