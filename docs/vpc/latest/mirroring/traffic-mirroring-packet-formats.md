# Understanding traffic mirror packet format

Mirrored traffic is encapsulated with a VXLAN header. All appliances that receive traffic
directly with this feature should be able parse a VXLAN-encapsulated packet, as shown in the
following example:

![Traffic Mirroring packet.](images/traffic-mirroring-packets.png)
For more information about the VXLAN protocol, see [RFC 7348](https://tools.ietf.org/html/rfc7348 "https://tools.ietf.org/html/rfc7348").

The following fields apply to Traffic Mirroring:

- **VXLAN ID** — The virtual network ID that you can assign
  to a traffic mirror session. If you do not assign a value, we assign a random value that is
  unique to all sessions in the account.
- **Source IP address** — The primary IP address of the
  source network interface.
- **Source port** — The port is determined by a 5-tuple hash
  of the original L2 packet, for ICMP, TCP, and UDP flows. For other flows, the port is
  determined by a 3-tuple hash of the original L2 packet.
- **Destination IP address** — The primary IP address
  of the appliance, Gateway Load Balancer endpoint, or Network Load Balancer (when the appliance is deployed behind one).
- **Destination port** — The port is 4789, which is the well
  known port for VXLAN.
  Appliances that received mirrored traffic through a Gateway Load Balancer should be able to parse both outer
  GENEVE encapsulation (from Gateway Load Balancer) and an inner VXLAN encapsulation (from VPC Traffic Mirroring) to retrieve the
  original L3 packet. The following shows an example:

![Traffic Mirroring packets include Gateway Load Balancer](images/traffic-mirroring-gwlb-packets.png)
