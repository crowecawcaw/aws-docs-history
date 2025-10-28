# Editing a reserved queue

When you edit a queue, you can change the following:

- The description, which helps you identify it in the queue
  dashboard.
- The auto renew status of the queue's pricing plan for reserved transcode
  slots (RTS). For more information, see [Pricing for reserved queues](how-you-pay-for-reserved-queues.md "how-you-pay-for-reserved-queues.md").
- The paused or active status of the queue. Pausing the queue prevents the
  service from starting any more jobs until you reactivate the queue.

The following tabs show two options for editing a reserved queue.

Console
To edit a reserved queue by using the MediaConvert console:

1. Open the [Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list "https://console.aws.amazon.com/mediaconvert/home#/queues/list") page in
   the MediaConvert console.
2. In the **Reserved queues** section, select
   the reserved queue that you want to edit.
3. On the queue’s page, choose **Edit
   queue**.
4. On the **Edit queue** page, make the changes
   that you want for the queue.
5. Choose **Save queue**.

AWS CLI
The following `update-queue` example updates the
description and status of an existing reserved queue.

```
aws mediaconvert update-queue \
	--region `region-name-1` \
	--description `"Updated description."` \
	--status `"PAUSED"` \
	--name `ReservedQueue1`
```

For more information about how to update queues by using the AWS CLI,
see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html").
