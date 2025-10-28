# Configure source settings for Amazon Kinesis Data Streams

Configure the source settings for Amazon Kinesis Data Streams to send information to a Firehose stream as
following.

###### Important

If you use the Kinesis Producer Library (KPL) to write data to a Kinesis data stream, you can use
aggregation to combine the records that you write to that Kinesis data stream. If you then
use that data stream as a source for your Firehose stream, Amazon Data Firehose de-aggregates the
records before it delivers them to the destination. If you configure your Firehose stream to
transform the data, Amazon Data Firehose de-aggregates the records before it delivers them to
AWS Lambda. For more information, see
[Developing Amazon Kinesis Data Streams Producers Using the Kinesis Producer
Library](../../../streams/latest/dev/developing-producers-with-kpl.md "../../../streams/latest/dev/developing-producers-with-kpl.md") and
[Aggregation](../../../streams/latest/dev/kinesis-kpl-concepts.md#kinesis-kpl-concepts-aggretation "../../../streams/latest/dev/kinesis-kpl-concepts.md#kinesis-kpl-concepts-aggretation").

Under the **Source settings**, choose an existing
stream in the **Kinesis data stream** list, or enter a data stream ARN in
the format `arn:aws:kinesis:[Region]:[AccountId]:stream/[StreamName]`.

If you do not have an existing data stream then choose **Create** to
create a new one from Amazon Kinesis console. You may need an IAM role that has the necessary
permission on the Kinesis stream. For more information, see [Grant Firehose access to an Amazon S3 destination](controlling-access.md#using-iam-s3 "controlling-access.md#using-iam-s3").
After you create a new stream, choose the refresh icon to update the **Kinesis
stream** list. If you have a large number of streams, filter the list using
**Filter by name**.

###### Note

When you configure a Kinesis data stream as the source of a
Firehose stream, the Amazon Data Firehose `PutRecord` and
`PutRecordBatch` operations are disabled. To add data
to your Firehose stream in this case, use the Kinesis Data Streams
`PutRecord` and `PutRecords`
operations.

Amazon Data Firehose starts reading data from the `LATEST` position of
your Kinesis stream. For more information about Kinesis Data Streams positions, see [GetShardIterator](../../../kinesis/latest/APIReference/API_GetShardIterator.md "../../../kinesis/latest/APIReference/API_GetShardIterator.md").

Amazon Data Firehose calls the Kinesis Data Streams [GetRecords](../../../kinesis/latest/APIReference/API_GetRecords.md "../../../kinesis/latest/APIReference/API_GetRecords.md") operation
once per second for each shard. However, when full backup is enabled,
Firehose calls the Kinesis Data Streams `GetRecords` operation twice per second
for each shard, one for primary delivery destination and another for
full backup.

More than one Firehose stream can read from the same Kinesis stream. Other
Kinesis applications (consumers) can also read from the same stream. Each
call from any Firehose stream or other consumer application counts against
the overall throttling limit for the shard. To avoid getting throttled,
plan your applications carefully. For more information about Kinesis Data Streams
limits, see [Amazon Kinesis Streams Limits](../../../streams/latest/dev/service-sizes-and-limits.md "../../../streams/latest/dev/service-sizes-and-limits.md").

Proceed to the next step to configure record transformation and format conversion.
