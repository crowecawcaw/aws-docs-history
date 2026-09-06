

# Stopping column statistics task run
<a name="stop-stats-run"></a>

You can stop a column statistics task run for a table using AWS Glue console, AWS CLI or using [StopColumnStatisticsTaskRun](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html#aws-glue-api-crawler-column-statistics-StopColumnStatisticsTaskRun) operation.

------
#### [ Console ]

**To stop a column statistics task run**

1. On AWS Glue console, choose **Tables** under Data Catalog.

1. Select the table with the column statistics task run is in progress.

1. On the **Table details** page, choose **Column statistics**.

1. Choose **Stop**.

   If you stop the task before the run is complete, column statistics won't be generated for the table.

------
#### [ AWS CLI ]

In the following example, replace values for `DatabaseName` and `TableName` with the actual database and table name.

```
aws glue stop-column-statistics-task-run --input-cli-json file://input.json
{
    "DatabaseName": "{{database_name}}",
    "TableName": "{{table_name}}"
}
```

------