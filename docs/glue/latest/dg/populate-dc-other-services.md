# Integrating with other AWS services

While you can use AWS Glue crawlers to populate the AWS Glue Data Catalog,
there are several AWS services that can automatically integrate with and populate the catalog for you.
The following sections provide more information about the specific use cases supported by AWS services that can
populate the Data Catalog.

###### Topics

- [AWS Lake Formation](#lf-dc "#lf-dc")
- [Amazon Athena](#ate-dc "#ate-dc")

## AWS Lake Formation

AWS Lake Formation is a service that makes it easier to set up a secure data lake in AWS. Lake Formation is built on AWS Glue, and Lake Formation and AWS Glue share the same AWS Glue Data Catalog.
You can register your Amazon S3 data location with Lake Formation, and use Lake Formation console to create
databases and tables in the AWS Glue Data Catalog, define data access policies, and audit data access
across your data lake from a central place. You can use the Lake Formation fine-grained access control to manage your existing Data Catalog resources and Amazon S3 data locations.

With data registered with Lake Formation, you can securely
share Data Catalog resources across IAM principals, AWS accounts, AWS organizations, and organizational
units.

For more information about creating Data Catalog resources using Lake Formation, see [Creating Data Catalog tables and databases](../../../lake-formation/latest/dg/populating-catalog.md "../../../lake-formation/latest/dg/populating-catalog.md") in the AWS Lake Formation Developer Guide.

## Amazon Athena

Amazon Athena uses the Data Catalog to store and retrieve table metadata for the Amazon S3 data in your AWS account.
The table metadata lets the Athena query engine know how to find, read, and process the data that you want to query.

You can populate the AWS Glue Data Catalog by using Athena `CREATE TABLE` statements directly. You can manually define and populate the schema and partition metadata
in the Data Catalog without needing to run a crawler.

1. In the Athena console, create a database that will store the table metadata in the Data Catalog.
2. Use the `CREATE EXTERNAL TABLE` statement to define the schema of your data source.
3. Use the `PARTITIONED BY` clause to define any partition keys if your data is partitioned.
4. Use the `LOCATION` clause to specify the Amazon S3 path where your actual data files are stored.
5. Run the `CREATE TABLE` statement.

This query creates the table metadata in the Data Catalog based on your defined schema and partitions,
without actually crawling the data.

You can query the table in Athena, and it will use the metadata from the Data Catalog to access and query your data files in Amazon S3.

For more information, see [Creating databases and tables](../../../athena/latest/ug/work-with-data.md "../../../athena/latest/ug/work-with-data.md") in the Amazon Athena User Guide.
