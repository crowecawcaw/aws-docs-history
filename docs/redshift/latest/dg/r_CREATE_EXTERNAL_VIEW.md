Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE EXTERNAL VIEW

The Data Catalog views preview feature is available only in the following Regions.

- US East (Ohio) (us-east-2)
- US East (N. Virginia) (us-east-1)
- US West (N. California) (us-west-1)
- Asia Pacific (Tokyo) (ap-northeast-1)
- Europe (Ireland) (eu-west-1)
- Europe (Stockholm) (eu-north-1)
  Creates a view in the Data Catalog. Data Catalog views are a single view schema that works with
  other SQL engines such as Amazon Athena and Amazon EMR. You can query the view from your choice of
  engine. For more information about Data Catalog views, see [Creating Data Catalog
  views](data-catalog-views-overview.md "data-catalog-views-overview.md").

## Syntax

```
CREATE EXTERNAL VIEW *schema\_name.view\_name* [ IF NOT EXISTS ]
{catalog_name.schema_name.view_name | awsdatacatalog.dbname.view_name | external_schema_name.view_name}
AS query_definition;
```

## Parameters

_schema_name.view_name_

The schema that’s attached to your AWS Glue database, followed by the name of
the view.

PROTECTED

Specifies that the CREATE EXTERNAL VIEW command should only complete if the
query within the query_definition can successfully complete.

IF NOT EXISTS

Creates the view if the view doesn’t already exist.

catalog_name.schema_name.view_name | awsdatacatalog.dbname.view_name |
external_schema_name.view_name

The notation of the schema to use when creating the view. You can specify to
use the AWS Glue Data Catalog, a Glue database that you created, or an external schema
that you created. See [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md") and
[CREATE EXTERNAL
SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md") for more information.

_query_definition_

The definition of the SQL query that Amazon Redshift runs to alter the view.

## Examples

The following example creates a Data Catalog view named
sample_schema.glue_data_catalog_view.

```
CREATE EXTERNAL PROTECTED VIEW sample_schema.glue_data_catalog_view IF NOT EXISTS
AS SELECT * FROM sample_database.remote_table "remote-table-name";
```
