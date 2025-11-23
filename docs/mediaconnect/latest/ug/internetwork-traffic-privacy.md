# Internetwork traffic privacy

To set up a private connection between your Amazon VPC and your corporate network, you can choose to set up either an IPsec VPN connection over the internet or a private physical connection using Direct Connect connection. Direct Connect enables you to
establish a private virtual interface from your on-premises network directly
to your Amazon VPC, providing you with a private, high-bandwidth network
connection between your network and your VPC. With multiple virtual
interfaces, you can establish private connectivity to multiple VPCs while
maintaining network isolation. For more information, see [What is AWS
Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md") and [What
is Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")

###### To route traffic directly between MediaConnect and your corporate network

via a virtual private cloud (VPC)

1. Set up a private connection between your Amazon VPC and your corporate network. You can choose between an IPsec VPN connection over the internet or a private
   physical connection using Direct Connect connection.
2. [Create a flow that uses a VPC
   source](flows-create-vpc-source.md "flows-create-vpc-source.md"). During this
   process, you add a VPC _interface_ to your
   flow to establish the initial connection between your VPC and your flow. You
   also specify that same VPC interface as the source for the new flow.

###### Note

If your flow already exists, you can update the flow to [add a VPC interface](vpc-interface-add.md "vpc-interface-add.md") and then
[add another source that uses that
VPC interface](source-adding-vpc.md "source-adding-vpc.md").
