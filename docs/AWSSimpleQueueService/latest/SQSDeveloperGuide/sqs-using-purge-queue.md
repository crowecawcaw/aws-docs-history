

# Purging messages from an queue using the Amazon SQS console
<a name="sqs-using-purge-queue"></a>

To keep an Amazon SQS queue but remove all its messages, you can purge the queue. This will delete all messages, including those that are currently invisible (in flight). The purge process can take up to 60 seconds, so wait the full 60 seconds regardless of the queue’s size.

**Important**  
When you purge a queue, you can't retrieve any of the deleted messages.

**To purge a queue (console)**

1. Open the Amazon SQS console at [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/).

1. In the navigation pane, choose **Queues**.

1. On the **Queues** page, choose the queue to purge. 

1. From **Actions**, choose **Purge**.

1. In the **Purge queue** dialog box, confirm the purge by entering **purge** and choosing **Purge**.
   + All messages are purged from the queue. The console displays a confirmation banner.