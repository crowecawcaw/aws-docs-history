# Working with Glue Data Catalog views in Amazon EMR

###### Note

Creating and managing AWS Glue Data Catalog views for use with EMR on EC2 is available with [Amazon EMR release 7.10.0](../ReleaseGuide/emr-7100-release.md "../ReleaseGuide/emr-7100-release.md") and later.

You can create and manage views in the AWS Glue Data Catalog for use with EMR on EC2. These are known commonly as AWS Glue Data Catalog views. These views are useful because they support multiple SQL query engines, so you
can access the same view across different AWS services, such as EMR on EC2, Amazon Athena, and Amazon Redshift.

By creating a view in the Data Catalog, you can use resource grants and tag-based access controls in AWS Lake Formation to grant access to it. Using this method
of access control, you don't have to configure additional access to the tables you referenced when creating the view. This method of granting permissions is called
definer semantics, and these views are called definer views. For more information about access control in Lake Formation, see
[Granting and revoking permissions on Data Catalog resources](../../../lake-formation/latest/dg/granting-catalog-permissions.md "../../../lake-formation/latest/dg/granting-catalog-permissions.md") in
the AWS Lake Formation Developer Guide.

Data Catalog views are useful for the following use cases:

- **Granular access control** – You can create a view that restricts data access based on the permissions the user needs. For example, you
  can use views in the Data Catalog to prevent employees who don’t work in the HR department from seeing personally identifiable information (PII).
- **Complete view definition** – By applying filters on your view in the Data Catalog, you make sure that data records available in a view
  in the Data Catalog are always complete.
- **Enhanced security** – The query definition used to create the view must be complete. This benefit means that views in
  the Data Catalog are less susceptible to SQL commands from malicious actors.
- **Simple sharing data** – Share data with other AWS accounts without moving data. For more information,
  see [Cross-account data sharing in Lake Formation](../../../lake-formation/latest/dg/cross-account-permissions.md "../../../lake-formation/latest/dg/cross-account-permissions.md").

## Creating a Data Catalog view

There are different ways to create a Data Catalog view. These include using the AWS CLI or Spark SQL. A few examples follow.

Using SQL The following shows the syntax for creating a Data Catalog view. Note the `MULTI DIALECT` view type. This distinguishes the Data Catalog view from other views. The `SECURITY` predicate
is specified as `DEFINER`. This indicates a Data Catalog view with `DEFINER` semantics.

```
CREATE [ OR REPLACE ] PROTECTED MULTI DIALECT VIEW [IF NOT EXISTS] view_name
[(column_name [COMMENT column_comment], ...) ]
[ COMMENT view_comment ]
[TBLPROPERTIES (property_name = property_value, ... )]
SECURITY DEFINER
AS query;
```

The following is a sample `CREATE` statement, following the syntax:

```
CREATE PROTECTED MULTI DIALECT VIEW catalog_view
SECURITY DEFINER
AS
SELECT order_date, sum(totalprice) AS price
FROM source_table
GROUP BY order_date
```

You can also create a view in dry-run mode, using SQL, to test view creation, without actually creating the resource. Using this option results in a "dry run"
that validates the input and, if the validation succeeds, returns the JSON of the AWS Glue table object that will represent
the view. In this case, The actual view isn't created.

```
CREATE [ OR REPLACE ] PROTECTED MULTI DIALECT VIEW `view_name`
SECURITY DEFINER
[ SHOW VIEW JSON ]
AS `view-sql`
```

Using the AWS CLI

###### Note

When you use the CLI command, the SQL used to create the view isn't parsed. This can result in a case where the view is created, but queries aren't successful. Be sure to test your SQL
syntax prior to creating the view.

You use the following CLI command to create a view:

```
aws glue create-table --cli-input-json '{
  "DatabaseName": "`database`",
  "TableInput": {
    "Name": "`view`",
    "StorageDescriptor": {
      "Columns": [
        {
          "Name": "`col1`",
          "Type": "`data-type`"
        },
        ...
        {
          "Name": "`col_n`",
          "Type": "`data-type`"
        }
      ],
      "SerdeInfo": {}
    },
    "ViewDefinition": {
      "SubObjects": [
        "arn:aws:glue:`aws-region`:`aws-account-id`:table/`database`/`referenced-table1`",
        ...
        "arn:aws:glue:`aws-region`:`aws-account-id`:table/`database`/`referenced-tableN`",
       ],
      "IsProtected": true,
      "Representations": [
        {
          "Dialect": "SPARK",
          "DialectVersion": "1.0",
          "ViewOriginalText": "`Spark-SQL`",
          "ViewExpandedText": "`Spark-SQL`"
        }
      ]
    }
  }
}'
```

## Supported view operations

The following command fragments show you various ways to work with Data Catalog views:

- **CREATE VIEW**

Creates a data-catalog view. The following is a sample that shows creating a view from an existing table:

```
CREATE PROTECTED MULTI DIALECT VIEW catalog_view
SECURITY DEFINER AS SELECT * FROM my_catalog.my_database.source_table
```

- **ALTER VIEW**

Available syntax:

    + `ALTER VIEW view_name [FORCE] ADD DIALECT AS query`
    + `ALTER VIEW view_name [FORCE] UPDATE DIALECT AS query`
    + `ALTER VIEW view_name DROP DIALECT`

You can use the `FORCE ADD DIALECT` option to force update the schema and sub objects as per the new engine dialect. Note that doing this can result in query errors if you don't also use `FORCE` to update
other engine dialects. The following shows a sample:

```
ALTER VIEW catalog_view FORCE ADD DIALECT
AS
SELECT order_date, sum(totalprice) AS price
FROM source_table
GROUP BY orderdate;
```

The following shows how to alter a view in order to update the dialect:

```
ALTER VIEW catalog_view UPDATE DIALECT AS
SELECT count(*) FROM my_catalog.my_database.source_table;
```

- **DESCRIBE VIEW**

Available syntax for describing a view:

    + `SHOW COLUMNS {FROM|IN} view_name [{FROM|IN} database_name]` – If the user has the required AWS Glue and Lake Formation permissions to describe the view, they
     can list the columns. The following shows a couple sample commands for showing columns:



    ```
    SHOW COLUMNS FROM my_database.source_table;
    SHOW COLUMNS IN my_database.source_table;
    ```
    + `DESCRIBE view_name` – If the user has the required AWS Glue and Lake Formation permissions to describe the view, they can list the columns in the view
     along with its metadata.

- **DROP VIEW**

Available syntax:

    + `DROP VIEW [ IF EXISTS ] view_name`


    The following sample shows a `DROP` statement that tests if a view exists prior to dropping it:



    ```
    DROP VIEW IF EXISTS catalog_view;
    ```

- **SHOW CREATE VIEW**
  - `SHOW CREATE VIEW view_name` – Shows the SQL statement that creates the specified view. The following is a sample that shows creating a data-catalog view:

  ```
  SHOW CREATE TABLE my_database.catalog_view;
  CREATE PROTECTED MULTI DIALECT VIEW my_catalog.my_database.catalog_view (
    net_profit,
    customer_id,
    item_id,
    sold_date)
  TBLPROPERTIES (
    'transient_lastDdlTime' = '1736267222')
  SECURITY DEFINER AS SELECT * FROM
  my_database.store_sales_partitioned_lf WHERE customer_id IN (SELECT customer_id from source_table limit 10)
  ```

- **SHOW VIEWS**

List all views in the catalog such asregular views, multi-dialect views (MDV), and MDV without Spark dialect. Available syntax is the following:

    + `SHOW VIEWS [{ FROM | IN } database_name] [LIKE regex_pattern]`:


    The following shows a sample command to show views:



    ```
    SHOW VIEWS IN marketing_analytics LIKE 'catalog_view*';
    ```

For more information about creating and configuring data-catalog views, see [Building AWS Glue Data Catalog views](../../../lake-formation/latest/dg/working-with-views.md "../../../lake-formation/latest/dg/working-with-views.md") in the AWS Lake Formation Developer Guide.

## Querying a Data Catalog view

After creating a Data Catalog view, you can query it using an Amazon EMR Spark job that has AWS Lake Formation fine-grained access control enabled. The job runtime role must have the Lake Formation
`SELECT` permission on the Data Catalog view. You don't need to grant access to the underlying tables referenced in the view.

Once you have everything set up, you can query your view. For example, after creating an Amazon EMR application in EMR Studio, you can run the following query to access a view.

```
SELECT * from `my_database`.`catalog_view` LIMIT 10;
```

A helpful function is the `invoker_principal`. It returns the unique identifier of the EMRS job runtime role. This can be used to
control the view output, based on the invoking principal. You can use this to add a condition in your view that refines query results, based on the calling role. The job runtime role must have
permission to the `LakeFormation:GetDataLakePrincipal` IAM action to use this function.

```
select invoker_principal();
```

You can add this function to a `WHERE` clause, for instance, to refine query results.

## Considerations and limitations

When you create Data Catalog views, the following apply:

- You can only create Data Catalog views with Amazon EMR 7.10 and above.
- The Data Catalog view definer must have `SELECT` access to the underlying base tables accessed by the view. Creating the Data Catalog view fails if a specific base table has any Lake Formation
  filters imposed on the definer role.
- Base tables must not have the `IAMAllowedPrincipals` data lake permission in Lake Formation. If present, the error _Multi Dialect views may only reference tables without IAMAllowedPrincipals permissions_ occurs.
- The table's Amazon S3 location must be registered as a Lake Formation data lake location. If the table isn't registered, the error _Multi Dialect views may only reference Lake Formation managed tables_ occurs. For information
  about how to register Amazon S3 locations in Lake Formation, see [Registering an Amazon S3 location](../../../lake-formation/latest/dg/register-location.md "../../../lake-formation/latest/dg/register-location.md") in the AWS Lake Formation Developer Guide.
- You can only create `PROTECTED` Data Catalog views. `UNPROTECTED` views aren't supported.
- You can't reference tables in another AWS account in a Data Catalog view definition. You also can't reference a table in the same account that's
  in a separate region.
- To share data across an account or region, the entire view must be be shared cross account and cross region, using Lake Formation resource links.
- User-defined functions (UDFs) aren't supported.
- You can use views based on Iceberg tables. The open-table formats Apache Hudi and Delta Lake are also supported.
- You can't reference other views in Data Catalog views.
- An AWS Glue Data Catalog view schema is always stored using lowercase. For example, if you use a DDL statement to create a Glue Data Catalog view with a column named `Castle`, the column
  created in the Glue Data Catalog will be made lowercase, to `castle`. If you then specify the column name in a DML query as `Castle` or `CASTLE`, EMR Spark will make the name lowercase
  for you in order to run the query. But the column heading displays using the casing that you specified in the query.

If you want a query to fail in a case where a column name specified in the DML query does not match the column name in the Glue Data Catalog, you can set `spark.sql.caseSensitive=true`.
