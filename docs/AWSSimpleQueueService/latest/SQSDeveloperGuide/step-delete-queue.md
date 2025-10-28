# Deleting an Amazon SQS queue

If you no longer use an Amazon SQS queue and don’t plan to use it in the near future,
delete the queue.

###### Tip

If you want to verify that a queue is empty before you delete it, see [Confirming that an Amazon SQS queue is empty](confirm-queue-is-empty.md "confirm-queue-is-empty.md").

You can delete a queue even when it isn't empty. To delete the messages in a queue but
not the queue itself, [purge the
queue](sqs-using-purge-queue.md "sqs-using-purge-queue.md").

###### To delete a queue (console)

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the navigation pane, choose **Queues**.
3. On the **Queues** page, choose the queue to delete.
4. Choose **Delete**.
5. In the **Delete queue** dialog box, confirm the deletion by
   entering `delete`.
6. Choose **Delete**.

###### To delete a queue (AWS CLI and API)

Choose the appropriate method to delete your queue based on your needs:

- AWS CLI: `aws sqs
delete-queue`
- AWS API: `DeleteQueue`
