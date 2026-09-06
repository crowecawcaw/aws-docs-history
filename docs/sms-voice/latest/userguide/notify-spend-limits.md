

# Notify spend limits
<a name="notify-spend-limits"></a>

Notify has its own dedicated monthly spend limit, separate from your SMS, MMS, and voice spend limits. Sending messages via Notify does not count against your SMS or voice spend limits.

The *account limit* is the maximum amount, in US dollars, that you can spend each month sending Notify messages. You can request an increase through the Service Quotas console.

The *enforced limit* is an optional spending cap between $1 and your account limit. When you reach the enforced limit, `SendNotifyTextMessage` and `SendNotifyVoiceMessage` return a `ServiceQuotaExceededException`.

Your Notify spend limit reflects the combined cost of the messaging channel fee and the Notify service fee for each message sent.

## Managing Notify spend limits
<a name="notify-spend-limits-manage"></a>

------
#### [ Console ]

**View spend limits**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. Navigate to a Notify configuration and choose the **Spend limit** tab.

1. The tab shows your max spend limit, enforced spend limit, current month spend, and remaining balance.

**Edit the enforced limit**

1. On the **Spend limit** tab, choose **Edit settings**.

1. Choose **Update enforced spend limit** and enter a new value, or choose **Default to max** to remove the override.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

Set an enforced spend limit:

```
aws pinpoint-sms-voice-v2 set-notify-message-spend-limit-override \
  --monthly-limit {{100}}
```

Remove the enforced limit (revert to account limit):

```
aws pinpoint-sms-voice-v2 delete-notify-message-spend-limit-override
```

View all spend limits (Notify appears alongside SMS and voice):

```
aws pinpoint-sms-voice-v2 describe-spend-limits
```

------

## Requesting a higher account limit
<a name="notify-spend-limits-increase"></a>

To increase your Notify account spend limit beyond the default, use the Service Quotas console or create a support case. For more information, see [Quotas for AWS End User Messaging SMS](quotas.md).