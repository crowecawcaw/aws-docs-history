For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Batch load

With _batch load_ for Amazon Timestream for LiveAnalytics, you can ingest CSV
files stored in Amazon S3 into Timestream in batches. With this new functionality, you can
have your data in Timestream for LiveAnalytics without having to rely on other tools or write custom code.
You can use batch load for backfilling data with flexible wait times, such as data
that isn't immediately required for querying or analysis.

You can create batch load tasks by using the AWS Management Console, the AWS CLI, and the AWS
SDKs. For more information, see [Using batch load with the console](batch-load-using-console.md "batch-load-using-console.md"), [Using batch load with the AWS CLI](batch-load-using-cli.md "batch-load-using-cli.md"), and [Using batch load with the AWS SDKs](batch-load-using-sdk.md "batch-load-using-sdk.md").

For more information about batch load, see [Using batch load in Timestream for LiveAnalytics](batch-load.md "batch-load.md").
