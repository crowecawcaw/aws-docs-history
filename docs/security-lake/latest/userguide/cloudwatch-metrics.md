

# CloudWatch metrics for Amazon Security Lake
<a name="cloudwatch-metrics"></a>

You can monitor Security Lake using Amazon CloudWatch, which collects raw data every minute and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on the data in your data lake. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met.

**Topics**
+ [Security Lake metrics and dimensions](#available-securitylake-metrics)
+ [Viewing CloudWatch metrics for Security Lake](#view-securitylake-metrics)
+ [Setting CloudWatch alarms for Security Lake metrics](#securitylake-alarm-metrics)

## Security Lake metrics and dimensions
<a name="available-securitylake-metrics"></a>

The `AWS/SecurityLake` namespace includes the following metrics.


| Metric | Description | 
| --- | --- | 
| `ProcessedSize` | The volume of data from natively-supported AWS services that's currently stored in your data lake.<br />Units: Bytes | 

The following dimensions are available for Security Lake metrics.


| Dimension | Description | 
| --- | --- | 
| `Account` | `ProcessedSize` metric for a specific AWS account. This dimension is available only when you view the `Per-Account Source Version Metrics` on CloudWatch. | 
| `Region` | `ProcessedSize` metric for a specific AWS Region. | 
| `Source` | `ProcessedSize` metric for a specific AWS log source. | 
| `SourceVersion` | `ProcessedSize` metric for a specific version of an AWS log source. | 

You can view metrics for specific AWS accounts (`Per-Account Source Version Metrics`) or for all accounts in an organization (`Per-Source Version Metrics`).

## Viewing CloudWatch metrics for Security Lake
<a name="view-securitylake-metrics"></a>

You can monitor metrics for Security Lake using the CloudWatch console, CloudWatch's own command line interface (CLI), or programmatically using the CloudWatch API. Choose your preferred method, and follow the steps to access Security Lake metrics.

------
#### [ CloudWatch console ]

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. On the navigation pane, choose **Metrics, All metrics**.

1. On the **Browse** tab, choose **Security Lake**.

1. Choose **Per-Account Source Version Metrics** or **Per-Source Version Metrics**.

1. Select a metric to view it in detail. You can also choose to do the following:
   + To sort the metrics, use the column heading.
   + To graph a metric, select the metric name, and choose a graphing option.
   + To filter by metric, select the metric name and then choose **Add to search**.

------
#### [ CloudWatch API ]

To access Security Lake metrics using the CloudWatch API, use the [`GetMetricStatistics`](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) action.

------
#### [ AWS CLI ]

To access Security Lake metrics using the AWS CLI, run the [`get-metric-statistics`](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/get-metric-statistics.html) command.

------

For more information about monitoring using metrics, see [Use Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) in the *Amazon CloudWatch User Guide*.

## Setting CloudWatch alarms for Security Lake metrics
<a name="securitylake-alarm-metrics"></a>

CloudWatch also allows you to set alarms when a threshold is met for a metric. For example, you could set an alarm for the **ProcessedSize** metric, so that you're notified when the volume of data from a specific source exceeds a specific threshold.

For instructions on setting alarms, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.