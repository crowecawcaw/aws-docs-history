

# OTel metrics pricing and storage
<a name="metrics-otel-pricing"></a>

OpenTelemetry metrics in CloudWatch use a per-GB ingestion model with included storage and query access. There are no per-metric, per-API-call, or separate storage charges. For current pricing details, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Key pricing characteristics
<a name="metrics-otel-pricing-characteristics"></a>

The OTel metrics pricing model has the following characteristics:
+ **Per-GB ingestion** — You pay based on the volume of data ingested, not the number of unique metric series.
+ **Storage included** — 15 months retention at no additional charge.
+ **Console queries free** — PromQL queries in the CloudWatch console (Query Studio, dashboards) are free.
+ **API queries charged per sample** — Programmatic PromQL queries are charged per million samples scanned.
+ **No per-metric charge** — Unlike Classic pricing, there is no cost per unique metric name or label combination.

## How OTel compares to Classic pricing
<a name="metrics-otel-pricing-comparison"></a>

The following table compares OTel metrics pricing with Classic metrics pricing.


| Feature | OTel Metrics | Classic Metrics | 
| --- | --- | --- | 
| Billing unit | Per GB ingested | Per metric per month | 
| Storage | 15 months included | 15 months included | 
| Console queries | Free | Free | 
| API queries | Per million samples scanned | Per 1,000 metrics requested (GetMetricData) | 
| High cardinality cost | Linear with data volume (not metric count) | Expensive — each unique dimension combination is a separate billable metric | 

## What counts as ingested data
<a name="metrics-otel-pricing-ingested-data"></a>

Each OTLP data point contributes its serialized size to the ingestion volume. The serialized size includes the following components:
+ Metric name
+ All labels (keys and values)
+ Resource attributes
+ Timestamp and value

Larger label sets produce more bytes per data point. You can monitor your ingestion volume in the CloudWatch console under Usage Metrics.

## Cost optimization tips
<a name="metrics-otel-pricing-optimization"></a>

Use the following strategies to optimize your OTel metrics costs:
+ Use shorter label values where possible. Label values contribute to the byte size of each data point.
+ Drop high-cardinality labels that you don't query (for example, request IDs) at the collector level.
+ For Container Insights OTel, the default collection generates a predictable volume based on cluster size.