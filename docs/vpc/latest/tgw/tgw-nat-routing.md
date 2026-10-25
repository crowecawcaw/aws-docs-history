

# Routing behavior for 1:1 NAT in AWS Transit Gateway
<a name="tgw-nat-routing"></a>

After translation, other networks reach an attachment with NAT rules through its NAT addresses. A route to each NAT CIDR must therefore exist in the transit gateway route tables that send traffic to the attachment.

## NAT system route support
<a name="tgw-nat-routing-system-route-support"></a>

`NatSystemRouteSupport` controls whether the transit gateway automatically installs routes for an attachment's NAT CIDRs, so other networks can reach the translated addresses. It doesn't affect translation, which is controlled by `NatGatewaySupport` and the attachment's NAT rules.

Whether you can change `NatSystemRouteSupport` depends on the attachment type:


| Attachment type | `NatSystemRouteSupport` | How the NAT CIDR becomes reachable | 
| --- | --- | --- | 
| VPC | Always enable; disable is rejected. | The transit gateway replaces the VPC CIDR's propagated route with a route to the NAT CIDR, when the rule exactly matches the VPC CIDR. | 
| Peering (static routing), Site-to-Site VPN (static routing) | Always disable; enable is rejected. | Add a static route for the NAT CIDR that targets the attachment. | 
| Connect, VPN Concentrator | Always disable; enable is rejected. | Your BGP peers must advertise the NAT CIDRs. | 
| Direct Connect gateway, Site-to-Site VPN (BGP) | enable (default) or disable | The transit gateway installs the route, or you advertise the NAT CIDR from your network. | 

NAT routes are installed only in route tables that the attachment propagates to. To reach a NAT CIDR from a route table the attachment doesn't propagate to, add a static route.

## Route type: system
<a name="tgw-nat-routing-system-routes"></a>

Routes that the transit gateway installs for NAT have the route type `system` in `SearchTransitGatewayRoutes` and `ExportTransitGatewayRoutes`. The other route types are `static` (routes you create) and `propagated` (routes learned from an attachment). `system` covers:
+ the route that replaces a VPC CIDR route with its NAT CIDR, and
+ the route the transit gateway installs for a Direct Connect gateway or BGP Site-to-Site VPN attachment when `NatSystemRouteSupport` is `enable`.

A NAT CIDR that you advertise from your own BGP peers appears as `propagated`. The route type shows who created the route, not whether NAT is involved.

**Route priority:** For routes with the same prefix, a `system` route ranks below a `static` route and above prefix list references and propagated routes. A static route you created for a prefix still takes priority over a NAT route for that prefix, so enabling NAT doesn't override routes you set manually. Longest-prefix match still applies first.

For more information, see [Route types](how-transit-gateways-work.md#tgw-route-types-overview).

## VPC attachments
<a name="tgw-nat-routing-vpc"></a>

When a rule's `MatchSourceCidr` exactly equals one of the VPC's CIDRs (primary or secondary), the transit gateway replaces the propagated route for that CIDR with a route to the rule's `NatCidr`. If `MatchSourceCidr` doesn't exactly match a VPC CIDR, for example a /24 inside a /16 VPC, the API accepts the rule and the rule still takes effect: traffic from the matching addresses is translated, and traffic to the rule's NAT addresses is translated back. However, no route is replaced. The propagated route for the VPC CIDR stays in place, and the transit gateway doesn't install a route for the rule's `NatCidr`. Until you add a static route for that `NatCidr` that targets the VPC attachment, traffic sent to the NAT addresses, including replies to translated traffic, isn't routed to the VPC attachment.

**Example:** VPC-A and VPC-B both use 10.0.0.0/16. VPC-C uses 172.16.0.0/16.

*Before NAT:* Because VPC-B overlaps VPC-A, which was attached first, VPC-B's CIDR isn't propagated, and VPC-B isn't reachable through the transit gateway.


| Prefix | Attachment | Route type | 
| --- | --- | --- | 
| 10.0.0.0/16 | tgw-attach-aaa (VPC-A) | propagated | 
| 172.16.0.0/16 | tgw-attach-ccc (VPC-C) | propagated | 

*After NAT* (VPC-A 10.0.0.0/16 mapped to 10.11.0.0/16, VPC-B 10.0.0.0/16 mapped to 10.12.0.0/16):


| Prefix | Attachment | Route type | 
| --- | --- | --- | 
| 10.11.0.0/16 | tgw-attach-aaa (VPC-A) | system | 
| 10.12.0.0/16 | tgw-attach-bbb (VPC-B) | system | 
| 172.16.0.0/16 | tgw-attach-ccc (VPC-C) | propagated | 

Each VPC now has a unique, reachable prefix. VPC-C has no NAT rules and is unchanged.

## Direct Connect gateway and BGP Site-to-Site VPN attachments
<a name="tgw-nat-routing-dx-vpn"></a>

For these attachments, `NatSystemRouteSupport` controls whether the transit gateway installs the NAT routes. The routes your network advertises aren't changed in either mode.
+ **`enable` (default):** The transit gateway installs a `system` route for each rule's `NatCidr`. The route is active while your network advertises a route that overlaps the rule's `MatchSourceCidr`, such as the same CIDR, a more specific route, or a summary route. Otherwise, the route's state is `blackhole` and traffic to the NAT CIDR is dropped. The original (pre-NAT) routes your network advertises aren't removed.
+ **`disable`:** No NAT routes are installed. Advertise the NAT CIDRs from your own BGP peers with the attributes you need, such as per-peer longest-prefix routes, AS-path prepending for active/standby, or identical attributes for ECMP.

**Example:** You configure a rule on a BGP Site-to-Site VPN attachment that translates 10.50.0.0/24 to 100.64.50.0/24, with `NatSystemRouteSupport` set to `disable`. The transit gateway does not install a route for 100.64.50.0/24. On your on-premises router, you add a network statement (or redistribute a static route) so your router advertises 100.64.50.0/24 over the VPN. Once advertised, the transit gateway learns 100.64.50.0/24 as a `propagated` route, and traffic to that CIDR is forwarded to the VPN attachment.

**Important**  
With `NatSystemRouteSupport` set to `disable`, your network no longer needs to advertise the original CIDR. If the original CIDR overlaps another attachment's CIDR, stop advertising it once you advertise the NAT CIDR, so the two routes don't compete for that prefix in the route table. Don't do this with `NatSystemRouteSupport` set to `enable`: the NAT route needs an advertised route that overlaps the original CIDR, and becomes a blackhole without one.

## Connect attachments and their transport
<a name="tgw-nat-routing-connect"></a>

You can configure NAT on a Connect attachment or on its transport attachment (VPC or Direct Connect gateway), but not on both. If NAT is already enabled on one of them, a request to enable NAT on the other is rejected with an `InvalidParameterValue` error. To move NAT from one to the other, disable it on the first attachment and wait for `NatGatewaySupport` to reach `disabled` before you enable it on the second.

## Brief traffic loss during changes
<a name="tgw-nat-routing-traffic-loss"></a>

When you enable NAT, change rules, or disable NAT, the address translation and the routes are updated separately and can take effect at slightly different times. For a short period, traffic to the new NAT addresses can be dropped. The change completes on its own, with no action needed. To limit the impact, change NAT configuration during a maintenance window, and update the addresses that peers use only after the change is complete.