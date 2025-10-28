# Subscribing a queue to an Amazon SNS

topic using the Amazon SQS console

You can subscribe one or more Amazon SQS queues to an Amazon SNS topic. When you publish
a message to a topic, Amazon SNS sends the message to each subscribed queue. Amazon SQS manages the
subscription and handles the required permissions. For more information about Amazon SNS, see [What is Amazon SNS?](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md") in the
_Amazon Simple Notification Service Developer Guide_.

When you subscribe an Amazon SQS queue to an Amazon SNS topic, Amazon SNS uses HTTPS to forward messages
to Amazon SQS. For information about using Amazon SNS with encrypted Amazon SQS queues, see [Configure KMS permissions
for AWS services](sqs-key-management.md#compatibility-with-aws-services "sqs-key-management.md#compatibility-with-aws-services").

###### Important

Amazon SQS supports a maximum of 20 statements for each access policy. Subscribing to an
Amazon SNS topic adds one such statement. Exceeding this amount will result in a failed topic
subscription delivery.

###### To subscribe a queue to an Amazon SNS topic (console)

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the navigation pane, choose **Queues**.
3. From the list of queues, choose the queue to subscribe to the Amazon SNS topic.
4. From **Actions**, choose **Subscribe to Amazon SNS
   topic**.
5. From the **Specify an Amazon SNS topic available for this queue**
   menu, choose the Amazon SNS topic for your queue.

If the SNS topic isn't listed, choose **Enter Amazon SNS topic ARN**
and then enter the topic's Amazon Resource Name (ARN). 6. Choose **Save**. 7. To verify the subscription, publish a message to the topic and view the message in
the queue. For more information, see [Amazon SNS message publishing](../../../sns/latest/dg/sns-publishing.md "../../../sns/latest/dg/sns-publishing.md") in the
_Amazon Simple Notification Service Developer Guide_.

## Cross-account subscriptions

If your Amazon SQS queue and Amazon SNS topic are in different AWS accounts, additional
permissions are required.

**Topic owner (Account A)**

Modify the Amazon SNS topic's access policy to allow the Amazon SQS queue's AWS account to
subscribe. Example policy statement:

```
{
  "Effect": "Allow",
  "Principal": { "AWS": "arn:aws:iam::111122223333:root" },
  "Action": "sns:Subscribe",
  "Resource": "arn:aws:sns:us-east-1:123456789012:MyTopic"
}
```

This policy allows account `111122223333` to subscribe to
`MyTopic`.

**Queue owner (Account B)**

Modify the Amazon SQS queue's access policy to allow the Amazon SNS topic to send messages.
Example policy statement:

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

This policy allows `MyTopic` to send messages to
`MyQueue`.

## Cross-region subscriptions

To subscribe to an Amazon SNS topic in a different AWS Region, ensure that:

- The Amazon SNS topic's access policy allows cross-region subscriptions.
- The Amazon SQS queue's access policy permits the Amazon SNS topic to send messages
  across regions.

For more information, [Sending
Amazon SNS messages to an Amazon SQS queue or AWS Lambda function in a different Region](../../../sns/latest/dg/sns-cross-region-delivery.md "../../../sns/latest/dg/sns-cross-region-delivery.md")
in the _Amazon Simple Notification Service Developer Guide_.
