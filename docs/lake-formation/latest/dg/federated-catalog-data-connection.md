

# Federating into external data sources in the AWS Glue Data Catalog
<a name="federated-catalog-data-connection"></a>

 You can connect the AWS Glue Data Catalog (Data Catalog) to data warehouses such as Amazon Redshift, Snowflake, cloud databases such as Amazon RDS, Amazon DynamoDB, Oracle, and streaming services such as Amazon MSK, and on-premises systems such as Teradata using AWS Glue connections. These connections are stored in the AWS Glue Data Catalog and registered with AWS Lake Formation, allowing you to create a federated catalog for each available data source. 

 A *federated catalog* is a top level container that points to a database in an external data system. It enables you to query the data directly from the external data system without extract, transform, and load (ETL) process. 

For more information about AWS Glue connections, see [Connecting to data](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html) in the AWS Glue Developer Guide.

Data lake administrators can create federated catalogs using [Amazon SageMaker Lakehouse](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/lakehouse.html) or [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html).

Data lake administrators can then grant fine-grained permissions on the objects within the catalog using Lake Formation, controlling access at various levels such as catalog, database, table, column, row, or cell. Data analysts can discover and query the cataloged data sources using Athena, with Lake Formation enforcing the defined access policies. Analysts can join data across multiple sources in a single query without needing to connect to each source individually. 

**Topics**
+ [Workflow](#connect-data-source-workflow)
+ [Prerequisites for connecting the Data Catalog to external data sources](connect-data-source-prerequisites.md)
+ [Creating a federated catalog using an AWS Glue connection](create-fed-catalog-data-source.md)
+ [Viewing catalog objects](view-fed-glue-connection-catalog.md)
+ [Deleting a federated catalog](delete-glue-fed-catalog.md)
+ [Querying federated catalogs](query-glue-fed-catalog.md)
+ [Additional resources](additional-resources-fed-connection.md)

## Workflow
<a name="connect-data-source-workflow"></a>

A data lake administrator or a user with the required permissions completes the following the steps for connecting the AWS Glue Data Catalog to an external data source.

1.  Creates an AWS Glue connection to the data source. When you register the connection, the IAM role used in registering the connection must have access to the Lambda function and the Amazon S3 spill bucket location. 

1.  Registers the connection with Lake Formation. 

1.  Creates a federated catalog in the Data Catalog using a AWS Glue connection to connect to the available data sources. The databases, tables, and views are automatically cataloged in the Data Catalog, and registered with Lake Formation. 

1.  Grants access to specific catalogs, databases, and tables to data analysts using Lake Formation permissions. Fine-grained access control policies can be defined across data lakes, warehouses, and OLTP sources using Lake Formation, enabling row-level and column-level security filters. 

    Data analysts can then access all data through the Data Catalog using SQL queries in Athena, without needing separate connections or data source credentials. Analysts can run federated SQL queries that scan data from multiple sources, joining data in-place without complex data pipelines. 