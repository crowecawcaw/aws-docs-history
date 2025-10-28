# Pricing for reserved queues

With reserved queues, you pay for the capacity in the queue regardless of
whether you use it. When you set up a reserved queue, you make a 12-month
commitment to a pricing plan. The pricing plan specifies a fixed number of
reserved transcode slots (RTS). For more information, see [MediaConvert
Pricing](https://aws.amazon.com/mediaconvert/pricing/ "https://aws.amazon.com/mediaconvert/pricing/").

###### Important

After you purchase your RTS, you can't cancel your 12-month
commitment.

You can purchase additional capacity for a reserved queue that already has
RTS. To purchase additional capacity, you extend your existing commitment with a
new 12-month commitment for a larger number of RTS. The new commitment begins
when you purchase the additional capacity. You can't decrease the number of RTS
in your reserved queue.

When your pricing plan term expires, your reserved queue persists. You can
still send jobs to it, but AWS Elemental MediaConvert doesn't run them.

###### About Auto Renew

You can set your pricing plan to auto renew. When your pricing plan term
ends, AWS Elemental MediaConvert checks the auto renew status. If auto renew is
enabled at that time, you automatically commit to another 12-month term for
the same number of RTS at the same price. You can change the auto renew
status at any time.

You can choose auto renew when you set up your queue. Anytime after that, you
can change the auto renew status on the **Edit** page for the
queue. For more information, see [Creating a reserved queue](creating-a-reserved-queue.md "creating-a-reserved-queue.md") and [Editing a reserved queue](editing-reserved-queues.md "editing-reserved-queues.md").

###### About billing when jobs hop queues

When you set up [queue
hopping](setting-up-queue-hopping-to-avoid-long-waits.md "setting-up-queue-hopping-to-avoid-long-waits.md") between a reserved queue and an on-demand queue,
MediaConvert bills you according to the queue that it runs your job from.
That is, if the job runs from your reserved queue, MediaConvert doesn't
bill you for the job. If the job runs from your on-demand queue,
MediaConvert bills you for the job at the on-demand rate.
