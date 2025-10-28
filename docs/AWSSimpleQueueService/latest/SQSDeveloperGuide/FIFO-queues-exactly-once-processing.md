# Exactly-once processing in

Amazon SQS

Unlike standard queues, FIFO queues don't introduce duplicate messages. FIFO queues
help you avoid sending duplicates to a queue. If you retry the `SendMessage`
action within the 5-minute deduplication interval, Amazon SQS doesn't introduce any
duplicates into the queue.

To configure deduplication, you must do one of the following:

- Enable content-based deduplication. This instructs Amazon SQS to use a SHA-256 hash
  to generate the message deduplication ID using the body of the
  message—but not the attributes of the message. For more information, see
  the documentation on the `CreateQueue`, `GetQueueAttributes`, and `SetQueueAttributes` actions in the
  _Amazon Simple Queue Service API Reference_.
- Explicitly provide the message deduplication ID (or view the sequence number)
  for the message. For more information, see the documentation on the `SendMessage`,
  `SendMessageBatch`, and `ReceiveMessage`
  actions in the _Amazon Simple Queue Service API Reference_.
