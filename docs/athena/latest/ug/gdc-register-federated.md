# Register federated catalogs in Athena

After you create connections to federated data sources, you can register them as
federated data catalogs for simplified data discovery and manage data access with
fine-grained permissions using Lake Formation. For more information, see [Register your connection as a Glue Data Catalog](register-connection-as-gdc.md "register-connection-as-gdc.md").

## Considerations and limitations

- DDL operations are not supported on federated catalogs.
- You can register the following connectors to integrate with AWS Glue for fine-grained access
  control:
  - [Azure Data Lake
    Storage](connectors-adls-gen2.md "connectors-adls-gen2.md")
  - [Azure
    Synapse](connectors-azure-synapse.md "connectors-azure-synapse.md")
  - [BigQuery](connectors-bigquery.md "connectors-bigquery.md")
  - [CMDB](connectors-cmdb.md "connectors-cmdb.md")
  - [Db2](connectors-ibm-db2.md "connectors-ibm-db2.md")
  - [Db2 iSeries](connectors-ibm-db2-as400.md "connectors-ibm-db2-as400.md")
  - [DocumentDB](connectors-docdb.md "connectors-docdb.md")
  - [DynamoDB](connectors-dynamodb.md "connectors-dynamodb.md")
  - [Google Cloud Storage](connectors-gcs.md "connectors-gcs.md")
  - [HBase](connectors-hbase.md "connectors-hbase.md")
  - [MySQL](connectors-mysql.md "connectors-mysql.md")
  - [OpenSearch](connectors-opensearch.md "connectors-opensearch.md")
  - [Oracle](connectors-oracle.md "connectors-oracle.md")
  - [PostgreSQL](connectors-postgresql.md "connectors-postgresql.md")
  - [Redshift](connectors-redshift.md "connectors-redshift.md")
  - [SAP HANA](connectors-sap-hana.md "connectors-sap-hana.md")
  - [Snowflake](connectors-snowflake.md "connectors-snowflake.md")
  - [SQL
    Server](connectors-microsoft-sql-server.md "connectors-microsoft-sql-server.md")
  - [Timestream](connectors-timestream.md "connectors-timestream.md")
  - [TPC-DS](connectors-tpcds.md "connectors-tpcds.md")

- When you create a resource link for Glue connection federation, the name of [resource link](../../../lake-formation/latest/dg/create-resource-link-database.md "../../../lake-formation/latest/dg/create-resource-link-database.md") must be same as the database name of the
  producer.
- Currently, only lowercase table and column names are recognized even if
  the data source is case insensitive.
