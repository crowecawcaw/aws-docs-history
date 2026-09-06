

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ALTER EXTERNAL VIEW
<a name="r_ALTER_EXTERNAL_VIEW"></a>

Use the ALTER EXTERNAL VIEW command to update your external view. Depending on which parameters you use, other SQL engines such as Amazon Athena and Amazon EMR Spark that can also reference this view might be affected. For more information about Data Catalog views, see [AWS Glue Data Catalog views](https://docs.aws.amazon.com/redshift/latest/dg/data-catalog-views-overview.html).

## Syntax
<a name="r_ALTER_EXTERNAL_VIEW-synopsis"></a>

```
ALTER EXTERNAL VIEW schema_name.view_name
{catalog_name.schema_name.view_name | awsdatacatalog.dbname.view_name | external_schema_name.view_name}
[FORCE] { AS (query_definition) | REMOVE DEFINITION }
```

## Parameters
<a name="r_ALTER_EXTERNAL_VIEW-parameters"></a>

 *schema\_name.view\_name*   
The schema that’s attached to your AWS Glue database, followed by the name of the view.

catalog\_name.schema\_name.view\_name \| awsdatacatalog.dbname.view\_name \| external\_schema\_name.view\_name  
The notation of the schema to use when altering the view. You can specify to use the AWS Glue Data Catalog, a Glue database that you created, or an external schema that you created. See [CREATE DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_DATABASE.html) and [CREATE EXTERNAL SCHEMA ](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_SCHEMA.html)for more information.

FORCE  
Whether AWS Lake Formation should update the definition of the view even if the objects referenced in the table are inconsistent with other SQL engines. If Lake Formation updates the view, the view is considered stale for the other SQL engines until those engines are updated as well.

 *AS query\_definition*   
The definition of the SQL query that Amazon Redshift runs to alter the view.

REMOVE DEFINITION  
Whether to drop and recreate the views. Views must be dropped and recreated to mark them as `PROTECTED`.

## Examples
<a name="r_ALTER_EXTERNAL_VIEW-examples"></a>

The following example alters a Data Catalog view named sample\_schema.glue\_data\_catalog\_view.

```
ALTER EXTERNAL VIEW sample_schema.glue_data_catalog_view
FORCE
REMOVE DEFINITION
```