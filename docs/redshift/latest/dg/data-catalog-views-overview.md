Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# AWS Glue Data Catalog views

This topic describes how to create views in the AWS Glue Data Catalog. You can use views in the Data Catalog to access
data in different data sources using the same schema.

By creating views in the Data Catalog, you can create a single common view schema and
metadata object to use across engines such as Amazon Athena and Amazon EMR Spark. Doing so lets you
use the same views across your data lakes and data warehouses to fit your use cases. Views
in the Data Catalog are special in that they are categorized as definer views, where access permissions
are defined by the user who created the view instead of the user querying the view. The
following are some use cases and benefits of creating views in the Data Catalog:

- Create a view that restricts data access based on the permissions the user needs.
  For example, you can use views in the Data Catalog to prevent employees who don’t work in the HR
  department from seeing personally identifiable information (PII).
- Make sure that users can’t access incomplete records. By applying certain filters
  onto your view in the Data Catalog, you make sure that data records inside a view in the Data Catalog are
  always complete.
- Data Catalog views have an included security benefit of making sure that the query
  definition used to create the view must complete to create the view. This security
  benefit means that views in the Data Catalog are not susceptible to SQL commands from
  malicious players.
- Views in the Data Catalog support the same advantages as normal views, such as letting users access a
  view without making the underlying table available to users.
  To create a view in the Data Catalog, you must have a [Spectrum external table](c-spectrum-external-tables.md "c-spectrum-external-tables.md"), an object that’s contained within a
  [Lake Formation-managed datashare](what_is_datashare.md#lf_datashare_overview "what_is_datashare.md#lf_datashare_overview"),
  or an [Apache Iceberg table](what_is_datashare.md#lf_datashare_overview "what_is_datashare.md#lf_datashare_overview").

Definitions of Data Catalog views are stored in the AWS Glue Data Catalog. Use AWS Lake Formation to grant access
through resource grants, column grants, or tag-based access controls. For more information
about granting and revoking access in Lake Formation, see [Granting and revoking
permissions on Data Catalog resources](../../../lake-formation/latest/dg/granting-catalog-permissions.md "../../../lake-formation/latest/dg/granting-catalog-permissions.md").

When you use Amazon Redshift to run a query referencing such AWS Glue Data Catalog views,
Amazon Redshift automatically masks fields in certain system table and view
columns when logging metadata about that query. For more information, see
[Secure logging](../mgmt/db-auditing-secure-logging.md "../mgmt/db-auditing-secure-logging.md") in the _Amazon Redshift Management Guide_.

## Prerequisites

Before you can create a view in the Data Catalog, make sure that you have the following prerequisites completed:

- Make sure that your IAM role has the following trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "glue.amazonaws.com",
 "lakeformation.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

- You also need the following pass role policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt1",
 "Action": [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "glue.amazonaws.com",
 "lakeformation.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

- Finally, you also need the following permissions.
  - `Glue:GetDatabase`
  - `Glue:GetDatabases`
  - `Glue:CreateTable`
  - `Glue:GetTable`
  - `Glue:UpdateTable`
  - `Glue:DeleteTable`
  - `Glue:GetTables`
  - `Glue:SearchTables`
  - `Glue:BatchGetPartition`
  - `Glue:GetPartitions`
  - `Glue:GetPartition`
  - `Glue:GetTableVersion`
  - `Glue:GetTableVersions`

## End-to-end example

Start by creating an external schema based on your Data Catalog database.

```
CREATE EXTERNAL SCHEMA IF NOT EXISTS external_schema FROM DATA CATALOG DATABASE 'external_data_catalog_db'
IAM_ROLE 'arn:aws:iam::123456789012:role/sample-role';
```

You can now create a Data Catalog view.

```
CREATE EXTERNAL PROTECTED VIEW external_schema.remote_view
AS SELECT * FROM external_schema.remote_table;
```

You can then start querying your view.

```
SELECT * FROM external_schema.remote_view;
```

For more information about the SQL commands related to views in the Data Catalog, see
[CREATE EXTERNAL VIEW](r_CREATE_EXTERNAL_VIEW.md "r_CREATE_EXTERNAL_VIEW.md"),
[ALTER EXTERNAL VIEW](r_ALTER_EXTERNAL_VIEW.md "r_ALTER_EXTERNAL_VIEW.md"), and
[DROP EXTERNAL VIEW](r_DROP_EXTERNAL_VIEW.md "r_DROP_EXTERNAL_VIEW.md").

## Considerations and limitations

The following are considerations and limitations that apply to views created in the Data Catalog.

- AWS Glue Data Catalog views are only supported on RA3 provisioned clusters or Redshift Serverless workgroups.
- You can’t create a Data Catalog view that is based off of another view.
- You can only have 10 base tables in a Data Catalog view.
- The definer of the view must have full `SELECT GRANTABLE` permissions on the base tables.
- Views can only contain Lake Formation objects and built-ins. The following objects are not permitted
  inside of a view.
  - System tables
  - User-defined functions (UDFs)
  - Redshift tables, views, materialized views, and late binding views that aren’t in a Lake Formation
    managed data share.

- Views can’t contain nested Redshift Spectrum tables.
- AWS Glue representations of the base objects of a view must be in the same AWS account and Region as the view.
