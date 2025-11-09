# Set up notifications in Kinesis Video Streams

When a media fragment is available for consumption, Kinesis Video Streams notifies customers using
Amazon Simple Notification Service (Amazon SNS) notifications.

###### Note

Amazon Kinesis Video Streams uses Amazon SNS Standard Topics for the communication. FIFO topics aren't currently supported.

The following topics explain how to get started with notifications.

###### Topics

- [Manage notification configurations](#manage-configurations "#manage-configurations")
- [About producer MKV tags](#producer-mkv-tags "#producer-mkv-tags")
- [Amazon SNS messages](#sns-messages "#sns-messages")
- [Cross-account Amazon SNS notification publishing](#cross-account-sns "#cross-account-sns")

## Manage notification configurations

To manage notification configurations, use `UpdateNotificationConfiguration` and `DescribeNotificationConfiguration`. See below for more information.

### UpdateNotificationConfiguration

Use this API operation to update the notification information for a stream. For more
information about the `UpdateNotificationConfiguration` feature, see [UpdateNotificationConfiguration](API_UpdateNotificationConfiguration.md "API_UpdateNotificationConfiguration.md") in the
_Amazon Kinesis Video Streams Developer Guide_.

###### Note

It takes at least one minute to initiate the notification after updating the notification
configuration. Wait at least one minute before invoking `PutMedia` after the update call.

### DescribeNotificationConfiguration

Use this API to describe a notification configuration attached to a stream. For more
information about the `DescribeNotificationConfiguration` feature, see [DescribeNotificationConfiguration](API_DescribeNotificationConfiguration.md "API_DescribeNotificationConfiguration.md") in the
_Amazon Kinesis Video Streams Developer Guide_.

## About producer MKV tags

You can use the Kinesis Video Streams producer SDK to tag specific fragments of interest by exposing an API operation in
the SDK. See a sample of how this works [in this section of code](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/samples/kvs_gstreamer_sample.cpp#L404 "https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/samples/kvs_gstreamer_sample.cpp#L404"). Upon calling this API, the SDK will add a set of predefined MKV tags along with the fragment
data. Kinesis Video Streams will recognize these special MKV tags and initiate notifications for the tagged fragments.

Any fragment metadata provided along with the Notification MKV tags will be published
as part of the Amazon SNS topic payload.

### Syntax for producer MKV tags

```

|+ Tags
| + Tag
|  // MANDATORY: Predefined MKV tag to trigger the notification for the fragment
|  + Simple
|   + Name: AWS_KINESISVIDEO_NOTIFICATION
|   + String
| // OPTIONAL: Key value pairs that will be sent as part of the Notification payload
|  + Simple
|   + Name: `CUSTOM_KEY_1` // Max 128 bytes
|   + String:`CUSTOM_VALUE_1` // Max 256 bytes
|  + Simple
|   + Name: `CUSTOM_KEY_2` // Max 128 bytes
|   + String: `CUSTOM_VALUE_2` // Max 256 bytes

```

### MKV tag limits

The following table lists the limitations associated with the metadata tags. If the
metadata tag limit is adjustable, you can request an increase through your account
manager.

| Limit                           | Max value | Adjustable |
| ------------------------------- | --------- | ---------- |
| Optional metadata key length    | 128       | No         |
| Optional metadata value length  | 256       | No         |
| Max number of optional metadata | 10        | Yes        |

## Amazon SNS messages

This topic contains more information about Amazon SNS messages and topic payloads.

###### Topics

- [Amazon SNS topic payload](#topic-payload "#topic-payload")
- [View your Amazon SNS messages](#viewing-messages "#viewing-messages")

### Amazon SNS topic payload

Any notification initiated through the previous workflow will deliver the Amazon SNS
topic payload, as shown in the following example. This example is an Amazon SNS message
that occurs after consuming notification data from an Amazon Simple Queue Service (Amazon SQS)
queue.

```
{
"Type" : "Notification",
"MessageId" : `Message ID`,
"TopicArn" : `SNS ARN`,
"Subject" : "Kinesis Video Streams Notification",
"Message" : "{\"StreamArn\":\`Stream Arn`,\"FragmentNumber\":\`Fragment Number`,\"FragmentStartProducerTimestamp\":`FragmentStartProducerTimestamp`,
                \"FragmentStartServerTimestamp\":`FragmentStartServerTimestamp`,\"NotificationType\":\"PERSISTED\",\"NotificationPayload\":{\ `CUSTOM_KEY_1`:\`CUSTOM_VALUE_1`,
                \`CUSTOM_KEY_2`:\`CUSTOM_VALUE_2`}}",
"Timestamp" : "2022-04-25T18:36:29.194Z",
"SignatureVersion" : `Signature Version`,
"Signature" : `Signature`,
"SigningCertURL" : `Signing Cert URL`,
"UnsubscribeURL" : `Unsubscribe URL`
}
```

```
Subject: "Kinesis Video Streams Notification"
Message:
{
    "StreamArn":`Stream Arn`,
    "FragmentNumber":`Fragment Number`,
    "FragmentStartProducerTimestamp":`Fragment Start Producer Timestamp`,
    "FragmentStartServerTimestamp":`Fragment Start Server Timestamp`,
    "NotificationType":"PERSISTED",
    "NotificationPayload":{
        `CUSTOM_KEY_1`:`CUSTOM_VALUE_1`,
        `CUSTOM_KEY_2`:`CUSTOM_VALUE_2`
    }
}
```

### View your Amazon SNS messages

You cannot read messages directly from an Amazon SNS topic because there's no API for doing so. To view the
messages, subscribe an SQS queue to the SNS topic, or choose any other [Amazon SNS supported
destination](../../../sns/latest/dg/sns-event-destinations.md "../../../sns/latest/dg/sns-event-destinations.md"). However, the most efficient option for viewing messages is to use Amazon SQS.

###### To view your Amazon SNS messages using Amazon SQS

1. Create an [Amazon SQS queue](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.md").
2. From the AWS Management Console, open the Amazon SNS topic set as a destination under
   `NotificationConfiguration`.
3. Choose **Create Subscription**, and then
   choose the Amazon SQS queue created in the first step.
4. Run a `PutMedia` session with the Notification configuration
   enabled and with the Notification MKV tags added to the fragments.
5. Choose the Amazon SQS queue in the Amazon SQS console, and then select **Send and receive messages** for the Amazon SQS
   queue.
6. Poll for messages. This command should show all notifications generated by
   the `PutMedia` session. For information about polling, see [Amazon SQS short and long polling.](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.md")

## Cross-account Amazon SNS notification publishing

To publish Amazon SNS notifications to a topic in a different AWS account, you need to configure both identity-based and resource-based policies. This setup allows Kinesis Video Streams to publish notifications from one account to an Amazon SNS topic in another account.

### Identity-based policy configuration

The IAM role or user that calls the `PutMedia` API must have `sns:Publish` permissions for the cross-account Amazon SNS topic. Add the following policy statement to the identity-based policy:

### Resource-based policy configuration

The Amazon SNS topic in the destination account must have a resource-based access policy that allows the source account to publish messages. Configure the Amazon SNS topic access policy as follows:

Replace `<kvs_streams_account_id>` with the AWS account ID where your Kinesis Video Streams streams are located, and `<sns_topic_arn>` with the ARN of your Amazon SNS topic.

### Requirements and considerations

- Both the identity-based policy (in the source account) and the resource-based policy (in the destination account) must be configured for cross-account publishing to work.
- The IAM role used for `PutMedia` operations must include `sns:Publish` permissions, even when using IoT certificates with role aliases.
