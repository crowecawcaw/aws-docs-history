# Secure HTAP Data Architecture Using TiDB Cloud

Publication date: **June 13, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

This reference architecture outlines a modern hybrid transactional/analytical processing (HTAP) data stack on AWS. It uses TiDB, an advanced, open-source, distributed SQL database that powers REST and GraphQL APIs, and near real-time analytics.

## Secure HTAP Data Architecture Using TiDB Cloud Diagram

![Reference architecture diagram showing a modern HTAP data stack on AWS using TiDB.](images/secure-htap-data-architecture-with-tidb-cloud.png)

1. Create RESTful microservices using **Amazon API Gateway** or
   **AWS AppSync** and **AWS Lambda**.
   It can use TiDB Cloud as the online transactional
   processing (OLTP) database. **Lambda** receives all requests and sends them to
   the TiDB Server using an **Amazon Virtual Private Cloud** (Amazon VPC) endpoint.
2. Powered by **AWS PrivateLink**, the endpoint connection is secure and
   private and does not expose your data to the public internet. The **AWS PrivateLink**
   connection also supports a secure connection between VPCs with overlapping
   Classless Inter-Domain Routing (CIDR).
3. Equipped with a massively parallel processing (MPP) engine, TiDB can efficiently handle
   both OLTP and online analytical processing (OLAP) workloads. TiDB uses row-based storage
   (TiKV) for OLTP workloads and column-based storage (TiFlash) for OLAP workloads. Data is
   asynchronously replicated to TiFlash using an extended Raft consensus algorithm for strong
   consistency. TiFlash is a separate set of nodes that isolates workloads and performance
   impact on the OLTP system.
4. Build business intelligence (BI) reports using **Amazon Quick**.
   Queries on TiDB are internally routed to TiFlash and optimized to handle analytical
   workloads. TiDB provides unified architecture and zero-ETL integration between
   OLTP and OLAP workloads.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/secure-htap-data-architecture-with-tidb-cloud.md "samples/secure-htap-data-architecture-with-tidb-cloud.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Contributors

Contributors to this reference architecture diagram include:

- Ayan Ray, Senior Partner Solutions Architect

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date          |
| ------------------- | ----------------------------------------------- | ------------- |
| Initial publication | Reference architecture diagram first published. | June 13, 2023 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
