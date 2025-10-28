# Troubleshoot Amazon SQS dead-letter queue and DLQ

redrive issues

The following topics cover the most common causes of Amazon SQS DLQ and DLQ redrive issues, and
how to troubleshoot them. For more information, see [How do I troubleshoot
Amazon SQS DLQ redrive issues?](https://repost.aws/knowledge-center/sqs-dead-letter-queue-redrive "https://repost.aws/knowledge-center/sqs-dead-letter-queue-redrive") in the _AWS Knowledge
Center Guide_.

## DLQ issues

Learn about common DLQ issues and how to solve them.

### Viewing messages using the console might cause messages to

be moved to a dead-letter queue

Amazon SQS counts viewing a message in the console against the corresponding queue's redrive
policy. Therefore, if you view a message in the console the number of times specified in the
corresponding queue's redrive policy, the message is moved to the corresponding queue's
dead-letter queue.

To adjust this behavior, you can do one of the following:

- Increase the **Maximum Receives** setting for the corresponding
  queue's redrive policy.
- Avoid viewing the corresponding queue's messages in the console.

### The `NumberOfMessagesSent` and

`NumberOfMessagesReceived` for a dead-letter queue don't match

If you send a message to a dead-letter queue manually, it is captured by the [NumberOfMessagesSent](sqs-available-cloudwatch-metrics.md "sqs-available-cloudwatch-metrics.md")
metric. However, if a message is sent to a dead-letter queue as a result of a failed
processing attempt, it isn't captured by this metric. Therefore, it's possible for the
values of `NumberOfMessagesSent` and [NumberOfMessagesReceived](sqs-available-cloudwatch-metrics.md "sqs-available-cloudwatch-metrics.md") to
be different.

### Creating and configuring a dead-letter queue

redrive

Dead-letter queue redrive requires you to set appropriate [permissions](sqs-configure-dead-letter-queue-redrive.md#sqs-configure-dead-letter-queue-redrive-permissions "sqs-configure-dead-letter-queue-redrive.md#sqs-configure-dead-letter-queue-redrive-permissions") for Amazon SQS to
receive messages from the dead-letter queue, and send messages to the destination queue. If
you don't have the correct permissions, the dead-letter queue redrive task can fail. You can
view the status of your message redrive task to remediate the issues, and try again.

### Standard and FIFO queue

message failure handling

[Standard queues](standard-queues.md "standard-queues.md")
keep processing messages until the expiration of the [retention period](sqs-dead-letter-queues.md#understanding-message-retention-periods "sqs-dead-letter-queues.md#understanding-message-retention-periods"). This continuous
processing minimizes chances of the queue being blocked by unconsumed messages. Having a
large number of messages that the consumer repeatedly fails to delete can increase costs,
and place extra load on the hardware. To keep costs down, move failed messages to the
dead-letter queue.

Standard queues also allow a high number of in-flight messages. If the majority of your
messages can't be consumed, and aren't sent to a dead-letter queue, your rate of processing
messages can slow down. To maintain the efficiency of your queue, make sure that your
application correctly handles message processing.

[FIFO queues](sqs-fifo-queues.md "sqs-fifo-queues.md")
provide exactly-once processing by consuming messages in sequence from a message group.
Therefore, although the consumer can continue to retrieve ordered messages from another
message group, the first message group remains unavailable until the message blocking the
queue is processed successfully or moved to a dead-letter queue.

Additionally, FIFO queues allow a lower number of in-flight messages. To keep your FIFO
queue from getting blocked by a message, make sure that your application correctly handles
message processing.

For more information, see [Amazon SQS message quotas](quotas-messages.md "quotas-messages.md") and [Amazon SQS best practices](sqs-best-practices.md "sqs-best-practices.md").

## DLQ-redrive issues

Learn about common DLQ-redrive issues and how to solve them.

### AccessDenied permission issue

The `AccessDenied` error occurs when the DLQ redrive fails because the
AWS Identity and Access Management (IAM) entity doesn't have the required permissions.

**Example error message:**

```
Failed to create redrive task. Error code: AccessDenied - Queue Permissions to Redrive.
```

The following API permissions are required to make DLQ redrive requests:

**To start a message redrive:**

- Dead-letter queue permissions:
  - `sqs:StartMessageMoveTask`
  - `sqs:ReceiveMessage`
  - `sqs:DeleteMessage`
  - `sqs:GetQueueAttributes`
  - `kms:Decrypt` – When either the dead-letter queue or the
    original source queue are encrypted.

- Destination queue permissions:
  - `sqs:SendMessage`
  - `kms:GenerateDataKey` – When the destination queue is
    encrypted.
  - `kms:Decrypt` – When the destination queue is
    encrypted.

**To cancel an in-progress message redrive:**

- Dead-letter queue permissions:
  - `sqs:CancelMessageMoveTask`
  - `sqs:ReceiveMessage`
  - `sqs:DeleteMessage`
  - `sqs:GetQueueAttributes`
  - `kms:Decrypt` – When either the dead-letter queue or the
    original source queue are encrypted.

**To show a message move status:**

- Dead-letter queue permissions:
  - `sqs:ListMessageMoveTasks`
  - `sqs:GetQueueAttributes`

### `NonExistentQueue` error

The `NonExistentQueue` error occurs when the Amazon SQS source queue doesn't
exist, or was deleted. Check and redrive to an Amazon SQS queue that is present.

**Example error message:**

```
Failed: AWS.SimpleQueueService.NonExistentQueue
```

### CouldNotDetermineMessageSource

error

The `CouldNotDetermineMessageSource` error occurs when you attempt to start a
DLQ redrive with the following scenarios:

- An Amazon SQS message sent directly to the DLQ with [`SendMessage`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") API.
- A message from the Amazon Simple Notification Service (Amazon SNS) topic or AWS Lambda function with the DLQ
  configured.

To resolve this error, choose **Redrive to a custom destination** when
you start the redrive. Then, enter the Amazon SQS queue ARN to move all messages from the DLQ to
the destination queue.

**Example error message:**

```
Failed: CouldNotDetermineMessageSource
```
