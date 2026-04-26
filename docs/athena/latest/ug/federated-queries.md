# Use Amazon Athena Federated Query

If you have data in sources other than Amazon S3, you can use Athena Federated Query to query the data in
place or build pipelines that extract data from multiple data sources and store the data in
Amazon S3. With Athena Federated Query, you can run SQL queries across data stored in relational,
non-relational, object, and custom data sources. For a full list of supported data sources,
see [Available data source connectors](connectors-available.md "connectors-available.md").

When you run a query against a data source, Athena invokes the connector to determine
which data to read, manages parallelism, and pushes down filter predicates. Connectors
can also restrict access to data based on the user who submits the query.

Athena uses _data source connectors_ to run federated queries on
underlying data. Athena supports two types of data source connectors with different
capabilities:

- AWS Glue Data Catalog federated connectors
  – These connectors use an AWS Glue connection to connect to the data source. They can be used with fine-grained data governance control support through Lake Formation.
  For more information, see [Federated catalog data connections](../../../lake-formation/latest/dg/federated-catalog-data-connection.md "../../../lake-formation/latest/dg/federated-catalog-data-connection.md") in the _AWS Lake Formation Developer Guide_.
  - Connectors associated with a Lambda can optionally be manually registered as an AWS Glue Data Catalog to be used with Lake Formation for fine-grained data governance
  - Starting April 21, 2026, certain newly created connectors are automatically registered as Glue Data Catalogs and do not use a Lambda function in your AWS account

- Athena data catalog federated connectors
  – These connectors are specific to Athena and cannot be registered as
  federated catalogs with AWS Glue Data Catalog. They require a Lambda function in
  your AWS account to query data. Custom connectors developed using the Athena Query Federation SDK
  are Athena data catalog connectors. For more information, see
  [Develop a data source connector using the Athena Query Federation SDK](connect-data-source-federation-sdk.md "connect-data-source-federation-sdk.md").
  For a list of data sources compatible with each type, see [Connector type support by data source](#federated-queries-connector-support "#federated-queries-connector-support").

###### Note

Third party developers may have used the Athena Query Federation SDK to write data source connectors.
For support or licensing issues with these data source connectors, please work with your
connector provider. These connectors are not tested or supported by AWS.

## Considerations and limitations

- Views – You can create and query views
  on federated data sources. Federated views are stored in AWS Glue, not the
  underlying data source. For more information, see [Query federated views](running-federated-queries.md#running-federated-queries-federated-views "running-federated-queries.md#running-federated-queries-federated-views").
- Delimited identifiers – Delimited
  identifiers (also known as quoted identifiers) begin and end with double
  quotation marks ("). Currently, delimited identifiers are not supported for
  federated queries in Athena.
- Write operations – Write operations like
  [INSERT INTO](insert-into.md "insert-into.md") are not supported.
  Attempting to do so may result in the error message **`This operation is
currently not supported for external catalogs`**.
- Pricing – For pricing information, see
  [Amazon Athena
  pricing](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/").
- JDBC driver – To use the JDBC driver
  with federated queries or an [external Hive metastore](connect-to-data-source-hive.md "connect-to-data-source-hive.md"),
  include `MetadataRetrievalMethod=ProxyAPI` in your JDBC connection
  string. For information about the JDBC driver, see [Connect to Amazon Athena with JDBC](connect-with-jdbc.md "connect-with-jdbc.md").
- Secrets Manager – To use the Athena Federated Query feature with
  AWS Secrets Manager, you must configure an Amazon VPC private endpoint for Secrets Manager. For more
  information, see [Create a Secrets Manager VPC private endpoint](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md#vpc-endpoint-create "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md#vpc-endpoint-create") in the _AWS Secrets Manager User Guide_.
- Passthrough queries – Passthrough queries are not supported after a data source is registered as an AWS Glue Data Catalog.

## Connector type support by data source

The following table shows the connector types that each data source supports.
Certain AWS Glue Data Catalog federated catalog connectors that you create on or after April 21, 2026,
do not require Lambda.

| Data source                                                                             | AWS Glue Data Catalog federated connectors | Athena data catalog federated connectors |
| --------------------------------------------------------------------------------------- | ------------------------------------------ | ---------------------------------------- | --- |
|                                                                                         | Without Lambda                             | With Lambda                              |     |
| [Amazon CloudWatch Logs](connectors-cloudwatch.md "connectors-cloudwatch.md")           |                                            | Yes                                      | Yes |
| [Amazon CloudWatch Metrics](connectors-cwmetrics.md "connectors-cwmetrics.md")          |                                            | Yes                                      | Yes |
| [Amazon DocumentDB](connectors-docdb.md "connectors-docdb.md")                          | Yes                                        | Yes                                      | Yes |
| [Amazon DynamoDB](connectors-dynamodb.md "connectors-dynamodb.md")                      | Yes                                        | Yes                                      | Yes |
| [Amazon MSK](connectors-msk.md "connectors-msk.md")                                     |                                            |                                          | Yes |
| [Amazon Neptune](connectors-neptune.md "connectors-neptune.md")                         |                                            |                                          | Yes |
| [Amazon OpenSearch](connectors-opensearch.md "connectors-opensearch.md")                | Yes                                        | Yes                                      | Yes |
| [Amazon Redshift](connectors-redshift.md "connectors-redshift.md")                      | Yes                                        | Yes                                      | Yes |
| [Amazon Timestream](connectors-timestream.md "connectors-timestream.md")                |                                            | Yes                                      | Yes |
| [Azure Data Lake Storage](connectors-adls-gen2.md "connectors-adls-gen2.md")            |                                            | Yes                                      | Yes |
| [Azure Synapse](connectors-azure-synapse.md "connectors-azure-synapse.md")              |                                            | Yes                                      | Yes |
| [Cloudera Hive](connectors-cloudera-hive.md "connectors-cloudera-hive.md")              |                                            | Yes                                      | Yes |
| [Cloudera Impala](connectors-cloudera-impala.md "connectors-cloudera-impala.md")        |                                            | Yes                                      | Yes |
| [CMDB](connectors-cmdb.md "connectors-cmdb.md")                                         |                                            | Yes                                      | Yes |
| [Confluent](connectors-kafka.md "connectors-kafka.md")                                  |                                            |                                          | Yes |
| [Custom](connect-data-source-federation-sdk.md "connect-data-source-federation-sdk.md") |                                            |                                          | Yes |
| [Db2](connectors-ibm-db2.md "connectors-ibm-db2.md")                                    |                                            | Yes                                      | Yes |
| [Db2 iSeries](connectors-ibm-db2-as400.md "connectors-ibm-db2-as400.md")                |                                            | Yes                                      | Yes |
| [Google BigQuery](connectors-bigquery.md "connectors-bigquery.md")                      | Yes                                        | Yes                                      | Yes |
| [Google Cloud Storage](connectors-gcs.md "connectors-gcs.md")                           |                                            | Yes                                      | Yes |
| [HBase](connectors-hbase.md "connectors-hbase.md")                                      |                                            | Yes                                      | Yes |
| [Hortonworks (Hive)](connectors-hortonworks.md "connectors-hortonworks.md")             |                                            |                                          | Yes |
| [Kafka](connectors-kafka.md "connectors-kafka.md")                                      |                                            |                                          | Yes |
| [MySQL](connectors-mysql.md "connectors-mysql.md")                                      | Yes                                        | Yes                                      | Yes |
| [Oracle](connectors-oracle.md "connectors-oracle.md")                                   | Yes                                        | Yes                                      | Yes |
| [PostgreSQL](connectors-postgresql.md "connectors-postgresql.md")                       | Yes                                        | Yes                                      | Yes |
| [Redis OSS](connectors-redis.md "connectors-redis.md")                                  |                                            |                                          | Yes |
| [SAP HANA](connectors-sap-hana.md "connectors-sap-hana.md")                             | Yes                                        | Yes                                      | Yes |
| [Snowflake](connectors-snowflake.md "connectors-snowflake.md")                          | Yes                                        | Yes                                      | Yes |
| [SQL Server](connectors-microsoft-sql-server.md "connectors-microsoft-sql-server.md")   | Yes                                        | Yes                                      | Yes |
| [Teradata](connectors-teradata.md "connectors-teradata.md")                             | Yes                                        | Yes                                      | Yes |
| [TPC-DS](connectors-tpcds.md "connectors-tpcds.md")                                     |                                            | Yes                                      | Yes |
| [Vertica](connectors-vertica.md "connectors-vertica.md")                                |                                            | Yes                                      | Yes |

## Videos

Watch the following videos to learn more about using Athena Federated Query.

###### Video: Analyze Results of Federated Query in Amazon Athena in Quick

The following video demonstrates how to analyze results of an Athena Federated Query
in Quick.

###### Video: Game Analytics Pipeline

The following video shows how to deploy a scalable serverless data pipeline to
ingest, store, and analyze telemetry data from games and services using Amazon Athena
federated queries.
