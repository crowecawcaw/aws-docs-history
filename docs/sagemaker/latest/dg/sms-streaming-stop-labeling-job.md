

# Stop a Streaming Labeling Job
<a name="sms-streaming-stop-labeling-job"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

You can manually stop your streaming labeling job using the operation [StopLabelingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopLabelingJob.html). 

If your labeling job remains idle for over 10 days, it is automatically stopped by Ground Truth. In this context, a labeling job is considered *idle* if no objects are sent to the Amazon SNS input topic and no objects remain in your Amazon SQS queue, waiting to be labeled. For example, if no data objects are fed to the Amazon SNS input topic and all the objects fed to the labeling job are already labeled, Ground Truth starts a timer. After the timer starts, if no items are received within a 10 day period, the labeling job is stopped. 

When a labeling job is stopped, its status is `STOPPING` while Ground Truth cleans up labeling job resources and unsubscribes your Amazon SNS topic from your Amazon SQS queue. The Amazon SQS is *not* deleted by Ground Truth because this queue may contain unprocessed data objects. You should manually delete the queue if you want to avoid incurring additional charges from Amazon SQS. To learn more, see [Amazon SQS pricing ](https://aws.amazon.com/sqs/pricing/).