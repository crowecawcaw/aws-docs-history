# Route tables and AWS Site-to-Site VPN route priority

[Route tables](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") determine where
network traffic from your VPC is directed. In your VPC route table, you must add a route
for your remote network and specify the virtual private gateway as the target. This
enables traffic from your VPC that's destined for your remote network to route via the
virtual private gateway and over one of the VPN tunnels. You can enable route
propagation for your route table to automatically propagate your network routes to the
table for you.

We use the most specific route in your route table that matches the traffic to
determine how to route the traffic (longest prefix match). If your route table has
overlapping or matching routes, the following rules apply:

- If propagated routes from a Site-to-Site VPN connection or AWS Direct Connect connection overlap
  with the local route for your VPC, the local route is most preferred even if the
  propagated routes are more specific.
- If propagated routes from a Site-to-Site VPN connection or AWS Direct Connect connection have the
  same destination CIDR block as other existing static routes (longest prefix
  match cannot be applied), we prioritize the static routes whose targets are an
  internet gateway, a virtual private gateway, a network interface, an instance
  ID, a VPC peering connection, a NAT gateway, a transit gateway, or a gateway VPC
  endpoint.
  For example, the following route table has a static route to an internet gateway, and
  a propagated route to a virtual private gateway. Both routes have a destination of
  `172.31.0.0/24`. In this case, all traffic destined for
  `172.31.0.0/24` is routed to the internet gateway — it is a static
  route and therefore takes priority over the propagated route.

| Destination   | Target                             |
| ------------- | ---------------------------------- |
| 10.0.0.0/16   | Local                              |
| 172.31.0.0/24 | vgw-11223344556677889 (propagated) |
| 172.31.0.0/24 | igw-12345678901234567 (static)     |

Only IP prefixes that are known to the virtual private gateway, whether through BGP
advertisements or a static route entry, can receive traffic from your VPC. The virtual
private gateway does not route any other traffic destined outside of received BGP
advertisements, static route entries, or its attached VPC CIDR. Virtual private gateways
do not support IPv6 traffic.

When a virtual private gateway receives routing information, it uses path selection to
determine how to route traffic. Longest prefix match applies, if all endpoints are
healthy. The health of a tunnel endpoint takes precedence over other routing attributes.
This precedence applies to VPNs on virtual private gateways and Transit Gateways. If the
prefixes are the same, then the virtual private gateway prioritizes routes as follows,
from most preferred to least preferred:

- BGP propagated routes from an AWS Direct Connect connection

Blackhole routes are not propagated to a Site-to-Site VPN customer gateway via BGP.

- Manually added static routes for a Site-to-Site VPN connection
- BGP propagated routes from a Site-to-Site VPN connection
- For matching prefixes where each Site-to-Site VPN connection uses BGP, the AS PATH is
  compared and the prefix with the shortest AS PATH is preferred.

###### Note

AWS strongly recommends using customer gateway devices that support
asymmetric routing.

For customer gateway devices that support asymmetric routing, we
_do not_ recommend using AS PATH prepending, to
ensure that both tunnels have equal AS PATH. This helps to ensure that the
multi-exit discriminator (MED) value that we set on a
tunnel during [VPN tunnel endpoint
updates](routing-vpn-tunnel-updates.md "routing-vpn-tunnel-updates.md") is used to determine tunnel priority.

For customer gateway devices that do not support asymmetric routing, you
can use AS PATH prepending and Local Preference to prefer one tunnel over
the other. However, when the egress path changes, this may cause traffic to
drop.

- When the AS PATHs are the same length and if the first AS in the AS_SEQUENCE
  is the same across multiple paths, multi-exit discriminators
  (MEDs) are compared. The path with the lowest MED value is preferred.
  Route priority is affected during [VPN
  tunnel endpoint updates](routing-vpn-tunnel-updates.md "routing-vpn-tunnel-updates.md").

On a Site-to-Site VPN connection, AWS selects one of the two redundant tunnels as the primary
egress path. This selection may change at times, and we strongly recommend that you
configure both tunnels for high availability, and allow asymmetric routing. The health
of a tunnel endpoint takes precedence over other routing attributes. This precedence
applies to VPNs on virtual private gateways and Transit Gateways.

For a virtual private gateway, one tunnel across all Site-to-Site VPN connections on the gateway
will be selected. To use more than one tunnel, we recommend exploring Equal Cost
Multipath (ECMP), which is supported for Site-to-Site VPN connections on a transit gateway. For
more information, see [Transit gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md") in
_Amazon VPC Transit Gateways_. ECMP is not supported for Site-to-Site VPN connections on
a virtual private gateway.

For Site-to-Site VPN connections that use BGP, the primary tunnel can be identified by the
multi-exit discriminator (MED) value. We recommend advertising more
specific BGP routes to influence routing decisions.

For Site-to-Site VPN connections that use static routing, the primary tunnel can be identified by
traffic statistics or metrics.
