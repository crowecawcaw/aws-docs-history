

# Secure HTAP Data Architecture Using TiDB Cloud
<a name="secure-htap-data-architecture-with-tidb-cloud"></a>

Publication date: **June 13, 2023 ([Diagram history](#diagram-history))**

This reference architecture outlines a modern hybrid transactional/analytical processing (HTAP) data stack on AWS. It uses TiDB, an advanced, open-source, distributed SQL database that powers REST and GraphQL APIs, and near real-time analytics.

## Secure HTAP Data Architecture Using TiDB Cloud Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing a modern HTAP data stack on AWS using TiDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/secure-htap-data-architecture-with-tidb-cloud/images/secure-htap-data-architecture-with-tidb-cloud.png)


1. Create RESTful microservices using **Amazon API Gateway** or **AWS AppSync** and **AWS Lambda**. It can use TiDB Cloud as the online transactional processing (OLTP) database. **Lambda** receives all requests and sends them to the TiDB Server using an **Amazon Virtual Private Cloud** (Amazon VPC) endpoint. 

1. Powered by **AWS PrivateLink**, the endpoint connection is secure and private and does not expose your data to the public internet. The **AWS PrivateLink** connection also supports a secure connection between VPCs with overlapping Classless Inter-Domain Routing (CIDR). 

1. Equipped with a massively parallel processing (MPP) engine, TiDB can efficiently handle both OLTP and online analytical processing (OLAP) workloads. TiDB uses row-based storage (TiKV) for OLTP workloads and column-based storage (TiFlash) for OLAP workloads. Data is asynchronously replicated to TiFlash using an extended Raft consensus algorithm for strong consistency. TiFlash is a separate set of nodes that isolates workloads and performance impact on the OLTP system. 

1. Build business intelligence (BI) reports using **Amazon Quick Sight**. Queries on TiDB are internally routed to TiFlash and optimized to handle analytical workloads. TiDB provides unified architecture and zero-ETL integration between OLTP and OLAP workloads. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Contributors
<a name="contributors"></a>

 Contributors to this reference architecture diagram include: 
+  Ayan Ray, Senior Partner Solutions Architect 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | June 13, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.