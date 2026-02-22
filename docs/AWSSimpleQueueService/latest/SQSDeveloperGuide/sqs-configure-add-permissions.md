# Configuring an access policy in

Amazon SQS

When you [edit](sqs-configure-edit-queue.md "sqs-configure-edit-queue.md") a queue, you can configure
its access policy to control who can interact with it.

- The access policy defines which accounts, users, and roles have permissions to
  access the queue.
- It specifies the allowed actions, such as [`SendMessage`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md"), [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md"), or [`DeleteMessage`](../APIReference/API_DeleteMessage.md "../APIReference/API_DeleteMessage.md").
- By default, only the queue owner has permission to send and receive
  messages.

###### \*\*To configure the access policy for an existing queue

(console)\*\*

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the navigation pane, choose **Queues**.
3. Choose a queue and choose **Edit**.
4. Scroll to the **Access policy** section.
5. Edit the **access policy statements** in the input box. For
   more on access policy statements, see [Identity and access management in
   Amazon SQS](security-iam.md "security-iam.md").
6. When you finish configuring the access policy, choose
   **Save**.
