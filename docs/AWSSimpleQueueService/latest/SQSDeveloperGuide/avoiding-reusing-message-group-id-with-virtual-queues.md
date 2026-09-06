

# Avoid reusing the same message group ID with virtual queues in Amazon SQS
<a name="avoiding-reusing-message-group-id-with-virtual-queues"></a>

When using virtual queues with a shared host queue, avoid reusing the same [`MessageGroupId`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) across different virtual queues. If multiple virtual queues share the same host queue and contain messages with the same `MessageGroupId`, those messages can block each other, preventing efficient processing. To ensure smooth message processing, assign unique `MessageGroupId` values for messages in different virtual queues.