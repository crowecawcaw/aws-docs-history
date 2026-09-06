

# IPv6-only Subnets in a Dual Stack Amazon Amazon VPC
<a name="ipv6-only-subnets"></a>

Publication date: **June 23, 2022 ([Diagram history](#ipv6-2-diagram-history))**

This architecture shows how to integrate IPv6-only subnets in your dual stack Amazon VPC. IPv6-only subnets can coexist with IPv4-only and dual stack subnets in the same Amazon VPC.

## IPv6-only subnets in a dual stack Amazon Amazon VPC architecture
<a name="ipv6-2-diagram1"></a>

![Architecture diagram showing IPv6-only subnets coexisting with IPv4-only and dual stack subnets in an Amazon VPC.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ipv6-vpc-architectures/images/ipv6-vpc-architectures-2.png)


The following numbered items describe the key components in this architecture:

1. To create IPv6-only subnets, you start with a dual stack Amazon Amazon VPC. The Amazon VPC needs to have a secondary IPv6 CIDR associated with it.

1. IPv6-only subnets only have an IPv6 CIDR associated with them, and do not need associated IPv4 CIDRs. IPv6-only subnets are bound to an Availability Zone the same as dual stack or IPv4-only subnets.

1. IPv6-only subnets can coexist in the same Amazon VPC as IPv4-only subnets and dual stack subnets. You can also choose to have dual stack VPCs with IPv6-only subnets, but keep in mind that the primary Amazon VPC CIDR is an IPv4 CIDR.

1. When you create an Amazon EC2 instance in the IPv6-only subnet, the IPv6 address is either automatically assigned from the subnet CIDR through DHCPv6, or you can manually configure it.

1. IPv6-only resources in IPv6-only subnets can communicate natively over IPv6 with other IPv6-only resources or dual stack resources in other subnets in the Amazon VPC.

1. IPv4-only resources in the IPv4-only subnets can communicate natively over IPv4 with other IPv4-only resources or dual stack resources in other subnets in the Amazon VPC.

**Note**  
IPv6-only resources in the IPv6-only subnets cannot communicate with IPv4-only resources in other subnets in the Amazon VPC.

## Further reading
<a name="ipv6-2-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ipv6-2-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](ipv6-dual-stack-internet.md#ipv6-1-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](#ipv6-2-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
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
| [Initial publication](ipv6-vpn-tgw.md#ipv6-16-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-tgw-connect.md#ipv6-17-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.