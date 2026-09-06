

# Metrics in Amazon CloudWatch
<a name="working_with_metrics"></a>

Metrics are data about the performance of your systems. Amazon CloudWatch collects metrics through two paths: AWS vended metrics from services such as Amazon EC2, Amazon EBS, and Amazon RDS, and custom metrics that you publish using the OpenTelemetry Protocol (OTLP) or the CloudWatch API.

## Overview
<a name="metrics-overview"></a>

### OpenTelemetry: open-source native metrics in CloudWatch
<a name="metrics-overview-otel-intro"></a>

CloudWatch supports OpenTelemetry as the recommended path for metric ingestion and querying. You can use vendor-agnostic, open-source instrumentation to send metrics to CloudWatch – the same OTel SDKs and collectors that work with Prometheus, Grafana, and other backends work with CloudWatch out of the box.

### Two metric models
<a name="metrics-overview-comparison"></a>

CloudWatch supports two metric models. Both are fully supported – choose based on your needs:


|  | **[OpenTelemetry Metrics (Recommended)](metrics-otel-recommended.md)** | **[CloudWatch Metrics (Classic)](metrics-classic.md)** | 
| --- | --- | --- | 
| **Identity** | Metric name, up to 150 labels | Namespace, metric name, up to 30 dimensions | 
| **Metric types** | Gauge, sum, histogram, exponential histogram | Single values, statistic sets | 
| **Ingestion** | OTLP endpoint (OTel SDKs, collectors) | PutMetricData API, EMF | 
| **Query APIs** | PromQL query API | GetMetricData, GetMetricStatistics, ListMetrics, CloudWatch Metrics Insights (SQL) | 
| **Alarms** | PromQL-based CloudWatch alarms | Standard CloudWatch alarms | 
| **Console** | CloudWatch Query Studio | CloudWatch Metrics console | 
| **Pricing model** | Per GB ingested | Per metric per month | 
| **Storage** | Up to 15 months | Up to 15 months (with automatic rollup) | 
| **Metric names** | Open-source native | Proprietary (CloudWatch-format) | 
| **Best for** | New workloads, containers, high-cardinality | Existing integrations, low-cardinality AWS service metrics | 

GetMetricData, GetMetricStatistics, ListMetrics, and CloudWatch Metrics Insights operate only on CloudWatch Metrics (Classic). Use the PromQL query API for OpenTelemetry Metrics.

### Getting started
<a name="metrics-overview-getting-started"></a>
+ **New to CloudWatch metrics?** Start with [OpenTelemetry Metrics (Recommended)](metrics-otel-recommended.md).
+ **Already using PutMetricData or EMF?** See [CloudWatch Metrics (Classic)](metrics-classic.md).
+ **Want AWS service metrics in PromQL?** Enable [AWS vended metrics in OpenTelemetry format](CloudWatch-OTelEnrichment.md).