# How Network Synthetic Monitor works

Network Synthetic Monitor is fully managed by AWS, and doesn't require separate agents on monitored resources.
Instead, you specify _probes_ by providing a VPC subnet and on-premises IP addresses.

When you create a monitor in Network Synthetic Monitor for AWS-hosted resources, AWS creates and manages the
infrastructure in the background that is required to perform round-trip time and packet loss measurements.
Because AWS manages the required configurations, you can scale your monitoring rapidly, without needing
to install or uninstall agents within your AWS infrastructure.

When probes are created, customized elastic network interfaces (ENIs) are created and attached to
probe instances and customer subnets. If Network Synthetic Monitor replaces a probe instance, for example, if it becomes
unhealthy, Network Synthetic Monitor detaches the ENIs and reattaches them to the probe replacement. This means that ENI IP
addresses are not changed after they are created, unless you delete a probe and create a new one for
the same source and destination.

Network Synthetic Monitor focuses monitoring on the routes taken by flows from your AWS-hosted resources
instead of broadly monitoring all flows from your AWS Region. If your workloads spread across
multiple Availability Zones, Network Synthetic Monitor can monitor routes from each of your private subnets.

Network Synthetic Monitor publishes round-trip time and packet loss metrics to your
Amazon CloudWatch account, based on the aggregation interval that you set when you create a
monitor. You can also use CloudWatch to set individual latency and packet loss thresholds for each monitor.
For example, you might create an alarm for a packet loss sensitive workload to notify you if the
packet loss average is higher than a static 0.1% threshold. You can also use CloudWatch anomaly
detection to alarm on packet loss or latency metrics that are outside your desired ranges.

## Availability and performance measurements

Network Synthetic Monitor sends periodic active probes from your AWS resource to your on-premises
destinations. When you create a monitor, you specify the following:

- **Aggregation interval:** The time, in seconds, that CloudWatch receives the measured results.
  This will be either every 30 or 60 seconds. The aggregation period you choose for the monitor
  applies to all probes in that monitor.
- **Probe sources (AWS resources):** A source for a probe is a VPC and associated subnets,
  or just a VPC subnet, in the Regions where your network operates.
- **Probe destinations (customer resources):** A destination for a probe
  is the combination of on-premises IP addresses, network protocols, ports, and network packet size.
- **Probe protocol:** One of the supported protocols, ICMP or TCP.
  For more information, see [Supported communication protocols](#nw-monitor-protocol "#nw-monitor-protocol").
- **Port (for TCP):** The port that your network uses to connect.
- **Packet size (for TCP):** The size, in bytes, of each packet transmitted between your AWS hosted
  resource and your destination on a single probe. You can specify a different packet size for each probe in a monitor.

A monitor publishes the following metrics:

- **Round-trip time:** This metric, measured in microseconds, is a measure of
  performance. It records the time it takes for the probe to be transmitted to the destination
  IP address and for the associated response to be received. The round-trip time is the average
  time observed during the aggregation interval.
- **Packet loss:** This metric measures the percentage of total packets sent and records the
  number of transmissions that didn't receive an associated response. No response implies that
  the packets were lost along the network path.

## Supported communication protocols

Network Synthetic Monitor supports two protocols for probes: ICMP and TCP.

ICMP-based probes carry ICMP echo requests from your AWS hosted resources to the
destination address, and expect an ICMP echo reply in response. Network Synthetic Monitor
uses the information on the ICMP echo request and reply messages to calculate round-trip
time and packet loss metrics.

TCP-based probes carry TCP SYN packets from your AWS hosted resources to the destination
address and port, and expect a TCP SYN+ACK packet in response. Network Synthetic Monitor uses the
information on the TCP SYN and TCP SYN+ACK messages to
calculate round-trip time and packet loss metrics. Network Synthetic Monitor periodically
switches source TCP ports to increase network coverage, which increases the probability
of detecting packet loss.

## Network health indicator for AWS

Network Synthetic Monitor publishes a network health indicator (NHI) metric that provides information on
issues with the AWS network for paths that include destinations connected through Direct Connect.

The NHI binary value is based on a statistical measure of the health of the AWS-controlled
network path from the AWS hosted resource, where the monitor is deployed, to the Direct
Connect location. Network Synthetic Monitor uses outlier detection to calculate availability drops or lower performance
along the network paths.

NHI is not accurate for Direct Connect attachments that use intermediary routing with Cloud WAN. When you
have a hybrid network that includes Cloud WAN, do not use the NHI value as an indication of a performance issue.

###### Note

Each time that you create a new monitor, add a probe, or re-activate a probe, the NHI for the
monitor is delayed by a few hours while AWS collects data to perform outlier detection.

To provide the NHI value, Network Synthetic Monitor applies statistical correlation across AWS
sample datasets, as well as to the packet loss and round-trip latency metrics for traffic
simulating your network path. NHI can be one of two values: 1 or 0. A value of 1
indicates that Network Synthetic Monitor observed a network degradation within the AWS controlled network
path. A value of 0 indicates that Network Synthetic Monitor did not observe any network degradation for the AWS
network along the path. Using the NHI value enables you to more quickly gain awareness of
the cause of network issues. For example, you can set alerts on the NHI metric so you're notified about ongoing issues
with the AWS network along your network paths.

## Support for IPv4 and IPv6 addresses

Network Synthetic Monitor provides availability and performance metrics over IPv4 or IPv6 networks, and can
monitor either IPv4 or IPv6 addresses from dual-stack VPCs. Network Synthetic Monitor doesn’t allow both IPv4
and IPv6 destinations to be configured in the same monitor; you can create separate
monitors for IPv4-only and IPv6-only destinations.
