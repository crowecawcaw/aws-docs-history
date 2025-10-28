Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP EXTERNAL VIEW

Drops an external view from the database. Dropping an external view removes it from all
SQL engines the view is associated with, such as Amazon Athena and Amazon EMR Spark. This command
can't be reversed. For more information about Data Catalog views, see [AWS Glue Data Catalog views](data-catalog-views-overview.md "data-catalog-views-overview.md").

## Syntax

```
DROP EXTERNAL VIEW *schema\_name.view\_name* [ IF EXISTS ]
{catalog_name.schema_name.view_name | awsdatacatalog.dbname.view_name | external_schema_name.view_name}
```

## Parameters

_schema_name.view_name_

The schema that’s attached to your AWS Glue database, followed by the name of
the view.

IF EXISTS

Drops the view only if it exists.

catalog_name.schema_name.view_name | awsdatacatalog.dbname.view_name |
external_schema_name.view_name

The notation of the schema to use when dropping the view. You can specify to
use the AWS Glue Data Catalog, a Glue database that you created, or an external schema
that you created. See [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md") and
[CREATE EXTERNAL
SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md") for more information.

_query_definition_

The definition of the SQL query that Amazon Redshift runs to alter the view.

## Examples

The following example drops a Data Catalog view named
sample_schema.glue_data_catalog_view.

```
DROP EXTERNAL VIEW sample_schema.glue_data_catalog_view IF EXISTS
```
