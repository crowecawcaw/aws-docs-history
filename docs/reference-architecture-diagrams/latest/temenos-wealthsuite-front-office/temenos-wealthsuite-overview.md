

# Temenos WealthSuite Front Office on AWS: Overview
<a name="temenos-wealthsuite-overview"></a>

Publication date: **January 6, 2023 ([Diagram history](#tw-ov-history))**

With this architecture, you can deploy the Temenos WealthSuite Front Office platform for wealth managers and private bankers. The solution uses [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) for containerized application layers, [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) for API management, and [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) for database services.

## Temenos WealthSuite overview diagram
<a name="tw-ov-diagram"></a>

![Reference architecture diagram showing Temenos WealthSuite Front Office by using Amazon EKS, Amazon API Gateway, Amazon MQ, and Amazon RDS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/temenos-wealthsuite-front-office/images/temenos-wealthsuite-overview.png)


The following steps describe the application layers and data flow for this architecture:

1. Serve the User Experience Platform (UXP) layer through Amazon EKS. The UXP includes an integrated development environment (IDE)-based UI and user experience (UX) designer with support for major mobile platforms.

1. Use the API layer on Amazon EKS as the key entry point for external interfaces. This layer contains the application business logic.

1. Run Finance Services (FIN) as a scalable set of calculation engines on Amazon EKS. Initiate processing from the API layer.

1. Support data import, extract, routing, and transformation through the Integration Layer (INT) on Amazon EKS. Process data in batch or near real-time modes across transport mechanisms including SFTP, HTTPS, [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/), Apache Kafka, and Enterprise Service Bus (ESB).

1. Use multiple AWS services as sources or targets of integration data, including Amazon MQ and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. Run the database on Amazon RDS for Oracle managed relational database services.

## Further reading
<a name="tw-ov-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="tw-ov-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#tw-ov-history) | Reference architecture diagram first published. | January 6, 2023 | 
| [Initial publication](temenos-wealthsuite-vpc-networking.md#tw-vpc-history) | Reference architecture diagram first published. | January 6, 2023 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.