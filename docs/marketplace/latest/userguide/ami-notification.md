

# Receiving Amazon SNS notifications for AMI products on AWS Marketplace
<a name="ami-notification"></a>

**Important**  
SNS notifications for AWS Marketplace AMI products are being replaced with Amazon EventBridge notifications. If you have existing AMI products integrated with SNS, they will continue to function. For more information, see [Managing AMI agreement events with Amazon EventBridge](ami-eventbridge-integration.md).

To receive notifications about changes to customer subscriptions for your products, you can subscribe to the Amazon Simple Notification Service (Amazon SNS) topics for AWS Marketplace provided to you during product creation. For example, you can know when customers accept a private offer. [Amazon SNS topic: aws-mp-subscription-notification](#ami-sns-subscription-message-body) is an Amazon SNS topic that is available for AMI products. This topic notifies you when a buyer subscribes or unsubscribes to a product. This notification is available for hourly pricing models, including hourly and hourly with annual. For more information, see the following sections.

**Note**  
During the product creation process, an Amazon SNS topic is created for your product. To subscribe to notifications, you need the Amazon Resource Name (ARN) of the Amazon SNS topic (for example, `arn:aws:sns:us-east-1:123456789012:aws-mp-subscription-notification-PRODUCTCODE`). The ARN is not available in the seller portal for server products. Contact the [AWS Marketplace operations team](https://aws.amazon.com/marketplace/management/contact-us) to request the ARN.

**Topics**
+ [Amazon SNS topic: aws-mp-subscription-notification](#ami-sns-subscription-message-body)
+ [Subscribing an Amazon SQS queue to the Amazon SNS topic](#subscribing-an-sqs-queue-to-an-sns-topic)

## Amazon SNS topic: aws-mp-subscription-notification
<a name="ami-sns-subscription-message-body"></a>

Each message in the `aws-mp-subscription-notification` topic for the `subscribe-success` and `subscribe-fail` action has the following format.

```
{
    "action": "{{action-name}}",
    "customer-identifier": " {{X01EXAMPLEX}}",
    "product-code": "{{n0123EXAMPLEXXXXXXXXXXXX}}",
    "offer-identifier": "{{offer-abcexample123}}"
}
```

The {{<action-name>}} will vary depending on the notification. Possible actions are:
+ `subscribe-success`
+ `subscribe-fail`
+ `unsubscribe-pending`
+ `unsubscribe-success`

The `offer-identifier` is included in the notification only when the action is `subscribe-success` or `subscribe-fail`. It isn't included in notifications when the action is `unsubscribe-pending` or `unsubscribe-success`. For offers created before January 2024, this identifier is included in the notification only for private offers. For offers created in January 2024 and later, this identifier is included in notifications for all offers, including both private offers and public offers.

For information on offer types, see the response from [DescribeEntity API](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-private-offers.html#describe-entity) or the offer visibility of an agreement in the [Agreements renewals dashboard](https://docs.aws.amazon.com/marketplace/latest/userguide/agreements-renewals-dashboard.html).

**Note**  
 For [DescribeEntity API](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-private-offers.html#describe-entity), if you find an AWS account in the account targeting facet of targeting rule for that offer, it is a private offer. If there is not an AWS account in the account targeting facet of targeting rule for that offer, it is a public offer.

## Subscribing an Amazon SQS queue to the Amazon SNS topic
<a name="subscribing-an-sqs-queue-to-an-sns-topic"></a>

We recommend subscribing an Amazon SQS queue to the provided SNS topics. For detailed instructions on creating an SQS queue and subscribing the queue to a topic, see [ Subscribing an Amazon SQS queue to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/subscribe-sqs-queue-to-sns-topic.html) in the *Amazon Simple Notification Service Developer Guide*.

**Note**  
You can only subscribe to AWS Marketplace SNS topics from the AWS account used to sell the products. However, you can forward the messages to a different account. For more information, see [Sending Amazon SNS messages to an Amazon SQS queue in a different account](https://docs.aws.amazon.com/sns/latest/dg/sns-send-message-to-sqs-cross-account.html) in the *Amazon Simple Notification Service Developer Guide*.

### Polling the SQS queue for notifications
<a name="polling-an-sqs-for-notifications"></a>

After you subscribe your SQS queue to an SNS topic, the messages are stored in SQS. You must define a service that continually polls the queue, looks for messages, and handles them accordingly.