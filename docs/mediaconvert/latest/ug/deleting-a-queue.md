# Deleting a queue

You can delete any queue other than the default queue. You can't delete a queue that
contains unprocessed jobs. The following tabs show how to delete an on-demand
queue.

Console
To delete an on-demand queue by using the MediaConvert
console:

1. Open the [Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list "https://console.aws.amazon.com/mediaconvert/home#/queues/list") page in
   the MediaConvert console.
2. Select the queue.
3. Choose **Delete queue**.

AWS CLI
The following `delete-queue` example deletes on-demand
queue.

```
aws mediaconvert delete-queue \
	--name `Queue1`
```

For more information about how to delete an on-demand queue by using
the AWS CLI, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/delete-queue.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/delete-queue.html").
