# SHOW TBLPROPERTIES

Shows one or more table properties of an Iceberg table. Only Athena-supported table
properties are shown.

## Synopsis

```
SHOW TBLPROPERTIES [`db_name`.]`table_name` [('`property_name`')]
```

## Example

```
SHOW TBLPROPERTIES iceberg_table
```
