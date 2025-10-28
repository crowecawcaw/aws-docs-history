# Amazon DynamoDB stream as a source for EventBridge Pipes

You can use EventBridge Pipes to receive records in a DynamoDB stream. You can then optionally filter
or enhance these records before sending them to a target for
processing. There are settings specific to Amazon DynamoDB Streams that you can choose when setting up the
pipe. EventBridge Pipes maintains the order of records from the data stream when sending that data to
the destination.

###### Important

Disabling a DynamoDB stream that is the source of a pipe results in that pipe becoming
unusable, even if you then re-enable the stream. This happens because:

- You cannot stop, start, or update a pipe whose source is disabled.
- You cannot update a pipe with a new source after creation. When you re-enable a DynamoDB stream,
  that stream is assigned a new Amazon Resource Name (ARN), and is no longer associated with your pipe.
  If you do re-enable the DynamoDB stream, you will then need to create a new pipe using the stream's new ARN.

**Example event**

The following sample event shows the information that's received by the pipe. You can use
this event to create and filter your event patterns , or to define input transformation. Not all
of the fields can be filtered. For more information about which fields you can filter, see [Event filtering in Amazon EventBridge Pipes](eb-pipes-event-filtering.md "eb-pipes-event-filtering.md").

```
[
  {
    "eventID": "1",
    "eventVersion": "1.0",
    "dynamodb": {
      "Keys": {
        "Id": {
          "N": "101"
        }
      },
      "NewImage": {
        "Message": {
          "S": "New item!"
        },
        "Id": {
          "N": "101"
        }
      },
      "StreamViewType": "NEW_AND_OLD_IMAGES",
      "SequenceNumber": "111",
      "SizeBytes": 26
    },
    "awsRegion": "us-west-2",
    "eventName": "INSERT",
    "eventSourceARN": "arn:aws:dynamodb:us-east-1:111122223333:table/EventSourceTable",
    "eventSource": "aws:dynamodb"
  },
  {
    "eventID": "2",
    "eventVersion": "1.0",
    "dynamodb": {
      "OldImage": {
        "Message": {
          "S": "New item!"
        },
        "Id": {
          "N": "101"
        }
      },
      "SequenceNumber": "222",
      "Keys": {
        "Id": {
          "N": "101"
        }
      },
      "SizeBytes": 59,
      "NewImage": {
        "Message": {
          "S": "This item has changed"
        },
        "Id": {
          "N": "101"
        }
      },
      "StreamViewType": "NEW_AND_OLD_IMAGES"
    },
    "awsRegion": "us-west-2",
    "eventName": "MODIFY",
    "eventSourceARN": "arn:aws:dynamodb:us-east-1:111122223333:table/EventSourceTable",
    "eventSource": "aws:dynamodb"
  }
]
```

## Polling and batching streams

EventBridge polls shards in your DynamoDB stream for records at a base rate of four times per second.
When records are available, EventBridge processes the event and waits for the result. If processing
succeeds, EventBridge resumes polling until it receives more records.

By default, EventBridge invokes your pipe as soon as records are available. If the batch that EventBridge reads from the source has only one record in it,
only one event is processed. To avoid processing a small number of records, you can tell the pipe to buffer records for up to five minutes by configuring a batching window.
Before processing the events, EventBridge continues to read records from the source until it has gathered a full batch, the batching window expires, or the batch reaches
the payload limit of 6 MB.

###### Important

The pipe will deliver the stream records from DynamoDB to Amazon SQS at least once.
To ensure that no records get dropped, we suggest setting a retry policy with a maximum age shorter than the retention period of the DynamoDB stream.
Generally, DynamoDB streams retain events for 24 hours.

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
To ensure no events are missed, specify the stream starting position as `TRIM_HORIZON`.

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
