# VPN Setup

This section describes the basic steps for setting up a VPN to communicate between your AMS-managed VPC
and your internal network.

###### Note

To gain overall understanding about using a VPN with AWS services refer to
[What is AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")
and all about
[Your Customer Gateway](../../../vpc/latest/adminguide/Introduction.md "../../../vpc/latest/adminguide/Introduction.md")
(your VPN appliance).

Follow the AWS VPN User Guide
[Getting Started](../../../vpn/latest/s2svpn/SetUpVPNConnections.md "../../../vpn/latest/s2svpn/SetUpVPNConnections.md")
and
[Testing the Site-to-Site VPN Connection](../../../vpn/latest/s2svpn/HowToTestEndToEnd_Linux.md "../../../vpn/latest/s2svpn/HowToTestEndToEnd_Linux.md")
sections to complete the following steps.

- Step 1: In your AWS VPC, Create a Customer Gateway
- Step 2: In your AWS VPC, Create a Virtual Private Gateway
- Step 3: In your AWS VPC, Enable Route Propagation in Your Route Table
- Step 4: In your AWS VPC, Update Your Security Group to Enable Inbound SSH, RDP, and ICMP Access
- Step 5: In your internal Network, Create a VPN Connection and Configure the Customer Gateway
- Step 6: Test VPN connectivity between the VPC and your internal network
