

# Dual Stack VPN Connectivity with AWS Transit Gateway
<a name="ipv6-vpn-tgw"></a>

Publication date: **June 23, 2022 ([Diagram history](#ipv6-16-diagram-history))**

This architecture shows how to build hybrid dual stack VPN connectivity with AWS Transit Gateway. The outer IP addresses of the VPN connections are public IPv4 addresses, while inner tunnel addresses can be configured for either IPv4 or IPv6 traffic.

## Dual Stack VPN Connectivity with AWS Transit Gateway architecture
<a name="ipv6-16-diagram1"></a>

![Architecture diagram showing dual stack vpn connectivity with aws transit gateway.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ipv6-vpc-architectures/images/ipv6-vpc-architectures-16.png)


The following numbered items describe the key components in this architecture:

1. To configure dual stack support for VPN, create two transit gateway VPN attachments, one for each IP stack.

1. The outer IP addresses of the VPN connections are public IPv4 addresses.

1. One of the VPN tunnels is configured with inner IPv6 addresses, and routes IPv6 traffic. This enables you to maintain IPv6-only in on-premises environments, and configure IPv6-only connectivity with AWS environments, as long as you keep the outer VPN tunnel IPv4 public addresses.

1. The other VPN tunnel is configured with inner IPv4 addresses, and routes IPv4 traffic, when you require both IPv4 and IPv6 connectivity between your AWS environments and your on-premises workloads.

## Further reading
<a name="ipv6-16-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ipv6-16-diagram-history"></a>

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
| [Initial publication](ipv6-nat64.md#ipv6-10-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-centralized-egress-nat64.md#ipv6-11-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-vpc-peering.md#ipv6-12-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-transit-gateway.md#ipv6-13-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-privatelink.md#ipv6-14-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-direct-connect.md#ipv6-15-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](#ipv6-16-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-tgw-connect.md#ipv6-17-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.