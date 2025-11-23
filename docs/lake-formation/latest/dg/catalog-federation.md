# Catalog federation to remote Iceberg catalogs

Catalog federation in AWS Glue provides direct and secure access to Iceberg tables, stored in Amazon S3 and cataloged in remote catalogs, using AWS analytics engines. Catalog federation synchronizes metadata across Data Catalog and remote catalogs when you access remote tables. It is supported by a wide variety of analytics engines, including Amazon Redshift, Amazon EMR, Amazon Athena, AWS Glue, third-party engines like Apache Spark, and more.

Catalog federation uses AWS Glue Data Catalog to communicate with remote catalog systems to discover tables and Lake Formation to authorize access to table data in Amazon S3. When you query a federated table, Data Catalog discovers the latest table information in the remote catalog at query time, getting the table's Amazon S3 location, current schema, and partition information. Your analytics engine (Amazon Athena, Amazon Redshift, Amazon EMR) then uses this information to access Iceberg data files directly from Amazon S3. Lake Formation manages access to table(s) by vending scoped credentials to the table data stored in Amazon S3, allowing the engines to apply fine-grained permissions to federated table(s).

## Features of Catalog Federation

###### Governed using Lake Formation

Federated Iceberg catalogs in Data Catalog are Lake Formation registered resources, allowing you to grant fine-grained row-, column-, cell-level permissions to Iceberg tables in federated Iceberg catalogs using Lake Formation grants. Federated Iceberg catalogs and associated objects can be securely shared across AWS accounts. Federated Iceberg catalogs also work with Lake Formation Tag-based access control allowing you to scale governance using tags.

###### Networking configurations

Catalog federation supports direct connections to remote catalog sources using standard HTTPS connectivity. It also supports connectivity through Amazon VPC when you want to maintain network isolation and connectivity using proxy support when you want secure communication through organization firewalls.

###### Topics

- [Federate to Snowflake Iceberg Catalog](catalog-federation-snowflake.md "catalog-federation-snowflake.md")
- [Federate to Databricks Unity Catalog](catalog-federation-databricks.md "catalog-federation-databricks.md")
