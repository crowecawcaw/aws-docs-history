# PERF03-BP02 Evaluate

available configuration options for data store

Understand and evaluate the various features and configuration options available for your
data stores to optimize storage space and performance for your workload.

**Common anti-patterns:**

- You only use one storage type, such as Amazon EBS, for all workloads.
- You use provisioned IOPS for all workloads without real-world testing against all
  storage tiers.
- You are not aware of the configuration options of your chosen data management solution.
- You rely solely on increasing instance size without looking at other available
  configuration options.
- You are not testing the scaling characteristics of your data store.

**Benefits of establishing this best practice:** By exploring and
experimenting with the data store configurations, you may be able to reduce the cost of
infrastructure, improve performance, and lower the effort required to maintain your workloads.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

A workload could have one or more data stores used based on data storage and access
requirements. To optimize your performance efficiency and cost, you must evaluate data access
patterns to determine the appropriate data store configurations. While you explore data store
options, take into consideration various aspects such as the storage options, memory, compute,
read replica, consistency requirements, connection pooling, and caching options. Experiment
with these various configuration options to improve performance efficiency metrics.

### Implementation steps

- Understand the current configurations (like instance type, storage size, or
  database engine version) of your data store.
- Review AWS documentation and best practices to learn about recommended
  configuration options that can help improve the performance of your data store. Key data
  store options to consider are the following:

| Configuration option                                                | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Offloading reads (like read replicas and caching)                   | + For DynamoDB tables, you can offload reads using DAX for caching.<br>+ You can create an Amazon ElastiCache (Redis OSS) cluster and configure your application<br>to read from the cache first, falling back to the database if the<br>requested item is not present.<br>+ Relational databases such as Amazon RDS and Aurora, and provisioned NoSQL<br>databases such as Neptune and Amazon DocumentDB all support adding read replicas<br>to offload the read portions of the workload.<br>+ Serverless databases such as DynamoDB will scale automatically. Ensure<br>that you have enough read capacity units (RCU) provisioned to handle the<br>workload.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Scaling writes (like partition key sharding or introducing a queue) | + For relational databases, you can increase the size of the instance<br>to accommodate an increased workload or increase the provisioned IOPs to<br>allow for an increased throughput to the underlying storage.<br>+ You can also introduce a queue in front of your database rather than<br>writing directly to the database. This pattern allows you to decouple the<br>ingestion from the database and control the flow-rate so the database does<br>not get overwhelmed.<br>+ Batching your write requests rather than creating many short-lived<br>transactions can help improve throughput in high-write volume relational<br>databases.<br>+ Serverless databases like DynamoDB can scale the write throughput<br>automatically or by adjusting the provisioned write capacity units (WCU)<br>depending on the capacity mode.<br>+ You can still run into issues with hot partitions when you reach the<br>throughput limits for a given partition key. This can be mitigated by<br>choosing a more evenly distributed partition key or by write-sharding the<br>partition key. |
| Policies to manage the lifecycle of your datasets                   | + You can use [Amazon S3<br>Lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") to manage your objects throughout their lifecycle. If<br>your access patterns are unknown, changing, or unpredictable, you can<br>use [Amazon S3<br>Intelligent-Tiering](../../../AmazonS3/latest/userguide/intelligent-tiering.md "../../../AmazonS3/latest/userguide/intelligent-tiering.md"), which monitors access patterns and<br>automatically moves objects that have not been accessed to lower-cost<br>access tiers. You can leverage [Amazon S3 Storage<br>Lens](../../../AmazonS3/latest/userguide/storage_lens.md "../../../AmazonS3/latest/userguide/storage_lens.md") metrics to identify optimization opportunities and gaps in<br>lifecycle management.<br>+ [Amazon EFS lifecycle<br>management](../../../efs/latest/ug/lifecycle-management-efs.md "../../../efs/latest/ug/lifecycle-management-efs.md") automatically manages file storage for your file<br>systems.                                |
| Connection management and pooling                                   | + Amazon RDS Proxy can be used with Amazon RDS and Aurora to manage connections to<br>the database.<br>+ Serverless databases such as DynamoDB do not have connections associated<br>with them, but consider the provisioned capacity and automatic scaling<br>policies to deal with spikes in load.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

- Perform experiments and benchmarking in non-production environment to identify
  which configuration option can address your workload requirements.
- Once you have experimented, plan your migration and validate your performance
  metrics.
- Use AWS monitoring (like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")) and optimization (like [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-lens/ "https://aws.amazon.com/s3/storage-lens/")) tools to continuously optimize your
  data store using real-world usage pattern.

## Resources

**Related documents:**

- [Cloud Storage with
  AWS](https://aws.amazon.com/products/storage/?ref=wellarchitected "https://aws.amazon.com/products/storage/?ref=wellarchitected")
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

**Related videos:**

- [AWS
  re:Invent 2023: Improve Amazon Elastic Block Store efficiency and be more cost-efficient](https://www.youtube.com/watch?v=7-CB02rqiuw "https://www.youtube.com/watch?v=7-CB02rqiuw")
- [AWS
  re:Invent 2023: Optimize storage price and performance with Amazon Simple Storage Service](https://www.youtube.com/watch?v=RxgYNrXPOLw "https://www.youtube.com/watch?v=RxgYNrXPOLw")
- [AWS
  re:Invent 2023: Building and optimizing a data lake on Amazon Simple Storage Service](https://www.youtube.com/watch?v=mpQa_Zm1xW8 "https://www.youtube.com/watch?v=mpQa_Zm1xW8")
- [AWS
  re:Invent 2023: What's new with AWS file storage](https://www.youtube.com/watch?v=yXIeIKlTFV0 "https://www.youtube.com/watch?v=yXIeIKlTFV0")
- [AWS
  re:Invent 2023: Dive deep into Amazon DynamoDB](https://www.youtube.com/watch?v=ld-xoehkJuU "https://www.youtube.com/watch?v=ld-xoehkJuU")

**Related examples:**

- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US")
- [Databases for Developers](https://catalog.workshops.aws/db4devs/en-US "https://catalog.workshops.aws/db4devs/en-US")
- [AWS Modern Data Architecture Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US")
- [Amazon EBS Autoscale](https://github.com/awslabs/amazon-ebs-autoscale "https://github.com/awslabs/amazon-ebs-autoscale")
- [Amazon S3 Examples](../../../sdk-for-javascript/v2/developer-guide/s3-examples.md "../../../sdk-for-javascript/v2/developer-guide/s3-examples.md")
- [Amazon DynamoDB
  Examples](https://github.com/aws-samples/aws-dynamodb-examples "https://github.com/aws-samples/aws-dynamodb-examples")
- [AWS Database
  migration samples](https://github.com/aws-samples/aws-database-migration-samples "https://github.com/aws-samples/aws-database-migration-samples")
- [Database
  Modernization Workshop](https://github.com/aws-samples/amazon-rds-purpose-built-workshop "https://github.com/aws-samples/amazon-rds-purpose-built-workshop")
- [Working with parameters on your Amazon RDS for Postgress DB](https://github.com/awsdocs/amazon-rds-user-guide/blob/main/doc_source/Appendix.PostgreSQL.CommonDBATasks.Parameters.md "https://github.com/awsdocs/amazon-rds-user-guide/blob/main/doc_source/Appendix.PostgreSQL.CommonDBATasks.Parameters.md")
