# 15 – Sustainability implementation guidance

Think about sustainability as being a non-functional requirement
when designing your systems. Determine how necessary
sustainability best practices baked into your development
lifecycle are, because sustainability best practice can be
applied across all workloads, not just data and analytics.

| **ID**  | **Priority** | **Best practice**                                                                                |
| ------- | ------------ | ------------------------------------------------------------------------------------------------ |
| BP 15.1 | Recommended  | Define your organization’s current environmental impact                                          |
| BP 15.2 | Recommended  | Encourage sustainable thinking                                                                   |
| BP 15.3 | Recommended  | Encourage a culture of data minimization                                                         |
| BP 15.4 | Recommended  | Implement data retention processes to remove unnecessary<br>data from your analytics environment |
| BP 15.5 | Recommended  | Optimize your data modeling and data storage for<br>efficient data retrieval                     |
| BP 15.6 | Recommended  | Prevent unnecessary data movement between systems and<br>applications                            |
| BP 15.7 | Recommended  | Efficiently manage your analytics infrastructure to<br>reduce underutilized resources            |

## Resources

Documentation and blogs

- AWS Customer Carbon Footprint:
  [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/ "https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/")
- Quick Suite: [Creating datasets](../../../quicksight/latest/user/creating-data-sets.md "../../../quicksight/latest/user/creating-data-sets.md")
- Amazon Athena data types:
  [Data
  types in Amazon Athena](../../../athena/latest/ug/data-types.md "../../../athena/latest/ug/data-types.md")
- Amazon Redshift data types:
  [Data
  types](../../../redshift/latest/dg/c_Supported_data_types.md "../../../redshift/latest/dg/c_Supported_data_types.md")
- Quick Suite:
  [Supported
  data types and values](../../../quicksight/latest/user/supported-data-types-and-values.md "../../../quicksight/latest/user/supported-data-types-and-values.md")
- Quick Suite: [Using AWS Lambda with Amazon Kinesis](../../../lambda/latest/dg/with-kinesis-example.md "../../../lambda/latest/dg/with-kinesis-example.md")
- Amazon Kinesis: [Monitoring the Amazon Kinesis Data Streams
  Service with Amazon CloudWatch](../../../streams/latest/dev/monitoring-with-cloudwatch.md "../../../streams/latest/dev/monitoring-with-cloudwatch.md")
- AWS Data Migration:
  [Top
  10 Data Migration](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0124-STG_Slide-Deck.pdf "https://pages.awscloud.com/rs/112-TZM-766/images/2020_0124-STG_Slide-Deck.pdf")
- Amazon S3 Lifecycle Management: [Managing your storage
  lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md")
- Amazon Kinesis: [Changing the Data Retention
  Period](../../../streams/latest/dev/kinesis-extended-retention.md "../../../streams/latest/dev/kinesis-extended-retention.md")
- AWS-Managed Service Kafka: [Adjust data retention
  parameters](../../../msk/latest/developerguide/bestpractices.md "../../../msk/latest/developerguide/bestpractices.md")
- Amazon S3 and Amazon Athena: [Partitioning and bucketing in Athena](../../../athena/latest/ug/bucketing-vs-partitioning.md "../../../athena/latest/ug/bucketing-vs-partitioning.md")
- Amazon Athena: [Partitioning data in Amazon Athena](../../../athena/latest/ug/partitions.md "../../../athena/latest/ug/partitions.md")
- Amazon Redshift development guide: [Database
  Developer Guide](https://docs.amazonaws.cn/en_us/redshift/latest/dg/redshift-dg.pdf "https://docs.amazonaws.cn/en_us/redshift/latest/dg/redshift-dg.pdf")
- Amazon Redshift: [Amazon Redshift Stored Procedures](https://docs.amazonaws.cn/en_us/redshift/latest/dg/stored-procedure-create.html "https://docs.amazonaws.cn/en_us/redshift/latest/dg/stored-procedure-create.html")
- Amazon Redshift: [DELETE
  Statement](../../../redshift/latest/dg/r_DELETE.md "../../../redshift/latest/dg/r_DELETE.md")
- Amazon Redshift: [Ingesting and querying semi-structured data in Amazon Redshift](../../../redshift/latest/dg/super-overview.md "../../../redshift/latest/dg/super-overview.md")
- Amazon Redshift data types:
  [Data
  types](../../../redshift/latest/dg/c_Supported_data_types.md "../../../redshift/latest/dg/c_Supported_data_types.md")
- Amazon Redshift: [Scheduling a query on the
  Amazon Redshift console](../../../redshift/latest/mgmt/query-editor-schedule-query.md "../../../redshift/latest/mgmt/query-editor-schedule-query.md")
- Amazon Redshift: [Choose the best sort key](../../../redshift/latest/dg/c_best-practices-sort-key.md "../../../redshift/latest/dg/c_best-practices-sort-key.md")
- Amazon Redshift Serverless:
  [Amazon Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/ "https://aws.amazon.com/redshift/redshift-serverless/")
- Amazon Redshift: [Automate your Amazon Redshift performance tuning with automatic table optimization](https://aws.amazon.com/blogs/big-data/automate-your-amazon-redshift-performance-tuning-with-automatic-table-optimization/ "https://aws.amazon.com/blogs/big-data/automate-your-amazon-redshift-performance-tuning-with-automatic-table-optimization/")
- Amazon Redshift: [Distribution styles](../../../redshift/latest/dg/c_choosing_dist_sort.md "../../../redshift/latest/dg/c_choosing_dist_sort.md")
- Amazon Redshift: [Performance optimization](../../../redshift/latest/dg/c_challenges_achieving_high_performance_queries.md "../../../redshift/latest/dg/c_challenges_achieving_high_performance_queries.md")
- Amazon Redshift best practices:
  [Amazon Redshift best practices for designing tables](../../../redshift/latest/dg/c_designing-tables-best-practices.md "../../../redshift/latest/dg/c_designing-tables-best-practices.md")
- Amazon Redshift:
  [Getting
  started with Amazon Redshift Spectrum](../../../redshift/latest/dg/c-getting-started-using-spectrum.md "../../../redshift/latest/dg/c-getting-started-using-spectrum.md")
- Amazon Redshift: [Querying external data using Amazon Redshift Spectrum](../../../redshift/latest/dg/c-using-spectrum.md "../../../redshift/latest/dg/c-using-spectrum.md")
- Amazon Redshift file compression parameter: [File compression
  parameters](../../../redshift/latest/dg/copy-parameters-file-compression.md "../../../redshift/latest/dg/copy-parameters-file-compression.md")
- Amazon Redshift Compression: [Compression encodings](../../../redshift/latest/dg/c_Compression_encodings.md "../../../redshift/latest/dg/c_Compression_encodings.md")
- Amazon Redshift: [Creating materialized views in
  Amazon Redshift](../../../redshift/latest/dg/materialized-view-overview.md "../../../redshift/latest/dg/materialized-view-overview.md")
- Amazon Redshift: [Querying data with federated queries in
  Amazon Redshift](../../../redshift/latest/dg/federated-overview.md "../../../redshift/latest/dg/federated-overview.md")
- Amazon Redshift compression and encoding: [Amazon Redshift Engineering’s Advanced Table Design Playbook: Compression Encodings](https://aws.amazon.com/blogs/big-data/amazon-redshift-engineerings-advanced-table-design-playbook-compression-encodings/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-engineerings-advanced-table-design-playbook-compression-encodings/")
- Modern data architecture: [Build a modern data architecture on AWS with Amazon AppFlow, AWS Lake Formation, and Amazon Redshift](https://aws.amazon.com/blogs/big-data/build-a-modern-data-architecture-on-aws-with-amazon-appflow-aws-lake-formation-and-amazon-redshift/ "https://aws.amazon.com/blogs/big-data/build-a-modern-data-architecture-on-aws-with-amazon-appflow-aws-lake-formation-and-amazon-redshift/")
- Amazon DynamoDB Compression: [Using data compression](../../../amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.md "../../../amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.md")
- Amazon Athena Compression Support: [Amazon Athena compression support](../../../athena/latest/ug/compression-formats.md "../../../athena/latest/ug/compression-formats.md")
- Use Amazon Athena for data virtualization: [Amazon Athena](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc")
- Running Presto and Trino on Amazon EMR: [Presto and Trino](../../../emr/latest/ReleaseGuide/emr-presto.md "../../../emr/latest/ReleaseGuide/emr-presto.md")
- Use pushdown predicated with Amazon Athena: [Top 10
  Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/ "https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/")
- Optimizing EMR Spark with leveraging pushdown predicates: [Optimize Spark
  performance](../../../emr/latest/ReleaseGuide/emr-spark-performance.md "../../../emr/latest/ReleaseGuide/emr-spark-performance.md")
- Amazon Athena: [Using Amazon Athena Federated
  Query](../../../athena/latest/ug/connect-to-a-data-source.md "../../../athena/latest/ug/connect-to-a-data-source.md")
- EMR-Managed Scaling:
  [Using
  EMR-Managed scaling in Amazon EMR](../../../emr/latest/ManagementGuide/emr-managed-scaling.md "../../../emr/latest/ManagementGuide/emr-managed-scaling.md")
- EMR-Managed Scaling:
  [Introducing
  Amazon EMR-Managed Scaling – Automatically Resize Clusters to
  Lower Cost](https://aws.amazon.com/blogs/big-data/introducing-amazon-emr-managed-scaling-automatically-resize-clusters-to-lower-cost/ "https://aws.amazon.com/blogs/big-data/introducing-amazon-emr-managed-scaling-automatically-resize-clusters-to-lower-cost/")
- Amazon EMR:
  [EMR
  File System (EMRFS)](../../../emr/latest/ReleaseGuide/emr-fs.md "../../../emr/latest/ReleaseGuide/emr-fs.md")
- Amazon Redshift cluster scaling:
  [How
  do I resize an Amazon Redshift cluster?](https://aws.amazon.com/premiumsupport/knowledge-center/resize-redshift-cluster/ "https://aws.amazon.com/premiumsupport/knowledge-center/resize-redshift-cluster/")
- Amazon EMR on EKS:
  [Amazon EMR on Amazon EKS](https://aws.amazon.com/emr/features/eks/ "https://aws.amazon.com/emr/features/eks/")
- Amazon EMR:
  [Launch
  a Spark job in a transient EMR cluster using a Lambda
  function](../../../prescriptive-guidance/latest/patterns/launch-a-spark-job-in-a-transient-emr-cluster-using-a-lambda-function.md "../../../prescriptive-guidance/latest/patterns/launch-a-spark-job-in-a-transient-emr-cluster-using-a-lambda-function.md")
-

**Whitepapers**

- Well-Architected Sustainability:
  [Optimizing
  your AWS Infrastructure for Sustainability, Part I:
  Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/ "https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/")
- Well-Architected Sustainability:
  [Optimizing
  your AWS Infrastructure for Sustainability, Part II:
  Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/ "https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/")

**Demonstrations**

- AWS Customer Carbon Footprint overview: [AWS Customer Carbon Footprint Tool
  Overview](https://www.youtube.com/watch?v=WqhAnLdg3rg "https://www.youtube.com/watch?v=WqhAnLdg3rg")
- AWS Data Migration (video): [Top 10 Data Migration Best
  Practices](https://www.youtube.com/watch?v=i0-pSHQJ7pA "https://www.youtube.com/watch?v=i0-pSHQJ7pA")
