# Configuring S3 Lifecycle event

notifications

To receive notice when Amazon S3 deletes an object or transitions it to another Amazon S3 storage
class as the result of following an S3 Lifecycle rule, you can set up an Amazon S3 event
notification.

You can receive notifications for the following S3 Lifecycle events:

- **Transition events** – By using the
  `s3:LifecycleTransition` event type, you can receive notification
  when an object is transitioned from one Amazon S3 storage class to another by an
  S3 Lifecycle configuration.
- **Expiration (delete) events** – By using the
  `LifecycleExpiration` event types, you can receive notifications
  whenever Amazon S3 deletes an object based on your S3 Lifecycle configuration.

There are two expiration event types:

    + The `s3:LifecycleExpiration:Delete` event type notifies you
     when an object in an unversioned bucket is deleted.
     `s3:LifecycleExpiration:Delete` also notifies you when an
     object version is permanently deleted by an S3 Lifecycle
     configuration.
    + The `s3:LifecycleExpiration:DeleteMarkerCreated` event type
     notifies you when S3 Lifecycle creates a delete marker after a current
     version of an object in a versioned bucket is deleted. S3 Lifecycle sets the delete marker's creation time to
     00:00 UTC (midnight) of the current day. This creation time might differ from the event time
     in the `s3:LifecycleExpiration:DeleteMarkerCreated` notification that S3
     sends. For more information,
     see [Deleting object versions from a
     versioning-enabled bucket](DeletingObjectVersions.md "DeletingObjectVersions.md").

Amazon S3 can publish event notifications to an Amazon Simple Notification Service (Amazon SNS) topic, an Amazon Simple Queue Service (Amazon SQS)
queue, or an AWS Lambda function. For more information, see [Amazon S3 Event Notifications](EventNotifications.md "EventNotifications.md").

For instructions on how to configure Amazon S3 Event Notifications, see [Enabling event notifications by using
Amazon SQS, Amazon SNS, and AWS Lambda](how-to-enable-disable-notification-intro.md "how-to-enable-disable-notification-intro.md").

The following is an example of a message that Amazon S3 sends to publish an
`s3:LifecycleExpiration:Delete` event. For more information, see [Event message structure](notification-content-structure.md "notification-content-structure.md").

```
{
   "Records":[
      {
         "eventVersion":"2.3",
         "eventSource":"aws:s3",
         "awsRegion":"us-west-2",
         "eventTime":"1970-01-01T00:00:00.000Z",
         "eventName":"LifecycleExpiration:Delete",
         "userIdentity":{
            "principalId":"s3.amazonaws.com"
         },
         "requestParameters":{
            "sourceIPAddress":"s3.amazonaws.com"
         },
         "responseElements":{
            "x-amz-request-id":"C3D13FE58DE4C810",
            "x-amz-id-2":"FMyUVURIY8/IgAtTv8xRjskZQpcIZ9KG4V5Wp6S7S/JRWeUWerMUE5JgHvANOjpD"
         },
         "s3":{
            "s3SchemaVersion":"1.0",
            "configurationId":"testConfigRule",
            "bucket":{
               "name":"`amzn-s3-demo-bucket`",
               "ownerIdentity":{
                  "principalId":"A3NL1KOZZKExample"
               },
               "arn":"arn:aws:s3:::`amzn-s3-demo-bucket`"
            },
            "object":{
               "key":"expiration/delete",
               "sequencer":"0055AED6DCD90281E5",
            }
         }
      }
   ]
}

```

Messages that Amazon S3 sends to publish an `s3:LifecycleTransition` event also
include the following information:

```
"lifecycleEventData":{
    "transitionEventData": {
        "destinationStorageClass": `the destination storage class for the object`
    }
}
```
