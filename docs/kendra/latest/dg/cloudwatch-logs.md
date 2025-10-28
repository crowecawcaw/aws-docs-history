# Monitoring Amazon Kendra with Amazon CloudWatch Logs

Amazon Kendra uses Amazon CloudWatch Logs to give you insight into the operation of your data sources.
Amazon Kendra logs process details for the documents as they are indexed. It logs errors from
your data source that occur while your documents are being indexed. You use CloudWatch Logs to
monitor, store and access the log files.

CloudWatch Logs stores log events in a log stream that is part of a log group. Amazon Kendra uses
these features as follows:

- Log groups—Amazon Kendra stores all of your log streams in a single log
  group for each index. Amazon Kendra creates the log group when the index is created.
  The log group identifier always begins with "aws/kendra/".
- Log stream—Amazon Kendra creates a new data source log stream in the log
  group for each index synchronization job that you run. It also creates a new
  document log stream when a stream reaches approximately 500 entries.
- Log entries—Amazon Kendra creates a log entry in the log stream as it
  indexes documents. Each entry provides information about processing the document
  or any errors that are encountered.
  For more information about using CloudWatch Logs, see [What Is Amazon Cloud
  Watch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") in the _Amazon Cloud Watch Logs User Guide_.

Amazon Kendra creates two types of log streams:

- [Data source log streams](#data-source-log-stream "#data-source-log-stream")
- [Document log streams](#document-log-stream "#document-log-stream")

## Data source log streams

Data source log streams publish entries about your index synchronization jobs.
Each synchronization job creates a new log stream that it uses to publish entries.
The log stream name is:

```
`data source id`/`YYYY`-`MM`-`DD`-`HH`/`data source sync job ID`
```

A new log stream is created for each synchronization job run.

There are three types of log messages published to a data source log
stream:

- A log message for a document that failed to be sent for indexing. The
  following is an example of this message for a document in an S3 data
  source:

```
{
    "DocumentId": "`document ID`",
    "S3Path": "s3://`bucket`/`prefix`/`object`",
    "Message": "Failed to ingest document via BatchPutDocument.",
    "ErrorCode": "InvalidRequest",
    "ErrorMessage": "No document metadata configuration found for document attribute key  city."
}
```

- A log message for a document that failed to be sent for deletion. The
  following is an example of this message:

```
{
    "DocumentId": "`document ID`",
    "Message": "Failed to delete document via BatchDeleteDocument.",
    "ErrorCode": "InvalidRequest",
    "ErrorMessage": "Document can't be deleted because it doesn't exist."
}
```

- A log message when an invalid metadata file for a document in an Amazon S3
  bucket is found. The following is an example of this message.

```
{
    "Message": "Found invalid metadata file `bucket`/`prefix`/`filename`.`extension`.metadata.json."
}
```

- For SharePoint and database connectors, Amazon Kendra only writes messages to
  the log stream if a document can't be indexed. The following is an example
  of the error message that Amazon Kendra logs.

```
{
    "DocumentID": "`document ID`",
    "IndexID": "`index ID`",
    "SourceURI": "",
    "CrawlStatus": "FAILED",
    "ErrorCode": "403",
    "ErrorMessage": "Access Denied",
    "DataSourceErrorCode": "403"
}
```

## Document log streams

Amazon Kendra logs information about processing documents while they are being indexed.
It logs a set of messages for documents stored in an Amazon S3 data source. It logs
errors only for documents stored in a Microsoft SharePoint or a database data
source.

If the documents were added to the index using the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") operation, the log stream is named as follows:

```
`YYYY`-`MM`-`DD`-`HH`/`UUID`
```

If the documents were added to the index using a datasource, the log stream is
named as follows:

```
`dataSourceId`/`YYYY`-`MM`-`DD`-`HH`/`UUID`
```

Each log stream contains up to 500 messages.

If indexing a document fails, this message is output to the log stream:

```
{
    "DocumentId": "`document ID`",
    "IndexName": "`index name`",
    "IndexId": "`index ID`"
    "SourceURI": "`source URI`"
    "IndexingStatus": "`DocumentFailedToIndex`",
    "ErrorCode": "400 | 500",
    "ErrorMessage": "`message`"
}
```

## View Amazon Kendra metrics for your synchronization

jobs

You can view a document-level sync run history report in CloudWatch for your data source
sync job by selecting **View Report**. A sync run history report
will have details about the progress and status of each document in the sync job. It
shows if a document succeeded, failed, or was skipped during the crawl, sync, and
index stages. You'll also find any error messages related to failed or skipped
documents. If the report doesn't show results for an in-progress sync job, the logs
may not be available yet. Check back later as data is emitted to the report as
events occur during the sync process.

To access your sync run history report, take the following steps:

1. Open the Amazon Kendra console at [https://console.aws.amazon.com/kendra/](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation menu, under **Data management**,
   choose **Data sources**, and then choose your data
   source.
3. From your data source summary page, scroll down and select the
   **Sync history** tab.
4. From **Sync run history**, select
   **Actions**.
5. From **Actions**, select **View
   report**. You will be redirected to the CloudWatch console where you will
   be able to access your report.

###### Note

A sync run history records if a document was successfully indexed during
ingestion, including attached ACLs and metadata, for all Amazon Kendra supported
connectors.

**If you're using the Amazon S3 connector:**

In addition to the vieing the document-level sync run history report in CloudWatch, you
can generate sync history reports for each document in your Amazon S3 data source and
copy it to an Amazon S3 bucket. During this process, your data is encrypted
using AWS KMS keys and can only be viewed by you. Reported document
status can be one of the following: **Failed**,
**Completed**, or **Succeeded with errors**.
Before you can generate sync status reports for Amazon S3, you must do the
following:

- Add the following Amazon Kendra service principal to your Amazon S3 access policy
- Create an Amazon S3 bucket with access permissions to Amazon Kendra

If you use the console, to generate a sync history report for Amazon S3, choose to
activate the **Generate reports** option from **Sync
history reports – _optional_** section on the
**Data source details** page. Then, enter the Amazon S3
bucket location and choose from the configuration options available. Reports will be
generated from the next sync after you have activated generate report.

If you delete the Amazon S3 bucket, you will lose your log data and will
have to set up a new bucket to store new sync reports.

###### Note

A sync history report provides information only about whether an Amazon S3
connector successfully crawled and ingested data.
