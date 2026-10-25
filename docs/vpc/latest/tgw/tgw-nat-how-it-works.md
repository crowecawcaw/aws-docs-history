

# How 1:1 NAT works in AWS Transit Gateway
<a name="tgw-nat-how-it-works"></a>

You apply NAT configuration at the attachment level. For each attachment, you define one or more rules. Each rule specifies a `MatchSourceCidr`, the source IP range of traffic arriving on that attachment, and a `NatCidr`, the range those source addresses are translated to.

When traffic arrives at the transit gateway on an attachment, the transit gateway checks whether the packet's source IP matches any `MatchSourceCidr` on that attachment. If it does, SNAT applies and the source IP is rewritten to the corresponding address in the `NatCidr`. The transit gateway then looks up a route for the packet's destination IP to find the destination attachment. At delivery, the transit gateway checks whether the destination IP falls in any `NatCidr` on the destination attachment. If it does, DNAT applies and the destination IP is rewritten back to the original address. Return traffic follows the same steps, with the source and destination attachments swapped.

## Prerequisites
<a name="tgw-nat-prerequisites"></a>

Before you configure 1:1 NAT, confirm the following:
+ You have an existing transit gateway, and you are the transit gateway owner. For a shared transit gateway, only the owner account can view or modify NAT configuration. For more information, see [Create a transit gateway in AWS Transit Gateway](create-tgw.md).
+ You have at least one attachment of a supported type. See [Supported attachment types](tgw-nat.md#tgw-nat-supported-attachments).
+ You have the IAM permissions `ec2:ModifyTransitGatewayAttachmentNatConfiguration` and `ec2:GetTransitGatewayAttachmentNatConfiguration`. `ec2:Describe*` grants do not include the `Get` action.
+ You have identified NAT CIDRs that:
  + are within RFC 1918 or CGNAT (RFC 6598, 100.64.0.0/10) ranges,
  + have the same prefix length as the original CIDR they map,
  + do not overlap any original CIDR or NAT CIDR already configured on the same attachment, and
  + don't overlap any other CIDR in your network: other attachments' NAT CIDRs, the CIDRs of attachments without NAT, and the CIDRs of the VPCs and on-premises networks that need to reach the NAT addresses.
**Note**  
The transit gateway checks for overlap only between rules on the same attachment. It doesn't check other attachments or your connected networks.  
**Overlap within the transit gateway:** If a NAT CIDR overlaps a range that's already routed in a transit gateway route table, traffic to the overlapping addresses is routed by longest-prefix match and route priority, and might not reach the intended attachment.
**Overlap with a network that sends to the NAT CIDR:** A VPC delivers traffic to addresses inside its own CIDR locally, so that traffic never reaches the transit gateway. For example, if VPC-A uses 10.0.0.0/16, VPC-A can't reach VPC-B through a NAT CIDR of 10.0.5.0/24, because those addresses are part of VPC-A's own range. The same applies to on-premises networks that route the overlapping range internally.
+ For attachments where NAT routes are not installed automatically (static VPN, static peering, Connect, and VPN Concentrator), you have planned static routes to the NAT CIDRs, or your peers advertise them.
+ Your VPC route tables route the NAT CIDRs you need to reach to the transit gateway.

## Example: Single NAT
<a name="tgw-nat-example-single"></a>

This example uses NAT on one attachment to control which addresses your AWS resources see for a branch office.
+ A branch office network, 10.10.100.0/24, connects to the transit gateway through a Site-to-Site VPN attachment.
+ An application runs in VPC-A, 172.16.0.0/16, which is attached to the same transit gateway. VPC-A has no NAT rules.
+ You want the application to see the branch at addresses from a dedicated range, 100.64.1.0/24, instead of the branch's internal addresses.

**Note**  
If the branch range overlaps a range already in use in your AWS environment, translate both networks, each to its own NAT CIDR. See [Example: Connecting VPCs with overlapping CIDRs](#tgw-nat-example-overlapping).

You configure the following rule on the VPN attachment.


| Rule \# | MatchSourceCidr | NatCidr | 
| --- | --- | --- | 
| 100 | 10.10.100.0/24 | 100.64.1.0/24 | 

The rule number identifies the rule on the attachment. It must be unique on the attachment and from 1 to 32766. Rule numbers don't set a priority: the CIDRs of the rules on an attachment can't overlap, so each address matches at most one rule.

**Branch to VPC-A:** Branch host 10.10.100.5 connects to the application at 172.16.0.10.

1. The packet arrives on the VPN attachment: src=10.10.100.5, dst=172.16.0.10.

1. The VPN attachment's rule translates the source: src becomes 100.64.1.5.

1. The route lookup for 172.16.0.10 matches the propagated route for 172.16.0.0/16, with target VPC-A.

1. VPC-A has no NAT rules, so the destination isn't changed. The packet is delivered to VPC-A: src=100.64.1.5, dst=172.16.0.10.

**VPC-A to branch (reply):** The application replies to 100.64.1.5.

1. VPC-A's route table sends 100.64.1.0/24 to the transit gateway. The packet arrives on the VPC attachment: src=172.16.0.10, dst=100.64.1.5.

1. The route lookup for 100.64.1.5 matches the route for 100.64.1.0/24, with target the VPN attachment.

1. The VPN attachment's rule translates the destination: dst becomes 10.10.100.5.

1. The packet is delivered to the branch: src=172.16.0.10, dst=10.10.100.5.

The application sees the branch only at 100.64.1.0/24.

**Routing requirements**
+ **Route to the NAT CIDR:**
  + **BGP VPN, `NatSystemRouteSupport` set to `enable` (default):** The transit gateway adds a route for 100.64.1.0/24 automatically. The route is active while the branch advertises a route that overlaps 10.10.100.0/24, such as 10.10.100.0/24 itself, a more specific route, or a summary route. Otherwise, the route's state is `blackhole` and traffic to 100.64.1.0/24 is dropped. The routes the branch advertises stay in the route table alongside the NAT route.
  + **BGP VPN, `NatSystemRouteSupport` set to `disable`:** Configure the branch router to advertise 100.64.1.0/24 instead of 10.10.100.0/24. Use this option to keep the branch's internal range out of the transit gateway route tables.
  + **Static VPN:** Add a static route for 100.64.1.0/24 that targets the VPN attachment.
+ **VPC-A route tables:** Route 100.64.1.0/24 to the transit gateway.
+ **VPC-A security groups and network ACLs:** Allow traffic from 100.64.1.0/24.

## Example: Connecting VPCs with overlapping CIDRs
<a name="tgw-nat-example-overlapping"></a>

When two or more networks use overlapping CIDRs, translate *each* of them to its own unique NAT CIDR. Every network is then reachable at a distinct address range, whatever its real addressing. This is the recommended way to use 1:1 NAT for overlapping networks.

Translating only one side doesn't work when the CIDRs are identical. The network without a rule would send replies to an address inside its own CIDR, and its VPC route table delivers that traffic locally instead of sending it to the transit gateway.

In this example, VPC-A and VPC-B both use 10.0.0.0/16. Each VPC attachment gets a rule that maps it to a unique NAT CIDR.


| Attachment | MatchSourceCidr | NatCidr | 
| --- | --- | --- | 
| VPC-A | 10.0.0.0/16 | 10.1.0.0/16 | 
| VPC-B | 10.0.0.0/16 | 10.2.0.0/16 | 

**VPC-A to VPC-B:** VPC-A instance 10.0.0.5 sends to VPC-B's NAT address 10.2.0.1.

1. The packet arrives on VPC-A: src=10.0.0.5, dst=10.2.0.1.

1. VPC-A's rule translates the source: src becomes 10.1.0.5.

1. The route lookup for 10.2.0.1 matches the NAT route for 10.2.0.0/16, with target VPC-B.

1. VPC-B's rule translates the destination: dst becomes 10.0.0.1.

1. The packet is delivered to VPC-B: src=10.1.0.5, dst=10.0.0.1.

**VPC-B to VPC-A (reply):** VPC-B instance 10.0.0.1 replies to 10.1.0.5.

1. VPC-B's rule translates the source: src becomes 10.2.0.1.

1. The route lookup for 10.1.0.5 matches the NAT route for 10.1.0.0/16, with target VPC-A.

1. VPC-A's rule translates the destination: dst becomes 10.0.0.5.

1. The packet is delivered to VPC-A: src=10.2.0.1, dst=10.0.0.5.

Each instance uses its own real address and reaches the other VPC at that VPC's NAT address. All translation happens at the transit gateway.

**Routing requirements**
+ NAT routes for VPC attachments are installed automatically. They replace the propagated route for the VPC CIDR when the rule's `MatchSourceCidr` exactly matches that CIDR.
+ Each VPC's route tables must route the other VPC's NAT CIDR to the transit gateway: 10.2.0.0/16 in VPC-A, and 10.1.0.0/16 in VPC-B.

**Note**  
Reserve a dedicated address block for NAT CIDRs, for example part of the CGNAT range (100.64.0.0/10), and give each overlapping network its own slice of it. NAT CIDRs must not be used anywhere else on the transit gateway or in your connected networks. In this example, no other attachment, VPC, or on-premises network can use 10.1.0.0/16 or 10.2.0.0/16.