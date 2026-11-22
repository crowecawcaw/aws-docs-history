

# Manage queues in the console

You can create and manage queues in the Kinesis console. On the **Queues** page, you can list, create, edit, and delete queues, and receive records from a queue to inspect what it delivers.

**To create a queue**

1. Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the navigation pane, choose **Queues**.

1. Choose **Create queue**.

1. For **Kinesis data stream**, choose the On-demand data stream that the queue delivers records from.

1. For **Queue name**, enter a name for the queue.

1. For **Starting position**, choose where the queue begins delivering records. The default is **Latest**.

1. For **Visibility timeout (seconds)**, enter the default visibility timeout for records the queue delivers, from 0 to 43,200 seconds (12 hours). The default is 30 seconds.

1. For **Dead-letter handling**, keep **Enable dead-letter handling** selected. For **Maximum receive count**, enter the number of times a record can be received without being acknowledged before the queue moves it to the dead-letter state, from 1 to 1,000. The default is 6.

1. To turn dead-letter handling off, clear **Enable dead-letter handling**. The queue then redelivers an unacknowledged record until it is acknowledged or its retention period ends.

1. (Optional) For **Tags**, add tags to the queue.

1. Choose **Create queue**.

1. Wait until the queue's status is **Active** before you receive records. A queue that is still creating returns no records.

**To view queue details**

1. Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the navigation pane, choose **Queues**.

1. Choose the name of the queue.

1. Review the **Details** panel, which shows the queue name, status, ARN, and the data stream the queue delivers records from, along with the starting position, the visibility timeout, and the creation date. It also shows whether dead-letter handling is enabled, the maximum receive count, and the number of dead-letter records.

   Then review the following tabs:
   + **Monitoring**: the Amazon CloudWatch metrics for the queue.
   + **Tags**: the tags on the queue.
   + **Access policy**: the resource policy that grants another account access to the queue.

**To edit a queue**

1. Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the navigation pane, choose **Queues**.

1. Choose the name of the queue, and then choose **Edit**.

1. Change the **Visibility timeout (seconds)**, **Dead-letter handling**, **Access policy**, or **Tags**. The data stream, the queue name, and the starting position are shown for reference and cannot be changed after the queue is created.

1. Choose **Save changes**.

**To delete a queue**

1. Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the navigation pane, choose **Queues**.

1. Select the queue to delete.

1. Choose **Delete**.

1. When prompted for confirmation, type **delete** in the field, and then choose **Delete**. Deleting a queue does not delete the stream or its records: the records stay in the stream until its retention period ends, and stream consumers and the other queues on the stream are not affected.

**To receive records from a queue**

1. Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. In the navigation pane, choose **Queues**.

1. Choose the name of the queue.

1. Choose **Receive records** to open the **Receive records** page.

1. (Optional) Choose **Receive settings**. For **Wait time**, enter how long each call waits for records before returning, from 1 to 20 seconds. For **Maximum records**, enter the number of records to return per call, from 1 to 10. Choose **Save**.

1. On the **Receive records** page, choose **Receive records** to start receiving. The records appear in the **Records** table with their record ID, receipt handle, partition key, approximate arrival time, and receive count.

1. Choose **Stop** to stop receiving. The records you received are in flight: they are not visible to any queue consumer instance for the duration of the visibility timeout, and then become visible again if they are not acknowledged.

1. To acknowledge a record so that the queue does not deliver it again, select it and then choose **Acknowledge**. To see the full contents of a record, select it and then choose **View details**.