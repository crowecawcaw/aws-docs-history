

# CloudWatch metrics in AWS Transit Gateway

Amazon VPC publishes data points to Amazon CloudWatch for your transit gateways and transit gateway attachments. CloudWatch enables you to retrieve statistics about those data points as an ordered set of time series data, known as *metrics*. Think of a metric as a variable to monitor, and the data points as the values of that variable over time. Each data point has an associated timestamp and an optional unit of measurement.

You can use metrics to verify that your system is performing as expected. For example, you can create a CloudWatch alarm to monitor a specified metric and initiate an action (such as sending a notification to an email address) if the metric goes outside what you consider an acceptable range.

Amazon VPC measures and sends its metrics to CloudWatch in 60-second intervals.

For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [Transit gateway metrics](#transit-gateway-metrics)
+ [Attachment-level and availability zone metrics](#transit-gateway-attachment-metrics)
+ [Multipath resilience metrics](#transit-gateway-multipath-resilience-metrics)
+ [Transit gateway metric dimensions](#transit-gateway-dimensions)

## Transit gateway metrics
<a name="transit-gateway-metrics"></a>

The `AWS/TransitGateway` namespace includes the following metrics. 

All metrics are always reported. Their values are dependent on the traffic through the transit gateway. See [Transit gateway metric dimensions](#transit-gateway-dimensions) for the supported dimensions.


| Metric | Description | 
| --- | --- | 
| BytesDropCountBlackhole | The number of bytes dropped because they matched a `blackhole` route.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesDropCountNoRoute | The number of bytes dropped because they did not match a route.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesDropCountNoPolicy | The number of bytes dropped because no policy rule matched. Equivalent to `BytesDropCountNoRoute` for standard route tables. A sustained non-zero value indicates missing or misconfigured rules.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesIn | The number of bytes received by the transit gateway.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesOut | The number of bytes sent from the transit gateway.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsIn | The number of packets received by the transit gateway.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsOut | The number of packets sent by the transit gateway.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesInNAT | The number of bytes received from an attachment whose source address was translated (SNAT) by that attachment's NAT rules. For more information, see [1:1 NAT in AWS Transit Gateway](tgw-nat.md).<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesOutNAT | The number of bytes sent to an attachment whose destination address was translated (DNAT) by that attachment's NAT rules. For more information, see [1:1 NAT in AWS Transit Gateway](tgw-nat.md).<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsInNAT | The number of packets received from an attachment whose source address was translated (SNAT) by that attachment's NAT rules. For more information, see [1:1 NAT in AWS Transit Gateway](tgw-nat.md).<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsOutNAT | The number of packets sent to an attachment whose destination address was translated (DNAT) by that attachment's NAT rules. For more information, see [1:1 NAT in AWS Transit Gateway](tgw-nat.md).<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropCountBlackhole | The number of packets dropped because they matched a `blackhole` route.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropCountNoRoute | The number of packets dropped because they did not match a route.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropCountNoPolicy | The number of packets dropped because no policy rule matched. Equivalent to `PacketDropCountNoRoute` for standard route tables. A sustained non-zero value indicates missing or misconfigured rules.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropCountTTLExpired | The number of packets dropped because the TTL expired.<br />**Statistics**: The only meaningful statistic is `Sum`. | 

## Attachment-level and availability zone metrics
<a name="transit-gateway-attachment-metrics"></a>

The following metrics are available for transit gateway attachments. All attachment metrics are published to the transit gateway owner's account. Individual attachment metrics are also published to the attachment owner's account. The attachment owner can view only the metrics for their own attachment. For more information on the supported attachment types, see [Resource attachments](how-transit-gateways-work.md#tgw-attachments-overview).

Availability zone metrics are available for enabled for availabilty zones (AZs) on transit gateway attachments. Only VPC attachments support per-AZ metrics. All AZ-level metrics are published to the transit gateway owner's account. Individual AZ metrics for an attachment are also published to the attachment owner's account. The attachment owner can view only the per-AZ metrics for their own attachment.

All metrics are always reported. Their values are dependent on the traffic in and/or out of the transit gateway attachment. See [Transit gateway metric dimensions](#transit-gateway-dimensions) for the supported dimensions.


| Metric | Description | 
| --- | --- | 
| BytesDropCountBlackhole | The number of bytes dropped because they matched a `blackhole` route on the transit gateway attachment.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesDropCountNoRoute | The number of bytes dropped because they did not match a route on the transit gateway attachment.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesDropCountNoPolicy | The number of bytes dropped because no policy rule matched on the transit gateway attachment. Equivalent to `BytesDropCountNoRoute` for standard route tables. A sustained non-zero value indicates missing or misconfigured rules.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesIn | The number of bytes received by the transit gateway from the attachment.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesOut | The number of bytes sent from the transit gateway to the attachment.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsIn | The number of packets received by the transit gateway from the attachment.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsOut | The number of packets sent by the transit gateway to the attachment.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesInNAT | The number of bytes received from an attachment whose source address was translated (SNAT) by that attachment's NAT rules. For more information, see [1:1 NAT in AWS Transit Gateway](tgw-nat.md).<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesOutNAT | The number of bytes sent to an attachment whose destination address was translated (DNAT) by that attachment's NAT rules. For more information, see [1:1 NAT in AWS Transit Gateway](tgw-nat.md).<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsInNAT | The number of packets received from an attachment whose source address was translated (SNAT) by that attachment's NAT rules. For more information, see [1:1 NAT in AWS Transit Gateway](tgw-nat.md).<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsOutNAT | The number of packets sent to an attachment whose destination address was translated (DNAT) by that attachment's NAT rules. For more information, see [1:1 NAT in AWS Transit Gateway](tgw-nat.md).<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropCountBlackhole | The number of packets dropped because they matched a `blackhole` route on the transit gateway attachment.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropCountNoRoute | The number of packets dropped because they did not match a route.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropCountNoPolicy | The number of packets dropped because no policy rule matched on the transit gateway attachment. Equivalent to `PacketDropCountNoRoute` for standard route tables. A sustained non-zero value indicates missing or misconfigured rules.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropCountTTLExpired | The number of packets dropped because the TTL expired.<br />**Statistics**: The only meaningful statistic is `Sum`. | 

The `BytesInNAT`, `BytesOutNAT`, `PacketsInNAT`, and `PacketsOutNAT` metrics count the subset of traffic translated by 1:1 NAT. The existing `BytesIn`, `BytesOut`, `PacketsIn`, and `PacketsOut` metrics continue to report all traffic. Each NAT metric is counted against the attachment whose rule applied. For example, traffic from an attachment without NAT rules to the NAT address of a VPC with NAT rules appears in that VPC attachment's `PacketsOutNAT`. It doesn't appear in the source attachment's `PacketsInNAT`. When both the source and destination are translated, a packet counts in both the source attachment's `PacketsInNAT` and the destination attachment's `PacketsOutNAT`.

## Multipath resilience metrics
<a name="transit-gateway-multipath-resilience-metrics"></a>

The following metrics are available for transit gateway peering attachments that have multipath resilience enabled. For more information about enabling multipath resilience, see [Enable multipath resilience for a transit gateway peering attachment](enable-multipath-resilience-tgw.md).

AWS Transit Gateway publishes these metrics in the `AWS/TransitGateway` namespace. Each metric reports traffic in one direction between this AWS Region and the peer Region for the attachment. The `MultipathResilienceSLANonCompliantSecondsToPeer` metric helps you track delivery against the service level agreement (SLA). For more information about the SLA, see [Multipath Resilience SLA](https://aws.amazon.com/vpc/features/vpc-multipath-resilience/sla) on the AWS website.


| Metric | Description | 
| --- | --- | 
| MultipathResiliencePacketsSentToPeer | The number of packets that multipath resilience received in this Region to send to the peer Region.<br />**Units**: Count<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| MultipathResiliencePacketsReceivedByPeer | The number of packets that the peer Region received from this Region.<br />**Units**: Count<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| MultipathResilienceAvailabilityToPeer | This is the percentage of packets sent to the peer Region in a one-minute period that multipath resilience measured as delivered. The value is calculated from the total packets sent and received in that minute. A value of 100 means that multipath resilience measured no packet loss in that minute. Minutes with too little traffic to measure always show 100, and minutes with no traffic show no value.<br />**Units**: Percent<br />**Statistics**: The only meaningful statistic is `Minimum`. | 
| MultipathResilienceSLANonCompliantSecondsToPeer | The number of seconds in which delivery of your packets from this Region to the peer Region was below the SLA threshold.<br />**Units**: Count<br />**Statistics**: The only meaningful statistic is `Sum`. | 

To filter the multipath resilience metric data, use the following combination of dimensions.


| Dimension | Description | 
| --- | --- | 
| TransitGatewayAttachment | Filter the metric data by transit gateway attachment. | 
| SourceRegion | Filter the metric data by the source Region. | 
| DestinationRegion | Filter the metric data by the destination Region. | 

## Transit gateway metric dimensions
<a name="transit-gateway-dimensions"></a>

Filter transit gateway metric data using the following dimensions:


| Dimension | Description | 
| --- | --- | 
| TransitGateway | Filters the metric data by transit gateway. | 
| TransitGatewayAttachment | Filters the metric data by transit gateway attachment. | 
| TransitGateway, AvailabilityZone | Filters the metric data by both transit gateway and availability zone. | 
| TransitGatewayAttachment, AvailabilityZone | Filters the metric data by both transit gateway attachment and availability zone. | 