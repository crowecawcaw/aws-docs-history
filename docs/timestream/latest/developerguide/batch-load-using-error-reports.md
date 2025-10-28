For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Using batch load error reports

Batch load tasks have one of the following status values:

- `CREATED` (**Created**) – Task is
  created.
- `IN_PROGRESS` (**In progress**) – Task is
  in progress.
- `FAILED` (**Failed**) – Task has completed.
  But one or more errors was detected.
- `SUCCEEDED` (**Completed**) – Task has
  completed with no errors.
- `PROGRESS_STOPPED` (**Progress stopped**) –
  Task has stopped but not completed. You can attempt to resume the task.
- `PENDING_RESUME` (**Pending resume**) – The
  task is pending to resume.
  When there are errors, an error log report is created in the S3 bucket defined for
  that. Errors are categorized as taskErrors or fileErrors in separate arrays. Following
  is an example error report.

```
{
    "taskId": "9367BE28418C5EF902676482220B631C",
    "taskErrors": [],
    "fileErrors": [
        {
            "fileName": "example.csv",
            "errors": [
                {
                    "reason": "The record timestamp is outside the time range of the data ingestion window.",
                    "lineRanges": [
                        [
                            2,
                            3
                        ]
                    ]
                }
            ]
        }
    ]
}
```
