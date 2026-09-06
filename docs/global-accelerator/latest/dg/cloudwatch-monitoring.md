

# Using Amazon CloudWatch with AWS Global Accelerator
<a name="cloudwatch-monitoring"></a>

AWS Global Accelerator publishes data points to Amazon CloudWatch for your accelerators. CloudWatch enables you to retrieve statistics about those data points as an ordered set of time-series data, known as *metrics*. Think of a metric as a variable to monitor, and the data points as the values of that variable over time. For example, you can monitor traffic through an accelerator over a specified time period. Each data point has an associated time stamp and an optional unit of measurement.

**Note**  
You must view CloudWatch metrics and logs for Global Accelerator in the US West (Oregon) Region, both in the console or when using the AWS CLI. When you use the AWS CLI, specify the US West (Oregon) Region for your command by including the following parameter: `--region us-west-2`.

You can use metrics to troubleshoot an initial Global Accelerator setup, to help determine whether traffic is arriving at an endpoint, and then responses are returning. View the CloudWatch metrics, which are logged automatically, to see if traffic is making it to your endpoints, such as a Network Load Balancer. There should be metrics for outbound from Global Accelerator towards the endpoints, and then from Global Accelerator back to the client, and the same for an endpoint, such as a load balancer. Traffic flowing in from Global Accelerator but not back out, or not reaching the load balancer, can indicate that you need to verify that your configuration allows traffic to flow through the expected ports and that your security group settings allow access.

You can also use metrics to verify that your system is performing as you expect it to. For example, you can create a CloudWatch alarm to monitor a specified metric, and then take action (such as sending a notification to an email address) if the metric goes outside what you consider an acceptable range.

Global Accelerator reports metrics to CloudWatch only when requests are flowing through the accelerator. If requests are flowing through the accelerator, Global Accelerator measures and sends its metrics in 60-second intervals. If there are no requests flowing through the accelerator or there is no data for a metric, the metric is not reported.

For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [Global Accelerator metrics](#cloudwatch-metrics-global-accelerator)
+ [Metric dimensions for accelerators](#cloudwatch-metric-dimensions-aga)
+ [Statistics for Global Accelerator metrics](#cloudwatch-metric-statistics)
+ [View CloudWatch metrics for your accelerators](#view-metric-data)

## Global Accelerator metrics
<a name="cloudwatch-metrics-global-accelerator"></a>

The `AWS/GlobalAccelerator` namespace includes the following metrics.


| Metric | Description | 
| --- | --- | 
| ActiveFlowCount | The total number of concurrent TCP and UDP connections from clients to endpoints for an accelerator in Global Accelerator. For TCP connections, which are terminated at the accelerator, a client opening a TCP connection to an endpoint counts as a single flow.<br />You can use this metric to better understand how many active users (connection count) are accessing an endpoint, or to determine if your resources need to be scaled to handle traffic.<br />**Reporting criteria**: Reported for accelerators that are configured and enabled.<br />**Statistics**: The only useful statistic is `Sum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, Listener, EndpointGroup`<br />+ `Accelerator, SourceRegion`<br />+ `Accelerator, DestinationEdge`<br />+ `Accelerator, TransportProtocol`<br />+ `Accelerator, AcceleratorIPAddress` | 
| Flows\_Dropped\_No\_Endpoint\_Found | The total number of TCP IPv6 packet flows that were dropped because no IPv6 endpoints were available. This could happen, for example, if you had an accelerator with a dual-stack IP address type and you changed the IP address type to IPv4 for an endpoint for the accelerator.<br />**Reporting criteria**: Reported for accelerators with dual-stack IP address types that are receiving IPv6 traffic when one of the following occurs:+ An accelerator with IPv6 endpoints serving traffic reports a 0 metric<br />+ An accelerator with misconfigured endpoints reports the total number of flows dropped<br />**Statistics**: The only useful statistic is `Sum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, AcceleratorIPAddress` | 
| HealthyEndpointCount | The total number of endpoints that are considered healthy. Global Accelerator regularly checks the status of endpoints on standard accelerators. These health checks run automatically. How and when these health checks run depends on the type of endpoint and the health check options for the endpoint. To learn more, see [Ensure health check access for your accelerator](about-endpoint-groups-health-check-options.md).<br />**Reporting criteria**: Reported for accelerators that are configured and enabled.<br />**Statistics**: The most useful statistics are `Minimum` and `Maximum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, Listener, EndpointGroup` | 
| NewFlowCount | The total number of new TCP and UDP flows (or connections) established from clients to endpoints in the time period.<br />**Reporting criteria**: There is a nonzero value.<br />**Statistics**: The only useful statistic is `Sum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, Listener, EndpointGroup`<br />+ `Accelerator, SourceRegion`<br />+ `Accelerator, DestinationEdge`<br />+ `Accelerator, TransportProtocol`<br />+ `Accelerator, AcceleratorIPAddress`<br />+ `Accelerator, NetworkProtocol` | 
| ProcessedBytesIn | The total number of incoming bytes processed by the accelerator, including TCP/IP headers. This count includes all traffic to endpoints.<br />**Reporting criteria**: There is a nonzero value.<br />**Statistics**: The only useful statistic is `Sum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, Listener, EndpointGroup`<br />+ `Accelerator, SourceRegion`<br />+ `Accelerator, DestinationEdge`<br />+ `Accelerator, TransportProtocol`<br />+ `Accelerator, AcceleratorIPAddress`<br />+ `Accelerator, NetworkProtocol` | 
| ProcessedBytesOut | The total number of outgoing bytes processed by the accelerator, including TCP/IP headers. This count includes traffic from endpoints, minus health check traffic.<br />**Reporting criteria**: There is a nonzero value.<br />**Statistics**: The only useful statistic is `Sum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, Listener, EndpointGroup`<br />+ `Accelerator, SourceRegion`<br />+ `Accelerator, DestinationEdge`<br />+ `Accelerator, TransportProtocol`<br />+ `Accelerator, AcceleratorIPAddress`<br />+ `Accelerator, NetworkProtocol` | 
| PacketsProcessed | The total number of packets processed by Global Accelerator for an accelerator, including traffic to and from endpoints, including health check traffic. This metric can help you to benchmark traffic volumes within a specific time period.<br />**Reporting criteria**: Reported for accelerators that are configured and enabled.<br />**Statistics**: The only useful statistic is `Sum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, Listener, EndpointGroup`<br />+ `Accelerator, SourceRegion`<br />+ `Accelerator, DestinationEdge`<br />+ `Accelerator, TransportProtocol`<br />+ `Accelerator, AcceleratorIPAddress` | 
| UnhealthyEndpointCount | The total number of endpoints that are considered unhealthy. Global Accelerator regularly checks the status of endpoints on standard accelerators. These health checks run automatically. How and when these health checks run depend on the type of endpoint and the health check options for the endpoint. To learn more, see [Ensure health check access for your accelerator](about-endpoint-groups-health-check-options.md).<br />**Reporting criteria**: Reported for accelerators that are configured and enabled.<br />**Statistics**: The most useful statistics are `Minimum` and `Maximum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, Listener, EndpointGroup` | 
| TCP\_AGA\_Reset\_Count | The total number of reset (RST) packets generated by AWS Global Accelerator ("AGA"). By using this metric, you can determine whether Global Accelerator is terminating client connections and sending resets back to the client endpoint.<br />For more information about evaluating and troubleshooting TCP RST generated by Global Accelerator, see [Troubleshooting Global Accelerator TCP reset issues](cloudwatch-metrics-globalaccelerator-tcp-resets.md).<br />**Reporting criteria**: Reported when there is traffic and there is a nonzero value.<br />**Statistics**: The only useful statistic is `Sum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, Listener, EndpointGroup`<br />+ `Accelerator, SourceRegion`<br />+ `Accelerator, DestinationEdge`<br />+ `Accelerator, AcceleratorIPAddress` | 
| TCP\_Client\_Reset\_Count | The total number of reset (RST) packets sent from a client to an endpoint. By using this metric, you can determine whether a client can keep a connection open with Global Accelerator or if the connection is reset unexpectedly early. This is useful, for example, when you configure Global Accelerator initially, and for visibility when you make a change to clients that create connection resets.<br />For more information about evaluating and troubleshooting TCP RST generated by Global Accelerator, see [Troubleshooting Global Accelerator TCP reset issues](cloudwatch-metrics-globalaccelerator-tcp-resets.md).<br />**Reporting criteria**: Reported when there is traffic and there is a nonzero value.<br />**Statistics**: The only useful statistic is `Sum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, Listener, EndpointGroup`<br />+ `Accelerator, SourceRegion`<br />+ `Accelerator, DestinationEdge`<br />+ `Accelerator, AcceleratorIPAddress` | 
| TCP\_Endpoint\_Reset\_Count | The total number of reset (RST) packets sent from an endpoint to a client. Using this metric, can help you determine when your client endpoints are overloaded.<br />For more information about evaluating and troubleshooting TCP RST generated by Global Accelerator, see [Troubleshooting Global Accelerator TCP reset issues](cloudwatch-metrics-globalaccelerator-tcp-resets.md).<br />**Reporting criteria**: Reported when there is traffic and there is a nonzero value.<br />**Statistics**: The only useful statistic is `Sum`.+ `Accelerator`<br />+ `Accelerator, Listener`<br />+ `Accelerator, Listener, EndpointGroup`<br />+ `Accelerator, SourceRegion`<br />+ `Accelerator, DestinationEdge`<br />+ `Accelerator, AcceleratorIPAddress` | 

## Metric dimensions for accelerators
<a name="cloudwatch-metric-dimensions-aga"></a>

To filter the metrics for your accelerator, use the following dimensions.


| Dimension | Description | 
| --- | --- | 
| Accelerator | Filters the metric data by accelerator. Specify the accelerator by the accelerator id (the final portion of the accelerator ARN). For example, if the ARN is `arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`, you specify the following: **1234abcd-abcd-1234-abcd-1234abcdefgh**.  | 
| Listener | Filters the metric data by listener. Specify the listener by the listener id (the final portion of the listener ARN). For example, if the ARN is `arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123wxyz`, you specify the following: **0123wxyz**. | 
| EndpointGroup | Filters the metric data by endpoint group. Specify the endpoint group by the AWS Region, for example, **us-east-1** (all lowercase). | 
| SourceRegion | Filters the metric data by source region, which is the geographic area of the AWS Regions where your application endpoints are running. Source region is one of the following:+ NA – United States and Canada<br />+ EU – Europe<br />+ AP – Asia Pacific\*<br />+ KR – South Korea<br />+ IN – India<br />+ AU – Australia<br />+ ME – Middle East<br />+ SA – South America<br />+ ZA – South Africa<br />\*Excluding South Korea and India | 
| DestinationEdge | Filters the metric data by destination edge, which is the geographic area of the AWS edge locations that serve your client traffic. Destination edge is one of the following:+ NA – United States and Canada<br />+ EU – Europe<br />+ AP – Asia Pacific\*<br />+ KR – South Korea<br />+ IN – India<br />+ AU – Australia<br />+ ME – Middle East<br />+ SA – South America<br />+ ZA – South Africa<br />\*Excluding South Korea and India | 
| TransportProtocol | Filters the metric data by transport protocol: UDP or TCP. | 
| AcceleratorIPAddress | Filters the metric data by the IP address of the accelerator: that is, one of the static IP addresses assigned to an accelerator. | 

## Statistics for Global Accelerator metrics
<a name="cloudwatch-metric-statistics"></a>

CloudWatch provides statistics based on the metric data points published by Global Accelerator. Statistics are aggregations of metric data over a specified period of time. When you request statistics, the returned data stream is identified by the metric name and dimension. A dimension is a name/value pair that uniquely identifies a metric. For example, you can request the processed bytes out for an accelerator where the bytes are served from AWS edge locations in Europe (destination edge is "EU").

The following are examples of metric/dimension combinations that you might find useful:
+ View the amount of traffic served (such as ProcessedBytesOut) by each of your two accelerator IP addresses to validate that your DNS configuration is correct.
+ View the geographical distribution of your user traffic and monitor how much of it is local (for example, North America to North America) or global (for example, Australia or India to North America). To determine this, view the metrics ProcessedBytesIn or ProcessedBytesOut with the dimensions DestinationEdge and SourceRegion set to specific values.
+ View the number of unhealthy endpoints across your accelerator, and determine which endpoint groups they belong to. If you have a large number of endpoint groups, this is especially useful to help you quickly find endpoint groups with endpoints that are experiencing issues. To determine this, view the metric UnhealthyEndpointCount with the dimensions Accelerator, Listener, and EndpointGroup.

## View CloudWatch metrics for your accelerators
<a name="view-metric-data"></a>

You can view the CloudWatch metrics for your accelerators using the CloudWatch console or the AWS CLI. In the console, metrics are displayed as monitoring graphs. The monitoring graphs show data points only if the accelerator is active and receiving requests. 

You must view CloudWatch metrics for Global Accelerator in the US West (Oregon) Region, both in the console or when using the AWS CLI. When you use the AWS CLI, specify the US West (Oregon) Region for your command by including the following parameter: `--region us-west-2`. 

To view metrics using the CloudWatch console, follow the steps in the Amazon CloudWatch User Guide and select the **GlobalAccelerator** namespace. To learn more, see [View available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html). 

**To get the statistics for a metric using the AWS CLI**  
Use the following [get-metric-statistics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/get-metric-statistics.html) command to get statistics for a specified metric and dimension. Note that CloudWatch treats each unique combination of dimensions as a separate metric. You can't retrieve statistics using combinations of dimensions that were not specifically published. You must specify the same dimensions that were used when the metrics were created.

The following example lists the total processed bytes in, per minute, for your accelerator serving from the North America (NA) destination edge.

```
aws cloudwatch get-metric-statistics --namespace AWS/GlobalAccelerator \
--metric-name ProcessedBytesIn \
--region us-west-2 \
--statistics Sum --period 60 \
--dimensions Name=Accelerator,Value=1234abcd-abcd-1234-abcd-1234abcdefgh Name=DestinationEdge,Value=NA \
--start-time 2019-12-18T20:00:00Z --end-time 2019-12-18T21:00:00Z
```

The following is example output from the command:

```
{
    "Label": "ProcessedBytesIn",
    "Datapoints": [
        {
            "Timestamp": "2019-12-18T20:45:00Z",
            "Sum": 2410870.0,
            "Unit": "Bytes"
        },
        {
            "Timestamp": "2019-12-18T20:47:00Z",
            "Sum": 0.0,
            "Unit": "Bytes"
        },
        {
            "Timestamp": "2019-12-18T20:46:00Z",
            "Sum": 0.0,
            "Unit": "Bytes"
        },
        {
            "Timestamp": "2019-12-18T20:42:00Z",
            "Sum": 1560.0,
            "Unit": "Bytes"
        },
        {
            "Timestamp": "2019-12-18T20:48:00Z",
            "Sum": 0.0,
            "Unit": "Bytes"
        },
        {
            "Timestamp": "2019-12-18T20:43:00Z",
            "Sum": 1343.0,
            "Unit": "Bytes"
        },
        {
            "Timestamp": "2019-12-18T20:49:00Z",
            "Sum": 0.0,
            "Unit": "Bytes"
        },
        {
            "Timestamp": "2019-12-18T20:44:00Z",
            "Sum": 35791560.0,
            "Unit": "Bytes"
        }
    ]
}
```