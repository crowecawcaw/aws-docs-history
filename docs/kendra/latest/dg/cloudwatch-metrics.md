

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Monitoring Amazon Kendra with Amazon CloudWatch
<a name="cloudwatch-metrics"></a>

To track the health of your indexes, use Amazon CloudWatch. With CloudWatch, you can get metrics for document synchronization for your index. You can also set up CloudWatch alarms to be notified when one or more metrics exceeds a threshold that you define. For example, you can monitor the number of documents submitted to be indexed or the number of documents that failed to be indexed.

You must have the appropriate CloudWatch permissions to monitor Amazon Kendra with CloudWatch. For more information, see [Authentication and Access Control for Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) in the *Amazon CloudWatch User Guide*.

## Viewing Amazon Kendra metrics
<a name="viewing-metrics"></a>

View Amazon Kendra metrics using the CloudWatch console.

**To view metrics (CloudWatch console)**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Metrics**, choose **All Metrics** and then choose **Kendra**.

1. Choose the dimension, choose a metric name, then choose **Add to graph**.

1. Choose a value for the date range. The metric count for the selected date range is displayed in the graph.

## Creating an alarm
<a name="cloudwatch-alarms"></a>

A CloudWatch alarm watches a single metric over a specified time period and performs one or more actions: sending a notification to an Amazon Simple Notification Service (Amazon SNS) top or Auto Scaling policy. The actions or actions are based on the value of the metric relative to a given threshold over a number of time periods that you specify. CloudWatch can also send you an Amazon SNS message when the alarm changes state.

CloudWatch alarms invoke actions only when the state changes and has persisted for the period that you specify.

**To set an alarm**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Alarms** and then choose **Create alarm**.

1. Select a metric. Choose a **Kendra** metric for your index and data source. Also set the time as set number of hours, days, weeks, or custom.

1. Choose your statistic. For example, **Average**. Also choose your alarm trigger time period as a set number of minutes, hours, per day, or custom.

1. Choose your threshold to trigger the alarm, whether to use a static value or a band and the condition to meet for the threshold.

1. Choose the alarm state for the trigger, whether the metric must fall outside your set threshold, or another state. Select who/which email to send the alarm notification to.

1. If you are satisfied with the alarm, choose **Create alarm**.

**Note**  
You must provide a name for your CloudWatch alarm.

## CloudWatch Metrics for index synchronization Jobs
<a name="cloudwatch-metric-sync-jobs"></a>

The following table describes the Amazon Kendra metrics for data source synchronization jobs.

If you use the API or CLI, you must specify the `Namespace` as 'AWS/Kendra' in addition to the `MetricName` of your choice when using [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) API.


| Metric | Description | 
| --- | --- | 
| DocumentsCrawled | The number of documents that the synchronization job scanned or discovered during the run.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsSubmittedForIndexing | The number of documents that the synchronization job submitted to the index.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsSubmittedForIndexingFailed | The number of documents that failed indexing. Check the contents of the CloudWatch log for the synchronization job for details.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsSubmittedForDeletion | The number of documents that the synchronization job asked to be removed from the index.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsSubmittedForDeletionFailed | The number of documents that failed to be deleted. Check the contents of the CloudWatch log for the synchronization job for details.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 

## Metrics for Amazon Kendra data sources
<a name="cloudwatch-metrics-data-source"></a>

The following table describes the Amazon Kendra metrics for data source synchronization jobs. Metrics marked with an asterisk (\*) are used only for Amazon S3 data sources.

If you use the API or CLI, you must specify the `Namespace` as 'AWS/Kendra' in addition to the `MetricName` of your choice when using [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) API.


| Metric | Description | 
| --- | --- | 
| DocumentsSkippedNoChange \* | The number of documents examined and found not to have changed so they weren't submitted for indexing.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsSkippedInvalidMetadata \* | The number of documents skipped because there was a problem with the associated metadata file. Check the contents of the CloudWatch log for the synchronization run for details.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsCrawled | The number of document files examined.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsSubmittedForDeletion | The number of documents examined that were deleted from the data source and submitted for deletion.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsSubmittedForDeletionFailed | The number of documents that failed deletion from a data source.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsSubmittedForIndexing | The number of documents examined and submitted for indexing.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsSubmittedForIndexingFailed | The number of documents submitted for idexing that couldn't be indexed.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 

## Metrics for indexed documents
<a name="cloudwatch-metrics-id"></a>

The following table describes the Amazon Kendra metrics for indexed documents. For documents that are indexed using the [BatchPutDocument](https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchPutDocument.html) operation, only the `IndexId` dimension is supported.

If you use the API or CLI, you must specify the `Namespace` as 'AWS/Kendra' in addition to the `MetricName` of your choice when using [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) API.


| Metric | Description | 
| --- | --- | 
| DocumentsIndexed | The number of documents indexed.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| DocumentsFailedToIndex | The number of documents that could not be indexed. Check the contents of the CloudWatch log for details.<br />Dimensions:+  IndexId <br />+  DataSourceId <br />Unit: Count | 
| IndexQueryCount | The number of index queries per minute.<br />Dimensions:+  IndexId <br />Unit: Count | 