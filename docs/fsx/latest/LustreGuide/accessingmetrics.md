# Accessing CloudWatch metrics

You can access Amazon FSx for Lustre metrics for CloudWatch in the following ways:

- The Amazon FSx for Lustre console.
- The CloudWatch console.
- The CloudWatch command line interface (CLI).
- The CloudWatch API.
  The following procedures show you how to access the metrics using these tools.

###### To view metrics using the Amazon FSx for Lustre console

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the navigation pane, choose **File systems**, then choose the
   file system that has the metrics that you want to view.
3. On the **Summary** page, choose **Monitoring & performance** to
   see the metrics for your file system.

There are four tabs on the **Monitoring & performance** panel.

    * Choose **Summary** (the default tab) to display any active warnings,
     CloudWatch alarms, and graphs for **File system activity**.
    * Choose **Storage** to view storage capacity, utilization metrics,
     and active warnings.
    * Choose **Performance** to view file server and storage performance
     metrics, and active warnings.
    * Choose **CloudWatch alarms** to view graphs of any alarms configured for your
     file system.

###### To view metrics using the CloudWatch console

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
2. In the navigation pane, choose **Metrics**.
3. Select the **FSx** namespace.
4. (Optional) To view a metric, enter its name in the search field.
5. (Optional) To explore metrics, select the category that best matches your
   question.

###### To access metrics from the AWS CLI

- Use the [`list-metrics`](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md")
  command with the `--namespace "AWS/FSx"` namespace. For more information, see
  the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

###### To access metrics from the CloudWatch API

- Call `GetMetricStatistics`. For more information, see [Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md").
