# Route evaluation

Cloud WAN evaluates routes at each core network edge in the following order:

1. The most specific route for the destination
2. For routes with the same destination IP address, but different targets, the
   following route priority is used:

   1. Static routes
   2. VPC-propagated routes in the same Region.
   3. For dynamic routes received at the core network with an
      _unequal_ AS path length and/or MED BGP
      attributes, Cloud WAN evaluates them in the following order:

      1. AS path length
      2. MED

   4. For dynamic routes received at the core network with
      _equal_ AS path length and MED BGP attributes,
      Cloud WAN evaluates them in the following order:

      1. Direct Connect gateway-propagated routes.
      2. Cloud WAN Connect-propagated routes in the same
         Region.
      3. Site-to-Site VPN-propagated routes in the same
         Region.
      4. Routes propagated from other sources, such as transit gateway peering
         and core network edges in other remote Regions
         over the AWS global infrastructure. If identical routes are
         received from two or more sources, a single attachment will be
         chosen in a deterministically random manner (this occurs on a per
         segment/network function group basis so you could see different destinations
         for the same route across different segment/network function groups).
