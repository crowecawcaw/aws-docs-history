

# Monitoring
<a name="nx-sms-scale-monitoring"></a>

AWS End User Messaging gives you two complementary views of your SMS messaging, plus a record of your API activity and a way to report message outcomes. This topic describes how to set up each one.


**Ways to monitor your SMS messaging**  

| What you monitor | How it works | 
| --- | --- | 
| **Overall delivery health** | Amazon CloudWatch metrics aggregate your sending into near real-time numbers (parts sent and delivered, spend, and messages blocked) that you watch on dashboards and alarm on. | 
| **Granular per-message events** | Message events report what happened to each individual message as it is sent and delivered. You route them to a destination with a configuration set, or consume them from Amazon EventBridge. | 
| **API activity** | AWS CloudTrail logs the AWS End User Messaging API calls made in your account. | 
| **Outcome feedback** | Message feedback lets you report whether each message reached its intended outcome, so you can track conversion and improve the deliverability signals AWS End User Messaging uses. | 

## Monitoring with CloudWatch
<a name="nx-sms-scale-monitoring-cloudwatch"></a>

You can monitor AWS End User Messaging using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. CloudWatch retains metric data for 15 months, so you can access historical information and gain a better perspective on how your application is performing. The namespace for AWS End User Messaging metrics is `AWS/SMSVoice`. The following table lists common SMS metrics you can monitor. For the complete list, see the `AWS/SMSVoice` namespace in the CloudWatch console.

**Note**  
AWS End User Messaging uses an AWS Identity and Access Management (IAM) service-linked role to publish metrics to CloudWatch. The service creates this role for you the first time you perform an action that publishes metrics, so in most cases you do not need to create it yourself.


**Common SMS metrics (AWS/SMSVoice namespace)**  

| Metric | Description | 
| --- | --- | 
| NumberOfTextMessagePartsSent | The number of SMS message parts sent. | 
| NumberOfTextMessagePartsDelivered | The number of SMS message parts confirmed delivered. | 
| NumberOfMessagesReceived | The number of inbound (two-way) messages received. | 
| TextMessageMonthlySpend | The month-to-date spend on SMS messages, in US Dollars. | 
| TextMessagesBlockedByProtect | The number of SMS messages blocked by a protect configuration. | 
| Messages expecting feedback | The number of messages sent with message feedback enabled that are awaiting an outcome. For more information, see [Message feedback](#nx-sms-scale-monitoring-feedback). | 

**Note**  
For some metrics, the result might be approximate due to the distributed nature of the service. In most cases, the count should be close to the actual number of messages processed.

### Filter metrics by origination identity type
<a name="nx-sms-scale-monitoring-dimensions"></a>

Several metrics in the `AWS/SMSVoice` namespace support the `OriginationIdentityType` dimension, which lets you filter and group a metric by the type of origination identity that sent the message. For SMS this applies to the text message part metrics (`NumberOfTextMessagePartsSent` and `NumberOfTextMessagePartsDelivered`) and to `TextMessagesBlockedByProtect`.

Use this dimension to compare sending and delivery across the identity types you use, for example to see how many parts were sent through a phone pool versus a sender ID. The dimension takes the following values.


**OriginationIdentityType dimension values**  

| Value | Description | 
| --- | --- | 
| PHONE\_NUMBER | Messages sent using a phone number (long code, short code, or toll-free number). | 
| SENDER\_ID | Messages sent using a sender ID. | 
| RCS\_AGENT | Messages sent using an AWS RCS Agent. | 
| POOL | Messages sent using a phone pool. When you send through a pool, AWS End User Messaging selects the appropriate origination identity automatically. | 

With CloudWatch, you can also create alarms that trigger based on metric thresholds. For example, you can create an alarm for the `NumberOfTextMessagePartsSent` metric so that if more than 1,000 text message parts are sent in one hour, an email notification is sent to an Amazon SNS topic. For more information, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

------
#### [ Console ]

**To create an alarm that notifies you when text message parts exceed a threshold**

1. Open the CloudWatch console.

1. Choose **Alarms** in the navigation pane, and then choose **Create alarm**.

1. Choose **Select metric**, choose the `AWS/SMSVoice` namespace, and choose the metric that you want to set an alarm for, such as `NumberOfTextMessagePartsSent`.

1. Set the statistic to **Sum**, the period to 1 hour, the condition to **Static** and **Greater than**, and enter the threshold value.

1. For the alarm action, choose an existing Amazon SNS topic to notify or create a new one, enter a name for the alarm, and choose **Create alarm**.

------
#### [ AWS CLI ]

Use the [put-metric-alarm](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html) command. The following example alarms when more than 1,000 text message parts are sent in one hour and notifies an Amazon SNS topic.

```
$ aws cloudwatch put-metric-alarm \
> --alarm-name {{HighTextMessagePartsSent}} \
> --namespace AWS/SMSVoice \
> --metric-name NumberOfTextMessagePartsSent \
> --statistic Sum \
> --period 3600 \
> --evaluation-periods 1 \
> --threshold 1000 \
> --comparison-operator GreaterThanThreshold \
> --alarm-actions arn:aws:sns:{{us-east-1}}:{{111122223333}}:{{snsTopic}}
```

------

## Send events to a destination with a configuration set
<a name="nx-sms-scale-monitoring-eventbridge"></a>

AWS End User Messaging emits an event for each message as it moves through sending and delivery. You route these events to a destination by creating a configuration set, adding one or more event destinations to it, and then specifying that configuration set when you send. The supported event destinations are Amazon CloudWatch, Amazon Data Firehose, and Amazon SNS.

To route events, create a configuration set, add one or more event destinations to it, and then specify that configuration set when you send. Both steps are shown in each tab.

------
#### [ Console ]

**To create a configuration set and add an event destination**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Configuration sets**, and then choose **Create configuration set**.

1. For **Configuration set name**, enter a descriptive name, and then choose **Create configuration set**.

1. On the **Configuration set details** page, choose **Add destination event**.

1. Under **Event details**, enter a name, and for **Destination type** choose Amazon SNS (or **CloudWatch** or **Firehose**), then choose a new or existing Amazon SNS topic.

1. Under **Event types**, choose **All SMS events (Recommended)**, or choose **Custom SMS events** to select specific event types.

1. Choose **Add event destination**.

------
#### [ AWS CLI ]

First, create the configuration set with the [create-configuration-set](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/create-configuration-set.html) command.

```
$ aws pinpoint-sms-voice-v2 create-configuration-set \
> --configuration-set-name {{configurationSet}}
```

Then add an event destination with the [create-event-destination](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/create-event-destination.html) command. The following example adds an Amazon SNS destination; you can also send events to CloudWatch or Firehose. Set `--matching-event-types` to the event types you want to send.

```
$ aws pinpoint-sms-voice-v2 create-event-destination \
> --event-destination-name {{eventDestinationName}} \
> --configuration-set-name {{configurationSet}} \
> --matching-event-types {{eventTypes}} \
> --sns-destination TopicArn=arn:aws:sns:{{us-east-1}}:{{111122223333}}:{{snsTopic}}
```

------

When you add a destination, you choose which events to send to it. You can send all SMS, MMS, and voice events, or select specific event types, such as only delivered, successful, or failed events. For the complete list of event types and what each one means, see [Event types for SMS, MMS, and voice](configuration-sets-event-types.md). For the required IAM roles for each destination type, see [Event destinations in AWS End User Messaging](nx-features-configuration-sets-event-destinations.md).

## Send events to a destination with Amazon EventBridge
<a name="nx-sms-scale-monitoring-eventbridge-bus"></a>

Unlike the other destinations, you do not add Amazon EventBridge to a configuration set. AWS End User Messaging sends events to Amazon EventBridge automatically, on your account's default event bus. To act on them, write Amazon EventBridge rules on the default bus that match the event type and route to a target such as Lambda, Amazon SNS, or Firehose. AWS End User Messaging sends the following events to Amazon EventBridge.


**Events sent to Amazon EventBridge**  

| Event (`detail-type`) | Description | 
| --- | --- | 
| Text Message Delivery Status Updated | The delivery status of an SMS message changed. | 
| Media Message Delivery Status Updated | The delivery status of an MMS message changed. | 
| Voice Message Delivery Status Updated | The delivery status of a voice message changed. | 
| Registration Status Change | The status of a registration, such as a phone number or sender ID registration, changed. | 

To act on these events, create an Amazon EventBridge rule on the default bus that matches the source `aws.sms-voice` and the `detail-type` you want, and set a target such as Lambda, Amazon SNS, or Firehose.

------
#### [ Console ]

**To create a rule for AWS End User Messaging events**

1. Open the Amazon EventBridge console and choose **Rules**, then **Create rule**.

1. Keep the default event bus, give the rule a name, and for the event pattern choose **Custom pattern**. Match `"source": ["aws.sms-voice"]` and the `detail-type` values you want.

1. Choose a target, such as a Lambda function, Amazon SNS topic, or Firehose stream, and then create the rule.

------
#### [ AWS CLI ]

Create the rule with the [put-rule](https://docs.aws.amazon.com/cli/latest/reference/events/put-rule.html) command, then attach a target with [put-targets](https://docs.aws.amazon.com/cli/latest/reference/events/put-targets.html).

```
$ aws events put-rule \
> --name {{sms-voice-delivery-status}} \
> --event-pattern '{"source":["aws.sms-voice"],"detail-type":["Text Message Delivery Status Updated"]}'

$ aws events put-targets \
> --rule {{sms-voice-delivery-status}} \
> --targets Id=1,Arn=arn:aws:lambda:{{us-east-1}}:{{111122223333}}:function:{{processEvent}}
```

------

For the full field reference and an example record for every event type, see [Messaging Events](nx-features-messaging-events.md).

## Message feedback
<a name="nx-sms-scale-monitoring-feedback"></a>

Delivery metrics and events tell you a message was delivered, but not whether it achieved its purpose, such as whether the recipient entered the one-time passcode you sent or completed the action the message asked for. Message feedback closes that loop: after you send, you report the final outcome, and AWS End User Messaging uses that signal to improve how it routes your traffic.

You can enable message feedback in two ways:
+ **Per message, at send time.** Add `--message-feedback-enabled` to an individual send request to turn it on for that message only.
+ **For every message, on a configuration set.** Turn the setting on in a configuration set so that every message you send with that configuration set has feedback enabled.

After you enable it, report the outcome once you know it. The following tabs show the configuration set setting in the console and the per-send flag in the AWS CLI.

------
#### [ Console ]

**To enable message feedback on a configuration set**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Configuration sets**, and then choose your configuration set.

1. Choose the **Set settings** tab, and then choose **Edit settings**.

1. For **Message feedback**, enable the setting, and then choose **Save changes**.

You report the outcome with the API or AWS CLI (`put-message-feedback`); there is no console action for reporting an individual message outcome.

------
#### [ AWS CLI ]

To enable feedback for a single message, add `--message-feedback-enabled` to your send command. To enable it for every message instead, turn the setting on in a configuration set (see the Console tab) and send with that configuration set.

```
$ aws pinpoint-sms-voice-v2 send-text-message \
> --destination-phone-number {{+12065550150}} \
> --origination-identity {{+14255550120}} \
> --message-body {{"text body"}} \
> --message-feedback-enabled
```

When you have a signal that the customer received or acted on the message, report the outcome with the [put-message-feedback](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/put-message-feedback.html) command, using the message ID from the send response. Set the status to `RECEIVED` or `FAILED`.

```
$ aws pinpoint-sms-voice-v2 put-message-feedback \
> --message-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
> --message-feedback-status {{RECEIVED}}
```

------

If you do not update the record within one hour it is automatically set to `FAILED`, and the CloudWatch feedback metrics update only after the record is set to `RECEIVED` or `FAILED`. For the full setup and outcome values, see [Message feedback](nx-features-message-feedback.md).

## Logging API calls with CloudTrail
<a name="nx-sms-scale-monitoring-cloudtrail"></a>

AWS CloudTrail captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS End User Messaging, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).