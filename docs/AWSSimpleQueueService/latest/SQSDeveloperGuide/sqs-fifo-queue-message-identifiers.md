# FIFO queue and message

identifiers in Amazon SQS

This section describes the identifiers of FIFO queues. These identifiers can help you
find and manipulate specific queues and messages.

## Identifiers for FIFO queues in

Amazon SQS

For more information about the following identifiers, see the _[Amazon Simple Queue Service API Reference](../APIReference.md "../APIReference.md")_.

### Queue name and URL

When you create a new queue, you must specify a queue name unique for your
AWS account and region. Amazon SQS assigns each queue you create an identifier
called a _queue URL_ that includes the queue name and other
Amazon SQS components. Whenever you want to perform an action on a queue, you provide
its queue URL.

The name of a FIFO queue must end with the `.fifo` suffix. The suffix counts towards the 80-character queue name quota.
To determine whether a queue is [FIFO](sqs-fifo-queues.md "sqs-fifo-queues.md"), you can check whether the queue name ends with the suffix.

The following is the queue URL for a FIFO queue named `MyQueue`
owned by a user with the AWS account number
`123456789012`.

```
https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue.fifo
```

You can retrieve the URL of a queue programmatically by listing your queues
and parsing the string that follows the account number. For more information,
see `ListQueues`.

### Message ID

Each message receives a system-assigned _message ID_ that
Amazon SQS returns to you in the `SendMessage` response. This identifier is useful for
identifying messages. The maximum length of a message ID is 100
characters.

### Receipt handle

Every time you receive a message from a queue, you receive a _receipt
handle_ for that message. This handle is associated with the
action of receiving the message, not with the message itself. To delete the
message or to change the message visibility, you must provide the receipt handle
(not the message ID). Thus, you must always receive a message before you can
delete it (you can't put a message into the queue and then recall it). The
maximum length of a receipt handle is 1,024 characters.

###### Important

If you receive a message more than once, each time you receive it, you get
a different receipt handle. You must provide the most recently received
receipt handle when you request to delete the message (otherwise, the
message might not be deleted).

The following is an example of a receipt handle (broken across three
lines).

```
MbZj6wDWli+JvwwJaBV+3dcjk2YW2vA3+STFFljTM8tJJg6HRG6PYSasuWXPJB+Cw
Lj1FjgXUv1uSj1gUPAWV66FU/WeR4mq2OKpEGYWbnLmpRCJVAyeMjeU5ZBdtcQ+QE
auMZc8ZRv37sIW2iJKq3M9MFx1YvV11A2x/KSbkJ0=
```

## Additional identifiers for

Amazon SQS FIFO queues

For more information about the following identifiers, see [Exactly-once processing in
Amazon SQS](FIFO-queues-exactly-once-processing.md "FIFO-queues-exactly-once-processing.md") and the _[Amazon Simple Queue Service API Reference](../APIReference.md "../APIReference.md")_.

### Message deduplication

ID

A token used in Amazon SQS FIFO queues to uniquely identify messages and prevent duplication. If multiple messages with the same deduplication ID are sent within a 5 minute deduplication interval, they are treated as duplicates, and only one copy is delivered. If you don't specify a deduplication ID and content-based deduplication is enabled, Amazon SQS generates a deduplication ID by hashing the message body. This mechanism ensures exactly-once delivery by eliminating duplicate messages within the specified time frame.

### Message group ID

The `MessageGroupId` is an attribute used only in Amazon SQS FIFO (First-In-First-Out) queues to organize messages into distinct groups. Messages within the same message group are always processed one at a time, in strict order, ensuring that no two messages from the same group are processed simultaneously. Standard queues do not use `MessageGroupId` and do not provide ordering guarantees. If strict ordering is required, use a FIFO queue instead.

### Sequence number

The large, non-consecutive number that Amazon SQS assigns to each message.
