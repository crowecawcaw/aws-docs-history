# Metrics in Amazon CloudWatch

Metrics are data about the performance of your systems. Amazon CloudWatch collects metrics through
two paths: AWS vended metrics from services such as Amazon EC2, Amazon EBS, and Amazon RDS, and custom
metrics that you publish using the OpenTelemetry Protocol (OTLP) or the CloudWatch API. Many AWS
services provide free metrics for resources by default. You can also enable detailed monitoring
for some resources, such as Amazon EC2 instances.

CloudWatch supports two query languages for metrics. The Prometheus Query Language (PromQL)
provides flexible analytics for OpenTelemetry metrics and AWS vended metrics published in
OpenTelemetry format. CloudWatch Metrics Insights provides a SQL-based query engine for traditional CloudWatch metrics. Both
support graphing, dashboards, and alarms.

Key Topics:

- [Metrics concepts](cloudwatch_concepts.md "cloudwatch_concepts.md")
- [Basic monitoring and detailed monitoring in CloudWatch](cloudwatch-metrics-basic-detailed.md "cloudwatch-metrics-basic-detailed.md")
- [Publish custom metrics](publishingMetrics.md "publishingMetrics.md")
- [Send metrics using OpenTelemetry (new)](CloudWatch-OpenTelemetry-Sections.md "CloudWatch-OpenTelemetry-Sections.md")
- [Publish AWS vended metrics as OpenTelemetry metrics (new)](publishingMetrics.md "publishingMetrics.md")
- [Query metrics with PromQL (new)](CloudWatch-PromQL.md "CloudWatch-PromQL.md")
- [Query your CloudWatch metrics with CloudWatch Metrics Insights](query_with_cloudwatch-metrics-insights.md "query_with_cloudwatch-metrics-insights.md")
- [Use metrics explorer to monitor resources by their tags and properties](CloudWatch-Metrics-Explorer.md "CloudWatch-Metrics-Explorer.md")
- [Use metric streams](CloudWatch-Metric-Streams.md "CloudWatch-Metric-Streams.md")
- [View available metrics](viewing_metrics_with_cloudwatch.md "viewing_metrics_with_cloudwatch.md")
- [Graphing metrics](graph_metrics.md "graph_metrics.md")
- [Using CloudWatch anomaly detection](CloudWatch_Anomaly_Detection.md "CloudWatch_Anomaly_Detection.md")
- [Using math expressions with CloudWatch metrics](using-metric-math.md "using-metric-math.md")
- [Use search expressions in graphs](using-search-expressions.md "using-search-expressions.md")
- [Get statistics for a metric](getting-metric-statistics.md "getting-metric-statistics.md")
