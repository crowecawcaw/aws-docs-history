# Receiving Amazon SNS notifications for AMI products on AWS Marketplace

To receive notifications about changes to customer subscriptions for your products, you can
subscribe to the Amazon Simple Notification Service (Amazon SNS) topics for AWS Marketplace provided to you during product creation. For
example, you can know when customers accept a private offer. [Amazon SNS topic:
aws-mp-subscription-notification](#ami-sns-subscription-message-body "#ami-sns-subscription-message-body") is an Amazon SNS topic that is available for AMI products. This topic notifies you when a buyer
subscribes or unsubscribes to a product. This notification is available for hourly pricing
models, including hourly and hourly with annual. For more information, see the following
sections.

###### Note

During the product creation process, an Amazon SNS topic is created for your product. To
subscribe to notifications, you need the Amazon Resource Name (ARN) of the Amazon SNS topic (for
example,
`arn:aws:sns:us-east-1:123456789012:aws-mp-subscription-notification-PRODUCTCODE`).
The ARN is not available in the seller portal for server products. Contact the [AWS Marketplace operations
team](https://aws.amazon.com/marketplace/management/contact-us "https://aws.amazon.com/marketplace/management/contact-us") to request the ARN.

###### Topics

- [Amazon SNS topic:
  aws-mp-subscription-notification](#ami-sns-subscription-message-body "#ami-sns-subscription-message-body")
- [Subscribing an Amazon SQS queue to the
  Amazon SNS topic](#subscribing-an-sqs-queue-to-an-sns-topic "#subscribing-an-sqs-queue-to-an-sns-topic")

## Amazon SNS topic:

aws-mp-subscription-notification

Each message in the `aws-mp-subscription-notification` topic for the
`subscribe-success` and `subscribe-fail` action has the following
format.

```
{
    "action": "`action-name`",
    "customer-identifier": " `X01EXAMPLEX`",
    "product-code": "`n0123EXAMPLEXXXXXXXXXXXX`",
    "offer-identifier": "`offer-abcexample123`"
}
```

The `<action-name>` will vary depending on the notification.
Possible actions are:

- `subscribe-success`
- `subscribe-fail`
- `unsubscribe-pending`
- `unsubscribe-success`

The `offer-identifier` is included in the notification only when the action is
`subscribe-success` or `subscribe-fail`. It isn't included in notifications when the action is
`unsubscribe-pending` or `unsubscribe-success`.
For offers created before January 2024, this identifier is included
in the notification only for private offers. For offers created in January 2024 and later, this
identifier is included in notifications for all offers, including both private offers and public offers.

For information on offer types, see the response from [DescribeEntity API](../APIReference/work-with-private-offers.md#describe-entity "../APIReference/work-with-private-offers.md#describe-entity") or the offer visibility of an agreement in
the [Agreements renewals dashboard](agreements-renewals-dashboard.md "agreements-renewals-dashboard.md").

###### Note

For [DescribeEntity API](../APIReference/work-with-private-offers.md#describe-entity "../APIReference/work-with-private-offers.md#describe-entity"), if you find an AWS account in the
account targeting facet of targeting rule for that offer, it is a private offer. If there is
not an AWS account in the account targeting facet of targeting rule for that offer, it is
a public offer.

## Subscribing an Amazon SQS queue to the

Amazon SNS topic

We recommend subscribing an Amazon SQS queue to the provided SNS topics. For detailed
instructions on creating an SQS queue and subscribing the queue to a topic, see [Subscribing
an Amazon SQS queue to an Amazon SNS topic](../../../sns/latest/dg/subscribe-sqs-queue-to-sns-topic.md "../../../sns/latest/dg/subscribe-sqs-queue-to-sns-topic.md") in the _Amazon Simple Notification Service Developer Guide_.

###### Note

You can only subscribe to AWS Marketplace SNS topics from the AWS account used to sell the
products. However, you can forward the messages to a different account. For more
information, see [Sending Amazon SNS messages to
an Amazon SQS queue in a different account](../../../sns/latest/dg/sns-send-message-to-sqs-cross-account.md "../../../sns/latest/dg/sns-send-message-to-sqs-cross-account.md") in the _Amazon Simple Notification Service Developer
Guide_.

### Polling the SQS queue for

notifications

After you subscribe your SQS queue to an SNS topic, the messages are stored in SQS. You
must define a service that continually polls the queue, looks for messages, and handles them
accordingly.
