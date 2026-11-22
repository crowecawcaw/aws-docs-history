

# ALTER TABLE UNSET TBLPROPERTIES

Drops existing properties from an Iceberg table.

## Synopsis
<a name="querying-iceberg-alter-table-unset-properties-synopsis"></a>

```sql
ALTER TABLE [{{db_name}}.]{{table_name}} UNSET TBLPROPERTIES ('{{property_name}}' [ , ... ])
```

## Example
<a name="querying-iceberg-alter-table-unset-properties-example"></a>

```sql
ALTER TABLE iceberg_table UNSET TBLPROPERTIES ('write_compression')
```

The following example removes the `write.data.path` property from an Iceberg table.

```sql
ALTER TABLE iceberg_table UNSET TBLPROPERTIES ('write.data.path')
```