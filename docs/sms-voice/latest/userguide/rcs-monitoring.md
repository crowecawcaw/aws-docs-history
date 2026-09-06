

# RCS CloudWatch metrics and monitoring
<a name="rcs-monitoring"></a>

AWS End User Messaging publishes RCS messaging metrics to CloudWatch in the `AWS/SMSVoice` namespace. You can use these metrics to monitor your RCS message delivery, track fallback behavior from RCS to SMS, and set alarms to alert you when delivery patterns change. RCS metrics are published alongside existing SMS and MMS metrics in the same namespace.

**Topics**
+ [RCS messaging metrics](#rcs-monitoring-rcs-metrics)
+ [Modified existing metrics with OriginationIdentityType dimension](#rcs-monitoring-modified-metrics)
+ [RCS metric dimensions](#rcs-monitoring-dimensions)
+ [Inbound RCS message metrics](#rcs-monitoring-inbound)
+ [Monitoring best practices for RCS](#rcs-monitoring-best-practices)

## RCS messaging metrics
<a name="rcs-monitoring-rcs-metrics"></a>

The `AWS/SMSVoice` namespace includes the following metrics specific to RCS messaging. These metrics track RCS message sending, delivery, and SMS fallback.


**RCS messaging metrics**  

| Metric | Description | Unit | Meaningful statistics | 
| --- | --- | --- | --- | 
| RCS.MessagesSent | The number of RCS messages sent. This metric counts messages that AWS End User Messaging accepted and attempted to deliver via RCS. Messages blocked by Protect or service limits are excluded from this count. | Count |  + Sum<br />+ Sample Count<br />+ Average  | 
| RCS.MessagesDelivered | The number of RCS messages successfully delivered to the recipient's device. A message is counted as delivered when AWS End User Messaging receives a delivery confirmation from the RCS infrastructure. | Count |  + Sum<br />+ Sample Count<br />+ Average  | 
| RCS.MessagesFallenBackToSMS | The number of messages that were initially attempted via RCS but fell back to SMS delivery. This metric helps you understand how often RCS delivery is unavailable for your recipients and can be used to track fallback rates over time. | Count |  + Sum<br />+ Sample Count<br />+ Average  | 

## Modified existing metrics with OriginationIdentityType dimension
<a name="rcs-monitoring-modified-metrics"></a>

With the addition of RCS, several existing metrics in the `AWS/SMSVoice` namespace now support the `OriginationIdentityType` dimension. This dimension allows you to filter metrics by the type of origination identity used to send the message, including AWS RCS Agents.

The following existing metrics now include the `OriginationIdentityType` dimension:
+ `NumberOfTextMessagePartsSent` — Filter by origination identity type to see how many text message parts were sent via each channel (phone number, sender ID, AWS RCS Agent, or pool).
+ `NumberOfTextMessagePartsDelivered` — Filter by origination identity type to compare delivery rates across channels.
+ `NumberOfMediaMessagePartsSent` — Filter by origination identity type to track media message sending by channel.
+ `NumberOfMediaMessagePartsDelivered` — Filter by origination identity type to compare media message delivery across channels.
+ `TextMessagesBlockedByProtect` — Filter by origination identity type to see which channels have messages blocked by Protect rules.
+ `MediaMessagesBlockedByProtect` — Filter by origination identity type to track Protect blocking by channel.

Use the `OriginationIdentityType` dimension with a value of `RCS_AGENT` to isolate metrics for messages sent through your AWS RCS Agent. For more information about the available dimension values, see [RCS metric dimensions](#rcs-monitoring-dimensions).

## RCS metric dimensions
<a name="rcs-monitoring-dimensions"></a>

You can use the following dimensions to filter and group RCS metrics. These dimensions are available for both the new RCS-specific metrics and the modified existing metrics described in the previous sections.

### OriginationIdentityType dimension
<a name="rcs-monitoring-dimensions-origination"></a>

The `OriginationIdentityType` dimension filters metrics by the type of origination identity used to send the message.


**OriginationIdentityType dimension values**  

| Value | Description | 
| --- | --- | 
| PHONE\_NUMBER | Messages sent using a phone number (long code, short code, or toll-free number). | 
| SENDER\_ID | Messages sent using a sender ID. | 
| RCS\_AGENT | Messages sent using an AWS RCS Agent. | 
| POOL | Messages sent using a phone pool. When you send through a pool, AWS End User Messaging selects the appropriate origination identity (AWS RCS Agent or phone number) automatically. | 

### MessageType dimension
<a name="rcs-monitoring-dimensions-messagetype"></a>

The `MessageType` dimension filters metrics by the type of message.


**MessageType dimension values**  

| Value | Description | 
| --- | --- | 
| TEXT | Text messages sent via RCS or SMS. | 
| MEDIA | Media messages (MMS). RCS in AWS End User Messaging currently supports text messages only. | 
| DELIVERY\_REPORT | Delivery report messages confirming message delivery status. | 

**Note**  
The `READ_REPORT` message type is not available because read receipts are not supported in the current release of RCS in AWS End User Messaging.

## Inbound RCS message metrics
<a name="rcs-monitoring-inbound"></a>

The existing `NumberOfMessagesReceived` metric in the `AWS/SMSVoice` namespace now includes inbound RCS messages. You can use the `OriginationIdentityType` dimension with a value of `RCS_AGENT` to filter for inbound messages received through your AWS RCS Agent.

The following dimensions are available for inbound RCS message metrics:
+ `OriginationIdentityType` — Use `RCS_AGENT` to filter for inbound RCS messages.
+ `IsoCountryCode` — Filter by the country code of the inbound message sender.
+ `MessageType` — Use `TEXT` to filter for text messages received via RCS. In the current release, RCS in AWS End User Messaging supports inbound text messages only.

## Monitoring best practices for RCS
<a name="rcs-monitoring-best-practices"></a>

Use the following best practices to monitor your RCS messaging operations and identify delivery issues early.

### Track RCS versus SMS delivery rates
<a name="rcs-monitoring-bp-delivery-rates"></a>

Compare `RCS.MessagesDelivered` against `RCS.MessagesFallenBackToSMS` to understand what percentage of your messages are delivered via RCS versus SMS. A high fallback rate may indicate that many of your recipients are on carriers or devices that don't support RCS. Use the following formulas to calculate key rates:

```
RCS delivery rate = 100 * SUM(RCS.MessagesDelivered) / SUM(RCS.MessagesSent)

SMS fallback rate = 100 * SUM(RCS.MessagesFallenBackToSMS) / SUM(RCS.MessagesSent)
```

Track these rates over time to identify trends as carrier and device support for RCS expands. A decreasing fallback rate indicates that more of your recipients are receiving messages via RCS.

### Set CloudWatch alarms for RCS metrics
<a name="rcs-monitoring-bp-alarms"></a>

Create CloudWatch alarms to alert you when RCS messaging patterns change unexpectedly. Consider setting alarms for the following conditions:
+ **High fallback rate** — Set an alarm when `RCS.MessagesFallenBackToSMS` exceeds a threshold percentage of `RCS.MessagesSent`. A sudden increase in fallback may indicate an issue with your AWS RCS Agent or a carrier outage.
+ **Delivery rate drop** — Set an alarm when the ratio of `RCS.MessagesDelivered` to `RCS.MessagesSent` drops below your expected delivery rate.
+ **Inbound message volume** — If you use two-way RCS messaging, set an alarm on `NumberOfMessagesReceived` (filtered by `OriginationIdentityType = RCS_AGENT`) to detect unexpected changes in inbound message volume.