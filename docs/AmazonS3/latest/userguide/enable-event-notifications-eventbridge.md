# Enabling Amazon EventBridge

You can enable Amazon EventBridge by using the S3 console, AWS Command Line Interface (AWS CLI), or Amazon S3 REST API. 

###### Note

After you enable EventBridge, it takes around five minutes for the
 changes to take effect.

###### To enable EventBridge event delivery in the S3 console.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the
 bucket that you want to enable events for.
4. Choose **Properties**.
5. Navigate to the **Event Notifications** section and
 find the **Amazon EventBridge** subsection. Choose
 **Edit**.
6. Under **Send notifications to Amazon EventBridge for all events in this
 bucket** choose **On**.
The following example creates a bucket notification configuration for bucket
 ``amzn-s3-demo-bucket1`` with Amazon EventBridge
 enabled.


```
aws s3api put-bucket-notification-configuration --bucket `amzn-s3-demo-bucket1` --notification-configuration='{ "EventBridgeConfiguration": {} }'
```
You can programmatically enable Amazon EventBridge on a bucket by calling the Amazon S3 REST API. For
 more information, see [PutBucketNotificationConfiguration](../API/API_PutBucketNotificationConfiguration.md "../API/API_PutBucketNotificationConfiguration.md") in the
 *Amazon Simple Storage Service API Reference*.

The following example shows the XML used to create a bucket notification
 configuration with Amazon EventBridge enabled.


```
<NotificationConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <EventBridgeConfiguration>
  </EventBridgeConfiguration>
</NotificationConfiguration>
```

## Creating EventBridge rules


Once enabled you can create Amazon EventBridge rules for certain tasks. For example, you can
 send email notifications when an object is created. For a full tutorial, see [Tutorial: Send a
 notification when an Amazon S3 object is created](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-s3-object-created-tutorial.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-s3-object-created-tutorial.html") in the
 *Amazon EventBridge User Guide*.
