# Install Network Flow Monitor agents on instances

To provide performance metrics for network flows in your AWS workloads, Network Flow Monitor relies on *agents* 
 that you install, which send the metrics to Network Flow Monitor. You install Network Flow Monitor agents on your instances, and then set the correct 
 permissions for the agents so that they can send metrics to the Network Flow Monitor backend.

An agent is a lightweight software application that you install on your resources, such as your VPC EC2 instances. 
 Agents send performance metrics to the Network Flow Monitor backend on an ongoing basis. Then, you can view the metrics on the 
 **Workload insights** page in the Network Flow Monitor console. You can also track detailed metrics for a specific
 network flow, or set of flows, by creating a monitor.

The instances that you install agents on must be running supported versions and distributions of Linux. 
 Network Flow Monitor supports agents to run only on Linux, and the Linux kernel version must be 5.8 or later. The following
 Linux distributions are supported. Note that agents are tested to run on the latest versions of these
 distributions.


* Amazon Linux
* Ubuntu
* Red Hat
* Suse Linux
* Debian distributions for both x86 and aarch64
You can establish a private connection between your VPC and Network Flow Monitor agents
 by using AWS PrivateLink. For more information, see [Using CloudWatch, CloudWatch Synthetics, and CloudWatch Network
 Monitoring with interface VPC endpoints](cloudwatch-and-interface-VPC.md "cloudwatch-and-interface-VPC.md").

The steps that you follow to deploy agents in your instances depend on the type of instance: VPC EC2 instances, 
 Amazon EKS Kubernetes instances, or self-managed (non-EKS) Kubernetes instances.

###### Contents

* [Install and manage agents for EC2 instances](CloudWatch-NetworkFlowMonitor-agents-ec2.md "CloudWatch-NetworkFlowMonitor-agents-ec2.md")
* [Install agents for self-managed Kubernetes instances](CloudWatch-NetworkFlowMonitor-agents-kubernetes-non-eks.md "CloudWatch-NetworkFlowMonitor-agents-kubernetes-non-eks.md")
* [Install the EKS AWS Network Flow Monitor Agent add-on](CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks.md "CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks.md")
