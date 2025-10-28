# Outage recovery scenarios

in Amazon SQS

The deduplication process in FIFO queues is time-sensitive. When designing your
application, ensure that both the producer and consumer can recover from client or
network outages without introducing duplicates or processing failures.

Producer considerations

- Amazon SQS enforces a 5-minute deduplication window.
- If a producer retries a [`SendMessage`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") request after 5-minutes, Amazon SQS
  treats it as a new message, potentially creating duplicates.
  Consumer considerations

- If a consumer fails to process a message before the visibility timeout
  expires, another consumer may receive and process it, leading to duplicate
  processing.
- Adjust the visibility timeout based on your application's processing
  time.
- Use the [`ChangeMessageVisibility`](../APIReference/API_ChangeMessageVisibility.md "../APIReference/API_ChangeMessageVisibility.md") API to extend the
  timeout while a message is still being processed.
- If a message repeatedly fails to process, route it to a [dead-letter queue (DLQ)](sqs-dead-letter-queues.md "sqs-dead-letter-queues.md") instead
  of allowing it to be reprocessed indefinitely.

- The producer must be aware of the deduplication interval of the queue.
  Amazon SQS has a deduplication interval of 5 minutes. Retrying
  `SendMessage` requests after the deduplication interval
  expires can introduce duplicate messages into the queue. For example, a
  mobile device in a car sends messages whose order is important. If the car
  loses cellular connectivity for a period of time before receiving an
  acknowledgement, retrying the request after regaining cellular connectivity
  can create a duplicate.
- The consumer must have a visibility timeout that minimizes the risk of
  being unable to process messages before the visibility timeout expires. You
  can extend the visibility timeout while the messages are being processed by
  calling the `ChangeMessageVisibility` action. However, if the
  visibility timeout expires, another consumer can immediately begin to
  process the messages, causing a message to be processed multiple times. To
  avoid this scenario, configure a [dead-letter queue](sqs-dead-letter-queues.md "sqs-dead-letter-queues.md").
