

# Subscribing a queue to an Amazon SNS topic using the Amazon SQS console
<a name="sqs-configure-subscribe-queue-sns-topic"></a>

You can subscribe one or more Amazon SQS queues to an Amazon SNS topic. When you publish a message to a topic, Amazon SNS sends the message to each subscribed queue. Amazon SQS manages the subscription and handles the required permissions. For more information about Amazon SNS, see [What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) in the *Amazon Simple Notification Service Developer Guide*.

When you subscribe an Amazon SQS queue to an Amazon SNS topic, Amazon SNS uses HTTPS to forward messages to Amazon SQS. For information about using Amazon SNS with encrypted Amazon SQS queues, see [Configure KMS permissions for AWS services](sqs-key-management.md#compatibility-with-aws-services).

**Important**  
Amazon SQS supports a maximum of 20 statements for each access policy. Subscribing to an Amazon SNS topic adds one such statement. Exceeding this amount will result in a failed topic subscription delivery.

**To subscribe a queue to an Amazon SNS topic (console)**

1. Open the Amazon SQS console at [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/).

1. In the navigation pane, choose **Queues**.

1. From the list of queues, choose the queue to subscribe to the Amazon SNS topic.

1. From **Actions**, choose **Subscribe to Amazon SNS topic**.

1. From the **Specify an Amazon SNS topic available for this queue** menu, choose the Amazon SNS topic for your queue. 

   If the SNS topic isn't listed, choose **Enter Amazon SNS topic ARN** and then enter the topic's Amazon Resource Name (ARN).

1. Choose **Save**. 

1. To verify the subscription, publish a message to the topic and view the message in the queue. For more information, see [Amazon SNS message publishing](https://docs.aws.amazon.com/sns/latest/dg/sns-publishing.html) in the *Amazon Simple Notification Service Developer Guide*.

## Cross-account subscriptions
<a name="cross-account-subscriptions"></a>

If your Amazon SQS queue and Amazon SNS topic are in different AWS accounts, additional permissions are required.

**Topic owner (Account A)**

Modify the Amazon SNS topic's access policy to allow the Amazon SQS queue's AWS account to subscribe. Example policy statement:

```
{
  "Effect": "Allow",
  "Principal": { "AWS": "arn:aws:iam::111122223333:root" },
  "Action": "sns:Subscribe",
  "Resource": "arn:aws:sns:us-east-1:123456789012:MyTopic"
}
```

This policy allows account `111122223333` to subscribe to `MyTopic`.

**Queue owner (Account B)**

Modify the Amazon SQS queue's access policy to allow the Amazon SNS topic to send messages. Example policy statement:

```
{
  "Effect": "Allow",
  "Principal": { "Service": "sns.amazonaws.com" },
  "Action": "sqs:SendMessage",
  "Resource": "arn:aws:sqs:us-east-1:111122223333:MyQueue",
  "Condition": {
    "ArnEquals": { "aws:SourceArn": "arn:aws:sns:us-east-1:123456789012:MyTopic" }
  }
}
```

This policy allows `MyTopic` to send messages to `MyQueue`.

## Cross-region subscriptions
<a name="cross-region-subscriptions"></a>

To subscribe to an Amazon SNS topic in a different AWS Region, ensure that:
+ The Amazon SNS topic's access policy allows cross-region subscriptions.
+ The Amazon SQS queue's access policy permits the Amazon SNS topic to send messages across regions.

For more information, [Sending Amazon SNS messages to an Amazon SQS queue or AWS Lambda function in a different Region](https://docs.aws.amazon.com/sns/latest/dg/sns-cross-region-delivery.html) in the *Amazon Simple Notification Service Developer Guide*.