

# 15 – Sustainability implementation guidance
<a name="design-principle-15"></a>

 Think about sustainability as being a non-functional requirement when designing your systems. Determine how necessary sustainability best practices baked into your development lifecycle are, because sustainability best practice can be applied across all workloads, not just data and analytics. 


|   **ID**   |   **Priority**   |   **Best practice**   | 
| --- | --- | --- | 
|  BP 15.1  |  Recommended  |  Define your organization’s current environmental impact  | 
|  BP 15.2  |  Recommended  |  Encourage sustainable thinking  | 
|  BP 15.3  |  Recommended  | Encourage a culture of data minimization | 
|  BP 15.4  |  Recommended  |  Implement data retention processes to remove unnecessary data from your analytics environment  | 
|  BP 15.5  |  Recommended  |  Optimize your data modeling and data storage for efficient data retrieval  | 
|  BP 15.6  |  Recommended  |  Prevent unnecessary data movement between systems and applications  | 
|  BP 15.7  |  Recommended  |  Efficiently manage your analytics infrastructure to reduce underutilized resources  | 

## Resources
<a name="resources"></a>

Documentation and blogs
+  AWS Customer Carbon Footprint: [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) 
+  Quick: [Creating datasets](https://docs.aws.amazon.com/quicksight/latest/user/creating-data-sets.html) 
+  Amazon Athena data types: [Data types in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-types.html) 
+  Amazon Redshift data types: [Data types](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html) 
+  Quick: [Supported data types and values](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-types-and-values.html) 
+  Quick: [Using AWS Lambda with Amazon Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis-example.html) 
+  Amazon Kinesis: [Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html) 
+  AWS Data Migration: [Top 10 Data Migration](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0124-STG_Slide-Deck.pdf) 
+  Amazon S3 Lifecycle Management: [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) 
+  Amazon Kinesis: [Changing the Data Retention Period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html) 
+  AWS-Managed Service Kafka: [Adjust data retention parameters](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html) 
+  Amazon S3 and Amazon Athena: [Partitioning and bucketing in Athena](https://docs.aws.amazon.com/athena/latest/ug/bucketing-vs-partitioning.html) 
+  Amazon Athena: [Partitioning data in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html) 
+  Amazon Redshift development guide: [Database Developer Guide](https://docs.amazonaws.cn/en_us/redshift/latest/dg/redshift-dg.pdf) 
+  Amazon Redshift: [Amazon Redshift Stored Procedures](https://docs.amazonaws.cn/en_us/redshift/latest/dg/stored-procedure-create.html) 
+  Amazon Redshift: [DELETE Statement](https://docs.aws.amazon.com/redshift/latest/dg/r_DELETE.html) 
+  Amazon Redshift: [Ingesting and querying semi-structured data in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/super-overview.html) 
+  Amazon Redshift data types: [Data types](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html) 
+  Amazon Redshift: [Scheduling a query on the Amazon Redshift console](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-schedule-query.html) 
+  Amazon Redshift: [Choose the best sort key](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key.html) 
+  Amazon Redshift Serverless: [Amazon Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/) 
+  Amazon Redshift: [Automate your Amazon Redshift performance tuning with automatic table optimization](https://aws.amazon.com/blogs/big-data/automate-your-amazon-redshift-performance-tuning-with-automatic-table-optimization/) 
+  Amazon Redshift: [Distribution styles](https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html) 
+  Amazon Redshift: [Performance optimization](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html) 
+  Amazon Redshift best practices: [Amazon Redshift best practices for designing tables](https://docs.aws.amazon.com/redshift/latest/dg/c_designing-tables-best-practices.html) 
+  Amazon Redshift: [Getting started with Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html) 
+  Amazon Redshift: [Querying external data using Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) 
+  Amazon Redshift file compression parameter: [File compression parameters](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-file-compression.html) 
+  Amazon Redshift Compression: [Compression encodings](https://docs.aws.amazon.com/redshift/latest/dg/c_Compression_encodings.html) 
+  Amazon Redshift: [Creating materialized views in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html) 
+  Amazon Redshift: [Querying data with federated queries in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/federated-overview.html) 
+  Amazon Redshift compression and encoding: [Amazon Redshift Engineering’s Advanced Table Design Playbook: Compression Encodings](https://aws.amazon.com/blogs/big-data/amazon-redshift-engineerings-advanced-table-design-playbook-compression-encodings/) 
+  Modern data architecture: [Build a modern data architecture on AWS with Amazon AppFlow, AWS Lake Formation, and Amazon Redshift](https://aws.amazon.com/blogs/big-data/build-a-modern-data-architecture-on-aws-with-amazon-appflow-aws-lake-formation-and-amazon-redshift/) 
+  Amazon DynamoDB Compression: [Using data compression](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.Compression.html) 
+  Amazon Athena Compression Support: [Amazon Athena compression support](https://docs.aws.amazon.com/athena/latest/ug/compression-formats.html) 
+  Use Amazon Athena for data virtualization: [Amazon Athena](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc) 
+  Running Presto and Trino on Amazon EMR: [Presto and Trino](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-presto.html) 
+  Use pushdown predicated with Amazon Athena: [Top 10 Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/) 
+  Optimizing EMR Spark with leveraging pushdown predicates: [Optimize Spark performance](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-performance.html) 
+  Amazon Athena: [Using Amazon Athena Federated Query](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html) 
+  EMR-Managed Scaling: [Using EMR-Managed scaling in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-scaling.html) 
+  EMR-Managed Scaling: [Introducing Amazon EMR-Managed Scaling – Automatically Resize Clusters to Lower Cost](https://aws.amazon.com/blogs/big-data/introducing-amazon-emr-managed-scaling-automatically-resize-clusters-to-lower-cost/) 
+  Amazon EMR: [EMR File System (EMRFS)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-fs.html) 
+  Amazon Redshift cluster scaling: [How do I resize an Amazon Redshift cluster?](https://aws.amazon.com/premiumsupport/knowledge-center/resize-redshift-cluster/) 
+  Amazon EMR on EKS: [Amazon EMR on Amazon EKS](https://aws.amazon.com/emr/features/eks/) 
+  Amazon EMR: [Launch a Spark job in a transient EMR cluster using a Lambda function](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/launch-a-spark-job-in-a-transient-emr-cluster-using-a-lambda-function.html) 

 **Whitepapers** 
+  Well-Architected Sustainability: [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/) 
+  Well-Architected Sustainability: [Optimizing your AWS Infrastructure for Sustainability, Part II: Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/) 

 **Demonstrations** 
+  AWS Customer Carbon Footprint overview: [AWS Customer Carbon Footprint Tool Overview](https://www.youtube.com/watch?v=WqhAnLdg3rg) 
+  AWS Data Migration (video): [Top 10 Data Migration Best Practices](https://www.youtube.com/watch?v=i0-pSHQJ7pA) 