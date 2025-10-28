# Amazon Quick Suite elastic network interface

The _Amazon Quick Suite elastic network interface_ is a logical
networking component in a VPC that represents a virtual network card. Quick Suite
creates at least two of these network interfaces to use with a VPC connection based off
of the subnets that are attached to it. Then you add the VPC connection to each Amazon Quick Sight
data source you create. The Quick Suite network interface alone doesn't give
Quick Suite direct access to your databases. The VPC connection works only for the
Amazon Quick Sight data sources that are configured to use it.

When you use the Amazon Quick Sight data source to query a database or other instance within your
VPC, all the network traffic from Amazon Quick Suite originates from this Amazon Quick Suite network
interface. Because the Amazon Quick Suite network interface exists inside your VPC, traffic
originating from it can reach destinations within your VPC by using their private IP
addresses. Each Amazon Quick Suite network interface gets its own private IP address that
comes from the subnet you configure. The private IP address is unique for each AWS
account, unlike the public IP range.
