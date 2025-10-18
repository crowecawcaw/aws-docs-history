# Configuring Amazon SNS notifications for CloudTrail


 You can be notified when CloudTrail publishes new log files to your Amazon S3 bucket. You manage
 notifications using Amazon Simple Notification Service (Amazon SNS).

Notifications are optional. If you want notifications, you configure CloudTrail to send update
 information to an Amazon SNS topic whenever a new log file has been sent. To receive these
 notifications, you can use Amazon SNS to subscribe to the topic. As a subscriber you can get
 updates sent to a Amazon Simple Queue Service (Amazon SQS) queue, which enables you to handle these notifications
 programmatically. 
 

###### Topics

* [Configuring CloudTrail to send notifications](#configure-cloudtrail-to-send-notifications "#configure-cloudtrail-to-send-notifications")

## Configuring CloudTrail to send notifications


On the CloudTrail console, you can configure a trail to use an Amazon SNS topic by enabling
 the **SNS notification delivery** option when you [create](cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console") 
 or [update](cloudtrail-update-a-trail-console.md "cloudtrail-update-a-trail-console.md") a trail. If you choose to use a new topic, CloudTrail creates the
 Amazon SNS topic for you and attaches an appropriate policy, so that CloudTrail has permission to publish to that topic.


With the AWS CLI, you can [create](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/create-trail.html "https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/create-trail.html") or [update](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/update-trail.html "https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/update-trail.html") 
 a trail to use an Amazon SNS topic by specifying a value for the `--sns-topic-name` parameter. You can specify the name or the ARN for the Amazon SNS topic.


When you create an SNS topic name, the name must meet the following requirements:



* Between 1 and 256 characters long
* Contain uppercase and lowercase ASCII letters, numbers, underscores, or hyphens

When you configure notifications for a multi-Region trail, notifications
 from all Regions are sent to the Amazon SNS topic that you specify. If you have one or more
 Region-specific trails, you must create a separate topic for each Region and subscribe to
 each individually. 


To receive notifications, subscribe to the Amazon SNS topic or topics that CloudTrail uses. You do
 this with the Amazon SNS console or Amazon SNS CLI commands. For more information, see [Subscribing to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html "https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html") in the
 *Amazon Simple Notification Service Developer Guide*. 


###### Note

CloudTrail sends a notification when log files are written to the Amazon S3 bucket. An active
 account can generate a large number of notifications. If you subscribe with email or
 SMS, you can receive a large volume of messages. We recommend that you subscribe using
 Amazon Simple Queue Service (Amazon SQS), which lets you handle notifications programmatically. For more
 information, see [Subscribing an Amazon SQS queue to an Amazon SNS topic (console)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-subscribe-queue-sns-topic.html "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-subscribe-queue-sns-topic.html") in the *Amazon Simple Queue Service Developer Guide*. 


The Amazon SNS notification consists of a JSON object that includes a `Message`
 field. The `Message` field lists the full path to the log file, as shown in the
 following example: 



```
{
    "s3Bucket": "amzn-s3-demo-bucket","s3ObjectKey": ["AWSLogs/123456789012/CloudTrail/us-east-2/2013/12/13/123456789012_CloudTrail_us-west-2_20131213T1920Z_LnPgDQnpkSKEsppV.json.gz"]
}
```

If multiple log files are delivered to your Amazon S3 bucket, a notification may contain
 multiple logs, as shown in the following example:



```
{
    "s3Bucket": "amzn-s3-demo-bucket",
    "s3ObjectKey": [
        "AWSLogs/123456789012/CloudTrail/us-east-2/2016/08/11/123456789012_CloudTrail_us-east-2_20160811T2215Z_kpaMYavMQA9Ahp7L.json.gz",
        "AWSLogs/123456789012/CloudTrail/us-east-2/2016/08/11/123456789012_CloudTrail_us-east-2_20160811T2210Z_zqDkyQv3TK8ZdLr0.json.gz",
        "AWSLogs/123456789012/CloudTrail/us-east-2/2016/08/11/123456789012_CloudTrail_us-east-2_20160811T2205Z_jaMVRa6JfdLCJYHP.json.gz"
    ]
}
```

If you choose to receive notifications by email, the body of the email consists of the
 content of the `Message` field. For information about the JSON structure,
 see [Fanout to Amazon SQS queues](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html "https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html") in the *Amazon Simple Notification Service Developer Guide*. Only the `Message`
 field shows CloudTrail information. The other fields contain information from the Amazon SNS service. 


If you create a trail with the CloudTrail API, you can specify an existing Amazon SNS topic that you
 want CloudTrail to send notifications to with the [`CreateTrail`](../APIReference/API_CreateTrail.md "../APIReference/API_CreateTrail.md") or [`UpdateTrail`](../APIReference/API_UpdateTrail.md "../APIReference/API_UpdateTrail.md") operations. You must make sure that the topic
 exists and that it has permissions that allow CloudTrail to send notifications to it. See [Amazon SNS topic policy for CloudTrail](cloudtrail-permissions-for-sns-notifications.md "cloudtrail-permissions-for-sns-notifications.md"). 


### Additional resources


For more information about Amazon SNS topics and about subscribing to them, see the [*Amazon Simple Notification Service Developer Guide*](https://docs.aws.amazon.com/sns/latest/dg/ "https://docs.aws.amazon.com/sns/latest/dg/").
