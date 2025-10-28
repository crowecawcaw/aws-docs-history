# Access CloudWatch Metrics for Amazon Data Firehose

You can monitor metrics for Amazon Data Firehose using the CloudWatch console, command line, or CloudWatch
API. The following procedures show you how to access metrics using these different
methods.

###### To access metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. On the navigation bar, choose a region.
3. In the navigation pane, choose **Metrics**.
4. Choose the **Firehose** namespace.
5. Choose **Firehose stream Metrics** or **Firehose
   Metrics**.
6. Select a metric to add to the graph.

###### To access metrics using the AWS CLI

Use the [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") and [get-metric-statistics](../../../cli/latest/reference/cloudwatch/get-metric-statistics.md "../../../cli/latest/reference/cloudwatch/get-metric-statistics.md") commands.

```
`aws cloudwatch list-metrics --namespace "AWS/Firehose"`
```

```
`aws cloudwatch get-metric-statistics --namespace "AWS/Firehose" \
--metric-name `DescribeDeliveryStream.Latency` --statistics Average --period 3600 \
--start-time 2017-06-01T00:00:00Z --end-time 2017-06-30T00:00:00Z`
```
