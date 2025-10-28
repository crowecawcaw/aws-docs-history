# Monitoring Amazon Kendra with Amazon CloudWatch

To track the health of your indexes, use Amazon CloudWatch. With CloudWatch, you can get metrics for
document synchronization for your index. You can also set up CloudWatch alarms to be notified
when one or more metrics exceeds a threshold that you define. For example, you can
monitor the number of documents submitted to be indexed or the number of documents that
failed to be indexed.

You must have the appropriate CloudWatch permissions to monitor Amazon Kendra with CloudWatch. For
more information, see [Authentication and Access Control for Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md") in the _Amazon CloudWatch
User Guide_.

## Viewing Amazon Kendra metrics

View Amazon Kendra metrics using the CloudWatch console.

###### To view metrics (CloudWatch console)

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Metrics**, choose **All
   Metrics** and then choose **Kendra**.
3. Choose the dimension, choose a metric name, then choose **Add to
   graph**.
4. Choose a value for the date range. The metric count for the selected date
   range is displayed in the graph.

## Creating an alarm

A CloudWatch alarm watches a single metric over a specified time period and performs one
or more actions: sending a notification to an Amazon Simple Notification Service (Amazon SNS) top or Auto Scaling
policy. The actions or actions are based on the value of the metric relative to a
given threshold over a number of time periods that you specify. CloudWatch can also send
you an Amazon SNS message when the alarm changes state.

CloudWatch alarms invoke actions only when the state changes and has persisted for the
period that you specify.

###### To set an alarm

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Alarms** and then choose **Create
   alarm**.
3. Select a metric. Choose a **Kendra** metric for your
   index and data source. Also set the time as set number of hours, days,
   weeks, or custom.
4. Choose your statistic. For example, **Average**. Also
   choose your alarm trigger time period as a set number of minutes, hours, per
   day, or custom.
5. Choose your threshold to trigger the alarm, whether to use a static value
   or a band and the condition to meet for the threshold.
6. Choose the alarm state for the trigger, whether the metric must fall
   outside your set threshold, or another state. Select who/which email to send
   the alarm notification to.
7. If you are satisfied with the alarm, choose **Create
   alarm**.

###### Note

You must provide a name for your CloudWatch alarm.

## CloudWatch Metrics for index synchronization

Jobs

The following table describes the Amazon Kendra metrics for data source
synchronization jobs.

If you use the API or CLI, you must specify the `Namespace` as
'AWS/Kendra' in addition to the `MetricName` of your choice when using
[GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") API.

| Metric                                | Description                                                                                                                                                                                                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DocumentsCrawled`                    | The number of documents that the synchronization job scanned or discovered during the run. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                                       |
| `DocumentsSubmittedForIndexing`       | The number of documents that the synchronization job submitted to the index. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                                                     |
| `DocumentsSubmittedForIndexingFailed` | The number of documents that failed indexing. Check the contents of the CloudWatch log for the synchronization job for details. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                  |
| `DocumentsSubmittedForDeletion`       | The number of documents that the synchronization job asked to be removed from the index. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                                         |
| `DocumentsSubmittedForDeletionFailed` | The number of documents that failed to be deleted. Check the contents of the CloudWatch log for the synchronization job for details. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                             | ## Metrics for Amazon Kendra data sources The following table describes the Amazon Kendra metrics for data source synchronization jobs. Metrics marked with an asterisk (\*) are used only for Amazon S3 data sources. If you use the API or CLI, you must specify the `Namespace` as 'AWS/Kendra' in addition to the `MetricName` of your choice when using [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") API.                                                                                               |
| Metric                                | Description                                                                                                                                                                                                                               |
| ---                                   | ---                                                                                                                                                                                                                                       |
| `DocumentsSkippedNoChange *`          | The number of documents examined and found not to have changed so they weren't submitted for indexing. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                           |
| `DocumentsSkippedInvalidMetadata *`   | The number of documents skipped because there was a problem with the associated metadata file. Check the contents of the CloudWatch log for the synchronization run for details. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count |
| `DocumentsCrawled`                    | The number of document files examined. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                                                                                           |
| `DocumentsSubmittedForDeletion`       | The number of documents examined that were deleted from the data source and submitted for deletion. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                              |
| `DocumentsSubmittedForDeletionFailed` | The number of documents that failed deletion from a data source. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                                                                 |
| `DocumentsSubmittedForIndexing`       | The number of documents examined and submitted for indexing. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                                                                     |
| `DocumentsSubmittedForIndexingFailed` | The number of documents submitted for idexing that couldn't be indexed. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                                                          | ## Metrics for indexed documents The following table describes the Amazon Kendra metrics for indexed documents. For documents that are indexed using the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") operation, only the `IndexId` dimension is supported. If you use the API or CLI, you must specify the `Namespace` as 'AWS/Kendra' in addition to the `MetricName` of your choice when using [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") API. |
| Metric                                | Description                                                                                                                                                                                                                               |
| ---                                   | ---                                                                                                                                                                                                                                       |
| `DocumentsIndexed`                    | The number of documents indexed. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                                                                                                 |
| `DocumentsFailedToIndex`              | The number of documents that could not be indexed. Check the contents of the CloudWatch log for details. Dimensions: <br>• IndexId <br>• DataSourceId Unit: Count                                                                         |
| `IndexQueryCount`                     | The number of index queries per minute. Dimensions: <br>• IndexId Unit: Count                                                                                                                                                             |
