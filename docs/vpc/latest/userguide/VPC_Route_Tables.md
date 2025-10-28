# Configure route tables

A _route table_ serves as the traffic controller for your virtual private cloud (VPC).
Each route table contains a set of rules, called _routes_, that determine where network
traffic from your subnet or gateway is directed. When you create a VPC, we also create the main route
table for the VPC. You can create additional route tables for your VPC, so that you have more granular
control over the network paths for your VPC.

You can use route tables to specify which networks your VPC can communicate with, such as other VPCs
or on-premises networks. Each route specifies a destination (CIDR block or prefix list) and a target
(such as an internet gateway, NAT gateway, VPC peering connection, or VPN connection). Traffic is
routed to targets based on its destination IP address. Route tables enable you to create complex
networking architectures that include public subnets, private subnets, VPN-only subnets, and isolated
subnets.

###### Contents

- [Route table concepts](RouteTables.md "RouteTables.md")
- [Subnet route tables](subnet-route-tables.md "subnet-route-tables.md")
- [Gateway route tables](gateway-route-tables.md "gateway-route-tables.md")
- [Route priority](route-tables-priority.md "route-tables-priority.md")
- [Example routing options](route-table-options.md "route-table-options.md")
- [Create a route table and routes](create-vpc-route-table.md "create-vpc-route-table.md")
- [Manage subnet route tables](WorkWithRouteTables.md "WorkWithRouteTables.md")
- [Replace the main route table](Route_Replacing_Main_Table.md "Route_Replacing_Main_Table.md")
- [Associate a route table with a gateway](associate-route-table-gateway.md "associate-route-table-gateway.md")
- [Replace or restore the target for a local route](replace-local-route-target.md "replace-local-route-target.md")
- [Advanced routing](advanced-routing.md "advanced-routing.md")
- [Troubleshoot reachability issues](route-table-routes-troubleshoot.md "route-table-routes-troubleshoot.md")
