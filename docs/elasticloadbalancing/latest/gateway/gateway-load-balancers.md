# Gateway Load Balancers

Use a Gateway Load Balancer to deploy and manage a fleet of virtual appliances that support the GENEVE
protocol.

A Gateway Load Balancer operates at the third layer of the Open Systems Interconnection (OSI) model. It
listens for all IP packets across all ports and forwards traffic to the target group that's
specified in the listener rule, using the GENEVE protocol on port 6081.

You can add or remove targets from your load balancer as your needs change, without
disrupting the overall flow of requests. ELB scales your load balancer as traffic to your
application changes over time. ELB can scale to the vast majority of workloads
automatically.

###### Contents

- [Load balancer state](#load-balancer-state "#load-balancer-state")
- [IP address type](#ip-address-type "#ip-address-type")
- [Availability Zones](#availability-zones "#availability-zones")
- [Idle timeout](#idle-timeout "#idle-timeout")
- [Load balancer attributes](#load-balancer-attributes "#load-balancer-attributes")
- [Network ACLs](#load-balancer-network-acl "#load-balancer-network-acl")
- [Asymmetric flows](#asymmetric-flows "#asymmetric-flows")
- [Network maximum transmission unit (MTU)](#mtu "#mtu")
- [Create a load balancer](create-load-balancer.md "create-load-balancer.md")
- [Update the IP address type](load-balancer-ip-address-type.md "load-balancer-ip-address-type.md")
- [Edit load balancer attributes](edit-load-balancer-attributes.md "edit-load-balancer-attributes.md")
- [Tag a load balancer](tag-load-balancer.md "tag-load-balancer.md")
- [Delete a load balancer](delete-load-balancer.md "delete-load-balancer.md")
- [LCU reservations](capacity-unit-reservation.md "capacity-unit-reservation.md")

## Load balancer state

A Gateway Load Balancer can be in one of the following states:

`provisioning`

The Gateway Load Balancer is being set up.

`active`

The Gateway Load Balancer is fully set up and ready to route traffic.

`failed`

The Gateway Load Balancer could not be set up.

## IP address type

You can set the types of IP addresses that the application servers can use to access
your Gateway Load Balancers.

Gateway Load Balancers support the following IP address types:

**`ipv4`**

Only IPv4 is supported.

**`dualstack`**

Both IPv4 and IPv6 are supported.

###### Considerations

- The virtual private cloud (VPC) and subnets that you specify for the load
  balancer must have associated IPv6 CIDR blocks.
- The route tables for the subnets in the service consumer VPC must route
  IPv6 traffic, and the network ACLs for these subnets must allow IPv6 traffic.
- A Gateway Load Balancer encapsulates both IPv4 and IPv6 client traffic with an IPv4 GENEVE header
  and sends it to the appliance. The appliance encapsulates both IPv4 and IPv6 client
  traffic with an IPv4 GENEVE header and sends it back to the Gateway Load Balancer.

For more information about IP address types, see [Update the IP address types for your Gateway Load Balancer](load-balancer-ip-address-type.md "load-balancer-ip-address-type.md").

## Availability Zones

When you create a Gateway Load Balancer, you enable one or more Availability Zones, and specify the
subnet that corresponds to each zone. When you enable multiple Availability Zones, it
ensures that the load balancer can continue to route traffic even if an Availability
Zone becomes unavailable. The subnets that you specify must each have at least 8
available IP addresses. Subnets cannot be removed after the load balancer is
created. To remove a subnet, you must create a new load balancer.

## Idle timeout

For each TCP request made through a Gateway Load Balancer, the state of that
connection is tracked. If no data is sent through the connection
by either the client or target for longer than the idle timeout,
the connection is closed. After the idle timeout period elapses,
the load balancer considers the next TCP SYN as a new flow and
routes it to a new target. However, data packets sent after the
idle timeout period elapses are dropped.

The default idle timeout value for TCP flows is 350 seconds,
but can be updated to any value between 60-6000 seconds. Clients
or targets can use TCP keepalive packets to reset the idle timeout.

###### Stickiness limitation

Your Gateway Load Balancers idle timeout can only be updated when using
5-tuple stickiness. When using 3-tuple or 2-tuple stickness,
the default idle timeout value is used. For more information,
see [Flow stickiness](edit-target-group-attributes.md#flow-stickiness "edit-target-group-attributes.md#flow-stickiness")

While UDP is connectionless, the load balancer maintains UDP
flow state based on the source and destination IP addresses and
ports. This ensures that packets that belong to the same flow are
consistently sent to the same target. After the idle timeout period
elapses, the load balancer considers the incoming UDP packet as a new
flow and routes it to a new target. Elastic Load Balancing sets the
idle timeout value for UDP flows to 120 seconds. This cannot be
changed.

EC2 instances must respond to a new request within 30 seconds in
order to establish a return path.

For more information, see [Update idle timeout](update-idle-timeout.md "update-idle-timeout.md").

## Load balancer attributes

The following are the load balancer attributes for Gateway Load Balancers:

`deletion_protection.enabled`

Indicates whether deletion protection is enabled. The default is
`false`.

`load_balancing.cross_zone.enabled`

Indicates whether cross-zone load balancing is enabled. The default
is `false`.

For more information, see [Edit load balancer attributes](edit-load-balancer-attributes.md "edit-load-balancer-attributes.md").

## Network ACLs

If the application servers and the Gateway Load Balancer endpoint are in the same subnet,
the NACL rules are evaluated for traffic from the application servers
to the Gateway Load Balancer endpoint.

## Asymmetric flows

Gateway Load Balancers support asymmetric flows when the load balancer processes the initial flow
packet and the response flow packet is not routed through the load balancer. Asymmetric
routing is not recommended, because it can result in reduced network performance. Gateway Load Balancers
do not support asymmetric flows when the load balancer does not process the initial flow
packet but the response flow packet is routed through the load balancer.

## Network maximum transmission unit (MTU)

The maximum transmission unit (MTU) is the size of the largest data packet that can be
transmitted through the network. The Gateway Load Balancer interface MTU supports packets up to 8,500
bytes. Packets with a size larger than 8500 bytes that arrive at the Gateway Load Balancer interface are
dropped.

A Gateway Load Balancer encapsulates IP traffic with a GENEVE header and forwards it to the appliance.
The GENEVE encapsulation process adds 68 bytes to the original packet. Therefore, to
support packets up to 8,500 bytes, ensure that the MTU setting of your appliance
supports packets of at least 8,568 bytes.

Gateway Load Balancers do not support IP fragmentation. Additionally, Gateway Load Balancers do not generate
ICMP message "Destination Unreachable: fragmentation needed and DF set".
Due to this, Path MTU Discovery (PMTUD) is not supported.
