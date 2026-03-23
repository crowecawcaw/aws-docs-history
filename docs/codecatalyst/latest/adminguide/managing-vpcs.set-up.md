Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Setting up an Amazon VPC

Use the following procedure to create a VPC.

###### To create a VPC

- Follow the instructions in the _Amazon VPC User Guide_ for [Creating a VPC](../../../vpc/latest/userguide/create-vpc.md#create-vpc-and-other-resources "../../../vpc/latest/userguide/create-vpc.md#create-vpc-and-other-resources").
  While following these instructions, keep in mind the VPC requirements needed to work with CodeCatalyst.
  For a tutorial that uses CloudFormation to create a VPC, see [AWS Solution: Amazon Virtual Private Cloud on AWS](https://aws.amazon.com/solutions/implementations/vpc/ "https://aws.amazon.com/solutions/implementations/vpc/").

## Amazon VPC setup requirements

In order for a VPC to work with CodeCatalyst, it must have the following requirements:

- For **Number of public subnets**, make sure that you have at least one [public subnet](../../../vpc/latest/userguide/configure-subnets.md#subnet-types "../../../vpc/latest/userguide/configure-subnets.md#subnet-types") in any Availability Zone.
- For **Number of private subnets**, make sure that you have one [private subnet](../../../vpc/latest/userguide/configure-subnets.md#subnet-types "../../../vpc/latest/userguide/configure-subnets.md#subnet-types") in each available Availability Zone in a region.
- Make sure your VPC has access to the internet. This can be done by adding a route with a destination of `0.0.0.0/0` to
  an [internet gateway](../../../vpc/latest/userguide/route-table-options.md#route-tables-internet-gateway "../../../vpc/latest/userguide/route-table-options.md#route-tables-internet-gateway") and a [NAT device](../../../vpc/latest/userguide/route-table-options.md#route-tables-nat "../../../vpc/latest/userguide/route-table-options.md#route-tables-nat").
- Make sure that the routing table for private subnets points to the NAT gateway. For more information, see
  [Routing to a NAT device](../../../vpc/latest/userguide/route-table-options.md#route-tables-nat "../../../vpc/latest/userguide/route-table-options.md#route-tables-nat") in the _Amazon VPC User Guide_.
- Make sure that your internet gateway is attached to the VPC. Public subnets should have a routing table to the internet gateway. For more information, see
  [Routing to an internet gateway](../../../vpc/latest/userguide/route-table-options.md#route-tables-internet-gateway "../../../vpc/latest/userguide/route-table-options.md#route-tables-internet-gateway") in the _Amazon VPC User Guide_.
- Make sure that your security groups allow outbound traffic.
- Make sure that your IPv4 CIDR block is **not** configured to the `172.16.0.0/12` IP address range. For more information, see
  [IPv4 VPC CIDR blocks](../../../vpc/latest/userguide/vpc-cidr-blocks.md#vpc-sizing-ipv4 "../../../vpc/latest/userguide/vpc-cidr-blocks.md#vpc-sizing-ipv4") in the _Amazon VPC User Guide_.
- As a best practice, make sure that your security groups have no inbound traffic allowed, unless you specifically require this for other reasons.
- CodeCatalyst does not support assigning a public IP address to the network interfaces that it creates. One way to do this, is to add a NAT device to use CodeCatalyst with your VPC. For more information, see
  [Connect to the internet or other networks using NAT devices](../../../vpc/latest/userguide/vpc-nat.md "../../../vpc/latest/userguide/vpc-nat.md") in the _Amazon VPC User Guide_.

## Troubleshooting your VPC setup

Use the information that appears in the error message to help you identify, diagnose,
and address issues.

The following are some guidelines to assist you when troubleshooting common VPC errors:

1. [Make sure that your internet gateway is attached to VPC](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Attach_Gateway").
2. [Make sure that the route table for your public subnet points to the
   internet gateway](../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-internet-gateway "../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-internet-gateway").
3. [Make
   sure that your network ACLs allow traffic to flow](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules").
4. [Make
   sure that your security groups allow traffic to flow](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules").
5. [Troubleshoot your NAT gateway](../../../vpc/latest/userguide/VPC-nat-gateway.md#nat-gateway-troubleshooting "../../../vpc/latest/userguide/VPC-nat-gateway.md#nat-gateway-troubleshooting").
6. [Make sure
   that the route table for private subnets points to the NAT
   gateway](../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-nat "../../../vpc/latest/userguide/VPC_Route_Tables.md#route-tables-nat").
7. [Make sure that your
   IPv4 CIDR block is not configured to the `172.16.0.0/12`
   IP address range](../userguide/devenvironments-troubleshooting.md#troubleshooting-devenvironments-vpc "../userguide/devenvironments-troubleshooting.md#troubleshooting-devenvironments-vpc").
