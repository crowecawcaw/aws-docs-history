

# Spending and limits
<a name="nx-notify-scale-spending"></a>

Notify has its own dedicated monthly spend limit, separate from your SMS, MMS, and voice spend limits. Sending messages through Notify does not count against your SMS or voice spend limits. Your Notify spend limit reflects the combined cost of the messaging channel fee and the Notify service fee for each message sent.

The *account limit* is the maximum amount, in US dollars, that you can spend each month sending Notify messages. The *enforced limit* is an optional spending cap between $1 and your account limit. When you reach the enforced limit, `SendNotifyTextMessage` and `SendNotifyVoiceMessage` return a `ServiceQuotaExceededException`.

In the console, navigate to a Notify configuration and choose the **Spend limit** tab to view your maximum spend limit, enforced spend limit, current month spend, and remaining balance, and choose **Edit settings** to change the enforced limit. From the AWS CLI, set an enforced limit with `set-notify-message-spend-limit-override`, remove it with `delete-notify-message-spend-limit-override`, and view all spend limits with `describe-spend-limits`.

```
$ aws pinpoint-sms-voice-v2 set-notify-message-spend-limit-override \
    --monthly-limit {{100}}
```

To increase your account spend limit beyond the default, use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/) or create a support case at the AWS Support Center.