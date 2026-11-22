

# SHOW CREATE VIEW

Shows the SQL statement that created the specified Athena or Data Catalog view. The SQL returned shows the create view syntax used in Athena. Calling `SHOW CREATE VIEW` on Data Catalog views requires Lake Formation admin or view definer permissions.

## Synopsis
<a name="synopsis"></a>

```sql
SHOW CREATE VIEW {{view_name}}
```

## Examples
<a name="examples"></a>

```sql
SHOW CREATE VIEW orders_by_date
```

See also [CREATE VIEW and CREATE PROTECTED MULTI DIALECT VIEW](create-view.md) and [DROP VIEW](drop-view.md).