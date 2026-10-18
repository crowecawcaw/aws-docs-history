

# Amazon SNS notifications for container products
<a name="container-notification"></a>

**Amazon SNS notifications aren't available to new sellers**  
If you registered your seller account after July 15, 2026, use Amazon EventBridge to receive events. If you registered on or before that date, you can continue to use Amazon SNS. For more information, see [Managing container agreement events with Amazon EventBridge](container-eventbridge-integration.md).

If you use Amazon SNS notifications, plan to migrate to EventBridge. New notifications are available only in EventBridge.

To receive notifications, you can subscribe to the Amazon Simple Notification Service (Amazon SNS) topics for AWS Marketplace provided to you during product creation. The topics provide notifications about changes to customers’ subscriptions for your products. For example, you can use these notifications to know when customers accept a private offer. 

**Note**  
During the product creation process, an Amazon SNS topic is created for your product. To subscribe to notifications, you need the Amazon Resource Name (ARN) of the Amazon SNS topic (for example, `arn:aws:sns:us-east-1:123456789012:aws-mp-subscription-notification-PRODUCTCODE`). The ARN is not available in the seller portal for server products. Contact the [AWS Marketplace operations team](https://aws.amazon.com/marketplace/management/contact-us) to request the ARN.

The following Amazon SNS topic is available for container products:
+ [Amazon SNS topic: `aws-mp-subscription-notification`](#container-sns-subscription-message-body) – This topic notifies you when a buyer subscribes or unsubscribes to a product. This is available for hourly pricing models, including hourly and hourly with long term.

## Amazon SNS topic: `aws-mp-subscription-notification`
<a name="container-sns-subscription-message-body"></a>

Each message in the `aws-mp-subscription-notification` topic has the following format.

```
{
    "action": "{{<action-name>}}",
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
<a name="subscribing-sqs-queue-to-sns-topic"></a>

We recommend subscribing an Amazon SQS queue to the provided SNS topics. For detailed instructions on creating an SQS queue and subscribing the queue to a topic, see [ Subscribing an Amazon SQS queue to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/subscribe-sqs-queue-to-sns-topic.html) in the *Amazon Simple Notification Service Developer Guide*.

**Note**  
You can only subscribe to AWS Marketplace SNS topics from the AWS account used to sell the products. However, you can forward the messages to a different account. For more information, see [Sending Amazon SNS messages to an Amazon SQS queue in a different account](https://docs.aws.amazon.com/sns/latest/dg/sns-send-message-to-sqs-cross-account.html) in the *Amazon Simple Notification Service Developer Guide*.

### Polling the SQS queue for notifications
<a name="polling-the-sqs-for-notifications"></a>

After you subscribe your SQS queue to an SNS topic, the messages are stored in SQS. You must define a service that continually polls the queue, looks for messages, and handles them accordingly.