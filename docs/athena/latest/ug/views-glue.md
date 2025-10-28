# Use Data Catalog views in Athena

Creating Data Catalog views in Amazon Athena requires a special `CREATE VIEW` statement.
Querying them uses conventional SQL `SELECT` syntax. Data Catalog views are also
referred to as _multi dialect_ views, or MDVs.

## Create a Data Catalog view

To create a Data Catalog view in Athena, use the following syntax.

```
CREATE [ OR REPLACE ] PROTECTED MULTI DIALECT VIEW `view_name`
SECURITY DEFINER
[ SHOW VIEW JSON ]
AS `athena-sql-statement`
```

###### Note

The `SHOW VIEW JSON` option applies to Data Catalog views only and not to
Athena views. Using the `SHOW VIEW JSON` option performs a "dry run" that
validates the input and, if the validation succeeds, returns the JSON of the AWS Glue
table object that will represent the view. The actual view is not created. If the
`SHOW VIEW JSON` option is not specified, validations are done and
the view is created as usual in the Data Catalog.

The following example shows how a user of the `Definer` role creates the
`orders_by_date` Data Catalog view. The example assumes that the
`Definer` role has full `SELECT` permissions on the
`orders` table in the `default` database.

```
CREATE PROTECTED MULTI DIALECT VIEW orders_by_date
SECURITY DEFINER
AS
SELECT orderdate, sum(totalprice) AS price
FROM orders
WHERE order_city = 'SEATTLE'
GROUP BY orderdate
```

For syntax information, see [CREATE PROTECTED MULTI
DIALECT VIEW](create-view.md#create-protected-multi-dialect-view "create-view.md#create-protected-multi-dialect-view").

## Query a Data Catalog view

After the view is created, the `Lake Formation` admin can grant `SELECT`
permissions on the Data Catalog view to the `Invoker` principals. The
`Invoker` principals can then query the view without having access to the
underlying base tables referenced by the view. The following is an example
`Invoker` query.

```
SELECT * from orders_by_date where price > 5000
```

## Considerations and limitations

Most of the following Data Catalog view limitations are specific to Athena. For additional
limitations on Data Catalog views that also apply to other services, see the Lake Formation
documentation.

- Data Catalog views cannot reference other views, database resource links, or table
  resource links.
- You can reference up to 10 tables in the view definition.
- Tables must not have the `IAMAllowedPrincipals` data lake
  permission in Lake Formation. If present, the error **`Multi Dialect views may
only reference tables without IAMAllowedPrincipals permissions`**
  occurs.
- The table's Amazon S3 location must be registered as a Lake Formation data lake location. If
  the table is not so registered, the error **`Multi Dialect views may
only reference Lake Formation managed tables`** occurs. For
  information about how to register Amazon S3 locations in Lake Formation, see [Registering an Amazon S3 location](../../../lake-formation/latest/dg/register-location.md "../../../lake-formation/latest/dg/register-location.md") in the _AWS Lake Formation Developer Guide_.
- The AWS Glue [GetTables](../../../glue/latest/webapi/API_GetTables.md "../../../glue/latest/webapi/API_GetTables.md") and [SearchTables](../../../glue/latest/webapi/API_SearchTables.md "../../../glue/latest/webapi/API_SearchTables.md") API calls do not update the
  `IsRegisteredWithLakeFormation` parameter. To view the correct
  value for the parameter, use the AWS Glue [GetTable](../../../glue/latest/webapi/API_GetTable.md "../../../glue/latest/webapi/API_GetTable.md") API. For more
  information, see [GetTables and SearchTables APIs do not update the value for the
  IsRegisteredWithLakeFormation parameter](../../../lake-formation/latest/dg/limitations.md#issue-GetTables-value "../../../lake-formation/latest/dg/limitations.md#issue-GetTables-value") in the _AWS Lake Formation Developer Guide_.
- The `DEFINER` principal can be only an IAM role.
- The `DEFINER` role must have full `SELECT` (grantable)
  permissions on the underlying tables.
- `UNPROTECTED` Data Catalog views are not supported.
- User-defined functions (UDFs) are not supported in the view definition.
- Athena federated data sources cannot be used in Data Catalog views.
- Data Catalog views are not supported for external Hive
  metastores.
- Athena displays an error message when it detects stale views. A stale view is
  reported when one of the following occurs:
  - The view references tables or databases that do not exist.
  - A schema or metadata change is made in a referenced table.
  - A referenced table is dropped and recreated with a different schema or
    configuration.

## Permissions

Data Catalog views require three roles: `Lake Formation Admin`, `Definer`, and
`Invoker`.

- `Lake Formation Admin` – Has access to
  configure all Lake Formation permissions.
- `Definer` – Creates the
  Data Catalog view. The `Definer` role must have full grantable
  `SELECT` permissions on all underlying tables that the view
  definition references.
- `Invoker` – Can query the
  Data Catalog view or check its metadata. To show the invoker of a query, you can use
  the `invoker_principal()` DML function. For more information, see
  [invoker_principal()](functions-env3.md#functions-env3-invoker-principal "functions-env3.md#functions-env3-invoker-principal").

The `Definer` role's trust relationships must allow the
`sts:AssumeRole` action for the AWS Glue and Lake Formation service principals. For
more information, see [Prerequisites
for creating views](../../../lake-formation/latest/dg/working-with-views.md#views-prereqs "../../../lake-formation/latest/dg/working-with-views.md#views-prereqs") in the _AWS Lake Formation Developer Guide_.

IAM permissions for Athena access are also required. For more information, see [AWS managed policies for Amazon Athena](managed-policies.md "managed-policies.md").
