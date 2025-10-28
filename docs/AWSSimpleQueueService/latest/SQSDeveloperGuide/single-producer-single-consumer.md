# Enabling deduplication for a

single-producer/consumer system in Amazon SQS

If you have a single producer and a single consumer, and messages are unique
because they include an application-specific message ID in the body, follow these
best practices:

- Enable content-based deduplication for the queue (each of your messages
  has a unique body). The producer can omit the message deduplication
  ID.
- When content-based deduplication is enabled for an Amazon SQS FIFO queue, and a
  message is sent with a deduplication ID, the [`SendMessage`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") deduplication ID overrides the
  generated content-based deduplication ID.
- Although the consumer isn't required to provide a receive request attempt
  ID for each request, it's a best practice because it allows fail-retry
  sequences to execute faster.
- You can retry send or receive requests because they don't interfere with
  the ordering of messages in FIFO queues.
