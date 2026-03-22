# Modifying an Amazon RDS event notification subscription

After you have created a subscription, you can change the subscription name, source identifier, categories, or
topic ARN.

###### To modify an Amazon RDS event notification subscription

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Event subscriptions**.
3. In the **Event subscriptions** pane, choose the subscription that you want to
   modify and choose **Edit**.
4. Make your changes to the subscription in either the **Target** or
   **Source** section.
5. Choose **Edit**. The Amazon RDS console indicates that the subscription is being
   modified.

![List DB event notification subscriptions](images/EventNotification-Modify2.png)
To modify an Amazon RDS event notification subscription, use the AWS CLI [`modify-event-subscription`](../../../cli/latest/reference/rds/modify-event-subscription.md "../../../cli/latest/reference/rds/modify-event-subscription.md")
command. Include the following required parameter:

- `--subscription-name`

###### Example

The following code enables `myeventsubscription`.

For Linux, macOS, or Unix:

```
aws rds modify-event-subscription \
    --subscription-name `myeventsubscription` \
    `--enabled`
```

For Windows:

```
aws rds modify-event-subscription ^
    --subscription-name `myeventsubscription` ^
    `--enabled`
```

To modify an Amazon RDS event, call the Amazon RDS API operation [`ModifyEventSubscription`](../APIReference/API_ModifyEventSubscription.md "../APIReference/API_ModifyEventSubscription.md").
Include the following required parameter:

- `SubscriptionName`
