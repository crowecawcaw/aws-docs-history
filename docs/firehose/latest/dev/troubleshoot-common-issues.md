# Common issues

The following are troubleshooting tips to help you solve common issues while you work with a Firehose stream.

## Firehose stream unavailable

Firehose stream is not available as a target for CloudWatch Logs,
CloudWatch Events, or AWS IoT action as some AWS
services can only send messages and events to a Firehose stream that is in the same
AWS Region. Verify that your Firehose stream is located in the same Region as your
other services.

## No data at destination

If there
are no data ingestion problems and the metrics emitted for the Firehose stream look
good, but you don't see the data at the destination, check the reader logic.
Make sure your reader is correctly parsing out all data.

## Data freshness metric increasing or

not emitted

Data freshness is a measure of how current your data is within your Firehose stream.
It is the age of the oldest data record in the Firehose stream, measured from the time
that Firehose ingested the data to the present time. Firehose provides metrics that you can use
to monitor data freshness. To identify the data-freshness metric for a given
destination, see [Monitor Amazon Data Firehose with
CloudWatch metrics](monitoring-with-cloudwatch-metrics.md "monitoring-with-cloudwatch-metrics.md").

If you enable backup for all events or all documents, monitor two separate
data-freshness metrics: one for the main destination and one for the backup.

If the data-freshness metric isn't being emitted, this means that there is no active
delivery for the Firehose stream. This happens when data delivery is completely blocked
or when there's no incoming data.

If the data-freshness metric is constantly increasing, this means that data delivery
is falling behind. This can happen for one of the following reasons.

- The destination can't handle the rate of delivery. If Firehose encounters
  transient errors due to high traffic, then the delivery might fall behind. This
  can happen for destinations other than Amazon S3 (it can happen for OpenSearch
  Service, Amazon Redshift, or Splunk). Ensure that your destination has enough capacity to
  handle the incoming traffic.
- The destination is slow. Data delivery might fall behind if Firehose encounters
  high latency. Monitor the destination's latency metric.
- The Lambda function is slow. This might lead to a data delivery rate that is
  less than the data ingestion rate for the Firehose stream. If possible, improve
  the efficiency of the Lambda function. For instance, if the function does network
  IO, use multiple threads or asynchronous IO to increase parallelism. Also,
  consider increasing the memory size of the Lambda function so that the CPU
  allocation can increase accordingly. This might lead to faster Lambda
  invocations. For information about configuring Lambda functions, see [Configuring AWS Lambda Functions](../../../lambda/latest/dg/resource-model.md "../../../lambda/latest/dg/resource-model.md").
- There are failures during data delivery. For information about how to monitor
  errors using Amazon CloudWatch Logs, see [Monitor Amazon Data Firehose Using
  CloudWatch Logs](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md").
- If the data source of the Firehose stream is a Kinesis data stream, throttling
  might be happening. Check the `ThrottledGetRecords`,
  `ThrottledGetShardIterator`, and
  `ThrottledDescribeStream` metrics. If there are multiple
  consumers attached to the Kinesis data stream, consider the following:
  - If the `ThrottledGetRecords` and
    `ThrottledGetShardIterator` metrics are high, we
    recommend you increase the number of shards provisioned for the data
    stream.
  - If the `ThrottledDescribeStream` is high, we recommend you
    add the `kinesis:listshards` permission to the role
    configured in [KinesisStreamSourceConfiguration](../APIReference/API_CreateDeliveryStream.md#Firehose-CreateDeliveryStream-request-KinesisStreamSourceConfiguration "../APIReference/API_CreateDeliveryStream.md#Firehose-CreateDeliveryStream-request-KinesisStreamSourceConfiguration").

- Low buffering hints for the destination. This might increase the number of
  round trips that Firehose needs to make to the destination, which might cause
  delivery to fall behind. Consider increasing the value of the buffering hints.
  For more information, see [BufferingHints](../APIReference/API_BufferingHints.md "../APIReference/API_BufferingHints.md").
- A high retry duration might cause delivery to fall behind when the errors are
  frequent. Consider reducing the retry duration. Also, monitor the errors and try
  to reduce them. For information about how to monitor errors using Amazon CloudWatch Logs, see
  [Monitor Amazon Data Firehose Using
  CloudWatch Logs](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md").
- If the destination is Splunk and `DeliveryToSplunk.DataFreshness`
  is high but `DeliveryToSplunk.Success` looks good, the Splunk cluster
  might be busy. Free the Splunk cluster if possible. Alternatively, contact AWS
  Support and request an increase in the number of channels that Firehose is using to
  communicate with the Splunk cluster.

## Record format conversion to Apache

Parquet fails

This happens if you take DynamoDB data that includes the `Set` type, stream it
through Lambda to a Firehose stream, and use an AWS Glue Data Catalog to convert the record format
to Apache Parquet.

When the AWS Glue crawler indexes the DynamoDB set data types (`StringSet`,
`NumberSet`, and `BinarySet`), it stores them in the data
catalog as `SET<STRING>`, `SET<BIGINT>`, and
`SET<BINARY>`, respectively. However, for Firehose to convert the data
records to the Apache Parquet format, it requires Apache Hive data types. Because the
set types aren't valid Apache Hive data types, conversion fails. To get conversion to
work, update the data catalog with Apache Hive data types. You can do that by changing
`set` to `array` in the data catalog.

###### To change one or more data types from `set` to `array` in

an AWS Glue data catalog

1. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. In the left pane, under the **Data catalog** heading, choose
   **Tables**.
3. In the list of tables, choose the name of the table where you need to modify
   one or more data types. This takes you to the details page for the table.
4. Choose the **Edit schema** button in the top right corner
   of the details page.
5. In the **Data type** column choose the first `set`
   data type.
6. In the **Column type** drop-down list, change the type from
   `set` to `array`.
7. In the **ArraySchema** field, enter
   `array<string>`, `array<int>`, or
   `array<binary>`, depending on the appropriate type of data for
   your scenario.
8. Choose **Update**.
9. Repeat the previous steps to convert other `set` types to
   `array` types.
10. Choose **Save**.

## Missing fields for transformed object for Lambda

When you use Lambda data transformation to change JSON data to Parquet object, some
fields might be missing after the transformation. It happens if your JSON object has
capital letters and the case sensitivity is set to `false`, which can
lead to a mismatch in JSON keys after data transformation causing missing data in
the resulting Parquet object in the s3 bucket.

To fix this, make sure the hose configuration has the `deserializationOption:
 case.insensitive` set to `true` so that the JSON keys matches
after the transformation.
