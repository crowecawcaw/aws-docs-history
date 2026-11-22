

# PERF03-BP01 Use a purpose-built data store that best supports your data access and storage requirements

 Datasets differ in structure, access pattern, and durability. Using one storage technology for every dataset forces trade-offs that degrade performance and raise cost. Match each dataset to a store designed for its characteristics. 

 **Desired outcome:** 
+  You have documented the characteristics of each dataset, including structure, volume, access pattern, latency, throughput, durability, and retention. 
+  You have matched each workload dataset to a data store built for those characteristics rather than to a single default engine. 
+  You maintain an inventory or data catalog that records where each dataset lives and why that store was chosen. 
+  Your teams select data stores from measured requirements and not from familiarity with one product. 

 **Common anti-patterns:** 
+  Teams standardize on one database engine because they already know it and force every workload onto it. 
+  Teams assume all workloads share the same storage and access requirements. 
+  Teams select a data store before documenting the data's structure, volume, and access pattern. 
+  Teams operate without a data catalog, which hides what data exists and where it is stored. 

 **Benefits of establishing this best practice:** 
+  Each workload runs on a store tuned to its access pattern, which improves latency and throughput. 
+  Costs drop because you stop paying for capabilities a workload does not need. 
+  Scaling stays predictable because each store is chosen for how its data grows. 
+  Teams make faster, evidence-based storage decisions from a shared inventory. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A purpose-built data store is designed for a specific data model and access pattern. For example, a relational database can hold a JSON document or a session token, but a document store or in-memory store serves those patterns faster and at lower cost. 

 Selection starts with the data. *Structure* describes whether data is relational, semi-structured, or unstructured. *Durability class* separates data that must persist from data that is ephemeral or transient. *Access pattern* describes whether the workload is read-heavy or write-heavy, and whether it favors transactional processing or analytical queries. Latency targets, throughput, input/output operations per second (IOPS), and retention period also shape which store fits. 

 For database workloads, the primary distinction is between transactional and analytical work. Online transaction processing (OLTP) favors many small, consistent reads and writes, which suits relational and key-value stores. Online analytical processing (OLAP) favors large scans and aggregations, which suits columnar and data-warehouse stores. Relational engines provide atomicity, consistency, isolation, and durability (ACID) guarantees and referential integrity. They have upper limits on provisioned storage and often need sharding to scale writes horizontally. Key-value and document stores relax joins and, in some configurations, strong consistency in exchange for greater horizontal scale. Serverless stores scale capacity automatically, while provisioned engines require you to size for peak. 

 Managed services reduce the undifferentiated work of patching, backup, and failover. Durability guarantees differ between stores. Match them to how much data loss the workload can tolerate. When a workload spans many patterns, a single store rarely suffices. A modern data architecture connects a data lake, a data warehouse, and purpose-built stores, so data moves between them. 

 AWS provides stores across every major category: object ([Amazon S3](https://aws.amazon.com/s3/)), block ([Amazon EBS](https://aws.amazon.com/ebs/)), file ([Amazon EFS](https://aws.amazon.com/efs/), [Amazon FSx](https://aws.amazon.com/fsx/)), streaming ([Amazon Kinesis](https://aws.amazon.com/kinesis/), [Amazon MSK](https://aws.amazon.com/msk/)), relational ([Amazon Aurora](https://aws.amazon.com/rds/aurora), [Amazon RDS](https://aws.amazon.com/rds), [Amazon Redshift](https://aws.amazon.com/redshift)), key-value ([Amazon DynamoDB](https://aws.amazon.com/dynamodb/)), document ([Amazon DocumentDB](https://aws.amazon.com/documentdb/)), in-memory ([Amazon ElastiCache](https://aws.amazon.com/elasticache/), [Amazon MemoryDB](https://aws.amazon.com/memorydb/)), graph ([Amazon Neptune](https://aws.amazon.com/neptune/)), time series ([Amazon Timestream](https://aws.amazon.com/timestream/)), and wide column ([Amazon Keyspaces (for Apache Cassandra)](https://aws.amazon.com/keyspaces/)). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory your data and build a catalog:** List the datasets across your workload and record each one in a shared inventory or data catalog. Without this record, you cannot reason about which store fits, and duplicate or orphaned data goes unnoticed. 

1.  **Document the characteristics of each dataset:** For every dataset, capture its structure (unstructured, semi-structured, or relational), volume and growth, durability class (persistent, ephemeral, or transient), ACID requirements, read-to-write ratio, latency and throughput targets, IOPS, and retention period. These measurements become the input to selection. 

1.  **Match requirements to a store category:** Work through the decisive questions for each dataset. How is the data structured? Is referential integrity or ACID compliance required? Is the workload OLTP or OLAP? How will storage grow, and does that favor a serverless or provisioned store? Would offloading reads to a cache or replica help? Use the answers to shortlist candidate stores from the AWS [storage](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html) and [database](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html) categories. 

1.  **Integrate multiple stores through a data layer:** If the workload spans several data models, connect your data lake, data warehouse, and purpose-built stores using a [modern data architecture](https://aws.amazon.com/big-data/datalakes-and-analytics/) so that each store handles the pattern it fits while data moves between them. 

1.  **Validate the choice with a proof of concept:** Before you commit, load representative data into the shortlisted store and test it against your real access patterns and performance targets. Confirm that latency, throughput, and scaling behavior meet the workload's requirements, and record the decision and its rationale in the catalog. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF03-BP02 Evaluate available configuration options for data store](perf03-bp02.md) 
+  [PERF03-BP04 Implement strategies to improve query performance in data store](perf03-bp04.md) 
+  [PERF03-BP05 Implement data access patterns that utilize caching](perf03-bp05.md) 

 **Related documents:** 
+  [AWS storage services overview](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html) 
+  [AWS database services overview](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html) 
+  [Cloud storage with AWS](https://aws.amazon.com/products/storage/) 
+  [Cloud databases with AWS](https://aws.amazon.com/products/databases/) 
+  [When to choose Amazon FSx](https://aws.amazon.com/fsx/when-to-choose-fsx/) 

 **Related examples:** 
+  [Optimize data pattern using Amazon Redshift data sharing](https://wellarchitectedlabs.com/) 
+  [Microsoft SQL Server AWS DMS replication demo](https://github.com/aws-samples/aws-dms-sql-server) 
+  [Amazon Neptune samples](https://github.com/aws-samples/amazon-neptune-samples) 

 **Related workshops:** 
+  [AWS purpose-built databases workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US) 
+  [AWS modern data architecture immersion day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US) 

 **Related services:** 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon EBS](https://aws.amazon.com/ebs/) 
+  [Amazon EFS](https://aws.amazon.com/efs/) 
+  [Amazon FSx](https://aws.amazon.com/fsx/) 
+  [Amazon Kinesis](https://aws.amazon.com/kinesis/) 
+  [Amazon MSK](https://aws.amazon.com/msk/) 
+  [Amazon Aurora](https://aws.amazon.com/rds/aurora) 
+  [Amazon RDS](https://aws.amazon.com/rds) 
+  [Amazon Redshift](https://aws.amazon.com/redshift) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon DocumentDB](https://aws.amazon.com/documentdb/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon MemoryDB](https://aws.amazon.com/memorydb/) 
+  [Amazon Neptune](https://aws.amazon.com/neptune/) 
+  [Amazon Timestream](https://aws.amazon.com/timestream/) 
+  [Amazon Keyspaces (for Apache Cassandra) (for Apache Cassandra)](https://aws.amazon.com/keyspaces/) 