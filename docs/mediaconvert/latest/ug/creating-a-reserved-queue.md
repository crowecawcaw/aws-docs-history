# Creating a reserved queue

If you decide to purchase additional capacity for your reserved queue, you can. For more
information, see [Purchasing additional RTS](purchasing-additional-capacity-for-a-reserved-queue.md "purchasing-additional-capacity-for-a-reserved-queue.md"). The
following tabs show different options for creating a reserved queue.

Console
To create a reserved queue by using the MediaConvert console:

1. Open the [Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list "https://console.aws.amazon.com/mediaconvert/home#/queues/list")
   page in the MediaConvert console.
2. Choose **Create reserved queue**.
3. Enter a **Reserved queue name**. Optionally enter a
   **Description**.
4. Optionally, use the **Reserved transcode slots (RTS) calculator** to
   help determine how many RTS that you need.
5. In the **Commitment to purchase RTS for reserved queue** section,
   enter the number of reserved transcode slots (RTS) that you want
   to purchase.
6. Review and agree to the pricing and time commitment. **After you
   commit to your pricing plan, you can't cancel it.**
   Optionally, select **Auto renew
   yearly**.
7. Choose **Create reserved queue**. Then review your reserved queue
   details and choose **Purchase.**

AWS CLI
The following `create-queue` example creates a reserved queue with one RTS
slot and a 12-month commitment.

```
aws mediaconvert create-queue \
	--region `region-name-1` \
	--pricing-plan `RESERVED` \
	--reservation-plan-settings `"Commitment=ONE_YEAR,RenewalType=EXPIRE,ReservedSlots=1"` \
	--name `ReservedQueue1` \
	--description `"Example reserved queue description."` \
	--tags `"KeyName1=string1,KeyName2=string2"`
```

For more information about how to create a reserved queue by using the
AWS CLI, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-queue.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-queue.html").
