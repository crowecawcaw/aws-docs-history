# Connect to data sources

## Overview

Amazon SageMaker Unified Studio notebooks can connect to multiple data sources including Amazon Simple Storage Service, AWS Glue
Data Catalog, Amazon Athena, Amazon Redshift, and third-party sources. You can query data directly from
these sources using SQL cells or Python code.

The notebook interface provides built-in connectors for AWS services and supports custom
connections for external data sources. Data connections are configured at the project level
and shared across notebooks.

## Prerequisites

1. Configured data connections in your Amazon SageMaker Unified Studio project
2. Appropriate IAM permissions to access data sources
3. Network connectivity to external data sources if applicable

## Procedure

To query data from Amazon Simple Storage Service:

1. Create a Python cell and use the AWS SDK to access S3 objects.
2. Use pandas or other libraries to read data from S3 into data frames.
3. Reference the data frame variables in subsequent cells.

To query AWS Glue Data Catalog tables:

1. Create a SQL cell and select the Athena (SQL) connection.
2. Write SQL queries against your cataloged tables.
3. The queries execute using Amazon Athena.
4. Results display as interactive tables below the cell.

To connect to Amazon Redshift:

1. Create a SQL cell and select your Redshift connection from the dropdown.
2. Write SQL queries against your Redshift data warehouse.
3. Execute the queries to retrieve results into the notebook.

To use Amazon Athena for Apache Spark:

1. Create Python cells that use Spark DataFrames for large-scale data processing.
2. Create SQL cells and choose the Athena (Spark) Connection to write SQL queries against your Spark DataFrames.
3. Reference Spark DataFrames by variable name to see rich table visualizations.
4. Access the Spark UI to monitor job progress and performance.

To work with third-party data sources:

1. Configure connections to external sources like Snowflake in your project settings. You
   can [view supported data sources here](../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.md "../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.md").
2. Use SQL cells with the appropriate connection to query external data.
3. Combine data from multiple sources using Python code to join datasets.
