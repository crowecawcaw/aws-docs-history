# Event notification types and destinations

Amazon S3 supports several event notification types and destinations where the
notifications can be published. You can specify the event type and destination when
configuring your event notifications. Only one destination can be specified for each
event notification. Amazon S3 event notifications send one event entry for each
notification message.

###### Topics

- [Supported event destinations](#supported-notification-destinations "#supported-notification-destinations")
- [Supported event types for SQS, SNS, and Lambda](#supported-notification-event-types "#supported-notification-event-types")
- [Supported event types for Amazon EventBridge](#supported-notification-event-types-eventbridge "#supported-notification-event-types-eventbridge")
- [Event ordering and duplicate events](#event-ordering-and-duplicate-events "#event-ordering-and-duplicate-events")

## Supported event destinations

Amazon S3 can send event notification messages to the following destinations.

- Amazon Simple Notification Service (Amazon SNS) topics
- Amazon Simple Queue Service (Amazon SQS) queues
- AWS Lambda
- Amazon EventBridge

However, only one destination type can be specified for each event notification.

###### Note

You must grant Amazon S3 permissions to post messages to an Amazon SNS topic or an Amazon SQS
queue. You must also grant Amazon S3 permission to invoke an AWS Lambda function on your
behalf. For instructions on how to grant these permissions, see [Granting permissions to publish event notification messages to a destination](grant-destinations-permissions-to-s3.md "grant-destinations-permissions-to-s3.md").

### Amazon SNS topic

Amazon SNS is a flexible, fully managed push messaging service. You can use this
service to push messages to mobile devices or distributed services. With
SNS, you can publish a message once, and deliver it one or more times.
Currently, Standard SNS is only allowed as an S3 event notification destination, whereas
SNS FIFO is not allowed.

Amazon SNS both coordinates and manages sending and delivering messages to
subscribing endpoints or clients. You can use the Amazon SNS console to create an
Amazon SNS topic that your notifications can be sent to.

The topic must be in the same AWS Region as your Amazon S3 bucket. For
instructions on how to create an Amazon SNS topic, see [Getting started with
Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the _Amazon Simple Notification Service Developer Guide_ and the [Amazon SNS FAQ](https://aws.amazon.com/sns/faqs/ "https://aws.amazon.com/sns/faqs/").

Before you can use the Amazon SNS topic that you created as an event notification
destination, you need the following:

- The Amazon Resource Name (ARN) for the Amazon SNS topic
- A valid Amazon SNS topic subscription. With it, topic subscribers are
  notified when a message is published to your Amazon SNS topic.

### Amazon SQS queue

Amazon SQS offers reliable and scalable hosted queues for storing messages as they
travel between computers. You can use Amazon SQS to transmit any volume of data
without requiring other services to be always available. You can use the Amazon SQS
console to create an Amazon SQS queue that your notifications can be sent to.

The Amazon SQS queue must be in the same AWS Region as your Amazon S3 bucket. For
instructions on how to create an Amazon SQS queue, see [What is
Amazon Simple Queue Service](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md") and [Getting started with Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.md") in the
_Amazon Simple Queue Service Developer Guide_.

Before you can use the Amazon SQS queue as an event notification destination, you
need the following:

- The Amazon Resource Name (ARN) for the Amazon SQS queue

###### Note

Amazon Simple Queue Service FIFO (First-In-First-Out) queues aren't supported as an Amazon S3 event
notification destination. To send a notification for an Amazon S3 event to an Amazon SQS
FIFO queue, you can use Amazon EventBridge. For more information, see [Enabling Amazon EventBridge](enable-event-notifications-eventbridge.md "enable-event-notifications-eventbridge.md").

### Lambda function

You can use AWS Lambda to extend other AWS services with custom logic, or
create your own backend that operates at AWS scale, performance, and security.
With Lambda, you can create discrete, event-driven applications that run only
when needed. You can also use it to scale these applications automatically from
a few requests a day to thousands a second.

Lambda can run custom code in response to Amazon S3 bucket events. You upload your
custom code to Lambda and create what's called a Lambda function. When Amazon S3
detects an event of a specific type, it can publish the event to AWS Lambda and
invoke your function in Lambda. In response, Lambda runs your function. One event
type it might detect, for example, is an object created event.

You can use the AWS Lambda console to create a Lambda function that uses the AWS
infrastructure to run the code on your behalf. The Lambda function must be in the
same Region as your S3 bucket. You must also have the name or the ARN of a Lambda
function to set up the Lambda function as an event notification
destination.

###### Warning

If your notification writes to the same bucket that triggers the notification, it could cause an execution loop. For example, if the bucket triggers a Lambda function each time an object is uploaded, and the function uploads an object to the bucket, then the function indirectly triggers itself. To avoid this, use two buckets, or configure the trigger to only apply to a prefix used for incoming objects.

For more information and an example of using Amazon S3 notifications with
AWS Lambda, see [Using AWS Lambda with
Amazon S3](../../../lambda/latest/dg/with-s3.md "../../../lambda/latest/dg/with-s3.md") in the _AWS Lambda Developer Guide_.

### Amazon EventBridge

Amazon EventBridge is a serverless event bus, which receives events from AWS services.
You can set up rules to match events and deliver them to targets, such as an
AWS service or an HTTP endpoint. For more information, see [What is EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") in the
_Amazon EventBridge User Guide_.

Unlike other destinations, you can either enable or disable events to be
delivered to EventBridge for a bucket. If you enable delivery, all events are sent to
EventBridge. Moreover, you can use EventBridge rules to route events to additional
targets.

## Supported event types for SQS, SNS, and Lambda

Amazon S3 can publish events of the following types. You specify these event types in
the notification configuration.

| Event types                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `s3:TestEvent`                                                                                                                                                                                               | When a notification is enabled, Amazon S3 publishes a test<br>notification. This is to ensure that the topic exists and that<br>the bucket owner has permission to publish the specified<br>topic.<br>If enabling the notification fails, you don't receive a test<br>notification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `s3:ObjectCreated:*`<br>`s3:ObjectCreated:Put`<br>`s3:ObjectCreated:Post`<br>`s3:ObjectCreated:Copy`<br>`s3:ObjectCreated:CompleteMultipartUpload`                                                           | Amazon S3 API operations such as `PUT`,<br>`POST`, and `COPY` can create an<br>object. With these event types, you can enable notifications<br>when an object is created using a specific API operation.<br>Alternatively, you can use the `s3:ObjectCreated:*`<br>event type to request notification regardless of the API that<br>was used to create an object.<br>`s3:ObjectCreated:CompleteMultipartUpload` includes<br>objects that are created using [UploadPartCopy](../API/API_UploadPartCopy.md "../API/API_UploadPartCopy.md") for Copy<br>operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `s3:ObjectRemoved:*`<br>`s3:ObjectRemoved:Delete`<br>`s3:ObjectRemoved:DeleteMarkerCreated`                                                                                                                  | By using the `ObjectRemoved` event types,<br>you can enable notification when an object or a batch of objects<br>is removed from a bucket.<br>You can request notification when an object is deleted or a<br>versioned object is permanently deleted by using the<br>`s3:ObjectRemoved:Delete` event type.<br>Alternatively, you can request notification when a delete marker<br>is created for a versioned object using<br>`s3:ObjectRemoved:DeleteMarkerCreated`. For<br>instructions on how to delete versioned objects, see [Deleting object versions from a versioning-enabled bucket](DeletingObjectVersions.md "DeletingObjectVersions.md"). You can also use a<br>wildcard `s3:ObjectRemoved:*` to request notification<br>anytime an object is deleted.<br>These event notifications don't alert you for automatic<br>deletes from lifecycle configurations or from failed<br>operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `s3:ObjectRestore:*`<br>`s3:ObjectRestore:Post`<br>`s3:ObjectRestore:Completed`<br>`s3:ObjectRestore:Delete`                                                                                                 | By using the `ObjectRestore` event types,<br>you can receive notifications for event initiation and<br>completion when restoring objects from the<br>S3 Glacier Flexible Retrieval storage class,<br>S3 Glacier Deep Archive storage class,<br>S3 Intelligent-Tiering Archive Access tier, and<br>S3 Intelligent-Tiering Deep Archive Access tier. You can also<br>receive notifications for when the restored copy of an object<br>expires.<br>The `s3:ObjectRestore:Post` event type notifies you<br>of object restoration initiation. The<br>`s3:ObjectRestore:Completed` event type notifies<br>you of restoration completion. The<br>`s3:ObjectRestore:Delete` event type notifies you<br>when the temporary copy of a restored object expires.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `s3:ReducedRedundancyLostObject`                                                                                                                                                                             | You receive this notification event when Amazon S3 detects that an<br>object of the RRS storage class is lost.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `s3:Replication:*`<br>`s3:Replication:OperationFailedReplication`<br>`s3:Replication:OperationMissedThreshold`<br>`s3:Replication:OperationReplicatedAfterThreshold`<br>`s3:Replication:OperationNotTracked` | By using the `Replication` event types, you can<br>receive notifications for replication configurations that have<br>S3 Replication metrics or S3 Replication Time Control (S3 RTC) enabled. You can monitor the<br>minute-by-minute progress of replication events by tracking<br>bytes pending, operations pending, and replication latency. For<br>information about replication metrics, see [Monitoring replication with metrics, event notifications, and statuses](replication-metrics.md "replication-metrics.md").<br>• The<br>`s3:Replication:OperationFailedReplication`<br>event type notifies you when an object that was eligible<br>for replication failed to replicate.<br>• The<br>`s3:Replication:OperationMissedThreshold`<br>event type notifies you when an object that was eligible<br>for replication that uses S3 RTC exceeds the 15-minute<br>threshold for replication.<br>• The<br>`s3:Replication:OperationReplicatedAfterThreshold`<br>event type notifies you when an object that was eligible<br>for replication that uses S3 RTC replicates after the<br>15-minute threshold.<br>• The `s3:Replication:OperationNotTracked`<br>event type notifies you when an object that was eligible<br>for live replication (either Same-Region Replication<br>[SRR] or Cross-Region Replication [CRR]) is no longer<br>being tracked by replication metrics. |
| `s3:LifecycleExpiration:*`<br>`s3:LifecycleExpiration:Delete`<br>`s3:LifecycleExpiration:DeleteMarkerCreated`                                                                                                | By using the `LifecycleExpiration` event<br>types, you can receive a notification when Amazon S3 deletes an object based<br>on your S3 Lifecycle configuration.<br>The `s3:LifecycleExpiration:Delete` event type<br>notifies you when an object in an unversioned bucket is deleted.<br>It also notifies you when an object version is permanently<br>deleted by an S3 Lifecycle configuration. The<br>`s3:LifecycleExpiration:DeleteMarkerCreated`<br>event type notifies you when S3 Lifecycle creates a delete marker<br>when a current version of an object in versioned bucket is<br>deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `s3:LifecycleTransition`                                                                                                                                                                                     | You receive this notification event when an object is<br>transitioned to another Amazon S3 storage class by an S3 Lifecycle<br>configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `s3:IntelligentTiering`                                                                                                                                                                                      | You receive this notification event when an object within the<br>S3 Intelligent-Tiering storage class moved to the Archive Access<br>tier or Deep Archive Access tier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `s3:ObjectTagging:*`<br>`s3:ObjectTagging:Put`<br>`s3:ObjectTagging:Delete`                                                                                                                                  | By using the `ObjectTagging` event types,<br>you can enable notification when an object tag is added or<br>deleted from an object.<br>The `s3:ObjectTagging:Put`<br>event type notifies you when a tag is PUT on an object or<br>an existing tag is updated. The `s3:ObjectTagging:Delete`<br>event type notifies you when a tag is removed from an object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `s3:ObjectAcl:Put`                                                                                                                                                                                           | You receive this notification event when an ACL is PUT on an<br>object or when an existing ACL is changed. An event is not generated<br>when a request results in no change to an object’s ACL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Supported event types for Amazon EventBridge

For a list of event types Amazon S3 will send to Amazon EventBridge, see [Using EventBridge](EventBridge.md "EventBridge.md").

## Event ordering and duplicate events

Amazon S3 Event Notifications is designed to deliver notifications at least once, but
they aren’t guaranteed to arrive in the same order that the events occurred. On rare
occasions, Amazon S3’s retry mechanism might cause duplicate S3 Event Notifications for
the same object event. For more about handling duplicate or out of order events, see
[Manage event ordering and duplicate events with Amazon S3 Event
Notifications](https://aws.amazon.com/blogs/storage/manage-event-ordering-and-duplicate-events-with-amazon-s3-event-notifications/ "https://aws.amazon.com/blogs/storage/manage-event-ordering-and-duplicate-events-with-amazon-s3-event-notifications/") on the _AWS Storage
Blog_.
