# Exporting log data to Amazon S3

This chapter provides you with information, so you can export log data from your log
groups to an Amazon S3 bucket for custom processing and analysis, or to load onto other systems.
You can export to a bucket in the same account or a different account.

You can do the following:

- Export log data to S3 buckets that are encrypted by SSE-KMS in AWS Key Management Service (AWS KMS)
- Export log data to S3 buckets that have S3 Object Lock enabled with a retention
  period
  We recommend that you don't regularly export to Amazon S3 as a way to continuously archive your
  logs. For that use case, we instead recommend that you use subscriptions. For more
  information about subscriptions, see [Real-time processing of log data with subscriptions](Subscriptions.md "Subscriptions.md").

To begin the export process, you must create an S3 bucket to store the exported log data.
You can store the exported files in your S3 bucket and define Amazon S3 lifecycle rules to
archive or delete exported files automatically.

You can export to S3 buckets that are encrypted with AES-256 or with SSE-KMS. Exporting to
buckets encrypted with DSSE-KMS is not supported.

You can export logs from multiple log groups or multiple time ranges to the same S3
bucket. To separate log data for each export task, you can specify a prefix that will be
used as the Amazon S3 key prefix for all exported objects.

###### Note

Time-based sorting on chunks of log data inside an exported file is not guaranteed.
You can sort the exported log field data by using Linux utilities. For example, the
following utility command sorts the events in all `.gz` files in a single
folder.

```
find . -exec zcat {} + | sed -r 's/^[0-9]+/\x0&/' | sort -z
```

The following utility command sorts .gz files from multiple subfolders.

```
find ./*/ -type f -exec zcat {} + | sed -r 's/^[0-9]+/\x0&/' | sort -z
```

Additionally, you can use another `stdout` command to pipe the sorted
output to another file to save it.

Log data can take up to 12 hours to become available for export. Export tasks time out
after 24 hours. If your export tasks are timing out, reduce the time range when you create
the export task.

For near real-time analysis of log data, see [Analyzing log data with CloudWatch Logs Insights](AnalyzingLogData.md "AnalyzingLogData.md") or [Real-time processing of log data with subscriptions](Subscriptions.md "Subscriptions.md") instead.

###### Contents

- [Concepts](#S3concepts "#S3concepts")
- [Export log data to Amazon S3 using the console](S3ExportTasksConsole.md "S3ExportTasksConsole.md")
- [Export log data to Amazon S3 using the AWS CLI](S3ExportTasks.md "S3ExportTasks.md")
- [Describe export tasks (CLI)](DescribeExportTasks.md "DescribeExportTasks.md")
- [Cancel an export task (CLI)](CancelExportTask.md "CancelExportTask.md")

## Concepts

Before you begin, become familiar with the following export concepts:

**log group name**

The name of the log group associated with an export task. The log data in
this log group will be exported to the specified S3 bucket.

**from (timestamp)**

A required timestamp expressed as the number of milliseconds since Jan 1,
1970 00:00:00 UTC. All log events in the log group that were ingested on or
after this time will be exported.

**to (timestamp)**

A required timestamp expressed as the number of milliseconds since Jan 1,
1970 00:00:00 UTC. All log events in the log group that were ingested before
this time will be exported.

**destination bucket**

The name of the S3 bucket associated with an export task. This bucket is
used to export the log data from the specified log group.

**destination prefix**

An optional attribute that is used as the Amazon S3 key prefix for all exported
objects. This helps create a folder-like organization in your bucket.
