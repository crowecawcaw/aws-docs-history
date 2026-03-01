# Understanding MemoryDB and VPCs

MemoryDB is fully integrated with Amazon VPC. For MemoryDB users, this means the following:

- MemoryDB always launches your cluster in a VPC.
- If you're new to AWS,
  a default VPC will be created for you automatically.
- If you have a default VPC and don't specify a subnet when you launch a cluster,
  the cluster launches into your default Amazon VPC.
  For more information, see
  [Detecting Your Supported Platforms and Whether You Have a Default VPC](../../../vpc/latest/userguide/default-vpc.md#detecting-platform "../../../vpc/latest/userguide/default-vpc.md#detecting-platform").

With Amazon VPC, you can create a virtual network in the AWS Cloud that closely resembles a
traditional data center. You can configure your VPC, including selecting its IP
address range, creating subnets, and configuring route tables, network gateways, and
security settings.

MemoryDB manages
software upgrades, patching, failure detection, and recovery.

## Overview of MemoryDB in a VPC

- A VPC is an isolated portion of the AWS Cloud that is assigned its own block of IP addresses.
- An internet gateway connects your VPC directly to the internet and provides access to other AWS resources such as Amazon Simple Storage Service (Amazon S3) that are running outside your VPC.
- An Amazon VPC subnet is a segment of the IP address range of a VPC where you can isolate AWS resources according to your security and operational needs.
- An Amazon VPC security group controls inbound and outbound traffic for your MemoryDB clusters and Amazon EC2 instances.
- You can launch a MemoryDB cluster in the subnet. The nodes have private IP addresses from the subnet's range of addresses.
- You can also launch Amazon EC2 instances in the subnet. Each Amazon EC2 instance has a private IP address from the subnet's range of addresses. The Amazon EC2 instance can connect to any node in the same subnet.
- For an Amazon EC2 instance in your VPC to be reachable from the internet, you need to assign a static, public address called a Elastic IP address to the instance.

## Prerequisites

To create a MemoryDB cluster within a VPC, your VPC must meet the following
requirements:

- Your VPC must allow nondedicated Amazon EC2 instances. You cannot use MemoryDB in a VPC that is
  configured for dedicated instance tenancy.
- A subnet group must be defined for your VPC. MemoryDB uses that subnet group to
  select a subnet and IP addresses within that subnet to associate with your
  nodes.
- A security group must be defined for your VPC, or you can use the default
  provided.
- CIDR blocks for each subnet must be large enough to provide spare IP addresses for MemoryDB to
  use during maintenance activities.

## Routing and security

You can configure routing in your VPC to control where traffic flows (for example, to the
internet gateway or virtual private gateway). With an internet gateway, your VPC
has direct access to other AWS resources that are not running in your VPC. If you
choose to have only a virtual private gateway with a connection to your
organization's local network, you can route your internet-bound traffic over the VPN
and use local security policies and firewall to control egress. In that case, you
incur additional bandwidth charges when you access AWS resources over the internet.

You can use Amazon VPC security groups to help secure the MemoryDB clusters and Amazon EC2 instances in your
Amazon VPC. Security groups act like a firewall at the instance level, not the subnet
level.

###### Note

We strongly recommend that you use DNS names to connect to your nodes, as the
underlying IP address can change over time.

## Amazon VPC documentation

Amazon VPC has its own set of documentation to describe how to create and use your Amazon VPC. The
following table shows where to find information in the Amazon VPC guides.

| Description                                                                                                                     | Documentation                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How to get started using Amazon VPC                                                                                             | [Getting started with Amazon VPC](../../../vpc/latest/userguide/vpc-getting-started.md "../../../vpc/latest/userguide/vpc-getting-started.md")                                                       |
| How to use Amazon VPC through the AWS Management Console                                                                        | [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md")                                                                                                         |
| Complete descriptions of all the Amazon VPC commands                                                                            | [Amazon EC2 Command Line Reference](../../../AWSEC2/latest/CommandLineReference.md "../../../AWSEC2/latest/CommandLineReference.md") (the Amazon VPC commands are found in the Amazon EC2 reference) |
| Complete descriptions of the Amazon VPC API operations, data types,<br>and errors                                               | [Amazon EC2 API Reference](../../../AWSEC2/latest/APIReference.md "../../../AWSEC2/latest/APIReference.md") (the Amazon VPC API operations are found in the Amazon EC2 reference)                    |
| Information for the network administrator who needs to configure<br>the gateway at your end of an optional IPsec VPN connection | [What is AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")                                                                                       |

For more detailed information about Amazon Virtual Private Cloud, see
[Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/").
