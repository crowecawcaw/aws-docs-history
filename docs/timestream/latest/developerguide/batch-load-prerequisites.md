For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Batch load prerequisites

This is a list of prerequisites for using batch load. For best practices, see
[Batch load best practices](batch-load-best-practices.md "batch-load-best-practices.md").

- Batch load source data is stored in Amazon S3 in CSV format with
  headers.
- For each Amazon S3 source bucket, you must have the following permissions
  in an attached policy:

```
"s3:GetObject",
"s3:GetBucketAcl"
"s3:ListBucket"
```

Similarly, for each Amazon S3 output bucket where reports are written, you must
have the following permissions in an attached policy:

```
"s3:PutObject",
"s3:GetBucketAcl"
```

For example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:GetBucketAcl",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-source-bucket1\u201d",
 "arn:aws:s3:::amzn-s3-demo-source-bucket2\u201d"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:PutObject",
 "s3:GetBucketAcl"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-destination-bucket\u201d"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

- Timestream for LiveAnalytics parses the CSV by mapping information that's provided in the data model to
  CSV headers. The data must have a column that represents the timestamp, at least
  one dimension column, and at least one measure column.
- The S3 buckets used with batch load must be in the same region and from the
  same account as the Timestream for LiveAnalytics table that is used in batch load.
- The `timestamp` column must be a long data type that represents the
  time since the Unix epoch. For example, the timestamp
  `2021-03-25T08:45:21Z` would be represented as
  `1616661921`. Timestream supports seconds, milliseconds,
  microseconds, and nanoseconds for the timestamp precision. When using the query
  language, you can convert between formats with functions such as
  `to_unixtime`. For more information, see [Date / time functions](date-time-functions.md "date-time-functions.md").
- Timestream supports the string data type for dimension values. It supports
  long, double, string, and boolean data types for measure columns.
  For batch load limits and quotas, see [Batch load](ts-limits.md#limits.batch-load "ts-limits.md#limits.batch-load").
