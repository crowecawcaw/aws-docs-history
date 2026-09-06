

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# CREATE EXTERNAL VIEW
<a name="r_CREATE_EXTERNAL_VIEW"></a>

The Data Catalog views preview feature is available only in the following Regions.
+ US East (Ohio) (us-east-2)
+ US East (N. Virginia) (us-east-1)
+ US West (N. California) (us-west-1)
+ Asia Pacific (Tokyo) (ap-northeast-1)
+ Europe (Ireland) (eu-west-1)
+ Europe (Stockholm) (eu-north-1)

Creates a view in the Data Catalog. Data Catalog views are a single view schema that works with other SQL engines such as Amazon Athena and Amazon EMR. You can query the view from your choice of engine. For more information about Data Catalog views, see [Creating Data Catalog views](https://docs.aws.amazon.com/redshift/latest/dg/data-catalog-views-overview.html).

## Syntax
<a name="r_CREATE_EXTERNAL_VIEW-synopsis"></a>

```
CREATE EXTERNAL VIEW schema_name.view_name [ IF NOT EXISTS ]
{catalog_name.schema_name.view_name | awsdatacatalog.dbname.view_name | external_schema_name.view_name}
AS query_definition;
```

## Parameters
<a name="r_CREATE_EXTERNAL_VIEW-parameters"></a>

 *schema\_name.view\_name*   
The schema that’s attached to your AWS Glue database, followed by the name of the view.

PROTECTED  
Specifies that the CREATE EXTERNAL VIEW command should only complete if the query within the query\_definition can successfully complete.

IF NOT EXISTS  
Creates the view if the view doesn’t already exist.

catalog\_name.schema\_name.view\_name \| awsdatacatalog.dbname.view\_name \| external\_schema\_name.view\_name  
The notation of the schema to use when creating the view. You can specify to use the AWS Glue Data Catalog, a Glue database that you created, or an external schema that you created. See [CREATE DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_DATABASE.html) and [CREATE EXTERNAL SCHEMA ](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_SCHEMA.html)for more information.

 *query\_definition*   
The definition of the SQL query that Amazon Redshift runs to alter the view.

## Examples
<a name="r_CREATE_EXTERNAL_VIEW-examples"></a>

The following example creates a Data Catalog view named sample\_schema.glue\_data\_catalog\_view.

```
CREATE EXTERNAL PROTECTED VIEW sample_schema.glue_data_catalog_view IF NOT EXISTS
AS SELECT * FROM sample_database.remote_table "remote-table-name";
```