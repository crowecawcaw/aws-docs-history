# Amazon SNS notifications for SaaS products

###### Important

SNS notifications for AWS Marketplace SaaS products are being replaced with Amazon EventBridge notifications. If you have existing SaaS products integrated with SNS, they will continue to function. New listings will eventually transition to using Amazon EventBridge instead of SNS. For more information, see [Managing SaaS subscription events with Amazon EventBridge](saas-eventbridge-integration.md "saas-eventbridge-integration.md").

To receive notifications, you subscribe to the Amazon Simple Notification Service (Amazon SNS) topics for AWS Marketplace provided to
you during product creation. The topics provide notifications about changes to customers’
subscriptions and contract entitlements for your products. This enables you to know when to
provide and revoke access for specific customers.

###### Note

During the product creation process, you'll receive the actual Amazon Resource Name (ARN)
to the SNS topic. For
example: `arn:aws:sns:us-east-1:123456789012:aws-mp-subscription-notification-PRODUCTCODE`

The following Amazon SNS topics are available to software as a service (SaaS) products:

- [Amazon SNS topic:
  aws-mp-entitlement-notification](#saas-sns-message-body "#saas-sns-message-body") –
  This topic notifies you when buyers create a new contract, upgrade it, renew it, or it
  expires. This is only available for products with pricing models that include a contract
  (also known as **SaaS Contracts** and **SaaS Contracts with
  Consumption (Overages)**).
- [Amazon SNS topic:
  aws-mp-subscription-notification](#saas-sns-subscription-message-body "#saas-sns-subscription-message-body") – This topic notifies you when
  a buyer subscribes to or unsubscribes from a product and includes the
  `offer-identifier` for private offers and a free trials flag for SaaS free
  trials. This is available for all pricing models, including contracts and subscriptions
  (also known as **SaaS Subscriptions**, **SaaS Contracts**,
  and **SaaS Contracts with Consumption (Overages)**.
  To learn more about the scenarios in which you respond to these notifications, see the
  following topics:

- [Integrating your SaaS subscription or Pay-As-You-Go product with AWS Marketplace](saas-integrate-subscription.md "saas-integrate-subscription.md")
- [Integrating your SaaS contract product with AWS Marketplace](saas-integrate-contract.md "saas-integrate-contract.md")
- [Integrating your SaaS contract-based product with AWS Marketplace](saas-integrate-contract-with-pay.md "saas-integrate-contract-with-pay.md")

## Amazon SNS topic:

`aws-mp-entitlement-notification`

Each message in the `aws-mp-entitlement-notification` topic has the following
format.

```
{
    "action": "`<action-name>`",
    "customer-identifier": " `X01EXAMPLEX`",
    "product-code": "`n0123EXAMPLEXXXXXXXXXXXX`",
}
```

The `<action-name>` will always be `entitlement-updated`.

###### Note

- For entitlement messages, regardless of the action (new, upgrade, renewal, or
  expired), the message is the same. A subsequent call to `GetEntitlement` is
  required to discover the content of the update.
- For **SaaS Contract with Consumption (Overages)**, sellers are
  provided with the [aws-mp-subscription-notification SNS topic](#saas-sns-subscription-message-body "#saas-sns-subscription-message-body"). This is an extra
  notification that a seller receives when they add on overage pricing. When a seller
  acquires new customers, instead of only getting `entitlement-updated` (which
  may refer to any kind of action), the seller receives a subscribe message indicating
  that this is a new customer.
- For future dated agreements (FDAs), this topic is initiated on the agreement start
  date (and not agreement sign date). It's also initiated when subsequent changes occur in
  the entitlement, such as cancellation, replacement, renewal, or expiration of the
  agreement.

Products with contract pricing (including contracts with pay-as-you-go) must respond to
these messages. For more information about how to respond, see [Scenario: Monitor changes to user
subscriptions](saas-integrate-contract.md#saas-contract-monitor-changes "saas-integrate-contract.md#saas-contract-monitor-changes").

## Amazon SNS topic:

`aws-mp-subscription-notification`

Each message in the `aws-mp-subscription-notification` topic has the following
format.

```
{
    "action": "`<action-name>`",
    "customer-identifier": " `X01EXAMPLEX`",
    "product-code": "`n0123EXAMPLEXXXXXXXXXXXX`",
    "offer-identifier": "`offer-abcexample123`",
    "isFreeTrialTermPresent":"true"
}
```

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

The `isFreeTrialTermPresent` property indicates if the buyer's subscription is
a free trial. The JSON value of this property is not a _boolean_ datatype.
Instead, the value is converted to a _string_ datatype. For more
information, see [SaaS free trials.](saas-free-trials.md "saas-free-trials.md")

The `<action-name>` will vary depending on the notification.
Possible actions are:

- `subscribe-success` – The `subscribe-success` message
  signals when the seller can begin sending metering records. If an [agreement-based offer](private-offers-upgrades-and-renewals.md#private-offers-upgrades-and-renewals-process "private-offers-upgrades-and-renewals.md#private-offers-upgrades-and-renewals-process") is accepted by the buyer, this
  message is sent again with the new `offer-identifier`.
- `subscribe-fail` – If the `subscribe-fail` message is
  generated, payment might have failed even though the buyer has already transitioned from
  the AWS Marketplace to the seller's SaaS landing page. The seller should wait for the
  `subscribe-success` message before allowing consumption of the
  product.
- `unsubscribe-pending` – When a buyer unsubscribes, an
  `unsubscribe-pending` message is sent first. This indicates that the seller
  has a limited time (about one hour) to get final metering records sent before the buyer is
  cancelled completely.
- `unsubscribe-success` – The `unsubscribe-success` message
  signals the completion of cancellation, after which no further metering records will be
  accepted.

###### Note

- If a buyer unsubscribes and then immediately successfully re-subscribes before the
  final `unsubscribe-success` message is sent, the final
  `unsubscribe-success` message will not be sent and a
  `subscribe-success` message will be sent instead.
- For future dated agreements (FDAs), the `subscribe-success` action is
  initiated on the agreement start date (and not agreement sign date).

Products with subscription pricing (including contracts with pay-as-you-go) must respond
to these messages. For more information about how to respond, see the following topics:

- [Integrating your SaaS subscription or Pay-As-You-Go product with AWS Marketplace](saas-integrate-subscription.md "saas-integrate-subscription.md")
- [Integrating your SaaS contract-based product with AWS Marketplace](saas-integrate-contract-with-pay.md "saas-integrate-contract-with-pay.md")

## Subscribing an SQS queue to the

SNS topic

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
