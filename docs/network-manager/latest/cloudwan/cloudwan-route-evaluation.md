

# Route evaluation
<a name="cloudwan-route-evaluation"></a>

Cloud WAN evaluates routes at each core network edge in the following order:

1. The most specific route for the destination

1. For routes with the same destination IP address, but different targets, the following route priority is used:

   1. Static routes

   1. VPC-propagated routes in the same Region.

   1. For dynamic routes received at the core network with an *unequal* AS path length and/or MED BGP attributes, Cloud WAN evaluates them in the following order:

      1.  AS path length

      1.  MED

   1. For dynamic routes received at the core network with *equal* AS path length and MED BGP attributes, Cloud WAN evaluates them in the following order:

      1.  Direct Connect gateway-propagated routes.

      1. Cloud WAN Connect-propagated routes in the same Region.

      1.  Site-to-Site VPN-propagated routes in the same Region.

      1. Routes propagated from other sources, such as transit gateway peering and core network edges in other remote Regions over the AWS global infrastructure. If identical routes are received from two or more sources, a single attachment will be chosen in a deterministically random manner (this occurs on a per segment/network function group basis so you could see different destinations for the same route across different segment/network function groups). 