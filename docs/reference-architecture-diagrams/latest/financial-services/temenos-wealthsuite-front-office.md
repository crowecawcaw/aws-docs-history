

# Temenos WealthSuite Front Office on AWS

Publication date: **January 6, 2023 ([Diagram history](diagram-history.md))**

With this architecture, you can deploy the Temenos WealthSuite Front Office platform for wealth managers and private bankers. The solution uses [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) for containerized application layers, [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) for API management, and [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) for database services.

## Overview
<a name="temenos-wealthsuite-front-office-overview"></a>

![Diagram showing Temenos WealthSuite Front Office with Amazon EKS, API Gateway, and Amazon RDS.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/temenos-wealthsuite-overview.png)


The following steps describe the architecture:

1. Serve the User Experience Platform (UXP) layer through Amazon EKS. The UXP includes an integrated development environment (IDE)-based UI and user experience (UX) designer with support for major mobile platforms.

1. Use the API layer on Amazon EKS as the key entry point for external interfaces. This layer contains the application business logic.

1. Run Finance Services (FIN) as a scalable set of calculation engines on Amazon EKS. Initiate processing from the API layer.

1. Support data import, extract, routing, and transformation through the Integration Layer (INT) on Amazon EKS. Process data in batch or near real-time modes across transport mechanisms including SFTP, HTTPS, [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/), Apache Kafka, and Enterprise Service Bus (ESB).

1. Use multiple AWS services as sources or targets of integration data, including Amazon MQ and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. Run the database on Amazon RDS for Oracle managed relational database services.

## Amazon VPC and networking
<a name="temenos-wealthsuite-front-office-vpc"></a>

With this architecture, you can deploy Temenos WealthSuite with Amazon VPC isolation and secure network access. The solution uses Amazon API Gateway private endpoints, Amazon Elastic Kubernetes Service containers on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) or [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), and [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) for on-premises connectivity.

![Diagram showing Temenos WealthSuite Amazon VPC and networking with API Gateway and Amazon EKS.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/temenos-wealthsuite-vpc-networking.png)


The following steps describe the architecture:

1. Use [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/), [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/), and [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) for security and performance for internet usage.

1. Use Amazon API Gateway private endpoints for secure on-premises access through a VPN or AWS Direct Connect.

1. Restrict access to the Amazon VPC to only through the Amazon API Gateway VpcLink resource.

1. Run Amazon EKS containers on AWS Fargate, Amazon EC2, or a combination of both.

1. Extend this architecture to three Availability Zones for additional resilience.

1. Access AWS services from within the Amazon VPC through endpoints. This removes the need for internet access.

1. Enhance database availability by using Amazon RDS Multi-AZ.

## Further reading
<a name="temenos-wealthsuite-front-office-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 