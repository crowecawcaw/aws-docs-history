# VPN setup

The basic steps that AMS follows for setting up a VPN to communicate between your AMS-managed VPC and
your internal network.

###### Note

To gain overall understanding about using a VPN with AWS services, see
[What is AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") and
[Your Customer Gateway](../../../vpc/latest/adminguide/Introduction.md "../../../vpc/latest/adminguide/Introduction.md") (your VPN appliance).

We follow the AWS VPN User Guide
[Getting Started](../../../vpn/latest/s2svpn/SetUpVPNConnections.md "../../../vpn/latest/s2svpn/SetUpVPNConnections.md") and
[Testing the Site-to-Site VPN
Connection](../../../vpn/latest/s2svpn/HowToTestEndToEnd_Linux.md "../../../vpn/latest/s2svpn/HowToTestEndToEnd_Linux.md") sections to complete the following steps:

1. In your AWS VPC, Create a Customer Gateway.
2. In your AWS VPC, Create a Virtual Private Gateway.
3. In your AWS VPC, Enable Route Propagation in Your Route Table.
4. In your AWS VPC, Update Your Security Group to Enable Inbound SSH, RDP, and ICMP Access.
5. In your internal Network, Create a VPN Connection and Configure the Customer Gateway.
6. Test VPN connectivity between the VPC and your internal network.
