# TopicConfiguration

A container for specifying the configuration for publication of messages to an Amazon Simple
 Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.


## Contents





**Events** 


The Amazon S3 bucket event about which to send notifications. For more information, see [Supported Event Types](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html") in
 the *Amazon S3 User Guide*.


Type: Array of strings


Valid Values: `s3:ReducedRedundancyLostObject | s3:ObjectCreated:* | s3:ObjectCreated:Put | s3:ObjectCreated:Post | s3:ObjectCreated:Copy | s3:ObjectCreated:CompleteMultipartUpload | s3:ObjectRemoved:* | s3:ObjectRemoved:Delete | s3:ObjectRemoved:DeleteMarkerCreated | s3:ObjectRestore:* | s3:ObjectRestore:Post | s3:ObjectRestore:Completed | s3:Replication:* | s3:Replication:OperationFailedReplication | s3:Replication:OperationNotTracked | s3:Replication:OperationMissedThreshold | s3:Replication:OperationReplicatedAfterThreshold | s3:ObjectRestore:Delete | s3:LifecycleTransition | s3:IntelligentTiering | s3:ObjectAcl:Put | s3:LifecycleExpiration:* | s3:LifecycleExpiration:Delete | s3:LifecycleExpiration:DeleteMarkerCreated | s3:ObjectTagging:* | s3:ObjectTagging:Put | s3:ObjectTagging:Delete`



Required: Yes




**TopicArn** 


The Amazon Resource Name (ARN) of the Amazon SNS topic to which Amazon S3 publishes a message when it
 detects events of the specified type.


Type: String


Required: Yes




**Filter** 


Specifies object key name filtering rules. For information about key name filtering, see [Configuring
 event notifications using object key name filtering](../userguide/notification-how-to-filtering.md "../userguide/notification-how-to-filtering.md") in the
 *Amazon S3 User Guide*.


Type: [NotificationConfigurationFilter](API_NotificationConfigurationFilter.md "API_NotificationConfigurationFilter.md") data type


Required: No




**Id** 


An optional unique identifier for configurations in a notification configuration. If you don't
 provide one, Amazon S3 will assign an ID.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/TopicConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/TopicConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/TopicConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/TopicConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/TopicConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/TopicConfiguration")
