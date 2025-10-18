# Using Network Synthetic Monitor

Network Synthetic Monitor provides visibility into the performance of the network connecting your AWS
 hosted applications to your on-premises destinations, and allows you to identify the source of any
 network performance degradation within minutes. Network Synthetic Monitor is fully managed by AWS, and doesn't require 
 separate agents on monitored resources. Use Network Synthetic Monitor to
 visualize packet loss and latency of your hybrid network connections, and set alerts and thresholds.
 Then, based on this information, you can take action to improve your end users’ experience. 

Network Synthetic Monitor is intended for network operators and application developers who want real-time
 insights into network performance.


## Network Synthetic Monitor key features



* Use Network Synthetic Monitor to benchmark your changing hybrid network environment with continuous
 real-time packet loss and latency metrics.
* When you connect by using AWS Direct Connect, Network Synthetic Monitor can help you to rapidly diagnose
 network degradation within the AWS network with the network health indicator (NHI), which
 Network Synthetic Monitor writes to your Amazon CloudWatch account. The NHI metric is a binary value, based on a probabilistic score 
 about whether network degradation is within AWS.
* Network Synthetic Monitor provides a fully-managed agent approach to monitoring, so you don’t need to install 
 agents either on VPCs or on-premises. To get started, you just need to specify a VPC subnet and an
 on-premises IP address. You can establish a private connection between your VPC and Network Synthetic Monitor resources
 by using AWS PrivateLink. For more information, see [Using CloudWatch, CloudWatch Synthetics, and CloudWatch Network
 Monitoring with interface VPC endpoints](cloudwatch-and-interface-VPC.md "cloudwatch-and-interface-VPC.md").
* Network Synthetic Monitor publishes metrics to CloudWatch Metrics. You can create dashboards to view your
 metrics, and also create actionable thresholds and alarms on the metrics that are specific to your
 application.

For more information, see [How Network Synthetic Monitor works](nw-monitor-how-it-works.md "nw-monitor-how-it-works.md").


## Network Synthetic Monitor terminology and components



* **Probes** — A probe is the traffic that's sent from an AWS-hosted
 resource to an on-premises destination IP address. Network Synthetic Monitor metrics measured by the probe 
 are written into your CloudWatch account for every probe that's configured in a monitor.
* **Monitor** — A monitor displays network performance and other health information
 for traffic that you have created Network Synthetic Monitor *probes* for. You add probes as part of
 creating a monitor, and then you can view network performance metrics information using the monitor.
 When you create a monitor for an application, you add an AWS hosted resource as the
 network source. Network Synthetic Monitor then creates a list of all possible probes between the AWS hosted
 resource and your destination IP addresses. You select the destinations that you want to monitor
 traffic for.
* **AWS network source** — An AWS network source is a monitor probe's originating
 AWS source, which is a subnet in one of your VPCs.
* **Destination** — A destination is the target in your on-premises network for the
 AWS network source. A destination is a combination of your on-premises IP addresses,
 network protocols, ports, and network packet size. IPv4 and IPv6 addresses are both supported.

## Network Synthetic Monitor requirements and limitations


The following summarizes requirements and limitations for Network Synthetic Monitor. For specific quotas (or limits),
 see [Network Synthetic Monitor](cloudwatch_limits.md#nw-monitor-quotas "cloudwatch_limits.md#nw-monitor-quotas").



* Monitor subnets must be owned by the same account as the monitor.
* Network Synthetic Monitor doesn't provide automatic network failover in the event of an AWS network
 issue.
* There's a charge for each probe that you create. For pricing details, see [Pricing for Network Synthetic Monitor](pricing-nw.md "pricing-nw.md").
