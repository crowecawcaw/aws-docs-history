

# PERF03-BP02 Evaluate available configuration options for data store
<a name="perf_data_evaluate_configuration_options_data_store"></a>

 Understand and evaluate the various features and configuration options available for your data stores to optimize storage space and performance for your workload. 

 **Common anti-patterns:** 
+  You only use one storage type, such as Amazon EBS, for all workloads. 
+  You use provisioned IOPS for all workloads without real-world testing against all storage tiers. 
+  You are not aware of the configuration options of your chosen data management solution. 
+  You rely solely on increasing instance size without looking at other available configuration options. 
+  You are not testing the scaling characteristics of your data store. 

 **Benefits of establishing this best practice:** By exploring and experimenting with the data store configurations, you may be able to reduce the cost of infrastructure, improve performance, and lower the effort required to maintain your workloads. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A workload could have one or more data stores used based on data storage and access requirements. To optimize your performance efficiency and cost, you must evaluate data access patterns to determine the appropriate data store configurations. While you explore data store options, take into consideration various aspects such as the storage options, memory, compute, read replica, consistency requirements, connection pooling, and caching options. Experiment with these various configuration options to improve performance efficiency metrics. 

### Implementation steps
<a name="implementation-steps"></a>
+  Understand the current configurations (like instance type, storage size, or database engine version) of your data store. 
+  Review AWS documentation and best practices to learn about recommended configuration options that can help improve the performance of your data store. Key data store options to consider are the following: 


<table>
<thead>
  <tr><th> Configuration option </th><th> Examples </th></tr>
</thead>
<tbody>
  <tr><td> Offloading reads (like read replicas and caching) </td><td> <ul><li>  For DynamoDB tables, you can offload reads using DAX for caching.  </li><li>  You can create an Amazon ElastiCache (Redis OSS) cluster and configure your application to read from the cache first, falling back to the database if the requested item is not present.  </li><li>  Relational databases such as Amazon RDS and Aurora, and provisioned NoSQL databases such as Neptune and Amazon DocumentDB all support adding read replicas to offload the read portions of the workload.  </li><li>  Serverless databases such as DynamoDB will scale automatically. Ensure that you have enough read capacity units (RCU) provisioned to handle the workload.  </li></ul> </td></tr>
  <tr><td> Scaling writes (like partition key sharding or introducing a queue) </td><td> <ul><li>  For relational databases, you can increase the size of the instance to accommodate an increased workload or increase the provisioned IOPs to allow for an increased throughput to the underlying storage.  </li><li>  You can also introduce a queue in front of your database rather than writing directly to the database. This pattern allows you to decouple the ingestion from the database and control the flow-rate so the database does not get overwhelmed.   </li><li>  Batching your write requests rather than creating many short-lived transactions can help improve throughput in high-write volume relational databases.  </li><li>  Serverless databases like DynamoDB can scale the write throughput automatically or by adjusting the provisioned write capacity units (WCU) depending on the capacity mode.   </li><li>  You can still run into issues with hot partitions when you reach the throughput limits for a given partition key. This can be mitigated by choosing a more evenly distributed partition key or by write-sharding the partition key.   </li></ul> </td></tr>
  <tr><td> Policies to manage the lifecycle of your datasets </td><td> <ul><li>  You can use <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html">Amazon S3 Lifecycle</a> to manage your objects throughout their lifecycle. If your access patterns are unknown, changing, or unpredictable, you can use <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html">Amazon S3 Intelligent-Tiering</a>, which monitors access patterns and automatically moves objects that have not been accessed to lower-cost access tiers. You can leverage <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html">Amazon S3 Storage Lens</a> metrics to identify optimization opportunities and gaps in lifecycle management.  </li><li>  <a href="https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html">Amazon EFS lifecycle management</a> automatically manages file storage for your file systems.  </li></ul> </td></tr>
  <tr><td> Connection management and pooling </td><td> <ul><li>  Amazon RDS Proxy can be used with Amazon RDS and Aurora to manage connections to the database.   </li><li>  Serverless databases such as DynamoDB do not have connections associated with them, but consider the provisioned capacity and automatic scaling policies to deal with spikes in load.  </li></ul> </td></tr>
</tbody>
</table>

+  Perform experiments and benchmarking in non-production environment to identify which configuration option can address your workload requirements. 
+  Once you have experimented, plan your migration and validate your performance metrics. 
+  Use AWS monitoring (like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)) and optimization (like [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-lens/)) tools to continuously optimize your data store using real-world usage pattern. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Cloud Storage with AWS](https://aws.amazon.com/products/storage/?ref=wellarchitected) 
+  [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) 
+  [Amazon EC2 Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html) 
+  [Amazon EFS: Amazon EFS Performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html) 
+  [Amazon FSx for Lustre Performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html) 
+  [Amazon FSx for Windows File Server Performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html) 
+  [Amazon Glacier: Amazon Glacier Documentation](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html) 
+  [Amazon S3: Request Rate and Performance Considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html) 
+  [Amazon EBS I/O Characteristics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html) 
+  [Cloud Databases with AWS ](https://aws.amazon.com/products/databases/?ref=wellarchitected) 
+  [AWS Database Caching ](https://aws.amazon.com/caching/database-caching/?ref=wellarchitected) 
+  [DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/?ref=wellarchitected) 
+  [Amazon Aurora best practices ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html?ref=wellarchitected) 
+  [Amazon Redshift performance ](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html?ref=wellarchitected) 
+  [Amazon Athena top 10 performance tips ](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected) 
+  [Amazon Redshift Spectrum best practices ](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/?ref=wellarchitected) 
+  [Amazon DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html?ref=wellarchitected) 

 **Related videos:** 
+  [AWS re:Invent 2023: Improve Amazon Elastic Block Store efficiency and be more cost-efficient](https://www.youtube.com/watch?v=7-CB02rqiuw) 
+  [AWS re:Invent 2023: Optimize storage price and performance with Amazon Simple Storage Service](https://www.youtube.com/watch?v=RxgYNrXPOLw) 
+  [AWS re:Invent 2023: Building and optimizing a data lake on Amazon Simple Storage Service](https://www.youtube.com/watch?v=mpQa_Zm1xW8) 
+  [AWS re:Invent 2023: What's new with AWS file storage](https://www.youtube.com/watch?v=yXIeIKlTFV0) 
+  [AWS re:Invent 2023: Dive deep into Amazon DynamoDB](https://www.youtube.com/watch?v=ld-xoehkJuU) 

 **Related examples:** 
+  [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US) 
+  [Databases for Developers](https://catalog.workshops.aws/db4devs/en-US) 
+  [AWS Modern Data Architecture Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US) 
+  [Amazon EBS Autoscale](https://github.com/awslabs/amazon-ebs-autoscale) 
+  [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html) 
+  [Amazon DynamoDB Examples](https://github.com/aws-samples/aws-dynamodb-examples) 
+  [AWS Database migration samples](https://github.com/aws-samples/aws-database-migration-samples) 
+  [Database Modernization Workshop](https://github.com/aws-samples/amazon-rds-purpose-built-workshop) 
+  [Working with parameters on your Amazon RDS for Postgress DB](https://github.com/awsdocs/amazon-rds-user-guide/blob/main/doc_source/Appendix.PostgreSQL.CommonDBATasks.Parameters.md) 