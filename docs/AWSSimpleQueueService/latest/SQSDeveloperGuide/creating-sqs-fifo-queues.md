# Creating an Amazon SQS FIFO queue and sending a

message

You can create an Amazon SQS FIFO queue and send messages using the console. This topic
explains how to set up queue parameters, including visibility timeout, message retention,
and deduplication, while following security best practices such as avoiding sensitive
information in queue names and enabling server-side encryption. It also covers defining
access policies, configuring dead-letter queues, and sending messages with FIFO-specific
attributes like message group ID and deduplication ID.

## Creating a FIFO queue using the Amazon SQS

console

You can use the Amazon SQS console to create [FIFO
queues](sqs-fifo-queues.md "sqs-fifo-queues.md"). The console provides default values for all settings except for the
queue name.

###### Important

On August 17, 2022, default server-side encryption (SSE) was applied to all Amazon SQS
queues.

Do not add personally identifiable information (PII) or other confidential or
sensitive information in queue names. Queue names are accessible to many Amazon Web Services,
including billing and CloudWatch logs. Queue names are not intended to be used for private
or sensitive data.

###### To create an Amazon SQS FIFO queue

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. Choose **Create queue**.
3. For **Type**, the **Standard** queue type is
   set by default. To create a FIFO queue, choose **FIFO**.

###### Note

You can't change the queue type after you create the queue. 4. Enter a **Name** for your queue.

The name of a FIFO queue must end with the `.fifo` suffix. The suffix counts towards the 80-character queue name quota.
To determine whether a queue is [FIFO](sqs-fifo-queues.md "sqs-fifo-queues.md"), you can check whether the queue name ends with the suffix. 5. (Optional) The console sets default values for the queue [configuration parameters](sqs-configure-queue-parameters.md "sqs-configure-queue-parameters.md").
Under **Configuration**, you can set new values for the
following parameters:

    1. For **Visibility timeout** , enter the duration and
     units. The range is from 0 seconds to 12 hours. The default value is 30
     seconds.
    2. For **Message retention period**, enter the duration
     and units. The range is from 1 minute to 14 days. The default value is 4
     days.
    3. For **Delivery delay**, enter the duration and units.
     The range is from 0 seconds to 15 minutes. The default value is 0
     seconds.
    4. For **Maximum message size**, enter a value. The
     range is from 1 KiB to 1024 KiB. The default value is 1024 KiB.
    5. For **Receive message wait time**, enter a value. The
     range is from 0 to 20 seconds. The default value is 0 seconds, which
     sets [short polling](sqs-short-and-long-polling.md "sqs-short-and-long-polling.md").
     Any non-zero value sets long polling.
    6. For a FIFO queue, choose **Content-based
     deduplication** to enable content-based deduplication. The
     default setting is disabled.
    7. (Optional) For a FIFO queue to enable higher throughput for sending and receiving messages in the queue,
    choose **Enable high throughput FIFO**.


    Choosing this option changes the related options (**Deduplication scope** and **FIFO throughput limit**)
    to the required settings for enabling high throughput for FIFO queues. If you change any of the settings required for using high throughput FIFO, normal
    throughput is in effect for the queue, and deduplication occurs as specified. For more information, see
    [High throughput for FIFO queues in Amazon SQS](high-throughput-fifo.md "high-throughput-fifo.md") and
    [Amazon SQS message quotas](quotas-messages.md "quotas-messages.md").

6. (Optional) Define an **Access policy**. The [access
   policy](sqs-creating-custom-policies-access-policy-examples.md "sqs-creating-custom-policies-access-policy-examples.md") defines the accounts, users, and roles that can access the
   queue. The access policy also defines the actions (such as [`SendMessage`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md"), [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md"), or [`DeleteMessage`](../APIReference/API_DeleteMessage.md "../APIReference/API_DeleteMessage.md")) that the users can access. The
   default policy allows only the queue owner to send and receive messages.

To define the access policy, do one of the following:

    * Choose **Basic** to configure who can send messages
     to the queue and who can receive messages from the queue. The console
     creates the policy based on your choices and displays the resulting
     access policy in the read-only JSON panel.
    * Choose **Advanced** to modify the JSON access policy
     directly. This allows you to specify a custom set of actions that each
     principal (account, user, or role) can perform.

7. For **Redrive allow policy**, choose
   **Enabled**. Select one of the following: **Allow
   all**, **By queue**, or **Deny
   all**. When choosing **By queue**, specify a list
   of up to 10 source queues by the Amazon Resource Name (ARN).
8. Amazon SQS provides managed server-side encryption by default. To choose an
   encryption key type, or to disable Amazon SQS managed server-side encryption, expand
   **Encryption**. For more on encryption key types, see [Configuring server-side encryption for a
   queue using SQS-managed encryption keys](sqs-configure-sqs-sse-queue.md "sqs-configure-sqs-sse-queue.md") and [Configuring server-side encryption for a queue
   using the Amazon SQS console](sqs-configure-sse-existing-queue.md "sqs-configure-sse-existing-queue.md").

###### Note

With SSE enabled, anonymous `SendMessage` and
`ReceiveMessage` requests to the encrypted queue will be
rejected. Amazon SQS security best practises recommend against using anonymous
requests. If you wish to send anonymous requests to an Amazon SQS queue, make
sure to disable SSE. 9. (Optional) To configure a [dead-letter queue](sqs-configure-dead-letter-queue.md "sqs-configure-dead-letter-queue.md") to receive undeliverable messages, expand
**Dead-letter queue**. 10. (Optional) To add [tags](sqs-configure-tag-queue.md "sqs-configure-tag-queue.md") to the
queue, expand **Tags**. 11. Choose **Create queue**. Amazon SQS creates the queue and displays
the queue's **Details** page.

Amazon SQS propagates information about the new queue across the system. Because Amazon SQS is a
distributed system, you might experience a slight delay before the console displays the
queue on the **Queues** page.

After creating a queue, you can [send messages](creating-sqs-standard-queues.md#sqs-send-messages "creating-sqs-standard-queues.md#sqs-send-messages")
to it, and [receive and delete
messages](step-receive-delete-message.md "step-receive-delete-message.md"). You can also [edit](sqs-configure-edit-queue.md "sqs-configure-edit-queue.md")
any of the queue configuration settings except the queue type.

## Sending a message using a FIFO queue

After you create your queue, you can send a message to it.

1. From the left navigation pane, choose **Queues**. From the
   queue list, select the queue that you created.
2. From **Actions**, choose **Send and receive
   messages**.

The console displays the **Send and receive messages**
page. 3. In the **Message body**, enter the message
text. 4. For a First-In-First-Out (FIFO) queue, enter a **Message group
ID**. For more information, see [FIFO queue delivery logic in
Amazon SQS](FIFO-queues-understanding-logic.md "FIFO-queues-understanding-logic.md"). 5. (Optional) For a FIFO queue, you can enter a **Message deduplication
ID**. If you enabled content-based deduplication for the queue, the
message deduplication ID isn't required. For more information, see [FIFO queue delivery logic in
Amazon SQS](FIFO-queues-understanding-logic.md "FIFO-queues-understanding-logic.md"). 6. FIFO queues does not support timers on individual messages. For more
information, see [Amazon SQS message timers](sqs-message-timers.md "sqs-message-timers.md"). 7. Choose **Send message**.

When your message is sent, the console displays a success message. Choose
**View details** to display information about the sent
message.
