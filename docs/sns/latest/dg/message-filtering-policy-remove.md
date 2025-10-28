# Removing a subscription filter policy in

Amazon SNS

To stop filtering the messages that are sent to a subscription, remove the subscription's
filter policy by overwriting it with an empty JSON body. After you remove the policy, the
subscription accepts every message that's published to it.

## Using the AWS Management Console

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. On the navigation panel, choose **Subscriptions**.
3. Select a subscription and then choose **Edit**.
4. On the **Edit
   `EXAMPLE1-23bc-4567-d890-ef12g3hij456`**
   page, expand the **Subscription filter policy** section.
5. In the **JSON editor** field, provide an empty JSON body for
   your filter policy: `{}`.
6. Choose **Save changes**.

Amazon SNS applies your filter policy to the subscription.

## Using the AWS CLI

To remove a filter policy with the AWS CLI, use the [`set-subscription-attributes`](../../../cli/latest/reference/sns/set-subscription-attributes.md "../../../cli/latest/reference/sns/set-subscription-attributes.md") command and provide an empty
JSON body for the `--attribute-value` argument:

```
`$` `aws sns set-subscription-attributes --subscription-arn `arn:aws:sns: ...` --attribute-name FilterPolicy --attribute-value "{}"`
```

## Using the Amazon SNS API

To remove a filter policy with the Amazon SNS API, make a request to the [`SetSubscriptionAttributes`](../api/API_SetSubscriptionAttributes.md "../api/API_SetSubscriptionAttributes.md") action. Set the
`AttributeName` parameter to `FilterPolicy`, and provide an
empty JSON body for the `AttributeValue` parameter.
