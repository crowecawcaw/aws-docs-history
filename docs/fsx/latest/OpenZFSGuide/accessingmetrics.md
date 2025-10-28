# Accessing CloudWatch metrics

You can access Amazon FSx metrics for CloudWatch in the following ways:

- The Amazon FSx console.
- The CloudWatch console.
- The CloudWatch command line interface (CLI).
- The CloudWatch API.
  The following procedures show you how to access the metrics using these tools.

###### To view metrics using the Amazon FSx console

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the navigation pane, choose **File systems**, then choose the
   file system that has the metrics that you want to view.
3. Choose **Actions > View details**.
4. On the **Summary** page, choose **Monitoring and performance** to
   see the metrics for your file system.

###### To view metrics using the CloudWatch console

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
2. In the navigation pane, choose **Metrics**.
3. Select the **FSx** namespace.
4. (Optional) To view a metric, enter its name in the search field.
5. (Optional) To explore metrics, select the category that best matches your question.
   _File system metrics_ and _Volume metrics_
   report summary-level metrics for individual file systems or volumes. _File
   system detailed metrics_ and _Volume detailed metrics_
   report more granular metrics within a file system or volume. For example, storage
   capacity that's used by snapshots.

###### To access metrics from the AWS CLI

- Use the [`list-metrics`](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md")
  command with the `--namespace "AWS/FSx"` namespace. For more information, see
  the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

###### To access metrics from the CloudWatch API

- Call `GetMetricStatistics`. For more information, see [Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md").
