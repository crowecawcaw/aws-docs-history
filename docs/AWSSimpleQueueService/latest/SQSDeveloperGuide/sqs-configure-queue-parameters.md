# Configuring queue parameters using the Amazon SQS

console

When [creating](creating-sqs-standard-queues.md#step-create-standard-queue "creating-sqs-standard-queues.md#step-create-standard-queue") or [editing](sqs-configure-edit-queue.md "sqs-configure-edit-queue.md") a queue, you can configure the following
parameters:

- **Visibility timeout** – The length of time that a message
  received from a queue (by one consumer) won't be visible to the other message consumers. For
  more information, see [Visibility timeout](sqs-visibility-timeout.md "sqs-visibility-timeout.md").

###### Note

Using the console to configure the visibility timeout configures the timeout value for
all of the messages in the queue. To configure the timeout for single or multiple
messages, you must use one of the AWS SDKs.

- **Message retention period** – The amount of time that Amazon SQS
  retains messages that remain in the queue. By default, the queue retains messages for four
  days. You can configure a queue to retain messages for up to 14 days. For more information,
  see [Message retention period](../APIReference/API_SetQueueAttributes.md "../APIReference/API_SetQueueAttributes.md").
- **Delivery delay** – The amount of time that Amazon SQS will delay
  before delivering a message that is added to the queue. For more information, see [Delivery delay](sqs-delay-queues.md "sqs-delay-queues.md").
- **Maximum message size** – The maximum message size for this
  queue. For more information, see [Maximum message
  size](sqs-s3-messages.md "sqs-s3-messages.md").
- **Receive message wait time** – The maximum amount of time that
  Amazon SQS waits for messages to become available after the queue gets a receive request. For
  more information, see [Amazon SQS short and long polling](sqs-short-and-long-polling.md "sqs-short-and-long-polling.md").
- **Enable content-based deduplication** – Amazon SQS can automatically
  create deduplication IDs based on the body of the message. For more information, see [Amazon SQS FIFO queues](sqs-fifo-queues.md "sqs-fifo-queues.md").
- **Enable high throughput FIFO** – Use to enable high throughput
  for messages in the queue. Choosing this option changes the related options ([Deduplication scope](enable-high-throughput-fifo.md "enable-high-throughput-fifo.md") and [FIFO throughput limit](enable-high-throughput-fifo.md "enable-high-throughput-fifo.md")) to the required
  settings for enabling high throughput for FIFO queues. For more information, see [High throughput for FIFO queues in Amazon SQS](high-throughput-fifo.md "high-throughput-fifo.md") and [Amazon SQS message quotas](quotas-messages.md "quotas-messages.md").
- **Redrive allow policy**: defines which source queues can use this queue as
  the dead-letter queue. For more information, see [Using dead-letter queues in Amazon SQS](sqs-dead-letter-queues.md "sqs-dead-letter-queues.md") .

###### To configure queue parameters for an existing queue (console)

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the navigation pane, choose **Queues**. Choose a queue and choose
   **Edit**.
3. Scroll to the **Configuration** section.
4. For **Visibility timeout** , enter the duration and units. The range is
   0 seconds to 12 hours. The default value is 30 seconds.
5. For **Message retention period**, enter the duration and units. The
   range is 1 minute to 14 days. The default value is 4 days.
6. For a standard queue, enter a value for **Receive message wait time**.
   The range is 0 to 20 seconds. The default value is 0 seconds, which sets [short polling](sqs-short-and-long-polling.md "sqs-short-and-long-polling.md"). Any non-zero value sets long
   polling.
7. For **Delivery delay**, enter the duration and units. The range is 0
   seconds to 15 minutes. The default value is 0 seconds.
8. For **Maximum message size**, enter a value. The
   range is from 1 KiB to 1024 KiB. The default value is 1024 KiB.
9. For a FIFO queue, choose **Enable content-based deduplication** to
   enable content-based deduplication. The default setting is disabled.
10. (Optional) For a FIFO queue to enable higher throughput for sending and receiving messages in the queue,
    choose **Enable high throughput FIFO**.

Choosing this option changes the related options (**Deduplication scope** and **FIFO throughput limit**)
to the required settings for enabling high throughput for FIFO queues. If you change any of the settings required for using high throughput FIFO, normal
throughput is in effect for the queue, and deduplication occurs as specified. For more information, see
[High throughput for FIFO queues in Amazon SQS](high-throughput-fifo.md "high-throughput-fifo.md") and
[Amazon SQS message quotas](quotas-messages.md "quotas-messages.md"). 11. For **Redrive allow policy**, choose **Enabled**.
Select from the following: **Allow all** (default), **By
queue** or **Deny all**. When choosing **By
queue**, specify a list of up to 10 source queues by the Amazon Resource Name
(ARN). 12. When you finish configuring the queue parameters, choose
**Save**.
