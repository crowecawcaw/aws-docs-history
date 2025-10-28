# Avoid

reusing the same message group ID with virtual queues in Amazon SQS

When using virtual queues with a shared host queue, avoid reusing the same [`MessageGroupId`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") across different virtual queues. If
multiple virtual queues share the same host queue and contain messages with the same
`MessageGroupId`, those messages can block each other, preventing
efficient processing. To ensure smooth message processing, assign unique
`MessageGroupId` values for messages in different virtual
queues.
