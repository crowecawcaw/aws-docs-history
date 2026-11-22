

# SHOW TBLPROPERTIES

Shows one or more table properties of an Iceberg table. Only Athena-supported table properties are shown.

## Synopsis
<a name="querying-iceberg-show-table-properties-synopsis"></a>

```sql
SHOW TBLPROPERTIES [{{db_name}}.]{{table_name}} [('{{property_name}}')]
```

## Example
<a name="querying-iceberg-show-table-properties-example"></a>

```sql
SHOW TBLPROPERTIES iceberg_table
```