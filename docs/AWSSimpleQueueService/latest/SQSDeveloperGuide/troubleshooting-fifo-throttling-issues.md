

# Troubleshoot FIFO throttling issues in Amazon SQS
<a name="troubleshooting-fifo-throttling-issues"></a>

By default, FIFO queues support 300 transactions per second, per API action for [`SendMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html), [`ReceiveMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html), and [`DeleteMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html). Requests over 300 TPS get the `ThrottlingException` error even if messages in the queue are available. To mitigate this, you can use following methods:
+ [Enabling high throughput for FIFO queues in Amazon SQS](enable-high-throughput-fifo.md).
+ Use the Amazon SQS API batch actions `SendMessageBatch`, `DeleteMessageBatch`, and `ChangeMessageVisibilityBatch` to increase the TPS limit of up to 3,000 messages per second per API action, and to reduce cost. For the `ReceiveMessage` API, set the `MaxNumberofMessages` parameter to receive up to ten messages per transaction. For more information, see [Amazon SQS batch actions](sqs-batch-api-actions.md).
+ For FIFO queues with high throughput, follow the recommendations to [optimize partition utilization](high-throughput-fifo.md#data-distribution-partition-limitations). Send messages with the same message group IDs in batches. Delete messages, or change the message visibility timeout values in batches with receipt handles from the same `ReceiveMessage` API requests.
+ Increase the number of unique [`MessageGroupId`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html#SQS-SendMessage-request-MessageGroupId) values. This allows for an even distribution across FIFO queue partitions. For more information, see Using the Amazon SQS message group ID.

For more information, see [Why doesn't my Amazon SQS FIFO queue return all messages or messages in other message groups?](https://repost.aws/knowledge-center/sqs-fifo-messages-not-returned) in the *AWS Knowledge Center Guide*.