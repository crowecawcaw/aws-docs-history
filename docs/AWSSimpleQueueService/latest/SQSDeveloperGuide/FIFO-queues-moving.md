# Moving from a standard queue to a FIFO queue in

Amazon SQS

If your existing application uses standard queues and you want to take advantage of
the ordering or exactly-once processing features of FIFO queues, you need to configure
both the queue and your application correctly.

###### Key considerations

- **Creating a FIFO Queue:** You cannot convert an
  existing standard queue into a FIFO queue. You must either create a new FIFO
  queue for your application or delete the existing standard queue and recreate it
  as a FIFO queue.
- **Delay Parameter:** FIFO queues do not support
  per-message delays, only per-queue delays. If your application sets the
  `DelaySeconds` parameter on each message, you must modify it to
  set `DelaySeconds` on the entire queue instead.
- **Message Group ID:** Provide a [message group ID](high-throughput-fifo.md#partitions-and-data-distribution "high-throughput-fifo.md#partitions-and-data-distribution") for every
  sent message. This ID enables parallel processing of messages while maintaining
  their respective order. Use a granular business dimension for the message group
  ID to better scale with FIFO queues. The more message group IDs you distribute
  messages to, the greater the number of messages available for
  consumption.
- **High Throughput Mode:** Use the recommended
  [high throughput mode](high-throughput-fifo.md#partitions-and-data-distribution "high-throughput-fifo.md#partitions-and-data-distribution")
  for FIFO queues to achieve increased throughput. For more information on
  messaging quotas, see [Amazon SQS message quotas](quotas-messages.md "quotas-messages.md").

###### Checklist for moving to FIFO queues

Before sending messages to a FIFO queue, confirm the following:

1.  **Configure delay settings**
    - Modify your application to remove per-message delays.
    - Set the `DelaySeconds` parameter on the entire
      queue.

2.  **Set message group IDs**
    - Organize messages into message groups by specifying a message group ID
      based on a business dimension.
    - Use more granular business dimensions to improve scalability.

3.  **Handle message deduplication**
    - If your application can't send messages with identical message bodies,
      provide a unique message deduplication ID for each message.
    - If your application sends messages with unique message bodies, enable
      content-based deduplication.

4.  **Configure the consumer**

        * Generally, no code changes are needed for the consumer.
        * If processing messages takes a long time and the visibility timeout is
         set high, consider adding a receive request attempt ID to each
         `ReceiveMessage` action. This helps retry receive
         attempts in case of networking failures and prevents queues from pausing
         due to failed receive attempts.

    By following these steps, you can ensure your application works correctly with FIFO
    queues, taking full advantage of their ordering and exactly-once processing features.
    For more detailed information, see the _[Amazon Simple Queue Service API Reference](../APIReference.md "../APIReference.md")_.
