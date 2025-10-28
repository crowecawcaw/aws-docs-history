# VPC peering connections

VPC peering enables you to connect two VPCs in the same or different AWS Regions. This enables instances in one VPC to communicate with instances in the other VPC as if they were all part of the same network.

VPC peering creates a direct network route between the two VPCs using private IPv4 addresses or IPv6 addresses. Traffic sent between the connected VPCs does not traverse the internet, a VPN connection, or an AWS Direct Connect connection. This makes VPC peering a secure way to share resources, such as databases or web servers, across VPC boundaries.

To establish a VPC peering connection, you create a peering connection request from one VPC and the owner of the other VPC accepts the request. After the connection is established, you can update your route tables to route traffic between the VPCs. This allows instances in one VPC to access resources in the other VPC.

VPC peering is an important tool for building multi-VPC architectures and sharing resources across organizational boundaries in AWS. It provides a simple, low-latency way to connect VPCs without the complexity of configuring a VPN or other networking service.

Use the following procedures to create and work with VPC peering connections.

###### Tasks

- [Create a VPC peering connection](create-vpc-peering-connection.md "create-vpc-peering-connection.md")
- [Accept or reject a VPC peering connection](accept-vpc-peering-connection.md "accept-vpc-peering-connection.md")
- [Update your route tables for a VPC peering connection](vpc-peering-routing.md "vpc-peering-routing.md")
- [Update your security groups to reference peer security groups](vpc-peering-security-groups.md "vpc-peering-security-groups.md")
- [Enable DNS resolution for a VPC peering connection](vpc-peering-dns.md "vpc-peering-dns.md")
- [Delete a VPC peering connection](delete-vpc-peering-connection.md "delete-vpc-peering-connection.md")
- [Troubleshoot a VPC peering connection](troubleshoot-vpc-peering-connections.md "troubleshoot-vpc-peering-connections.md")
