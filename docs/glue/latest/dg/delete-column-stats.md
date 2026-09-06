

# Deleting column statistics
<a name="delete-column-stats"></a>

You can delete column statistics using the [DeleteColumnStatisticsForTable](https://docs.aws.amazon.com/glue/latest/webapi/API_DeleteColumnStatisticsForTable.html) API operation or AWS CLI. The following example shows how to delete column statistics using AWS Command Line Interface (AWS CLI).

```
aws glue delete-column-statistics-for-table \
    --database-name '{{database_name}}' \
    --table-name '{{table_name}}' \
    --column-name '{{column_name}}'
```