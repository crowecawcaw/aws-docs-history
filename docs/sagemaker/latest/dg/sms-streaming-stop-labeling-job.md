# Stop a Streaming Labeling

Job

You can manually stop your streaming labeling job using the operation [StopLabelingJob](../APIReference/API_StopLabelingJob.md "../APIReference/API_StopLabelingJob.md").

If your labeling job remains idle for over 10 days, it is automatically stopped by
Ground Truth. In this context, a labeling job is considered _idle_ if no
objects are sent to the Amazon SNS input topic and no objects remain in your Amazon SQS queue,
waiting to be labeled. For example, if no data objects are fed to the Amazon SNS input topic
and all the objects fed to the labeling job are already labeled, Ground Truth starts a timer.
After the timer starts, if no items are received within a 10 day period, the labeling
job is stopped.

When a labeling job is stopped, its status is `STOPPING` while Ground Truth cleans
up labeling job resources and unsubscribes your Amazon SNS topic from your Amazon SQS queue. The
Amazon SQS is _not_ deleted by Ground Truth because this queue may
contain unprocessed data objects. You should manually delete the queue if you want to
avoid incurring additional charges from Amazon SQS. To learn more, see [Amazon SQS pricing](https://aws.amazon.com/sqs/pricing/ "https://aws.amazon.com/sqs/pricing/") .
