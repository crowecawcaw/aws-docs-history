# ALTER TABLE UNSET TBLPROPERTIES

Drops existing properties from an Iceberg table.

## Synopsis

```
ALTER TABLE [`db_name`.]`table_name` UNSET TBLPROPERTIES ('`property_name`' [ , ... ])
```

## Example

```
ALTER TABLE iceberg_table UNSET TBLPROPERTIES ('write_compression')
```
