

# Temenos T24 Transact

Publication date: **November 12, 2021 ([Diagram history](diagram-history.md))**

With this architecture, you can deploy the Temenos T24 Transact core banking solution on AWS. The solution uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) for access control, [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) for containerized online transaction processing (OLTP), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) with [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for read-only queries.

## Service architecture
<a name="temenos-t24-transact-service"></a>

![Diagram showing how to deploy Temenos T24 Transact with API Gateway, Amazon ECS, and Lambda.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/temenos-t24-service.png)


The following steps describe the architecture:

1. Provide security at the perimeter by using AWS security services such as [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) (web application firewall) and [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html).

1. Control and monitor access to T24 through Amazon API Gateway.

1. Handle read-only query activity by using Lambda processing and query-optimized DynamoDB storage.

1. Handle OLTP transactions in scalable, containerized application processes running in Amazon ECS.

1. Ingest events from selected topics of [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/) into DynamoDB tables by using Lambda.

1. Choose from relational database options including [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/), [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), Amazon RDS for SQL Server, or NuoDB.

## Amazon VPC and networking
<a name="temenos-t24-transact-vpc"></a>

With this architecture, you can deploy Temenos T24 with Amazon VPC isolation and secure network access. The solution uses Amazon API Gateway private endpoints for on-premises connectivity and [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) for container compute.

![Diagram showing Temenos T24 Amazon VPC and networking with API Gateway and AWS Fargate.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/temenos-t24-vpc-networking.png)


The following steps describe the architecture:

1. Use [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/), AWS WAF, and AWS Shield for security and performance for internet usage.

1. Use Amazon API Gateway private endpoints for secure on-premises access through a VPN or [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).

1. Restrict access to the Amazon VPC to only through the Amazon API Gateway VpcLink resource.

1. Run Amazon Elastic Container Service containers on AWS Fargate. You can also run your containers on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), or a combination of both AWS Fargate and Amazon EC2.

1. Access AWS services from within the Amazon VPC through endpoints. This removes the need for internet access.

## Availability Zones
<a name="temenos-t24-transact-availability"></a>

With this architecture, you can deploy Temenos T24 with high availability across multiple Availability Zones. The solution uses Amazon API Gateway HTTP API connected to an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/), AWS Fargate with automatic scaling, and [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/) for messaging.

![Diagram showing Temenos T24 high availability across Availability Zones with Amazon MQ and Amazon RDS Multi-AZ.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/temenos-t24-availability-zones.png)


The following steps describe the architecture:

1. Connect Amazon API Gateway HTTP API directly to the Application Load Balancer through the VpcLink resource.

1. Use Amazon MQ active-standby for high availability. You can also use a network of brokers for fast reconnection.

1. Use automatic scaling capabilities for all container services.

1. Enhance database availability by using Amazon RDS Multi-AZ.

1. Extend this architecture to three Availability Zones for additional resilience.

## Further reading
<a name="temenos-t24-transact-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 