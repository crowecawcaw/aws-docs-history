# Using the message deduplication

ID in Amazon SQS

[`MessageDeduplicationId`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") is a token used only in Amazon SQS FIFO
queues to prevent duplicate message delivery. It ensures that within a 5-minute
deduplication window, only one instance of a message with the same deduplication ID is
processed and delivered.

If Amazon SQS has already accepted a message with a specific deduplication ID, any
subsequent messages with the same ID will be acknowledged but not delivered to
consumers.

###### Note

Amazon SQS continues tracking the deduplication ID even after the message has been received and deleted.

###### Topics

- [When to provide a message
  deduplication ID in Amazon SQS](providing-message-deduplication-id.md "providing-message-deduplication-id.md")
- [Enabling deduplication for a
  single-producer/consumer system in Amazon SQS](single-producer-single-consumer.md "single-producer-single-consumer.md")
- [Outage recovery scenarios
  in Amazon SQS](designing-for-outage-recovery-scenarios.md "designing-for-outage-recovery-scenarios.md")
- [Configuring visibility timeouts
  in Amazon SQS](working-with-visibility-timeouts.md "working-with-visibility-timeouts.md")
