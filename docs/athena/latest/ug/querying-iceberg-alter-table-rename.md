

# ALTER TABLE RENAME
<a name="querying-iceberg-alter-table-rename"></a>

Renames a table.

Because the table metadata of an Iceberg table is stored in Amazon S3, you can update the database and table name of an Iceberg managed table without affecting underlying table information.

## Synopsis
<a name="querying-iceberg-alter-table-rename-synopsis"></a>

```
ALTER TABLE [{{db_name}}.]{{table_name}} RENAME TO [{{new_db_name}}.]{{new_table_name}}
```

## Example
<a name="querying-iceberg-alter-table-rename-example"></a>

```
ALTER TABLE my_db.my_table RENAME TO my_db2.my_table2
```