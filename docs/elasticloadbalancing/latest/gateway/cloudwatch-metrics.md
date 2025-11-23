# CloudWatch metrics for your Gateway Load Balancer

ELB publishes data points to Amazon CloudWatch for your Gateway Load Balancers and your targets. CloudWatch enables
you to retrieve statistics about those data points as an ordered set of time-series
data, known as _metrics_. Think of a metric as a variable to monitor,
and the data points as the values of that variable over time. For example, you can
monitor the total number of healthy targets for a Gateway Load Balancer over a specified time period.
Each data point has an associated time stamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example,
you can create a CloudWatch alarm to monitor a specified metric and initiate an action (such
as sending a notification to an email address) if the metric goes outside of what you
consider an acceptable range.

ELB reports metrics to CloudWatch only when requests are flowing through the Gateway Load Balancer. If
there are requests flowing, ELB measures and sends its metrics in 60-second intervals.
If there are no requests flowing or no data for a metric, the metric is not
reported.

For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Contents

- [Gateway Load Balancer metrics](#metrics "#metrics")
- [Metric dimensions for Gateway Load Balancers](#metric-dimensions "#metric-dimensions")
- [View CloudWatch metrics for your Gateway Load Balancer](#view-metric-data "#view-metric-data")

## Gateway Load Balancer metrics

The `AWS/GatewayELB` namespace includes the following metrics.

| Metric                  | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ActiveFlowCount`       | The total number of concurrent flows (or connections) from<br>clients to targets.<br>**Reporting criteria**: There is<br>a nonzero value<br>**Statistics**: The most useful<br>statistics are `Average`, `Maximum`, and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                       |
| `ConsumedLCUs`          | The number of load balancer capacity units (LCU) used by your<br>load balancer. You pay for the number of LCUs that you use per<br>hour. For more information, see [ELB<br>Pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/").<br>**Reporting criteria**: Always<br>reported<br>**Statistics**: All<br>Dimensions<br>• `LoadBalancer` |
| `HealthyHostCount`      | The number of targets that are considered healthy.<br>**Reporting criteria**: Reported<br>if health checks are enabled<br>**Statistics**: The most useful<br>statistics are `Maximum` and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`,<br>`TargetGroup`<br>• `AvailabilityZone`,<br>`LoadBalancer`,<br>`TargetGroup`                                                                                 |
| `NewFlowCount`          | The total number of new flows (or connections) established<br>from clients to targets in the time period.<br>**Reporting criteria**: There is<br>a nonzero value<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                  |
| `PeakBytesPerSecond`    | The highest average bytes processed per second, calculated every<br>10 seconds during the sampling window. This metric does not include health check<br>traffic.<br>**Reporting criteria**: Always reported<br>**Statistics**: The most useful<br>statistic is `Maximum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                   |
| `PeakPacketsPerSecond`  | The highest average packet rate (packets processed per second), calculated<br>every 10 seconds during the sampling window. This metric includes health check<br>traffic.<br>**Reporting criteria**: Always reported<br>**Statistics**: The most useful statistic<br>is `Maximum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                           |
| `ProcessedBytes`        | The total number of bytes processed by the load balancer. This<br>count includes traffic to and from targets, but not health check<br>traffic.<br>**Reporting criteria**: There is<br>a nonzero value<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                             |
| `ProcessedPackets`      | The total number of packets processed by the load balancer.<br>This count includes traffic to and from targets, including<br>health check traffic.<br>**Reporting criteria**: Always reported.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                    |
| `RejectedFlowCount`     | The total number of flows (or connections) rejected by the load balancer.<br>**Reporting criteria**: Always reported.<br>**Statistics**: The most useful<br>statistics are `Average`, `Maximum`, and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                          |
| `RejectedFlowCount_TCP` | The number of TCP flows (or connections) rejected by the load balancer.<br>**Reporting criteria**: There is a nonzero value.<br>**Statistics**: The most useful statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                         |
| `UnHealthyHostCount`    | The number of targets that are considered unhealthy.<br>**Reporting criteria**: Reported<br>if health checks are enabled<br>**Statistics**: The most useful<br>statistics are `Maximum` and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`,<br>`TargetGroup`<br>• `AvailabilityZone`,<br>`LoadBalancer`,<br>`TargetGroup`                                                                               |

## Metric dimensions for Gateway Load Balancers

To filter the metrics for your Gateway Load Balancer, use the following dimensions.

| Dimension          | Description                                                                                                                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AvailabilityZone` | Filters the metric data by Availability Zone.                                                                                                                                            |
| `LoadBalancer`     | Filters the metric data by Gateway Load Balancer. Specify the Gateway Load Balancer as<br>follows:<br>gateway/_load-balancer-name_/_1234567890123456_<br>(the final portion of the ARN). |
| `TargetGroup`      | Filters the metric data by target group. Specify the target<br>group as follows:<br>targetgroup/_target-group-name_/_1234567890123456_<br>(the final portion of the target group ARN).   |

## View CloudWatch metrics for your Gateway Load Balancer

You can view the CloudWatch metrics for your Gateway Load Balancers by using the Amazon EC2 console. These
metrics are displayed as monitoring graphs. The monitoring graphs show data points
if the Gateway Load Balancer is active and receiving requests.

Alternatively, you can view metrics for your Gateway Load Balancer using the CloudWatch console.

###### To view metrics using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. To view metrics filtered by target group, do the following:
   1. In the navigation pane, choose **Target
      Groups**.
   2. Select your target group and choose
      **Monitoring**.
   3. (Optional) To filter the results by time, select a time range from
      **Showing data for**.
   4. To get a larger view of a single metric, select its graph.

3. To view metrics filtered by Gateway Load Balancer, do the following:
   1. In the navigation pane, choose **Load
      Balancers**.
   2. Select your Gateway Load Balancer and choose
      **Monitoring**.
   3. (Optional) To filter the results by time, select a time range from
      **Showing data for**.
   4. To get a larger view of a single metric, select its graph.

###### To view metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Select the **GatewayELB** namespace.
4. (Optional) To view a metric across all dimensions, enter its name in the
   search field.

###### To view metrics using the AWS CLI

Use the following [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") command to list the available metrics:

```
`aws cloudwatch list-metrics --namespace AWS/GatewayELB`
```

###### To get the statistics for a metric using the AWS CLI

Use the following [get-metric-statistics](../../../cli/latest/reference/cloudwatch/get-metric-statistics.md "../../../cli/latest/reference/cloudwatch/get-metric-statistics.md") command get statistics for the specified
metric and dimension. Note that CloudWatch treats each unique combination of
dimensions as a separate metric. You can't retrieve statistics using
combinations of dimensions that were not specially published. You must specify
the same dimensions that were used when the metrics were created.

```
`aws cloudwatch get-metric-statistics --namespace AWS/GatewayELB \
--metric-name UnHealthyHostCount --statistics Average --period 3600 \
--dimensions Name=LoadBalancer,Value=net/my-load-balancer/50dc6c495c0c9188 \
Name=TargetGroup,Value=targetgroup/my-targets/73e2d6bc24d8a067 \
--start-time 2017-04-18T00:00:00Z --end-time 2017-04-21T00:00:00Z`
```

The following is example output.

```
{
    "Datapoints": [
        {
            "Timestamp": "2020-12-18T22:00:00Z",
            "Average": 0.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2020-12-18T04:00:00Z",
            "Average": 0.0,
            "Unit": "Count"
        },
        ...
    ],
    "Label": "UnHealthyHostCount"
}
```
