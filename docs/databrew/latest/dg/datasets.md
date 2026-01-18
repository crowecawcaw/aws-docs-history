# Connecting to your data

For more information on connecting to the following data sources, choose the section
that applies to you.

- **AWS Glue Data Catalog**
  – You can use the Data Catalog to define references to data objects
  stored in the AWS Cloud, including the following services:

      + Amazon Redshift
      + Aurora MySQL
      + Aurora PostgreSQL
      + Amazon RDS for MySQL
      + Amazon RDS for PostgreSQL

  DataBrew recognizes all Lake Formation permissions that have been applied to Data Catalog
  resources, so DataBrew users can only access these resources if they're authorized.

To create a dataset, you specify a Data Catalog database name and a table name.
DataBrew takes care of the other connection details.

- **AWS Data Exchange**
  – You can choose from hundreds of third-party data sources that are available
  in AWS Data Exchange. By subscribing to
  these data sources, you always have the most up-to-date version of the data.

To create a dataset, you specify the name of a Data Exchange data product that you're
subscribed to or entitled to use.

- **JDBC driver connections** – You can create
  a dataset by connecting DataBrew to a JDBC-compatible data source. DataBrew supports
  connecting to the following sources through JDBC:
  - Amazon Redshift
  - Microsoft SQL Server
  - MySQL
  - Oracle
  - PostgreSQL
  - Snowflake

###### Topics

- [Using drivers with AWS Glue DataBrew](dbms-driver-connections.md "dbms-driver-connections.md")
- [Supported JDBC drivers](jdbc-drivers.md "jdbc-drivers.md")
