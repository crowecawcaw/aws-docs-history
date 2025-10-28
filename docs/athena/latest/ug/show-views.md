# SHOW VIEWS

Lists the Athena or Data Catalog views in a list of `STRING` type values. Each value
in the list is the name of a view in the specified database, or in the current database if
you omit the database name. Use the optional `LIKE` clause with a regular
expression to restrict the list of view names. For Data Catalog views, lists only the views that
use Athena SQL syntax. Other Data Catalog views are filtered out.

## Synopsis

```
SHOW VIEWS [IN `database_name`] [LIKE '`regular_expression`']
```

### Parameters

**[IN database\_name]**

Specifies the `database_name` from which views will be
listed. If omitted, the database from the current context is
assumed.

**[LIKE 'regular\_expression']**

Filters the list of views to those that match the
`regular_expression` you specify. Only the wild card
character `*`, which indicates any character, or
`|`, which indicates a choice between characters, can be
used.

## Examples

```
SHOW VIEWS
```

```
SHOW VIEWS IN marketing_analytics LIKE 'orders*'
```

See also [SHOW COLUMNS](show-columns.md "show-columns.md"), [SHOW CREATE VIEW](show-create-view.md "show-create-view.md"), [DESCRIBE VIEW](describe-view.md "describe-view.md"), and [DROP VIEW](drop-view.md "drop-view.md").
