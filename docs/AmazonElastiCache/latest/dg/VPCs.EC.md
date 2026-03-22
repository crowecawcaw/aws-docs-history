# Understanding ElastiCache and Amazon VPCs

ElastiCache is fully integrated with the Amazon Virtual Private Cloud (Amazon VPC). For ElastiCache users, this means the following:

- If your AWS account supports only the EC2-VPC platform,
  ElastiCache always launches your cluster in an Amazon VPC.
- If you're new to AWS,
  your clusters will be deployed into an Amazon VPC.
  A default VPC will be created for you automatically.
- If you have a default VPC and don't specify a subnet when you launch a cluster,
  the cluster launches into your default Amazon VPC.
  For more information, see
  [Detecting Your Supported Platforms and Whether You Have a Default VPC](../../../vpc/latest/userguide/default-vpc.md#detecting-platform "../../../vpc/latest/userguide/default-vpc.md#detecting-platform").

With Amazon Virtual Private Cloud, you can create a virtual network in the AWS cloud that closely resembles a
traditional data center. You can configure your Amazon VPC, including selecting its IP
address range, creating subnets, and configuring route tables, network gateways, and
security settings.

The basic functionality of ElastiCache is the same in a virtual private cloud; ElastiCache manages
software upgrades, patching, failure detection and recovery whether your clusters
are deployed inside or outside an Amazon VPC.

ElastiCache cache nodes deployed outside an Amazon VPC are assigned an IP address to which
the endpoint/DNS name resolves. This provides connectivity from Amazon Elastic Compute Cloud (Amazon EC2)
instances. When you launch an ElastiCache cluster into an Amazon VPC private subnet, every cache
node is assigned a private IP address within that subnet.

## Overview of ElastiCache in an Amazon VPC

The following diagram and table describe the Amazon VPC environment, along with ElastiCache clusters and
Amazon EC2 instances that are launched in the Amazon VPC.

![Diagram showing the Amazon VPC environment with ElastiCache clusters and Amazon EC2 instances.](images/vpc-overview-diagram.png)

|                          |                                                                                                                                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Numbered bullet point 1. | The Amazon VPC is an isolated portion of the AWS Cloud that is assigned its own block of IP<br>addresses.                                                                                                                       |
| Numbered bullet point 2. | An Internet gateway connects your Amazon VPC directly to the Internet and provides access to<br>other AWS resources such as Amazon Simple Storage Service<br>(Amazon S3) that are running outside your Amazon VPC.              |
| Numbered bullet point 3. | An Amazon VPC subnet is a segment of the IP address range of an Amazon VPC where you can<br>isolate AWS resources according to your security and operational<br>needs.                                                          |
| Numbered bullet point 4. | A routing table in the Amazon VPC directs network traffic between the subnet and the<br>Internet. The Amazon VPC has an implied router, which is symbolized in<br>this diagram by the circle with the R.                        |
| Numbered bullet point 5. | An Amazon VPC security group controls inbound and outbound traffic for your ElastiCache clusters<br>and Amazon EC2 instances.                                                                                                   |
| Numbered bullet point 6. | You can launch an ElastiCache cluster in the subnet. The cache nodes have private<br>IP addresses from the subnet's range of addresses.                                                                                         |
| Numbered bullet point 7. | You can also launch Amazon EC2 instances in the subnet. Each Amazon EC2 instance has a private IP<br>address from the subnet's range of addresses. The Amazon EC2 instance<br>can connect to any cache node in the same subnet. |
| Numbered bullet point 8. | For an Amazon EC2 instance in your Amazon VPC to be reachable from the Internet, you need to assign<br>a static, public address called an Elastic IP address to the<br>instance.                                                |

## Prerequisites

To create an ElastiCache cluster within an Amazon VPC, your Amazon VPC must meet the following
requirements:

- The Amazon VPC must allow nondedicated Amazon EC2 instances. You cannot use ElastiCache in an Amazon VPC that is
  configured for dedicated instance tenancy.
- A cache subnet group must be defined for your Amazon VPC. ElastiCache uses that cache subnet group to
  select a subnet and IP addresses within that subnet to associate with your VPC endpoints or
  cache nodes.
- CIDR blocks for each subnet must be large enough to provide spare IP addresses for ElastiCache to
  use during maintenance activities.

## Routing and security

You can configure routing in your Amazon VPC to control where traffic flows (for example, to the
Internet gateway or virtual private gateway). With an Internet gateway, your Amazon VPC
has direct access to other AWS resources that are not running in your Amazon VPC. If you
choose to have only a virtual private gateway with a connection to your
organization's local network, you can route your Internet-bound traffic over the VPN
and use local security policies and firewall to control egress. In that case, you
incur additional bandwidth charges when you access AWS resources over the Internet.

You can use Amazon VPC security groups to help secure the ElastiCache clusters and Amazon EC2 instances in your
Amazon VPC. Security groups act like a firewall at the instance level, not the subnet
level.

###### Note

We strongly recommend that you use DNS names to connect to your cache nodes, as the
underlying IP address can change.

## Amazon VPC documentation

Amazon VPC has its own set of documentation to describe how to create and use your
Amazon VPC. The following table gives links to the Amazon VPC guides.

| Description                                                                                                                     | Documentation                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How to get started using Amazon VPC                                                                                             | [Getting started with Amazon VPC](../../../vpc/latest/userguide/vpc-getting-started.md "../../../vpc/latest/userguide/vpc-getting-started.md")                                         |
| How to use Amazon VPC through the AWS Management Console                                                                        | [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md")                                                                                           |
| Complete descriptions of all the Amazon VPC commands                                                                            | [Amazon EC2 Command Line Reference](../../../cli/latest/reference/ec2.md "../../../cli/latest/reference/ec2.md") (the Amazon VPC commands are found in the Amazon EC2 reference)       |
| Complete descriptions of the Amazon VPC API operations, data types,<br>and errors                                               | [Amazon EC2 Command Line Reference](../../../cli/latest/reference/ec2.md "../../../cli/latest/reference/ec2.md") (the Amazon VPC API operations are found in the Amazon EC2 reference) |
| Information for the network administrator who needs to configure<br>the gateway at your end of an optional IPsec VPN connection | [What is AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")                                                                         |

For more detailed information about Amazon Virtual Private Cloud, see
[Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/").
