# Direct Connect gateway attachments in AWS Cloud WAN

AWS Cloud WAN now supports native integration with Direct Connect, simplifying connectivity between
your on-premises networks and the AWS cloud. The new capability enables you to directly
attach your Direct Connect gateways to Cloud WAN without the need for an intermediate
AWS Transit Gateway, allowing seamless connectivity between your data centers or offices with
Amazon Virtual Private Cloud (VPCs) across AWS Regions globally.

Cloud WAN allows you to build, monitor, and manage a unified global network that
interconnects your resources in the AWS cloud and your on-premises environments. Direct Connect
allows you to create a dedicated network connection to AWS bypassing the public Internet
and provides improved application performance, greater privacy and security. Previously, you
needed to deploy an intermediate transit gateway to interconnect your Direct Connect-based networks
with Cloud WAN. Now you can directly attach your Direct Connect gateway to a Cloud WAN core
network, simplifying connectivity between your on-premises locations and VPCs. Cloud WAN
Direct Connect gateway attachments add support for automatic route propagation between AWS
and on-premises networks using BGP (Border Gateway Protocol). Direct Connect gateway
attachments also support existing Cloud WAN features, such as central policy-based
management, tag-based attachment automation and segmentation for advanced security.

## Prerequisites

The following are required before you can create a Direct Connect gateway attachment in
a core network:

- You must have a Direct Connect account and a valid Direct Connect gateway. A
  specific Direct Connect gateway can't be used for any other gateway types as long as
  it remains associated with a core network. This includes virtual gateways,
  transit gateways, and private virtual interfaces.
- Only one core network can be associated with a Direct Connect gateway.

For more information about Direct Connect, see the [_AWS Direct Connect
User Guide_](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md").

## Limitations

The following limits apply to Direct Connect gateway attachments in a core
network:

- You can't configure static routes pointing to a Direct Connect gateway attachment
  as the next hop in a core network policy. Routes must be dynamically advertised
  from the on-premises network to core network.
- Direct Connect Border Gateway Protocol (BGP) communities are not supported in a
  Cloud WAN network.
- You can't configure a list of allowed prefixes to be advertised over the
  Direct Connect gateway attachment from Cloud WAN to an on-premises network.
- The ASN of a Direct Connect gateway must be outside of the ASN range configured for
  the core network. For example, if you have an ASN range of 64512 - 65534 for
  the core network, the ASN of the Direct Connect gateway must use an ASN outside
  of that range.
- Private IP VPN and Connect attachments are not supported when a Direct Connect
  gateway attachment is the transport type.

## Route propagation

A Direct Connect gateway attachments support BGP-based dynamic routing for both inbound and
outbound directions.

For inbound routes,

- Cloud WAN learns BGP routes advertised from your on-premises location
  via the Direct Connect gateway and the transit virtual interface. Routes are learnt
  in the segment route-tables of the associated core network edges for the
  attachment.
- Routes learned in segment route table can be routed across all
  AWS Regions for that segment.
- Cloud WAN follows the route evaluation order for the same prefixes learned
  over multiple attachments. See [Route evaluation](cloudwan-create-attachment.md#cloudwan-route-evaluation "cloudwan-create-attachment.md#cloudwan-route-evaluation") for
  more information.

For outbound routes,

- Cloud WAN propagates routes from the segment route table to the Direct Connect
  gateway, which in turn advertises these routes over transit virtual interfaces
  to your on-premises locations via BGP.
- Each core network edge associated with the Direct Connect gateway attachment
  advertises only its local routes towards the Direct Connect gateway.
- The AS_PATH BGP attribute is retained in these route advertisements to your
  on-premises locations. For more information about AS_PATH and BGP, see [Private virtual interface and transit virtual interface routing
  policies](../../../directconnect/latest/UserGuide/routing-and-bgp.md#private-routing-policies "../../../directconnect/latest/UserGuide/routing-and-bgp.md#private-routing-policies") in the _AWS Direct Connect User
  Guide_.

## Pricing

As with other Cloud WAN attachments, there is a per-hour charge and per-gigabyte
charge for using Direct Connect gateway attachments in a Cloud WAN core network. For more
details about pricing, see [AWS Cloud WAN
Pricing](https://aws.amazon.com/cloud-wan/pricing/ "https://aws.amazon.com/cloud-wan/pricing/").

###### Topics

- [Create a Direct Connect gateway
  attachment](cloudwan-dxattachment-add.md "cloudwan-dxattachment-add.md")
- [View or edit a Direct Connect gateway
  attachment](cloudwan-dxattachment-update.md "cloudwan-dxattachment-update.md")
