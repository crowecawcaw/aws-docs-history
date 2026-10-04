

# Monitoring
<a name="nx-rcs-scale-monitoring"></a>

AWS End User Messaging gives you several complementary views of your RCS messaging: aggregate delivery health in Amazon CloudWatch, per-message delivery receipts with channel attribution, and granular message events that you route to a destination. This topic describes how to set up each one.


**Ways to monitor your RCS messaging**  

| What you monitor | How it works | 
| --- | --- | 
| **Overall delivery health** | Amazon CloudWatch metrics in the `AWS/SMSVoice` namespace aggregate your RCS sending into near real-time numbers (messages sent, delivered, and fallen back to SMS) that you watch on dashboards and alarm on. The fallback metric lets you track how often RCS delivery is unavailable for your recipients and watch your RCS-to-SMS fallback rate over time. | 
| **Per-message events** | Message events report what happened to each individual message as it moves through its lifecycle, including its final delivery status, the channel that delivered it (RCS or the SMS fallback), and recipient interactions such as reads, typing, and tapped suggestions. You route these events to a destination with a configuration set. | 
| **API activity** | AWS CloudTrail records the AWS End User Messaging API calls that your account makes, so you can see who did what and when for auditing and troubleshooting. | 
| **Outcome feedback** | Message feedback lets you report whether each message reached its intended outcome, so you can track conversion and improve the deliverability signals AWS End User Messaging uses. | 

## Monitoring with CloudWatch
<a name="nx-rcs-scale-monitoring-cloudwatch"></a>

You can monitor AWS End User Messaging using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. CloudWatch retains metric data for 15 months, so you can access historical information and gain a better perspective on how your RCS messaging is performing. The namespace for AWS End User Messaging metrics is `AWS/SMSVoice`, where RCS metrics are published alongside your SMS and MMS metrics.

**Note**  
AWS End User Messaging uses an AWS Identity and Access Management (IAM) service-linked role to publish metrics to CloudWatch. The service creates this role for you the first time you perform an action that publishes metrics, so in most cases you do not need to create it yourself.

### Metrics
<a name="nx-rcs-mon-metrics"></a>

AWS End User Messaging publishes RCS messaging metrics to CloudWatch in the `AWS/SMSVoice` namespace. You can use these metrics to monitor your RCS message delivery, track fallback behavior from RCS to SMS, and set alarms to alert you when delivery patterns change. RCS metrics are published alongside existing SMS and MMS metrics in the same namespace.

#### RCS messaging metrics
<a name="nx-rcs-mon-metrics-rcs-metrics"></a>

The `AWS/SMSVoice` namespace includes the following metrics specific to RCS messaging. These metrics track RCS message sending, delivery, and SMS fallback.


**RCS messaging metrics**  

| Metric | Description | Unit | Meaningful statistics | 
| --- | --- | --- | --- | 
| RCS.MessagesSent | The number of RCS messages sent. This metric counts messages that AWS End User Messaging accepted and attempted to deliver via RCS. Messages blocked by Protect or service limits are excluded from this count. | Count |  + Sum<br />+ Sample Count<br />+ Average  | 
| RCS.MessagesDelivered | The number of RCS messages successfully delivered to the recipient's device. A message is counted as delivered when AWS End User Messaging receives a delivery confirmation from the RCS infrastructure. | Count |  + Sum<br />+ Sample Count<br />+ Average  | 
| RCS.MessagesFallenBackToSMS | The number of messages that were initially attempted via RCS but fell back to SMS delivery. This metric helps you understand how often RCS delivery is unavailable for your recipients and can be used to track fallback rates over time. | Count |  + Sum<br />+ Sample Count<br />+ Average  | 

#### OriginationIdentityType dimension
<a name="nx-rcs-mon-metrics-dimensions-origination"></a>

The `OriginationIdentityType` dimension filters metrics by the type of origination identity used to send the message.


**OriginationIdentityType dimension values**  

| Value | Description | 
| --- | --- | 
| PHONE\_NUMBER | Messages sent using a phone number (long code, short code, or toll-free number). | 
| SENDER\_ID | Messages sent using a sender ID. | 
| RCS\_AGENT | Messages sent using an AWS RCS Agent. | 
| POOL | Messages sent using a phone pool. When you send through a pool, AWS End User Messaging selects the appropriate origination identity (AWS RCS Agent or phone number) automatically. | 

#### MessageType dimension
<a name="nx-rcs-mon-metrics-dimensions-messagetype"></a>

The `MessageType` dimension filters metrics by the type of message.


**MessageType dimension values**  

| Value | Description | 
| --- | --- | 
| TEXT | Text messages sent via RCS or SMS. | 
| MEDIA | Media messages (MMS). RCS in AWS End User Messaging currently supports text messages only. | 
| DELIVERY\_REPORT | Delivery report messages confirming message delivery status. | 

**Note**  
The `READ_REPORT` message type is not available because read receipts are not supported in the current release of RCS in AWS End User Messaging.

#### Modified existing metrics with OriginationIdentityType dimension
<a name="nx-rcs-mon-metrics-modified-metrics"></a>

With the addition of RCS, several existing metrics in the `AWS/SMSVoice` namespace now support the `OriginationIdentityType` dimension. This dimension allows you to filter metrics by the type of origination identity used to send the message, including AWS RCS Agents.

The following existing metrics now include the `OriginationIdentityType` dimension:


| Metric | Description | 
| --- | --- | 
| `NumberOfTextMessagePartsSent` | Filter by origination identity type to see how many text message parts were sent via each channel (phone number, sender ID, AWS RCS Agent, or pool). | 
| `NumberOfTextMessagePartsDelivered` | Filter by origination identity type to compare delivery rates across channels. | 
| `NumberOfMediaMessagePartsSent` | Filter by origination identity type to track media message sending by channel. | 
| `NumberOfMediaMessagePartsDelivered` | Filter by origination identity type to compare media message delivery across channels. | 
| `TextMessagesBlockedByProtect` | Filter by origination identity type to see which channels have messages blocked by Protect rules. | 
| `MediaMessagesBlockedByProtect` | Filter by origination identity type to track Protect blocking by channel. | 

Use the `OriginationIdentityType` dimension with a value of `RCS_AGENT` to isolate metrics for messages sent through your AWS RCS Agent. For more information about the available dimension values, see [OriginationIdentityType dimension](#nx-rcs-mon-metrics-dimensions-origination).

#### Inbound RCS message metrics
<a name="nx-rcs-mon-metrics-inbound"></a>

The existing `NumberOfMessagesReceived` metric in the `AWS/SMSVoice` namespace now includes inbound RCS messages. You can use the `OriginationIdentityType` dimension with a value of `RCS_AGENT` to filter for inbound messages received through your AWS RCS Agent.

Inbound RCS messages are the messages that recipients send back to your AWS RCS Agent in a two-way conversation, such as a reply to a prompt or a tap on a suggested reply. AWS End User Messaging counts each inbound message in the `NumberOfMessagesReceived` metric, so you can track inbound RCS volume alongside inbound SMS in the same metric and tell them apart with the `OriginationIdentityType` dimension.

To receive and monitor inbound RCS messages, configure a two-way Amazon SNS topic on your AWS RCS Agent. AWS End User Messaging delivers each inbound message to that topic and publishes the `NumberOfMessagesReceived` metric. For how to set up two-way messaging, see [Inbound messaging](nx-rcs-send-inbound.md).

The following dimensions are available for inbound RCS message metrics:


| Dimension | How to use it | 
| --- | --- | 
| `OriginationIdentityType` | Use `RCS_AGENT` to filter for inbound RCS messages. | 
| `IsoCountryCode` | Filter by the country code of the inbound message sender. | 
| `MessageType` | Use `TEXT` to filter for text messages received via RCS. In the current release, RCS in AWS End User Messaging supports inbound text messages only. | 

#### Set CloudWatch alarms for RCS metrics
<a name="nx-rcs-mon-metrics-bp-alarms"></a>

Create CloudWatch alarms to alert you when RCS messaging patterns change unexpectedly. Consider setting alarms for the following conditions:


| Alarm on | Why | 
| --- | --- | 
| **High fallback rate** | Set an alarm when `RCS.MessagesFallenBackToSMS` exceeds a threshold percentage of `RCS.MessagesSent`. A sudden increase in fallback may indicate an issue with your AWS RCS Agent or a carrier outage. | 
| **Delivery rate drop** | Set an alarm when the ratio of `RCS.MessagesDelivered` to `RCS.MessagesSent` drops below your expected delivery rate. | 
| **Inbound message volume** | If you use two-way RCS messaging, set an alarm on `NumberOfMessagesReceived` (filtered by `OriginationIdentityType = RCS_AGENT`) to detect unexpected changes in inbound message volume. | 

You can create a Amazon CloudWatch alarm that sends a notification when an RCS metric crosses a threshold you set. For example, you can alarm when your RCS-to-SMS fallback rate rises above an expected level. For more information, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

------
#### [ Console ]

**To create an alarm that notifies you when an RCS metric exceeds a threshold**

1. Open the CloudWatch console.

1. Choose **Alarms** in the navigation pane, and then choose **Create alarm**.

1. Choose **Select metric**, choose the `AWS/SMSVoice` namespace, and choose the RCS metric that you want to set an alarm for, such as `RCS.MessagesFallenBackToSMS`.

1. Set the statistic to **Sum**, the period to 1 hour, the condition to **Static** and **Greater than**, and enter the threshold value.

1. For the alarm action, choose an existing Amazon SNS topic to notify or create a new one, enter a name for the alarm, and choose **Create alarm**.

------
#### [ AWS CLI ]

Use the [put-metric-alarm](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html) command. The following example alarms when more than 100 RCS messages fall back to SMS in one hour and notifies an Amazon SNS topic.

```
$ aws cloudwatch put-metric-alarm \
> --alarm-name {{HighRcsFallbackRate}} \
> --namespace AWS/SMSVoice \
> --metric-name RCS.MessagesFallenBackToSMS \
> --statistic Sum \
> --period 3600 \
> --evaluation-periods 1 \
> --threshold 100 \
> --comparison-operator GreaterThanThreshold \
> --alarm-actions arn:aws:sns:{{us-east-1}}:{{111122223333}}:{{snsTopic}}
```

------

## Send events to a destination
<a name="nx-rcs-mon-events"></a>

When you send RCS messages with AWS End User Messaging, the RCS platform generates an event for each message as it moves through its lifecycle (delivered, read, expired, or fallen back to SMS) and for each recipient interaction (a typing indicator or a suggestion tap). You route these events to a destination so that you can confirm delivery, trigger fallback logic, and measure engagement.

Outbound status events are delivered through configuration set event destinations. Inbound interaction events (typing indicators and suggestion taps) are delivered to the two-way Amazon SNS topic that you configure on your RCS agent. Every RCS event also carries an `rcsBusinessId` and an `agentIsoCountryCode` that identify the RCS agent.

### Channel attribution
<a name="nx-rcs-mon-events-channel-attribution"></a>

Delivery receipts include channel attribution that indicates whether the message was delivered via RCS or the SMS fallback. This is important for understanding your delivery mix and for billing purposes.
+ When a message is delivered via RCS, the delivery receipt indicates RCS as the delivery channel and includes the AWS RCS Agent identity.
+ When a message falls back to SMS, the delivery receipt indicates SMS as the delivery channel and includes the SMS phone number identity that was used for delivery.
+ When a direct send (AWS RCS Agent ARN) fails, the delivery receipt indicates RCS as the attempted channel with a failure status. No SMS fallback receipt is generated.

For how delivery channel affects billing, see [Spending and cost](nx-rcs-scale-spending.md).

### Routing events to destinations
<a name="nx-rcs-mon-events-routing"></a>

AWS End User Messaging routes RCS events through configuration set event destinations. You configure event destinations on the configuration set that is associated with your sending operations. Supported destinations include:


| Destination | When to use it | 
| --- | --- | 
| Amazon SNS | Use an Amazon SNS topic for real-time event processing, including triggering AWS Lambda functions to respond to delivery receipts or suggestion taps. | 
| Amazon Data Firehose | Use a Firehose delivery stream to send events to Amazon S3, Amazon Redshift, or other analytics destinations for long-term storage and reporting. | 
| Amazon CloudWatch Logs | Use CloudWatch Logs for debugging, log analysis, and setting up CloudWatch alarms on event patterns (for example, alerting on high rejection rates). | 

To learn how to create and configure event destinations, see [Event destinations in AWS End User Messaging](nx-features-configuration-sets-event-destinations.md).

When you call `SendRcsMessage`, specify the `ConfigurationSetName` parameter to associate the message with your configuration set. Outbound status events generated by that message are routed to the destinations you configured.

When you configure the event types that an event destination matches, you can select `RCS_ALL` to subscribe to all RCS event types with a single matching type, instead of listing each RCS event type individually (such as `RCS_DELIVERED` and `RCS_READ`).

**Note**  
Inbound interaction events, including typing indicators and suggestion taps (postbacks), are delivered to the two-way Amazon SNS topic configured on your RCS agent, not to configuration set event destinations.

For the full catalog of RCS event types (delivery status, read receipts, typing indicators, TTL expiration, fallback, suggestion taps, and conversational pricing events), the fields each one carries, and example payloads, see [RCS example log](nx-features-messaging-events.md#configuration-sets-event-format-rcs-example).

## Message feedback
<a name="nx-rcs-scale-monitoring-feedback"></a>

Message feedback lets you report whether a recipient received or acted on an RCS message, so that Amazon CloudWatch delivery metrics reflect the real outcome and not only what the platform reported. You enable feedback in one of two ways:
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
$ aws pinpoint-sms-voice-v2 send-rcs-message \
> --destination-phone-number {{+12065550150}} \
> --origination-identity {{rcs-c020de2520714385964ebf7b095c4b60}} \
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
<a name="nx-rcs-scale-monitoring-cloudtrail"></a>

AWS CloudTrail captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS End User Messaging, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).