

# Spending and cost
<a name="nx-mms-scale-spending"></a>

This topic explains how to monitor the amount of money that you spend when you send MMS messages through AWS End User Messaging, and how to read the usage types on your bill. If you only want to view your monthly charges, including the amount of money you've spent, use the AWS Billing and Cost Management console, which provides an estimate of your bill for the current month and your final charges for previous months.

**Topics**
+ [Monitor your spending with CloudWatch](#nx-mms-scale-spending-monitor)
+ [Understand MMS billing and usage reports](#nx-mms-scale-spending-billing)

## Monitor your spending with CloudWatch
<a name="nx-mms-scale-spending-monitor"></a>

To quickly determine how much money you've spent sending messages during the current month, use the Metrics section of the CloudWatch console. CloudWatch retains metric data for 15 months, so you can view real-time data and analyze historical trends.

**Important**  
You must create a service-linked role for CloudWatch metrics to be collected.

**To view MMS spending metrics in CloudWatch**

1. Open the CloudWatch console.

1. In the navigation pane, choose **Metrics**.

1. On the **All metrics** tab, choose **SMSVoice**, and then choose **Account Metrics**.

1. Select **MediaMessageMonthlySpend**. The graph updates to display the amount of money spent on MMS during the current month.
**Note**  
This metric doesn't appear until you send at least one MMS message using AWS End User Messaging.

You can also create a CloudWatch billing alarm that notifies you through an Amazon SNS topic when your monthly MMS spending exceeds a certain amount. Before you create a billing alarm, set your AWS Region to US East (N. Virginia) Region, because billing metric data is stored there and represents worldwide charges. For more information, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

## Understand MMS billing and usage reports
<a name="nx-mms-scale-spending-billing"></a>

Unlike SMS, which is billed per message part, MMS is billed per message. A single MMS message is delivered as one message part and is not broken into multiple parts, so each MMS message that AWS End User Messaging accepts generates a single billable send regardless of the size of the media or the length of the text body. For more information about pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

The MMS channel generates a usage type on your bill for each combination of destination country and origination identity. The usage type follows the same field format as the SMS usage type, with the message type reading **OutboundMMS** rather than **OutboundSMS**.

**Note**  
The exact MMS usage type string format, the set of usage types generated per send (message count, message fees, and any carrier fees), and whether MMS incurs carrier fees in the United States and Canada [needs SME confirmation]. Confirm the MMS usage type details against the AWS Billing and Cost Management usage report before publishing specific examples.

You can use tags for organizing your bill to reflect your own cost structure. For example, you can tag several resources with a specific campaign name, and then organize your billing information to see the total cost of that campaign across several services. For more information, see [Cost allocation and tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.