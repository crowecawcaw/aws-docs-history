# Walkthrough: Configuring a
 bucket for notifications (SNS topic or SQS queue)

You can receive Amazon S3 notifications using Amazon Simple Notification Service (Amazon SNS) or Amazon Simple Queue Service (Amazon SQS). In
 this walkthrough, you add a notification configuration to your bucket using an Amazon SNS
 topic and an Amazon SQS queue.

###### Note

Amazon Simple Queue Service FIFO (First-In-First-Out) queues aren't supported as an Amazon S3 event
 notification destination. To send a notification for an Amazon S3 event to an Amazon SQS
 FIFO queue, you can use Amazon EventBridge. For more information, see [Enabling Amazon EventBridge](enable-event-notifications-eventbridge.md "enable-event-notifications-eventbridge.md").

###### Topics

* [Walkthrough summary](#notification-walkthrough-summary "#notification-walkthrough-summary")
* [Step 1: Create an Amazon SQS
 queue](#step1-create-sqs-queue-for-notification "#step1-create-sqs-queue-for-notification")
* [Step 2: Create an Amazon SNS
 topic](#step1-create-sns-topic-for-notification "#step1-create-sns-topic-for-notification")
* [Step 3: Add a notification configuration
 to your bucket](#step2-enable-notification "#step2-enable-notification")
* [Step 4: Test the setup](#notification-walkthrough-1-test "#notification-walkthrough-1-test")

## Walkthrough summary


This walkthrough helps you do the following:



* Publish events of the `s3:ObjectCreated:*` type to an Amazon SQS
 queue.
* Publish events of the `s3:ReducedRedundancyLostObject` type to
 an Amazon SNS topic.

For information about notification configuration, see [Using Amazon SQS, Amazon SNS, and Lambda](how-to-enable-disable-notification-intro.md "how-to-enable-disable-notification-intro.md").


You can do all these steps using the console, without writing any code. In
 addition, code examples using AWS SDKs for Java and .NET are also provided to help
 you add notification configurations programmatically.


The procedure includes the following steps:



1. Create an Amazon SQS queue.


Using the Amazon SQS console, create an SQS queue. You can access any messages
 Amazon S3 sends to the queue programmatically. But, for this walkthrough, you
 verify notification messages in the console. 


You attach an access policy to the queue to grant Amazon S3 permission to post
 messages.
2. Create an Amazon SNS topic.


Using the Amazon SNS console, create an SNS topic and subscribe to the topic.
 That way, any events posted to it are delivered to you. You specify
 email as the communications protocol. After you create a topic, Amazon SNS
 sends an email. You use the link in the email to confirm the topic
 subscription. 


You attach an access policy to the topic to grant Amazon S3 permission to post
 messages.
3. Add notification configuration to a bucket.

## Step 1: Create an Amazon SQS
 queue


Follow the steps to create and subscribe to an Amazon Simple Queue Service (Amazon SQS) queue.


1. Using the Amazon SQS console, create a queue. For instructions, see [Getting Started with
 Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html") in the *Amazon Simple Queue Service Developer Guide*.
2. Replace the access policy that's attached to the queue with the following
 policy.


	1. In the Amazon SQS console, in the **Queues** list, choose the queue name.
	2. On the **Access policy** tab, choose **Edit**.
	3. Replace the access policy that's attached to the queue. In it, provide
	 your Amazon SQS ARN, source bucket name, and bucket owner account
	 ID.
	
	
	
	JSON
	
	
	
	
	
	```
	`{
	 "Version":"2012-10-17", 
	 "Id": "example-ID",
	 "Statement": [
	 {
	 "Sid": "example-statement-ID",
	 "Effect": "Allow",
	 "Principal": {
	 "Service": "s3.amazonaws.com"
	 },
	 "Action": [
	 "SQS:SendMessage"
	 ],
	 "Resource": "`arn:aws:sqs:us-west-2:111122223333:s3-notification-queue`",
	 "Condition": {
	 "ArnLike": {
	 "aws:SourceArn": "arn:aws:s3:*:*:`awsexamplebucket1`"
	 },
	 "StringEquals": {
	 "aws:SourceAccount": "`bucket-owner-account-id`"
	 }
	 }
	 }
	 ]
	}`
	
	```
	4. Choose **Save**.
3. (Optional) If the Amazon SQS queue or the Amazon SNS topic is server-side encryption
 enabled with AWS Key Management Service (AWS KMS), add the following policy to the associated
 symmetric encryption customer managed key. 


You must add the policy to a customer managed key because you cannot modify the
 AWS managed key for Amazon SQS or Amazon SNS. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Id": "example-ID",
 "Statement": [
 {
 "Sid": "example-statement-ID",
 "Effect": "Allow",
 "Principal": {
 "Service": "s3.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```





For more information about using SSE for Amazon SQS and Amazon SNS with AWS KMS, see
 the following:




	* [Key
	 management](https://docs.aws.amazon.com/sns/latest/dg/sns-key-management.html "https://docs.aws.amazon.com/sns/latest/dg/sns-key-management.html") in the
	 *Amazon Simple Notification Service Developer Guide*.
	* [Key management](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.html "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.html") in the
	 *Amazon Simple Queue Service Developer Guide*.
4. Note the queue ARN. 


The SQS queue that you created is another resource in your AWS account.
 It has a unique Amazon Resource Name (ARN). You need this ARN in the
 next step. The ARN is of the following format:



```
arn:aws:sqs:`aws-region`:`account-id`:`queue-name`
```

## Step 2: Create an Amazon SNS
 topic


Follow the steps to create and subscribe to an Amazon SNS topic.


1. Using Amazon SNS console, create a topic. For instructions, see [Creating an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html "https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html") in
 the *Amazon Simple Notification Service Developer Guide*.
2. Subscribe to the topic. For this exercise, use email as the communications
 protocol. For instructions, see [Subscribing to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html "https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html") in the
 *Amazon Simple Notification Service Developer Guide*. 


You get an email requesting you to confirm your subscription to the topic.
 Confirm the subscription.
3. Replace the access policy attached to the topic with the following policy.
 In it, provide your SNS topic ARN, bucket name, and bucket owner's
 account ID.
4. Note the topic ARN.


The SNS topic you created is another resource in your AWS account, and
 it has a unique ARN. You will need this ARN in the next step. The ARN will
 be of the following format:



```
arn:aws:sns:`aws-region`:`account-id`:`topic-name`
```

## Step 3: Add a notification configuration
 to your bucket


You can enable bucket notifications either by using the Amazon S3 console or
 programmatically by using AWS SDKs. Choose any one of the options to configure
 notifications on your bucket. This section provides code examples using the AWS
 SDKs for Java and .NET.


### Option A: Enable
 notifications on a bucket using the console


Using the Amazon S3 console, add a notification configuration requesting Amazon S3 to do
 the following:



* Publish events of the **All object create
 events** type to your Amazon SQS queue.
* Publish events of the **Object in RRS
 lost** type to your Amazon SNS topic.

After you save the notification configuration, Amazon S3 posts a test message,
 which you get via email. 


For instructions, see [Enabling and configuring event notifications using the Amazon S3 console](enable-event-notifications.md "enable-event-notifications.md"). 


### Option B: Enable
 notifications on a bucket using the AWS SDKs



.NET
The following C# code example provides a complete code listing
 that adds a notification configuration to a bucket. You must
 update the code and provide your bucket name and SNS topic ARN.
 For
 information about setting up and running the code examples, see [Getting Started
 with the AWS SDK for .NET](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/net-dg-setup.html "https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/net-dg-setup.html") in the *AWS SDK for .NET Developer
 Guide*. 



```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class EnableNotificationsTest
    {
        private const string bucketName = "*** bucket name ***";
        private const string snsTopic = "*** SNS topic ARN ***";
        private const string sqsQueue = "*** SQS topic ARN ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USWest2;
        private static IAmazonS3 client;

        public static void Main()
        {
            client = new AmazonS3Client(bucketRegion);
            EnableNotificationAsync().Wait();
        }

        static async Task EnableNotificationAsync()
        {
            try
            {
               PutBucketNotificationRequest request = new PutBucketNotificationRequest
                {
                    BucketName = bucketName
                };

                TopicConfiguration c = new TopicConfiguration
                {
                    Events = new List<EventType> { EventType.ObjectCreatedCopy },
                    Topic = snsTopic
                };
                request.TopicConfigurations = new List<TopicConfiguration>();
                request.TopicConfigurations.Add(c);
                request.QueueConfigurations = new List<QueueConfiguration>();
                request.QueueConfigurations.Add(new QueueConfiguration()
                {
                    Events = new List<EventType> { EventType.ObjectCreatedPut },
                    Queue = sqsQueue
                });
                
                PutBucketNotificationResponse response = await client.PutBucketNotificationAsync(request);
            }
            catch (AmazonS3Exception e)
            {
                Console.WriteLine("Error encountered on server. Message:'{0}' ", e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unknown error encountered on server. Message:'{0}' ", e.Message);
            }
        }
    }
}

```


Java
For examples of how to configure bucket notifications with the AWS SDK for Java, see [Process S3 event notifications](../API/s3_example_s3_Scenario_ProcessS3EventNotification_section.md "../API/s3_example_s3_Scenario_ProcessS3EventNotification_section.md") in the *Amazon S3 API Reference*.




## Step 4: Test the setup


Now, you can test the setup by uploading an object to your bucket and verifying
 the event notification in the Amazon SQS console. For instructions, see [Receiving a Message](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.htmlReceiveMessage.html "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.htmlReceiveMessage.html") in the
 *Amazon Simple Queue Service Developer Guide "Getting Started" section*.
