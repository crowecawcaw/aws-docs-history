# Metrics in Amazon CloudWatch

Metrics are data about the performance of your systems. By default, many services provide
free metrics for resources (such as Amazon EC2 instances, Amazon EBS volumes, and Amazon RDS DB instances). You
can also enable detailed monitoring for some resources, such as your Amazon EC2 instances, or publish
your own application metrics. Amazon CloudWatch can load all the metrics in your account (both AWS
resource metrics and application metrics that you provide) for search, graphing, and
alarms.

Metric data is kept for 15 months, enabling you to view both up-to-the-minute data and
historical data.

To graph metrics in the console, you can use CloudWatch Metrics Insights, a high-performance SQL query engine that
you can use to identify trends and patterns within all your metrics in real time. CloudWatch Metrics Insights supports
querying up to two weeks of historical data, enabling comprehensive analysis of metric trends.

###### Topics

- [Metrics concepts](cloudwatch_concepts.md "cloudwatch_concepts.md")
- [Basic monitoring and detailed monitoring in CloudWatch](cloudwatch-metrics-basic-detailed.md "cloudwatch-metrics-basic-detailed.md")
- [Query your CloudWatch metrics with CloudWatch Metrics Insights](query_with_cloudwatch-metrics-insights.md "query_with_cloudwatch-metrics-insights.md")
- [Use metrics explorer to monitor resources by their tags and properties](CloudWatch-Metrics-Explorer.md "CloudWatch-Metrics-Explorer.md")
- [Use metric streams](CloudWatch-Metric-Streams.md "CloudWatch-Metric-Streams.md")
- [View available metrics](viewing_metrics_with_cloudwatch.md "viewing_metrics_with_cloudwatch.md")
- [Graphing metrics](graph_metrics.md "graph_metrics.md")
- [Using CloudWatch outlier detection](CloudWatch_Anomaly_Detection.md "CloudWatch_Anomaly_Detection.md")
- [Using math expressions with CloudWatch metrics](using-metric-math.md "using-metric-math.md")
- [Use search expressions in graphs](using-search-expressions.md "using-search-expressions.md")
- [Get statistics for a metric](getting-metric-statistics.md "getting-metric-statistics.md")
- [Publish custom metrics](publishingMetrics.md "publishingMetrics.md")
