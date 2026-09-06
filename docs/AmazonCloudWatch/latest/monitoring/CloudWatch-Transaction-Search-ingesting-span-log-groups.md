

# Spans
<a name="CloudWatch-Transaction-Search-ingesting-span-log-groups"></a>

 Spans sent to X-Ray are ingested and managed in a log group called `aws/spans`. This topic describes which CloudWatch Logs features are available for transaction spans. 

**Available features**  
 The following CloudWatch Logs features are available for transaction spans. 
+  [Metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) – Use metric filters to extract custom metrics from spans. 
+  [Subscriptions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html) – Use subscriptions to access a real-time feed of span events from CloudWatch Logs. 
+  [Log anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html) – Use log anomaly detection to establish a baseline for spans sent to the `aws/spans` log group. 
+  [Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) – Use Contributor Insights to analyze span data and create a time series displaying contributor data. 

**Unsupported features**  
 The following are features not supported for transaction spans. 
+  Spans cannot be sent to CloudWatch Logs with the `PutLogEvents` API. 
+  Span data cannot be [enriched or transformed](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html). 

**Note**  
 Span ingestion is charged separately from log ingestion. For information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/). 