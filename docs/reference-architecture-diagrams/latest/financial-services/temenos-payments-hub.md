

# Temenos Payments Hub

Publication date: **September 2, 2021 ([Diagram history](diagram-history.md))**

With this architecture, you can deploy the Temenos Payments Hub on AWS. This comprehensive platform for payment initiation and distribution uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) for API management, [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) for containerized processing, and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for lightweight microservices.

## Service architecture
<a name="temenos-payments-hub-service"></a>

![Requests flow through API Gateway to Lambda microservices and Amazon ECS backed by DynamoDB and relational databases.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/temenos-payments-hub-service.png)


The following steps describe the architecture:

1. Use Amazon API Gateway private endpoints for secure on-premises access through a VPN or [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).

1. Control and monitor access to the application and its APIs through Amazon API Gateway.

1. Deploy lightweight microservices in Lambda with an optimized data store in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

1. Handle online transaction processing (OLTP) in scalable, containerized application processes running in Amazon ECS.

1. Access AWS services, including [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) and [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/), from within the Amazon VPC through endpoints. This removes the need for internet access.

1. Choose from relational database options including [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/), and NuoDB.

## Availability Zones
<a name="temenos-payments-hub-availability"></a>

With this architecture, you can deploy Temenos Payments Hub with high availability across multiple Availability Zones. The solution uses Amazon Elastic Container Service containers on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) with automatic scaling, and [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/) for messaging.

![Diagram showing high availability for Temenos Payments Hub across Availability Zones with Amazon MQ.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/temenos-payments-hub-availability.png)


The following steps describe the architecture:

1. Connect Amazon API Gateway HTTP API directly to the [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) through the VpcLink resource.

1. Run Amazon ECS containers on AWS Fargate. You can also run your containers on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), or a combination of both AWS Fargate and Amazon EC2.

1. Use Amazon MQ active/standby for high availability messaging. You can also use a network of brokers for fast reconnection.

1. Extend this architecture to three Availability Zones for additional resilience.

1. Use automatic scaling capabilities for all container services.

1. Enhance database availability by using Amazon RDS Multi-AZ deployment.

## Further reading
<a name="temenos-payments-hub-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 