# Using the message group ID with Amazon SQS FIFO Queues

In FIFO (First-In-First-Out) queues, [`MessageGroupId`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") is an attribute that organizes messages into distinct groups.
Messages within the same message group are always processed one at a time, in strict order,
ensuring that no two messages from the same group are processed simultaneously.
In standard queues, using `MessageGroupId` enables [fair queues](sqs-fair-queues.md "sqs-fair-queues.md").
If strict ordering is required, use a FIFO queue.

###### Topics

- [Interleaving multiple
  ordered message groups in Amazon SQS](interleaving-multiple-ordered-message-groups.md "interleaving-multiple-ordered-message-groups.md")
- [Preventing duplicate processing in a multiple-producer/consumer system in
  Amazon SQS](avoding-processing-duplicates-in-multiple-producer-consumer-system.md "avoding-processing-duplicates-in-multiple-producer-consumer-system.md")
- [Avoid large message
  backlogs with the same message group ID in Amazon SQS](avoid-backlog-with-the-same-message-group-id.md "avoid-backlog-with-the-same-message-group-id.md")
- [Avoid
  reusing the same message group ID with virtual queues in Amazon SQS](avoiding-reusing-message-group-id-with-virtual-queues.md "avoiding-reusing-message-group-id-with-virtual-queues.md")
