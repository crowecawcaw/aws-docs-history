Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER EXTERNAL VIEW

Use the ALTER EXTERNAL VIEW command to update your external view. Depending on which
parameters you use, other SQL engines such as Amazon Athena and Amazon EMR Spark that can also
reference this view might be affected. For more information about Data Catalog views, see [AWS Glue Data Catalog views](data-catalog-views-overview.md "data-catalog-views-overview.md").

## Syntax

```
ALTER EXTERNAL VIEW *schema\_name.view\_name*
{catalog_name.schema_name.view_name | awsdatacatalog.dbname.view_name | external_schema_name.view_name}
[FORCE] { AS (query_definition) | REMOVE DEFINITION }
```

## Parameters

_schema_name.view_name_

The schema that’s attached to your AWS Glue database, followed by the name of
the view.

catalog_name.schema_name.view_name | awsdatacatalog.dbname.view_name |
external_schema_name.view_name

The notation of the schema to use when altering the view. You can specify to
use the AWS Glue Data Catalog, a Glue database that you created, or an external schema
that you created. See [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md") and
[CREATE EXTERNAL
SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md") for more information.

FORCE

Whether AWS Lake Formation should update the definition of the view even if the
objects referenced in the table are inconsistent with other SQL engines. If
Lake Formation updates the view, the view is considered stale for the other SQL engines
until those engines are updated as well.

_AS query_definition_

The definition of the SQL query that Amazon Redshift runs to alter the view.

REMOVE DEFINITION

Whether to drop and recreate the views. Views must be dropped and recreated
to mark them as `PROTECTED`.

## Examples

The following example alters a Data Catalog view named
sample_schema.glue_data_catalog_view.

```
ALTER EXTERNAL VIEW sample_schema.glue_data_catalog_view
FORCE
REMOVE DEFINITION
```
