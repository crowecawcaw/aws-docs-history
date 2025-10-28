# Accessing the Data Catalog

You can use the AWS Glue Data Catalog (Data Catalog) to discover and understand your data. Data Catalog provides a consistent way to maintain schema definitions,
data types, locations, and other metadata. You can access the Data Catalog using the following methods:

- AWS Glue console – You can access and manage the Data Catalog through the AWS Glue console, a web-based user interface.
  The console allows you to browse and search for databases, tables, and their associated metadata, as well as create, update, and delete metadata definitions.
- AWS Glue crawler – Crawlers are programs that automatically scan your data sources and populate the Data Catalog with metadata.
  You can create and run crawlers to discover and catalog data from various sources like Amazon S3, Amazon RDS, Amazon DynamoDB,
  Amazon CloudWatch, and JDBC-compliant relational databases such as MySQL, and PostgreSQL as well as several non-AWS sources such as Snowflake and Google BigQuery.
- AWS Glue APIs – You can access the Data Catalog programmatically using the AWS Glue APIs.
  These APIs allow you to interact with the Data Catalog programmatically, enabling automation and integration with other applications
  and services.
- AWS Command Line Interface (AWS CLI) – You can use the AWS CLI to access and manage the Data Catalog from the command line.
  The CLI provides commands for creating, updating, and deleting metadata definitions, as well as querying
  and retrieving metadata information.
- Integration with other AWS services – The Data Catalog integrates with various other AWS services,
  allowing you to access and utilize the metadata stored in the catalog.
  For example, you can use Amazon Athena to query data sources using the metadata in the Data Catalog,
  and use AWS Lake Formation to manage data access and governance for the Data Catalog resources.

###### Topics

- [Connecting to the Data Catalog using AWS Glue Iceberg REST endpoint](connect-glu-iceberg-rest.md "connect-glu-iceberg-rest.md")
- [Connecting to the Data Catalog using AWS Glue Iceberg REST extension endpoint](connect-glue-iceberg-rest-ext.md "connect-glue-iceberg-rest-ext.md")
- [AWS Glue REST APIs for Apache Iceberg specifications](iceberg-rest-apis.md "iceberg-rest-apis.md")
- [Connecting to Data Catalog from a standalone Spark application](connect-gludc-spark.md "connect-gludc-spark.md")
- [Data mapping between Amazon Redshift and Apache Iceberg](data-mapping-rs-iceberg.md "data-mapping-rs-iceberg.md")
- [Considerations and limitations when using AWS Glue Iceberg REST Catalog APIs](limitation-glue-iceberg-rest-api.md "limitation-glue-iceberg-rest-api.md")
