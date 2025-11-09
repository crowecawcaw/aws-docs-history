# Monitoring AWS End User Messaging SMS with Amazon CloudWatch

You can monitor AWS End User Messaging SMS using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical
information and gain a better perspective on how your web application or service is performing. You can also set
alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

AWS End User Messaging SMS uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts"). A service-linked role is a unique type of IAM role that is
linked directly to AWS End User Messaging SMS. Service-linked roles are predefined by AWS End User Messaging SMS and
include all the permissions that the service requires to call other AWS services on your
behalf. You must create a [service-linked role](using-service-linked-roles.md#using-service-linked-roles.title "using-service-linked-roles.md#using-service-linked-roles.title") for CloudWatch metrics to be collected.

## CloudWatch metrics for AWS End User Messaging SMS

The following sections list the metrics and dimensions for AWS End User Messaging SMS.

###### Important

You must create a [service-linked role](using-service-linked-roles.md#using-service-linked-roles.title "using-service-linked-roles.md#using-service-linked-roles.title") for CloudWatch metrics to be collected.

###### Note

For some metrics, the result may be approximate due to the distributed nature of the
service. In most cases, the count should be close to the actual number of messages
processed.

For AWS End User Messaging SMS, you might want to watch for **TextMessageMonthlySpend**, **MediaMessageMonthlySpend**
and **VoiceMessageMonthlySpend** and trigger an alarm when greater
than, greater than or equal to, or equal to the threshold. The namespace for AWS End User Messaging SMS is
`AWS/SMSVoice`.

###### Topics

- [Message spend metrics](#cw-metrics-message-spend "#cw-metrics-message-spend")
- [Message delivery metrics](#cw-metrics-message-delivery "#cw-metrics-message-delivery")
- [Message conversion metrics](#cw-metrics-message-conversion "#cw-metrics-message-conversion")
- [Protect metrics](#filter-and-monitor-messages-metrics "#filter-and-monitor-messages-metrics")
- [Dimensions](#cw-metrics-message-dimensions "#cw-metrics-message-dimensions")

### Message spend metrics

| Message spend metrics        | Metric                                                                                        | Description | Unit    | Meaningful statistics |
| ---------------------------- | --------------------------------------------------------------------------------------------- | ----------- | ------- | --------------------- |
| **TextMessageMonthlySpend**  | The amount of money (in US Dollars) that you have spent sending SMS messages<br>this month.   | US Dollars  | Maximum |
| **VoiceMessageMonthlySpend** | The amount of money (in US Dollars) that you have spent sending Voice messages<br>this month. | US Dollars  | Maximum |
| **MediaMessageMonthlySpend** | The amount of money (in US Dollars) that you have spent sending MMS messages<br>this month.   | US Dollars  | Maximum |

### Message delivery metrics

The `AWS/SMSVoice` namespace includes the following message delivery
metrics.

| Message delivery metrics               | Metric                                                                                                                            | Description | Unit                                                                   | Meaningful statistics |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------- | --------------------- |
| **NumberOfTextMessagePartsSent**       | Number of text message parts sent. Excludes messages that are blocked by Protect<br>and service limits like message spend limits  | Count       | • Sum<br>• Sample Count<br>• Max<br>• Min<br>• Average<br>• Percentile |
| **NumberOfMediaMessagePartsSent**      | Number of media message parts sent. Excludes messages that are blocked by Protect<br>and service limits like message spend limits | Count       | • Sum<br>• Sample Count<br>• Max<br>• Min<br>• Average<br>• Percentile |
| **NumberOfTextMessagePartsDelivered**  | Number of text message parts delivered to the recipient.                                                                          | Count       | • Sum<br>• Sample Count<br>• Max<br>• Min<br>• Average<br>• Percentile |
| **NumberOfMediaMessagePartsDelivered** | Number of media message parts delivered to the recipient.                                                                         | Count       | • Sum<br>• Sample Count<br>• Max<br>• Min<br>• Average<br>• Percentile |

### Message feedback metrics

The `AWS/SMSVoice` namespace includes the following message feedback
metrics.

| Message feedback metrics                   | Metric                                                                                                                                                                                                                                                                                                                                                                                           | Description | Unit                                 | Meaningful statistics |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ------------------------------------ | --------------------- |
| **NumberOfTextMessagesExpectingFeedback**  | The total number of text messages for which feedback is tracked.<br>\*_NumberOfTextMessagesExpectingFeedback_<br>• will have<br>a value of 1 for each `SendTextMessage` request with<br>MessageFeedbackEnabled enabled.                                                                                                                                                                          | Count       | • Sum<br>• Sample Count<br>• Average |
| **NumberOfMediaMessagesExpectingFeedback** | The total number of media messages for which feedback is<br>tracked.\*_NumberOfMediaMessagesExpectingFeedback_<br>• will have a value of 1<br>for each `SendMediaMessage` request with MessageFeedbackEnabled<br>enabled.                                                                                                                                                                        | Count       | • Sum<br>• Sample Count<br>• Average |
| **NumberOfTextMessagesWithFeedback**       | The total number of text messages for which feedback was tracked and a<br>feedback response was received.**NumberOfTextMessagesWithFeedback\*<br>• will have a value of 1 for each<br>message that receives a feedback. Percentage of messages with feedback can be<br>determined by `100<br>• SUM(**NumberOfTextMessagesWithFeedback**) / SUM(**NumberOfTextMessagesExpectingFeedback\*\*)`     | Count       | • Sum<br>• Sample Count<br>• Average |
| **NumberOfMediaMessagesWithFeedback**      | The total number of media messages for which feedback was tracked and a<br>feedback response was received.**NumberOfMediaMessagesWithFeedback\*<br>• will have a value of 1 for<br>each message that receives a feedback. Percentage of messages with feedback can be<br>determined by `100<br>• SUM(**NumberOfMediaMessagesWithFeedback**) / SUM(**NumberOfMediaMessagesExpectingFeedback\*\*)` | Count       | • Sum<br>• Sample Count<br>• Average |

### Protect metrics in AWS End User Messaging SMS

The `AWS/SMSVoice` namespace includes the following Protect metrics.

| Metric name                       | Description                                                                                                                                                                                                                                                                                                                                    | Unit  | Meaningful Statistics                |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------------------------------ |
| **TextMessagesBlockedByProtect**  | Number of text messages blocked due to country mode block rules.<br>**TextMessagesBlockedByProtect\*<br>• will have a value<br>of 1 if the message is blocked by protect and 0 if the message is not blocked.<br>The percentage of SMS messages blocked by Protect can be determined by `100<br>• AVG(**TextMessagesBlockedByProtect\*\*)`.    | Count | • Sum<br>• Average<br>• Sample Count |
| **MediaMessagesBlockedByProtect** | Number of media messages blocked due to country mode block rules.<br>**MediaMessagesBlockedByProtect\*<br>• will have a value<br>of 1 if the message is blocked by protect and 0 if the message is not blocked.<br>The percentage of MMS messages blocked by Protect can be determined by `100<br>• AVG(**MediaMessagesBlockedByProtect\*\*)`. | Count | • Sum<br>• Average<br>• Sample Count |

### Dimensions

You can use the following dimensions to refine the metrics listed in the previous tables.
These dimensions allow you to filter and group the metrics based on specific attributes of
your SMS and voice messages.

| Dimension                                | Description                                                                                             |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| None                                     | Do not filter                                                                                           |
| IsoCountryCode                           | This dimension filters the data you request by ISO country code                                         |
| MessageFeedbackStatus                    | This dimension filters the data you request by the message feedback status of<br>`RECEIVED` or `FAILED` |
| ProtectConfigurationId                   | This dimension filters the data you request by protect configuration                                    |
| [IsoCountryCode, MessageFeedbackStatus]  | This dimension filters the data you request by ISO country code and message<br>feedback status          |
| [ProtectConfigurationId, IsoCountryCode] | This dimension filters the data you request by protect configuration and ISO<br>country code            |
