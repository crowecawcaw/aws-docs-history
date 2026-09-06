

# Use Athena SQL
<a name="using-athena-sql"></a>

You can use Athena SQL to query your data in-place in Amazon S3 using the [AWS Glue Data Catalog](data-sources-glue.md), [an external Hive metastore](connect-to-data-source-hive.md), or [federated queries](federated-queries.md) using a variety of [prebuilt connectors](connectors-available.md) to other data sources.

You can also:
+ Connect to business intelligence tools and other applications using [Athena's JDBC and ODBC drivers](https://docs.aws.amazon.com/athena/latest/ug/athena-bi-tools-jdbc-odbc.html). 
+ Query [AWS service logs](querying-aws-service-logs.md). 
+ Query [Apache Iceberg tables](querying-iceberg.md), including time travel queries, and [Apache Hudi datasets](querying-hudi.md). 
+ Query [geospatial data](querying-geospatial-data.md). 
+ Query using [machine learning inference](https://docs.aws.amazon.com/athena/latest/ug/querying-mlmodel.html) from Amazon SageMaker AI.
+ Query using your own [user-defined functions](https://docs.aws.amazon.com/athena/latest/ug/querying-udf.html).
+ Speed up query processing of highly-partitioned tables and automate partition management by using [partition projection](https://docs.aws.amazon.com/athena/latest/ug/partition-projection.html).

**Topics**
+ [Understanding tables, databases, and data catalogs in Athena](understanding-tables-databases-and-the-data-catalog.md)
+ [Get started](getting-started.md)
+ [Connect to data sources](work-with-data-stores.md)
+ [Connect to Amazon Athena with ODBC and JDBC drivers](athena-bi-tools-jdbc-odbc.md)
+ [Create databases and tables](work-with-data.md)
+ [Create a table from query results (CTAS)](ctas.md)
+ [Use SerDes](serde-reference.md)
+ [Run SQL queries in Amazon Athena](querying-athena-tables.md)
+ [Use Athena ACID transactions](acid-transactions.md)
+ [Amazon Athena security](security.md)
+ [Workload management](workload-management.md)
+ [Athena engine versioning](engine-versions.md)
+ [SQL reference for Athena](ddl-sql-reference.md)
+ [Troubleshoot issues in Athena](troubleshooting-athena.md)
+ [Code samples](code-samples.md)