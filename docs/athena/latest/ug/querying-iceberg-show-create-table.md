

# SHOW CREATE TABLE

Displays a `CREATE TABLE` DDL statement that can be used to recreate the Iceberg table in Athena. If Athena cannot reproduce the table structure (for example, because custom table properties are specified in the table), an `UNSUPPORTED` error is thrown.

## Synopsis
<a name="querying-iceberg-show-create-table-synopsis"></a>

```sql
SHOW CREATE TABLE [{{db_name}}.]{{table_name}}
```

## Example
<a name="querying-iceberg-show-create-table-example"></a>

```sql
SHOW CREATE TABLE iceberg_table
```