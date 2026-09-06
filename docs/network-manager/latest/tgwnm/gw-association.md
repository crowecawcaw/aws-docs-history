

# Gateway associations in AWS Global Networks for Transit Gateways
<a name="gw-association"></a>

Create a customer gateway association with either a device or with a transit gateway Connect peer.

## Customer gateway associations
<a name="cgw-associations"></a>

To add your on-premises network to your global network, you associate a customer gateway with your device, and optionally, a link. The customer gateway must already be in your global network as part of a VPN attachment in your transit gateway. If you specify a link, it must already be associated with the specified device.

For more information about creating a customer gateway, see [Create a Customer Gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-cgw) in the *AWS Site-to-Site VPN User Guide*. For more information about creating a VPN attachment to a transit gateway, see [Transit Gateway VPN Attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html) in *Amazon VPC Transit Gateways*.

For more information about viewing the topology of your on-premises network in Network Manager, see [Access transit gateway network dashboards using AWS Network Manager](nm-monitoring-console.md) />.

## Transit Gateway Connect peer associations
<a name="tgw-associations"></a>

You can associate a [Connect peer](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html#tgw-connect-peer) (in a transit gateway Connect attachment) with a device, and optionally, with a link.

 If you specify a link, it must be associated with the specified device.

**Topics**
+ [Customer gateway associations](#cgw-associations)
+ [Transit Gateway Connect peer associations](#tgw-associations)
+ [Associate a customer gateway with a device](nm-cgw-associate.md)
+ [Disassociate a customer gateway association from a device](nm-cgw-diasssociate.md)
+ [Add a Connect peer association](connect-peer-association.md)
+ [Disassociate a Connect peer from a device](nm-cgw-connect-disassociate.md)