# VPC

A _virtual private cloud (VPC)_ is a virtual network
dedicated to your AWS account. The Amazon VPC service that provides it is a networking
layer for your AWS resources. Using Amazon VPC, you can define a virtual network in your
own logically isolated area within the AWS Cloud. A VPC closely resembles a
traditional network that you might operate in your own data center, with the benefits of
using the AWS scalable infrastructure. Amazon VPC for Amazon EC2 virtual computing environments,
known as _instances_, can be used for a variety of AWS resources.

VPCs offer options that allow for flexibility in a secure environment, for
example:

- To configure your VPC, you can set its IP address range, create subnets,
  configure route tables, network gateways, network interfaces, and security
  settings.
- To make the AWS Cloud an extension of your data center, you can connect your
  VPC to your own corporate data center.
- You can connect your instances in the VPC to the internet, or keep your
  instances isolated on a private network.
- To protect the resources in each subnet, you can use multiple layers of
  security, including security groups and network access control lists (ACLs).
  For more information, see the [Amazon VPC User
  Guide](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

If you have a default VPC and don't specify a subnet when you launch an instance, the
instance is launched into your default VPC. You can launch instances into your default
VPC without needing to know anything about Amazon VPC.

If you don't already have a VPC or want to use a new one, you can create one by
following the instructions in [Getting started
with Amazon VPC](../../../vpc/latest/userguide/vpc-getting-started.md "../../../vpc/latest/userguide/vpc-getting-started.md") in the _Amazon VPC User Guide_. This
section offers guidance on how to set up your VPC. The guidance includes options for
public and private subnets and for AWS Site-to-Site VPN access for your corporate
network (known as _on-premises access_). You can also
use VPC peering or AWS Direct Connect to reach an on-premises database instance.

**Using the AWS CLI**

You can start to set up a VPC in Amazon EC2 by using the [`aws
 ec2 create-vpc`](../../../cli/latest/reference/ec2/create-vpc.md "../../../cli/latest/reference/ec2/create-vpc.md") command. To learn more about VPC settings for the
AWS CLI, see [Examples
for VPC](../../../vpc/latest/userguide/VPC_Scenarios.md "../../../vpc/latest/userguide/VPC_Scenarios.md") in the _Amazon VPC User Guide_.

**Using the Amazon EC2 console**

To view your VPC or create a new one in Amazon EC2, sign in to the AWS Management Console and open the
Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
To create a new VPC, choose **Launch VPC Wizard** and follow the
instructions. Note your new VPC ID for future reference. To view VPCs, choose
**Your VPCs** on the left side.

**Amazon VPC resources in VPC guides and AWS Support articles**

For general information, see [Working with VPCs
and subnets](../../../vpc/latest/userguide/working-with-vpcs.md "../../../vpc/latest/userguide/working-with-vpcs.md").

For step-by-step instructions for setting up a VPC, see the following topics (choose
the ones that relate to your scenario):

- [Create an IPv4 VPC and subnets using the AWS CLI](../../../vpc/latest/userguide/vpc-subnets-commands-example.md "../../../vpc/latest/userguide/vpc-subnets-commands-example.md")
- [Sharing public subnets and private subnets](../../../vpc/latest/userguide/example-vpc-share.md "../../../vpc/latest/userguide/example-vpc-share.md")
- [Working with site-to-site VPN](../../../vpn/latest/s2svpn/working-with-site-site.md "../../../vpn/latest/s2svpn/working-with-site-site.md")
- [AWS
  Site-to-Site VPN Network Administrator Guide](../../../vpc/latest/adminguide/Welcome.md "../../../vpc/latest/adminguide/Welcome.md") (choose your network
  device for specific instructions)
- [Generic Customer Gateway Device Without Border Gateway Protocol](../../../vpc/latest/adminguide/GenericConfigNoBGP.md#DetailedViewCustomerGateway6 "../../../vpc/latest/adminguide/GenericConfigNoBGP.md#DetailedViewCustomerGateway6")
  (recommended for customer gateways)
  If you want to migrate data source instances into the same VPC, see the following
  AWS Support articles:

- [How do I change the VPC for an Amazon RDS DB instance?](https://aws.amazon.com/premiumsupport/knowledge-center/change-vpc-rds-db-instance/ "https://aws.amazon.com/premiumsupport/knowledge-center/change-vpc-rds-db-instance/")
- [How do I move my EC2 instance to another subnet, Availability Zone, or
  VPC?](https://aws.amazon.com/premiumsupport/knowledge-center/move-ec2-instance/ "https://aws.amazon.com/premiumsupport/knowledge-center/move-ec2-instance/")
- [How do I move my Amazon Redshift cluster from one VPC to another
  VPC?](https://aws.amazon.com/premiumsupport/knowledge-center/move-redshift-cluster-vpcs/ "https://aws.amazon.com/premiumsupport/knowledge-center/move-redshift-cluster-vpcs/")
  For troubleshooting information, see [How do I troubleshoot issues with VPC route tables?](https://aws.amazon.com/premiumsupport/knowledge-center/troubleshoot-vpc-route-table/ "https://aws.amazon.com/premiumsupport/knowledge-center/troubleshoot-vpc-route-table/"), an article with video
  created by AWS Support.
