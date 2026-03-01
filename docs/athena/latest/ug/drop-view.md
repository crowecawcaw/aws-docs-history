# DROP VIEW

Drops (deletes) an existing Athena or AWS Glue Data Catalog view. The optional `IF EXISTS`
clause causes the error to be suppressed if the view does not exist.

For Data Catalog views, drops the view only if Athena view syntax (dialect) is present in the
Data Catalog view. For example, if a user calls `DROP VIEW` from Athena, the view is
dropped only if the Athena dialect exists in the view. Otherwise, the operation fails.
Dropping Data Catalog views requires Lake Formation admin or view definer permissions.

For more information, see [Work with views](views.md "views.md") and [Use Data Catalog views in Athena](views-glue.md "views-glue.md").

## Synopsis

```
DROP VIEW [ IF EXISTS ] `view_name`
```

## Examples

```
DROP VIEW orders_by_date
```

```
DROP VIEW IF EXISTS orders_by_date
```

See also [CREATE VIEW and CREATE PROTECTED MULTI DIALECT VIEW](create-view.md "create-view.md"), [SHOW COLUMNS](show-columns.md "show-columns.md"), [SHOW CREATE VIEW](show-create-view.md "show-create-view.md"), [SHOW VIEWS](show-views.md "show-views.md"), and [DESCRIBE VIEW](describe-view.md "describe-view.md").
