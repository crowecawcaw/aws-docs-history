

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# DROP EXTERNAL VIEW
<a name="r_DROP_EXTERNAL_VIEW"></a>

Drops an external view from the database. Dropping an external view removes it from all SQL engines the view is associated with, such as Amazon Athena and Amazon EMR Spark. This command can't be reversed. For more information about Data Catalog views, see [AWS Glue Data Catalog views](https://docs.aws.amazon.com/redshift/latest/dg/data-catalog-views-overview.html).

## Syntax
<a name="r_DROP_EXTERNAL_VIEW-synopsis"></a>

```
DROP EXTERNAL VIEW schema_name.view_name [ IF EXISTS ]
{catalog_name.schema_name.view_name | awsdatacatalog.dbname.view_name | external_schema_name.view_name}
```

## Parameters
<a name="r_DROP_EXTERNAL_VIEW-parameters"></a>

 *schema\_name.view\_name*   
The schema that’s attached to your AWS Glue database, followed by the name of the view.

IF EXISTS  
Drops the view only if it exists.

catalog\_name.schema\_name.view\_name \| awsdatacatalog.dbname.view\_name \| external\_schema\_name.view\_name  
The notation of the schema to use when dropping the view. You can specify to use the AWS Glue Data Catalog, a Glue database that you created, or an external schema that you created. See [CREATE DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_DATABASE.html) and [CREATE EXTERNAL SCHEMA ](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_SCHEMA.html) for more information.

 *query\_definition*   
The definition of the SQL query that Amazon Redshift runs to alter the view.

## Examples
<a name="r_DROP_EXTERNAL_VIEW-examples"></a>

The following example drops a Data Catalog view named sample\_schema.glue\_data\_catalog\_view.

```
DROP EXTERNAL VIEW sample_schema.glue_data_catalog_view IF EXISTS
```