# ALTER TABLE RENAME

Renames a table.

Because the table metadata of an Iceberg table is stored in Amazon S3, you can update
the database and table name of an Iceberg managed table without affecting underlying
table information.

## Synopsis

```
ALTER TABLE [`db_name`.]`table_name` RENAME TO [`new_db_name`.]`new_table_name`
```

## Example

```
ALTER TABLE my_db.my_table RENAME TO my_db2.my_table2
```
