# Subnets for your VPC

A _subnet_ is a range of IP addresses in your VPC.
You can create AWS resources, such as EC2 instances, in specific subnets.

###### Contents

- [Subnet basics](#subnet-basics "#subnet-basics")
- [Subnet security](#subnet-security "#subnet-security")
- [Create a subnet](create-subnets.md "create-subnets.md")
- [Add or remove an IPv6 CIDR block from your subnet](subnet-associate-ipv6-cidr.md "subnet-associate-ipv6-cidr.md")
- [Modify the IP addressing attributes of your subnet](subnet-public-ip.md "subnet-public-ip.md")
- [Subnet CIDR reservations](subnet-cidr-reservation.md "subnet-cidr-reservation.md")
- [Route tables](VPC_Route_Tables.md "VPC_Route_Tables.md")
- [Middlebox routing wizard](middlebox-routing-console.md "middlebox-routing-console.md")
- [Delete a subnet](subnet-deleting.md "subnet-deleting.md")

## Subnet basics

Each subnet must reside entirely within one Availability Zone and cannot span zones. By
launching AWS resources in separate Availability Zones, you can protect your applications
from the failure of a single Availability Zone.

###### Contents

- [Subnet IP address range](#subnet-ip-address-range "#subnet-ip-address-range")
- [Subnet types](#subnet-types "#subnet-types")
- [Subnet diagram](#subnet-diagram "#subnet-diagram")
- [Subnet routing](#subnet-routing "#subnet-routing")
- [Subnet settings](#subnet-settings "#subnet-settings")

### Subnet IP address range

When you create a subnet, you specify its IP addresses, depending on the configuration of
the VPC:

- IPv4 only – The subnet has an IPv4 CIDR block but does
  not have an IPv6 CIDR block. Resources in an IPv4-only subnet must communicate over IPv4.
- Dual stack – The subnet has both an IPv4 CIDR block and
  an IPv6 CIDR block. The VPC must have both an IPv4 CIDR block and an IPv6 CIDR
  block. Resources in a dual-stack subnet can communicate over IPv4 and IPv6.
- IPv6 only – The subnet has an IPv6 CIDR block but does
  not have an IPv4 CIDR block. The VPC must have an IPv6 CIDR block. Resources in an IPv6-only
  subnet must communicate over IPv6.

###### Note

Resources in IPv6-only subnets are assigned IPv4 link-local addresses from CIDR block
169.254.0.0/16. These addresses are used to communicate with services
that are available only in the VPC. For examples, see [Link-local addresses](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#link-local-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#link-local-addresses") in the _Amazon EC2 User Guide_.

For more information, see [IP addressing for your VPCs and subnets](vpc-ip-addressing.md "vpc-ip-addressing.md").

### Subnet types

The subnet type is determined by how you configure routing for your subnets. For
example:

- Public subnet – The subnet has a direct
  route to an [internet gateway](VPC_Internet_Gateway.md "VPC_Internet_Gateway.md").
  Resources in a public subnet can access the public internet.
- Private subnet – The subnet does not have a
  direct route to an internet gateway. Resources in a private subnet require a
  [NAT device](vpc-nat.md "vpc-nat.md") to access the public
  internet.
- VPN-only subnet – The subnet has a route to a
  [Site-to-Site VPN connection](../../../vpn/latest/s2svpn.md "../../../vpn/latest/s2svpn.md") through a virtual private
  gateway. The subnet does not have a route to an internet gateway.
- Isolated subnet – The subnet has no
  routes to destinations outside its VPC. Resources in an isolated subnet can
  only access or be accessed by other resources in the same VPC.
- EVS subnet – This type of subnet is created using Amazon EVS. For more information, see [VLAN subnet](../../../evs/latest/userguide/concepts.md#concepts-evs-network "../../../evs/latest/userguide/concepts.md#concepts-evs-network") in the _Amazon EVS User Guide_.

### Subnet diagram

The following diagram shows a VPC with subnets in two Availability Zones and an
internet gateway. Each Availability Zone has a public subnet and a private subnet.

![A VPC with subnets in two Availability Zones.](images/subnet-diagram.png)

For diagrams that show subnets in Local Zones and Wavelength Zones, see [How AWS Local Zones work](../../../local-zones/latest/ug/how-local-zones-work.md "../../../local-zones/latest/ug/how-local-zones-work.md") and
[How AWS Wavelength works](../../../wavelength/latest/developerguide/how-wavelengths-work.md "../../../wavelength/latest/developerguide/how-wavelengths-work.md").

### Subnet routing

Each subnet must be associated with a route table, which specifies the allowed routes
for outbound traffic leaving the subnet. Every subnet that you create is automatically
associated with the main route table for the VPC. You can change the association, and you can
change the contents of the main route table. For more information, see [Configure route tables](VPC_Route_Tables.md "VPC_Route_Tables.md").

### Subnet settings

All subnets have a modifiable attribute that determines whether a network interface
created in that subnet is assigned a public IPv4 address and, if applicable, an IPv6 address.
This includes the primary network interface (for example, eth0) that's created for an instance when you
launch an instance in that subnet. Regardless of the subnet attribute, you can still override
this setting for a specific instance during launch.

After you create a subnet, you can modify the following settings for the subnet:

- Auto-assign IP settings: Enables you to configure the
  auto-assign IP settings to automatically request a public IPv4 or IPv6
  address for a new network interface in this subnet.
- Resource-based Name (RBN) settings: Enables you to specify
  the hostname type for EC2 instances in this subnet and configure how DNS A
  and AAAA record queries are handled. For more information, see
  [Amazon EC2 instance hostname types](../../../AWSEC2/latest/UserGuide/ec2-instance-naming.md "../../../AWSEC2/latest/UserGuide/ec2-instance-naming.md")
  in the _Amazon EC2 User Guide_.

## Subnet security

To protect your AWS resources, we recommend that you use private subnets.
Use a bastion host or NAT device to provide internet access to resources,
such as EC2 instances, in a private subnet.

AWS provides features that you can use to increase security for the resources in your VPC.
_Security groups_ allow inbound and outbound traffic for associated resources, such as EC2 instances.
_Network ACLs_ allow or deny inbound and outbound traffic at the subnet level.
In most cases, security groups can meet your needs. However, you can use network ACLs if you want an additional layer of security.
For more information, see [Compare security groups and network ACLs](infrastructure-security.md#VPC_Security_Comparison "infrastructure-security.md#VPC_Security_Comparison").

By design, each subnet must be associated with a network ACL. Every subnet that you
create is automatically associated with the default network ACL for the VPC. The default
network ACL allows all inbound and outbound traffic. You can update the default network
ACL, or create custom network ACLs and associate them with your subnets. For more
information, see [Control subnet traffic with network access control lists](vpc-network-acls.md "vpc-network-acls.md").

You can create a flow log on your VPC or subnet to capture the traffic that flows to and
from the network interfaces in your VPC or subnet. You can also create a flow log on an
individual network interface. For more information, see [Logging IP traffic using VPC Flow Logs](flow-logs.md "flow-logs.md").
