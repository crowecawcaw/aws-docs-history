

# ALTER TABLE DROP COLUMN
<a name="querying-iceberg-alter-table-drop-column"></a>

Drops a column from an existing Iceberg table.

## Synopsis
<a name="querying-iceberg-alter-table-drop-column-synopsis"></a>

```
ALTER TABLE [{{db_name}}.]{{table_name}} DROP COLUMN {{col_name}}
```

## Example
<a name="querying-iceberg-alter-table-drop-column-example"></a>

```
ALTER TABLE iceberg_table DROP COLUMN userid
```