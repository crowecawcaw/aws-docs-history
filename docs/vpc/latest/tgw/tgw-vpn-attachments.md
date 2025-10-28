# AWS Site-to-Site VPN attachments in

AWS Transit Gateway

You can connect a Site-to-Site VPN attachment to a transit gateway in AWS Transit Gateway, allowing you to connect
your VPCs and on-premises networks. Both dynamic and static routes are supported, as well as
IPv4 and IPv6.

**Requirements**

- Attaching a VPN connection to your transit gateway requires that you specify the VPN
  customer gateway, which have specific device requirements. Before creating a Site-to-Site VPN
  attachment, review the customer gateway requirements to ensure that your gateway is
  set up correctly. For more information about these requirements, including example
  gateway configuration files, see

[Requirements for your Site-to-Site VPN customer gateway device](../../../vpn/latest/s2svpn/CGRequirements.md "../../../vpn/latest/s2svpn/CGRequirements.md") in the _AWS Site-to-Site VPN User
Guide_.

- For static VPNs, you'll also need to first add the static routes to the transit gateway
  route table. Static routes in a transit gateway route table that target a VPN
  attachment are not filtered by the Site-to-Site VPN as this might allow
  unintended outbound traffic flow when using a BGP-based VPN. For the steps to
  add a static route to a transit gateway route table, see [Create a static route](tgw-create-static-route.md "tgw-create-static-route.md").
  You can create, view, or delete a transit gateway Site-to-Site VPN attachment using either the Amazon VPC
  console or using the AWS CLI.

###### Tasks

- [Create a transit gateway attachment to a VPN](create-vpn-attachment.md "create-vpn-attachment.md")
- [View a VPN attachment](view-vpn-attachment.md "view-vpn-attachment.md")
- [Delete a VPN attachment](delete-vpn-attachment.md "delete-vpn-attachment.md")
