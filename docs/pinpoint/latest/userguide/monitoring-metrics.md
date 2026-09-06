

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Amazon Pinpoint metrics that are exported to CloudWatch
<a name="monitoring-metrics"></a>

The following topics describe the metrics that Amazon Pinpoint exports to CloudWatch.

**Topics**
+ [Metrics related to message delivery](#monitoring-metrics-delivery)
+ [Metrics related to endpoints](#monitoring-metrics-endpoints)
+ [Metrics related to import jobs](#monitoring-metrics-import-jobs)
+ [Metrics related to one-time passwords](#monitoring-metrics-one-time-passwords)
+ [Metrics related to events](#monitoring-metrics-events)

## Metrics related to message delivery
<a name="monitoring-metrics-delivery"></a>



| Metric | Description | 
| --- | --- | 
| `DirectSendMessagePermanentFailure` | The number of messages that weren't sent because of a permanent issue.<br />This type of issue usually occurs when an endpoint is expired or invalid. When this type of issue occurs, Amazon Pinpoint doesn't attempt to redeliver the message.<br />Units: *Count*<br />Dimensions: ApplicationId, Channel | 
| `DirectSendMessageTemporaryFailure` | The number of direct messages that failed to send because of a temporary issue.<br />This type of issue usually indicates that an internal issue with the Amazon Pinpoint service prevented the message from being sent. When this type of issue occurs, Amazon Pinpoint doesn't attempt to redeliver the message.<br />Units: *Count*<br />Dimensions: ApplicationId, Channel | 
| `CampaignSendMessagePermanentFailure` | The number of campaign messages that weren't sent because of a permanent issue. <br />This type of issue usually occurs when an endpoint token is expired or invalid. <br />Units: *Count*<br />Dimensions: ApplicationId, Channel | 
| `CampaignSendMessageTemporaryFailure` | The number of messages that a campaign attempted to send, but that weren't sent because of a temporary issue.<br />This type of issue usually indicates that an internal issue with the Amazon Pinpoint service prevented the message from being sent. When this type of issue occurs, Amazon Pinpoint doesn't attempt to redeliver the message.<br />Units: *Count*<br />Dimensions: ApplicationId, Channel | 
| `DirectSendMessageThrottled` | The number of direct messages that weren't sent because your account's ability to send messages was throttled.<br />Units: *Count*<br />Dimensions: ApplicationId, Channel | 
| `CampaignSendMessageThrottled` | The number of campaign messages that weren't sent because your account's ability to send messages was throttled.<br />Units: *Count*<br />Dimensions: ApplicationId, Channel | 
| `CampaignSendMessageLatency` | The amount of time, in seconds, that passed between the time when the campaign started running and the time when it finished running.<br />Units: *Count*<br />Dimensions: ApplicationId, Channel | 

## Metrics related to endpoints
<a name="monitoring-metrics-endpoints"></a>



| Metric | Description | 
| --- | --- | 
| `EndpointRegistrationFailure` | The number of endpoint registrations submitted through an AWS SDK or the Amazon Pinpoint API that couldn't be imported. <br />This type of issue usually occurs when an incoming endpoint record is invalid.<br />Units: *Count*<br />Dimensions: ApplicationId | 

## Metrics related to import jobs
<a name="monitoring-metrics-import-jobs"></a>



| Metric | Description | 
| --- | --- | 
| `ImportedEndpointFailure` | The number of endpoints in an import job that couldn't be imported because they were invalid.<br />Units: *Count*<br />Dimensions: ApplicationId | 
| `ImportJobFailure` | The number of import jobs that couldn't be completed for any reason.<br />Units: *Count*<br />Dimensions: ApplicationId | 
| `ImportJobDuration` | The amount of time, in seconds, that elapsed between the beginning and the end of each import job.<br />Units: *Count*<br />Dimensions: ApplicationId | 

## Metrics related to one-time passwords
<a name="monitoring-metrics-one-time-passwords"></a>



| Metric | Description | 
| --- | --- | 
| `OTPVerificationSuccess` | The number of One-Time Password (OTP) verification requests that succeeded.<br />Units: *Count*<br />Dimensions: ApplicationId | 
| `OTPVerificationAttempt` | The total number of attempts to verify an OTP.<br />Units: *Count*<br />Dimensions: ApplicationId | 
| `OTPVerificationFailure` | The total number of OTP verification requests that failed.<br />Units: *Count*<br />Dimensions: ApplicationId | 
| `OTPVerificationFailureFinalAttempt` | The total number of OTP verification requests that failed on the final attempt.<br />Units: *Count*<br />Dimensions: ApplicationId | 

## Metrics related to events
<a name="monitoring-metrics-events"></a>



| Metric | Description | 
| --- | --- | 
| `TotalEvents` | The total number of events that Amazon Pinpoint recorded. This metric includes events that were recorded by AWS SDKs or by the Amazon Pinpoint API.<br />Units: *Count*<br />Dimensions: ApplicationId | 
| `ExportedEvents` | The total number of events that were successfully written to the event stream for exporting.<br />Units: *Count*<br />Dimensions: ApplicationId | 
| `ExportEventErrors` | The total number of errors that occurred after writing to the event stream. These errors can include issues that aren't related to Amazon Pinpoint. <br />For example, this error could occur when the volume of events that you stream to Firehose exceeds your provisioned throughput.<br />Units: *Count*<br />Dimensions: ApplicationId, ErrorCode | 