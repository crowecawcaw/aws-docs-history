# Get started with Network Flow Monitor

To help you get started, the section provides a high level overview of the steps to configure,
 and then gain insights, with Network Flow Monitor. For details, see the additional sections in this guide 
 about initializing Network Flow Monitor, configuring agents, and creating monitors.


* Initialize Network Flow Monitor, to accept service-linked role permissions, create a
 *scope* for monitoring in Network Flow Monitor, and create an initial topology. If you want
 to observe network performance for network flows for instances in multiple accounts, you
 must integrate with AWS Organizations, and then add the accounts to your scope. To learn more, see
 [Initialize Network Flow Monitor](CloudWatch-NetworkFlowMonitor-configure-begin.md "CloudWatch-NetworkFlowMonitor-configure-begin.md").
* Deploy *agents* on your instances, by using AWS Systems Manager or 
 by configuring Kubernetes, depending on how your resources are deployed. If you install
 agents on VPC EC2 instances, make sure that you enable permissions for agents on each instance
 to send metrics to the Network Flow Monitor backend. To learn more, see
 [Install Network Flow Monitor agents on instances](CloudWatch-NetworkFlowMonitor-agents.md "CloudWatch-NetworkFlowMonitor-agents.md").
* Review top contributor metrics for network flows returned by the agents,
 to gain *workload insights*. Workload insights provide a high-level
 view of the performance for network flows in the scope you're monitoring.
* Based on the network flows that you want to see detailed network information
 about, create one or more *monitors*. For each monitor, specify the
 local and remote resources that you want to monitor network flows between. Using a monitor, you can 
 see detailed metrics and information, including the network health indicator, as
 well as view network paths for specific network flows, over time periods that you select.
* On a regular basis: 




	+ Review network flow information in the monitors that
	 you've created, to learn about and help troubleshoot network impairments in your workloads.
	+ Review workload insights for the network flows that
	 you're monitoring, to determine if the monitors that you've created are covering the 
	 most relevant network flows or if it would be helpful to create new monitors.
