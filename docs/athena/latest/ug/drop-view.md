

# DROP VIEW
<a name="drop-view"></a>

Drops (deletes) an existing Athena or AWS Glue Data Catalog view. The optional `IF EXISTS` clause causes the error to be suppressed if the view does not exist.

For Data Catalog views, drops the view only if Athena view syntax (dialect) is present in the Data Catalog view. For example, if a user calls `DROP VIEW` from Athena, the view is dropped only if the Athena dialect exists in the view. Otherwise, the operation fails. Dropping Data Catalog views requires Lake Formation admin or view definer permissions.

For more information, see [Work with views](views.md) and [Use Data Catalog views in Athena](views-glue.md).

## Synopsis
<a name="synopsis"></a>

```
DROP VIEW [ IF EXISTS ] {{view_name}}
```

## Examples
<a name="examples"></a>

```
DROP VIEW orders_by_date
```

```
DROP VIEW IF EXISTS orders_by_date
```

See also [CREATE VIEW and CREATE PROTECTED MULTI DIALECT VIEW](create-view.md), [SHOW COLUMNS](show-columns.md), [SHOW CREATE VIEW](show-create-view.md), [SHOW VIEWS](show-views.md), and [DESCRIBE VIEW](describe-view.md).