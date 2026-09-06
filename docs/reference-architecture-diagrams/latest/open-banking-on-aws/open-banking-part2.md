

# Open Banking on AWS: Services and operations
<a name="open-banking-part2"></a>

Publication date: **September 7, 2021 ([Diagram history](#ob-p2-history))**

With this architecture, you can implement Open Banking API microservices, manage identity, and monitor security posture. The solution uses [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) with [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) for containerized services, [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for consent storage, and [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/) for threat detection.

## Open Banking services and operations diagram
<a name="ob-p2-diagram"></a>

![Reference architecture diagram showing Open Banking microservices, identity, and security by using Amazon ECS, AWS Fargate, DynamoDB, and Amazon GuardDuty.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/open-banking-on-aws/images/open-banking-part2.png)


The following steps describe the services and operational components for this architecture:

1. Connect securely between VPCs and services hosted on AWS or on-premises by using [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/).

1. Implement Open Banking API specifications for Account Information and Payments services by using multiple container-based microservices hosted on Amazon ECS with AWS Fargate. Cache customer account information by using [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/). Host webhooks for payment status in this layer.

1. Store consumer consents, aggregated data, and API performance metrics in DynamoDB.

1. Hold a copy of the system of record in [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/). Synchronize data in near real time from the bank core system.

1. Implement the identity provider (IdP) for OAuth 2.0 in a separate AWS account so that other workloads in the bank can consume it securely.

1. Provide a separate developer sandbox for the third party to integrate with the bank AWS environment and build their products.

1. Monitor for malicious activity and unauthorized behavior by using GuardDuty. Get a comprehensive view of security alerts and security posture across AWS accounts by using [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/).

1. Collect logs from all services in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Analyze and monitor logs by using [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/).

1. Manage configuration by using AWS Systems Manager. Deploy environments by using [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/). Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/), [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/), and [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) for notification capability between services.

## Further reading
<a name="ob-p2-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="ob-p2-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](open-banking-overview.md#ob-overview-history) | Reference architecture diagram first published. | September 7, 2021 | 
| [Initial publication](open-banking-part1.md#ob-p1-history) | Reference architecture diagram first published. | September 7, 2021 | 
| [Initial publication](#ob-p2-history) | Reference architecture diagram first published. | September 7, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.