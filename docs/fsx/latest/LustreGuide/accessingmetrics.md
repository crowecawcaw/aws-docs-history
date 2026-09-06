

# Accessing CloudWatch metrics
<a name="accessingmetrics"></a>

You can access Amazon FSx for Lustre metrics for CloudWatch in the following ways: 
+ The Amazon FSx for Lustre console.
+ The CloudWatch console.
+ The CloudWatch command line interface (CLI).
+ The CloudWatch API.

The following procedures show you how to access the metrics using these tools.

## Using the Amazon FSx for Lustre console
<a name="cwmetrics-fsx-console"></a>

**To view metrics using the Amazon FSx for Lustre console**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. From the navigation pane, choose **File systems**, then choose the file system that has the metrics that you want to view.

1. On the **Summary** page, choose **Monitoring & performance** to see the metrics for your file system.

   There are four tabs on the **Monitoring & performance** panel.
   + Choose **Summary** (the default tab) to display any active warnings, CloudWatch alarms, and graphs for **File system activity**.
   + Choose **Storage** to view storage capacity, utilization metrics, and active warnings.
   + Choose **Performance** to view file server and storage performance metrics, and active warnings.
   + Choose **CloudWatch alarms** to view graphs of any alarms configured for your file system.

## Using the CloudWatch console
<a name="cwmetrics-cw-console"></a>

**To view metrics using the CloudWatch console**

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch).

1. In the navigation pane, choose **Metrics**. 

1. Select the **FSx** namespace.

1. (Optional) To view a metric, enter its name in the search field.

1. (Optional) To explore metrics, select the category that best matches your question.

## Using the AWS CLI
<a name="cw-metrics-cli"></a>

**To access metrics from the AWS CLI**
+ Use the [`list-metrics`](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) command with the `--namespace "AWS/FSx"` namespace. For more information, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/).

## Using the CloudWatch API
<a name="cw-metrics-cw-api"></a>

**To access metrics from the CloudWatch API**
+ Call `[GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html)`. For more information, see [Amazon CloudWatch API Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/). 