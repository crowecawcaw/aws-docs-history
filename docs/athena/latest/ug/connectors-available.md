

# Available data source connectors
<a name="connectors-available"></a>

This section lists prebuilt Athena data source connectors that you can use to query a variety of data sources external to Amazon S3. To use a connector in your Athena queries, configure it and deploy it to your account. 

## Considerations and limitations
<a name="connectors-available-considerations"></a>
+ Some prebuilt connectors require that you create a VPC and a security group before you can use the connector. For information about creating VPCs, see [Create a VPC for a data source connector or AWS Glue connection](athena-connectors-vpc-creation.md). 
+ To use the Athena Federated Query feature with AWS Secrets Manager, you must configure an Amazon VPC private endpoint for Secrets Manager. For more information, see [Create a Secrets Manager VPC private endpoint](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html#vpc-endpoint-create) in the *AWS Secrets Manager User Guide*. 
+ For connectors that do not support predicate pushdown, queries that include a predicate take longer to execute. For small datasets, very little data is scanned, and queries take an average of about 2 minutes. However, for large datasets, many queries can time out.
+ Some federated data sources use terminology to refer data objects that is different from Athena. For more information, see [Understand federated table name qualifiers](tables-qualifiers.md).
+ We update our connectors periodically based on upgrades from the database or data source provider. We do not support data sources that are at end-of-life for support.
+ For connectors that do not support pagination when you list tables, the web service can time out if your database has many tables and metadata. The following connectors provide pagination support for listing tables:
  + DocumentDB
  + DynamoDB
  + MySQL
  + OpenSearch
  + Oracle
  + PostgreSQL
  + Redshift
  + SQL Server

## Case resolver modes in Federation SDK
<a name="case-resolver-modes"></a>

The Federation SDK supports the following standardized case resolver modes for schema and table names:
+ `NONE` – Does not change case of the given schema and table names.
+ `LOWER` – Lower case all given schema and table names.
+ `UPPER` – Upper case all given schema and table names.
+ `ANNOTATION` – This mode is maintained for backward compatibility only and is supported exclusively by existing Snowflake and SAP HANA connectors.
+ `CASE_INSENSITIVE_SEARCH` – Perform case insensitive searches against schema and tables names.

## Connector support for case resolver modes
<a name="connector-support-matrix"></a>

### Basic mode support
<a name="basic-mode-support"></a>

All JDBC connectors support the following basic modes:
+ `NONE`
+ `LOWER`
+ `UPPER`

### Annotation mode support
<a name="annotation-mode-support"></a>

Only the following connectors support the `ANNOTATION` mode:
+ Snowflake
+ SAP HANA

**Note**  
It is recommended to use CASE\_INSENSITIVE\_SEARCH instead of ANNOTATION.

### Case-insensitive search support
<a name="case-insensitive-search-support"></a>

The following connectors support `CASE_INSENSITIVE_SEARCH`:
+ DataLake Gen2
+ Snowflake
+ Oracle
+ Synapse
+ MySQL
+ PostgreSQL
+ Redshift
+ ClickHouse
+ SQL Server
+ DB2

## Case resolver limitations
<a name="case-resolver-limitations"></a>

Be aware of the following limitations when using case resolver modes:
+ When using `LOWER` mode, your schema name and all tables within the schema must be in lowercase.
+ When using `UPPER` mode, your schema name and all tables within the schema must be in uppercase.
+ When using `CASE_INSENSITIVE_SEARCH`:
  + Schema names must be unique
  + Table names within a schema must be unique (for example, you cannot have both "Apple" and "APPLE")
+ Glue integration limitations:
  + Glue only supports lowercase names
  + Only `NONE` or `LOWER` modes will work when registering your Lambda function with GlueDataCatalog/LakeFormation

## Additional information
<a name="connectors-available-additional-resources"></a>
+ For information about deploying an Athena data source connector, see [Use Amazon Athena Federated Query](federated-queries.md). 
+ For information about queries that use Athena data source connectors, see [Run federated queries](running-federated-queries.md).

**Topics**
+ [Considerations and limitations](#connectors-available-considerations)
+ [Case resolver modes in Federation SDK](#case-resolver-modes)
+ [Connector support for case resolver modes](#connector-support-matrix)
+ [Case resolver limitations](#case-resolver-limitations)
+ [Additional information](#connectors-available-additional-resources)
+ [Azure Data Lake Storage](connectors-adls-gen2.md)
+ [Azure Synapse](connectors-azure-synapse.md)
+ [Cloudera Hive](connectors-cloudera-hive.md)
+ [Cloudera Impala](connectors-cloudera-impala.md)
+ [CloudWatch](connectors-cloudwatch.md)
+ [CloudWatch metrics](connectors-cwmetrics.md)
+ [CMDB](connectors-cmdb.md)
+ [Db2](connectors-ibm-db2.md)
+ [Db2 iSeries](connectors-ibm-db2-as400.md)
+ [DocumentDB](connectors-docdb.md)
+ [DynamoDB](connectors-dynamodb.md)
+ [Google BigQuery](connectors-bigquery.md)
+ [Google Cloud Storage](connectors-gcs.md)
+ [HBase](connectors-hbase.md)
+ [Hortonworks](connectors-hortonworks.md)
+ [Kafka](connectors-kafka.md)
+ [MSK](connectors-msk.md)
+ [MySQL](connectors-mysql.md)
+ [Neptune](connectors-neptune.md)
+ [OpenSearch](connectors-opensearch.md)
+ [Oracle](connectors-oracle.md)
+ [PostgreSQL](connectors-postgresql.md)
+ [Redis OSS](connectors-redis.md)
+ [Redshift](connectors-redshift.md)
+ [SAP HANA](connectors-sap-hana.md)
+ [Snowflake](connectors-snowflake.md)
+ [SQL Server](connectors-microsoft-sql-server.md)
+ [Teradata](connectors-teradata.md)
+ [Timestream](connectors-timestream.md)
+ [TPC-DS](connectors-tpcds.md)
+ [Vertica](connectors-vertica.md)

**Note**  
The [AthenaJdbcConnector](https://serverlessrepo.aws.amazon.com/applications/us-east-1/292517598671/AthenaJdbcConnector) (latest version 2022.4.1) has been deprecated. Instead, use a database-specific connector like those for [MySQL](connectors-mysql.md), [Redshift](connectors-redshift.md), or [PostgreSQL](connectors-postgresql.md).