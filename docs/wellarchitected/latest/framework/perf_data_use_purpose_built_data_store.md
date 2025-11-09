# PERF03-BP01 Use a purpose-built data

store that best supports your data access and storage requirements

Understand data characteristics (like shareable, size, cache size, access patterns,
latency, throughput, and persistence of data) to select the right purpose-built data stores
(storage or database) for your workload.

**Common anti-patterns:**

- You stick to one data store because there is internal experience and knowledge of one
  particular type of database solution.
- You assume that all workloads have similar data storage and access requirements.
- You have not implemented a data catalog to inventory your data assets.

**Benefits of establishing this best practice:** Understanding data
characteristics and requirements allows you to determine the most efficient and performant
storage technology appropriate for your workload needs.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

When selecting and implementing data storage, make sure that the querying, scaling, and
storage characteristics support the workload data requirements. AWS provides numerous data
storage and database technologies including block storage, object storage, streaming storage,
file system, relational, key-value, document, in-memory, graph, time series, and ledger
databases. Each data management solution has options and configurations available to you to
support your use-cases and data models. By understanding data characteristics and
requirements, you can break away from monolithic storage technology and restrictive,
one-size-fits-all approaches to focus on managing data appropriately.

### Implementation steps

- Conduct an inventory of the various data types that exist in your workload.
- Understand and document data characteristics and requirements, including:
  - Data type (unstructured, semi-structured, relational)
  - Data volume and growth
  - Data durability: persistent, ephemeral, transient
  - ACID (atomicity, consistency, isolation, durability) requirements
  - Data access patterns (read-heavy or write-heavy)
  - Latency
  - Throughput
  - IOPS (input/output operations per second)
  - Data retention period

- Learn about different data stores ([storage](../../../whitepapers/latest/aws-overview/storage-services.md "../../../whitepapers/latest/aws-overview/storage-services.md") and [database](../../../whitepapers/latest/aws-overview/database.md "../../../whitepapers/latest/aws-overview/database.md") services) available for
  your workload on AWS that can meet your data characteristics, as outlined in [PERF01-BP01 Learn
  about and understand available cloud services and features](perf_architecture_understand_cloud_services_and_features.md "perf_architecture_understand_cloud_services_and_features.md"). Some examples of
  AWS storage technologies and their key characteristics include:

| **Type**             | **AWS Services**                                                                                                                                                                                                                                     | **Key characteristics**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Object storage       | [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")                                                                                                                                                                                 | Unlimited scalability, high availability, and multiple options for<br>accessibility. Transferring and accessing objects in and out of Amazon S3 can use a<br>service, such as [Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/ "https://aws.amazon.com/s3/transfer-acceleration/") or [Access Points](https://aws.amazon.com/s3/features/access-points/ "https://aws.amazon.com/s3/features/access-points/"), to support your<br>location, security needs, and access patterns. |
| Archiving storage    | [Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/")                                                                                                                            | Built for data archiving.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Streaming storage    | [Amazon Kinesis](https://aws.amazon.com/kinesis/ "https://aws.amazon.com/kinesis/")<br>[Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/ "https://aws.amazon.com/msk/")                                           | Efficient ingestion and storage of streaming data.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Shared file system   | [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/")                                                                                                                                                 | Mountable file system that can be accessed by multiple types of<br>compute solutions.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Shared file system   | [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/")                                                                                                                                                                              | Built on the latest AWS compute solutions to support four commonly used<br>file systems: NetApp ONTAP, OpenZFS, Windows File Server, and Lustre.<br>Amazon FSx [latency,<br>throughput, and IOPS](https://aws.amazon.com/fsx/when-to-choose-fsx/ "https://aws.amazon.com/fsx/when-to-choose-fsx/") vary per file system and should be considered<br>when selecting the right file system for your workload needs.                                                                                       |
| Block storage        | [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/")                                                                                                                                                 | Scalable, high-performance block-storage service designed for Amazon Elastic Compute Cloud<br>(Amazon EC2). Amazon EBS includes SSD-backed storage for transactional, IOPS-intensive<br>workloads and HDD-backed storage for throughput-intensive workloads.                                                                                                                                                                                                                                            |
| Relational database  | [Amazon Aurora](https://aws.amazon.com/rds/aurora "https://aws.amazon.com/rds/aurora"), [Amazon RDS](https://aws.amazon.com/rds "https://aws.amazon.com/rds"), [Amazon Redshift](https://aws.amazon.com/redshift "https://aws.amazon.com/redshift"). | Designed to support ACID (atomicity, consistency, isolation, durability)<br>transactions, and maintain referential integrity and strong data consistency.<br>Many traditional applications, enterprise resource planning (ERP), customer<br>relationship management (CRM), and ecommerce use relational databases to store<br>their data.                                                                                                                                                               |
| Key-value database   | [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")                                                                                                                                                               | Optimized for common access patterns, typically to store and retrieve<br>large volumes of data. High-traffic web apps, ecommerce systems, and gaming<br>applications are typical use-cases for key-value databases.                                                                                                                                                                                                                                                                                     |
| Document database    | [Amazon DocumentDB](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/")                                                                                                                                                         | Designed to store semi-structured data as JSON-like documents. These<br>databases help developers build and update applications such as content<br>management, catalogs, and user profiles quickly.                                                                                                                                                                                                                                                                                                     |
| In-memory database   | [Amazon ElastiCache](https://aws.amazon.com/elasticache/ "https://aws.amazon.com/elasticache/") , [Amazon MemoryDB for Redis](https://aws.amazon.com/memorydb/ "https://aws.amazon.com/memorydb/")                                                   | Used for applications that require real-time access to data, lowest<br>latency and highest throughput. You may use in-memory databases for application<br>caching, session management, gaming leaderboards, low latency ML feature store,<br>microservices messaging system, and a high-throughput streaming mechanism                                                                                                                                                                                  |
| Graph database       | [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/")                                                                                                                                                                  | Used for applications that must navigate and query millions of<br>relationships between highly connected graph datasets with millisecond latency<br>at large scale. Many companies use graph databases for fraud detection, social<br>networking, and recommendation engines.                                                                                                                                                                                                                           |
| Time Series database | [Amazon Timestream](https://aws.amazon.com/timestream/ "https://aws.amazon.com/timestream/")                                                                                                                                                         | Used to efficiently collect, synthesize, and derive insights from data<br>that changes over time. IoT applications, DevOps, and industrial telemetry can<br>utilize time-series databases.                                                                                                                                                                                                                                                                                                              |
| Wide column          | [Amazon Keyspaces (for Apache<br>Cassandra)](https://aws.amazon.com/mcs/ "https://aws.amazon.com/mcs/")                                                                                                                                              | Uses tables, rows, and columns, but unlike a relational database, the<br>names and format of the columns can vary from row to row in the same table. You<br>typically see a wide column store in high scale industrial apps for equipment<br>maintenance, fleet management, and route optimization.                                                                                                                                                                                                     |
| Ledger               | [Amazon Quantum Ledger Database (Amazon<br>QLDB)](https://aws.amazon.com/qldb/ "https://aws.amazon.com/qldb/")                                                                                                                                       | Provides a centralized and trusted authority to maintain a scalable,<br>immutable, and cryptographically verifiable record of transactions for every<br>application. We see ledger databases used for systems of record, supply chain,<br>registrations, and even banking transactions.                                                                                                                                                                                                                 |

- If you are building a data platform, leverage [modern data
  architecture](https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/ "https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/") on AWS to integrate your data lake, data warehouse, and
  purpose-built data stores.
- The key questions that you need to consider when choosing a data store for your
  workload are as follows:

| Question                                                                                                                                                                   | Things to consider                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How is the data structured?                                                                                                                                                | + If the data is unstructured, consider an object-store such as [Amazon S3](https://aws.amazon.com/products/storage/data-lake-storage/ "https://aws.amazon.com/products/storage/data-lake-storage/")<br>or a NoSQL database such as [Amazon DocumentDB](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/")<br>+ For key-value data, consider [DynamoDB](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/"), [Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/elasticache/redis/ "https://aws.amazon.com/elasticache/redis/") or [Amazon MemoryDB](https://aws.amazon.com/memorydb/ "https://aws.amazon.com/memorydb/") |
| What level of referential integrity is required?                                                                                                                           | + For foreign key constraints, relational databases such as [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/") and [Aurora](https://aws.amazon.com/rds/aurora/ "https://aws.amazon.com/rds/aurora/") can provide this level of integrity.<br>+ Typically, within a NoSQL data-model, you would de-normalize your<br>data into a single document or collection of documents to be retrieved in<br>a single request rather than joining across documents or tables.                                                                                                                                                                                    |
| Is ACID (atomicity, consistency, isolation, durability) compliance<br>required?                                                                                            | + If the ACID properties associated with relational databases are<br>required, consider a relational database such as [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/") and [Aurora](https://aws.amazon.com/rds/aurora/ "https://aws.amazon.com/rds/aurora/").<br>+ If strong consistency is required for [NoSQL database](https://aws.amazon.com/nosql/ "https://aws.amazon.com/nosql/"), you can use strongly consistent<br>reads with [DynamoDB](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/").                                                                                                                       |
| How will the storage requirements change over time? How does this impact<br>scalability?                                                                                   | + Serverless databases such as [DynamoDB](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/") and [Amazon Quantum Ledger Database (Amazon QLDB)](https://aws.amazon.com/qldb/ "https://aws.amazon.com/qldb/") will scale dynamically.<br>+ Relational databases have upper bounds on provisioned storage, and<br>often must be horizontally partitioned using mechanisms such as sharding<br>once they reach these limits.                                                                                                                                                                                                                           |
| What is the proportion of read queries in relation to write queries? Would<br>caching be likely to improve performance?                                                    | + Read-heavy workloads can benefit from a caching layer, like [ElastiCache](https://aws.amazon.com/elasticache/ "https://aws.amazon.com/elasticache/") or [DAX](https://aws.amazon.com/dynamodb/dax/ "https://aws.amazon.com/dynamodb/dax/") if the database is<br>DynamoDB.<br>+ Reads can also be offloaded to read replicas with relational<br>databases such as [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/").                                                                                                                                                                                                                              |
| Does storage and modification (OLTP<br>• Online Transaction Processing) or<br>retrieval and reporting (OLAP<br>• Online Analytical Processing) have a higher<br>priority?  | + For high-throughput read as-is transactional processing, consider a<br>NoSQL database such as DynamoDB.<br>+ For high-throughput and complex read patterns (like join) with<br>consistency use Amazon RDS.<br>+ For analytical queries, consider a columnar database such as [Amazon Redshift](https://aws.amazon.com/redshift/ "https://aws.amazon.com/redshift/") or exporting the data<br>to Amazon S3 and performing analytics using [Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/") or [Amazon Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/").                                                    |
| What level of durability does the data require?                                                                                                                            | + Aurora automatically replicates your data across three Availability<br>Zones within a Region, meaning your data is highly durable with less<br>chance of data loss.<br>+ DynamoDB is automatically replicated across multiple Availability Zones,<br>providing high availability and data durability.<br>+ Amazon S3 provides 11 nines of durability. Many database services, such as<br>Amazon RDS and DynamoDB, support exporting data to Amazon S3 for long-term retention<br>and archival.                                                                                                                                                                          |
| Is there a desire to move away from commercial database engines or<br>licensing costs?                                                                                     | + Consider open-source engines such as PostgreSQL and MySQL on Amazon RDS or<br>Aurora.<br>+ Leverage [AWS Database Migration Service](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/") and<br>[AWS Schema Conversion Tool](https://aws.amazon.com/dms/schema-conversion-tool/ "https://aws.amazon.com/dms/schema-conversion-tool/") to perform migrations from commercial database<br>engines to open-source                                                                                                                                                                                                                                                   |
| What is the operational expectation for the database? Is moving to managed<br>services a primary concern?                                                                  | + Leveraging Amazon RDS instead of Amazon EC2, and DynamoDB or Amazon DocumentDB instead of<br>self-hosting a NoSQL database can reduce operational overhead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| How is the database currently accessed? Is it only application access, or<br>are there business intelligence (BI) users and other connected off-the-shelf<br>applications? | + If you have dependencies on external tooling then you may have to<br>maintain compatibility with the databases they support. Amazon RDS is fully<br>compatible with the difference engine versions that it supports including<br>Microsoft SQL Server, Oracle, MySQL, and PostgreSQL.                                                                                                                                                                                                                                                                                                                                                                                   |

- Perform experiments and benchmarking in a non-production environment to identify
  which data store can address your workload requirements.

## Resources

**Related documents:**

- [Amazon EBS Volume
  Types](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md")
- [Amazon EC2
  Storage](../../../AWSEC2/latest/UserGuide/Storage.md "../../../AWSEC2/latest/UserGuide/Storage.md")
- [Amazon EFS: Amazon EFS
  Performance](../../../efs/latest/ug/performance.md "../../../efs/latest/ug/performance.md")
- [Amazon FSx for Lustre
  Performance](../../../fsx/latest/LustreGuide/performance.md "../../../fsx/latest/LustreGuide/performance.md")
- [Amazon FSx for Windows File Server Performance](../../../fsx/latest/WindowsGuide/performance.md "../../../fsx/latest/WindowsGuide/performance.md")
- [Amazon Glacier:
  Amazon Glacier Documentation](../../../amazonglacier/latest/dev/introduction.md "../../../amazonglacier/latest/dev/introduction.md")
- [Amazon S3: Request Rate and
  Performance Considerations](../../../AmazonS3/latest/dev/request-rate-perf-considerations.md "../../../AmazonS3/latest/dev/request-rate-perf-considerations.md")
- [Cloud Storage with AWS](https://aws.amazon.com/products/storage/ "https://aws.amazon.com/products/storage/")
- [Amazon EBS I/O Characteristics](../../../AWSEC2/latest/WindowsGuide/ebs-io-characteristics.md "../../../AWSEC2/latest/WindowsGuide/ebs-io-characteristics.md")
- [Cloud Databases with
  AWS](https://aws.amazon.com/products/databases/?ref=wellarchitected "https://aws.amazon.com/products/databases/?ref=wellarchitected")
- [AWS Database
  Caching](https://aws.amazon.com/caching/database-caching/?ref=wellarchitected "https://aws.amazon.com/caching/database-caching/?ref=wellarchitected")
- [DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/?ref=wellarchitected "https://aws.amazon.com/dynamodb/dax/?ref=wellarchitected")
- [Amazon Aurora
  best practices](../../../AmazonRDS/latest/UserGuide/Aurora.md "../../../AmazonRDS/latest/UserGuide/Aurora.md")
- [Amazon Redshift performance](../../../redshift/latest/dg/c_challenges_achieving_high_performance_queries.md "../../../redshift/latest/dg/c_challenges_achieving_high_performance_queries.md")
- [Amazon Athena top 10 performance tips](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected "https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected")
- [Amazon Redshift Spectrum best practices](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/?ref=wellarchitected "https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/?ref=wellarchitected")
- [Amazon DynamoDB best practices](../../../amazondynamodb/latest/developerguide/BestPractices.md "../../../amazondynamodb/latest/developerguide/BestPractices.md")
- [Choose between
  Amazon EC2 and Amazon RDS](../../../prescriptive-guidance/latest/migration-sql-server/comparison.md "../../../prescriptive-guidance/latest/migration-sql-server/comparison.md")
- [Best Practices for Implementing Amazon ElastiCache](../../../AmazonElastiCache/latest/red-ug/BestPractices.md "../../../AmazonElastiCache/latest/red-ug/BestPractices.md")

**Related videos:**

- [AWS re:Invent 2023: Improve
  Amazon Elastic Block Store efficiency and be more cost-efficient](https://www.youtube.com/watch?v=7-CB02rqiuw "https://www.youtube.com/watch?v=7-CB02rqiuw")
- [AWS re:Invent 2023: Optimizing
  storage price and performance with Amazon Simple Storage Service](https://www.youtube.com/watch?v=RxgYNrXPOLw "https://www.youtube.com/watch?v=RxgYNrXPOLw")
- [AWS re:Invent 2023: Building
  and optimizing a data lake on Amazon Simple Storage Service](https://www.youtube.com/watch?v=mpQa_Zm1xW8 "https://www.youtube.com/watch?v=mpQa_Zm1xW8")
- [AWS re:Invent 2022: Building
  modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o "https://www.youtube.com/watch?v=Uk2CqEt5f0o")
- [AWS re:Invent 2022: Building
  data mesh architectures on AWS](https://www.youtube.com/watch?v=nGRvlobeM_U "https://www.youtube.com/watch?v=nGRvlobeM_U")
- [AWS re:Invent 2023: Deep dive
  into Amazon Aurora and its innovations](https://www.youtube.com/watch?v=je6GCOZ22lI "https://www.youtube.com/watch?v=je6GCOZ22lI")
- [AWS re:Invent 2023: Advanced
  data modeling with Amazon DynamoDB](https://www.youtube.com/watch?v=PVUofrFiS_A "https://www.youtube.com/watch?v=PVUofrFiS_A")
- [AWS re:Invent 2022:
  Modernize apps with purpose-built databases](https://www.youtube.com/watch?v=V-DiplATdi0 "https://www.youtube.com/watch?v=V-DiplATdi0")
- [Amazon DynamoDB deep dive:
  Advanced design patterns](https://www.youtube.com/watch?v=6yqfmXiZTlM "https://www.youtube.com/watch?v=6yqfmXiZTlM")

**Related examples:**

- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US")
- [Databases for Developers](https://catalog.workshops.aws/db4devs/en-US "https://catalog.workshops.aws/db4devs/en-US")
- [AWS Modern Data Architecture Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US")
- [Build a Data Mesh on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US")
- [Amazon S3 Examples](../../../sdk-for-javascript/v2/developer-guide/s3-examples.md "../../../sdk-for-javascript/v2/developer-guide/s3-examples.md")
- [Optimize Data Pattern using Amazon Redshift Data Sharing](https://wellarchitectedlabs.com/sustainability/300_labs/300_optimize_data_pattern_using_redshift_data_sharing/ "https://wellarchitectedlabs.com/sustainability/300_labs/300_optimize_data_pattern_using_redshift_data_sharing/")
- [Database
  Migrations](https://github.com/aws-samples/aws-database-migration-samples "https://github.com/aws-samples/aws-database-migration-samples")
- [MS SQL Server - AWS Database Migration Service
  (AWS DMS) Replication Demo](https://github.com/aws-samples/aws-dms-sql-server "https://github.com/aws-samples/aws-dms-sql-server")
- [Database
  Modernization Hands On Workshop](https://github.com/aws-samples/amazon-rds-purpose-built-workshop "https://github.com/aws-samples/amazon-rds-purpose-built-workshop")
- [Amazon Neptune
  Samples](https://github.com/aws-samples/amazon-neptune-samples "https://github.com/aws-samples/amazon-neptune-samples")
