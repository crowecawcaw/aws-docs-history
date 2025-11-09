# Using Amazon CloudWatch

Metrics

You can get monitoring data for your Tape Gateway by using either the AWS Management Console or
the CloudWatch API. The console displays a series of graphs based on the raw data from the
CloudWatch API. The CloudWatch API can also be used through one of the [Amazon AWS Software Development Kits (SDKs)](https://aws.amazon.com/tools "https://aws.amazon.com/tools") or the [Amazon CloudWatch API](https://aws.amazon.com/cloudwatch "https://aws.amazon.com/cloudwatch") tools. Depending on
your needs, you might prefer to use either the graphs displayed in the console or
retrieved from the API.

Regardless of which method you choose to use to work with metrics, you must specify
the following information:

- The metric dimension to work with. A _dimension_ is a
  name-value pair that helps you to uniquely identify a metric. The dimensions for
  Storage Gateway are `GatewayId` and `GatewayName`. In the
  CloudWatch console, you can use the `Gateway Metrics` view to easily select
  gateway-specific and tape-specific dimensions. For more information about
  dimensions, see [Dimensions](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension") in the _Amazon CloudWatch User Guide_.
- The metric name, such as `ReadBytes`.
  The following table summarizes the types of Storage Gateway metric data that are
  available to you.

| Amazon CloudWatch Namespace | Dimension                  | Description                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/StorageGateway`        | `GatewayId`, `GatewayName` | These dimensions filter for metric data that describes aspects of<br>the Tape Gateway. You can identify a Tape Gateway to work with by<br>specifying both the `GatewayId` and the<br>`GatewayName` dimensions.<br>Throughput and latency data of a Tape Gateway is based on all the<br>virtual tapes in the Tape Gateway.<br>Data is available automatically in 5-minute periods at no charge. |

Working with gateway and tape metrics is similar to working with other service
metrics. You can find a discussion of some of the most common metrics tasks in the CloudWatch
documentation listed following:

- [Viewing
  Available Metrics](../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md")
- [Getting Statistics for a
  Metric](../../../AmazonCloudWatch/latest/monitoring/US_GetStatistics.md "../../../AmazonCloudWatch/latest/monitoring/US_GetStatistics.md")
- [Creating CloudWatch
  Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
