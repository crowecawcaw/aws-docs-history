

# IPv4 Targets for Dual Stack Internet-facing Network Load Balancer
<a name="ipv6-nlb-ipv4-targets"></a>

Publication date: **June 23, 2022 ([Diagram history](#ipv6-6-diagram-history))**

This architecture shows how to enable IPv4 and IPv6 internet connectivity to your application using [NLBs](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html). The NLB and target group instances continue using IPv4 for communication while supporting dual stack clients.

## IPv4 Targets for Dual Stack Internet-facing Network Load Balancer architecture
<a name="ipv6-6-diagram1"></a>

![Architecture diagram showing ipv4 targets for dual stack internet-facing network load balancer.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ipv6-vpc-architectures/images/ipv6-vpc-architectures-6.png)


The following numbered items describe the key components in this architecture:

1. Configure your [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) NLB subnets for dual stack internet connectivity by adding the default routes for IPv4 and IPv6.

1. Deploy your dual stack internet-facing NLB, and select the dual stack NLB subnets in the Amazon VPC.

1. Your application stack remains unchanged with the dual stack added functionality for your application endpoints with NLB. The NLB and target group instances continue using IPv4 for communication.

1. The application clients query for the application name and receive the IPv4 or IPv6 address of the endpoint, based on their capabilities. For single stack customers, their stack determines the protocol to be used. For dual stack enabled clients, the operating system configuration determines the use of IPv4 or IPv6 for communication.

1. The clients open connections to the application endpoint, using either IPv4 or IPv6.

1. The NLB distributes traffic to the healthy targets in the target groups using IPv4 connections.

## Further reading
<a name="ipv6-6-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ipv6-6-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](ipv6-dual-stack-internet.md#ipv6-1-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-only-subnets.md#ipv6-2-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-only-internet.md#ipv6-3-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-alb-ipv4-targets.md#ipv6-4-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](ipv6-alb-ipv6-targets.md#ipv6-5-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
| [Initial publication](#ipv6-6-diagram-history) | Reference architecture diagram first published. | June 23, 2022 | 
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