# Create an AWS Cloud WAN Connect peer for a core

network

You can create a either a GRE Connect peer or a Tunnel-less Connect peer for an existing
Connect attachment using either the AWS Cloud WAN console or the command line/API.

###### Topics

- [Add a GRE Connect peer using the
  console](#cloudwan-connect-peer-console "#cloudwan-connect-peer-console")
- [Add a Tunnel-less Connect peer
  using the console](#cloudwan-connect-peer-tlc-attachment "#cloudwan-connect-peer-tlc-attachment")
- [Add a Connect peer using the command line or
  API](#cloudwan-connect-peer-cli "#cloudwan-connect-peer-cli")

## Add a GRE Connect peer using the

console

The following steps add a GRE Connect peer using the console.

###### To add a Connect peer using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. Under **Core network** in the navigation pane, choose **Attachments**.
5. Choose an attachment with a resource type of **Connect**.

The **Details** tab displays the **Connect
protocol**. Make sure to choose a Connect attachment where the
Connect protocol is **GRE**. 6. Choose the **Connect peers** tab. 7. Choose **Create Connect peer**. 8. Enter a **Name** to identify the Connect peer. 9. (Optional) For the **Core network GRE address**, enter the
GRE outer IP address for the core network edge. By default, the first available
address from the Inside CIDR block is used. 10. For the **Peer GRE address**, enter the GRE outer IP address for
the customer appliance. This is peer IP address (GRE outer IP address) on the
appliance side of the Connect peer.

This can be any IP address. The IP address can be an IPv4 or IPv6 address, but
it must be the same IP address family as the transit gateway address. 11. For **BGP Inside CIDR blocks IPv4**, enter the range of inside
IPv4 addresses used for BGP peering. Use a `/29` CIDR block from the
`169.254.0.0/16` range. 12. (Optional) For **BGP Inside CIDR blocks IPv6**, enter the range
of inside IPv6 addresses used for BGP peering. Use a `/125` CIDR block
from the `fd00::/8` range. 13. For **Peer ASN**, specify the Border Gateway Protocol (BGP)
Autonomous System Number (ASN) for the appliance. You can use an existing ASN
that's assigned to your network. If you do not have one, you can use any ASN in
the `1-4294967294` range.

The default is the same ASN as the core network edge. If you configure the
**Peer ASN** to be different than the core network edge ASN
(eBGP), you must configure ebgp-multihop with a time-to-live (TTL) value of
`2`. 14. (Optional) In the **Tags** section, add
**Key** and **Value** pairs to further
help identify this resource. You can add multiple tags by choosing **Add
tag**, or remove any tag by choosing **Remove
tag**. 15. Choose **Create Connect peer**.

## Add a Tunnel-less Connect peer

using the console

The following steps add a Tunnel-less Connect peer using the console.

###### To add a Tunnel-less Connect peer using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. Under **Core network** in the navigation pane, choose **Attachments**.
5. Choose an attachment with a resource type of **Connect**.

The **Details** tab displays the **Connect
protocol**. Make sure to choose a Connect attachment where the
Connect protocol is **NO_ENCAP**. 6. Choose the **Connect peers** tab. 7. Choose **Create Connect peer**. 8. Enter a **Name** to identify the Tunnel-less Connect
peer. 9. For the **Peer BGP address**, enter the appliance's
private IPv4 address.

###### Note

BGP peering primarily uses IPv4 addresses, but it does support IPv6
address exchange through MP-BGP. To establsih BGP sessions for IPv6 Unicast,
you must have IPv4 Unicast addressing. 10. For the **Peer ASN**, specify the BGP ASN for the
appliance.

You can use an existing ASN that's assigned to your network. If you do not
have one, you can use any ASN in the `1-4294967294` range. The
default is the same ASN as the core network edge. If you configure the
**Peer ASN** to be different from the core network edge
ASN (eBGP), you must configure ebgp-multihop with a time-to-live (TTL) value
of 2. 11. For **Subnet**, choose the subnet of the appliance.

###### Note

We recommend you run your appliance in the same subnet as your
transport VPC attachment. 12. (Optional) In the **Tags** section, add
**Key** and **Value** pairs to further
help identify this resource. You can add multiple tags by choosing **Add
tag**, or remove any tag by choosing **Remove
tag**. 13. Choose **Create Connect peer**.

## Add a Connect peer using the command line or

API

Use the command line or API to create an AWS Cloud WAN Connect peer.

###### To create a Connect peer using the command line or API

- Use `create-connect-peer`. See [create-connect-peer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-connect-peer.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-connect-peer.html").
