# Avoiding inconsistent message

processing in Amazon SQS

Because Amazon SQS is a distributed system, it is possible for a consumer to not receive a
message even when Amazon SQS marks the message as delivered while returning successfully from
a [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md") API method call. In this case, Amazon SQS
records the message as delivered at least once, although the consumer has never received
it. Because no additional attempts to deliver messages are made under these conditions,
we don't recommend setting the number of maximum receives to 1 for a [dead-letter queue](sqs-dead-letter-queues.md "sqs-dead-letter-queues.md").
