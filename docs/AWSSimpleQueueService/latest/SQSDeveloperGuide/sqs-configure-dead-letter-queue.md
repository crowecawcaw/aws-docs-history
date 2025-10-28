# Configure a dead-letter queue using the

Amazon SQS console

A dead-letter queue (DLQ) is a queue that receives messages that were not successfully
processed from another queue, known as the source queue. Amazon SQS does _not_ create the dead-letter queue automatically.
You must first create the queue before using it as a dead-letter queue.
When configuring a DLQ, the queue type must match the source queue type—a [FIFO queue](sqs-fifo-queues.md "sqs-fifo-queues.md") can only use a FIFO DLQ, and a [standard queue](standard-queues.md "standard-queues.md") can only use a standard DLQ. You can
configure a dead-letter queue when you create or edit a queue. For more details, see [Using dead-letter queues in Amazon SQS](sqs-dead-letter-queues.md "sqs-dead-letter-queues.md") .

###### To configure a dead-letter queue for an existing queue (console)

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the navigation pane, choose **Queues**.
3. Select the **source queue** (the queue that will send
   failed messages to the dead-letter queue), then choose **Edit**.
4. Scroll to the **Dead-letter queue** section and toggle
   **Enabled**.
5. Under **Dead-letter queue settings**, choose the
   Amazon Resource Name (ARN) of an existing queue that you want to use as the
   **dead-letter queue**.
6. Set the **Maximum receives** value, which defines how
   many times a message can be received before being sent to the dead-letter queue
   (valid range: **1 to 1,000**).
7. Choose **Save**.
