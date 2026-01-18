# Monitor Amazon Data Firehose with

CloudWatch metrics

###### Important

Be sure to enable alarms on all CloudWatch metrics that belong to your destination in order to identify errors in timely manner.

Amazon Data Firehose integrates with Amazon CloudWatch metrics so that you can collect, view, and analyze
CloudWatch metrics for your Firehose streams. For example, you can monitor the
`IncomingBytes` and `IncomingRecords` metrics to keep track of
data ingested into Amazon Data Firehose from data producers.

Amazon Data Firehose collects and publishes CloudWatch metrics every minute. However, if bursts of incoming data occur only for a few seconds, they may not be fully captured or visible in the one-minute metrics. This is because CloudWatch metrics are aggregated from Amazon Data Firehose over one-minute intervals.

The metrics collected for Firehose streams are free of charge. For information about Kinesis
agent metrics, see [Monitor Kinesis Agent health](agent-health.md "agent-health.md").

###### Topics

- [CloudWatch metrics for dynamic partitioning](#dp-metrics-cw "#dp-metrics-cw")
- [CloudWatch metrics for data delivery](#fh-metrics-cw "#fh-metrics-cw")
- [Data ingestion metrics](#fh-ingestion-metrics "#fh-ingestion-metrics")
- [API-level CloudWatch metrics](#fh-metrics-api-cw "#fh-metrics-api-cw")
- [Data Transformation CloudWatch Metrics](#fh-metrics-data-transformation "#fh-metrics-data-transformation")
- [CloudWatch Logs Decompression Metrics](#decompression-metrics-cw "#decompression-metrics-cw")
- [Format Conversion CloudWatch Metrics](#fh-metrics-format-conversion "#fh-metrics-format-conversion")
- [Server-Side Encryption (SSE) CloudWatch Metrics](#fh-metrics-sse "#fh-metrics-sse")
- [Dimensions for Amazon Data Firehose](#firehose-metric-dimensions "#firehose-metric-dimensions")
- [Amazon Data Firehose Usage Metrics](#fh-metrics-usage "#fh-metrics-usage")

## CloudWatch metrics for dynamic partitioning

If [dynamic partitioning](dynamic-partitioning.md "dynamic-partitioning.md")
is enabled, the AWS/Firehose namespace includes
the following metrics.

| Metric                     | Description                                                                                                                                                                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ActivePartitionsLimit`    | The maximum number of active partitions that a Firehose stream<br>processes before sending data to the error bucket.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                              |
| `PartitionCount`           | The number of partitions that are being processed, in other<br>words, the active partition count. This number varies between 1<br>and the partition count limit of 500 (default).<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count |
| `PartitionCountExceeded`   | This metric indicates if you are exceeding the partition count<br>limit. It emits 1 or 0 based on whether limit is breached or<br>not.                                                                                                                   |
| `JQProcessing.Duration`    | Returns the amount of time it took to execute JQ expression in<br>the JQ Lambda function.<br>Units: Milliseconds                                                                                                                                         |
| `PerPartitionThroughput`   | Indicates the throughput that is being processed per<br>partition. This metric enables you to monitor the per partition<br>throughput.<br>Units: StandardUnit.BytesSecond                                                                                |
| `DeliveryToS3.ObjectCount` | Indicates the number of objects that are being delivered to<br>your S3 bucket.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                    |

## CloudWatch metrics for data delivery

The `AWS/Firehose` namespace includes the following service-level
metrics. If you see small drops in the average for `BackupToS3.Success`,
`DeliveryToS3.Success`, `DeliveryToSplunk.Success`,
`DeliveryToAmazonOpenSearchService.Success`, or
`DeliveryToRedshift.Success`, that doesn't indicate that there's data
loss. Amazon Data Firehose retries delivery errors and doesn't move forward until the records are
successfully delivered either to the configured destination or to the backup S3
bucket.

###### Topics

- [Delivery to OpenSearch Service](#fh-es-metrics "#fh-es-metrics")
- [Delivery to OpenSearch
  Serverless](#fh-serverless-metrics "#fh-serverless-metrics")
- [Delivery to Amazon Redshift](#fh-redshift-metrics "#fh-redshift-metrics")
- [Delivery to Amazon S3](#fh-s3-metrics "#fh-s3-metrics")
- [Delivery to Snowflake](#fh-snowflake-metrics "#fh-snowflake-metrics")
- [Delivery to Splunk](#fh-splunk-metrics "#fh-splunk-metrics")
- [Delivery to HTTP Endpoints](#fh-http-metrics "#fh-http-metrics")

### Delivery to OpenSearch Service

| Metric                                               | Description                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DeliveryToAmazonOpenSearchService.Bytes`            | The number of bytes indexed to OpenSearch Service over the<br>specified time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                |
| `DeliveryToAmazonOpenSearchService.DataFreshness`    | The age (from getting into Amazon Data Firehose to now) of the oldest<br>record in Amazon Data Firehose. Any record older than this age has been<br>delivered to OpenSearch Service.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Seconds                              |
| `DeliveryToAmazonOpenSearchService.Records`          | The number of records indexed to OpenSearch Service over<br>the specified time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                              |
| `DeliveryToAmazonOpenSearchService.Success`          | The sum of the successfully indexed records.                                                                                                                                                                                                                                               |
| `DeliveryToS3.Bytes`                                 | The number of bytes delivered to Amazon S3 over the specified<br>time period. Amazon Data Firehose emits this metric only when you enable<br>backup for all documents.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                              |
| `DeliveryToS3.DataFreshness`                         | The age (from getting into Amazon Data Firehose to now) of the oldest<br>record in Amazon Data Firehose. Any record older than this age has been<br>delivered to the S3 bucket. Amazon Data Firehose emits this metric only<br>when you enable backup for all documents.<br>Units: Seconds |
| `DeliveryToS3.Records`                               | The number of records delivered to Amazon S3 over the specified<br>time period. Amazon Data Firehose emits this metric only when you enable<br>backup for all documents.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                            |
| `DeliveryToS3.Success`                               | The sum of successful Amazon S3 put commands. Amazon Data Firehose always<br>emits this metric regardless of whether backup is enabled<br>for failed documents only or for all documents.                                                                                                  |
| `DeliveryToAmazonOpenSearchService.AuthFailure`      | Authentication/authorization error. Verify the OS/ES<br>cluster policy and role permissions.<br>0 indicates that there is no issue. 1 indicates<br>authentication failure.                                                                                                                 |
| `DeliveryToAmazonOpenSearchService.DeliveryRejected` | Delivery rejected error. Verify the OS/ES cluster policy<br>and role permissions.<br>0 indicates that there is no issue. 1 indicates that<br>there's a delivery failure.                                                                                                                   |

### Delivery to OpenSearch

Serverless

| Metric                                                  | Description                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DeliveryToAmazonOpenSearchServerless.Bytes`            | The number of bytes indexed to OpenSearch Serverless over<br>the specified time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                             |
| `DeliveryToAmazonOpenSearchServerless.DataFreshness`    | The age (from getting into Amazon Data Firehose to now) of the oldest<br>record in Amazon Data Firehose. Any record older than this age has been<br>delivered to OpenSearch Serverless.<br>Units: Seconds                                                                                  |
| `DeliveryToAmazonOpenSearchServerless.Records`          | The number of records indexed to OpenSearch Serverless<br>over the specified time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                           |
| `DeliveryToAmazonOpenSearchServerless.Success`          | The sum of the successfully indexed records.                                                                                                                                                                                                                                               |
| `DeliveryToS3.Bytes`                                    | The number of bytes delivered to Amazon S3 over the specified<br>time period. Amazon Data Firehose emits this metric only when you enable<br>backup for all documents.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                              |
| `DeliveryToS3.DataFreshness`                            | The age (from getting into Amazon Data Firehose to now) of the oldest<br>record in Amazon Data Firehose. Any record older than this age has been<br>delivered to the S3 bucket. Amazon Data Firehose emits this metric only<br>when you enable backup for all documents.<br>Units: Seconds |
| `DeliveryToS3.Records`                                  | The number of records delivered to Amazon S3 over the specified<br>time period. Amazon Data Firehose emits this metric only when you enable<br>backup for all documents.<br>Units: Count                                                                                                   |
| `DeliveryToS3.Success`                                  | The sum of successful Amazon S3 put commands. Amazon Data Firehose always<br>emits this metric regardless of whether backup is enabled<br>for failed documents only or for all documents.                                                                                                  |
| `DeliveryToAmazonOpenSearchServerless.AuthFailure`      | Authentication/authorization error. Verify the OS/ES<br>cluster policy and role permissions.<br>0 indicates that there is no issue. 1 indicates that there<br>is an authentication failure.                                                                                                |
| `DeliveryToAmazonOpenSearchServerless.DeliveryRejected` | Delivery rejected error. Verify the OS/ES cluster policy<br>and role permissions.<br>0 indicates that there is no issue. 1 indicates that there<br>is a delivery failure.                                                                                                                  |

### Delivery to Amazon Redshift

| Metric                             | Description                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DeliveryToRedshift.Bytes`         | The number of bytes copied to Amazon Redshift over the specified time<br>period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                              |
| `DeliveryToRedshift.Records`       | The number of records copied to Amazon Redshift over the specified<br>time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                            |
| `DeliveryToRedshift.Success`       | The sum of successful Amazon Redshift COPY commands.                                                                                                                                                                                                                                                                                                 |
| `DeliveryToS3.Bytes`               | The number of bytes delivered to Amazon S3 over the specified<br>time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                                                                                 |
| `DeliveryToS3.DataFreshness`       | The age (from getting into Amazon Data Firehose to now) of the oldest<br>record in Amazon Data Firehose. Any record older than this age is<br>delivered to the S3 bucket.<br>Units: Seconds                                                                                                                                                          |
| `DeliveryToS3.Records`             | The number of records delivered to Amazon S3 over the specified<br>time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                               |
| `DeliveryToS3.Success`             | The sum of successful Amazon S3 put commands.                                                                                                                                                                                                                                                                                                        |
| `DeliveryToRedshift.DataFreshness` | The age (from getting into Amazon Data Firehose to now) of the oldest<br>record in Amazon Data Firehose. Any record that is older than this age<br>is delivered to the Amazon Redshift cluster.                                                                                                                                                      |
| `BackupToS3.Bytes`                 | The number of bytes delivered to Amazon S3 for backup over the<br>specified time period. Amazon Data Firehose emits this metric when backup<br>to Amazon S3 is enabled.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                       |
| `BackupToS3.DataFreshness`         | The age (from getting into Amazon Data Firehose to now) of the oldest<br>record in Amazon Data Firehose. Any record older than this age has been<br>delivered to the Amazon S3 bucket for backup. Amazon Data Firehose emits<br>this metric when backup to Amazon S3 is enabled.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds |
| `BackupToS3.Records`               | The number of records delivered to Amazon S3 for backup over<br>the specified time period. Amazon Data Firehose emits this metric when<br>backup to Amazon S3 is enabled.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                     |
| `BackupToS3.Success`               | The sum of successful Amazon S3 put commands for backup.<br>Amazon Data Firehose emits this metric when backup to Amazon S3 is<br>enabled.                                                                                                                                                                                                           |

### Delivery to Amazon S3

The metrics in the following table are related to delivery to Amazon S3 when it is
the main destination of the Firehose stream.

| Metric                       | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DeliveryToS3.Bytes`         | The number of bytes delivered to Amazon S3 over the specified<br>time period. When data transformation is enabled, this metric<br>reflects the pre-processed byte size before transformation.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                     |
| `DeliveryToS3.DataFreshness` | The age (from getting into Amazon Data Firehose to now) of the oldest<br>record in Amazon Data Firehose. Any record older than this age has been<br>delivered to the S3 bucket.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds                                                                                                                                                      |
| `DeliveryToS3.Records`       | The number of records delivered to Amazon S3 over the specified<br>time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                                                                                   |
| `DeliveryToS3.Success`       | The sum of successful Amazon S3 put commands.                                                                                                                                                                                                                                                                                                                                                            |
| `BackupToS3.Bytes`           | The number of bytes delivered to Amazon S3 for backup over the<br>specified time period. Amazon Data Firehose emits this metric when backup<br>is enabled (which is only possible when data transformation<br>is also enabled).<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                   |
| `BackupToS3.DataFreshness`   | Age (from getting into Amazon Data Firehose to now) of the oldest record<br>in Amazon Data Firehose. Any record older than this age has been delivered<br>to the Amazon S3 bucket for backup. Amazon Data Firehose emits this metric when<br>backup is enabled (which is only possible when data<br>transformation is also enabled).<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds |
| `BackupToS3.Records`         | The number of records delivered to Amazon S3 for backup over<br>the specified time period. Amazon Data Firehose emits this metric when<br>backup is enabled (which is only possible when data<br>transformation is also enabled).<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                 |
| `BackupToS3.Success`         | The sum of successful Amazon S3 put commands for backup.<br>Amazon Data Firehose emits this metric when backup is enabled (which is<br>only possible when data transformation is also<br>enabled).                                                                                                                                                                                                       |

### Delivery to Snowflake

| Metric                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DeliveryToSnowflake.Bytes`             | The number of bytes delivered to Snowflake over the specified<br>time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                                                                                                                                                                                      |
| `DeliveryToSnowflake.DataFreshness`     | Age (from getting into Firehose to now) of the oldest record<br>in Firehose. Any record older than this age has been delivered<br>to Snowflake. Note that it can take a few seconds to commit<br>data to Snowflake after Firehose insert call is successful. For<br>the time it takes to commit data to Snowflake, refer to the<br>`DeliveryToSnowflake.DataCommitLatency`<br>metric.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds |
| `DeliveryToSnowflake.DataCommitLatency` | The time it takes for the data to be committed to Snowflake<br>after Firehose inserted records successfully.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units:<br>Seconds                                                                                                                                                                                                                                                                       |
| `DeliveryToSnowflake.Records`           | The number of records delivered to Snowflake over the<br>specified time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                                                                                                                                    |
| `DeliveryToSnowflake.Success`           | The sum of successful insert calls made to Snowflake.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `DeliveryToS3.Bytes`                    | The number of bytes delivered to Amazon S3 over the specified time<br>period. This metric is only available when delivery to Snowflake<br>fails and Firehose attempts to backup failed data to<br>S3.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                                                              |
| `DeliveryToS3.Records`                  | The number of records delivered to Amazon S3 over the specified<br>time period. This metric is only available when delivery to<br>Snowflake fails and Firehose attempts to backup failed data to<br>S3.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                            |
| `DeliveryToS3.Success`                  | The sum of successful Amazon S3 put commands. This metric is only<br>available when delivery to Snowflake fails and Firehose attempts to<br>backup failed data to S3.                                                                                                                                                                                                                                                                                     |
| `BackupToS3.DataFreshness`              | Age (from into Firehose to now) of the oldest record in Firehose.<br>Any record older than this age is backed up to the Amazon S3 bucket.<br>This metric is available when the Firehose stream is configured to<br>back up all data.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds                                                                                                                                                  |
| `BackupToS3.Records`                    | The number of records delivered to Amazon S3 for backup over the<br>specified time period. This metric is available when the Firehose<br>stream is configured to back up all data.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units:Count                                                                                                                                                                                                  |
| `BackupToS3.Bytes`                      | The number of bytes delivered to Amazon S3 for backup over the<br>specified time period. This metric is available when the Firehose<br>stream is configured to back up all data.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units:Count                                                                                                                                                                                                    |
| `BackupToS3.Success`                    | The sum of successful Amazon S3 put commands for backup. Firehose<br>emits this metric when the Firehose stream is configured to back up<br>all data.                                                                                                                                                                                                                                                                                                     |

### Delivery to Splunk

| Metric                            | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DeliveryToSplunk.Bytes`          | The number of bytes delivered to Splunk over the specified<br>time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                                                                                                                                              |
| `DeliveryToSplunk.DataAckLatency` | The approximate duration it takes to receive an<br>acknowledgement from Splunk after Amazon Data Firehose sends it data. The<br>increasing or decreasing trend for this metric is more<br>useful than the absolute approximate value. Increasing<br>trends can indicate slower indexing and acknowledgement<br>rates from Splunk indexers.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds |
| `DeliveryToSplunk.DataFreshness`  | Age (from getting into Amazon Data Firehose to now) of the oldest record<br>in Amazon Data Firehose. Any record older than this age has been delivered<br>to Splunk.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds                                                                                                                                                                       |
| `DeliveryToSplunk.Records`        | The number of records delivered to Splunk over the<br>specified time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                                                                                            |
| `DeliveryToSplunk.Success`        | The sum of the successfully indexed records.                                                                                                                                                                                                                                                                                                                                                                   |
| `DeliveryToS3.Success`            | The sum of successful Amazon S3 put commands. This metric is<br>emitted when backup to Amazon S3 is enabled.                                                                                                                                                                                                                                                                                                   |
| `BackupToS3.Bytes`                | The number of bytes delivered to Amazon S3 for backup over the<br>specified time period. Amazon Data Firehose emits this metric when the<br>Firehose stream is configured to back up all<br>documents.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                  |
| `BackupToS3.DataFreshness`        | Age (from getting into Amazon Data Firehose to now) of the oldest record<br>in Amazon Data Firehose. Any record older than this age has been delivered<br>to the Amazon S3 bucket for backup. Amazon Data Firehose emits this metric when<br>the Firehose stream is configured to back up all<br>documents.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds                                |
| `BackupToS3.Records`              | The number of records delivered to Amazon S3 for backup over<br>the specified time period. Amazon Data Firehose emits this metric when the<br>Firehose stream is configured to back up all<br>documents.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                |
| `BackupToS3.Success`              | Sum of successful Amazon S3 put commands for backup. Amazon Data Firehose<br>emits this metric when the Firehose stream is configured to back<br>up all documents.                                                                                                                                                                                                                                             |

### Delivery to HTTP Endpoints

| Metric                                    | Description                                                                                                                                      |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DeliveryToHttpEndpoint.Bytes`            | The number of bytes delivered successfully to the HTTP<br>endpoint.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes       |
| `DeliveryToHttpEndpoint.Records`          | The number of records delivered successfully to the HTTP<br>endpoint.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Counts    |
| `DeliveryToHttpEndpoint.DataFreshness`    | Age of the oldest record in Amazon Data Firehose.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds                            |
| `DeliveryToHttpEndpoint.Success`          | The sum of all successful data delivery requests to the<br>HTTP endpoint.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count |
| `DeliveryToHttpEndpoint.ProcessedBytes`   | The number of attempted processed bytes, including<br>retries.                                                                                   |
| `DeliveryToHttpEndpoint.ProcessedRecords` | The number of attempted records including retries.                                                                                               |

## Data ingestion metrics

###### Topics

- [Data ingestion through Kinesis Data Streams](#fh-ingestion-kds-metrics "#fh-ingestion-kds-metrics")
- [Data ingestion through Direct
  PUT](#fh-ingestion-directput-metrics "#fh-ingestion-directput-metrics")
- [Data ingestion from MSK](#fh-ingestion-msk-metrics "#fh-ingestion-msk-metrics")

### Data ingestion through Kinesis Data Streams

| Metric                              | Description                                                                                                                                                                                                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DataReadFromKinesisStream.Bytes`   | When the data source is a Kinesis data stream, this metric<br>indicates the number of bytes read from that data stream.<br>This number includes rereads due to failovers.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                   |
| `DataReadFromKinesisStream.Records` | When the data source is a Kinesis data stream, this metric<br>indicates the number of records read from that data stream.<br>This number includes rereads due to failovers.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                 |
| `ThrottledDescribeStream`           | The total number of times the `DescribeStream`<br>operation is throttled when the data source is a Kinesis<br>data stream.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                  |
| `ThrottledGetRecords`               | The total number of times the `GetRecords`<br>operation is throttled when the data source is a Kinesis<br>data stream.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                      |
| `ThrottledGetShardIterator`         | The total number of times the<br>`GetShardIterator` operation is throttled<br>when the data source is a Kinesis data stream.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                |
| `KinesisMillisBehindLatest`         | When the data source is a Kinesis data stream, this metric<br>indicates the number of milliseconds that the last read<br>record is behind the newest record in the Kinesis data<br>stream.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Millisecond |

### Data ingestion through Direct

PUT

| Metric                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BackupToS3.Bytes`                                | The number of bytes delivered to Amazon S3 for backup over the<br>specified time period. Amazon Data Firehose emits this metric when data<br>transformation is enabled for Amazon S3 or Amazon Redshift<br>destinations.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                |
| `BackupToS3.DataFreshness`                        | Age (from getting into Amazon Data Firehose to now) of the oldest record<br>in Amazon Data Firehose. Any record older than this age has been delivered<br>to the Amazon S3 bucket for backup. Amazon Data Firehose emits this metric when<br>data transformation is enabled for Amazon S3 or Amazon Redshift<br>destinations.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds              |
| `BackupToS3.Records`                              | The number of records delivered to Amazon S3 for backup over<br>the specified time period. Amazon Data Firehose emits this metric when data<br>transformation is enabled for Amazon S3 or Amazon Redshift<br>destinations.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                              |
| `BackupToS3.Success`                              | Sum of successful Amazon S3 put commands for backup. Amazon Data Firehose<br>emits this metric when data transformation is enabled for<br>Amazon S3 or Amazon Redshift destinations.                                                                                                                                                                                                                           |
| `BytesPerSecondLimit`                             | The current maximum number of bytes per second that a<br>Firehose stream can ingest before throttling. To request an<br>increase to this limit, go to the [AWS<br>Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") and choose **Create<br>case**, then choose **Service limit<br>increase**.                                                         |
| `DeliveryToAmazonOpenSearchService.Bytes`         | The number of bytes indexed to OpenSearch Service over the<br>specified time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                                                                                                                                    |
| `DeliveryToAmazonOpenSearchService.DataFreshness` | The age (from getting into Amazon Data Firehose to now) of the oldest<br>record in Amazon Data Firehose. Any record older than this age has been<br>delivered to OpenSearch Service.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds                                                                                                                                                       |
| `DeliveryToAmazonOpenSearchService.Records`       | The number of records indexed to OpenSearch Service over<br>the specified time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                                                                                  |
| `DeliveryToAmazonOpenSearchService.Success`       | The sum of the successfully indexed records.                                                                                                                                                                                                                                                                                                                                                                   |
| `DeliveryToRedshift.Bytes`                        | The number of bytes copied to Amazon Redshift over the specified time<br>period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                                                                                                                                        |
| `DeliveryToRedshift.Records`                      | The number of records copied to Amazon Redshift over the specified<br>time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                                                                                      |
| `DeliveryToRedshift.Success`                      | The sum of successful Amazon Redshift COPY commands.                                                                                                                                                                                                                                                                                                                                                           |
| `DeliveryToS3.Bytes`                              | The number of bytes delivered to Amazon S3 over the specified<br>time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                                                                                                                                           |
| `DeliveryToS3.DataFreshness`                      | The age (from getting into Amazon Data Firehose to now) of the oldest<br>record in Amazon Data Firehose. Any record older than this age has been<br>delivered to the S3 bucket.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds                                                                                                                                                            |
| `DeliveryToS3.Records`                            | The number of records delivered to Amazon S3 over the specified<br>time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                                                                                         |
| `DeliveryToS3.Success`                            | The sum of successful Amazon S3 put commands.                                                                                                                                                                                                                                                                                                                                                                  |
| `DeliveryToSplunk.Bytes`                          | The number of bytes delivered to Splunk over the specified<br>time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                                                                                                                                              |
| `DeliveryToSplunk.DataAckLatency`                 | The approximate duration it takes to receive an<br>acknowledgement from Splunk after Amazon Data Firehose sends it data. The<br>increasing or decreasing trend for this metric is more<br>useful than the absolute approximate value. Increasing<br>trends can indicate slower indexing and acknowledgement<br>rates from Splunk indexers.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds |
| `DeliveryToSplunk.DataFreshness`                  | Age (from getting into Amazon Data Firehose to now) of the oldest record<br>in Amazon Data Firehose. Any record older than this age has been delivered<br>to Splunk.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Seconds                                                                                                                                                                       |
| `DeliveryToSplunk.Records`                        | The number of records delivered to Splunk over the<br>specified time period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                                                                                            |
| `DeliveryToSplunk.Success`                        | The sum of the successfully indexed records.                                                                                                                                                                                                                                                                                                                                                                   |
| `IncomingBytes`                                   | The number of bytes ingested successfully into the Firehose stream over the specified time period. Data ingestion could be throttled when it exceeds one of the Firehose stream limits.<br>Throttled data will not be counted for `IncomingBytes`.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                      |
| `IncomingPutRequests`                             | The number of successful PutRecord and PutRecordBatch<br>requests over a specified period of time.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                                                                      |
| `IncomingRecords`                                 | The number of records ingested successfully into the Firehose stream over the specified time period. Data ingestion could be throttled when it exceeds one of the Firehose stream limits.<br>Throttled data will not be counted for `IncomingRecords`.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                  |
| `RecordsPerSecondLimit`                           | The current maximum number of records per second that a<br>Firehose stream can ingest before throttling.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                                                                |
| `ThrottledRecords`                                | The number of records that were throttled because data<br>ingestion exceeded one of the Firehose stream limits.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                                                                                                         |

### Data ingestion from MSK

| Metric                             | Description                                                                                                                                                                                                                                                      |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DataReadFromSource.Records`       | The number of records read from the source Kafka Topic.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                   |
| `DataReadFromSource.Bytes`         | The number of bytes read from the source Kafka Topic.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                     |
| `SourceThrottled.Delay`            | The amount of time that the source Kafka cluster is delayed in returning the records from the source Kafka Topic.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Milliseconds                                                                       |
| `BytesPerSecondLimit`              | Current limit of throughput at which Firehose is going to read from each partition of the source Kafka Topic.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes/sec                                                                         |
| `KafkaOffsetLag`                   | The difference between the largest offset of the record that Firehose has read from the source Kafka Topic<br>and the largest offset of the record available from the source Kafka Topic.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count |
| `FailedValidation.Records`         | The number of records that failed record validation.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                                      |
| `FailedValidation.Bytes`           | The number of bytes that failed record validation.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                                                                                                        |
| `DataReadFromSource.Backpressured` | Indicates that a Firehose stream is delayed in reading records from the source partition either because<br>BytesPerSecondLimit per partition has exceeded or that the normal flow of delivery is slow or has stopped<br>Units: Boolean                           |

## API-level CloudWatch metrics

The `AWS/Firehose` namespace includes the following API-level
metrics.

| Metric                            | Description                                                                                                                                                                                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DescribeDeliveryStream.Latency`  | The time taken per `DescribeDeliveryStream`<br>operation, measured over the specified time period.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Milliseconds                                                                 |
| `DescribeDeliveryStream.Requests` | The total number of `DescribeDeliveryStream`<br>requests.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                            |
| `ListDeliveryStreams.Latency`     | The time taken per `ListDeliveryStream` operation,<br>measured over the specified time period.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Milliseconds                                                                     |
| `ListDeliveryStreams.Requests`    | The total number of `ListFirehose` requests.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                         |
| `PutRecord.Bytes`                 | The number of bytes put to the Firehose stream using<br>`PutRecord` over the specified time<br>period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                               |
| `PutRecord.Latency`               | The time taken per `PutRecord` operation, measured<br>over the specified time period.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Milliseconds                                                                              |
| `PutRecord.Requests`              | The total number of `PutRecord` requests, which is<br>equal to total number of records from `PutRecord`<br>operations.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                               |
| `PutRecordBatch.Bytes`            | The number of bytes put to the Firehose stream using<br>`PutRecordBatch` over the specified time<br>period.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes                                                          |
| `PutRecordBatch.Latency`          | The time taken per `PutRecordBatch` operation,<br>measured over the specified time period.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Milliseconds                                                                         |
| `PutRecordBatch.Records`          | The total number of records from `PutRecordBatch`<br>operations.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                     |
| `PutRecordBatch.Requests`         | The total number of `PutRecordBatch`<br>requests.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                                    |
| `PutRequestsPerSecondLimit`       | The maximum number of put requests per second that a<br>Firehose stream can handle before throttling. This number<br>includes PutRecord and PutRecordBatch requests.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count |
| `ThrottledDescribeStream`         | The total number of times the `DescribeStream`<br>operation is throttled when the data source is a Kinesis data<br>stream.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                           |
| `ThrottledGetRecords`             | The total number of times the `GetRecords`<br>operation is throttled when the data source is a Kinesis data<br>stream.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                               |
| `ThrottledGetShardIterator`       | The total number of times the `GetShardIterator`<br>operation is throttled when the data source is a Kinesis data<br>stream.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                         |
| `UpdateDeliveryStream.Latency`    | The time taken per `UpdateDeliveryStream`<br>operation, measured over the specified time period.<br>Statistics: Minimum, Maximum, Average, Samples<br>Units: Milliseconds                                                                   |
| `UpdateDeliveryStream.Requests`   | The total number of `UpdateDeliveryStream`<br>requests.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count                                                                                                              |

## Data Transformation CloudWatch Metrics

If data transformation with Lambda is enabled, the `AWS/Firehose` namespace
includes the following metrics.

| Metric                       | Description                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `ExecuteProcessing.Duration` | The time it takes for each Lambda function invocation performed by Firehose.<br>Units: Milliseconds             |
| `ExecuteProcessing.Success`  | The sum of the successful Lambda function invocations over the sum of the<br>total Lambda function invocations. |
| `SucceedProcessing.Records`  | The number of successfully processed records over the specified time period.<br>Units: Count                    |
| `SucceedProcessing.Bytes`    | The number of successfully processed bytes over the specified time period.<br>Units: Bytes                      |

## CloudWatch Logs Decompression Metrics

If decompression is enabled for CloudWatch Logs delivery, the `AWS/Firehose` namespace includes the following metrics.

| Metric                              | Description                                                                                                      |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `OutputDecompressedBytes.Success`   | Successful decompressed data in bytes<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes     |
| `OutputDecompressedBytes.Failed`    | Failed decompressed data in bytes<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Bytes         |
| `OutputDecompressedRecords.Success` | Number of successful decompressed records<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count |
| `OutputDecompressedRecords.Failed`  | Number of failed decompressed records<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count     |

## Format Conversion CloudWatch Metrics

If format conversion is enabled, the `AWS/Firehose` namespace
includes the following metrics.

| Metric                      | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| `SucceedConversion.Records` | The number of successfully converted records.<br>Units: Count        |
| `SucceedConversion.Bytes`   | The size of the successfully converted records.<br>Units: Bytes      |
| `FailedConversion.Records`  | The number of records that could not be converted.<br>Units: Count   |
| `FailedConversion.Bytes`    | The size of the records that could not be converted.<br>Units: Bytes |

## Server-Side Encryption (SSE) CloudWatch Metrics

The `AWS/Firehose` namespace includes the following metrics that are
related to SSE.

| Metric               | Description                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `KMSKeyAccessDenied` | The number of times the service encounters a<br>`KMSAccessDeniedException` for the<br>Firehose stream.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count |
| `KMSKeyDisabled`     | The number of times the service encounters a<br>`KMSDisabledException` for the Firehose stream.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count        |
| `KMSKeyInvalidState` | The number of times the service encounters a<br>`KMSInvalidStateException` for the<br>Firehose stream.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count |
| `KMSKeyNotFound`     | The number of times the service encounters a<br>`KMSNotFoundException` for the Firehose stream.<br>Statistics: Minimum, Maximum, Average, Sum, Samples<br>Units: Count        |

## Dimensions for Amazon Data Firehose

To filter metrics by Firehose stream, use the `DeliveryStreamName`
dimension.

## Amazon Data Firehose Usage Metrics

You can use CloudWatch usage metrics to provide visibility into your account's usage of
resources. Use these metrics to visualize your current service usage on CloudWatch graphs
and dashboards.

Service quota usage metrics are in the AWS/Usage namespace and are collected
every three minutes.

Currently, the only metric name in this namespace that CloudWatch publishes is
`ResourceCount`. This metric is published with the dimensions
`Service`, `Class`, `Type`, and
`Resource`.

| Metric          | Description                                                                                                                                                                                                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ResourceCount` | The number of the specified resources running in your account.<br>The resources are defined by the dimensions associated with the<br>metric.<br>The most useful statistic for this metric is MAXIMUM, which<br>represents the maximum number of resources used during the<br>3-minute period. |

The following dimensions are used to refine the usage metrics that are published
by Amazon Data Firehose.

| Dimension  | Description                                                                                                                                      |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Service`  | The name of the AWS service containing the resource. For<br>Amazon Data Firehose usage metrics, the value for this dimension is<br>`Firehose`.   |
| `Class`    | The class of resource being tracked. Amazon Data Firehose API usage metrics<br>use this dimension with a value of `None`.                        |
| `Type`     | The type of resource being tracked. Currently, when the<br>Service dimension is `Firehose`, the only valid value<br>for Type is `Resource`.      |
| `Resource` | The name of the AWS resource. Currently, when the Service<br>dimension is `Firehose`, the only valid value for<br>Resource is `DeliveryStreams`. |
