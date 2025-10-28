# Limitations for bringing Amazon Redshift data warehouse data into the AWS Glue Data Catalog

You can catalog, and manage access to analytic data in Amazon Redshift data warehouses using the
AWS Glue Data Catalog. The following limitations apply:

- Cross-account sharing is not supported at the federated catalog level. However, you can
  share individual databases and tables from within a federated catalog across AWS accounts.
- You must have **Cross account version settings** version 4 for sharing databases or tables in the federated catalog across AWS accounts.
- The Data Catalog supports the creation of only top-level catalogs.
- You can only update the description of catalogs in the Redshift Managed Storage
  (RMS).
- Setting up permissions on federated catalogs as well as databases and tables in the
  federated catalog to `IAMAllowedPrincipals` group is not supported.

- Data Definition Language (DDL) operations on the catalog from engines like Athena,
  Amazon EMR Spark, or others, including setting catalog configurations, are not supported.
- Performing DDL operations on RMS tables using Athena is not supported.
- Creating materialized views is not supported, whether it is through Athena, Apache Spark, the AWS Glue Data Catalog, or the Amazon Redshift consumer.
- Athena doesn't support a multi-catalog experience. It can only connect to a single, specific catalog at a time.
  Athena can't access or query across multiple catalogs simultaneously.
- Tagging and branching operations on Iceberg tables through Athena and Amazon Redshift are not
  supported.
- Time Travel on RMS tables is not supported.
- Multi-level catalogs with data lake tables are not supported. All data stored in Amazon S3 for use
  with data lake tables must reside in the default AWS Glue Data Catalog, and can't be organized into
  multi-level catalogs.
- In Amazon Redshift, datashares are not added to the registered namespace. Clusters and namespaces are
  synonymous, once you publish a cluster to the AWS Glue Data Catalog, you can't add new data.
- Amazon EMR on EC2 doesn't support joining across RMS tables and Amazon S3 tables. Only EMR Serverless
  supports this capability.
- External schemas and tables are not supported.
- RMS tables are accessible only from the extension endpoint in AWS Glue Iceberg REST
  Catalog.
- Hive tables are not accessible from third-party engines connected to the AWS Glue Iceberg REST
  Catalog.
- The read_committed isolation level on RMS tables through Spark will be
  supported.
- Redshift database names are treated as case-insensitive in the AWS Glue Data Catalog,
  restricted to 128 characters, and can be alphanumeric with dashes (-) and underscores (\_).
- The catalog names are case-insensitive, restricted to 50 characters, and can be alphanumeric
  with dashes (-) and underscores (\_).
- Amazon Redshift doesn't support using Lake Formation SQL-style GRANT and REVOKE commands to manage access
  permissions on tables published to the AWS Glue Data Catalog.
- Row-level security and dynamic data masking policies that are attached to the producer
  (source) Amazon Redshift cluster will not be enforced. Instead, access permissions defined in Lake Formation
  will be enforced on the shared data.
- Performing Data Definition Language (DDL) and Data Manipulation Language (DML) operations on table links are not supported.
- If reserved keywords are not properly escaped, it will result in failures or errors.
- Encryption of data in multi-catalog scenarios is not supported.
