

# Temenos T24 Transact: Service architecture
<a name="temenos-t24-service"></a>

Publication date: **November 12, 2021 ([Diagram history](#t24-svc-history))**

With this architecture, you can deploy the Temenos T24 Transact core banking solution on AWS. The solution uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) for access control, [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) for containerized online transaction processing (OLTP), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) with [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for read-only queries.

## Temenos T24 Transact service diagram
<a name="t24-svc-diagram"></a>

![Reference architecture diagram showing how to deploy Temenos T24 Transact by using Amazon API Gateway, Amazon ECS, Lambda, and DynamoDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/temenos-t24-transact/images/temenos-t24-service.png)


The following steps describe the service components and data flow for this architecture:

1. Provide security at the perimeter by using AWS security services such as [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) (web application firewall) and [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html).

1. Control and monitor access to T24 through Amazon API Gateway.

1. Handle read-only query activity by using Lambda processing and query-optimized DynamoDB storage.

1. Handle OLTP transactions in scalable, containerized application processes running in Amazon ECS.

1. Ingest events from selected topics of [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/) into DynamoDB tables by using Lambda.

1. Choose from relational database options including [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/), [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), Amazon RDS for SQL Server, or NuoDB.

## Further reading
<a name="t24-svc-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="t24-svc-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#t24-svc-history) | Reference architecture diagram first published. | November 12, 2021 | 
| [Initial publication](temenos-t24-vpc-networking.md#t24-vpc-history) | Reference architecture diagram first published. | November 12, 2021 | 
| [Initial publication](temenos-t24-availability-zones.md#t24-az-history) | Reference architecture diagram first published. | November 12, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.