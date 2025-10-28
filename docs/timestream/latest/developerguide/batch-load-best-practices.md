For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Batch load best practices

Batch load works best (high throughput) when adhering to the following conditions and
recommendations:

1. CSV files submitted for ingestion are small, specifically with a file size of
   100 MB–1 GB, to improve parallelism and speed of ingestion.
2. Avoid simultaneously ingesting data into the same table (e.g. using the
   WriteRecords API operation, or a scheduled query) when the batch load is in
   progress. This might lead to throttles, and the batch load task will
   fail.
3. Do not add, modify, or remove files from the S3 bucket used in batch load
   while the batch load task is running.
4. Do not delete or revoke permissions from tables or source, or report S3
   buckets that have scheduled or in-progress batch load tasks.
5. When ingesting data with a high cardinality set of dimension values, follow
   guidance at [Recommendations for
   partitioning multi-measure records](data-modeling.md#data-modeling-multi-measure-partitioning "data-modeling.md#data-modeling-multi-measure-partitioning").
6. Make sure you test the data for correctness by submitting a small file. You
   will be charged for any data submitted to batch load regardless of correctness.
   For more information about pricing, see [Amazon Timestream pricing](https://aws.amazon.com/timestream/pricing/ "https://aws.amazon.com/timestream/pricing/").
7. Do not resume a batch load task unless
   `ActiveMagneticStorePartitions` are below 250. The job may be
   throttled and fail. Submiting multiple jobs at the same time for the same
   database should reduce the number.
   The following are console best practices:

8. Use the [builder](batch-load-using-console.md#batch-load-using-visual-builder "batch-load-using-console.md#batch-load-using-visual-builder") only
   for simpler data modeling that uses only one measure name for multi-measure
   records.
9. For more complex data modeling, use JSON. For example, use JSON when you use
   multiple measure names when using multi-measure records.
   For additional Timestream for LiveAnalytics best practices, see [Best practices](best-practices.md "best-practices.md").
