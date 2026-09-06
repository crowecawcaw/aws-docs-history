

# Configuring cost allocation tags for a queue using the Amazon SQS console
<a name="sqs-configure-tag-queue"></a>

To organize and identify your Amazon SQS queues, you can add cost allocation tags. For more information, see [Amazon SQS cost allocation tags](sqs-queue-tags.md).
+ The Tagging tab on the Details page displays the queue's tags.
+ You can add or modify tags when [creating](creating-sqs-standard-queues.md#step-create-standard-queue) or [editing](sqs-configure-edit-queue.md) a queue.

**To configure tags for an existing queue (console)**

1. Open the Amazon SQS console at [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/).

1. In the navigation pane, choose **Queues**. 

1. Choose a queue and choose **Edit**. 

1. Scroll to the **Tags** section.

1. Add, modify, or remove the queue tags:

   1. To add a tag, choose **Add new tag**, enter a **Key** and **Value**, and then choose **Add new tag**.

   1. To update a tag, change its **Key** and **Value**.

   1. To remove a tag, choose **Remove** next to its key-value pair.

1. When you finish configuring the tags, choose **Save**.