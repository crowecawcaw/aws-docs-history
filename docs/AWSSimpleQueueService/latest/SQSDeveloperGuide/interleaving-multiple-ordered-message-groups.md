# Interleaving multiple

ordered message groups in Amazon SQS

To interleave multiple ordered message groups within a single FIFO queue, assign a
[`MessageGroupId`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") to each group (for example, session
data for different users). This allows multiple consumers to read from the queue
simultaneously while ensuring that messages within the same group are processed in
order.

When a message with a specific `MessageGroupId` is being processed and
is invisible, no other consumer can process messages from that same group until the
visibility timeout expires or the message is deleted.
