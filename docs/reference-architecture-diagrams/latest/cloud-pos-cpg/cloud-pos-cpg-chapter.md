

# Cloud Point-of-Sale (POS) System on AWS for CPG
<a name="cloud-pos-cpg-chapter"></a>

## Overview
<a name="cloud-pos-overview"></a>

A modern point-of-sale (POS) system does much more than provide checkout for customers. While extra capabilities are welcome, they complicate maintenance and make upgrades more complex. Consumer packaged goods (CPG) companies need a scalable and maintainable POS solution for direct-to-consumer store sales.

This architecture shows four key features a cloud-based POS system should have: checkout, order capture, product management, and back office. You can share these features with a direct-to-consumer (DTC) ecommerce implementation.

Publication date: October 2021

![Store devices connecting through AWS Outposts and edge services, with or Site-to-Site VPN connectivity to the AWS Cloud integration layer, serverless application layer, purpose-built data layer, and management and analytics services.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/cloud-pos-cpg/images/cloud-pos-cpg.png)


**Download:** [Architecture diagram (PDF)](samples/cloud-pos-cpg.zip)

## Architecture
<a name="cloud-pos-architecture"></a>

The following steps describe the architecture:

1. [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/) adds AWS compute and storage capability at stores. It uses 1U and 2U form factors.

1. AWS edge services improve user experience and speed content delivery. [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) and [Lambda@Edge](https://docs.aws.amazon.com/lambda/latest/dg/) integrate with external service providers such as payment gateways and tax calculators.

1. You choose either [https://docs.aws.amazon.com/directconnect/latest/UserGuide/](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) or AWS Site-to-Site VPN for data security in transit.

1. [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/), and [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/appsync/latest/devguide/) form the integration layer. They handle incoming requests and integrate with the backend application layer, the data layer, and corporate system APIs.

1. The data layer uses purpose-built databases. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) handles key-value data. [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) stores relational data. [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/) provides caching. [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) stores objects.

1. The serverless application layer implements the four cloud POS features. [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/), and run the business logic. The application layer also accesses internal systems on the corporate network.

1. The management, analytics, and managed service layer provides ad hoc reporting, monitoring, security, and data protection. It integrates with native AWS services.

1. The application layer integrates with existing internal and third-party applications on corporate networks. Business users and existing business intelligence (BI) and enterprise resource planning (ERP) systems support day-to-day activities.

## Diagram history
<a name="cloud-pos-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#cloud-pos-history) | Reference architecture diagram first published. | October 1, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.