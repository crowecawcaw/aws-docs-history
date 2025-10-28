# Accessing CloudWatch metrics

You can see Amazon File Cache metrics for Amazon CloudWatch Logs in many ways. You can view them through
the CloudWatch console, or you can access them using the CloudWatch CLI or the CloudWatch API. The following
procedures show you how to access the metrics using these various tools.

###### To view metrics using the CloudWatch console

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
2. In the navigation pane, choose **Metrics**.
3. Select the **FSx** namespace.
4. (Optional) To view a metric, type its name in the search field.
5. (Optional) To filter by dimension, select **FileCacheId**.

###### To access metrics from the AWS CLI

- Use the [`list-metrics`](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md")
  command with the `--namespace "AWS/FSx"` namespace. For more information, see
  the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

###### To access metrics from the CloudWatch API

- Call `GetMetricStatistics`. For more information, see [Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md").
