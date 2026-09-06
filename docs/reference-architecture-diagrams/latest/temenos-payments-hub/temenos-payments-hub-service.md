

# Temenos Payments Hub: Service architecture
<a name="temenos-payments-hub-service"></a>

Publication date: **September 2, 2021 ([Diagram history](#tph-svc-history))**

With this architecture, you can deploy the Temenos Payments Hub on AWS. This comprehensive platform for payment initiation and distribution uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) for API management, [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) for containerized processing, and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for lightweight microservices.

## Temenos Payments Hub service diagram
<a name="tph-svc-diagram"></a>

![Reference architecture diagram showing how to deploy Temenos Payments Hub by using Amazon API Gateway, Amazon ECS, Lambda, and DynamoDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/temenos-payments-hub/images/temenos-payments-hub-service.png)


The following steps describe the service components and data flow for this architecture:

1. Use Amazon API Gateway private endpoints for secure on-premises access through a VPN or [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).

1. Control and monitor access to the application and its APIs through Amazon API Gateway.

1. Deploy lightweight microservices in Lambda with an optimized data store in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

1. Handle online transaction processing (OLTP) in scalable, containerized application processes running in Amazon ECS.

1. Access AWS services, including [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) and [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/), from within the Amazon VPC through endpoints. This removes the need for internet access.

1. Choose from relational database options including [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/), and NuoDB.

## Further reading
<a name="tph-svc-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="tph-svc-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#tph-svc-history) | Reference architecture diagram first published. | September 2, 2021 | 
| [Initial publication](temenos-payments-hub-availability.md#tph-az-history) | Reference architecture diagram first published. | September 2, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.