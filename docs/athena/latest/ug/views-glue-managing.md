# Manage Data Catalog views

You can use DDL commands to update and manage your Data Catalog views.

## Update a Data Catalog view

The `Lake Formation` admin or definer can use the `ALTER VIEW UPDATE
 DIALECT` syntax to update the view definition. The following example
modifies the view definition to select columns from the `returns` table
instead of the `orders` table.

```
ALTER VIEW orders_by_date UPDATE DIALECT
AS
SELECT return_date, sum(totalprice) AS price
FROM returns
WHERE order_city = 'SEATTLE'
GROUP BY orderdate
```

## Supported DDL actions for AWS Glue Data Catalog views

Athena supports the following actions for AWS Glue Data Catalog views.

| Statement                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ALTER VIEW DIALECT](alter-view-dialect.md "alter-view-dialect.md")                                                                            | Updates a Data Catalog view by either adding an engine dialect or<br>by updating or dropping an existing engine dialect.                                                                                                                                                                                                            |
| [CREATE PROTECTED MULTI DIALECT VIEW](create-view.md#create-protected-multi-dialect-view "create-view.md#create-protected-multi-dialect-view") | Creates a Data Catalog view from a specified `SELECT`<br>query. For more information, see [CREATE PROTECTED MULTI DIALECT VIEW](create-view.md#create-protected-multi-dialect-view "create-view.md#create-protected-multi-dialect-view").<br>The optional `OR REPLACE` clause lets you update<br>the existing view by replacing it. |
| [DESCRIBE VIEW](describe-view.md "describe-view.md")                                                                                           | Shows the list of columns for the named view. This allows you<br>to examine the attributes of a complex view.                                                                                                                                                                                                                       |
| [DROP VIEW](drop-view.md "drop-view.md")                                                                                                       | Deletes an existing view. The optional `IF EXISTS`<br>clause suppresses the error if the view does not exist.                                                                                                                                                                                                                       |
| [SHOW CREATE VIEW](show-create-view.md "show-create-view.md")                                                                                  | Shows the SQL statement that creates the specified<br>view.                                                                                                                                                                                                                                                                         |
| [SHOW VIEWS](show-views.md "show-views.md")                                                                                                    | Lists the views in the specified database, or in the current<br>database if you omit the database name. Use the optional<br>`LIKE` clause with a regular expression to<br>restrict the list of view names. You can also see the list of<br>views in the left pane in the console.                                                   |
| [SHOW COLUMNS](show-columns.md "show-columns.md")                                                                                              | Lists the columns in the schema for a view.                                                                                                                                                                                                                                                                                         |
