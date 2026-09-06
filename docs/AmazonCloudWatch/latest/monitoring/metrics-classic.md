

# CloudWatch Metrics (Classic)
<a name="metrics-classic"></a>

CloudWatch Metrics (Classic) uses the `PutMetricData` API and embedded metric format (EMF) for ingestion, and provides CloudWatch Metrics Insights (SQL-based queries) for analysis. Classic metrics support up to 30 dimensions per metric with per-metric-per-month pricing.

Use Classic metrics when you have existing integrations with the CloudWatch API, need compatibility with AWS service metrics that are not yet available in OpenTelemetry format, or prefer SQL-based querying with CloudWatch Metrics Insights.

**Topics**
+ [Metrics concepts](cloudwatch_concepts.md)
+ [Basic monitoring and detailed monitoring in CloudWatch](cloudwatch-metrics-basic-detailed.md)
+ [Publish custom metrics (PutMetricData / EMF)](publishingMetrics.md)
+ [Query your CloudWatch metrics with CloudWatch Metrics Insights](query_with_cloudwatch-metrics-insights.md)
+ [View available metrics](viewing_metrics_with_cloudwatch.md)
+ [Retrieve metric data (GetMetricData)](metrics-classic-getdata.md)
+ [Get statistics for a metric (GetMetricStatistics)](getting-metric-statistics.md)
+ [Use metrics explorer to monitor resources by their tags and properties](CloudWatch-Metrics-Explorer.md)
+ [Use search expressions in graphs](using-search-expressions.md)
+ [Use metric streams](CloudWatch-Metric-Streams.md)
+ [Math expressions with metrics](using-metric-math.md)
+ [Using CloudWatch anomaly detection](CloudWatch_Anomaly_Detection.md)
+ [Grafana integration](CloudWatch-Grafana-support.md)
+ [AWS services that publish CloudWatch metrics](aws-services-cloudwatch-metrics.md)