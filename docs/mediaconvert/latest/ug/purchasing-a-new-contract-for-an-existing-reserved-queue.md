# Purchasing additional RTS for an expired reserved queue

After your initial pricing plan term for reserved transcode slots (RTS) expires, your
reserved queue persists without the capacity to run transcoding jobs. You can send
jobs to the queue, but MediaConvert doesn't process them. To begin processing jobs
through the queue again, you can set up a new pricing plan, which requires a new
12-month commitment.

The following tabs show two options for purchasing transcoding capacity for an
expired reserved queue.

Console
To purchase transcoding capacity for an expired reserved queue by
using the MediaConvert console:

1. Open the [Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list "https://console.aws.amazon.com/mediaconvert/home#/queues/list") page in
   the MediaConvert console.
2. Choose the reserved queue that you want to edit.
3. On the queue’s page, choose **Edit
   queue**.
4. On the **Edit queue** page, choose
   **Renew**.
5. In the **Commitment to purchase RTS for reserved
   queue** section, specify the number of reserved
   transcode slots (RTS) that you want to purchase.
6. Review and agree to the pricing and time commitment. **After you commit to your pricing plan, you can't
   cancel or revert it.** Optionally select
   **Auto renew yearly**.
7. Choose **Purchase additional capacity**. Then
   review your reserved queue details and choose
   **Purchase**.
8. Choose **Save queue**.

AWS CLI
The following `update-queue` example adds one RTS to an
existing expired reserved queue and begins a new 12-month
commitment.

```
aws mediaconvert update-queue \
	--region `region-name-1` \
	--reservation-plan-settings `"Commitment=ONE_YEAR,RenewalType=EXPIRE,ReservedSlots=1"` \
	--name `ReservedQueue1`
```

For more information about how to update queues by using the AWS CLI,
see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html").
