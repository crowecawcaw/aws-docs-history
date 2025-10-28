# Gateway associations in AWS Global Networks for Transit Gateways

Create a customer gateway association with either a device or with a transit gateway Connect peer.

## Customer gateway associations

To add your on-premises network to your global network, you associate a customer
gateway with your device, and optionally, a link. The customer gateway must already be
in your global network as part of a VPN attachment in your transit gateway. If you
specify a link, it must already be associated with the specified device.

For more information about creating a customer gateway, see [Create a Customer
Gateway](../../../vpn/latest/s2svpn/SetUpVPNConnections.md#vpn-create-cgw "../../../vpn/latest/s2svpn/SetUpVPNConnections.md#vpn-create-cgw") in the _AWS Site-to-Site VPN User Guide_. For more information
about creating a VPN attachment to a transit gateway, see [Transit Gateway VPN Attachments](../../../vpc/latest/tgw/tgw-vpn-attachments.md "../../../vpc/latest/tgw/tgw-vpn-attachments.md")
in _Amazon VPC Transit Gateways_.

For more information about viewing
the topology of your on-premises network in Network Manager, see [Access transit gateway network dashboards using AWS Network Manager](nm-monitoring-console.md "nm-monitoring-console.md")
/>.

## Transit Gateway Connect peer associations

You can associate a [Connect peer](../../../vpc/latest/tgw/tgw-connect.md#tgw-connect-peer "../../../vpc/latest/tgw/tgw-connect.md#tgw-connect-peer") (in a transit gateway
Connect attachment) with a device, and optionally, with a link.

If you specify a link, it must be associated with the specified device.

###### Topics

- [Associate a customer gateway with a device](nm-cgw-associate.md "nm-cgw-associate.md")
- [Disassociate a customer gateway association from a device](nm-cgw-diasssociate.md "nm-cgw-diasssociate.md")
- [Add a Connect peer association](connect-peer-association.md "connect-peer-association.md")
- [Disassociate a Connect peer from a device](nm-cgw-connect-disassociate.md "nm-cgw-connect-disassociate.md")
