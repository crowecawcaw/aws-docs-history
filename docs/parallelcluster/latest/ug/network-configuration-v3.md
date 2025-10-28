# Network configurations

AWS ParallelCluster uses Amazon Virtual Private Cloud (VPC) for networking. VPC provides a flexible and configurable networking platform where
you can deploy clusters.

The VPC must have `DNS Resolution = yes`, `DNS Hostnames = yes` and DHCP options with the correct domain name for the
Region. The default DHCP Option Set already specifies the required _AmazonProvidedDNS_. If specifying more than one domain name
server, see [DHCP options sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") in the _Amazon VPC User
Guide_.

AWS ParallelCluster supports the following high-level configurations:

- One subnet for both head and compute nodes.
- Two subnets, with the head node in one public subnet, and compute nodes in a private subnet. The subnets can be either new or existing ones.
  All of these configurations can operate with or without public IP addressing. AWS ParallelCluster can also be deployed to use an HTTP proxy for
  all AWS requests. The combinations of these configurations result in many deployment scenarios. For example, you can configure a single public
  subnet with all access over the internet. Or, you can configure a fully private network using AWS Direct Connect and HTTP proxy for all traffic.

Starting from AWS ParallelCluster 3.0.0 it is possible to configure different `SecurityGroups`, `AdditionalSecurityGroups`
and `PlacementGroup` settings for each queue. For more information, see [HeadNode](HeadNode-v3.md "HeadNode-v3.md") / [Networking](HeadNode-v3.md#HeadNode-v3-Networking "HeadNode-v3.md#HeadNode-v3-Networking")
and [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking")
and [AwsBatchQueues](Scheduling-v3.md#Scheduling-v3-AwsBatchQueues "Scheduling-v3.md#Scheduling-v3-AwsBatchQueues") / [Networking](Scheduling-v3.md#Scheduling-v3-AwsBatchQueues-Networking "Scheduling-v3.md#Scheduling-v3-AwsBatchQueues-Networking").

For illustrations of some networking scenarios, see the following architecture diagrams.

###### Topics

- [AWS ParallelCluster in a single public subnet](network-configuration-v3-single-subnet.md "network-configuration-v3-single-subnet.md")
- [AWS ParallelCluster using two subnets](network-configuration-v3-two-subnets.md "network-configuration-v3-two-subnets.md")
- [AWS ParallelCluster in a single private subnet connected using
  AWS Direct Connect](network-configuration-v3-single-subnet-direct-connect.md "network-configuration-v3-single-subnet-direct-connect.md")
- [AWS ParallelCluster with AWS Batch
  scheduler](network-configuration-v3-batch.md "network-configuration-v3-batch.md")
- [AWS ParallelCluster in a single subnet with no internet
  access](aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md "aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md")
