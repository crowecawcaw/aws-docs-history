

# Dual Stack Peering Connectivity for the Amazon Amazon VPC
<a name="ipv6-vpc-peering"></a>

Publication date: **June 23, 2022 ([Diagram history](#ipv6-12-diagram-history))**

This architecture shows how to configure IPv4 and IPv6 Amazon VPC peering connectivity. [Amazon Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) peering natively supports routing for both IP stacks, and you can create both intra-Region and cross-Region Amazon VPC peering connections.

## Dual Stack Peering Connectivity for the Amazon Amazon VPC architecture
<a name="ipv6-12-diagram1"></a>

![Architecture diagram showing dual stack peering connectivity for the amazon .](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ipv6-vpc-architectures/images/ipv6-vpc-architectures-12.png)


The following numbered items describe the key components in this architecture:

1. Amazon Amazon VPC peering natively supports routing for both IP stacks, and you can create both intra-Region and cross-Region Amazon VPC peering connections.

1. Update the route tables of VPCs with both the IPv4 and IPv6 CIDR blocks of the peered VPCs, with the respective peering connection ID as a target.

1. With Amazon VPC peering, IPv4 and IPv6 CIDR blocks of peered VPCs cannot overlap.

## Further reading
<a name="ipv6-12-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ipv6-12-diagram-history"></a>

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
| [Initial publication](#ipv6-12-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-transit-gateway.md#ipv6-13-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-privatelink.md#ipv6-14-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-direct-connect.md#ipv6-15-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-vpn-tgw.md#ipv6-16-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-tgw-connect.md#ipv6-17-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.