

# Spending and cost
<a name="nx-sms-scale-spending"></a>

This topic explains how to monitor the amount of money that you spend when you send SMS, MMS, and voice messages through AWS End User Messaging, and how to read the usage types on your bill. If you only want to view your monthly charges, including the amount of money you've spent, use the AWS Billing and Cost Management console, which provides an estimate of your bill for the current month and your final charges for previous months.

**Topics**
+ [Monitor your spending with CloudWatch](#nx-sms-scale-spending-monitor)
+ [Understand SMS billing and usage reports](#nx-sms-scale-spending-billing)

## Monitor your spending with CloudWatch
<a name="nx-sms-scale-spending-monitor"></a>

To quickly determine how much money you've spent sending messages during the current month, use the Metrics section of the CloudWatch console. CloudWatch retains metric data for 15 months, so you can view real-time data and analyze historical trends.

**Important**  
You must create a service-linked role for CloudWatch metrics to be collected.

**To view SMS, MMS, and voice spending metrics in CloudWatch**

1. Open the CloudWatch console.

1. In the navigation pane, choose **Metrics**.

1. On the **All metrics** tab, choose **SMSVoice**, and then choose **Account Metrics**.

1. Select from **TextMessageMonthlySpend**, **MediaMessageMonthlySpend**, and **VoiceMessageMonthlySpend**. The graph updates to display the amount of money spent during the current month.
**Note**  
These metrics don't appear until you send at least one message using AWS End User Messaging.

You can also create a CloudWatch billing alarm that notifies you through an Amazon SNS topic when your monthly SMS, MMS, or voice spending exceeds a certain amount. Before you create a billing alarm, set your AWS Region to US East (N. Virginia) Region, because billing metric data is stored there and represents worldwide charges. For more information, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

## Understand SMS billing and usage reports
<a name="nx-sms-scale-spending-billing"></a>

The SMS channel generates a usage type that contains five fields in the following format: `{{Region code}}–{{MessagingType}}–{{ISO}}–{{RouteType}}–{{OriginationID}}–{{MessageCount/Fee}}`. For example, SMS messages sent from the Asia Pacific (Tokyo) Region to a Japanese phone number would appear as **APN1–OutboundSMS–JP–Standard–Senderid–MessageCount**. The following table describes the fields in the usage type. For more information about pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).



| Field | Description | 
| --- | --- | 
| {{Region code}} | The AWS Region prefix that indicates where the SMS message was sent from, such as APN1 for the Asia Pacific (Tokyo) Region or USE1 for the US East (N. Virginia) Region. | 
| {{MessagingType}} | The message type being sent. For outbound SMS, it reads OutboundSMS. | 
| {{ISO}} | The two-digit ISO country code that the message was sent to. | 
| {{RouteType}} | The route type that the message was sent through. Currently, all messages are sent through the Standard route type. | 
| {{OriginationID}} | The origination identity that was used to send the message, such as TollFree, 10DLC, Shortcode, Longcode, Senderid, or Sharedroute. | 
| {{MessageCount/Fee}} | Either the number of messages sent or the cost associated with sending them: MessageCount, MessageFees, CarrierFeeCount, or CarrierFees. | 

Messages sent through AWS End User Messaging for outbound SMS generate two to four usage types per combination of ISO country and origination identity. For example, if you sent 10 messages to the United Kingdom (ISO code GB) using a short code from USE1, you can expect the following two usage types on your bill:

```
  1. USE1-OutboundSMS-GB-Standard-Shortcode-MessageCount
  2. USE1-OutboundSMS-GB-Standard-Shortcode-MessageFee
```

If you sent 10 messages to the United States (ISO code US) using a 10DLC number from CAN1, you can expect four usage types, because 10DLC to US recipients also generates carrier fee usage types:

```
  1. CAN1-OutboundSMS-US-Standard-10DLC-MessageCount
  2. CAN1-OutboundSMS-US-Standard-10DLC-MessageFee
  3. CAN1-OutboundSMS-US-Standard-10DLC-CarrierFeeCount
  4. CAN1-OutboundSMS-US-Standard-10DLC-CarrierFees
```

You can use tags for organizing your bill to reflect your own cost structure. For example, you can tag several resources with a specific campaign name, and then organize your billing information to see the total cost of that campaign across several services. For more information, see [Cost allocation and tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.