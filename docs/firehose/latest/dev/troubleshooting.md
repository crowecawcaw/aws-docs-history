# Troubleshoot errors in Amazon Data Firehose

If Firehose encounters errors while delivering or processing data, it retries until the
configured retry duration expires. If the retry duration ends before the data is delivered
successfully, Firehose backs up the data to the configured S3 backup bucket. If the destination
is Amazon S3 and delivery fails or if delivery to the backup S3 bucket fails, Firehose keeps
retrying until the retention period ends.

For information about tracking delivery errors using CloudWatch, see [Monitor Amazon Data Firehose Using
CloudWatch Logs](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md").

Direct PUTFor `DirectPut` Firehose streams, Firehose retains the records for 24 hours. For a
Firehose stream whose data source is a Kinesis data stream, you can change the retention period
as described in [Changing the Data Retention Period](../../../streams/latest/dev/kinesis-extended-retention.md "../../../streams/latest/dev/kinesis-extended-retention.md"). In this case, Firehose retries the following
operations indefinitely: `DescribeStream`, `GetRecords`, and
`GetShardIterator`.

If the Firehose stream uses `DirectPut`, check the `IncomingBytes`
and `IncomingRecords` metrics to see if there's incoming traffic. If you are
using the `PutRecord` or `PutRecordBatch`, make sure you catch
exceptions and retry. We recommend a retry policy with exponential back-off with jitter and
several retries. Also, if you use the `PutRecordBatch` API, make sure your code
checks the value of [FailedPutCount](../APIReference/API_PutRecordBatch.md#Firehose-PutRecordBatch-response-FailedPutCount "../APIReference/API_PutRecordBatch.md#Firehose-PutRecordBatch-response-FailedPutCount") in the response even when the API call succeeds.

Kinesis Data StreamIf the Firehose stream uses a Kinesis data stream as its source, check the
`IncomingBytes` and `IncomingRecords` metrics for the source data
stream. Additionally, ensure that the `DataReadFromKinesisStream.Bytes` and
`DataReadFromKinesisStream.Records` metrics are being emitted for the
Firehose stream.
