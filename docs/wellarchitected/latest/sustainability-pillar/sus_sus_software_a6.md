# SUS03-BP05 Use software patterns and architectures that best

support data access and storage patterns

Understand how data is used within your workload, consumed by your users, transferred, and stored.
Use software patterns and architectures that best support data access and storage to minimize the compute,
networking, and storage resources required to support the workload.

**Common anti-patterns:**

- You assume that all workloads have similar data storage and access patterns.
- You only use one tier of storage, assuming all workloads fit within that tier.
- You assume that data access patterns will stay consistent over time.
- Your architecture supports a potential high data access burst, which results in the resources remaining idle most of the time.

**Benefits of establishing this best practice:** Selecting and optimizing your architecture based on data access and storage patterns will help decrease development complexity and increase overall utilization. Understanding when to use global tables, data partitioning, and caching will help you decrease operational overhead and scale based on your workload needs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To improve long-term workload sustainability, use architecture patterns that support data access and storage characteristics for your workload. These patterns help you efficiently retrieve and process data. For example, you can use [modern data architecture on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/ "https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/") with purpose-built services optimized for your unique analytics use cases. These architecture patterns allow for efficient data processing and reduce the resource usage.

### Implementation steps

- **Understand data characteristics:** Analyze your data characteristics and access patterns to identify the correct configuration for your cloud resources. Key characteristics to consider include:
  - **Data type:** structured, semi-structured, unstructured
  - **Data growth:** bounded, unbounded
  - **Data durability:** persistent, ephemeral, transient
  - **Access patterns** reads or writes, update frequency, spiky, or consistent

- **Use optimal architecture patterns:** Use architecture patterns that best support data access and storage patterns.
  - [Patterns for enabling data persistence](../../../prescriptive-guidance/latest/modernization-data-persistence/enabling-patterns.md "../../../prescriptive-guidance/latest/modernization-data-persistence/enabling-patterns.md")
  - [Let’s Architect! Modern data architectures](https://aws.amazon.com/blogs/architecture/lets-architect-modern-data-architectures/ "https://aws.amazon.com/blogs/architecture/lets-architect-modern-data-architectures/")
  - [Databases on AWS: The Right Tool for the Right Job](https://www.youtube.com/watch?v=-pb-DkD6cWg "https://www.youtube.com/watch?v=-pb-DkD6cWg")

- **Use purpose-built services:** Use technologies that are fit-for-purpose.
  - Use technologies that work natively with compressed data.
    - [Athena Compression Support file formats](../../../athena/latest/ug/compression-formats.md "../../../athena/latest/ug/compression-formats.md")
    - [Format Options for ETL Inputs and Outputs in AWS Glue](../../../glue/latest/dg/aws-glue-programming-etl-format.md "../../../glue/latest/dg/aws-glue-programming-etl-format.md")
    - [Loading compressed data files from Amazon S3 with Amazon Redshift](../../../redshift/latest/dg/t_loading-gzip-compressed-data-files-from-S3.md "../../../redshift/latest/dg/t_loading-gzip-compressed-data-files-from-S3.md")

  - Use purpose-built [analytics services](https://aws.amazon.com/big-data/datalakes-and-analytics/?nc2=h_ql_prod_an_a "https://aws.amazon.com/big-data/datalakes-and-analytics/?nc2=h_ql_prod_an_a") for data processing in your architecture. For detail on AWS purpose-built analytics services, see [AWS re:Invent 2022 - Building modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o "https://www.youtube.com/watch?v=Uk2CqEt5f0o").
  - Use the database engine that best supports your dominant query pattern. Manage your database indexes for efficient querying. For further details, see [AWS Databases](https://aws.amazon.com/products/databases/ "https://aws.amazon.com/products/databases/") and [AWS re:Invent 2022 - Modernize apps with purpose-built databases](https://www.youtube.com/watch?v=V-DiplATdi0 "https://www.youtube.com/watch?v=V-DiplATdi0").

- **Minimize data transfer:** Select network protocols that reduce the amount of network capacity consumed in your architecture.

## Resources

**Related documents:**

- [COPY
  from columnar data formats with Amazon Redshift](../../../redshift/latest/dg/copy-usage_notes-copy-from-columnar.md "../../../redshift/latest/dg/copy-usage_notes-copy-from-columnar.md")
- [Converting
  Your Input Record Format in Firehose](../../../firehose/latest/dev/record-format-conversion.md "../../../firehose/latest/dev/record-format-conversion.md")
- [Improve
  query performance on Amazon Athena by Converting to Columnar
  Formats](../../../athena/latest/ug/convert-to-columnar.md "../../../athena/latest/ug/convert-to-columnar.md")
- [Monitoring
  DB load with Performance Insights on Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.md")
- [Monitoring
  DB load with Performance Insights on Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md")
- [Amazon S3 Intelligent-Tiering storage class](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/ "https://aws.amazon.com/s3/storage-classes/intelligent-tiering/")
- [Build a CQRS event store with Amazon DynamoDB](https://aws.amazon.com/blogs/database/build-a-cqrs-event-store-with-amazon-dynamodb/ "https://aws.amazon.com/blogs/database/build-a-cqrs-event-store-with-amazon-dynamodb/")

**Related videos:**

- [AWS re:Invent 2022 - Building data mesh architectures on AWS](https://www.youtube.com/watch?v=nGRvlobeM_U "https://www.youtube.com/watch?v=nGRvlobeM_U")
- [AWS re:Invent 2023 - Deep dive into Amazon Aurora and its innovations](https://www.youtube.com/watch?v=je6GCOZ22lI "https://www.youtube.com/watch?v=je6GCOZ22lI")
- [AWS re:Invent 2023 - Improve Amazon EBS efficiency and be more cost-efficient](https://www.youtube.com/watch?v=7-CB02rqiuw "https://www.youtube.com/watch?v=7-CB02rqiuw")
- [AWS re:Invent 2023 - Optimizing storage price and performance with Amazon S3](https://www.youtube.com/watch?v=RxgYNrXPOLw "https://www.youtube.com/watch?v=RxgYNrXPOLw")
- [AWS re:Invent 2023 - Building and optimizing a data lake on Amazon S3](https://www.youtube.com/watch?v=mpQa_Zm1xW8 "https://www.youtube.com/watch?v=mpQa_Zm1xW8")
- [AWS re:Invent 2023 - Advanced event-driven patterns with Amazon EventBridge](https://www.youtube.com/watch?v=6X4lSPkn4ps "https://www.youtube.com/watch?v=6X4lSPkn4ps")

**Related examples:**

- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US")
- [AWS Modern Data Architecture Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US")
- [Build a Data Mesh on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US")
