

# Spending and cost
<a name="nx-rcs-scale-spending"></a>

This topic explains how RCS messages are priced, how to monitor the amount of money that you spend sending them, and how to set a monthly spending limit. If you only want to view your monthly charges, use the AWS Billing and Cost Management console, which provides an estimate of your bill for the current month and your final charges for previous months.

RCS pricing has two components: an AWS message fee and a carrier fee that is passed through with no markup. AWS End User Messaging charges only for RCS messages that are confirmed delivered to the device. If a message falls back to SMS, you are charged for the SMS that is delivered, not for the failed RCS attempt. For current rates, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

**Topics**
+ [Monitor your spending with CloudWatch](#nx-rcs-scale-spending-monitor)
+ [Set a monthly spending limit for RCS](#nx-rcs-scale-spending-limit)
+ [Understand RCS billing and usage reports](#nx-rcs-scale-spending-billing)

## Monitor your spending with CloudWatch
<a name="nx-rcs-scale-spending-monitor"></a>

To quickly determine how much money you've spent sending RCS messages during the current month, use the Metrics section of the CloudWatch console. CloudWatch retains metric data for 15 months, so you can view real-time data and analyze historical trends.

**Important**  
You must create a service-linked role for CloudWatch metrics to be collected.

**To view RCS spending metrics in CloudWatch**

1. Open the CloudWatch console.

1. In the navigation pane, choose **Metrics**.

1. On the **All metrics** tab, choose **SMSVoice**, and then choose **Account Metrics**.

1. Select the RCS monthly spend metric. The graph updates to display the amount of money spent on RCS during the current month.
**Note**  
The metric doesn't appear until you send at least one RCS message using AWS End User Messaging.

**Note**  
Confirm the exact RCS monthly spend metric name in the CloudWatch `SMSVoice` Account Metrics namespace before publishing [needs SME confirmation]. The other channels use `TextMessageMonthlySpend`, `MediaMessageMonthlySpend`, and `VoiceMessageMonthlySpend`.

You can also create a CloudWatch billing alarm that notifies you through an Amazon SNS topic when your monthly RCS spending exceeds a certain amount. Before you create a billing alarm, set your AWS Region to US East (N. Virginia) Region, because billing metric data is stored there and represents worldwide charges. For more information, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

## Set a monthly spending limit for RCS
<a name="nx-rcs-scale-spending-limit"></a>

AWS End User Messaging enforces a monthly spending limit for RCS messages. The limit has two values: a maximum limit that AWS sets for your account, and an enforced limit that you can set to a lower value to cap your own spending. When your RCS spending reaches the enforced limit for the month, AWS End User Messaging stops sending RCS messages until the next calendar month or until you raise the limit. To raise the maximum limit, request an increase as described in [Quotas](nx-features-quotas.md).

Set your own enforced limit with the `SetRcsMessageSpendLimitOverride` operation, and remove it with `DeleteRcsMessageSpendLimitOverride` to return to the maximum limit. You can view the current limits with the `DescribeSpendLimits` operation.

## Understand RCS billing and usage reports
<a name="nx-rcs-scale-spending-billing"></a>

RCS is billed per delivered message rather than per message part. Each RCS message that is confirmed delivered generates a single billable send, regardless of whether it is a text message, a rich card, or a carousel. A message that falls back to SMS is billed as an SMS message. For more information about pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

**Note**  
Confirm the exact RCS usage type string format on your bill, the set of usage types generated per send (message fee and pass-through carrier fee), and the per-country carrier fee treatment against the AWS Billing and Cost Management usage report before publishing specific examples [needs SME confirmation].

You can use tags for organizing your bill to reflect your own cost structure. For example, you can tag several resources with a specific campaign name, and then organize your billing information to see the total cost of that campaign across several services. For more information, see [Cost allocation and tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.