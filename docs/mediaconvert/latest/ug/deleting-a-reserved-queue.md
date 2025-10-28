# Deleting a reserved queue

You can delete any queue other than the default queue. You can't delete a reserved
queue that has an active pricing plan or that contains unprocessed jobs. The
following tabs show two options for deleting a reserved queue.

Console
To delete a reserved queue by using the MediaConvert console:

1. Open the [Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list "https://console.aws.amazon.com/mediaconvert/home#/queues/list") page in
   the MediaConvert console.
2. Choose the reserved queue that you want to edit.
3. On the queue’s page, choose **Delete
   queue**.

AWS CLI
The following `delete-queue` deletes an expired reserved
queue.

```
aws mediaconvert delete-queue \
	--region `region-name-1` \
	--name `ReservedQueue1`
```

For more information about how to update queues by using the AWS CLI,
see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html").
