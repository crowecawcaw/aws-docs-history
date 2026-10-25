

# How 1:1 NAT works in AWS Cloud WAN
<a name="cloudwan-nat-how-it-works"></a>

## Prerequisites
<a name="cloudwan-nat-prerequisites"></a>

Before you configure 1:1 NAT, confirm the following:
+ You have an existing Cloud WAN core network. For more information, see [Quick start: Create an AWS Cloud WAN global network and core network](cloudwan-getting-started.md).
+ You're the core network owner.
+ You have at least one attachment of a supported type in a valid state. The attachment can be in the `AVAILABLE` state or a pending state; see [Attachment states](#cloudwan-nat-attachment-states).
+ You have the IAM permissions `networkmanager:UpdateAttachmentNatConfiguration` and `networkmanager:ListAttachmentNatConfigurations`.
+ You've chosen NAT CIDRs (Classless Inter-Domain Routing blocks) that:
  + are within RFC 1918 or CGNAT (RFC 6598, `100.64.0.0/10`) space,
  + have the same prefix length as the original CIDR they map,
  + don't overlap any original CIDR or NAT CIDR already configured on the same attachment, and
  + don't overlap any other address range in your network, including other attachments' NAT CIDRs, the CIDRs of attachments without NAT rules, and the CIDRs of the VPCs and on-premises networks that need to reach the NAT addresses.
+ Your core network policy allows the NAT CIDRs to propagate to the segments that need to reach them. Check segment sharing, segment actions, and any routing policies that filter prefixes.
+ For attachments where NAT routes aren't installed automatically, you've planned static routes to the NAT CIDRs in your core network policy, or your peers advertise them.
+ Your VPC route tables route the NAT CIDRs you need to reach to the core network.

**Note**  
Cloud WAN checks for overlap only between rules on the same attachment. It doesn't check other attachments or your connected networks.  
**Overlap within the core network** – If a NAT CIDR overlaps a range that's already routed in a segment, traffic to the overlapping addresses is routed by longest-prefix match and route priority, and might not reach the intended attachment.
**Overlap with a network that sends to the NAT CIDR** – A VPC delivers traffic to addresses inside its own CIDR locally, so that traffic never reaches the core network. For example, if VPC-A uses `10.0.0.0/16`, VPC-A can't reach VPC-B through a NAT CIDR of `10.0.5.0/24`, because those addresses are part of VPC-A's own range. The same applies to on-premises networks that route the overlapping range internally.

## Attachment states
<a name="cloudwan-nat-attachment-states"></a>

You can configure NAT on an attachment in the `AVAILABLE` state, or in one of these pending states:


| Attachment state | What happens when you update NAT configuration | 
| --- | --- | 
| PENDING\_TAG\_ACCEPTANCE | The NAT update is applied, and the attachment then returns to PENDING\_TAG\_ACCEPTANCE. | 
| PENDING\_ATTACHMENT\_ACCEPTANCE | The NAT update isn't applied until the attachment is accepted. Until then, NatGatewaySupport and every rule in NatGatewayRules show the state PENDING\_ATTACHMENT\_ACCEPTANCE. | 

## Example: single NAT
<a name="cloudwan-nat-example-single"></a>

A Site-to-Site VPN attachment from a branch office uses the CIDR `10.10.100.0/24`, which conflicts with a range already in use in your core network. You configure the following rule on the VPN attachment.


| Rule \# | matchSourceCidr | natCidr | 
| --- | --- | --- | 
| 100 | 10.10.100.0/24 | 100.64.1.0/24 | 

Traffic from `10.10.100.5` arrives on the VPN attachment. Cloud WAN applies source NAT (SNAT), rewrites the source to `100.64.1.5`, and routes the packet based on its destination. Resources in your core network see the branch at `100.64.1.5`. Responses are sent to `100.64.1.5` and match the route for `100.64.1.0/24` to the VPN attachment. Cloud WAN applies destination NAT (DNAT) and rewrites the destination back to `10.10.100.5` before delivering the packet to the VPN attachment.

## Example: Connecting VPCs with overlapping CIDRs
<a name="cloudwan-nat-example-overlapping"></a>

When two or more networks use overlapping CIDRs, translate **each** of them to its own unique NAT CIDR. Every network is then reachable at a distinct address range, whatever its real addressing. This is the recommended way to use 1:1 NAT for overlapping networks.

Translating only one side doesn't work when the CIDRs are identical. The network without a rule would send replies to an address inside its own CIDR, and its VPC route table delivers that traffic locally instead of sending it to the core network.

In this example, VPC-A and VPC-B both use `10.0.0.0/16`. Each VPC attachment gets a rule that maps it to a unique NAT CIDR. Both attachments are in the same segment, or in segments that share routes.


| Attachment | Original CIDR | NAT CIDR | 
| --- | --- | --- | 
| VPC-A | 10.0.0.0/16 | 10.1.0.0/16 | 
| VPC-B | 10.0.0.0/16 | 10.2.0.0/16 | 

**VPC-A to VPC-B:** VPC-A instance `10.0.0.5` sends to VPC-B's NAT address `10.2.0.1`.

1. The packet arrives on VPC-A: `src=10.0.0.5`, `dst=10.2.0.1`.

1. VPC-A's rule translates the source: src becomes `10.1.0.5`.

1. The route lookup for `10.2.0.1` matches the NAT route for `10.2.0.0/16`, with target VPC-B.

1. VPC-B's rule translates the destination: dst becomes `10.0.0.1`.

1. The packet is delivered to VPC-B: `src=10.1.0.5`, `dst=10.0.0.1`.

**VPC-B to VPC-A (reply):** VPC-B instance `10.0.0.1` replies to `10.1.0.5`.

1. VPC-B's rule translates the source: src becomes `10.2.0.1`.

1. The route lookup for `10.1.0.5` matches the NAT route for `10.1.0.0/16`, with target VPC-A.

1. VPC-A's rule translates the destination: dst becomes `10.0.0.5`.

1. The packet is delivered to VPC-A: `src=10.2.0.1`, `dst=10.0.0.5`.

Each instance uses its own real address and reaches the other VPC at that VPC's NAT address. All translation happens in the core network.

**Routing requirements**
+ NAT routes for VPC attachments are installed automatically in the attachment's segment. They replace the VPC CIDR's route when the rule's `MatchSourceCidr` exactly matches that CIDR.
+ The NAT routes must reach the other attachment's segment. If the VPCs are in different segments, check segment sharing and any routing policies that filter prefixes.
+ Each VPC's route tables must route the other VPC's NAT CIDR to the core network: `10.2.0.0/16` in VPC-A, and `10.1.0.0/16` in VPC-B.

**Note**  
Reserve a dedicated address block for NAT CIDRs, for example part of the CGNAT range (`100.64.0.0/10`), and give each overlapping network its own slice of it. NAT CIDRs must not be used anywhere else in your core network or connected networks. In this example, no other attachment, VPC, or on-premises network can use `10.1.0.0/16` or `10.2.0.0/16`.