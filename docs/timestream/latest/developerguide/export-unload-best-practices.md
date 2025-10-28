For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Best practices for UNLOAD from

Timestream for LiveAnalytics

Following are best practices related to the UNLOAD command.

- The amount of data that can be exported to S3 bucket using the
  `UNLOAD` command is not bounded. However, the query times out in
  60 minutes and we recommend exporting no more than 60GB of data in a single
  query. If you need to export more than 60GB of data, split the job across
  multiple queries.
- While you can send thousands of requests to S3 to upload the data, it is
  recommended to parallelize the write operations to multiple S3 prefixes. Refer
  to documentation [here](../../../AmazonS3/latest/userguide/optimizing-performance.md "../../../AmazonS3/latest/userguide/optimizing-performance.md"). S3
  API call rate could be throttled when multiple readers/writers access the same
  folder.
- Given the limit on S3 key length for defining a prefix, we recommend having
  bucket and folder names within 10-15 characters, especially when using
  `partitioned_by` clause.
- When you receive a 4XX or 5XX for queries containing the `UNLOAD`
  statement, it is possible that partial results are written into the S3 bucket.
  Timestream for LiveAnalytics does not delete any data from your bucket. Before executing another
  `UNLOAD` query with same S3 destination, we recommend to manually
  delete the files created by the failed query. You can identify the files written
  by a failed query with the corresponding `QueryExecutionId`. For
  failed queries, Timestream for LiveAnalytics does not export a manifest file to the S3 bucket.
- Timestream for LiveAnalytics uses multi-part upload to export query results to S3. When you receive a
  4XX or 5XX from Timestream for LiveAnalytics for queries containing an UNLOAD statement, Timestream for LiveAnalytics does a
  best-effort abortion of multi-part upload but it is possible that some
  incomplete parts are left behind. Hence, we recommended to set up an auto
  cleanup of incomplete multi-part uploads in your S3 bucket by following the
  guidelines [here](https://aws.amazon.com/blogs/aws-cloud-financial-management/discovering-and-deleting-incomplete-multipart-uploads-to-lower-amazon-s3-costs/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/discovering-and-deleting-incomplete-multipart-uploads-to-lower-amazon-s3-costs/").

## Recommendations for accessing the data in CSV format using CSV parser

- CSV parsers don’t allow you to have same character in delimiter, escape,
  and quote character.
- Some CSV parsers cannot interpret complex data types such as Arrays, we
  recommend interpreting those through JSON deserializer.

## Recommendations for accessing the data in Parquet format

1. If your use case requires UTF-8 character support in schema aka column
   name, we recommend using [Parquet-mr library](https://github.com/apache/parquet-mr "https://github.com/apache/parquet-mr").
2. The timestamp in your results is represented as a 12 byte integer
   (INT96)
3. Timeseries will be represented as
   `array<row<time, value>>`, other nested
   structures will use corresponding datatypes supported in Parquet
   format

## Using partition_by

clause

- The column used in the `partitioned_by` field should be the
  last column in the select query. If more than one column is used in the
  `partitioned_by` field, the columns should be the last
  columns in the select query and in the same order as used in the
  `partition_by` field.
- The column values used to partition the data (`partitioned_by`
  field) can contain only ASCII characters. While Timestream for LiveAnalytics allows UTF-8 characters
  in the values, S3 supports only ASCII characters as object keys.
