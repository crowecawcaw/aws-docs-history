

# NAT64
<a name="ipv6-nat64"></a>

Publication date: **June 23, 2022 ([Diagram history](#ipv6-10-diagram-history))**

This architecture shows how NAT64 enables communication between IPv6-only resources and IPv4-only endpoints. NAT64 is automatically available on your existing NAT gateways or on any new NAT gateways you create.

## NAT64 architecture
<a name="ipv6-10-diagram1"></a>

![Architecture diagram showing nat64.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ipv6-vpc-architectures/images/ipv6-vpc-architectures-10.png)


The following numbered items describe the key components in this architecture:

1. NAT64 is automatically available on your existing NAT gateways or on any new NAT gateways you create. It is not a feature you enable or disable.

1. You need to route traffic for the well-known **64:ff9b::/96** prefix through the NAT gateway, which performs the necessary translation on the traffic to allow IPv6 services to access IPv4 services outside that subnet.

1. The IPv6 packet from the IPv6-only instance is sent to the NAT64 gateway. The source IP is the instance IPv6 address, and the destination IP is the DNS64 synthesized IPv6 address returned by the [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) Resolver.

1. From the **64:ff9b::/96** prefix, the NAT gateway recognizes that the original destination is IPv4 and translates the IPv6 packets to IPv4 by replacing the source IPv6 with its own private IPv4 address, and the destination IPv6 to IPv4 by truncating the **64:ff9b::/96** prefix.

1. Traffic can go to IPv4-only resources in the same [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

1. Traffic can go to IPv4-only endpoints on the internet, if the NAT gateway is public and has an elastic IP associated.

1. Traffic can go to IPv4-only resources in the private network, over VPN, [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html), Amazon VPC peering, or Transit Gateway.

## Further reading
<a name="ipv6-10-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ipv6-10-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](ipv6-dual-stack-internet.md#ipv6-1-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-only-subnets.md#ipv6-2-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-only-internet.md#ipv6-3-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-alb-ipv4-targets.md#ipv6-4-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-alb-ipv6-targets.md#ipv6-5-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-nlb-ipv4-targets.md#ipv6-6-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-nlb-ipv6-targets.md#ipv6-7-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-internal-elb.md#ipv6-8-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-dns64.md#ipv6-9-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](#ipv6-10-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-centralized-egress-nat64.md#ipv6-11-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-vpc-peering.md#ipv6-12-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-transit-gateway.md#ipv6-13-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-privatelink.md#ipv6-14-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-direct-connect.md#ipv6-15-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-vpn-tgw.md#ipv6-16-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-tgw-connect.md#ipv6-17-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.