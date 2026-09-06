

# Configuring an access policy in Amazon SQS
<a name="sqs-configure-add-permissions"></a>

When you [edit](sqs-configure-edit-queue.md) a queue, you can configure its access policy to control who can interact with it.
+ The access policy defines which accounts, users, and roles have permissions to access the queue.
+ It specifies the allowed actions, such as [`SendMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html), [`ReceiveMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html), or [`DeleteMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html).
+ By default, only the queue owner has permission to send and receive messages.

****To configure the access policy for an existing queue (console)****

1. Open the Amazon SQS console at [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/).

1. In the navigation pane, choose **Queues**. 

1. Choose a queue and choose **Edit**. 

1. Scroll to the **Access policy** section.

1. Edit the **access policy statements** in the input box. For more on access policy statements, see [Identity and access management in Amazon SQS](security-iam.md).

1. When you finish configuring the access policy, choose **Save**.