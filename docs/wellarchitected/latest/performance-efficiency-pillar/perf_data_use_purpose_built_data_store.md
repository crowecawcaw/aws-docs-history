

# PERF03-BP01 Use a purpose-built data store that best supports your data access and storage requirements
<a name="perf_data_use_purpose_built_data_store"></a>

 Understand data characteristics (like shareable, size, cache size, access patterns, latency, throughput, and persistence of data) to select the right purpose-built data stores (storage or database) for your workload. 

 **Common anti-patterns:** 
+  You stick to one data store because there is internal experience and knowledge of one particular type of database solution. 
+  You assume that all workloads have similar data storage and access requirements. 
+  You have not implemented a data catalog to inventory your data assets. 

 **Benefits of establishing this best practice:** Understanding data characteristics and requirements allows you to determine the most efficient and performant storage technology appropriate for your workload needs. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 When selecting and implementing data storage, make sure that the querying, scaling, and storage characteristics support the workload data requirements. AWS provides numerous data storage and database technologies including block storage, object storage, streaming storage, file system, relational, key-value, document, in-memory, graph, time series, and ledger databases. Each data management solution has options and configurations available to you to support your use-cases and data models. By understanding data characteristics and requirements, you can break away from monolithic storage technology and restrictive, one-size-fits-all approaches to focus on managing data appropriately. 

### Implementation steps
<a name="implementation-steps"></a>
+  Conduct an inventory of the various data types that exist in your workload. 
+  Understand and document data characteristics and requirements, including: 
  +  Data type (unstructured, semi-structured, relational) 
  +  Data volume and growth 
  +  Data durability: persistent, ephemeral, transient 
  +  ACID (atomicity, consistency, isolation, durability) requirements 
  +  Data access patterns (read-heavy or write-heavy) 
  +  Latency 
  +  Throughput 
  +  IOPS (input/output operations per second) 
  +  Data retention period 
+  Learn about different data stores ([storage](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html) and [database](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html) services) available for your workload on AWS that can meet your data characteristics, as outlined in [PERF01-BP01 Learn about and understand available cloud services and features](perf_architecture_understand_cloud_services_and_features.md). Some examples of AWS storage technologies and their key characteristics include: 


<table>
<thead>
  <tr><th> <b>Type</b> </th><th> <b>AWS Services</b> </th><th> <b>Key characteristics</b> </th></tr>
</thead>
<tbody>
  <tr><td>Object storage</td><td> <a href="https://aws.amazon.com/s3/">Amazon S3</a> </td><td> Unlimited scalability, high availability, and multiple options for accessibility. Transferring and accessing objects in and out of Amazon S3 can use a service, such as <a href="https://aws.amazon.com/s3/transfer-acceleration/">Transfer Acceleration</a> or <a href="https://aws.amazon.com/s3/features/access-points/">Access Points</a>, to support your location, security needs, and access patterns. </td></tr>
  <tr><td>Archiving storage</td><td> <a href="https://aws.amazon.com/s3/storage-classes/glacier/">Amazon Glacier</a> </td><td> Built for data archiving. </td></tr>
  <tr><td>Streaming storage</td><td> <a href="https://aws.amazon.com/kinesis/">Amazon Kinesis</a> <br /><a href="https://aws.amazon.com/msk/"> Amazon Managed Streaming for Apache Kafka (Amazon MSK) </a></td><td> Efficient ingestion and storage of streaming data. </td></tr>
  <tr><td>Shared file system</td><td><a href="https://aws.amazon.com/efs/">Amazon Elastic File System (Amazon EFS)</a></td><td> Mountable file system that can be accessed by multiple types of compute solutions. </td></tr>
  <tr><td>Shared file system</td><td> <a href="https://aws.amazon.com/fsx/">Amazon FSx</a> </td><td> Built on the latest AWS compute solutions to support four commonly used file systems: NetApp ONTAP, OpenZFS, Windows File Server, and Lustre. Amazon FSx <a href="https://aws.amazon.com/fsx/when-to-choose-fsx/">latency, throughput, and IOPS</a> vary per file system and should be considered when selecting the right file system for your workload needs. </td></tr>
  <tr><td>Block storage</td><td> <a href="https://aws.amazon.com/ebs/">Amazon Elastic Block Store (Amazon EBS)</a> </td><td> Scalable, high-performance block-storage service designed for Amazon Elastic Compute Cloud (Amazon EC2). Amazon EBS includes SSD-backed storage for transactional, IOPS-intensive workloads and HDD-backed storage for throughput-intensive workloads. </td></tr>
  <tr><td>Relational database</td><td> <a href="https://aws.amazon.com/rds/aurora">Amazon Aurora</a>, <a href="https://aws.amazon.com/rds">Amazon RDS</a>, <a href="https://aws.amazon.com/redshift">Amazon Redshift</a>. </td><td> Designed to support ACID (atomicity, consistency, isolation, durability) transactions, and maintain referential integrity and strong data consistency. Many traditional applications, enterprise resource planning (ERP), customer relationship management (CRM), and ecommerce use relational databases to store their data. </td></tr>
  <tr><td>Key-value database</td><td> <a href="https://aws.amazon.com/dynamodb/">Amazon DynamoDB</a> </td><td> Optimized for common access patterns, typically to store and retrieve large volumes of data. High-traffic web apps, ecommerce systems, and gaming applications are typical use-cases for key-value databases. </td></tr>
  <tr><td>Document database</td><td> <a href="https://aws.amazon.com/documentdb/">Amazon DocumentDB</a> </td><td> Designed to store semi-structured data as JSON-like documents. These databases help developers build and update applications such as content management, catalogs, and user profiles quickly.  </td></tr>
  <tr><td>In-memory database</td><td> <a href="https://aws.amazon.com/elasticache/">Amazon ElastiCache</a> , <a href="https://aws.amazon.com/memorydb/">Amazon MemoryDB for Redis</a> </td><td> Used for applications that require real-time access to data, lowest latency and highest throughput. You may use in-memory databases for application caching, session management, gaming leaderboards, low latency ML feature store, microservices messaging system, and a high-throughput streaming mechanism </td></tr>
  <tr><td>Graph database</td><td> <a href="https://aws.amazon.com/neptune/">Amazon Neptune</a> </td><td> Used for applications that must navigate and query millions of relationships between highly connected graph datasets with millisecond latency at large scale. Many companies use graph databases for fraud detection, social networking, and recommendation engines. </td></tr>
  <tr><td>Time Series database</td><td> <a href="https://aws.amazon.com/timestream/">Amazon Timestream</a> </td><td> Used to efficiently collect, synthesize, and derive insights from data that changes over time. IoT applications, DevOps, and industrial telemetry can utilize time-series databases. </td></tr>
  <tr><td> Wide column </td><td> <a href="https://aws.amazon.com/mcs/">Amazon Keyspaces (for Apache Cassandra)</a> </td><td> Uses tables, rows, and columns, but unlike a relational database, the names and format of the columns can vary from row to row in the same table. You typically see a wide column store in high scale industrial apps for equipment maintenance, fleet management, and route optimization.  </td></tr>
  <tr><td> Ledger </td><td> <a href="https://aws.amazon.com/qldb/">Amazon Quantum Ledger Database (Amazon QLDB)</a> </td><td> Provides a centralized and trusted authority to maintain a scalable, immutable, and cryptographically verifiable record of transactions for every application. We see ledger databases used for systems of record, supply chain, registrations, and even banking transactions.   </td></tr>
</tbody>
</table>

+  If you are building a data platform, leverage [modern data architecture](https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/) on AWS to integrate your data lake, data warehouse, and purpose-built data stores. 
+  The key questions that you need to consider when choosing a data store for your workload are as follows: 


<table>
<thead>
  <tr><th> Question </th><th> Things to consider </th></tr>
</thead>
<tbody>
  <tr><td> How is the data structured? </td><td> <ul><li>  If the data is unstructured, consider an object-store such as <a href="https://aws.amazon.com/products/storage/data-lake-storage/">Amazon S3</a> or a NoSQL database such as <a href="https://aws.amazon.com/documentdb/">Amazon DocumentDB</a>  </li><li>  For key-value data, consider <a href="https://aws.amazon.com/documentdb/">DynamoDB</a>, <a href="https://aws.amazon.com/elasticache/redis/">Amazon ElastiCache (Redis OSS)</a> or <a href="https://aws.amazon.com/memorydb/">Amazon MemoryDB</a>  </li></ul> </td></tr>
  <tr><td> What level of referential integrity is required? </td><td> <ul><li>  For foreign key constraints, relational databases such as <a href="https://aws.amazon.com/rds/">Amazon RDS</a> and <a href="https://aws.amazon.com/rds/aurora/">Aurora</a> can provide this level of integrity.  </li><li>  Typically, within a NoSQL data-model, you would de-normalize your data into a single document or collection of documents to be retrieved in a single request rather than joining across documents or tables.   </li></ul> </td></tr>
  <tr><td> Is ACID (atomicity, consistency, isolation, durability) compliance required? </td><td> <ul><li>  If the ACID properties associated with relational databases are required, consider a relational database such as <a href="https://aws.amazon.com/rds/">Amazon RDS</a> and <a href="https://aws.amazon.com/rds/aurora/">Aurora</a>.  </li><li>  If strong consistency is required for <a href="https://aws.amazon.com/nosql/">NoSQL database</a>, you can use strongly consistent reads with <a href="https://aws.amazon.com/documentdb/">DynamoDB</a>.  </li></ul> </td></tr>
  <tr><td> How will the storage requirements change over time? How does this impact scalability? </td><td> <ul><li>  Serverless databases such as <a href="https://aws.amazon.com/documentdb/">DynamoDB</a> and <a href="https://aws.amazon.com/qldb/">Amazon Quantum Ledger Database (Amazon QLDB)</a> will scale dynamically.  </li><li>  Relational databases have upper bounds on provisioned storage, and often must be horizontally partitioned using mechanisms such as sharding once they reach these limits.  </li></ul> </td></tr>
  <tr><td> What is the proportion of read queries in relation to write queries? Would caching be likely to improve performance? </td><td> <ul><li>  Read-heavy workloads can benefit from a caching layer, like <a href="https://aws.amazon.com/elasticache/">ElastiCache</a> or <a href="https://aws.amazon.com/dynamodb/dax/">DAX</a> if the database is DynamoDB.  </li><li>  Reads can also be offloaded to read replicas with relational databases such as <a href="https://aws.amazon.com/rds/">Amazon RDS</a>.  </li></ul> </td></tr>
  <tr><td> Does storage and modification (OLTP - Online Transaction Processing) or retrieval and reporting (OLAP - Online Analytical Processing) have a higher priority? </td><td> <ul><li>  For high-throughput read as-is transactional processing, consider a NoSQL database such as DynamoDB.  </li><li>  For high-throughput and complex read patterns (like join) with consistency use Amazon RDS.  </li><li>  For analytical queries, consider a columnar database such as <a href="https://aws.amazon.com/redshift/">Amazon Redshift</a> or exporting the data to Amazon S3 and performing analytics using <a href="https://aws.amazon.com/athena/">Athena</a> or <a href="https://aws.amazon.com/quicksight/">Amazon Quick</a>.  </li></ul> </td></tr>
  <tr><td> What level of durability does the data require? </td><td> <ul><li>  Aurora automatically replicates your data across three Availability Zones within a Region, meaning your data is highly durable with less chance of data loss.  </li><li>  DynamoDB is automatically replicated across multiple Availability Zones, providing high availability and data durability.  </li><li>  Amazon S3 provides 11 nines of durability. Many database services, such as Amazon RDS and DynamoDB, support exporting data to Amazon S3 for long-term retention and archival.  </li></ul> </td></tr>
  <tr><td> Is there a desire to move away from commercial database engines or licensing costs? </td><td> <ul><li>  Consider open-source engines such as PostgreSQL and MySQL on Amazon RDS or Aurora.  </li><li>  Leverage <a href="https://aws.amazon.com/dms/">AWS Database Migration Service</a> and <a href="https://aws.amazon.com/dms/schema-conversion-tool/">AWS Schema Conversion Tool</a> to perform migrations from commercial database engines to open-source  </li></ul> </td></tr>
  <tr><td> What is the operational expectation for the database? Is moving to managed services a primary concern? </td><td> <ul><li>  Leveraging Amazon RDS instead of Amazon EC2, and DynamoDB or Amazon DocumentDB instead of self-hosting a NoSQL database can reduce operational overhead.  </li></ul> </td></tr>
  <tr><td> How is the database currently accessed? Is it only application access, or are there business intelligence (BI) users and other connected off-the-shelf applications? </td><td> <ul><li>  If you have dependencies on external tooling then you may have to maintain compatibility with the databases they support. Amazon RDS is fully compatible with the difference engine versions that it supports including Microsoft SQL Server, Oracle, MySQL, and PostgreSQL.  </li></ul> </td></tr>
</tbody>
</table>

+  Perform experiments and benchmarking in a non-production environment to identify which data store can address your workload requirements. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) 
+  [Amazon EC2 Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html) 
+  [Amazon EFS: Amazon EFS Performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html) 
+  [Amazon FSx for Lustre Performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html) 
+  [Amazon FSx for Windows File Server Performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html) 
+  [Amazon Glacier: Amazon Glacier Documentation](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html) 
+  [Amazon S3: Request Rate and Performance Considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html) 
+  [Cloud Storage with AWS](https://aws.amazon.com/products/storage/) 
+  [Amazon EBS I/O Characteristics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html) 
+  [Cloud Databases with AWS ](https://aws.amazon.com/products/databases/?ref=wellarchitected) 
+  [AWS Database Caching ](https://aws.amazon.com/caching/database-caching/?ref=wellarchitected) 
+  [DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/?ref=wellarchitected) 
+  [Amazon Aurora best practices ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html?ref=wellarchitected) 
+  [Amazon Redshift performance ](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html?ref=wellarchitected) 
+  [Amazon Athena top 10 performance tips ](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected) 
+  [Amazon Redshift Spectrum best practices ](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/?ref=wellarchitected) 
+  [Amazon DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html?ref=wellarchitected) 
+  [Choose between Amazon EC2 and Amazon RDS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/comparison.html) 
+ [ Best Practices for Implementing Amazon ElastiCache ](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/BestPractices.html)

 **Related videos:** 
+  [AWS re:Invent 2023: Improve Amazon Elastic Block Store efficiency and be more cost-efficient](https://www.youtube.com/watch?v=7-CB02rqiuw) 
+  [AWS re:Invent 2023: Optimizing storage price and performance with Amazon Simple Storage Service](https://www.youtube.com/watch?v=RxgYNrXPOLw) 
+  [AWS re:Invent 2023: Building and optimizing a data lake on Amazon Simple Storage Service](https://www.youtube.com/watch?v=mpQa_Zm1xW8) 
+  [AWS re:Invent 2022: Building modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o) 
+  [AWS re:Invent 2022: Building data mesh architectures on AWS](https://www.youtube.com/watch?v=nGRvlobeM_U) 
+  [AWS re:Invent 2023: Deep dive into Amazon Aurora and its innovations](https://www.youtube.com/watch?v=je6GCOZ22lI) 
+  [AWS re:Invent 2023: Advanced data modeling with Amazon DynamoDB](https://www.youtube.com/watch?v=PVUofrFiS_A) 
+ [AWS re:Invent 2022: Modernize apps with purpose-built databases](https://www.youtube.com/watch?v=V-DiplATdi0)
+ [ Amazon DynamoDB deep dive: Advanced design patterns ](https://www.youtube.com/watch?v=6yqfmXiZTlM)

 **Related examples:** 
+  [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US) 
+  [Databases for Developers](https://catalog.workshops.aws/db4devs/en-US) 
+  [AWS Modern Data Architecture Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US) 
+  [Build a Data Mesh on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US) 
+  [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html) 
+  [Optimize Data Pattern using Amazon Redshift Data Sharing](https://wellarchitectedlabs.com/sustainability/300_labs/300_optimize_data_pattern_using_redshift_data_sharing/) 
+  [Database Migrations](https://github.com/aws-samples/aws-database-migration-samples) 
+  [MS SQL Server - AWS Database Migration Service (AWS DMS) Replication Demo](https://github.com/aws-samples/aws-dms-sql-server) 
+  [Database Modernization Hands On Workshop](https://github.com/aws-samples/amazon-rds-purpose-built-workshop) 
+  [Amazon Neptune Samples](https://github.com/aws-samples/amazon-neptune-samples) 