# Create and work with monitors in Network Flow Monitor

You create a monitor to see details about the network performance for one or several network flows
 for a workload. For each monitor, Network Flow Monitor publishes end-to-end performance metrics and 
 a network health indicator (NHI), and generates network paths of individual network flows. 
 After you create a monitor, you can view information provided by the monitor
 in the console on the **Monitors** tab.

Flow monitors can help you to assess network performance issues
 that are impacting your workloads, including impairments within an AWS Region
 and issues on the AWS global network between a local and a remote Region. 
 The network health indicator (NHI) provided by the monitor
 also captures the health of the AWS global network on your workload’s 
 network paths between Regions. This helps you to quickly identify whether 
 impairments in a local Region, in the AWS global network, or in the remote Region
 are affecting your workloads. 

For remote Regions, monitors can provide network visibility for flows to 
 the Region’s public IP address, and for private traffic flowing to a remote Region over 
 VPC peering or Transit Gateway peering.

After you create a monitor, you can edit the monitor to make changes (except change the monitor
 name) or delete the monitor, at any time.

The following sections includes procedures for creating, editing, and deleting monitors in
 the Network Flow Monitor console.

###### Contents

* [Create a monitor](CloudWatch-NetworkFlowMonitor-configure-monitors-create.md "CloudWatch-NetworkFlowMonitor-configure-monitors-create.md")
* [Edit a monitor](CloudWatch-NetworkFlowMonitor-configure-monitors-edit.md "CloudWatch-NetworkFlowMonitor-configure-monitors-edit.md")
* [Delete a monitor](CloudWatch-NetworkFlowMonitor-configure-monitors-delete.md "CloudWatch-NetworkFlowMonitor-configure-monitors-delete.md")
