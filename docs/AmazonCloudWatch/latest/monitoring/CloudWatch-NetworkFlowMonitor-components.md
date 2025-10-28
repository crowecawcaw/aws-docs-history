# Components and features of Network Flow Monitor

Network Flow Monitor uses or references the following concepts.

**Agents**
An _agent_ in Network Flow Monitor is a software application that you install on your Amazon EC2
instance resources. The application has two parts:

- The first part receives events related to TCP connections and is registered
  within the Linux kernel using eBPF. eBPF is the Linux extended Berkley Packet Filter (eBPF)
  capability that allows a designated program to receive certain events raised by the Linux kernel.
- The second part aggregates the statistics collected by the eBPF portion.
  The agent sends the aggregated metrics to the Network Flow Monitor backend about every 30 seconds,
  with a 5 second potential jitter (in other words, 25 to 35 seconds).

For more information about agents, see [How it works](CloudWatch-NetworkFlowMonitor-inside-network-flow-monitor.md "CloudWatch-NetworkFlowMonitor-inside-network-flow-monitor.md").

**Top contributors**
_Top contributors_ are the network flows that have the highest values for
a specific metric (such as retransmissions) in your Network Flow Monitor scope or
among the network flows you're tracking in a monitor. Reviewing the
flows with the highest reported numbers for performance metric measurements can
help you see where there might be impairments to investigate. Network Flow Monitor returns
performance metrics for top contributors in your monitoring scope for
_workload insights_. In addition, if you create a monitor,
Network Flow Monitor returns performance metrics for top contributors for the
network flows that you choose for the monitor.

**Local and remote resources**
A _local resource_ is the host location—or
a location of multiple hosts—where a Network Flow Monitor agent is installed. It can be a
subnet, a VPC, an Availability Zone, or an AWS Region. For example, consider a workload
that consists of an interaction between a web service and a backend database, for
example, DynamoDB. In this scenario, the local resource is the subnet of the EC2 instance
hosting the web service, which also runs the agent. A network flow is typically
directional, though it can be configured to be bi-directional.

A _remote resource_ is the other end of a network flow. In this example
of a web service with a backend database, DynamoDB is the remote resource. A remote resource
can be a subnet, a VPC, an Availability Zone, an AWS service, or an AWS Region. If you
specify a Region as a remote resource, Network Flow Monitor measures performance for the network
flow up to the edge of the Region. It does not measure performance to specific endpoints within
the Region.

A resource is identified by the ARN of the resource, the name of the AWS
service, or, for an Availability Zone or Region, by the name of the zone or Region.

**Workload insights**
_Workload insights_ includes the performance metrics returned for all the network
flows in your scope. In the AWS Management Console, the **Workload insights** page provides
performance data about workloads where you've installed Network Flow Monitor agents on workload instances.
The **Workload insights** page provides a view into your applications that includes
the amount of data transferred and several other metrics, grouped into categories of workloads. For
example, you can see all the metrics for workloads with traffic between Availability Zones (AZs)
or within an AZ. By using these insights, you can select workloads for which you want to create a
monitor to see more details and to track network performance on an ongoing basis.

**Monitors**
You create a _monitor_ so that you can monitor, on an ongoing basis, the
network performance for one or several specific workloads, and see more detailed information
about the network flows. For each monitor, Network Flow Monitor publishes end-to-end performance metrics, and
a network health indicator (NHI), which you can use to help determine attribution for impairments.
We recommend that you review information on the **Workload insights** page to see
which network flows you want to focus on, and then create a monitor for those flows. Then, by regularly
reviewing **Workload insights**, you can decide if you have the monitors
that you need, or if creating new monitors would be helpful.

**Network health indicator (NHI)**
The _network health indicator_ (NHI) is a binary value that informs you
whether there were AWS network issues for one or more of the network flows tracked by a monitor,
during a time period that you choose. When the NHI value is 1, or **Degraded**,
there was an AWS network issue for at least one network flow. With the NHI indicator,
you can quickly decide whether to focus troubleshooting efforts on an AWS network issue
or network problems originating with your workloads.

For more information, see [View Network Flow Monitor metrics in CloudWatch](CloudWatch-NetworkFlowMonitor-cw-metrics.md "CloudWatch-NetworkFlowMonitor-cw-metrics.md").

**Scope**
In Network Flow Monitor, the _scope_ is the account or accounts that you
have observability for when you look at network performance indicators. If you sign in as
a management account and configure AWS Organizations with CloudWatch, you can set your scope to more than one
account in your organization (up to 100 accounts total). Otherwise, if you sign in with an
AWS account that does not have management permissions in Organizations, or if you have not configured
Organizations with CloudWatch, Network Flow Monitor sets your scope to the account that you're signed in with.

After you have configured Organizations, you can change your scope by adding or removing accounts.
However, whenever you change the scope, Network Flow Monitor must create a new topology of the resources in
the scope. For more information, see [Add multiple accounts to your scope](CloudWatch-NetworkFlowMonitor-multi-account.md#CloudWatch-NetworkFlowMonitor-multi-account.config-scope "CloudWatch-NetworkFlowMonitor-multi-account.md#CloudWatch-NetworkFlowMonitor-multi-account.config-scope").

Network Flow Monitor generates a unique **scope ID** for the scope. Queries for metrics data use
the scope ID to determine the resources that the Network Flow Monitor generates metrics for. (You must
install agents to gather and submit metrics data before you can view the performance metrics for
an account with Network Flow Monitor.)

**Query ID**
Network Flow Monitor generates a unique _query ID_ for each query that
is created to retrieve performance metrics data, such as a query for top contributors for a monitor.
By using a query ID with an API call in Network Flow Monitor, you can check the status of a query, stop
a query, run the query again, or work with the query in other ways.

**Performance metrics**
Network Flow Monitor gathers and calculates end-to-end _performance metrics_, including TCP
round-trip time (RTT), TCP retransmissions, TCP retransmission time outs, and bytes transferred
for each flow that is in your Network Flow Monitor scope. The service aggregates these metrics and returns them to the service backend.
You can view top contributors by metric type. When you see an anomaly in Network Flow Monitor, you can also
check the network health indicator (NHI) to see if there is an underlying AWS network issue.

Be aware that RTT data can be sparse because RTT is not always calculated.

You can also use Amazon CloudWatch features to create dashboards, alarms, and notifications based on these metrics.
For example, you can learn about setting up alarms with Network Flow Monitor metrics by reviewing the information
in [Create alarms with Network Flow Monitor](CloudWatch-NetworkFlowMonitor-create-alarm.md "CloudWatch-NetworkFlowMonitor-create-alarm.md").
