

# Routing behavior for 1:1 NAT in AWS Cloud WAN
<a name="cloudwan-nat-routing"></a>

The core network routes traffic to NAT'd attachments using the translated (NAT) addresses. A route to each NAT CIDR must exist in the attachment's segment route table, and in any segment that shares routes with it. Depending on the attachment type, Cloud WAN installs that route for you, or you provide it with a static route or a BGP advertisement.


| Attachment type | `NatSystemRouteSupport` | How the NAT CIDR becomes reachable | 
| --- | --- | --- | 
| VPC | Always enable; disable is rejected. | Cloud WAN replaces the VPC CIDR route with a route to the NAT CIDR. No action needed. | 
| Connect | Always disable; enable is rejected. | Your BGP peers must advertise the NAT CIDRs. | 
| Direct Connect gateway, Site-to-Site VPN (BGP) | enable (default) or disable | Cloud WAN installs the route, or you advertise the NAT CIDR from your BGP peers. | 
| Site-to-Site VPN (static routing) | Always disable; enable is rejected. | Add a static route for the NAT CIDR to your core network policy. | 

## Route type: system
<a name="cloudwan-nat-routing-system"></a>

Routes that Cloud WAN installs for NAT have the route type `SYSTEM` in `GetNetworkRoutes` and in the console. The other route types are static (routes you define in your core network policy) and propagated (routes learned from an attachment). The system type covers:
+ the route that replaces a VPC CIDR route with its NAT CIDR, and
+ the route Cloud WAN installs for a Direct Connect gateway or BGP Site-to-Site VPN attachment when route installation is enabled.

A NAT CIDR that you advertise from your own BGP peers appears as propagated. The route type shows who created the route, not whether NAT is involved. Route types may be added in the future, so make sure your applications handle values they don't recognize.

**Route priority:** For routes with the same prefix, a system route ranks below a static route and above propagated routes. A static route you define for a prefix still takes priority over a NAT route, so enabling NAT doesn't override routes you set manually. Longest-prefix match still applies first.

## Direct Connect gateway and BGP Site-to-Site VPN attachments
<a name="cloudwan-nat-routing-dx-vpn"></a>
+ **Route installation disabled** – Cloud WAN doesn't install NAT routes. Advertise the NAT CIDRs from your own BGP routers with the attributes you need, such as AS path, MED, or communities. Use this option to control path selection: per-peer longest-prefix routes, active/standby, or ECMP.
+ **Route installation enabled (default)** – Cloud WAN installs a system route for each rule's NAT CIDR, with an empty AS path. Traffic to the NAT CIDR is forwarded along the routes your network advertises that overlap the rule's original CIDR. If your network advertises nothing that overlaps the original CIDR, the NAT route drops traffic. Use this option if you can't or prefer not to change your on-premises router configuration.

For these attachment types, the original (pre-NAT) routes your network advertises aren't removed in either mode. Translation works the same in both modes; the setting controls only route installation.

## Advertising NAT CIDRs to your on-premises network
<a name="cloudwan-nat-routing-advertise"></a>

When a VPC's CIDR route is replaced by its NAT CIDR, Cloud WAN advertises the NAT CIDR, not the original VPC CIDR, to BGP-capable attachments (Site-to-Site VPN, Direct Connect gateway, Connect). Your on-premises routers see the NAT CIDR with the core network's ASN in the AS path. They no longer receive the original VPC CIDR.

## Brief traffic loss during changes
<a name="cloudwan-nat-routing-traffic-loss"></a>

When you enable NAT, change rules, or disable NAT, the address translation and the routes are updated separately. They can take effect at slightly different times. For a short period, traffic to the new NAT addresses can be dropped. The change completes on its own, and you don't need to take any action. To limit the impact, change NAT configuration during a maintenance window, and update the addresses that peers use only after the change is complete.