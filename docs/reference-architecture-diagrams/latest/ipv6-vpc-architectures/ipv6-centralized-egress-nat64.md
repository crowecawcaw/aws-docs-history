

# Centralized Egress Traffic with NAT64
<a name="ipv6-centralized-egress-nat64"></a>

Publication date: **June 23, 2022 ([Diagram history](#ipv6-11-diagram-history))**

This architecture shows how to centralize egress traffic to IPv4-only endpoints on the internet by forwarding all traffic to the well-known **64:ff9b::/96** prefix from all your spoke VPCs to a central egress Amazon VPC with a public NAT gateway through AWS Transit Gateway.

## Centralized Egress Traffic with NAT64 architecture
<a name="ipv6-11-diagram1"></a>

![Architecture diagram showing centralized egress traffic with nat64.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ipv6-vpc-architectures/images/ipv6-vpc-architectures-11.png)


The following numbered items describe the key components in this architecture:

1. You need to enable DNS64 in all the subnets where you want your IPv6-only workloads to communicate with IPv4-only destinations. The [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) Resolver looks up the DNS record for the service queried. If there is no IPv6 address associated with the destination, it synthesizes one by prepending the well-known **64:ff9b::/96** prefix to the IPv4 address in the record.

1. You need to route traffic for the well-known **64:ff9b::/96** prefix through the NAT gateway located in the egress Amazon VPC. As per the spoke Amazon VPC A private subnet route table, all the traffic to the **64:ff9b::/96** prefix is routed first to the TGW ENI.

1. In the AWS Transit Gateway route table associated to the spoke Amazon VPC attachments, you need to add a static route sending all the traffic to the **64:ff9b::/96** prefix through the egress Amazon VPC attachment.

1. As per the egress Amazon VPC TGW subnet route table, all the traffic to the **64:ff9b::/96** prefix is routed to the NAT gateway.

1. The NAT gateway recognizes that the original destination is IPv4 and translates the IPv6 packets to IPv4 by replacing the source IPv6 with its own public EIP IPv4 address, and the destination IPv6 to IPv4 by truncating the **64:ff9b::/96** prefix.

## Further reading
<a name="ipv6-11-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ipv6-11-diagram-history"></a>

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
| [Initial publication](#ipv6-11-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-vpc-peering.md#ipv6-12-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-transit-gateway.md#ipv6-13-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-privatelink.md#ipv6-14-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-direct-connect.md#ipv6-15-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-vpn-tgw.md#ipv6-16-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-tgw-connect.md#ipv6-17-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.