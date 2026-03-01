# Install Network Flow Monitor agents on EC2 and self-managed Kubernetes instances

To provide performance metrics for network flows in your AWS workloads, Network Flow Monitor relies on _agents_
that you install, which send the metrics to Network Flow Monitor. You install Network Flow Monitor agents on your instances, and then set the correct
permissions for the agents so that they can send metrics to the Network Flow Monitor backend.

An agent is a lightweight software application that you install on your resources, such as your VPC EC2 instances.
Agents send performance metrics to the Network Flow Monitor backend on an ongoing basis. Then, you can view the metrics on the
**Workload insights** page in the Network Flow Monitor console. You can also track detailed metrics for a specific
network flow, or set of flows, by creating a monitor.

The steps that you follow to deploy agents in your instances depend on the type of instance: Amazon EKS Kubernetes instances,
VPC EC2 instances, or self-managed (non-EKS) Kubernetes instances.

- For information about working with Amazon EKS, including installing agents on EKS,
  see [Work with EKS](CloudWatch-NetworkFlowMonitor-work-with-eks.md "CloudWatch-NetworkFlowMonitor-work-with-eks.md").
- For information about installing agents on VPC EC2 instances and self-managed Kubernetes instances,
  see the sections in this chapter.
  You can establish a private connection between your VPC and Network Flow Monitor agents
  by using AWS PrivateLink. For more information, see [Using CloudWatch, CloudWatch Synthetics, and CloudWatch Network Monitoring with interface VPC endpoints](cloudwatch-and-interface-VPC.md "cloudwatch-and-interface-VPC.md").

###### Contents

- [Linux versions supported for Network Flow Monitor agents](CloudWatch-NetworkFlowMonitor-agents-versions.md "CloudWatch-NetworkFlowMonitor-agents-versions.md")
- [Install and manage agents for EC2 instances](CloudWatch-NetworkFlowMonitor-agents-ec2.md "CloudWatch-NetworkFlowMonitor-agents-ec2.md")
- [Install agents for self-managed Kubernetes instances](CloudWatch-NetworkFlowMonitor-agents-kubernetes-non-eks.md "CloudWatch-NetworkFlowMonitor-agents-kubernetes-non-eks.md")
