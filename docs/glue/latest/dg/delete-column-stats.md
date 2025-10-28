# Deleting column statistics

You can delete column statistics using the [DeleteColumnStatisticsForTable](../webapi/API_DeleteColumnStatisticsForTable.md "../webapi/API_DeleteColumnStatisticsForTable.md") API operation or AWS CLI. The following
example shows how to delete column statistics using AWS Command Line Interface (AWS CLI).

```
aws glue delete-column-statistics-for-table \
    --database-name '`database_name`' \
    --table-name '`table_name`' \
    --column-name '`column_name`'

```
