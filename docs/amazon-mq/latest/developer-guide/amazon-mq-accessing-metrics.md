

# Accessing CloudWatch metrics for Amazon MQ
<a name="amazon-mq-accessing-metrics"></a>

 You can access CloudWatch metrics using the AWS Management Console, AWS CLI, and API. 

You may want to access CloudWatch metrics without using the AWS Management Console.

To access Amazon MQ metrics using the AWS CLI, use the `[get-metric-statistics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/get-metric-statistics.html)` command. For more information, see [Get Statistics for a Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/getting-metric-statistics.html) in the *Amazon CloudWatch User Guide*.

To access Amazon MQ metrics using the CloudWatch API, use the `[GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html)` action. For more information, see [Get Statistics for a Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/getting-metric-statistics.html) in the *Amazon CloudWatch User Guide*.

## Accessing CloudWatch metrics using the AWS Management Console
<a name="amazon-mq-accessing-metrics-console"></a>

The following example shows you how to access CloudWatch metrics for Amazon MQ using the AWS Management Console.If you're already signed into the Amazon MQ console, on the broker **Details** page, choose **Actions**, **View CloudWatch metrics**. 

1. Sign in to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. On the navigation panel, choose **Metrics**.

1. Select the **AmazonMQ** metric namespace.

1. Select one of the following metric dimensions:
   + **Broker Metrics**
   + **Queue Metrics by Broker**
   + **Topic Metrics by Broker**

   In this example, **Broker Metrics** is selected.

1. You can now examine your Amazon MQ metrics:
   + To sort the metrics, use the column heading.
   + To graph the metric, select the check box next to the metric.
   + To filter by metric, choose the metric name and then choose **Add to search**.