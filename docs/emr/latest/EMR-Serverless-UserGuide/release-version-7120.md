# EMR Serverless 7.12.0

The following table lists the application versions available with
EMR Serverless 7.12.0.

| Application  | Version |
| ------------ | ------- |
| Apache Spark | 3.5.6   |
| Apache Hive  | 3.1.3   |
| Apache Tez   | 0.10.2  |

###### EMR Serverless 7.12.0 release notes

- **New features**
  - **Serverless storage for EMR Serverless** – Amazon EMR serverless introduces serverless storage, with EMR release 7.12 and later, that eliminates local disk provisioning for Apache Spark workloads. EMR Serverless automatically handles intermediate data operation such as shuffle with no storage charges. Serverless storage decouples storage from compute, allowing Spark to release workers immediately when idle rather than keeping them active to preserve temporary data. To learn more, see [aws.amazon.com/serverless-storage-for-emr-serverless](aws.amazon.com/serverless-storage-for-emr-serverless.md "aws.amazon.com/serverless-storage-for-emr-serverless.md").
  - **Iceberg Materialized Views** - Starting Amazon EMR 7.12.0, Amazon EMR Spark supports creation and management of Iceberg Materialized Views (MV)
  - **Hudi Full Table Access** - Starting Amazon EMR 7.12.0, Amazon EMR now supports Full Table Access (FTA) control for Apache Hudi in Apache Spark based on your policies defined in Lake Formation. This feature enables read and write operations from your Amazon EMR Spark jobs on Lake Formation registered tables when the job role has full table access.
  - **Iceberg version upgrade** - Amazon EMR 7.12.0 supports Apache Iceberg version 1.10
