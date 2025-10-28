# Amazon Kinesis stream as a source for EventBridge Pipes

You can use EventBridge Pipes to receive records in a Kinesis data stream. You can then optionally
filter or enhance these records before sending them to one of the available destinations for
processing. There are settings specific to Kinesis that you can choose when setting up the pipe.
EventBridge Pipes maintains the order of records from the data stream when sending that data to the
destination.

A Kinesis data stream is a set of [shards](../../../kinesis/latest/dev/key-concepts.md#shard "../../../kinesis/latest/dev/key-concepts.md#shard"). Each shard contains a sequence of data records.
A **consumer** is an application that processes the data from a Kinesis data stream. You can map an EventBridge Pipe to a shared-throughput consumer
(standard iterator), or to a dedicated-throughput consumer with [enhanced fan-out](../../../kinesis/latest/dev/enhanced-consumers.md "../../../kinesis/latest/dev/enhanced-consumers.md").

For standard iterators, EventBridge uses the HTTP protocol to poll each shard in your Kinesis stream
for records. The pipe shares the read throughput with other consumers of the shard.

To minimize latency and maximize read throughput, you can create a data stream consumer with
enhanced fan-out. Stream consumers get a dedicated connection to each shard that doesn't impact
other applications reading from the stream. The dedicated throughput can help if you have many
applications reading the same data, or if you're reprocessing a stream with large records. Kinesis
pushes records to EventBridge over HTTP/2. For information about Kinesis data streams, see [Reading Data from Amazon Kinesis Data
Streams](../../../kinesis/latest/dev/building-consumers.md "../../../kinesis/latest/dev/building-consumers.md").

**Example event**

The following sample event shows the information that is received by the pipe. You can use
this event to create and filter your event patterns, or to define input transformation. Not all
of the fields can be filtered. For more information about which fields you can filter, see [Event filtering in Amazon EventBridge Pipes](eb-pipes-event-filtering.md "eb-pipes-event-filtering.md").

```
[
  {
    "kinesisSchemaVersion": "1.0",
    "partitionKey": "1",
    "sequenceNumber": "49590338271490256608559692538361571095921575989136588898",
    "data": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
    "approximateArrivalTimestamp": 1545084650.987
    "eventSource": "aws:kinesis",
    "eventVersion": "1.0",
    "eventID": "shardId-000000000006:49590338271490256608559692538361571095921575989136588898",
    "eventName": "aws:kinesis:record",
    "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
    "awsRegion": "us-east-2",
    "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream"
  },
  {
    "kinesisSchemaVersion": "1.0",
    "partitionKey": "1",
    "sequenceNumber": "49590338271490256608559692540925702759324208523137515618",
    "data": "VGhpcyBpcyBvbmx5IGEgdGVzdC4=",
    "approximateArrivalTimestamp": 1545084711.166
    "eventSource": "aws:kinesis",
    "eventVersion": "1.0",
    "eventID": "shardId-000000000006:49590338271490256608559692540925702759324208523137515618",
    "eventName": "aws:kinesis:record",
    "invokeIdentityArn": "arn:aws:iam::123456789012:role/lambda-role",
    "awsRegion": "us-east-2",
    "eventSourceARN": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream"
  }
]
```

## Polling and batching streams

EventBridge polls shards in your Kinesis stream for records at a base rate of four times per second.
When records are available, EventBridge processes the event and waits for the result. If processing
succeeds, EventBridge resumes polling until it receives more records.

By default, EventBridge invokes your pipe as soon as records are available. If the batch that EventBridge reads from the source has only one record in it,
only one event is processed. To avoid processing a small number of records, you can tell the pipe to buffer records for up to five minutes by configuring a batching window.
Before processing the events, EventBridge continues to read records from the source until it has gathered a full batch, the batching window expires, or the batch reaches
the payload limit of 6 MB.

You can also increase concurrency by processing multiple batches from each shard in parallel.
EventBridge can process up to 10 batches in each shard simultaneously.
If you increase the number of concurrent batches per shard, EventBridge still ensures in-order processing at the partition key level.

Configure the `ParallelizationFactor` setting to process one shard of a Kinesis or DynamoDB data stream with more than one Pipe execution simultaneously.
You can specify the number of concurrent batches that EventBridge polls from a shard via a parallelization factor from 1 (default) to 10.
For example, when you set `ParallelizationFactor` to 2, you can have 200 concurrent EventBridge Pipe executions at maximum to process 100 Kinesis data shards.
This helps scale up the processing throughput when the data volume is volatile and the `IteratorAge` is high.
Note that parallelization factor will not work if you are using Kinesis aggregation.

## Polling and stream starting position

Be aware that stream source polling during pipe creation and updates is eventually consistent.

- During pipe creation, it may take several minutes to start polling events from the stream.
- During pipe updates to the source polling configuration, it may take
  several minutes to stop and restart polling events from the stream.

This means that if you specify `LATEST` as the starting position for the stream,
the pipe could miss events sent during pipe creation or updates.
To ensure no events are missed, specify the stream starting position as `TRIM_HORIZON` or `AT_TIMESTAMP`.

## Reporting batch item failures

When EventBridge consumes and processes streaming data from an source, by default it
checkpoints to the highest sequence number of a batch, but only when the batch is a complete
success. To avoid reprocessing
successfully processed messages in a failed batch, you can configure your enrichment or target
to return an object indicating which messages succeeded and which failed. This is called a
partial batch response.

For more information, see [Partial batch failure](eb-pipes-batching-concurrency.md#pipes-partial-batch-failure "eb-pipes-batching-concurrency.md#pipes-partial-batch-failure").

### Success and failure conditions

If you return any of the following, EventBridge treats a batch as a complete success:

- An empty `batchItemFailure` list
- A null `batchItemFailure` list
- An empty `EventResponse`
- A null `EventResponse`

If you return any of the following, EventBridge treats a batch as a complete failure:

- An empty string `itemIdentifier`
- A null `itemIdentifier`
- An `itemIdentifier` with a bad key name

EventBridge retries failures based on your retry strategy.
