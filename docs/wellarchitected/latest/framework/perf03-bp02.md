

# PERF03-BP02 Evaluate available configuration options for data store

 A data store's default configuration rarely matches a specific workload. Every store exposes options that trade cost, capacity, consistency, and speed against one another. Evaluate and test the configuration before you rely on it. 

 **Desired outcome:** 
+  You have evaluated the configuration options of each data store against your workload's access patterns. 
+  You run a configuration tuned to your requirements rather than the default settings. 
+  You have tested scaling, backup, and restore behavior before relying on a configuration in production. 
+  You refine configuration continuously from real usage metrics. 

 **Common anti-patterns:** 
+  Teams use one storage type for every workload regardless of its access pattern. 
+  Teams provision maximum IOPS everywhere without testing against lower-cost tiers. 
+  Teams remain unaware of the configuration options their chosen store exposes. 
+  Teams scale only by increasing instance size and ignore other options. 
+  Teams never test how the store behaves as load grows. 
+  Teams overlook backup and restore time, and the time to reach full performance after a restore. 

 **Benefits of establishing this best practice:** 
+  Performance improves because configuration matches the workload's read, write, and consistency needs. 
+  Infrastructure costs fall when you size to real demand instead of worst-case defaults. 
+  Recovery stays predictable because you have measured backup and restore behavior. 
+  Maintenance effort drops as auto-tuning and managed features take over routine work. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Effective tuning depends on your workload's read-to-write ratio, consistency tolerance, and how demand changes over time. 

 Reads and writes scale by different mechanisms, and conflating them leads to over-provisioning. You can offload reads with read replicas, a cache, or geo-distributed copies. Replicas introduce replication lag, so route reads that require read-after-write consistency to the primary. For writes, you can increase instance size, raise provisioned throughput, or batch requests. You can also place a queue in front of the store to decouple ingestion from persistence. A queue smooths spikes but adds latency and another component to operate. For key-value stores, write throughput often collapses on a *hot partition*, where one partition key receives a disproportionate share of traffic. A more evenly distributed key, write-sharding, or adaptive capacity addresses this, but only if you design for it before the traffic arrives. 

 Lifecycle and tiering options change the cost and performance of data as it ages. Frequently accessed data belongs in fast, higher-cost storage, while cold data can move to lower-cost tiers automatically. When access patterns are unknown or shifting, automatic tiering handles the placement decisions, though it adds monitoring cost and, for retrieval from cold tiers, latency. Connection handling is a separate failure mode. Relational databases have finite connection slots, and a workload that opens connections without pooling can exhaust them under load, which looks like a performance problem but is a configuration problem. Serverless stores remove connection limits but shift the tuning to capacity modes and scaling policies. 

 Measure recovery behavior: backup time, restore time, and the time a store needs to reach full performance after a restore. A store that restores quickly but serves cold, slow reads for an hour afterward might not meet your recovery objective. Test candidate configurations in a non-production environment against representative load, then promote the configuration that meets your targets. 

 [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-lens/) surface usage patterns that guide tuning. [Amazon RDS Performance Insights](https://aws.amazon.com/cloudwatch/features/analytics-and-insights/) and [Amazon DynamoDB CloudWatch Contributor Insights](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/contributorinsights_HowItWorks.html) expose access and query hotspots. Auto-tuning features such as [Amazon Aurora query plan management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.overview.html), [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/), and [Cruise Control for Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/cruise-control.html) reduce ongoing manual tuning. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Baseline the current configuration:** Record the current settings of each data store, including instance type, storage size and type, engine version, capacity mode, and consistency settings. This baseline is the reference point for every change you test. 

1.  **Evaluate read-offloading options:** For read-heavy workloads, assess read replicas, an in-memory cache, or geo-distributed copies such as [Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) or [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/global-tables/). Confirm that your consistency requirements tolerate replication lag before you route reads away from the primary. 

1.  **Evaluate write-scaling options:** For write-heavy workloads, weigh instance sizing, provisioned throughput, request batching, and queue-based decoupling. For key-value stores, design the partition key to avoid hot partitions and enable adaptive capacity where available. 

1.  **Apply lifecycle and tiering policies:** Configure automatic data tiering to match cost and performance to how data ages, using [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html), [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html), [Amazon EFS lifecycle management](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html), [Amazon ElastiCache data tiering](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html), or [Amazon MSK tiered storage](https://docs.aws.amazon.com/msk/latest/developerguide/msk-tiered-storage.html). 

1.  **Manage connections and pooling:** For connection-limited databases, add connection pooling with a service such as [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html). For serverless stores, tune capacity and scaling policies instead of connection counts. 

1.  **Benchmark in a non-production environment and plan migration:** Load representative data and run candidate configurations against realistic load. Measure performance, scaling, and backup and restore time, including time to full performance after a restore, then plan the migration and validate metrics against your targets. 

1.  **Monitor and auto-tune continuously:** Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-lens/), and [Amazon RDS Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.html) to refine configuration against real usage, and enable auto-tuning features where they fit the workload. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF03-BP01 Use a purpose-built data store that best supports your data access and storage requirements](perf03-bp01.md) 
+  [PERF03-BP03 Collect and record data store performance metrics](perf03-bp03.md) 
+  [PERF03-BP04 Implement strategies to improve query performance in data store](perf03-bp04.md) 

 **Related documents:** 
+  [Cloud storage with AWS](https://aws.amazon.com/products/storage/) 
+  [Cloud databases with AWS](https://aws.amazon.com/products/databases/) 
+  [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) 
+  [Amazon EC2 storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html) 
+  [Amazon EBS I/O characteristics](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-io-characteristics.html) 
+  [Provisioned rate for volume initialization for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html#volume-initialization-rate) 
+  [Amazon EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html) 
+  [Amazon FSx for Lustre performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html) 
+  [Amazon FSx for Windows File Server performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html) 
+  [Amazon S3 request rate and performance considerations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html) 
+  [Amazon Aurora best practices](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.BestPractices.html) 
+  [Amazon Redshift performance](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html) 
+  [Amazon DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html) 

 **Related examples:** 
+  [Amazon DynamoDB examples](https://github.com/aws-samples/aws-dynamodb-examples) 

 **Related workshops:** 
+  [AWS purpose-built databases workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US) 
+  [AWS modern data architecture immersion day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon EBS](https://aws.amazon.com/ebs/) 
+  [Amazon EFS](https://aws.amazon.com/efs/) 
+  [Amazon FSx](https://aws.amazon.com/fsx/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon RDS](https://aws.amazon.com/rds/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 