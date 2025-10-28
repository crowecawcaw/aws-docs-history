# Configure a VPC with Private

Subnets and a NAT Gateway

If you plan to provide your WorkSpaces in WorkSpaces Pools with access to the internet, we
recommend that you configure a VPC with two private subnets for your WorkSpaces and a NAT
gateway in a public subnet. You can create and configure a new VPC to use with a NAT
gateway, or add a NAT gateway to an existing VPC. For additional VPC configuration
recommendations, see [VPC Setup Recommendations for
WorkSpaces Pools](vpc-setup-recommendations.md "vpc-setup-recommendations.md").

The NAT gateway lets the WorkSpaces in your private subnets connect to the internet or
other AWS services, but prevents the internet from initiating a connection with
those WorkSpaces. In addition, unlike configurations that use the **Default
Internet Access** option for enabling internet access for WorkSpaces, this
configuration is not limited to 100 WorkSpaces.

For information about using NAT Gateways and this configuration, see
[NAT Gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") and [VPC with Public and Private Subnets (NAT)](../../../vpc/latest/userguide/VPC_Scenario2.md "../../../vpc/latest/userguide/VPC_Scenario2.md") in the
_Amazon VPC User Guide_.

###### Contents

- [Create and Configure a New VPC](create-configure-new-vpc-with-private-public-subnets-nat.md "create-configure-new-vpc-with-private-public-subnets-nat.md")
- [Add a NAT Gateway to an Existing
  VPC](add-nat-gateway-existing-vpc.md "add-nat-gateway-existing-vpc.md")
- [Enable Internet
  Access for WorkSpaces Pools](managing-network-manual-enable-internet-access.md "managing-network-manual-enable-internet-access.md")
