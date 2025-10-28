# Working with AWS Glue Data Catalog views in AWS Glue

You can create and manage views in the AWS Glue Data Catalog, commonly known as AWS Glue Data Catalog views. These views are useful because they support multiple SQL
query engines, allowing you to access the same view across different AWS services, such as Amazon Athena, Amazon Redshift, and AWS Glue.
You can use views based on Apache Iceberg, Apache Hudi, and Delta Lake.

By creating a view in the Data Catalog, you can use resource grants and tag-based access controls in AWS Lake Formation to grant access to it.
Using this method of access control, you don't have to configure additional access to the tables referenced when creating the view. This method of
granting permissions is called definer semantics, and these views are called definer views. For more information about access control in
AWS Lake Formation, see [Granting and revoking permissions on Data Catalog resources](../../../lake-formation/latest/dg/granting-catalog-permissions.md "../../../lake-formation/latest/dg/granting-catalog-permissions.md") in the AWS Lake Formation Developer Guide.

Data Catalog views are useful for the following use cases:

- **Granular access control** – You can create a view that restricts data access based on the permissions the user
  needs. For example, you can use views in the Data Catalog to prevent employees who don't work in the HR department from seeing personally identifiable
  information (PII).
- **Complete view definition** – By applying filters on your view in the Data Catalog, you ensure that data records
  available in the view are always complete.
- **Enhanced security** – The query definition used to create the view must be complete, making Data Catalog views
  less susceptible to SQL commands from malicious actors.
- **Simple data sharing** – Share data with other AWS accounts without moving data, using cross-account data
  sharing in AWS Lake Formation.

## Creating a Data Catalog view

You can create Data Catalog views using the AWS CLI and AWS Glue ETL scripts using Spark SQL. The syntax for creating a Data Catalog view includes specifying
the view type as `MULTI DIALECT` and the `SECURITY` predicate as `DEFINER`, indicating a definer view.

Example SQL statement to create a Data Catalog view:

```
CREATE PROTECTED MULTI DIALECT VIEW database_name.catalog_view SECURITY DEFINER
AS SELECT order_date, sum(totalprice) AS price
FROM source_table
GROUP BY order_date;
```

After creating a Data Catalog view, you can use an IAM role with the AWS Lake Formation `SELECT` permission on the view to query it from
services like Amazon Athena, Amazon Redshift, or AWS Glue ETL jobs. You don't need to grant access to the underlying tables referenced
in the view.

For more information on creating and configuring Data Catalog views, see
[Building AWS Glue Data Catalog views](../../../lake-formation/latest/dg/working-with-views.md "../../../lake-formation/latest/dg/working-with-views.md") in the
AWS Lake Formation Developer Guide.

## Supported view operations

The following command fragments show you various ways to work with Data Catalog views:

**CREATE VIEW**

Creates a data-catalog view. The following is a sample that shows creating a view from an existing table:

```
CREATE PROTECTED MULTI DIALECT VIEW catalog_view
SECURITY DEFINER AS SELECT * FROM my_catalog.my_database.source_table
```

**ALTER VIEW**

Available syntax:

```
ALTER VIEW view_name [FORCE] ADD DIALECT AS query
ALTER VIEW view_name [FORCE] UPDATE DIALECT AS query
ALTER VIEW view_name DROP DIALECT

```

You can use the `FORCE ADD DIALECT` option to force update the schema and sub objects as per the new engine dialect. Note that doing this
can result in query errors if you don't also use `FORCE` to update other engine dialects. The following shows a sample:

```
ALTER VIEW catalog_view FORCE ADD DIALECTAS
SELECT order_date, sum(totalprice) AS priceFROM source_tableGROUP BY orderdate;
```

The following shows how to alter a view in order to update the dialect:

```
ALTER VIEW catalog_view UPDATE DIALECT AS
SELECT count(*) FROM my_catalog.my_database.source_table;
```

**DESCRIBE VIEW**

Available syntax for describing a view:

`SHOW COLUMNS {FROM|IN} view_name [{FROM|IN} database_name]` – If the user has the required AWS Glue and AWS Lake Formation
permissions to describe the view, they can list the columns. The following shows a couple sample commands for showing columns:

```
SHOW COLUMNS FROM my_database.source_table;
SHOW COLUMNS IN my_database.source_table;
```

`DESCRIBE view_name` – If the user has the required AWS Glue and AWS Lake Formation permissions to describe the view, they can
list the columns in the view along with its metadata.

**DROP VIEW**

Available syntax:

```
DROP VIEW [ IF EXISTS ] view_name
```

The following sample shows a `DROP` statement that tests if a view exists prior to dropping it:

```
DROP VIEW IF EXISTS catalog_view;
```

`SHOW CREATE VIEW view_name` – Shows the SQL statement that creates the specified view. The following is a sample that shows
creating a data-catalog view:

```
SHOW CREATE TABLE my_database.catalog_view;CREATE PROTECTED MULTI DIALECT VIEW my_catalog.my_database.catalog_view (
  net_profit,
  customer_id,
  item_id,
  sold_date)
TBLPROPERTIES (
  'transient_lastDdlTime' = '1736267222')
SECURITY DEFINER AS SELECT * FROM
my_database.store_sales_partitioned_lf WHERE customer_id IN (SELECT customer_id from source_table limit 10)
```

**SHOW VIEWS**

List all views in the catalog, such as regular views, multi-dialect views (MDV), and MDV without Spark dialect. Available syntax is the following:

```
SHOW VIEWS [{ FROM | IN } database_name] [LIKE regex_pattern]:
```

The following shows a sample command to show views:

```
SHOW VIEWS IN marketing_analytics LIKE 'catalog_view*';
```

For more information about creating and configuring data-catalog views, see
[Building AWS Glue Data Catalog views](../../../lake-formation/latest/dg/working-with-views.md "../../../lake-formation/latest/dg/working-with-views.md") in the AWS Lake Formation Developer Guide.

## Querying a Data Catalog view

After creating a Data Catalog view, you can query the view. The IAM role configured in your AWS Glue jobs must have the Lake Formation
**SELECT** permission on the Data Catalog view. You don't need to grant access to the underlying tables referenced in
the view.

Once you have everything set up, you can query your view. For example, you can run the following query to access a view.

```
SELECT * from my_database.catalog_view LIMIT 10;
```

## Limitations

Consider the following limitations when you use Data Catalog views.

- You can only create Data Catalog views with AWS Glue 5.0 and above.
- The Data Catalog view definer must have `SELECT` access to the underlying base tables accessed by the view. Creating the Data
  Catalog view fails if a specific base table has any Lake Formation filters imposed on the definer role.
- Base tables must not have the `IAMAllowedPrincipals` data lake permission in AWS Lake Formation. If present, the
  error **Multi Dialect views may only reference tables without IAMAllowedPrincipals permissions occurs**.
- The table's Amazon S3 location must be registered as a AWS Lake Formation data lake location. If the table isn't registered, the error
  `Multi Dialect views may only reference AWS Lake Formation managed tables` occurs. For information about how to register
  Amazon Amazon S3 locations in AWS Lake Formation, see
  [Registering an Amazon S3 location](../../../lake-formation/latest/dg/register-data-lake.md "../../../lake-formation/latest/dg/register-data-lake.md") in the AWS Lake Formation Developer Guide.
- You can only create `PROTECTED` Data Catalog views. `UNPROTECTED` views aren't supported.
- You can't reference tables in another AWS account in a Data Catalog view definition. You also can't reference a table in the same account
  that's in a separate region.
- To share data across an account or region, the entire view must be shared cross account and cross region, using AWS Lake Formation
  resource links.
- User-defined functions (UDFs) aren't supported.
- You can't reference other views in Data Catalog views.
