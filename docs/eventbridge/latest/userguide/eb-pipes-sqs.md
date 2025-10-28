# Amazon Simple Queue Service as a source in EventBridge Pipes

You can use EventBridge Pipes to receive records from an Amazon SQS queue. You can then optionally
filter or enhance these records before sending them to an available destination for processing.

You can use a pipe to process messages in an Amazon Simple Queue Service (Amazon SQS) queue. EventBridge Pipes support [standard queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.md") and
[first-in, first-out (FIFO) queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.md"). With Amazon SQS, you can offload tasks from one component of your application by sending
them to a queue and processing them asynchronously.

EventBridge polls the queue and invokes your pipe synchronously with an event that contains queue messages. EventBridge reads messages in batches and invokes your
pipe once for each batch. When your pipe successfully processes a batch, EventBridge deletes its messages from the queue.

By default, EventBridge polls up to 10 messages in your queue simultaneously and sends that batch
to your pipe. To avoid invoking the pipe with a small number of records, you can tell the event
source to buffer records for up to five minutes by configuring a batch window.
Before invoking the pipe, EventBridge continues to
poll messages from the Amazon SQS standard queue until one of these things occurs:

- The batch window expires.
- The invocation payload size quota is reached.
- The configured maximum batch size is reached.

###### Note

If you're using a batch window and your Amazon SQS queue contains low traffic, EventBridge might wait for
up to 20 seconds before invoking your pipe. This is true even if you set a batch window for
fewer than 20 seconds. For FIFO queues, records contain additional attributes that are related
to deduplication and sequencing.

When EventBridge reads a batch, the messages stay in the queue but are hidden for the length of the queue's [visibility timeout](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.md").
If your pipe successfully processes the batch, EventBridge deletes the messages from the queue. By default, if your pipe encounters an error while processing a batch,
all messages in that batch become visible in the queue again. For this reason, your pipe code must be able to process the same message multiple times without unintended
side effects. You can modify this reprocessing behavior by including batch item failures in your pipe response. The following example shows an event for a batch of two messages.

**Example events**

The following sample event shows the information that is received by the pipe. You can use
this event to create and filter your event patterns, or to define input transformation. Not all
of the fields can be filtered. For more information about which fields you can filter, see [Event filtering in Amazon EventBridge Pipes](eb-pipes-event-filtering.md "eb-pipes-event-filtering.md").

**Standard queue**

```
[
  {
    "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
    "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
    "body": "Test message.",
    "attributes": {
      "ApproximateReceiveCount": "1",
      "SentTimestamp": "1545082649183",
      "SenderId": "AIDAIENQZJOLO23YVJ4VO",
      "ApproximateFirstReceiveTimestamp": "1545082649185"
    },
    "messageAttributes": {},
    "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
    "eventSource": "aws:sqs",
    "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
    "awsRegion": "us-east-2"
  },
  {
    "messageId": "2e1424d4-f796-459a-8184-9c92662be6da",
    "receiptHandle": "AQEBzWwaftRI0KuVm4tP+/7q1rGgNqicHq...",
    "body": "Test message.",
    "attributes": {
      "ApproximateReceiveCount": "1",
      "SentTimestamp": "1545082650636",
      "SenderId": "AIDAIENQZJOLO23YVJ4VO",
      "ApproximateFirstReceiveTimestamp": "1545082650649"
    },
    "messageAttributes": {},
    "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
    "eventSource": "aws:sqs",
    "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
    "awsRegion": "us-east-2"
  }
]
```

**FIFO queue**

```
[
  {
    "messageId": "11d6ee51-4cc7-4302-9e22-7cd8afdaadf5",
    "receiptHandle": "AQEBBX8nesZEXmkhsmZeyIE8iQAMig7qw...",
    "body": "Test message.",
    "attributes": {
      "ApproximateReceiveCount": "1",
      "SentTimestamp": "1573251510774",
      "SequenceNumber": "18849496460467696128",
      "MessageGroupId": "1",
      "SenderId": "AIDAIO23YVJENQZJOL4VO",
      "MessageDeduplicationId": "1",
      "ApproximateFirstReceiveTimestamp": "1573251510774"
    },
    "messageAttributes": {},
    "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
    "eventSource": "aws:sqs",
    "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:fifo.fifo",
    "awsRegion": "us-east-2"
  }
]
```

## Scaling and processing

For standard queues, EventBridge uses [long polling](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.md") to poll a queue until it becomes active.
When messages are available, EventBridge reads up to five batches and sends them to your pipe. If messages are still available, EventBridge increases the number
of processes that are reading batches by up to 300 more instances per minute. The maximum number of batches that a pipe can process simultaneously is 1,000.

For FIFO queues, EventBridge sends messages to your pipe in the order that it receives them. When
you send a message to a FIFO queue, you specify a [message group ID](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.md"). Amazon SQS
facilitates delivering messages in the same group to EventBridge, in order. EventBridge sorts the received
messages into groups and sends only one batch at a time for a group. If your pipe returns an
error, the pipe attempts all retries on the affected messages before EventBridge receives additional
messages from the same group.

## Configuring a queue to use with EventBridge Pipes

[Create an Amazon SQS queue](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.md") to serve as an source for your pipe. Then configure the queue to allow
time for your pipe to process each batch of events—and for EventBridge to retry in response to throttling errors as it scales up.

To allow your pipe time to process each batch of records, set the source queue's
visibility timeout to at least six times the combined runtime of the pipe enrichment and
target components. The extra time allows for EventBridge to retry if your pipe is throttled while
processing a previous batch.

If your pipe fails to process a message multiple times, Amazon SQS can send it to a [dead-letter queue](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.md"). When your pipe
returns an error, EventBridge keeps it in the queue. After the visibility timeout occurs, EventBridge
receives the message again. To send messages to a second queue after a number of receives,
configure a dead-letter queue on your source queue.

###### Note

Make sure that you configure the dead-letter queue on the source queue, not on the pipe. The dead-letter queue that you configure on a pipe is used for the pipe's
asynchronous invocation queue, not for source queues.

If your pipe returns an error, or can't be invoked because it's at maximum concurrency,
processing might succeed with additional attempts. To give messages more chances to be
processed before sending them to the dead-letter queue, set the `maxReceiveCount`
on the source queue's redrive policy to at least **5**.

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
