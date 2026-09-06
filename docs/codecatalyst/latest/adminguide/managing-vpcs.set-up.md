

Amazon CodeCatalyst will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For more information, see [Migrating from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

# Setting up an Amazon VPC
<a name="managing-vpcs.set-up"></a>

Use the following procedure to create a VPC.

**To create a VPC**
+ Follow the instructions in the *Amazon VPC User Guide* for [Creating a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-and-other-resources). While following these instructions, keep in mind the VPC requirements needed to work with CodeCatalyst.

For a tutorial that uses CloudFormation to create a VPC, see [AWS Solution: Amazon Virtual Private Cloud on AWS](https://aws.amazon.com/solutions/implementations/vpc/).

## Amazon VPC setup requirements
<a name="managing-vpcs.requirements"></a>

In order for a VPC to work with CodeCatalyst, it must have the following requirements:
+ For **Number of public subnets**, make sure that you have at least one [public subnet](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-types) in any Availability Zone.
+ For **Number of private subnets**, make sure that you have one [private subnet](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-types) in each available Availability Zone in a region.
+ Make sure your VPC has access to the internet. This can be done by adding a route with a destination of `0.0.0.0/0` to an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html#route-tables-internet-gateway) and a [NAT device](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html#route-tables-nat).
+ Make sure that the routing table for private subnets points to the NAT gateway. For more information, see [Routing to a NAT device](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html#route-tables-nat) in the *Amazon VPC User Guide*.
+ Make sure that your internet gateway is attached to the VPC. Public subnets should have a routing table to the internet gateway. For more information, see [Routing to an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html#route-tables-internet-gateway) in the *Amazon VPC User Guide*.
+ Make sure that your security groups allow outbound traffic.
+ Make sure that your IPv4 CIDR block is **not** configured to the `172.16.0.0/12` IP address range. For more information, see [IPv4 VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html#vpc-sizing-ipv4) in the *Amazon VPC User Guide*.
+ As a best practice, make sure that your security groups have no inbound traffic allowed, unless you specifically require this for other reasons.
+ CodeCatalyst does not support assigning a public IP address to the network interfaces that it creates. One way to do this, is to add a NAT device to use CodeCatalyst with your VPC. For more information, see [Connect to the internet or other networks using NAT devices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat.html) in the *Amazon VPC User Guide*.

## Troubleshooting your VPC setup
<a name="managing-vpcs.troubleshooting"></a>

Use the information that appears in the error message to help you identify, diagnose, and address issues.

The following are some guidelines to assist you when troubleshooting common VPC errors:

1. [Make sure that your internet gateway is attached to VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html#Add_IGW_Attach_Gateway).

1. [Make sure that the route table for your public subnet points to the internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-tables-internet-gateway).

1. [Make sure that your network ACLs allow traffic to flow](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules).

1. [Make sure that your security groups allow traffic to flow](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules).

1. [Troubleshoot your NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC-nat-gateway.html#nat-gateway-troubleshooting).

1. [Make sure that the route table for private subnets points to the NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-tables-nat).

1. [Make sure that your IPv4 CIDR block is not configured to the `172.16.0.0/12` IP address range](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironments-troubleshooting.html#troubleshooting-devenvironments-vpc).