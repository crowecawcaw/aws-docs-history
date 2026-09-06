

# CloudWatch metrics for your Gateway Load Balancer
<a name="cloudwatch-metrics"></a>

Elastic Load Balancing publishes data points to Amazon CloudWatch for your Gateway Load Balancers and your targets. CloudWatch enables you to retrieve statistics about those data points as an ordered set of time-series data, known as *metrics*. Think of a metric as a variable to monitor, and the data points as the values of that variable over time. For example, you can monitor the total number of healthy targets for a Gateway Load Balancer over a specified time period. Each data point has an associated time stamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example, you can create a CloudWatch alarm to monitor a specified metric and initiate an action (such as sending a notification to an email address) if the metric goes outside of what you consider an acceptable range.

Elastic Load Balancing reports metrics to CloudWatch only when requests are flowing through the Gateway Load Balancer. If there are requests flowing, Elastic Load Balancing measures and sends its metrics in 60-second intervals. If there are no requests flowing or no data for a metric, the metric is not reported.

For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [Gateway Load Balancer metrics](#metrics)
+ [Metric dimensions for Gateway Load Balancers](#metric-dimensions)
+ [View CloudWatch metrics for your Gateway Load Balancer](#view-metric-data)

## Gateway Load Balancer metrics
<a name="metrics"></a>

The `AWS/GatewayELB` namespace includes the following metrics.


| Metric | Description | 
| --- | --- | 
| ActiveFlowCount | The total number of concurrent flows (or connections) from clients to targets.<br />**Reporting criteria**: There is a nonzero value<br />**Statistics**: The most useful statistics are `Average`, `Maximum`, and `Minimum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| ConsumedLCUs | The number of load balancer capacity units (LCU) used by your load balancer. You pay for the number of LCUs that you use per hour. For more information, see [Elastic Load Balancing Pricing](https://aws.amazon.com/elasticloadbalancing/pricing/).<br />**Reporting criteria**: Always reported<br />**Statistics**: All+  `LoadBalancer`  | 
| HealthyHostCount | The number of targets that are considered healthy.<br />**Reporting criteria**: Reported if health checks are enabled<br />**Statistics**: The most useful statistics are `Maximum` and `Minimum`.+  `LoadBalancer`, `TargetGroup` <br />+  `AvailabilityZone`, `LoadBalancer`, `TargetGroup`  | 
| NewFlowCount | The total number of new flows (or connections) established from clients to targets in the time period.<br />**Reporting criteria**: There is a nonzero value<br />**Statistics**: The most useful statistic is `Sum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| PacketsDroppedCount\_InvalidGeneveTunnel | When returning the packet back to GWLB, the target appliance is required to swap the GENEVE tunnel source and destination IP addresses, and use the correct GENEVE destination port (6081). If the packet is not compliant with the above guideline, GWLB will drop the packet, and increment this metric.<br />**Reporting criteria**: Always reported<br />**Statistics**: The most useful statistic is `Sum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| PacketsDroppedCount\_InvalidGwlbEndpointId | The appliance is required to return the GwlbeEniId in the TLV when responding back to GWLB. If this TLV is missing, GWLB will drop the packet and increment this metric.<br />**Reporting criteria**: Always reported<br />**Statistics**: The most useful statistic is `Sum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| PacketsDroppedCount\_InvalidGwlbFlowCookie | The appliance is required to return FlowCookie TLV as is when responding back to GWLB. This metric is incremented if the flow cookie for a given flow does not match.<br />**Reporting criteria**: Always reported<br />**Statistics**: The most useful statistic is `Sum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| PacketsDroppedCount\_MissingFlowEntry | GWLB tracks a flow entry for each active flow that it processes. If the flow entry for a return-path packet is missing, GWLB will drop the packet and increment this metric. A flow entry can be missing if the flow has timed out, the packet does not belong to a known flow, or the flow was evicted due to system load.<br />**Reporting criteria**: Always reported<br />**Statistics**: The most useful statistic is `Sum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| PeakBytesPerSecond | The highest average bytes processed per second, calculated every 10 seconds during the sampling window. This metric does not include health check traffic.<br />**Reporting criteria**: Always reported<br />**Statistics**: The most useful statistic is `Maximum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| PeakPacketsPerSecond | The highest average packet rate (packets processed per second), calculated every 10 seconds during the sampling window. This metric includes health check traffic.<br />**Reporting criteria**: Always reported<br />**Statistics**: The most useful statistic is `Maximum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| ProcessedBytes | The total number of bytes processed by the load balancer. This count includes traffic to and from targets, but not health check traffic.<br />**Reporting criteria**: There is a nonzero value<br />**Statistics**: The most useful statistic is `Sum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| ProcessedPackets | The total number of packets processed by the load balancer. This count includes traffic to and from targets, including health check traffic.<br />**Reporting criteria**: Always reported.<br />**Statistics**: The most useful statistic is `Sum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| RejectedFlowCount | The total number of flows (or connections) rejected by the load balancer.<br />**Reporting criteria**: Always reported.<br />**Statistics**: The most useful statistics are `Average`, `Maximum`, and `Minimum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| RejectedFlowCount\_TCP | The number of TCP flows (or connections) rejected by the load balancer.<br />**Reporting criteria**: There is a nonzero value.<br />**Statistics**: The most useful statistic is `Sum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| TCP\_GWLB\_Reset\_Count | The total number of TCP reset (RST) packets generated by the Gateway Load Balancer when the TCP reset feature is active.<br />**Reporting criteria**: Always reported<br />**Statistics**: The most useful statistic is `Sum`.+  `LoadBalancer` <br />+  `AvailabilityZone`, `LoadBalancer`  | 
| UnHealthyHostCount | The number of targets that are considered unhealthy.<br />**Reporting criteria**: Reported if health checks are enabled<br />**Statistics**: The most useful statistics are `Maximum` and `Minimum`.+  `LoadBalancer`, `TargetGroup` <br />+  `AvailabilityZone`, `LoadBalancer`, `TargetGroup`  | 

## Metric dimensions for Gateway Load Balancers
<a name="metric-dimensions"></a>

To filter the metrics for your Gateway Load Balancer, use the following dimensions.


| Dimension | Description | 
| --- | --- | 
| AvailabilityZone | Filters the metric data by Availability Zone. | 
| LoadBalancer | Filters the metric data by Gateway Load Balancer. Specify the Gateway Load Balancer as follows: gateway/*load-balancer-name*/*1234567890123456* (the final portion of the ARN). | 
| TargetGroup | Filters the metric data by target group. Specify the target group as follows: targetgroup/*target-group-name*/*1234567890123456* (the final portion of the target group ARN). | 

## View CloudWatch metrics for your Gateway Load Balancer
<a name="view-metric-data"></a>

You can view the CloudWatch metrics for your Gateway Load Balancers by using the Amazon EC2 console. These metrics are displayed as monitoring graphs. The monitoring graphs show data points if the Gateway Load Balancer is active and receiving requests.

Alternatively, you can view metrics for your Gateway Load Balancer using the CloudWatch console.

**To view metrics using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. To view metrics filtered by target group, do the following:

   1. In the navigation pane, choose **Target Groups**.

   1. Select your target group and choose **Monitoring**.

   1. (Optional) To filter the results by time, select a time range from **Showing data for**.

   1. To get a larger view of a single metric, select its graph.

1. To view metrics filtered by Gateway Load Balancer, do the following:

   1. In the navigation pane, choose **Load Balancers**.

   1. Select your Gateway Load Balancer and choose **Monitoring**.

   1. (Optional) To filter the results by time, select a time range from **Showing data for**.

   1. To get a larger view of a single metric, select its graph.

**To view metrics using the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Select the **GatewayELB** namespace.

1. (Optional) To view a metric across all dimensions, enter its name in the search field.

**To view metrics using the AWS CLI**  
Use the following [list-metrics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) command to list the available metrics:

```
aws cloudwatch list-metrics --namespace AWS/GatewayELB
```

**To get the statistics for a metric using the AWS CLI**  
Use the following [get-metric-statistics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/get-metric-statistics.html) command get statistics for the specified metric and dimension. Note that CloudWatch treats each unique combination of dimensions as a separate metric. You can't retrieve statistics using combinations of dimensions that were not specially published. You must specify the same dimensions that were used when the metrics were created.

```
aws cloudwatch get-metric-statistics --namespace AWS/GatewayELB \
--metric-name UnHealthyHostCount --statistics Average  --period 3600 \
--dimensions Name=LoadBalancer,Value=net/my-load-balancer/50dc6c495c0c9188 \
Name=TargetGroup,Value=targetgroup/my-targets/73e2d6bc24d8a067 \
--start-time 2017-04-18T00:00:00Z --end-time 2017-04-21T00:00:00Z
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