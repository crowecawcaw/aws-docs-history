# Creating objects in the AWS Glue Data Catalog

AWS Lake Formation uses the AWS Glue Data Catalog (Data Catalog) to store metadata about data lakes, data sources,
transforms, and targets. Metadata is data about the underlying data in your dataset. Each AWS account has one Data Catalog per AWS Region.

Metadata in the Data Catalog is organized in a three-level data hierarchy comprising catalogs,
databases, and tables. It organizes data from various sources into logical containers called
catalogs. Each catalog represents data from sources like Amazon Redshift data warehouses,
Amazon DynamoDB databases, and third-party data sources such as Snowflake, MySQL, and
over 30 external data sources, which are integrated through federated connectors. You can also
create new catalogs in the Data Catalog to store data in S3 Table Buckets or Redshift Managed Storage
(RMS).

Tables store information about the underlying data, including schema information, partition
information, and data location. Databases are collections of tables. The Data Catalog also contains
resource links, which are links to shared catalogs, databases and tables in external accounts,
and are used for cross-account access to data in the data lake.

The Data Catalog is a nested catalog object that contains catalogs, databases and tables. It is
referenced by the AWS account ID, and is the default catalog in an account and an
AWS Region. The Data Catalog uses a three-level hierarchy (catalog.database.table) to organize
tables.

- Catalog – The top-most level of Data Catalog’s three level metadata hierarchy. You can add
  multiple catalogs in a Data Catalog through federation.
- Database – The second level of the metadata hierarchy comprising of tables and views. A database is also referred to as a schema in many data systems like Amazon Redshift and Trino.
- Table and view – The third-level of the Data Catalog's 3-level data hierarchy.
  All Iceberg tables in Amazon S3 are stored in the default Data Catalog having Catalog ID = AWS account ID. You can create federated catalogs in AWS Glue Data Catalog that store definitions of tables in Amazon Redshift, Amazon S3 Table storage, or other third-party data sources through federation.

###### Topics

- [Creating a catalog](creating-catalog.md "creating-catalog.md")
- [Creating a database](creating-database.md "creating-database.md")
- [Creating tables](creating-tables.md "creating-tables.md")
- [Building AWS Glue Data Catalog views](working-with-views.md "working-with-views.md")
