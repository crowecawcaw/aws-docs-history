# Populating the AWS Glue Data Catalog

You can populate the AWS Glue Data Catalog using the following methods:

- AWS Glue crawler – An AWS Glue crawler can automatically discover and catalog data sources like
  databases, data lakes, and streaming data. The crawlers are the most common and
  recommended method to populate the Data Catalog as they can automatically discover and infer
  metadata for a wide variety of data sources.
- Manually adding metadata – You can manually define databases, tables, and
  connection details and add them to the Data Catalog using the AWS Glue console, Lake Formation console,
  AWS CLI, or AWS Glue APIs. Manual entry is useful when you want to catalog data sources that
  cannot be crawled.
- Integrating with other AWS services – You can populate the Data Catalog with
  metadata from services like AWS Lake Formation and Amazon Athena. These services can discover and
  register data sources in the Data Catalog.
- Populating from an existing metadata repository – If you have an existing
  metadata store like Apache Hive Metastore, you can use AWS Glue to import that metadata into
  the Data Catalog. For more information, see [Migration between the Hive Metastore and the AWS Glue Data Catalog](https://github.com/aws-samples/aws-glue-samples/tree/master/utilities/Hive_metastore_migration "https://github.com/aws-samples/aws-glue-samples/tree/master/utilities/Hive_metastore_migration") on GitHub.

###### Topics

- [Using crawlers to populate the Data Catalog](add-crawler.md "add-crawler.md")
- [Defining metadata manually](populate-dg-manual.md "populate-dg-manual.md")
- [Integrating with other AWS services](populate-dc-other-services.md "populate-dc-other-services.md")
- [Data Catalog settings](console-data-catalog-settings.md "console-data-catalog-settings.md")
