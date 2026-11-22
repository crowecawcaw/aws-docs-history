

# ALTER TABLE DROP COLUMN

Drops a column from an existing Iceberg table.

## Synopsis
<a name="querying-iceberg-alter-table-drop-column-synopsis"></a>

```sql
ALTER TABLE [{{db_name}}.]{{table_name}} DROP COLUMN {{col_name}}
```

## Example
<a name="querying-iceberg-alter-table-drop-column-example"></a>

```sql
ALTER TABLE iceberg_table DROP COLUMN userid
```