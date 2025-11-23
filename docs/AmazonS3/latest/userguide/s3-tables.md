# Working with Amazon S3 Tables and table buckets

Amazon S3 Tables provide S3 storage that’s optimized for analytics workloads, with features
designed to continuously improve query performance and reduce storage costs for tables.
S3 Tables are purpose-built for storing tabular data, such as daily purchase transactions,
streaming sensor data, or ad impressions. Tabular data represents data in columns and rows,
like in a database table.

The data in S3 Tables is stored in a new bucket type: a
_table bucket_, which stores tables as subresources.
Table buckets support storing tables in the Apache Iceberg format. Using
standard SQL statements, you can query your tables with query engines that support
Iceberg, such as Amazon Athena, Amazon Redshift, and Apache Spark.

###### Topics

- [Features of S3 Tables](#s3-tables-features "#s3-tables-features")
- [Related services](#s3-tables-services "#s3-tables-services")
- [Tutorial: Getting started with S3 Tables](s3-tables-getting-started.md "s3-tables-getting-started.md")
- [Table buckets](s3-tables-buckets.md "s3-tables-buckets.md")
- [S3 Tables maintenance](s3-tables-maintenance-overview.md "s3-tables-maintenance-overview.md")
- [Table namespaces](s3-tables-namespace.md "s3-tables-namespace.md")
- [Tables in S3 table buckets](s3-tables-tables.md "s3-tables-tables.md")
- [Accessing table data](s3-tables-access.md "s3-tables-access.md")
- [S3 Tables AWS Regions, endpoints, and service
  quotas](s3-tables-regions-quotas.md "s3-tables-regions-quotas.md")
- [Making requests to S3 Tables over IPv6](s3-tables-ipv6.md "s3-tables-ipv6.md")
- [Security for S3 Tables](s3-tables-security-overview.md "s3-tables-security-overview.md")
- [Logging and monitoring for S3 Tables](s3-tables-monitoring-overview.md "s3-tables-monitoring-overview.md")

## Features of S3 Tables

**Purpose-built storage for tables**

S3 table buckets are specifically designed for tables. Table buckets
provide higher transactions per second (TPS) and better query throughput
compared to self-managed tables in S3 general purpose buckets. Table buckets
deliver the same durability, availability, and scalability as other Amazon S3
bucket types.

**Built-in support for Apache
Iceberg**

Tables in your table buckets are stored in [Apache Iceberg](https://aws.amazon.com//what-is/apache-iceberg/ "https://aws.amazon.com//what-is/apache-iceberg/")
format. You can query these tables using standard SQL in query engines that
support Iceberg. Iceberg has a variety of
features to optimize query performance, including schema evolution and
partition evolution.

With Iceberg, you can change how your data is organized so
that it can evolve over time without requiring you to rewrite your queries
or rebuild your data structures. Iceberg is designed to help
ensure data consistency and reliability through its support for
transactions. To help you correct issues or perform time travel queries, you
can track how data changes over time and roll back to historical
versions.

**Automated table optimization**

To optimize your tables for querying, S3 continuously performs automatic
maintenance operations, such as compaction, snapshot management, and
unreferenced file removal. These operations increase table performance by
compacting smaller objects into fewer, larger files. Maintenance operations
also reduce your storage costs by cleaning up unused objects. This automated
maintenance streamlines the operation of data lakes at scale by reducing the
need for manual table maintenance. For each table and table bucket, you can
customize maintenance configurations.

**Access management and security**

You can manage access for both table buckets and individual tables with
AWS Identity and Access Management (IAM) and [Service Control Policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in AWS Organizations. S3 Tables uses a
different service namespace than Amazon S3: the _s3tables_
namespace. Therefore, you can design policies specifically for the
S3 Tables service and its resources. You can design policies to grant
access to individual tables, all tables within a table namespace, or entire
table buckets. All Amazon S3 Block Public Access settings are always enabled
for table buckets and cannot be disabled.

**Integration with AWS analytics
services**

You can automatically integrate your Amazon S3 table buckets with Amazon SageMaker Lakehouse through the S3 console. This integration allows AWS analytics services to
automatically discover and access your table data through the AWS Glue Data Catalog. After the integration,
you can work with your tables using analytics services such as Amazon Athena, Amazon Redshift, Quick Suite, and more.
For more information about how the integration works, see [Integrating Amazon S3 Tables with AWS analytics
services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").

## Related services

You can use the following AWS services with S3 Tables to support your specific
analytics applications.

- [**Amazon Athena**](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md") – Athena is an
  interactive query service that you can use to analyze data directly in Amazon S3 by
  using standard SQL. You can also use Athena to interactively run data analytics
  by using Apache Spark without having to plan for, configure, or
  manage resources. When you run Apache Spark applications on
  Athena, you submit Spark code for processing and receive the
  results directly.
- [**AWS Glue**](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") – AWS Glue is a serverless data-integration service that allows
  you to discover, prepare, move, and integrate data from multiple sources. You
  can use AWS Glue for analytics, machine learning (ML), and application development.
  AWS Glue also includes additional productivity and data-operations tooling for
  authoring, running jobs, and implementing business workflows.
- [**Amazon SageMaker Unified Studio**](../../../sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.md "../../../sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.md") – SageMaker Unified Studio delivers an integrated experience for analytics and AI with unified access to all your data. Collaborate and build in SageMaker Unified Studio using familiar AWS tools for SQL analytics, data processing, model development, and generative AI, accelerated by [Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md").
- [**Amazon EMR**](../../../emr/latest/ManagementGuide/emr-what-is-emr.md "../../../emr/latest/ManagementGuide/emr-what-is-emr.md") – Amazon EMR is a managed cluster platform that simplifies running
  big data frameworks, such as Apache Hadoop and Apache
  Spark, on AWS to process and analyze vast amounts of data.
- [**Amazon Redshift**](../../../redshift/latest/mgmt/welcome.md "../../../redshift/latest/mgmt/welcome.md") – Amazon Redshift is a petabyte-scale
  data warehouse service in the cloud. You can use Amazon Redshift Serverless to access and analyze
  data without all of the configurations of a provisioned data warehouse.
  Resources are automatically provisioned and data warehouse capacity is
  intelligently scaled to deliver fast performance for even the most demanding and
  unpredictable workloads. You don't incur charges when the data warehouse is
  idle, so you only pay for what you use. You can load data and start querying
  right away in the Amazon Redshift query editor v2 or in your favorite business intelligence
  (BI) tool.
- [**Quick Suite**](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md") – Quick Suite is a
  business analytics service to build visualizations, perform ad hoc analysis, and
  quickly get business insights from your data. Quick Suite seamlessly discovers
  AWS data sources and delivers fast and responsive query performance by using
  the Quick Suite Super-fast, Parallel, In-Memory, Calculation Engine (SPICE).
- [**AWS Lake Formation**](../../../lake-formation/latest/dg/what-is-lake-formation.md "../../../lake-formation/latest/dg/what-is-lake-formation.md") – Lake Formation is a managed
  service that streamlines the
  process
  to set up, secure, and manage your data lakes. Lake Formation helps you discover your data
  sources and then catalog, cleanse, and transform the data. With Lake Formation, you can
  manage fine-grained access control for your data lake data on Amazon S3 and its
  metadata in AWS Glue Data Catalog.
