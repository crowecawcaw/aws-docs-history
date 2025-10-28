# Enabling unrestricted internet browsing for Amazon WorkSpaces Secure Browser

(recommended)

Follow these steps to configure a VPC with a NAT gateway for unrestricted internet
browsing. This grants WorkSpaces Secure Browser access to sites on the public internet, and private sites
hosted in or with a connection to your VPC.

###### To configure a VPC with a NAT gateway for unrestricted internet browsing

If you want your WorkSpaces Secure Browser portal to have access to both public internet content and
private VPC content, follow these steps:

###### Note

If you already configured a VPC, complete the following steps to add a NAT gateway
to your VPC. If you need to create a new VPC, see [Creating a new VPC for Amazon WorkSpaces Secure Browser](create-vpc.md "create-vpc.md").

1. To create your NAT gateway, complete the steps in [Create a NAT
   gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating"). Make sure that this NAT gateway has public connectivity, and is in
   a public subnet in your VPC.
2. You must specify at least two private subnets from different Availability Zones.
   Assigning your subnets to different Availability Zones helps to ensure better
   availability and fault tolerance. For information about how to create a second private
   subnet, see [Adding a second private subnet](vpc-step3.md "vpc-step3.md").

###### Note

To make sure every streaming instance has internet access, do not attach a
public subnet to your WorkSpaces Secure Browser portal. 3. Update the route table associated with your private subnets to point
internet-bound traffic to the NAT gateway. This enables the streaming instances in
your private subnets to communicate with the internet. For information on how to
associate a route table with a private subnet, complete the steps in [Configure
route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md").
