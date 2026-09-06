

# Temenos T24 Transact: Availability Zones architecture
<a name="temenos-t24-availability-zones"></a>

Publication date: **November 12, 2021 ([Diagram history](#t24-az-history))**

With this architecture, you can deploy Temenos T24 with high availability across multiple Availability Zones. The solution uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) HTTP API connected to an Application Load Balancer, [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) with automatic scaling, and [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/) for messaging.

## Temenos T24 Availability Zones diagram
<a name="t24-az-diagram"></a>

![Reference architecture diagram showing Temenos T24 high availability across Availability Zones by using AWS Fargate, Amazon MQ, and Amazon RDS Multi-AZ.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/temenos-t24-transact/images/temenos-t24-availability-zones.png)


The following steps describe the high availability components for this architecture:

1. Connect Amazon API Gateway HTTP API directly to the Application Load Balancer through the VpcLink resource.

1. Use Amazon MQ active-standby for high availability. You can also use a network of brokers for fast reconnection.

1. Use automatic scaling capabilities for all container services.

1. Enhance database availability by using [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) Multi-AZ.

1. Extend this architecture to three Availability Zones for additional resilience.

## Further reading
<a name="t24-az-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="t24-az-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](temenos-t24-service.md#t24-svc-history) | Reference architecture diagram first published. | November 12, 2021 | 
| [Initial publication](temenos-t24-vpc-networking.md#t24-vpc-history) | Reference architecture diagram first published. | November 12, 2021 | 
| [Initial publication](#t24-az-history) | Reference architecture diagram first published. | November 12, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.