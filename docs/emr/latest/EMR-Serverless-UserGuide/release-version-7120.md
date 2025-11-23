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
  - **Iceberg Materialized Views** - Starting Amazon EMR 7.12.0, Amazon EMR Spark supports creation and management of Iceberg Materialized Views (MV)
  - **Hudi Full Table Access** - Starting Amazon EMR 7.12.0, Amazon EMR now supports Full Table Access (FTA) control for Apache Hudi in Apache Spark based on your policies defined in Lake Formation. This feature enables read and write operations from your Amazon EMR Spark jobs on Lake Formation registered tables when the job role has full table access.
  - **Iceberg version upgrade** - Amazon EMR 7.12.0 supports Apache Iceberg version 1.10
