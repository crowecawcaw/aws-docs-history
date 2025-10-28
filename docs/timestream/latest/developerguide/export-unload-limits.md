For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Limits for UNLOAD from Timestream for LiveAnalytics

Following are limits related to the `UNLOAD` command.

- Concurrency for queries using the `UNLOAD` statement is 1 query per
  second (QPS). Exceeding the query rate might result in throttling.
- Queries containing `UNLOAD` statement can export at most 100
  partitions per query. We recommend to check the distinct count of the selected
  column before using it to partition the exported data.
- Queries containing `UNLOAD` statement time out after 60
  minutes.
- The maximum size of the files that the `UNLOAD` statement creates
  in Amazon S3 is 78 GB.
  For other limits for Timestream for LiveAnalytics, see [Quotas](ts-limits.md "ts-limits.md")
