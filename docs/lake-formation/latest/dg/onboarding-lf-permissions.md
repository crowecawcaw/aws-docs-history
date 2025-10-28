# Onboarding to Lake Formation permissions

AWS Lake Formation uses the AWS Glue Data Catalog (Data Catalog) to store metadata for the Amazon S3 data lakes and external data sources such as Amazon Redshift in the form of catalogs, databases
and tables. Metadata in the Data Catalog is organized in a three-level data hierarchy comprising catalogs, databases, and tables.
It organizes data from various sources into logical containers called catalogs. Databases are collections of tables. The Data Catalog also
contains resource links, which are links to shared databases and tables in external accounts,
and are used for cross-account access to data in the data lake. Each AWS account has one
Data Catalog per AWS Region.

Lake Formation provides a relational database management system (RDBMS) permissions model to grant or
revoke access to catalogs, databases, tables, and columns in the Data Catalog with underlying data in
Amazon S3.

Before you learn about the details of the Lake Formation permissions model, it is helpful to review
the following background information:

- Data lakes managed by Lake Formation reside in designated locations in Amazon Simple Storage Service (Amazon S3).
  The Data Catalog also contains catalog objects.
  Each catalog represents data from sources like Amazon Redshift data warehouses, Amazon DynamoDB databases,
  and third-party data sources such as Snowflake, MySQL, and over 30 external data sources, which are integrated through federated connectors.
- Lake Formation maintains a Data Catalog that contains metadata about source data to be imported into
  your data lakes, such as data in logs and relational databases, and about data in your data
  lakes in Amazon S3. The Data Catalog also contains metadata about data from external data sources other than Amazon S3. The metadata is organized as catalogs, databases and tables. Metadata tables contain
  schema, location, partitioning, and other information about the data that they represent.
  Metadata databases are collections of tables.
- The Lake Formation Data Catalog is the same Data Catalog used by AWS Glue. You can use AWS Glue crawlers to
  create Data Catalog tables, and you can use AWS Glue extract, transform, and load (ETL) jobs to
  populate the underlying data in your data lakes.
- The catalogs, databases, and tables in the Data Catalog are referred to as _Data Catalog resources_. Tables in the Data Catalog are referred to as _metadata tables_ to distinguish them from tables in data sources
  or tabular data in Amazon S3. The data that the metadata tables point to in Amazon S3 or in data
  sources is referred to as _underlying data_.
- A _principal_ is a user or role, an Amazon Quick Suite
  user or group, a user or group that authenticates with Lake Formation through a SAML provider, or for
  cross-account access control, an AWS account ID, organization ID, or organizational unit
  ID.
- AWS Glue crawlers create metadata tables, but you can also manually create metadata tables
  with the Lake Formation console, the API, or the AWS Command Line Interface (AWS CLI). When creating a metadata table,
  you must specify a location. When you create a database, the location is optional. Table
  locations can be Amazon S3 locations or data source locations such as an Amazon Relational Database Service (Amazon RDS)
  database. Database locations are always Amazon S3 locations.
- Services that integrate with Lake Formation, such as Amazon Athena and Amazon Redshift, can access the
  Data Catalog to obtain metadata and to check authorization for running queries. For a complete
  list of integrated services, see [AWS service integrations with Lake Formation](service-integrations.md "service-integrations.md").

###### Topics

- [Overview of Lake Formation permissions](lf-permissions-overview.md "lf-permissions-overview.md")
- [Lake Formation personas and IAM permissions reference](permissions-reference.md "permissions-reference.md")
- [Changing the default settings for your data
  lake](change-settings.md "change-settings.md")
- [Implicit Lake Formation permissions](implicit-permissions.md "implicit-permissions.md")
- [Lake Formation permissions reference](lf-permissions-reference.md "lf-permissions-reference.md")
- [Integrating IAM Identity Center](identity-center-integration.md "identity-center-integration.md")
- [Adding an Amazon S3 location to your data lake](register-data-lake.md "register-data-lake.md")
- [Hybrid access mode](hybrid-access-mode.md "hybrid-access-mode.md")
- [Creating objects in the AWS Glue Data Catalog](populating-catalog.md "populating-catalog.md")
- [Importing data using workflows in Lake Formation](workflows.md "workflows.md")
