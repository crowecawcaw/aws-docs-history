

# Register federated catalogs in Athena
<a name="gdc-register-federated"></a>

After you create connections to federated data sources, you can register them as federated data catalogs for simplified data discovery and manage data access with fine-grained permissions using Lake Formation. For more information, see [Register your connection as a Glue Data Catalog](register-connection-as-gdc.md).

## Considerations and limitations
<a name="gdc-register-federated-consideration"></a>
+ DDL operations are not supported on federated catalogs. 
+ You can register the following connectors to integrate with AWS Glue for fine-grained access control:
  + [Azure Data Lake Storage](connectors-adls-gen2.md)
  + [Azure Synapse](connectors-azure-synapse.md)
  + [BigQuery](connectors-bigquery.md)
  + [CMDB](connectors-cmdb.md)
  + [Db2](connectors-ibm-db2.md)
  + [Db2 iSeries](connectors-ibm-db2-as400.md)
  + [DocumentDB](connectors-docdb.md)
  + [DynamoDB](connectors-dynamodb.md)
  + [Google Cloud Storage](connectors-gcs.md)
  + [HBase](connectors-hbase.md)
  + [MySQL](connectors-mysql.md)
  + [OpenSearch](connectors-opensearch.md)
  + [Oracle](connectors-oracle.md)
  + [PostgreSQL](connectors-postgresql.md)
  + [Redshift](connectors-redshift.md)
  + [SAP HANA](connectors-sap-hana.md)
  + [Snowflake](connectors-snowflake.md)
  + [SQL Server](connectors-microsoft-sql-server.md)
  + [Timestream](connectors-timestream.md)
  + [TPC-DS](connectors-tpcds.md)
+ When you create a resource link for Glue connection federation, the name of [resource link](https://docs.aws.amazon.com/lake-formation/latest/dg/create-resource-link-database.html) must be same as the database name of the producer.
+ Currently, only lowercase table and column names are recognized even if the data source is case insensitive.