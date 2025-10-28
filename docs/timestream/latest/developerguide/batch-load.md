For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Using batch load in Timestream for LiveAnalytics

With _batch load_ for Amazon Timestream for LiveAnalytics, you can ingest CSV files
stored in Amazon S3 into Timestream in batches. With this new functionality, you can have your data
in Timestream for LiveAnalytics without having to rely on other tools or write custom code. You can use batch load
for backfilling data with flexible wait times, such as data that isn't immediately required
for querying or analysis.

You can create batch load tasks by using the AWS Management Console, the AWS CLI, and the AWS SDKs. For
more information, see [Using batch load with the console](batch-load-using-console.md "batch-load-using-console.md"), [Using batch load with the AWS CLI](batch-load-using-cli.md "batch-load-using-cli.md"), and [Using batch load with the AWS SDKs](batch-load-using-sdk.md "batch-load-using-sdk.md").

In addition to batch load, you can write multiple records at the same time with the
WriteRecords API operation. For guidance about which to use, see [Choosing between the WriteRecords API
operation and batch load](writes.md "writes.md").

###### Topics

- [Batch load concepts in Timestream](batch-load-concepts.md "batch-load-concepts.md")
- [Batch load prerequisites](batch-load-prerequisites.md "batch-load-prerequisites.md")
- [Batch load best practices](batch-load-best-practices.md "batch-load-best-practices.md")
- [Preparing a batch load data
  file](batch-load-preparing-data-file.md "batch-load-preparing-data-file.md")
- [Data model mappings for batch
  load](batch-load-data-model-mappings.md "batch-load-data-model-mappings.md")
- [Using batch load with the console](batch-load-using-console.md "batch-load-using-console.md")
- [Using batch load with the AWS CLI](batch-load-using-cli.md "batch-load-using-cli.md")
- [Using batch load with the AWS SDKs](batch-load-using-sdk.md "batch-load-using-sdk.md")
- [Using batch load error reports](batch-load-using-error-reports.md "batch-load-using-error-reports.md")
