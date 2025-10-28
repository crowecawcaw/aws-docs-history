# DROP TABLE

Drops an Iceberg table.

###### Warning

Because Iceberg tables are considered managed tables in Athena, dropping an
Iceberg table also removes all the data in the table.

## Synopsis

```
DROP TABLE [IF EXISTS] [`db_name`.]`table_name`
```

## Example

```
DROP TABLE iceberg_table
```
