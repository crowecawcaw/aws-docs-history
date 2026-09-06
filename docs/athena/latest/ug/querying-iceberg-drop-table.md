

# DROP TABLE
<a name="querying-iceberg-drop-table"></a>

Drops an Iceberg table.

**Warning**  
Because Iceberg tables are considered managed tables in Athena, dropping an Iceberg table also removes all the data in the table.

## Synopsis
<a name="querying-iceberg-drop-table-synopsis"></a>

```
DROP TABLE [IF EXISTS] [{{db_name}}.]{{table_name}}
```

## Example
<a name="querying-iceberg-drop-table-example"></a>

```
DROP TABLE iceberg_table
```