# Spans

Spans sent to X-Ray are ingested and managed in a log group called `aws/spans`.
This topic describes which CloudWatch Logs features are available for transaction spans.

###### Available features

The following CloudWatch Logs features are available for transaction spans.

- [Metric filters](../logs/MonitoringLogData.md "../logs/MonitoringLogData.md") – Use metric filters to extract custom metrics from spans.
- [Subscriptions](../logs/Subscriptions.md "../logs/Subscriptions.md") – Use subscriptions to access a real-time feed of span events from CloudWatch Logs.
- [Log outlier detection](../logs/LogsAnomalyDetection.md "../logs/LogsAnomalyDetection.md") – Use log outlier detection to establish a baseline for spans sent to the `aws/spans` log group.
- [Contributor Insights](ContributorInsights.md "ContributorInsights.md") – Use Contributor Insights to analyze span data and create a time series displaying contributor data.

###### Unsupported features

The following are features not supported for transaction spans.

- Spans cannot be sent to CloudWatch Logs with the `PutLogEvents` API.
- Span data cannot be [enriched or transformed](../logs/CloudWatch-Logs-Transformation.md "../logs/CloudWatch-Logs-Transformation.md").

###### Note

Span ingestion is charged separately from log ingestion.
For information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
