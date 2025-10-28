# VPC subnet configuration for AWS Network Firewall

When you associate a firewall to your VPC, you must provide a subnet for each
Availability Zone where you want to place a firewall endpoint to filter traffic. A
common configuration is to have a firewall endpoint in each zone where you have
customer subnets that you want to protect, but you can also have a firewall endpoint
filter traffic from multiple zones.

Additionally, you can use VPC endpoint associations to define multiple endpoints in an
Availability Zone and to use the firewall for VPCs other than the one specified in the firewall.
For any subnet where you use a firewall, the VPC subnet management described here is the same.

###### Note

If you plan to use your firewall for multiple VPCs,
the additional VPCs can only have firewall endpoints defined in Availability Zones where the firewall
already has endpoints defined for the primary VPC.

When you create the firewall or define a VPC endpoint association, Network Firewall adds
a firewall endpoint to each of the subnets that you've specified.
Each firewall endpoint uses the firewall's associated firewall policy configuration to
filter traffic that you route through it.

To prepare a VPC for your Network Firewall firewall, in each Availability Zone where you want a firewall endpoint,
create the subnets that you will use for the endpoints. Each subnet must have at least one IP address available. Your can't change the IP address type after you create the subnet.

Network Firewall supports up to 100 Gbps of network traffic per firewall endpoint. If you require more traffic
bandwidth, you can define additional endpoints in VPC endpoint associations, or you can
split your resources into subnets and create a Network Firewall firewall in each subnet.

###### Note

Reserve these firewall subnets for the exclusive use of Network Firewall. A firewall
endpoint can't filter traffic coming into or going out of the subnet in which it
resides, so don't place other applications in the firewall endpoint subnets.

For information about managing subnets in your VPC, see
[VPCs and subnets](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md")
in the _Amazon Virtual Private Cloud User Guide_.

When you create your Network Firewall firewall, you must provide at least one zone and subnet
for the firewall configuration. You can add and remove subnets after you create a
firewall. You can manage VPC endpoint associations for any firewall that you've created or
that has been shared with you.
