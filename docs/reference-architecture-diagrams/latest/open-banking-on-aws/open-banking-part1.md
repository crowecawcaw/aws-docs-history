

# Open Banking on AWS: Networking and security
<a name="open-banking-part1"></a>

Publication date: **September 7, 2021 ([Diagram history](#ob-p1-history))**

With this architecture, you can connect on-premises core banking systems to AWS and expose Open Banking APIs securely. The solution uses [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) for connectivity, [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/) for network hub management, and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) for API management with [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) integration.

## Open Banking networking and security diagram
<a name="ob-p1-diagram"></a>

![Reference architecture diagram showing Open Banking networking and security by using AWS Direct Connect, AWS Transit Gateway, Amazon API Gateway, and AWS WAF.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/open-banking-on-aws/images/open-banking-part1.png)


The following steps describe the networking and security components for this architecture:

1. Send and receive all new and updated transactions between core banking systems and AWS by using streaming technologies such as Apache Kafka and message queue (MQ) mechanisms.

1. Connect the bank data center to AWS by using a combination of AWS Direct Connect and [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/). Use two diverse AWS Direct Connect connections for maximum resiliency.

1. Use AWS Transit Gateway as the central hub on AWS to manage interconnectivity between workloads running in different AWS accounts. Share the AWS Direct Connect and VPN connection with other workloads in the bank.

1. Provide secure outbound access from an outbound Amazon VPC through a proxy.

1. Authenticate accredited third parties and provide access tokens through mutual TLS (mTLS) for transport layer security.

1. Expose Open Banking APIs and Authorization APIs through Amazon API Gateway. Integrate AWS WAF with Amazon API Gateway for web protection.

1. Store public certificates of clients in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) as a trust store for validating requests. Validate the authenticity of third parties against a Trust Service Provider (TSP).

1. Connect Amazon API Gateway to the private subnets hosting microservices in other AWS accounts through a private integration Amazon VPC and AWS PrivateLink.

1. Provide traffic management and domain name resolution by using [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/). Deliver static data through [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) with [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) protection.

## Further reading
<a name="ob-p1-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="ob-p1-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](open-banking-overview.md#ob-overview-history) | Reference architecture diagram first published. | September 7, 2021 | 
| [Initial publication](#ob-p1-history) | Reference architecture diagram first published. | September 7, 2021 | 
| [Initial publication](open-banking-part2.md#ob-p2-history) | Reference architecture diagram first published. | September 7, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.