

# Hybrid DNS Resolution with Amazon Route 53 Resolver Endpoints (IPv6)
<a name="hybrid-dns-ipv6"></a>

Publication date: **January 17, 2025 ([Diagram history](#hdns6-diagram-history))**

This architecture shows how to resolve DNS queries between a corporate data center and an [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) using [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) Resolver endpoints in an IPv6-only subnet configuration. DNS64 and a private NAT gateway (NAT64 enabled) allow the IPv6-only [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) (Amazon EC2) instance to communicate with IPv4 resources in the corporate data center.

## Hybrid DNS resolution architecture (IPv6)
<a name="hdns6-diagram1"></a>

![Architecture diagram showing hybrid DNS resolution between a corporate data center and an AWS VPC using Amazon Route 53 Resolver endpoints with IPv6-only subnets, DNS64, and NAT64.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/hybrid-dns-route53/images/hybrid-dns-route53-3.png)


The following steps describe the data flow in this architecture:

1. An Amazon EC2 instance in the IPv6-only subnet makes an AAAA DNS query for **app.corp.internal** and sends it to the Route 53 Resolver in the VPC.

1. A Route 53 forwarding rule is configured to forward any DNS query for **corp.internal** to the corporate data center. The DNS query is sent to the Route 53 Resolver outbound endpoint.

1. The Route 53 Resolver outbound endpoint forwards the query to the on-premises DNS resolver over the private connection between AWS and the corporate data center, using either [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) or AWS Site-to-Site VPN.

1. DNS resolution for **corp.internal** domain names is carried out by the DNS resolver located in the corporate data center.

1. Once the domain name has been resolved by the data center's DNS resolver, the Route 53 Resolver synthesizes an IPv6 address by prepending 64:ff9b::/96 to the IPv4 address (as DNS64 is enabled).

1. As per the VPC route table, the Amazon EC2 instance sends the traffic to the private NAT gateway (NAT64 enabled), and traffic gets routed to the data center's client through either AWS Direct Connect or AWS Site-to-Site VPN.

## Further reading
<a name="hdns6-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="hdns6-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](hybrid-dns-ipv4.md#hdns4-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 
| [Initial publication](hybrid-dns-dualstack.md#hdnsd-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 
| [Initial publication](#hdns6-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 
| [Initial publication](hybrid-dns-profiles.md#hdnsp-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.