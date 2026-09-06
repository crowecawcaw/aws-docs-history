

# Log classes
<a name="CloudWatch_Logs_Log_Classes"></a>

CloudWatch Logs offers two classes of log groups:
+ The *CloudWatch Logs Standard* log class is a full-featured option for logs that require real-time monitoring or logs that you access frequently.
+ The *CloudWatch Logs Infrequent Access* log class is a new log class that you can use to cost-effectively consolidate your logs. This log class offers a subset of CloudWatch Logs capabilities including managed ingestion, storage, cross-account log analytics, and encryption with a lower ingestion price per GB. The Infrequent Access log class is ideal for ad-hoc querying and after-the-fact forensic analysis on infrequently accessed logs.

**Note**  
For charges, the Standard and Infrequent Access log classes differ in ingestion costs only. Storage charges and CloudWatch Logs Insights charges are the same in each log class.

For more information about CloudWatch Logs pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

**Important**  
After a log group is created, its log class can't be changed.

## Supported features
<a name="Log_Class_Features"></a>

The following table lists the features for each log class.


| Feature | Standard | Infrequent Access | 
| --- | --- | --- | 
| Fully managed log ingestion and storage | Yes ✓ | Yes ✓ | 
| [ Cross-account features](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html)  | Yes ✓ | Yes ✓ | 
| [Encryption with AWS KMS](encrypt-log-data-kms.md) | Yes ✓ | Yes ✓ | 
| [CloudWatch Logs Insights query commands](AnalyzingLogData.md) | Yes ✓ | Yes ✓ (Most commands– see [Logs Insights QL commands supported in log classes](CWL_AnalyzeLogData_Classes.md).) | 
| [CloudWatch Logs Insights discovered fields](CWL_AnalyzeLogData-discoverable-fields.md) | Yes ✓ | Yes ✓ | 
| [Facets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Facets.html) | Yes ✓ | No | 
| [Using CloudWatch Pipeline to transform logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-pipelines.html) | Yes ✓ | Yes ✓ | 
| [Export to Amazon S3](S3Export.md) | Yes ✓ | Yes ✓ | 
| [S3 Tables Integration](s3-tables-integration.md) | Yes ✓ | Yes ✓ | 
| [Scheduled Queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ScheduledQueries.html) | Yes ✓ | Yes ✓ | 
| [Using OpenSearch PPL or OpenSearch SQL to query in CloudWatch Logs Insights;](AnalyzingLogData.md) | Yes ✓ | Yes ✓ | 
|  [Natural language query assist](CloudWatchLogs-Insights-Query-Assist.md)  | Yes ✓ | No | 
| [CloudWatch Logs Anomaly Detection](LogsAnomalyDetection.md) | Yes ✓ | No | 
| [Live Tail](CloudWatchLogs_LiveTail.md) | Yes ✓ | No | 
| [Field indexing](CloudWatchLogs-Field-Indexing.md) | Yes ✓ | No | 
| [Compare to previous time range](CWL_AnalyzeLogData_Compare.md) | Yes ✓ | No | 
| [Subscription filters](Subscriptions.md) | Yes ✓ | No | 
| [GetLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html) and [FilterLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html) API operations | Yes ✓ | Not supported. Use CloudWatch Logs Insights to view log events stored in log groups in the Infrequent Access log class. | 
| [Metric filters](MonitoringLogData.md) | Yes ✓ | No | 
| [Container Insights log ingestion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html)  | Yes ✓ | No | 
| [Lambda Insights log ingestion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html)  | Yes ✓ | No | 
| [Sensitive data protection with masking](mask-sensitive-log-data.md) | Yes ✓ | Yes ✓ | 
| [Embedded metrics format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html)  | Yes ✓ | No | 

**Note**  
In addition to these two log classes, there is a `Delivery` log class. Use the `Delivery` log class only for delivering AWS Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for two days. This retention period is fixed and cannot be changed. This log class doesn't offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries. 