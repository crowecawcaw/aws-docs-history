# `AWS runtime for Apache Spark` (emr-spark-8.0-preview)

The following table lists the application versions available with `AWS runtime for Apache Spark` (emr-spark-8.0-preview).

| Application version information | Application  | Version |
| ------------------------------- | ------------ | ------- |
| Spark                           | 4.0.1-amzn-0 |

###### **`AWS runtime for Apache Spark` (emr-spark-8.0-preview) release notes**

- **Preview release** – This is a preview release of `AWS runtime for Apache Spark` featuring Apache Spark 4.0.1. This preview is available on EMR Serverless only.
- **Regional Availability** - This preview release is available in all AWS Regions where EMR Serverless is available, except China and AWS GovCloud (US) regions.
- **Application version information** - This release ships with the following application versions:
  - AWS SDK for Java 2.35.5, 1.12.792
  - Python **3.9**, 3.11, 3.12
  - Scala 2.13.16
  - AmazonCloudWatchAgent 1.300034.0-amzn-0
  - Delta 4.0.0-amzn-0-spark
  - Iceberg 1.10.0-amzn-spark-0
  - This release ships with Amazon Corretto **17** (built on OpenJDK) by default for applications that support Corretto 17 (JDK 17).

- **Preview limitations** - The following capabilities are not available in this preview release:
  - **Interactive and Integration Features**: SageMaker Unified Studio, EMR Studio integration, Spark Connect, Livy, and JupyterEnterpriseGateway are not supported.
  - **Table Formats and Access Control**: Hudi, Delta Universal Format, and fine-grained access control (FGAC) with row-level or column-level filtering and DDL/DML operators are not supported.
  - **Data Connectors**: spark-sql-kinesis, emr-dynamodb, and spark-redshift connectors are not available.
  - **History Server**: The Persistent Spark History Server is not available in this preview release. Users can still access the live Spark UI to monitor and debug active serverless jobs in real-time.
  - **Specialized Features**: Materialized Views are not available.

- **Preview capabilities** - You can test the following capabilities in this preview release. This preview release is not recommended for production workloads:
  - **SQL Features**: ANSI SQL mode with stricter type handling, SQL PIPE syntax (|>) for chaining operations, VARIANT data type for semi-structured JSON data, SQL scripting with control flow statements and session variables, and SQL user-defined functions.
  - **Streaming Enhancements**: Arbitrary Stateful Processing API v2 with transformWithState operator, State Data Source Reader for queryable streaming state (experimental), and enhanced state store with improved RocksDB changelog checkpointing.
  - **Table Format Support**: Apache Iceberg v3 with VARIANT data type support, AWS S3 Tables integration, and Full Table Access (FTA) with AWS Lake Formation for Iceberg, Delta Lake, and Hive tables.

- **Additional Documentation** - For additional Apache Spark documentation, see [Apache Spark 4.0.1 Release Documentation](https://spark.apache.org/releases/spark-release-4-0-1.html "https://spark.apache.org/releases/spark-release-4-0-1.html").

###### Getting Started

To get started with Apache Spark 4.0.1 preview, create an EMR Serverless application using the AWS CLI:

```
aws emr-serverless create-application --type spark \
  --release-label emr-spark-8.0-preview \
  --region us-east-1 --name spark4-preview
```
