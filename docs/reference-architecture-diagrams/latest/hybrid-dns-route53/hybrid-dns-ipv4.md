

# Hybrid DNS Resolution with Amazon Route 53 Resolver Endpoints (IPv4)
<a name="hybrid-dns-ipv4"></a>

Publication date: **January 17, 2025 ([Diagram history](#hdns4-diagram-history))**

This architecture shows how to resolve DNS queries bidirectionally between a corporate data center and an [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) using [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) Resolver inbound and outbound endpoints. Connectivity between environments is provided through [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) or AWS Site-to-Site VPN.

## Hybrid DNS resolution architecture (IPv4)
<a name="hdns4-diagram1"></a>

![Architecture diagram showing hybrid DNS resolution between a corporate data center and an AWS VPC using Amazon Route 53 Resolver inbound and outbound endpoints over IPv4.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/hybrid-dns-route53/images/hybrid-dns-route53-1.png)


The following steps describe the data flow in this architecture:

1. An Amazon Elastic Compute Cloud (Amazon EC2) instance needs to resolve the domain name **corp.internal**. The authoritative DNS for this domain is located at the corporate data center. The DNS query is sent to the Route 53 Resolver in the VPC.

1. A Route 53 forwarding rule is configured to forward any DNS query for **corp.internal** to the corporate data center.

1. The DNS query is sent to the Route 53 Resolver outbound endpoint.

1. The Route 53 Resolver outbound endpoint forwards the query to the on-premises DNS resolver over the private connection between AWS and the corporate data center, using either AWS Direct Connect or AWS Site-to-Site VPN.

1. DNS resolution for **corp.internal** domain names is carried out by the DNS resolver located in the corporate data center.

1. A client located in the corporate data center needs to resolve an **aws.example100.internal** domain name. It sends the query to its pre-configured DNS resolver.

1. The DNS resolver in the corporate data center has a forwarding rule that points any DNS query for **aws.example100.internal** to the Route 53 Resolver inbound endpoint.

1. The forwarded query arrives at the Route 53 Resolver inbound endpoint through either AWS Direct Connect or an AWS Site-to-Site VPN.

1. The Route 53 Resolver inbound endpoint sends the query to the Route 53 Resolver within the VPC.

1. The private hosted zone associated with the VPC holds the DNS records for **aws.example100.internal**, so the Route 53 Resolver can resolve the query.

## Further reading
<a name="hdns4-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="hdns4-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#hdns4-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 
| [Initial publication](hybrid-dns-dualstack.md#hdnsd-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 
| [Initial publication](hybrid-dns-ipv6.md#hdns6-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 
| [Initial publication](hybrid-dns-profiles.md#hdnsp-diagram-history) | Reference architecture diagram first published. | January 17, 2025 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.