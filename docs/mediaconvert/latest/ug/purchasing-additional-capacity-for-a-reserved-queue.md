# Purchasing additional RTS

To increase the number of jobs that your reserved queue can process at once, you can
purchase additional capacity for it. To purchase additional capacity, you extend
your existing commitment with a new 12-month commitment for a larger number of
reserved transcode slots (RTS). The new commitment begins when you purchase the
additional capacity. You can't decrease the number of RTS in your reserved queue.
You can't cancel your commitment or revert to your original commitment after you
increase the capacity.

The following tabs show how to purchase additional capacity for a reserved queue.

Console
To purchase additional capacity for a reserved queue by using the
MediaConvert console:

1. Open the [Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list "https://console.aws.amazon.com/mediaconvert/home#/queues/list") page in
   the MediaConvert console.
2. In the **Reserved queues** section, select
   the reserved queue that you want to purchase additional capacity
   for.
3. Choose **Purchase additional
   capacity**.
4. In the **Commitment to purchase RTS for reserved
   queue** section, enter the number of reserved
   transcode slots (RTS) that you want to purchase. This number
   includes both the original amount of reserved transcode slots
   and the new additional capacity.
5. Review and agree to the pricing and time commitment. **After you commit to your pricing plan, you can't
   cancel or revert it.** Optionally, select
   **Auto renew yearly**.
6. Choose **Purchase additional capacity**. Then
   review your reserved queue details and choose
   **Purchase**.

AWS CLI
The following `update-queue` example adds an additional RTS
to an existing reserved queue and begins a new 12-month
commitment.

```
aws mediaconvert update-queue \
	--region `region-name-1` \
	--reservation-plan-settings `"Commitment=ONE_YEAR,RenewalType=EXPIRE,ReservedSlots=2"` \
	--name `ReservedQueue1`
```

For more information about how to update queues by using the AWS CLI, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html").
