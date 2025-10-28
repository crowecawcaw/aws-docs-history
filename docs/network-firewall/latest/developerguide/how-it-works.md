# How AWS Network Firewall works

AWS Network Firewall is a stateful, managed, network firewall and intrusion detection and
prevention service for Amazon Virtual Private Cloud (Amazon VPC). You can combine Network Firewall with services and
components that you use with your VPC, for example an internet gateway, a NAT gateway, a
VPN, or a transit gateway. For information about managing your Amazon Virtual Private Cloud VPC, see the
[Amazon Virtual Private Cloud User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md"). You need a VPC to use Network Firewall.

The firewall protects the subnets within your VPC by filtering traffic going between the
subnets and locations outside of your VPC. The following example figure depicts the
placement of a firewall in a very simple architecture.

![An AWS Region has a VPC in a single Availability Zone with an internet gateway. A VPC spans the Region and contains a Network Firewall firewall subnet and a customer subnet. The firewall subnet is between the customer subnet and an internet gateway and is filtering traffic in both directions.](images/arch-igw-simple.png)
To enable the firewall's protection, you modify your Amazon VPC route tables to send your network
traffic through the Network Firewall firewall endpoints. For information about managing route tables for your VPC, see
[Route
tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon Virtual Private Cloud User
Guide_.
