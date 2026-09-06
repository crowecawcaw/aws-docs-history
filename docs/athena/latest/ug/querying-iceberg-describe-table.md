

# DESCRIBE
<a name="querying-iceberg-describe-table"></a>

Describes table information.

## Synopsis
<a name="querying-iceberg-describe-table-synopsis"></a>

```
DESCRIBE [FORMATTED] [{{db_name}}.]{{table_name}}
```

When the `FORMATTED` option is specified, the output displays additional information such as table location and properties.

## Example
<a name="querying-iceberg-describe-table-example"></a>

```
DESCRIBE iceberg_table
```