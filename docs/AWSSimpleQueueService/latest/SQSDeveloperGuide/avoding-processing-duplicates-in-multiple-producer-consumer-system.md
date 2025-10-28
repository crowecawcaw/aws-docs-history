# Preventing duplicate processing in a multiple-producer/consumer system in

Amazon SQS

In a high-throughput, low-latency system where message ordering is not a priority,
producers can assign a unique [`MessageGroupId`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") to each message. This ensures that
Amazon SQS FIFO queues eliminate duplicates, even in a
multiple-producer/multiple-consumer setup. While this approach prevents duplicate
messages, it does not guarantee message ordering since each message is treated as
its own independent group.

In any system with multiple producers and consumers, there is always a risk of
duplicate delivery. If a consumer fails to process a message before the visibility
timeout expires, Amazon SQS makes the message available again, potentially allowing
another consumer to pick it up. To mitigate this, ensure proper message
acknowledgment and visibility timeout settings based on processing time.
