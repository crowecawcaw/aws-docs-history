# What is Network Flow Monitor?

Network Flow Monitor is a feature of Amazon CloudWatch Network Monitoring. Network Flow Monitor uses fully-managed agents that you
install in your AWS workloads to return performance and availability metrics about network flows.
Using Network Flow Monitor, you can access near real-time metrics, including retransmissions and data transferred, for your
actual workloads. You can also identify whether an underlying AWS network issue occurred for the
network flows tracked by a monitor, by checking network health indicator (NHI) values.

**Key features of Network Flow Monitor**

- With Network Flow Monitor, you receive near real-time metrics for the latency and packet-loss
  experienced by TCP-based traffic within your VPC network, so that you can track and investigate
  network issues for your workload traffic.
- When your AWS workloads experience network degradation, Network Flow Monitor helps you to
  determine if the problem is caused by your application workload or the underlying AWS infrastructure.
  Then, you can quickly focus troubleshooting on the area where the issue is occurring.
  **How to use Network Flow Monitor**

With Network Flow Monitor, you install lightweight agents on your instances, which collect and
aggregate performance metrics. Network Flow Monitor agents analyze TCP traffic, and then export performance
metrics to the Network Flow Monitor service backend.

Agents gather the following metrics for your workloads: TCP round-trip time (RTT), TCP
retransmission timeouts, TCP retransmissions, and data (bytes) transferred. After you install agents
on your instances, the agents detect the corresponding workloads that are hosted by the instances. The
agents then generate network performance metrics and send the metrics to the Network Flow Monitor backend. Metrics
are aggregated into categories such as subnets, Availability Zones, VPCs, and AWS services.

Performance metrics for top contributors (by metric type) from all network flows that are in your Network Flow Monitor scope
are shown on the **Workload insights** tab in the AWS Management Console. By reviewing the
tables and graphs of top contributors, you can determine where there might be impairments that
you want to troubleshoot and which workloads you want to monitor on an ongoing basis, by creating
a monitor.

With a monitor, you can monitor specific workloads more closely over time and see detailed
information about specific network flows. In addition to viewing performance metrics for the top
contributors for the network flows that you've selected, you can view network path information with
the network hops that a network flow has traversed, to help you troubleshoot issues. In addition,
Network Flow Monitor generates a network health indicator (NHI) for monitors. An NHI value of **Degraded**
indicates that there were AWS network issues for at least one of the network flows tracked by
your monitor, during the time period that you've selected.

In addition to reviewing the information in monitors that you create,
we recommend that you also check back regularly to review metrics on the
**Workload insights** page, to see the latest top contributors
for performance metrics for your network flows. As you review the latest information, consider
if it would be helpful to add or remove workloads from your current monitors, or create new monitors.

###### Contents

- [Supported AWS Regions](CloudWatch-NetworkFlowMonitor-Regions.md "CloudWatch-NetworkFlowMonitor-Regions.md")
- [Components](CloudWatch-NetworkFlowMonitor-components.md "CloudWatch-NetworkFlowMonitor-components.md")
- [How it works](CloudWatch-NetworkFlowMonitor-inside-network-flow-monitor.md "CloudWatch-NetworkFlowMonitor-inside-network-flow-monitor.md")
- [Pricing](CloudWatch-NetworkFlowMonitor.md "CloudWatch-NetworkFlowMonitor.md")
