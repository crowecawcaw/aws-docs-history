

# Secure HTAP data architecture using TiDB Cloud

Publication date: **June 13, 2023 ([Diagram history](diagram-history.md))**

This reference architecture outlines a modern hybrid transactional/analytical processing (HTAP) data stack on AWS. It uses TiDB, an advanced, open-source, distributed SQL database that powers REST and GraphQL APIs, and near real-time analytics.

## Secure HTAP data architecture using TiDB Cloud diagram
<a name="secure-htap-diagram"></a>

![Requests pass through API Gateway and Lambda to TiDB Cloud over AWS PrivateLink for OLTP and OLAP.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/financial-services/images/secure-htap-data-architecture-with-tidb-cloud.png)


The following steps describe the architecture:

1. Create RESTful microservices using [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) or [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/) and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/). It can use TiDB Cloud as the online transactional processing (OLTP) database. Lambda receives all requests and sends them to the TiDB Server using an [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/) (Amazon VPC) endpoint. 

1. Powered by [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/), the endpoint connection is secure and private and does not expose your data to the public internet. The AWS PrivateLink connection also supports a secure connection between VPCs with overlapping Classless Inter-Domain Routing (CIDR). 

1. Equipped with a massively parallel processing (MPP) engine, TiDB can efficiently handle both OLTP and online analytical processing (OLAP) workloads. TiDB uses row-based storage (TiKV) for OLTP workloads and column-based storage (TiFlash) for OLAP workloads. Data is asynchronously replicated to TiFlash using an extended Raft consensus algorithm for strong consistency. TiFlash is a separate set of nodes that isolates workloads and performance impact on the OLTP system. 

1. Build business intelligence (BI) reports using [AWS Quick](https://docs.aws.amazon.com/quick/latest/userguide/). Queries on TiDB are internally routed to TiFlash and optimized to handle analytical workloads. TiDB provides unified architecture and zero-ETL integration between OLTP and OLAP workloads. 

## Further reading
<a name="secure-htap-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 