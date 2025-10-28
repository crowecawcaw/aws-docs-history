# Add a NAT Gateway to an Existing

VPC

If you have already configured a VPC, complete the following steps to add a
NAT gateway to your VPC. If you need to create a new VPC, see [Create and Configure a New VPC](create-configure-new-vpc-with-private-public-subnets-nat.md "create-configure-new-vpc-with-private-public-subnets-nat.md").

###### To add a NAT gateway to an existing VPC

1. To create your NAT gateway, complete the steps in
   [Creating a NAT Gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-creating") in the
   _Amazon VPC User Guide_.
2. Verify that your VPC has at least one private subnet. We recommend
   that you specify two private subnets from different Availability Zones
   for high availability and fault tolerance. For information about how to
   create a second private subnet, see [Step 3: Add a Second Private Subnet](create-configure-new-vpc-with-private-public-subnets-nat.md#vpc-with-private-and-public-subnets-add-private-subnet-nat "create-configure-new-vpc-with-private-public-subnets-nat.md#vpc-with-private-and-public-subnets-add-private-subnet-nat").
3. Update the route table associated with one or more of your private
   subnets to point internet-bound traffic to the NAT gateway. This enables
   the streaming instances in your private subnets to communicate with the
   internet. To do so, complete the steps in [Updating Your Route Table](../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-create-route "../../../vpc/latest/userguide/vpc-nat-gateway.md#nat-gateway-create-route") in the
   _Amazon VPC User Guide_.
   **Next Steps**

To enable your WorkSpaces in WorkSpaces Pools to access the internet, complete the steps
in [Enable Internet
Access for WorkSpaces Pools](managing-network-manual-enable-internet-access.md "managing-network-manual-enable-internet-access.md").
