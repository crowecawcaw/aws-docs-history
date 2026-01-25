# Network Load Balancers

A Network Load Balancer serves as the single point of contact for clients.
Clients send requests to the Network Load Balancer, and the Network Load Balancer sends them to targets,
such as EC2 instances, in one or more Availability Zones.

To configure your Network Load Balancer, you create [target groups](load-balancer-target-groups.md "load-balancer-target-groups.md"), and then register targets with your target groups. Your Network Load Balancer
is most effective if you ensure that each enabled Availability Zone has at least
one registered target. You also create [listeners](load-balancer-listeners.md "load-balancer-listeners.md") to check for connection requests from clients and route requests from
clients to the targets in your target groups.

Network Load Balancers support connections from clients over VPC peering, AWS managed VPN, Direct Connect,
and third-party VPN solutions.

###### Contents

- [Load balancer state](#load-balancer-state "#load-balancer-state")
- [IP address type](#ip-address-type "#ip-address-type")
- [Connection idle timeout](#connection-idle-timeout "#connection-idle-timeout")
- [Load balancer attributes](#load-balancer-attributes "#load-balancer-attributes")
- [Cross-zone load balancing](#cross-zone-load-balancing "#cross-zone-load-balancing")
- [DNS name](#dns-name "#dns-name")
- [Load balancer zonal health](#load-balancer-zonal-health "#load-balancer-zonal-health")
- [Create a load balancer](create-network-load-balancer.md "create-network-load-balancer.md")
- [Update Availability Zones](availability-zones.md "availability-zones.md")
- [Update the IP address
  type](load-balancer-ip-address-type.md "load-balancer-ip-address-type.md")
- [Edit load balancer attributes](edit-load-balancer-attributes.md "edit-load-balancer-attributes.md")
- [Update the security groups](load-balancer-security-groups.md "load-balancer-security-groups.md")
- [Tag a load balancer](load-balancer-tags.md "load-balancer-tags.md")
- [Delete a load balancer](load-balancer-delete.md "load-balancer-delete.md")
- [View the resource map](view-resource-map.md "view-resource-map.md")
- [CloudWatch logs](load-balancer-cloudwatch-logs.md "load-balancer-cloudwatch-logs.md")
- [Zonal shift](zonal-shift.md "zonal-shift.md")
- [LCU reservations](capacity-unit-reservation.md "capacity-unit-reservation.md")

## Load balancer state

A Network Load Balancer can be in one of the following states:

`provisioning`

The Network Load Balancer is being set up.

`active`

The Network Load Balancer is fully set up and ready to route traffic.

`failed`

The Network Load Balancer couldn't be set up.

## IP address type

You can set the types of IP addresses that clients can use with your Network Load Balancer.

Network Load Balancers support the following IP address types:

**`ipv4`**

Clients must connect using IPv4 addresses (for example, 192.0.2.1).

**`dualstack`**

Clients can connect to the Network Load Balancer using both IPv4 addresses (for example,
192.0.2.1) and IPv6 addresses (for example, 2001:0db8:85a3:0:0:8a2e:0370:7334).

###### Considerations

- The Network Load Balancer communicates with targets based on the IP address type of
  the target group.
- To support source IP preservation for UDP IPv6 listeners, ensure that
  **Enable prefix for IPv6 source NAT** is turned on.
- When you enable dualstack mode for the Network Load Balancer, Elastic Load Balancing provides an AAAA
  DNS record for the Network Load Balancer. Clients that communicate with the Network Load Balancer
  using IPv4 addresses resolve the A DNS record. Clients that communicate
  with the Network Load Balancer using IPv6 addresses resolve the AAAA DNS record.
- Access to your internal dualstack Network Load Balancer through the internet gateway
  is blocked to prevent unintended internet access. However, this does not prevent
  other internet access (for example, through peering, Transit Gateway, AWS Direct Connect, or
  Site-to-Site VPN).

For more information, see [Update the IP address types for your Network Load Balancer](load-balancer-ip-address-type.md "load-balancer-ip-address-type.md").

## Connection idle timeout

For each TCP request that a client makes through a Network Load Balancer, the state of that connection
is tracked. If no data is sent through the connection by either the client or target for
longer than the idle timeout, the connection is no longer tracked. If a client or target
sends data after the idle timeout period elapses, the client receives a TCP RST packet to
indicate that the connection is no longer valid.

The default idle timeout value for TCP flows is 350 seconds, but can be updated to any
value between 60-6000 seconds. Clients or targets can use TCP keepalive packets to restart
the idle timeout. Keepalive packets sent to maintain TLS connections can't contain data or
payload.

The connection idle timeout for TLS listeners is 350 seconds and can't be modified.
When a TLS listener receives a TCP keepalive packet from either a client or a target,
the load balancer generates TCP keepalive packets and sends them to both the front-end
and back-end connections every 20 seconds. You can't modify this behavior.

While UDP is connectionless, the load balancer maintains UDP flow state based on the
source and destination IP addresses and ports. This ensures that packets that belong to
the same flow are consistently sent to the same target. After the idle timeout period
elapses, the load balancer considers the incoming UDP packet as a new flow and routes it
to a new target. Elastic Load Balancing sets the idle timeout value for UDP flows to 120 seconds. This
cannot be changed.

EC2 instances must respond to a new request within 30 seconds in order to establish a
return path.

For more information, see [Update idle timeout](update-idle-timeout.md "update-idle-timeout.md").

## Load balancer attributes

You can configure your Network Load Balancer by editing its attributes. For more
information, see [Edit load balancer attributes](edit-load-balancer-attributes.md "edit-load-balancer-attributes.md").

The following are the load balancer attributes for Network Load Balancers:

`access_logs.s3.enabled`

Indicates whether access logs stored in Amazon S3 are enabled. The default is
`false`.

`access_logs.s3.bucket`

The name of the Amazon S3 bucket for the access logs. This attribute is
required if access logs are enabled. For more information, see [Bucket requirements](enable-access-logs.md#access-logging-bucket-requirements "enable-access-logs.md#access-logging-bucket-requirements").

`access_logs.s3.prefix`

The prefix for the location in the Amazon S3 bucket.

`deletion_protection.enabled`

Indicates whether [deletion
protection](edit-load-balancer-attributes.md#deletion-protection "edit-load-balancer-attributes.md#deletion-protection") is enabled. The default is `false`.

`ipv6.deny_all_igw_traffic`

Blocks internet gateway (IGW) access to the Network Load Balancer, preventing
unintended access to your internal Network Load Balancer through an internet
gateway. It is set to `false` for internet-facing Network Load Balancers
and `true` for internal Network Load Balancers. This attribute does not
prevent non-IGW internet access (for example, through peering, Transit Gateway,
AWS Direct Connect, or Site-to-Site VPN).

`load_balancing.cross_zone.enabled`

Indicates whether [cross-zone
load balancing](#cross-zone-load-balancing "#cross-zone-load-balancing") is enabled. The default is
`false`.

`dns_record.client_routing_policy`

Indicates how traffic is distributed among the Network Load Balancers Availability
Zones. The possible values are `availability_zone_affinity` with
100 percent zonal affinity, `partial_availability_zone_affinity`
with 85 percent zonal affinity, and `any_availability_zone`
with 0 percent zonal affinity.

`secondary_ips.auto_assigned.per_subnet`

The number of [secondary IP
addresses](edit-load-balancer-attributes.md#secondary-ip-addresses "edit-load-balancer-attributes.md#secondary-ip-addresses") to configure. Use to resolve port allocation errors if
you can't add targets. The valid range is 0 to 7. The default is 0. After
you set this value, you can't decrease it.

`zonal_shift.config.enabled`

Indicates whether [zonal shift](zonal-shift.md "zonal-shift.md") is enabled.
The default is `false`.

## Cross-zone load balancing

By default, each Network Load Balancer node distributes traffic across the registered targets
in its Availability Zone only. If you turn on cross-zone load balancing, each Network Load Balancer node distributes traffic across the registered targets in all enabled
Availability Zones. You can also turn on cross-zone load balancing at the target group
level. For more information, see [Cross-zone load balancing for target groups](edit-target-group-attributes.md#target-group-cross-zone "edit-target-group-attributes.md#target-group-cross-zone")
and [Cross-zone load balancing](../userguide/how-elastic-load-balancing-works.md#cross-zone-load-balancing "../userguide/how-elastic-load-balancing-works.md#cross-zone-load-balancing") in the _Elastic Load Balancing User Guide_.

## DNS name

Each Network Load Balancer receives a default Domain Name System (DNS) name with the following syntax:
`name`-`id`.elb.`region`.amazonaws.com.
For example, my-load-balancer-1234567890abcdef.elb.us-east-2.amazonaws.com.

If you'd prefer to use a DNS name that is easier to remember, you can create a custom
domain name and associate it with the DNS name for your Network Load Balancer. When a client
makes a request using this custom domain name, the DNS server resolves it to the DNS
name for your Network Load Balancer.

First, register a domain name with an accredited domain name registrar. Next, use your
DNS service, such as your domain registrar, to create a DNS record to route requests
to your Network Load Balancer. For more information, see the documentation for your DNS service.
For example, if you use Amazon Route 53 as your DNS service, you create an alias record that
points to your Network Load Balancer. For more information, see [Routing traffic to an ELB load
balancer](../../../Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.md "../../../Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.md") in the _Amazon Route 53 Developer Guide_.

The Network Load Balancer has one IP address per enabled Availability Zone. These are the IP
addresses of the Network Load Balancer nodes. The DNS name of the Network Load Balancer resolves to
these addresses. For example, suppose that the custom domain name for your Network Load Balancer
is `example.networkloadbalancer.com`. Use the following
**dig** or **nslookup** command to determine the IP
addresses of the Network Load Balancer nodes.

**Linux or Mac**

```
`$` `dig +short `example.networkloadbalancer.com``
```

**Windows**

```
`C:\>` `nslookup `example.networkloadbalancer.com``
```

The Network Load Balancer has DNS records for its nodes. You can use DNS names
with the following syntax to determine the IP addresses of the Network Load Balancer nodes:
`az`.`name`-`id`.elb.`region`.amazonaws.com.

**Linux or Mac**

```
`$` `dig +short `us-east-2b.my-load-balancer-1234567890abcdef.elb.us-east-2.amazonaws.com``
```

**Windows**

```
`C:\>` `nslookup `us-east-2b.my-load-balancer-1234567890abcdef.elb.us-east-2.amazonaws.com``
```

## Load balancer zonal health

Network Load Balancers have zonal DNS records and IP addresses in Route 53 for each enabled
availability zone. When a Network Load Balancer fails a zonal health check for a particular
availability zone, its DNS record is removed from Route 53. Load balancer zonal
health is monitored using the Amazon CloudWatch metric `ZonalHealthStatus`, giving you
more insight into events that cause a fail-away to implement preventative measure
to ensure optimal application availability. For more information see,
[Network Load Balancer metrics](load-balancer-cloudwatch-metrics.md#load-balancer-metrics-nlb "load-balancer-cloudwatch-metrics.md#load-balancer-metrics-nlb").

Network Load Balancers can fail zonal health checks for multiple reasons, causing them to become
unhealthy. See below for common causes of unhealthy Network Load Balancers caused by failed zonal
health checks.

###### Check for the following possible causes:

- There are no healthy targets for the load balancer
- The number of healthy targets is less than the configured minimum
- There is a zonal shift or zonal auto-shift in progress
- Traffic is being automatically shifted to healthy zones due to detected issues
