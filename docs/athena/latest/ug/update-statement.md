

# UPDATE
<a name="update-statement"></a>

Updates rows in an Apache Iceberg table. `UPDATE` is transactional and is supported only for Apache Iceberg tables. The statement works only on existing rows and cannot be used to insert or append a row.

## Synopsis
<a name="update-statement-synopsis"></a>

To update the rows in an Iceberg table, use the following syntax.

```
UPDATE [{{db_name}}.]{{table_name}} SET xx=yy[,...] [WHERE {{predicate}}]
```

For more information and examples, see the `UPDATE` section of [Update Iceberg table data](querying-iceberg-updating-iceberg-table-data.md).