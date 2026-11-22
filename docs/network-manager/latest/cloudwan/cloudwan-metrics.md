

# CloudWatch metrics in AWS Cloud WAN

You can use the following features to monitor your Cloud WAN network, analyze traffic patterns, and troubleshoot issues with your Cloud WAN global network.

## Cloud WAN metrics and dimensions
<a name="cloudwan-metrics-tbl"></a>

You can use metrics to verify that your system is performing as expected. For example, you can create a CloudWatch alarm to monitor a specified metric and initiate an action (such as sending a notification to an email address) if the metric goes outside what you consider an acceptable range.

Amazon VPC measures and sends its metrics to CloudWatch in 60-second intervals.

For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

The `AWS/Network Manager` namespace includes the following metrics. All metrics are always reported. 


| Metric | Description | 
| --- | --- | 
| BytesDropCountBlackhole | The number of bytes dropped because they matched a `blackhole` route.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesDropCountNoRoute | The number of bytes dropped because they did not match a route.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesIn | The number of bytes received by the core network.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesOut | The number of bytes sent from the core network.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsIn | The number of packets received by the core network.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsOut | The number of packets sent by the core network.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropCountBlackhole | The number of packets dropped because they matched a `blackhole` route.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropCountNoRoute | The number of packets dropped because they did not match a route.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketDropTTLExpired | The number of packets dropped because the TTL expired.<br />**Statistics**: The only meaningful statistic is `Sum`. | 

### 1:1 NAT metrics
<a name="cloudwan-metrics-nat"></a>

Cloud WAN publishes four metrics in the `AWS/Network Manager` namespace for traffic translated by 1:1 network address translation (NAT). They count a subset of the traffic in the existing `PacketsIn`, `PacketsOut`, `BytesIn`, and `BytesOut` metrics, which continue to report all traffic. Cloud WAN publishes NAT metrics every minute in the US West (Oregon) AWS Region, like other Cloud WAN metrics.

The following table describes the 1:1 NAT metrics.


| Metric | Description | 
| --- | --- | 
| PacketsInNAT | Packets received from an attachment whose source address was translated (SNAT) by that attachment's NAT rules.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| PacketsOutNAT | Packets sent to an attachment whose destination address was translated (DNAT) by that attachment's NAT rules.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesInNAT | Bytes received from an attachment whose source address was translated (SNAT) by that attachment's NAT rules.<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| BytesOutNAT | Bytes sent to an attachment whose destination address was translated (DNAT) by that attachment's NAT rules.<br />**Statistics**: The only meaningful statistic is `Sum`. | 

Cloud WAN counts each metric against the attachment whose rule applied. With double NAT, a packet counts in both the source attachment's `PacketsInNAT` and the destination attachment's `PacketsOutNAT`.

**Dimensions**
+ `CoreNetwork`, `EdgeLocation`
+ `CoreNetwork`, `Attachment`
+ `CoreNetwork`, `Attachment`, `EdgeLocation` (Direct Connect gateway attachments)
+ `CoreNetwork`, `EdgeLocation`, `AvailabilityZone` (VPC attachments only)
+ `CoreNetwork`, `Attachment`, `AvailabilityZone` (VPC attachments only)

Cloud WAN publishes NAT metrics to the core network owner's account. For an attachment owned by another account, Cloud WAN also publishes them to the attachment owner's account.

### Cloud WAN multipath resilience metrics
<a name="cloudwan-metrics-multipath-resilience"></a>

Cloud WAN publishes the following metrics for core networks that have multipath resilience enabled in the core network policy. For more information about enabling multipath resilience, see [Enable multipath resilience in a core network policy](enable-multipath-resilience-cloudwan.md).

Cloud WAN publishes these metrics in the `AWS/Network Manager` namespace for each edge set. Each metric reports traffic in one direction between an edge location in this Region and the peer edge location. The `MultipathResilienceSLANonCompliantSecondsToPeer` metric helps you track delivery against the service level agreement (SLA). For more information about the SLA, see [Multipath Resilience SLA](https://aws.amazon.com/vpc/features/vpc-multipath-resilience/sla) on the AWS website.

The following table lists the multipath resilience metrics and their descriptions.


| Metric | Description | 
| --- | --- | 
| MultipathResiliencePacketsSentToPeer | The number of packets that multipath resilience received at this edge location to send to the peer edge location.<br />**Units**: Count<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| MultipathResiliencePacketsReceivedByPeer | The number of packets that the peer edge location received from this edge location.<br />**Units**: Count<br />**Statistics**: The only meaningful statistic is `Sum`. | 
| MultipathResilienceAvailabilityToPeer | This is the percentage of packets sent to the peer edge location in a one-minute period that multipath resilience measured as delivered. The value is calculated from the total packets sent and received in that minute. A value of 100 means that multipath resilience measured no packet loss in that minute. Minutes with too little traffic to measure always show 100, and minutes with no traffic show no value.<br />**Units**: Percent<br />**Statistics**: The only meaningful statistic is `Minimum`. | 
| MultipathResilienceSLANonCompliantSecondsToPeer | The number of seconds in which delivery of your packets from this edge location to the peer edge location was below the SLA threshold.<br />**Units**: Count<br />**Statistics**: The only meaningful statistic is `Sum`. | 

To filter the metric data, use the following combination of dimensions.


| Dimension | Description | 
| --- | --- | 
| CoreNetwork, SourceEdgeLocation, DestinationEdgeLocation | Filter the metric data by core network, source edge location, and destination edge location. | 

### Cloud WAN metric dimensions
<a name="cloudwan-metrics-dims"></a>

 Filter metric data by a combination of the following Cloud WAN core network metric dimensions.


| Dimension | Description | 
| --- | --- | 
| CoreNetwork, EdgeLocation | Filters the metric data by core network. | 
| Attachment, CoreNetwork | Filters the metric data by core network attachment. | 
| AvailabilityZone, CoreNetwork, EdgeLocation | Filters the metric data by availability zone. This is only applicable for Direct Connect. | 
| Attachment, AvailabilityZone, CoreNetwork | Filters the metric data by both core network attachment and availability zone. | 

## AWS Cloud WAN usage metrics
<a name="cloudwan-metrics-usage"></a>

Cloud WAN usage metrics correspond to AWS service quotas for Cloud WAN. You can configure alarms that alert you when your usage approaches a service quota. For more information about CloudWatch integration with service quotas, see [CloudWatch usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.html) in the *Amazon CloudWatch User Guide*.

The `AWS/Usage` namespace reports the following metric for Cloud WAN:


| Metric | Description | 
| --- | --- | 
| ResourceCount | The number of the specified resources running in your account. The resources are defined by the dimensions associated with the metric.**Statistics**: The only meaningful statistic is `MAXIMUM`. | 

### AWS Cloud WAN metric dimensions
<a name="cloudwan-usage-metrics-dims"></a>

 The following dimensions are used to refine the usage metrics that are published by Cloud WAN.


| Dimension | Description | 
| --- | --- | 
| Service | The name of the AWS service containing the resource. For Cloud WAN usage metrics, the value for this dimension is NetworkManager. | 
| Type | The type of entity that is being reported. Currently, the only valid value for Cloud WAN usage metrics is Resource. | 
| Resource | The type of resource that is running. Currently, valid values for Cloud WAN usage metrics include RoutesPropagated/Inbound and RoutesPropagated/Outbound, which return the number of routes advertised and learnt over Direct Connect attachments. | 
| ResourceID | The unique identifier for the resource, such as a core network attachmentId, and might include a region code prefix for region-specific resources. | 
| Class | This dimension is reserved for future use. | 