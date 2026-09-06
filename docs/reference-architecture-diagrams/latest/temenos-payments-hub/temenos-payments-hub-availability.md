

# Temenos Payments Hub: Availability Zones architecture
<a name="temenos-payments-hub-availability"></a>

Publication date: **September 2, 2021 ([Diagram history](#tph-az-history))**

With this architecture, you can deploy Temenos Payments Hub with high availability across multiple Availability Zones. The solution uses [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) containers on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) with automatic scaling, and [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/) for messaging.

## Temenos Payments Hub Availability Zones diagram
<a name="tph-az-diagram"></a>

![Reference architecture diagram showing high availability for Temenos Payments Hub across multiple Availability Zones by using Amazon ECS, AWS Fargate, and Amazon MQ.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/temenos-payments-hub/images/temenos-payments-hub-availability.png)


The following steps describe the high availability components for this architecture:

1. Connect [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) HTTP API directly to the Application Load Balancer through the VpcLink resource.

1. Run Amazon ECS containers on AWS Fargate. You can also run your containers on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), or a combination of both AWS Fargate and Amazon EC2.

1. Use Amazon MQ active/standby for high availability messaging. You can also use a network of brokers for fast reconnection.

1. Extend this architecture to three Availability Zones for additional resilience.

1. Use automatic scaling capabilities for all container services.

1. Enhance database availability by using [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) Multi-AZ deployment.

## Further reading
<a name="tph-az-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="tph-az-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](temenos-payments-hub-service.md#tph-svc-history) | Reference architecture diagram first published. | September 2, 2021 | 
| [Initial publication](#tph-az-history) | Reference architecture diagram first published. | September 2, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.