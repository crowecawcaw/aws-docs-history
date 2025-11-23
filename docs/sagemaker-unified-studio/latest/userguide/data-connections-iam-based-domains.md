# Data and catalog connections in IAM-based

domains

Amazon SageMaker Unified Studio notebooks can connect to multiple data sources including Amazon S3, AWS Glue Data
Catalog, Amazon Athena, Amazon Redshift, and third-party sources. You can query data directly from
these sources using SQL cells or Python code. The notebook interface provides built-in
connectors for AWS services and supports custom connections for external data sources. Data
connections are configured at the project level and shared across notebooks.

## Prerequisites

1. Configured data connections in your Amazon SageMaker Unified Studio project
2. Appropriate IAM permissions to access data sources
3. Network connectivity to external data sources if applicable

## Supported data connections

Amazon SageMaker Unified Studio supports the following data connections for IAM-based domains:

### Databases and data warehouses

- Amazon DocumentDB
- Amazon DynamoDB
- Amazon Redshift
- Aurora MySQL
- Aurora PostgreSQL
- Azure SQL
- Google BigQuery
- Microsoft SQL Server
- MySQL
- Oracle
- PostgreSQL
- Snowflake

### Storage

- Amazon S3

## AWS resources created by

connections

When you create a connection in Amazon SageMaker Unified Studio, the following resources are created in your
AWS account(s) behind the scenes:

- AWS Glue connection - a connection object that stores core connection
  information.

Those resources are visible in the account where Amazon SageMaker Unified Studio domain is hosted and you can
discover and describe them through Console or API/SDK/CLI of the corresponding service (in
this case - AWS Glue).
