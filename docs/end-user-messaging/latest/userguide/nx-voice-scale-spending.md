

# Spending and cost
<a name="nx-voice-scale-spending"></a>

This topic explains how to monitor the amount of money that you spend when you send voice messages through AWS End User Messaging. If you only want to view your monthly charges, including the amount of money you've spent, use the AWS Billing and Cost Management console, which provides an estimate of your bill for the current month and your final charges for previous months.

**Topics**
+ [Monitor your spending with CloudWatch](#nx-voice-scale-spending-monitor)
+ [Understand voice billing and usage reports](#nx-voice-scale-spending-billing)

## Monitor your spending with CloudWatch
<a name="nx-voice-scale-spending-monitor"></a>

To quickly determine how much money you've spent sending voice messages during the current month, use the Metrics section of the CloudWatch console. CloudWatch retains metric data for 15 months, so you can view real-time data and analyze historical trends.

**Important**  
You must create a service-linked role for CloudWatch metrics to be collected.

**To view voice spending metrics in CloudWatch**

1. Open the CloudWatch console.

1. In the navigation pane, choose **Metrics**.

1. On the **All metrics** tab, choose **SMSVoice**, and then choose **Account Metrics**.

1. Select **VoiceMessageMonthlySpend**. The graph updates to display the amount of money spent on voice messages during the current month.
**Note**  
This metric doesn't appear until you send at least one voice message using AWS End User Messaging.

You can also create a CloudWatch billing alarm that notifies you through an Amazon SNS topic when your monthly voice spending exceeds a certain amount. Before you create a billing alarm, set your AWS Region to US East (N. Virginia) Region, because billing metric data is stored there and represents worldwide charges. For more information, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

## Understand voice billing and usage reports
<a name="nx-voice-scale-spending-billing"></a>

Voice charges depend on the recipient's country and the duration of each call, so voice bills differently from SMS. The exact voice usage-type format and the per-message or per-minute billing specifics are [needs SME confirmation] — confirm the current voice usage types and charge units before you rely on them for cost allocation. For current voice pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

You can use tags for organizing your bill to reflect your own cost structure. For example, you can tag several resources with a specific campaign name, and then organize your billing information to see the total cost of that campaign across several services. For more information, see [Cost allocation and tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.