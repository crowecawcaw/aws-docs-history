

# Hybrid DNS Resolution with Amazon Route 53 Resolver Endpoints (Dual-Stack)
<a name="hybrid-dns-dualstack"></a>

Publication date: **January 17, 2025 ([Diagram history](#hdnsd-diagram-history))**

This architecture shows how to resolve DNS queries bidirectionally between a corporate data center and an [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) using [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) Resolver inbound and outbound endpoints in a dual-stack configuration. Connectivity is provided through [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) or AWS Cloud WAN with [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) or AWS Site-to-Site VPN.

For more information about IPv6 and dual-stack architectures, see the [Dual Stack and IPv6-only Amazon VPC Reference Architectures](../ipv6-vpc-architectures/index.html) guide in this series.

For hybrid environments, see [IPv6 requirements for AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/ipv4-ipv6.html) and [AWS Direct Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html).

## Hybrid DNS resolution architecture (dual-stack)
<a name="hdnsd-diagram1"></a>

![Architecture diagram showing hybrid DNS resolution between a corporate data center and an AWS VPC using Amazon Route 53 Resolver endpoints in a dual-stack IPv4 and IPv6 configuration.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/hybrid-dns-route53/images/hybrid-dns-route53-2.png)


The following steps describe the data flow in this architecture:

1. An Amazon Elastic Compute Cloud (Amazon EC2) instance in a dual-stack subnet makes an AAAA DNS query for **app.corp.internal** and sends it to the Route 53 Resolver in the VPC.

1. A Route 53 forwarding rule is configured to forward any DNS query for **corp.internal** to the corporate data center. The DNS query is sent to the IPv6 addresses of the Route 53 Resolver outbound endpoint.

1. The Route 53 Resolver outbound endpoint forwards the query to the on-premises DNS resolver. As per VPC routing and AWS Transit Gateway or AWS Cloud WAN routing configuration, the query is sent to the corporate data center through the hybrid connection, using either AWS Direct Connect or AWS Site-to-Site VPN.

1. DNS resolution for **corp.internal** domain names is carried out by the DNS resolver located in the corporate data center.

1. A client located in the corporate data center makes an AAAA DNS query for **aws.example100.internal** and sends it to its on-premises DNS resolver. The DNS resolver has a conditional forwarder that forwards all DNS queries for **example100.internal** to the IPv6 addresses of the Route 53 Resolver inbound endpoint.

1. The forwarded query arrives at the Route 53 Resolver inbound endpoint through the hybrid connection and AWS Transit Gateway or AWS Cloud WAN. The inbound endpoint sends the query to the Route 53 Resolver within the VPC.

1. The private hosted zone associated with the VPC holds the DNS records for **aws.example100.internal**, so the Route 53 Resolver can resolve the query.

## Further reading
<a name="hdnsd-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="hdnsd-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](hybrid-dns-ipv4.md#hdns4-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 
| [Initial publication](#hdnsd-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 
| [Initial publication](hybrid-dns-ipv6.md#hdns6-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 
| [Initial publication](hybrid-dns-profiles.md#hdnsp-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.