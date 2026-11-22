

# Direct Connect gateway attachments in AWS Cloud WAN

AWS Cloud WAN now supports native integration with Direct Connect, simplifying connectivity between your on-premises networks and the AWS cloud. The new capability enables you to directly attach your Direct Connect gateways to Cloud WAN without the need for an intermediate AWS Transit Gateway, allowing seamless connectivity between your data centers or offices with Amazon Virtual Private Cloud (VPCs) across AWS Regions globally.

Cloud WAN allows you to build, monitor, and manage a unified global network that interconnects your resources in the AWS cloud and your on-premises environments. Direct Connect allows you to create a dedicated network connection to AWS bypassing the public Internet and provides improved application performance, greater privacy and security. Previously, you needed to deploy an intermediate transit gateway to interconnect your Direct Connect-based networks with Cloud WAN. Now you can directly attach your Direct Connect gateway to a Cloud WAN core network, simplifying connectivity between your on-premises locations and VPCs. Cloud WAN Direct Connect gateway attachments add support for automatic route propagation between AWS and on-premises networks using BGP (Border Gateway Protocol). Direct Connect gateway attachments also support existing Cloud WAN features, such as central policy-based management, tag-based attachment automation and segmentation for advanced security. 

## Prerequisites
<a name="cloudwan-dxattach-prereqs"></a>

The following are required before you can create a Direct Connect gateway attachment in a core network:
+ You must have a Direct Connect account and a valid Direct Connect gateway. A specific Direct Connect gateway can't be used for any other gateway types as long as it remains associated with a core network. This includes virtual gateways, transit gateways, and private virtual interfaces.
+ Only one core network can be associated with a Direct Connect gateway.

 For more information about Direct Connect, see the [*AWS Direct Connect User Guide*](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html).

## Limitations
<a name="cloudwan-dxattach-limits"></a>

The following limits apply to Direct Connect gateway attachments in a core network:
+ You can't configure static routes pointing to a Direct Connect gateway attachment as the next hop in a core network policy. Routes must be dynamically advertised from the on-premises network to core network.
+ You can't configure a list of allowed prefixes to be advertised over the Direct Connect gateway attachment from Cloud WAN to an on-premises network.
+ The ASN of a Direct Connect gateway must be outside of the ASN range configured for the core network. For example, if you have an ASN range of 64512 - 65534 for the core network, the ASN of the Direct Connect gateway must use an ASN outside of that range.
+ Private IP VPN and Connect attachments are not supported when a Direct Connect gateway attachment is the transport type.

## Route propagation
<a name="cloudwan-dxattach-routes"></a>

A Direct Connect gateway attachments support BGP-based dynamic routing for both inbound and outbound directions. 

For inbound routes, 
+ Cloud WAN learns BGP routes advertised from your on-premises location via the Direct Connect gateway and the transit virtual interface. Routes are learnt in the segment route-tables of the associated core network edges for the attachment.
+ Routes learned in segment route table can be routed across all AWS Regions for that segment.
+ Cloud WAN follows the route evaluation order for the same prefixes learned over multiple attachments. See [Route evaluation](cloudwan-route-evaluation.md) for more information. 
+ Direct Connect gateway will advertise routes from all on-premises locations towards all segment route-tables of the associated core network edges for the attachment. 

For outbound routes,
+ Cloud WAN propagates routes from the segment route table to the Direct Connect gateway, which in turn advertises these routes over transit virtual interfaces to your on-premises locations via BGP.
+ Each core network edge associated with the Direct Connect gateway attachment advertises only its local routes towards the Direct Connect gateway.
+ The AS\_PATH BGP attribute is retained in these route advertisements to your on-premises locations. For more information about AS\_PATH and BGP, see [Private virtual interface and transit virtual interface routing policies](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html#private-routing-policies) in the *AWS Direct Connect User Guide*.

You can use Border Gateway Protocol (BGP) communities with Direct Connect gateway attachments for both inbound and outbound route propagation. You can match on, add, or remove BGP communities using Cloud WAN routing policies. Some restrictions apply to the BGP communities that are supported. For more information about these restrictions, see [Direct Connect gateway and AWS Cloud WAN core network associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-cloud-wan.html) in the *AWS Direct Connect User Guide*. For more information about routing policies, see [AWS Cloud WAN Routing policies](cloudwan-routing-policies.md).

## Segment isolation
<a name="cloudwan-dxattach-segment-isolation"></a>

A Direct Connect gateway routes traffic independently of your core network. Cloud WAN routing policies, segment isolation, and the isolated attachments setting only control routing within the core network. They don't control how traffic is handled if it reaches a Direct Connect gateway. If an on-premises network advertises a supernet that overlaps with your VPC CIDRs, traffic destined for one VPC follows the supernet route to the Direct Connect gateway. The gateway then hairpins it back to the target VPC. As a result, VPCs can reach each other across the isolation boundary. This applies whether the VPCs are in different segments, or in the same segment with isolated attachments enabled. For more information about Direct Connect gateways, see [Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html) in the *AWS Direct Connect User Guide*.

For example, suppose you advertise the supernet `10.0.0.0/8` from on-premises. It overlaps the CIDRs of VPCs in a prod segment (`10.1.0.0/16`) and a dev segment (`10.2.0.0/16`). Those VPCs can communicate through the Direct Connect gateway, even though Cloud WAN keeps the segments isolated.

To prevent this, advertise specific on-premises prefixes that don't overlap with your VPC CIDRs, rather than a broad supernet. This preserves Cloud WAN segmentation with no additional configuration, and it's the simplest, most reliable mitigation. If your organization can't avoid advertising an overlapping supernet, use one of the approaches in the following sections.

### Cross-segment communication
<a name="cloudwan-dxattach-segment-isolation-cross-segment"></a>

Use one of the following approaches:
+ **Separate Direct Connect gateway for each routing domain.** A Direct Connect gateway attachment can be associated with only a single segment. In many designs, that attachment uses one shared hybrid segment that reaches the workload segments (such as prod and dev) through segment sharing, or through inspection with a service insertion (`send-via`) action. Because that single gateway serves multiple workload segments, an overlapping supernet can hairpin traffic between them. To maintain end-to-end segmentation, create a separate Direct Connect gateway and attachment for each routing domain. Associate each gateway directly with its workload segment. You can also associate it with its own dedicated hybrid segment when that domain is shared with several similar workload segments. Each Direct Connect gateway is its own routing domain, so traffic from one segment can't hairpin into another. Consider the type of Direct Connect connection you use, because each gateway requires additional virtual interfaces (VIFs).
+ **Blackhole routes.** Use `create-route` segment actions to install blackhole routes for CIDRs that shouldn't be reachable from a segment. Make them more specific than, or equal in prefix length to, the supernet advertised over Direct Connect. For example, to stop the dev segment from reaching the prod VPC through the `10.0.0.0/8` supernet, add a blackhole route for `10.1.0.0/16` to the dev segment. Because `10.1.0.0/16` is more specific than `10.0.0.0/8`, Cloud WAN drops that traffic instead of forwarding it to the Direct Connect gateway. Add the equivalent blackhole route for `10.2.0.0/16` to the prod segment to block the reverse path. For more information, see [Segment routes](cloudwan-policy-network-actions-routes.md#cloudwan-policy-version-routes).

### Isolated attachment communication
<a name="cloudwan-dxattach-segment-isolation-isolated-attachments"></a>

A separate Direct Connect gateway doesn't help here, because all isolated attachments stay in the same segment. Use blackhole routes instead. For more information, see [Segment routes](cloudwan-policy-network-actions-routes.md#cloudwan-policy-version-routes).

## Pricing
<a name="cloudwan-dxattach-pricing"></a>

As with other Cloud WAN attachments, there is a per-hour charge and per-gigabyte charge for using Direct Connect gateway attachments in a Cloud WAN core network. For more details about pricing, see [AWS Cloud WAN Pricing](https://aws.amazon.com/cloud-wan/pricing/).

**Topics**
+ [Prerequisites](#cloudwan-dxattach-prereqs)
+ [Limitations](#cloudwan-dxattach-limits)
+ [Route propagation](#cloudwan-dxattach-routes)
+ [Segment isolation](#cloudwan-dxattach-segment-isolation)
+ [Pricing](#cloudwan-dxattach-pricing)
+ [Create a Direct Connect gateway attachment](cloudwan-dxattachment-add.md)
+ [View or edit a Direct Connect gateway attachment](cloudwan-dxattachment-update.md)