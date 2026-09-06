

# Access CloudWatch Metrics for Amazon Data Firehose
<a name="cloudwatch-metrics"></a>

You can monitor metrics for Amazon Data Firehose using the CloudWatch console, command line, or CloudWatch API. The following procedures show you how to access metrics using these different methods. 

**To access metrics using the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. On the navigation bar, choose a region.

1. In the navigation pane, choose **Metrics**.

1. Choose the **Firehose** namespace.

1. Choose **Firehose stream Metrics** or **Firehose Metrics**.

1. Select a metric to add to the graph.

**To access metrics using the AWS CLI**  
Use the [list-metrics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) and [get-metric-statistics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/get-metric-statistics.html) commands.

```
aws cloudwatch list-metrics --namespace "AWS/Firehose"
```

```
aws cloudwatch get-metric-statistics --namespace "AWS/Firehose" \
--metric-name {{DescribeDeliveryStream.Latency}} --statistics Average --period 3600 \
--start-time 2017-06-01T00:00:00Z --end-time 2017-06-30T00:00:00Z
```