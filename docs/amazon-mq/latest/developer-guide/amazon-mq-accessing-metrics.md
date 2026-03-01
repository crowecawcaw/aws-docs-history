# Accessing CloudWatch metrics for Amazon MQ

You can access CloudWatch metrics using the AWS Management Console, AWS CLI, and API.

You may want to access CloudWatch metrics without using the AWS Management Console.

To access Amazon MQ metrics using the AWS CLI, use the `get-metric-statistics` command.
For more information, see [Get Statistics for a Metric](../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md "../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md") in the
_Amazon CloudWatch User Guide_.

To access Amazon MQ metrics using the CloudWatch API, use the `GetMetricStatistics` action.
For more information, see [Get Statistics for a Metric](../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md "../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md") in the
_Amazon CloudWatch User Guide_.

## Accesing CloudWatch metrics using the AWS Management Console

The following example shows you how to access CloudWatch metrics for Amazon MQ using the
AWS Management Console.If you're already signed into the Amazon MQ console, on the broker
**Details** page, choose **Actions**,
**View CloudWatch metrics**.

1.  Sign in to the [CloudWatch
    console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2.  On the navigation panel, choose **Metrics**.
3.  Select the **AmazonMQ** metric namespace.
4.  Select one of the following metric dimensions:

        * **Broker Metrics**
        * **Queue Metrics by Broker**
        * **Topic Metrics by Broker**

    In this example, **Broker Metrics** is selected.

5.  You can now examine your Amazon MQ metrics:
    - To sort the metrics, use the column heading.

    - To graph the metric, select the check box next to the
      metric.
    - To filter by metric, choose the metric name and then choose
      **Add to search**.
