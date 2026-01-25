# CloudWatch metrics for your Network Load Balancer

Elastic Load Balancing publishes data points to Amazon CloudWatch for your load balancers and your targets. CloudWatch
enables you to retrieve statistics about those data points as an ordered set of
time-series data, known as _metrics_. Think of a metric as a variable
to monitor, and the data points as the values of that variable over time. For example,
you can monitor the total number of healthy targets for a load balancer over a specified
time period. Each data point has an associated time stamp and an optional unit of
measurement.

You can use metrics to verify that your system is performing as expected. For example,
you can create a CloudWatch alarm to monitor a specified metric and initiate an action (such
as sending a notification to an email address) if the metric goes outside what you
consider an acceptable range.

Elastic Load Balancing reports metrics to CloudWatch only when requests are flowing through the load
balancer. If there are requests flowing through the load balancer, Elastic Load Balancing measures and
sends its metrics in 60-second intervals. If there are no requests flowing through the
load balancer or no data for a metric, the metric is not reported. For Network Load Balancers with
security groups, traffic rejected by the security groups is not captured in the CloudWatch
metrics.

For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Contents

- [Network Load Balancer metrics](#load-balancer-metrics-nlb "#load-balancer-metrics-nlb")
- [Metric dimensions for
  Network Load Balancers](#load-balancer-metric-dimensions-nlb "#load-balancer-metric-dimensions-nlb")
- [Statistics for Network Load Balancer metrics](#metric-statistics "#metric-statistics")
- [View CloudWatch metrics for your load balancer](#view-metric-data "#view-metric-data")

## Network Load Balancer metrics

The `AWS/NetworkELB` namespace includes the following metrics.

| Metric                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ActiveFlowCount`                             | The total number of concurrent flows (or connections) from<br>clients to targets. This metric includes connections in the<br>SYN_SENT and ESTABLISHED states. TCP connections are not<br>terminated at the load balancer, so a client opening a TCP<br>connection to a target counts as a single flow.<br>**Reporting criteria**: Always<br>reported.<br>**Statistics**: The most useful<br>statistics are `Average`, `Maximum`, and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`<br>• `TargetGroup`                                                                                     |
| `ActiveFlowCount_TCP`                         | The total number of concurrent TCP flows (or connections) from<br>clients to targets. This metric includes connections in the<br>SYN_SENT and ESTABLISHED state. TCP connections are not<br>terminated at the load balancer, so a client opening a TCP<br>connection to a target counts as a single flow.<br>**Reporting criteria**: There is<br>a nonzero value<br>**Statistics**: The most useful<br>statistics are `Average`, `Maximum`, and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`<br>• `TargetGroup`                                                                          |
| `ActiveFlowCount_TLS`                         | The total number of concurrent TLS flows (or connections) from<br>clients to targets. This metric includes connections in the<br>SYN_SENT and ESTABLISHED state.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistics are `Average`, `Maximum`, and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`<br>• `TargetGroup`                                                                                                                                                                                                                  |
| `ActiveFlowCount_UDP`                         | The total number of concurrent UDP flows (or connections) from<br>clients to targets.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistics are `Average`, `Maximum`, and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`<br>• `TargetGroup`                                                                                                                                                                                                                                                                                             |
| `ActiveZonalShiftHostCount`                   | The number of targets that are actively participating in zonal<br>shift currently.<br>**Reporting criteria**: Reported<br>when the load balancer is opt-in for zonal shift.<br>**Statistics**: The most useful<br>statistics are `Maximum`, and `Minimum`.<br>Dimensions<br>• `LoadBalancer`,<br>`TargetGroup`<br>• `AvailabilityZone`,<br>`LoadBalancer`,<br>`TargetGroup`                                                                                                                                                                                                                                                            |
| `ClientTLSNegotiationErrorCount`              | The total number of TLS handshakes that failed during<br>negotiation between a client and a TLS listener.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`                                                                                                                                                                                                                                                                                                                                                                          |
| `ConsumedLCUs`                                | The number of load balancer capacity units (LCU) used by your<br>load balancer. You pay for the number of LCUs that you use per<br>hour. For more information, see [Elastic Load Balancing<br>Pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/").<br>**Reporting criteria**: Always<br>reported.<br>**Statistics**: All<br>Dimensions<br>• `LoadBalancer`                                                                                                                                                                                                           |
| `ConsumedLCUs_TCP`                            | The number of load balancer capacity units (LCU) used by your<br>load balancer for TCP. You pay for the number of LCUs that you<br>use per hour. For more information, see [Elastic Load Balancing<br>Pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/").<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: All<br>Dimensions<br>• `LoadBalancer`                                                                                                                                                                                          |
| `ConsumedLCUs_TLS`                            | The number of load balancer capacity units (LCU) used by your<br>load balancer for TLS. You pay for the number of LCUs that you<br>use per hour. For more information, see [Elastic Load Balancing<br>Pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/").<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: All<br>Dimensions<br>• `LoadBalancer`                                                                                                                                                                                          |
| `ConsumedLCUs_UDP`                            | The number of load balancer capacity units (LCU) used by your<br>load balancer for UDP. You pay for the number of LCUs that you<br>use per hour. For more information, see [Elastic Load Balancing<br>Pricing](https://aws.amazon.com/elasticloadbalancing/pricing/ "https://aws.amazon.com/elasticloadbalancing/pricing/").<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: All<br>Dimensions<br>• `LoadBalancer`                                                                                                                                                                                          |
| `HealthyHostCount`                            | The number of targets that are considered healthy. This metric<br>does not include any Application Load Balancers registered as targets.<br>**Reporting criteria**: Reported if there are registered targets.<br>**Statistics**: The most useful<br>statistics are `Maximum` and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`,<br>`TargetGroup`<br>• `AvailabilityZone`,<br>`LoadBalancer`,<br>`TargetGroup`                                                                                                                                                                                                                        |
| `NewFlowCount`                                | The total number of new flows (or connections) established<br>from clients to targets in the time period.<br>**Reporting criteria**: Always<br>reported.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`<br>• `TargetGroup`                                                                                                                                                                                                                                                                                                                     |
| `NewFlowCount_TCP`                            | The total number of new TCP flows (or connections) established<br>from clients to targets in the time period.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`<br>• `TargetGroup`                                                                                                                                                                                                                                                                                                        |
| `NewFlowCount_TLS`                            | The total number of new TLS flows (or connections) established<br>from clients to targets in the time period.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`<br>• `TargetGroup`                                                                                                                                                                                                                                                                                                        |
| `NewFlowCount_UDP`                            | The total number of new UDP flows (or connections) established<br>from clients to targets in the time period.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`<br>• `TargetGroup`                                                                                                                                                                                                                                                                                                        |
| `NewFlowCount_QUIC`                           | The total number of UDP datagrams that required a routing decision<br>in the time period.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                               |
| `PeakBytesPerSecond`                          | The highest average bytes processed per second, calculated every<br>10 seconds during the sampling window. This metric does not include health check<br>traffic.<br>**Reporting criteria**: Always reported<br>**Statistics**: The most useful<br>statistic is `Maximum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                 |
| `PeakPacketsPerSecond`                        | Highest average packet rate (packets processed per second),<br>calculated every 10 seconds during the sampling window. This<br>metric includes health check traffic.<br>**Reporting criteria**: Always reported.<br>**Statistics**: The most useful<br>statistic is `Maximum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                            |
| `PortAllocationErrorCount`                    | The total number of ephemeral port allocation errors during a<br>client IP translation operation. A non-zero value indicates<br>dropped client connections.<br>Note: Network Load Balancers support 55,000 simultaneous connections or about<br>55,000 connections per minute to each unique target (IP address<br>and port) when performing client address translation. To fix<br>port allocation errors, add more targets to the target<br>group.<br>**Reporting criteria**: Always reported.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer` |
| `ProcessedBytes`                              | The total number of bytes processed by the load balancer,<br>including TCP/IP headers. This count includes traffic to and<br>from targets, minus health check traffic.<br>**Reporting criteria**: Always<br>reported.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                           |
| `ProcessedBytes_TCP`                          | The total number of bytes processed by TCP listeners.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                                                                   |
| `ProcessedBytes_TLS`                          | The total number of bytes processed by TLS listeners.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                                                                   |
| `ProcessedBytes_UDP`                          | The total number of bytes processed by UDP listeners.<br>**Reporting criteria**: There is<br>a nonzero value<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                                                                    |
| `ProcessedBytes_QUIC`                         | The total number of bytes processed by QUIC listeners.<br>**Reporting criteria**: There is<br>a nonzero value<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                                                                   |
| `ProcessedPackets`                            | The total number of packets processed by the load balancer.<br>This count includes traffic to and from targets, including<br>health check traffic.<br>**Reporting criteria**: Always reported.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                  |
| `RejectedFlowCount`                           | The total number of flows (or connections) rejected by the load balancer.<br>**Reporting criteria**: Always reported.<br>**Statistics**: The most useful<br>statistics are `Average`, `Maximum`, and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                        |
| `RejectedFlowCount_TCP`                       | The number of TCP flows (or connections) rejected by the load balancer.<br>**Reporting criteria**: There is a nonzero value.<br>**Statistics**: The most useful statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                                                       |
| `ReservedLCUs`                                | The number of load balancer capacity units (LCUs) reserved<br>for your load balancer using LCU Reservation.<br>**Reporting criteria**: There is a nonzero value<br>**Statistics**: All<br>Dimensions<br>• `LoadBalancer`                                                                                                                                                                                                                                                                                                                                                                                                               |
| `SecurityGroupBlockedFlowCount_Inbound_ICMP`  | The number of new ICMP messages rejected by the inbound rules<br>of the load balancer security groups.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                  |
| `SecurityGroupBlockedFlowCount_Inbound_TCP`   | The number of new TCP flows rejected by the inbound rules of<br>the load balancer security groups.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                      |
| `SecurityGroupBlockedFlowCount_Inbound_UDP`   | The number of new UDP flows rejected by the inbound rules of<br>the load balancer security groups.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                      |
| `SecurityGroupBlockedFlowCount_Outbound_ICMP` | The number of new ICMP messages rejected by the outbound rules<br>of the load balancer security groups.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                 |
| `SecurityGroupBlockedFlowCount_Outbound_TCP`  | The number of new TCP flows rejected by the outbound rules of<br>the load balancer security groups.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                     |
| `SecurityGroupBlockedFlowCount_Outbound_UDP`  | The number of new UDP flows rejected by the outbound rules of<br>the load balancer security groups.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                                                     |
| `TargetTLSNegotiationErrorCount`              | The total number of TLS handshakes that failed during<br>negotiation between a TLS listener and a target.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`                                                                                                                                                                                                                                                                                                                                                                          |
| `TCP_Client_Reset_Count`                      | The total number of reset (RST) packets sent from a client to<br>a target. These resets are generated by the client and forwarded<br>by the load balancer.<br>**Reporting criteria**: Always<br>reported.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                       |
| `TCP_ELB_Reset_Count`                         | The total number of reset (RST) packets generated by the load<br>balancer. For more information, see [Troubleshooting](load-balancer-troubleshooting.md#elb-reset-count-metric "load-balancer-troubleshooting.md#elb-reset-count-metric").<br>**Reporting criteria**: Always<br>reported.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                       |
| `TCP_Target_Reset_Count`                      | The total number of reset (RST) packets sent from a target to<br>a client. These resets are generated by the target and forwarded<br>by the load balancer.<br>**Reporting criteria**: Always<br>reported.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                       |
| `UnHealthyHostCount`                          | The number of targets that are considered unhealthy. This<br>metric does not include any Application Load Balancers registered as targets.<br>**Reporting criteria**: Reported if there are registered targets.<br>**Statistics**: The most useful<br>statistics are `Maximum` and<br>`Minimum`.<br>Dimensions<br>• `LoadBalancer`,<br>`TargetGroup`<br>• `AvailabilityZone`,<br>`LoadBalancer`,<br>`TargetGroup`                                                                                                                                                                                                                      |
| `UnhealthyRoutingFlowCount`                   | The number of flows (or connections) that are routed using the<br>routing failover action (fail open). This metric is not supported<br>for TLS listeners.<br>**Reporting criteria**: There is<br>a nonzero value.<br>**Statistics**: The most useful<br>statistic is `Sum`.                                                                                                                                                                                                                                                                                                                                                            |
| `ZonalHealthStatus`                           | The number of Availability Zones that the load balancer considers<br>healthy. The load balancer emits a 1 for each healthy Availability<br>Zone and a 0 for each unhealthy Availability Zone.<br>**Reporting criteria**: Reported<br>if health checks are enabled.<br>**Statistics**: The most useful<br>statistics are `Maximum` and `Minimum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                          |
| `QUIC_Unknown_Server_ID_Packet_Drop_Count`    | The number of UDP datagrams dropped which contain a server ID not associated with a target in the Network Load Balancer.<br>**Reporting criteria**: Reported<br>only for QUIC listeners.<br>**Statistics**: The most useful<br>statistic is `Sum`.<br>Dimensions<br>• `LoadBalancer`<br>• `AvailabilityZone`,<br>`LoadBalancer`                                                                                                                                                                                                                                                                                                        |

## Metric dimensions for

Network Load Balancers

To filter the metrics for your load balancer, use the following dimensions.

| Dimension          | Description                                                                                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AvailabilityZone` | Filters the metric data by Availability Zone.                                                                                                                                          |
| `LoadBalancer`     | Filters the metric data by load balancer. Specify the load<br>balancer as follows:<br>net/_load-balancer-name_/_1234567890123456_<br>(the final portion of the load balancer ARN).     |
| `TargetGroup`      | Filters the metric data by target group. Specify the target<br>group as follows:<br>targetgroup/_target-group-name_/_1234567890123456_<br>(the final portion of the target group ARN). |

## Statistics for Network Load Balancer metrics

CloudWatch provides statistics based on the metric data points published by Elastic Load Balancing.
Statistics are metric data aggregations over specified period of time. When you
request statistics, the returned data stream is identified by the metric name and
dimension. A dimension is a name/value pair that uniquely identifies a metric. For
example, you can request statistics for all the healthy EC2 instances behind a load
balancer launched in a specific Availability Zone.

The `Minimum` and `Maximum` statistics reflect the minimum
and maximum values of the data points reported by the individual load balancer nodes
in each sampling window. Increases in the maximum of `HealthyHostCount`
correspond to decreases in the minimum of `UnHealthyHostCount`. It's
recommended to monitor maximum `HealthyHostCount`, invoking the alarm when
the maximum `HealthyHostCount` falls below your required minimum, or being
`0`. This can help in identifying when your targets have become unhealthy.
It's also recommended to monitor minimum `UnHealthyHostCount`, invoking the
alarm when the minimum `UnHealthyHostCount` rises above `0`. This
allows you to become aware when there are no longer any registered targets.

The `Sum` statistic is the aggregate value across all load balancer
nodes. Because metrics include multiple reports per period, `Sum` is only
applicable to metrics that are aggregated across all load balancer nodes.

The `SampleCount` statistic is the number of samples measured. Because
metrics are gathered based on sampling intervals and events, this statistic is
typically not useful. For example, with `HealthyHostCount`,
`SampleCount` is based on the number of samples that each load
balancer node reports, not the number of healthy hosts.

## View CloudWatch metrics for your load balancer

You can view the CloudWatch metrics for your load balancers using the Amazon EC2 console.
These metrics are displayed as monitoring graphs. The monitoring graphs show data
points if the load balancer is active and receiving requests.

Alternatively, you can view metrics for your load balancer using the CloudWatch
console.

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

3. To view metrics filtered by load balancer, do the following:
   1. In the navigation pane, choose **Load
      Balancers**.
   2. Select your load balancer and choose
      **Monitoring**.
   3. (Optional) To filter the results by time, select a time range from
      **Showing data for**.
   4. To get a larger view of a single metric, select its graph.

###### To view metrics using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Select the **NetworkELB** namespace.
4. (Optional) To view a metric across all dimensions, type its name in the
   search field.

###### To view metrics using the AWS CLI

Use the following [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") command to list the available metrics:

```
`aws cloudwatch list-metrics --namespace AWS/NetworkELB`
```

###### To get the statistics for a metric using the AWS CLI

Use the following [get-metric-statistics](../../../cli/latest/reference/cloudwatch/get-metric-statistics.md "../../../cli/latest/reference/cloudwatch/get-metric-statistics.md") command get statistics for the specified
metric and dimension. Note that CloudWatch treats each unique combination of
dimensions as a separate metric. You can't retrieve statistics using
combinations of dimensions that were not specially published. You must specify
the same dimensions that were used when the metrics were created.

```
`aws cloudwatch get-metric-statistics --namespace AWS/NetworkELB \
--metric-name UnHealthyHostCount --statistics Average --period 3600 \
--dimensions Name=LoadBalancer,Value=net/my-load-balancer/50dc6c495c0c9188 \
Name=TargetGroup,Value=targetgroup/my-targets/73e2d6bc24d8a067 \
--start-time 2017-04-18T00:00:00Z --end-time 2017-04-21T00:00:00Z`
```

The following is example output:

```
{
    "Datapoints": [
        {
            "Timestamp": "2017-04-18T22:00:00Z",
            "Average": 0.0,
            "Unit": "Count"
        },
        {
            "Timestamp": "2017-04-18T04:00:00Z",
            "Average": 0.0,
            "Unit": "Count"
        },
        ...
    ],
    "Label": "UnHealthyHostCount"
}
```
