

# Multipath resilience metrics and dimensions

The following metrics are available for VPC peering connections that have multipath resilience enabled. For more information about enabling multipath resilience, see [Enable multipath resilience for a VPC peering connection](enable-multipath-resilience-peering.md). The description column includes the [units](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Unit) and [statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html) for each metric.

Amazon VPC publishes these metrics in the `AWS/EC2` namespace. Each metric reports traffic in one direction between this Region and the peer Region. The `MultipathResilienceSLANonCompliantSecondsToPeer` metric helps you track delivery against the service level agreement (SLA). For more information about the SLA, see [Multipath Resilience SLA](https://aws.amazon.com/vpc/features/vpc-multipath-resilience/sla) on the AWS website.

The following table lists the multipath resilience metrics and their descriptions.


| Metric | Description | 
| --- | --- | 
| MultipathResiliencePacketsSentToPeer | The number of packets that multipath resilience received in this Region to send to the peer Region.<br />Units: Count<br />Statistics: The most useful statistic is `Sum`. | 
| MultipathResiliencePacketsReceivedByPeer | The number of packets that the peer Region received from this Region.<br />Units: Count<br />Statistics: The most useful statistic is `Sum`. | 
| MultipathResilienceAvailabilityToPeer | This is the percentage of packets sent to the peer Region in a one-minute period that multipath resilience measured as delivered. The value is calculated from the total packets sent and received in that minute. A value of 100 means that multipath resilience measured no packet loss in that minute. Minutes with too little traffic to measure always show 100, and minutes with no traffic show no value.<br />Units: Percent<br />Statistics: The most useful statistic is `Minimum`. | 
| MultipathResilienceSLANonCompliantSecondsToPeer | The number of seconds in which delivery of your packets from this Region to the peer Region was below the SLA threshold.<br />Units: Count<br />Statistics: The most useful statistic is `Sum`. | 

To filter the metric data, use the following combination of dimensions.


| Dimension | Description | 
| --- | --- | 
| ConnectionId | Filter the metric data by the VPC peering connection ID. | 
| SourceRegion | Filter the metric data by the source Region. | 
| DestinationRegion | Filter the metric data by the destination Region. | 