# Using Lambda with Amazon SQS

###### Note

If you want to send data to a target other than a Lambda function or enrich the data before sending it, see [Amazon EventBridge Pipes](../../../eventbridge/latest/userguide/eb-pipes.md "../../../eventbridge/latest/userguide/eb-pipes.md").

You can use a Lambda function to process messages in an Amazon Simple Queue Service (Amazon SQS) queue. Lambda
supports both [standard queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.md") and [first-in, first-out (FIFO) queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.md") for [event source mappings](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md"). The Lambda function and the Amazon SQS queue must be in the same AWS Region, although they can be in [different AWS accounts](with-sqs-cross-account-example.md "with-sqs-cross-account-example.md").

When processing Amazon SQS messages, you need to implement partial batch response logic to prevent successfully processed messages from being retried when some messages in a batch fail. The [Batch Processor utility](https://docs.powertools.aws.dev/lambda/python/latest/utilities/batch/ "https://docs.powertools.aws.dev/lambda/python/latest/utilities/batch/") from Powertools for AWS Lambda simplifies this implementation by automatically handling partial batch response logic, reducing development time and improving reliability.

###### Topics

- [Understanding polling and batching behavior for Amazon SQS event source mappings](#sqs-polling-behavior "#sqs-polling-behavior")
- [Example standard queue message event](#example-standard-queue-message-event "#example-standard-queue-message-event")
- [Example FIFO queue message event](#sample-fifo-queues-message-event "#sample-fifo-queues-message-event")
- [Creating and configuring an Amazon SQS event source mapping](services-sqs-configure.md "services-sqs-configure.md")
- [Configuring scaling behavior for SQS event source mappings](services-sqs-scaling.md "services-sqs-scaling.md")
- [Handling errors for an SQS event source in Lambda](services-sqs-errorhandling.md "services-sqs-errorhandling.md")
- [Lambda parameters for Amazon SQS event source mappings](services-sqs-parameters.md "services-sqs-parameters.md")
- [Using event filtering with an Amazon SQS event source](with-sqs-filtering.md "with-sqs-filtering.md")
- [Tutorial: Using Lambda with Amazon SQS](with-sqs-example.md "with-sqs-example.md")
- [Tutorial: Using a cross-account Amazon SQS queue as an event
  source](with-sqs-cross-account-example.md "with-sqs-cross-account-example.md")

## Understanding polling and batching behavior for Amazon SQS event source mappings

With Amazon SQS event source mappings, Lambda polls the queue and invokes your function [synchronously](invocation-sync.md "invocation-sync.md") with an event. Each event can contain a batch of multiple messages from the queue. Lambda receives
these events one batch at a time, and invokes your function once for each batch. When your function successfully
processes a batch, Lambda deletes its messages from the queue.

When Lambda receives a batch, the messages stay in the queue but are hidden for the length of the queue's
[visibility timeout](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.md"). If your function successfully processes all messages in the batch, Lambda deletes
the messages from the queue. By default, if your function encounters an error while processing a batch, all
messages in that batch become visible in the queue again after the visibility timeout expires. For this reason,
your function code must be able to process the same message multiple times without unintended side effects.

###### Warning

Lambda event source mappings process each event at least once, and duplicate processing of records can occur. To avoid potential issues
related to duplicate events, we strongly recommend that you make your function code idempotent. To learn more, see [How do I make my Lambda function idempotent](https://repost.aws/knowledge-center/lambda-function-idempotent "https://repost.aws/knowledge-center/lambda-function-idempotent")
in the AWS Knowledge Center.

To prevent Lambda from processing a message multiple times, you can either configure your event source
mapping to include [batch item failures](services-sqs-errorhandling.md#services-sqs-batchfailurereporting "services-sqs-errorhandling.md#services-sqs-batchfailurereporting") in your
function response, or you can use the [DeleteMessage](../../../AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.md") API to
remove messages from the queue as your Lambda function successfully processes them.

For more information about configuration parameters that Lambda supports for SQS event source
mappings, see [Creating an SQS event source mapping](services-sqs-configure.md#events-sqs-eventsource "services-sqs-configure.md#events-sqs-eventsource").

## Example standard queue message event

###### Example Amazon SQS message event (standard queue)

```
{
    "Records": [
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
            "messageAttributes": {
                "myAttribute": {
                    "stringValue": "myValue",
                    "stringListValues": [],
                    "binaryListValues": [],
                    "dataType": "String"
                }
            },
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
}
```

By default, Lambda polls up to 10 messages in your queue at once and sends that batch to your function. To avoid
invoking the function with a small number of records, you can configure the event source to buffer records for up
to 5 minutes by configuring a batch window. Before invoking the function, Lambda continues to poll messages from the
standard queue until the batch window expires, the [invocation payload size
quota](gettingstarted-limits.md "gettingstarted-limits.md") is reached, or the configured maximum batch size is reached.

If you're using a batch window and your SQS queue contains very low traffic, Lambda might wait for up to 20
seconds before invoking your function. This is true even if you set a batch window lower than 20 seconds.

###### Note

In Java, you might experience null pointer errors when deserializing JSON. This could be due to how case of "Records" and "eventSourceARN" is converted by the JSON object mapper.

## Example FIFO queue message event

For FIFO queues, records contain additional attributes that are related to deduplication and sequencing.

###### Example Amazon SQS message event (FIFO queue)

```
{
    "Records": [
        {
            "messageId": "11d6ee51-4cc7-4302-9e22-7cd8afdaadf5",
            "receiptHandle": "AQEBBX8nesZEXmkhsmZeyIE8iQAMig7qw...",
            "body": "Test message.",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1573251510774",
                `"SequenceNumber": "18849496460467696128",
 "MessageGroupId": "1",`
                "SenderId": "AIDAIO23YVJENQZJOL4VO",
                `"MessageDeduplicationId": "1",`
                "ApproximateFirstReceiveTimestamp": "1573251510774"
            },
            "messageAttributes": {},
            "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:fifo.fifo",
            "awsRegion": "us-east-2"
        }
    ]
}
```
