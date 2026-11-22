

# Open Banking on AWS

Publication date: **September 7, 2021 ([Diagram history](diagram-history.md))**

With this architecture, you can open APIs for authorized third parties and implement Open Banking regulations. Third parties access consumer data (account balances, transactions, statements) or initiate payment submissions with customer consent. This supports use cases such as spend analysis, credit decisioning, and ecommerce payments.

## Overview
<a name="open-banking-on-aws-overview"></a>

![A consumer grants a third party consent to access bank data, validated by a Trust Service Provider.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/open-banking-overview.png)


The following steps describe the architecture:

1. Access the licensed or accredited third-party application and provide consent for the third party to access consumer data or initiate a payment submission request.

1. Use third parties as authorized institutions that provide value-added services on top of regular banking needs (accounts information, payments). This approach supports use cases such as spend analysis, credit decisioning, and ecommerce payments.

1. Validate the authenticity of banks and third parties through a Trust Service Provider (TSP) authorized by a supervisory government body. The TSP issues digital certificates to third parties.

1. Connect the bank IT environment, including AWS and data center components.

## Networking and security
<a name="open-banking-on-aws-networking"></a>

With this architecture, you can connect on-premises core banking systems to AWS and expose Open Banking APIs securely. The solution uses [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) for connectivity, [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/) for network hub management, and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) for API management with [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) integration.

![Diagram showing Open Banking networking and security with AWS Direct Connect and API Gateway.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/open-banking-part1.png)


The following steps describe the architecture:

1. Send and receive all new and updated transactions between core banking systems and AWS by using streaming technologies such as Apache Kafka and message queue (MQ) mechanisms.

1. Connect the bank data center to AWS by using a combination of AWS Direct Connect and [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/). Use two diverse AWS Direct Connect connections for maximum resiliency.

1. Use AWS Transit Gateway as the central hub on AWS to manage interconnectivity between workloads running in different AWS accounts. Share the AWS Direct Connect and VPN connection with other workloads in the bank.

1. Provide secure outbound access from an outbound Amazon VPC through a proxy.

1. Authenticate accredited third parties and provide access tokens through mutual TLS (mTLS) for transport layer security.

1. Expose Open Banking APIs and Authorization APIs through Amazon API Gateway. Integrate AWS WAF with Amazon API Gateway for web protection.

1. Store public certificates of clients in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) as a trust store for validating requests. Validate the authenticity of third parties against a Trust Service Provider (TSP).

1. Connect Amazon API Gateway to the private subnets hosting microservices in other AWS accounts through a private integration Amazon VPC and [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/).

1. Provide traffic management and domain name resolution by using [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/). Deliver static data through [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) with [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) protection.

## Services and operations
<a name="open-banking-on-aws-services"></a>

With this architecture, you can implement Open Banking API microservices, manage identity, and monitor security posture. The solution uses [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) with [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) for containerized services, [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for consent storage, and [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/) for threat detection.

![Diagram showing Open Banking microservices, identity, and security with Amazon ECS and GuardDuty.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/open-banking-part2.png)


The following steps describe the architecture:

1. Connect securely between VPCs and services hosted on AWS or on-premises by using AWS PrivateLink.

1. Implement Open Banking API specifications for Account Information and Payments services by using multiple container-based microservices hosted on Amazon ECS with AWS Fargate. Cache customer account information by using [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/). Host webhooks for payment status in this layer.

1. Store consumer consents, aggregated data, and API performance metrics in DynamoDB.

1. Hold a copy of the system of record in [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/). Synchronize data in near real time from the bank core system.

1. Implement the identity provider (IdP) for OAuth 2.0 in a separate AWS account so that other workloads in the bank can consume it securely.

1. Provide a separate developer sandbox for the third party to integrate with the bank AWS environment and build their products.

1. Monitor for malicious activity and unauthorized behavior by using GuardDuty. Get a comprehensive view of security alerts and security posture across AWS accounts by using [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/).

1. Collect logs from all services in Amazon S3. Analyze and monitor logs by using [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/).

1. Manage configuration by using AWS Systems Manager. Deploy environments by using [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/). Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/), [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/), and [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) for notification capability between services.

## Further reading
<a name="open-banking-on-aws-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 