# Creating an Amazon SQS standard queue and sending

a message

You can create a [standard queue](standard-queues.md "standard-queues.md") and send messages
using the Amazon SQS console. This topic also emphasizes best practices, including avoiding
sensitive information in queue names and utilizing managed server-side encryption.

## Creating a standard queue using the Amazon SQS

console

###### Important

On August 17, 2022, default server-side encryption (SSE) was applied to all Amazon SQS
queues.

Do not add personally identifiable information (PII) or other confidential or
sensitive information in queue names. Queue names are accessible to many Amazon Web Services,
including billing and CloudWatch logs. Queue names are not intended to be used for private
or sensitive data.

###### To create an Amazon SQS standard queue

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. Choose **Create queue**.
3. For **Type**, the **Standard** queue type is
   set by default.

###### Note

You can't change the queue type after you create the queue. 4. Enter a **Name** for your queue. 5. (Optional) The console sets default values for the queue [configuration parameters](sqs-configure-queue-parameters.md "sqs-configure-queue-parameters.md").
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

## Sending a message using a standard queue

After your queue has been created, you can send a message to it.

1. From the left navigation pane, choose **Queues**. From the
   queue list, select the queue that you created.
2. From **Actions**, choose **Send and receive
   messages**.

The console displays the **Send and receive messages**
page. 3. In the **Message body**, enter the message
text. 4. For a standard queue, you can enter a value for **Delivery
delay** and choose the units. For example, enter `60`
and choose **seconds**. For more information, see [Amazon SQS message timers](sqs-message-timers.md "sqs-message-timers.md"). 5. Choose **Send message**.

When your message is sent, the console displays a success message. Choose
**View details** to display information about the sent
message.
