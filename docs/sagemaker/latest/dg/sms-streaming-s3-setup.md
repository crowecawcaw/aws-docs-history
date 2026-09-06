

# Creating Amazon S3 based bucket event notifications based of the Amazon SNS defined in your labeling job
<a name="sms-streaming-s3-setup"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

Changes to your Amazon S3 bucket, event notifications, are enabled either the Amazon S3 console, API, language specific AWS SDKs, or the AWS Command Line Interface. Events must use the same Amazon SNS input topic ARN, `SnsTopicArn`, specified in the `InputConfig` parameter as part of your `CreateLabelingJob` request.

**Amazon S3 bucket notifications and your input data should not be the same Amazon S3 bucket**  
When you create event notifications do not use the same Amazon S3 location that you specified as your `S3OutputPath` in the `OutputConfig` parameters. Linking the two buckets may result in unwanted data objects being processed by Ground Truth for labeling.

You control the types of events that you want to send to your Amazon SNS topic. Ground Truth creates a labeling job when you send [object creation events](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/enable-event-notifications.html#enable-event-notifications-types).

The event structure sent to your Amazon SNS input topic must be a JSON message formatted using the same structure found in [Event message structure](https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html).

To see examples of how you can set up an event notification for your Amazon S3 bucket using the Amazon S3 console, AWS SDK for .NET, and AWS SDK for Java, follow this walkthrough,[Walkthrough: Configure a bucket for notifications (SNS topic or SQS queue)](https://docs.aws.amazon.com/AmazonS3/latest/dev/ways-to-add-notification-config-to-bucket.html) in the *Amazon Simple Storage Service User Guide*.

Amazon EventBridge notifications are not natively supported. To use EventBridge based notification you must update the output format to match the JSON format used in the [Event message structure](https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html).