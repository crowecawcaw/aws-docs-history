# Configure a VPC for WorkSpaces Pools

When you set up WorkSpaces Pools, you must specify the virtual private cloud (VPC) and at
least one subnet in which to launch your WorkSpaces. A VPC is a virtual network in your own
logically isolated area within the Amazon Web Services Cloud. A subnet is a range of IP addresses
in your VPC.

When you configure your VPC for WorkSpaces Pools, you can specify either public or private
subnets, or a mix of both types of subnets. A public subnet has direct access to the
internet through an internet gateway. A private subnet, which doesn't have a route to an
internet gateway, requires a Network Address Translation (NAT) gateway or NAT instance
to provide access to the internet.

###### Contents

- [VPC Setup Recommendations for
  WorkSpaces Pools](vpc-setup-recommendations.md "vpc-setup-recommendations.md")
- [Configure a VPC with Private
  Subnets and a NAT Gateway](managing-network-internet-NAT-gateway.md "managing-network-internet-NAT-gateway.md")
- [Configure a New or
  Existing VPC with a Public Subnet](managing-network-default-internet-access.md "managing-network-default-internet-access.md")
- [Use the Default VPC, Public Subnet,
  and Security Group](default-vpc-with-public-subnet.md "default-vpc-with-public-subnet.md")
