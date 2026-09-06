

# Use Amazon Athena Federated Query
<a name="federated-queries"></a>

If you have data in sources other than Amazon S3, you can use Athena Federated Query to query the data in place or build pipelines that extract data from multiple data sources and store the data in Amazon S3. With Athena Federated Query, you can run SQL queries across data stored in relational, non-relational, object, and custom data sources. For a full list of supported data sources, see [Available data source connectors](connectors-available.md). 

When you run a query against a data source, Athena invokes the connector to determine which data to read, manages parallelism, and pushes down filter predicates. Connectors can also restrict access to data based on the user who submits the query.

Athena uses *data source connectors* to run federated queries on underlying data. Athena supports two types of data source connectors with different capabilities: 
+ **AWS Glue Data Catalog federated connectors** – These connectors use an AWS Glue connection to connect to the data source. They can be used with fine-grained data governance control support through Lake Formation. For more information, see [Federated catalog data connections](https://docs.aws.amazon.com/lake-formation/latest/dg/federated-catalog-data-connection.html) in the *AWS Lake Formation Developer Guide*. 
  + Connectors associated with a Lambda can optionally be manually registered as an AWS Glue Data Catalog to be used with Lake Formation for fine-grained data governance 
  + Starting April 21, 2026, certain newly created connectors are automatically registered as Glue Data Catalogs and do not use a Lambda function in your AWS account 
+ **Athena data catalog federated connectors** – These connectors are specific to Athena and cannot be registered as federated catalogs with AWS Glue Data Catalog. They require a Lambda function in your AWS account to query data. Custom connectors developed using the Athena Query Federation SDK are Athena data catalog connectors. For more information, see [Develop a data source connector using the Athena Query Federation SDK](connect-data-source-federation-sdk.md). 

For a list of data sources compatible with each type, see [Connector type support by data source](#federated-queries-connector-support).

**Note**  
Third party developers may have used the Athena Query Federation SDK to write data source connectors. For support or licensing issues with these data source connectors, please work with your connector provider. These connectors are not tested or supported by AWS. 

## Considerations and limitations
<a name="connect-to-a-data-source-considerations"></a>
+ **Views** – You can create and query views on federated data sources. Federated views are stored in AWS Glue, not the underlying data source. For more information, see [Query federated views](running-federated-queries.md#running-federated-queries-federated-views).
+ **Delimited identifiers** – Delimited identifiers (also known as quoted identifiers) begin and end with double quotation marks ("). Currently, delimited identifiers are not supported for federated queries in Athena.
+ **Write operations** – Write operations like [INSERT INTO](insert-into.md) are not supported. Attempting to do so may result in the error message This operation is currently not supported for external catalogs.
+  **Pricing** – For pricing information, see [Amazon Athena pricing](https://aws.amazon.com/athena/pricing/).
+ **JDBC driver** – To use the JDBC driver with federated queries or an [external Hive metastore](connect-to-data-source-hive.md), include `MetadataRetrievalMethod=ProxyAPI` in your JDBC connection string. For information about the JDBC driver, see [Connect to Amazon Athena with JDBC](connect-with-jdbc.md). 
+ **Secrets Manager** – To use the Athena Federated Query feature with AWS Secrets Manager, you must configure an Amazon VPC private endpoint for Secrets Manager. For more information, see [Create a Secrets Manager VPC private endpoint](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html#vpc-endpoint-create) in the *AWS Secrets Manager User Guide*.
+ **Passthrough queries** – Passthrough queries are not supported after a data source is registered as an AWS Glue Data Catalog.

## Connector type support by data source
<a name="federated-queries-connector-support"></a>

The following table shows the connector types that each data source supports. Certain AWS Glue Data Catalog federated catalog connectors that you create on or after April 21, 2026, do not require Lambda.


<table>
<thead>
  <tr><th>Data source</th><th colspan="2">AWS Glue Data Catalog federated connectors</th><th>Athena data catalog federated connectors</th></tr>
  <tr><th></th><th>Without Lambda</th><th>With Lambda</th><th></th></tr>
</thead>
<tbody>
  <tr><td><a href="connectors-cloudwatch.md">Amazon CloudWatch Logs</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-cwmetrics.md">Amazon CloudWatch Metrics</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-docdb.md">Amazon DocumentDB</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-dynamodb.md">Amazon DynamoDB</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-msk.md">Amazon MSK</a></td><td></td><td></td><td>Yes</td></tr>
  <tr><td><a href="connectors-neptune.md">Amazon Neptune</a></td><td></td><td></td><td>Yes</td></tr>
  <tr><td><a href="connectors-opensearch.md">Amazon OpenSearch</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-redshift.md">Amazon Redshift</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-timestream.md">Amazon Timestream</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-adls-gen2.md">Azure Data Lake Storage</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-azure-synapse.md">Azure Synapse</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-cloudera-hive.md">Cloudera Hive</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-cloudera-impala.md">Cloudera Impala</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-cmdb.md">CMDB</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-kafka.md">Confluent</a></td><td></td><td></td><td>Yes</td></tr>
  <tr><td><a href="connect-data-source-federation-sdk.md">Custom</a></td><td></td><td></td><td>Yes</td></tr>
  <tr><td><a href="connectors-ibm-db2.md">Db2</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-ibm-db2-as400.md">Db2 iSeries</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-bigquery.md">Google BigQuery</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-gcs.md">Google Cloud Storage</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-hbase.md">HBase</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-hortonworks.md">Hortonworks (Hive)</a></td><td></td><td></td><td>Yes</td></tr>
  <tr><td><a href="connectors-kafka.md">Kafka</a></td><td></td><td></td><td>Yes</td></tr>
  <tr><td><a href="connectors-mysql.md">MySQL</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-oracle.md">Oracle</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-postgresql.md">PostgreSQL</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-redis.md">Redis OSS</a></td><td></td><td></td><td>Yes</td></tr>
  <tr><td><a href="connectors-sap-hana.md">SAP HANA</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-snowflake.md">Snowflake</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-microsoft-sql-server.md">SQL Server</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-teradata.md">Teradata</a></td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-tpcds.md">TPC-DS</a></td><td></td><td>Yes</td><td>Yes</td></tr>
  <tr><td><a href="connectors-vertica.md">Vertica</a></td><td></td><td>Yes</td><td>Yes</td></tr>
</tbody>
</table>


## Videos
<a name="connect-to-a-data-source-videos"></a>

Watch the following videos to learn more about using Athena Federated Query.

**Video: Analyze Results of Federated Query in Amazon Athena in Quick**  
The following video demonstrates how to analyze results of an Athena Federated Query in Quick.

[![AWS Videos](http://img.youtube.com/vi/HyM5d0TmwAQ/0.jpg)](http://www.youtube.com/watch?v=HyM5d0TmwAQ)


**Video: Game Analytics Pipeline**  
The following video shows how to deploy a scalable serverless data pipeline to ingest, store, and analyze telemetry data from games and services using Amazon Athena federated queries.

[![AWS Videos](http://img.youtube.com/vi/xcS-flUMVbs/0.jpg)](http://www.youtube.com/watch?v=xcS-flUMVbs)
