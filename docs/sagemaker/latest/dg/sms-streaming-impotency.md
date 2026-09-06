

# Duplicate message handling
<a name="sms-streaming-impotency"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

For data objects sent in real time, Ground Truth guarantees idempotency by ensuring each unique object is only sent for labeling once, even if the input message referring to that object is received multiple times (duplicate messages). To do this, each data object sent to a streaming labeling job is assigned a *deduplication ID*, which is identified with a *deduplication key*. If you send your requests to label data objects directly through your Amazon SNS input topic using Amazon SNS messages, you can optionally choose a custom deduplication key and deduplication IDs for your objects. For more information, see [Specify a deduplication key and ID in an Amazon SNS message](sms-streaming-impotency-create.md).

If you do not provide your own deduplication key, or if you use the Amazon S3 configuration to send data objects to your labeling job, Ground Truth uses one of the following for the deduplication ID:
+ For messages sent directly to your Amazon SNS input topic, Ground Truth uses the SNS message ID. 
+ For messages that come from an Amazon S3 configuration, Ground Truth creates a deduplication ID by combining the Amazon S3 URI of the object with the [sequencer token](https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html) in the message.

**Note**  
Do not use the `$` character in your label attribute name. 