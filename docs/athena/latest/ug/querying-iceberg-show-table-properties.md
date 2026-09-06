

# SHOW TBLPROPERTIES
<a name="querying-iceberg-show-table-properties"></a>

Shows one or more table properties of an Iceberg table. Only Athena-supported table properties are shown.

## Synopsis
<a name="querying-iceberg-show-table-properties-synopsis"></a>

```
SHOW TBLPROPERTIES [{{db_name}}.]{{table_name}} [('{{property_name}}')]
```

## Example
<a name="querying-iceberg-show-table-properties-example"></a>

```
SHOW TBLPROPERTIES iceberg_table
```