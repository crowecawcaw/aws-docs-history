# Data connections in the lakehouse architecture of Amazon SageMaker

The lakehouse architecture provides a unified approach to managing data connections across AWS services
and enterprise applications. These connections provide a consistent experience for creating,
testing, and exploring data sources, regardless of the underlying data platform.

## Capabilities

With the lakehouse architecture connections, you can do the following:

- Create connections to a variety of data sources, including business applications and external data sources
- Manage data connections in a single place
- Test the connectivity of your data sources to ensure they are working as
  expected
- Browse the metadata and preview the data from your connected sources
- Reuse the same connection across different AWS services like AWS Glue, Amazon Athena
  and Amazon SageMaker AI
- Manage credentials using AWS Secrets Manager
- Authenticate using basic authentication methods such as OAuth2 and IAM

## Supported data sources

The lakehouse architecture connections support several popular data sources, including the
following:

| Supported Data Sources   | Data Source | Type |
| ------------------------ | ----------- | ---- |
| Google BigQuery          | Database    |
| Amazon DocumentDB        | Database    |
| Amazon DynamoDB          | Database    |
| Amazon Redshift          | Database    |
| MySQL                    | Database    |
| PostgreSQL               | Database    |
| SQL Server               | Database    |
| Snowflake                | Database    |
| Oracle                   | Database    |
| Amazon Aurora MySQL      | Database    |
| Amazon Aurora PostgreSQL | Database    |
| Microsoft Azure SQL      | Database    |

###### Note

The lakehouse architecture currently supports lowercase table, column, and database names. For optimal
experience in the lakehouse architecture, ensure that all database identifiers are in lowercase.

## Use the lakehouse architecture connections

After you've added data sources to the lakehouse architecture, you can use it in various AWS
services:

- Amazon SageMaker Unified Studio – Browse metadata, preview sample data, and run SQL queries against the
  connected data.
- AWS Glue – Use the connection for ETL jobs and crawlers.
- Amazon Athena – Query data directly using Athena's federated query capabilities. For
  more information, see [Register federated catalogs in
  Amazon Athena](../../../athena/latest/ug/gdc-register-federated.md "../../../athena/latest/ug/gdc-register-federated.md").
- Amazon SageMaker AI – Access data for building machine learning models.

## Understanding resources for the lakehouse architecture of Amazon SageMaker

When you create a connection in Amazon SageMaker Unified Studio, several resources are created in your AWS
account(s) behind the scenes. These resources can include:

- AWS Glue connection - A connection object is created in the AWS Glue crawler. This stores the
  core connection information and is used by various AWS services.
- Athena data catalog - For connections that will be used with Athena , an Athena data
  catalog is created. This allows Athena to query the external data source.
- AWS Glue data catalog entries - Databases, tables, and schemas from your external data
  source are registered in the Data Catalog. This enables AWS services to understand the
  structure of your external data.
- Lambda (for Athena Federated Query) - For some data sources, a Lambda function is
  created to facilitate federated queries. This function acts as a bridge between Athena
  and the external data source.

To view these resources, access the respective AWS service consoles (AWS Glue, Athena, IAM,
etc.) in the AWS account associated with your Amazon SageMaker Unified Studio project.

In these consoles, look for resources with names that include your Amazon SageMaker Unified Studio project ID or
connection name.

For more information about how to create a data connection and explore a connected data
source, see .
