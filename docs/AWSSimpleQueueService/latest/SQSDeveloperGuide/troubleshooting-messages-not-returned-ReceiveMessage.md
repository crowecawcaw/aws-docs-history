# Troubleshoot messages not

returned for an Amazon SQS ReceiveMessage API call

The following topics cover the most common causes why an Amazon SQS message may not be returned
to consumers, and how to troubleshoot them. For more information, see [Why can't I receive messages from
my Amazon SQS queue?](https://repost.aws/knowledge-center/sqs-queue-message "https://repost.aws/knowledge-center/sqs-queue-message") in the _AWS Knowledge Center
Guide_.

## Empty queue

To determine if a queue is empty, use long polling to call the [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md") API. You can also use the
`ApproximateNumberOfMessagesVisible`,
`ApproximateNumberOfMessagesNotVisible`, and
`ApproximateNumberOfMessagesDelayed` CloudWatch metrics. If all the metric values are
set to 0 for several minutes, the queue is considered empty.

## In flight limit reached

If you use [long polling](sqs-short-and-long-polling.md#sqs-long-polling "sqs-short-and-long-polling.md#sqs-long-polling") and if the queue’s in
flight limit (120000 by default) is breached, Amazon SQS won't return
error messages that [exceed quota limits](sqs-quotas.md "sqs-quotas.md").

## Message delay

If the Amazon SQS queue is configured as a [delay queue](sqs-delay-queues.md "sqs-delay-queues.md"),
or the messages were sent with [message timers](sqs-message-timers.md "sqs-message-timers.md"), then
the messages aren't visible until the delay time ends. To verify if a queue is configured as a
delay queue, use the [`GetQueueAttributes`](../APIReference/API_GetQueueAttributes.md "../APIReference/API_GetQueueAttributes.md") API `DelaySeconds` attribute, or from
the queue console under **Delivery delay**. Check the [ApproximateNumberOfMessagesDelayed](sqs-available-cloudwatch-metrics.md "sqs-available-cloudwatch-metrics.md") CloudWatch metric to understand if any
messages are delayed.

## Message is in flight

If a different consumer has polled the message, the message will be in flight or invisible
for the [visibility timeout](sqs-visibility-timeout.md "sqs-visibility-timeout.md") period. The
additional polls might return an empty receive. Check the [ApproximateNumberOfMessagesVisible](sqs-available-cloudwatch-metrics.md "sqs-available-cloudwatch-metrics.md") CloudWatch
metric to understand the number of messages that are available to be received. In the case of
FIFO queues, if a message with the message group ID is in flight, then no more messages will
be returned unless you delete the message, or it becomes visible. This is because [message ordering](sqs-fifo-queues.md "sqs-fifo-queues.md") is maintained at the message group level
in a FIFO queue.

## Polling method

If you are using [short polling](sqs-short-and-long-polling.md#sqs-short-polling "sqs-short-and-long-polling.md#sqs-short-polling"), ([WaitTimeSeconds](../APIReference/API_ReceiveMessage.md#API_ReceiveMessage_RequestSyntax "../APIReference/API_ReceiveMessage.md#API_ReceiveMessage_RequestSyntax") is 0) Amazon SQS samples a subset of its servers, and returns messages
from only those servers. Therefore, you might not get the messages even if they are available
for to be received. Subsequent poll requests will return the messages.

If you are using [long polling](sqs-short-and-long-polling.md#sqs-long-polling "sqs-short-and-long-polling.md#sqs-long-polling"), Amazon SQS polls all the
servers and sends a response after collecting at least one available message, and up to the
maximum number that's specified. If the value for ReceiveMessage [WaitTimeSeconds](../APIReference/API_ReceiveMessage.md#API_ReceiveMessage_RequestSyntax "../APIReference/API_ReceiveMessage.md#API_ReceiveMessage_RequestSyntax") is too low, you might not receive all the available messages.
