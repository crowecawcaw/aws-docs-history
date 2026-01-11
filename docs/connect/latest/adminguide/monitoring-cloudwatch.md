# Monitoring your Amazon Connect instance using CloudWatch

Amazon Connect sends data about your instance to CloudWatch metrics so that you can collect, view, and
analyze CloudWatch metrics for your Amazon Connect virtual contact center. You can use this data to monitor key
operational metrics and set up alarms. Data about your contact center is sent to CloudWatch every 1
minute.

When you view the CloudWatch metrics dashboard, you can specify the refresh interval for the data
displayed. The values displayed in the dashboard reflect the values for the refresh interval you
define. For example, if you set the refresh interval to 1 minute, the values displayed are for a
minute period. You can select a refresh interval of 10 seconds, but Amazon Connect does not send data
more often than every 1 minute. Metrics that are sent to CloudWatch are available for two weeks, and
then discarded. To learn more about metrics in CloudWatch, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Note

If your Amazon Connect instance was created on or before October 2018, you need to provide Amazon Connect
with permission to begin publishing chat metrics to your CloudWatch account. To do so, create an
IAM policy with the following permission and attach it to the Amazon Connect service role. You can
find the Amazon Connect service role on the **Account overview** page for your Amazon Connect
instance.

```
{
  "Effect": "Allow",
  "Action": "cloudwatch:PutMetricData",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "cloudwatch:namespace": "AWS/Connect"
    }
  }
}
```

## Amazon Connect metrics sent to CloudWatch

The `AWS/Connect` namespace includes the following metrics.

| Metric                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CallsBreachingConcurrencyQuota  | The total number of voice calls that exceeded the concurrent calls quota for the<br>instance. For the total number of<br>calls that breach the quota, take a look at the Sum statistic.<br>For example, assume your contact center experiences the following volumes, and<br>your service quota is 100 concurrent calls:<br>• 0:00 : 125 concurrent calls. This is 25 over the quota.<br>• 0:04 : 135 concurrent calls. This is 35 over the quota.<br>• 0:10 : 150 concurrent calls. This is 50 over the quota.<br>CallsBreachingConcurrencyQuota = 110: the total number of voice calls that<br>exceeded the quota between 0:00 and 0:10.<br>Unit: Count<br>Dimension:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **VoiceCalls**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| CallBackNotDialableNumber       | The number of times a queued callback to a customer could not be dialed because<br>the customer's number is in a country for which outbound calls are not allowed for<br>the instance. The countries allowed for an instance are defined by the service<br>quotas.<br>Unit: Count<br>Dimensions:<br>• **InstanceId** The ID of your instance<br>• **MetricGroup**: **ContactFlow**<br>• **ContactFlowName**: The name of your flow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| CallRecordingUploadError        | The number of call recordings that failed to upload to the Amazon S3 bucket<br>configured for your instance. This is the bucket specified in **Data<br>Storage\*<br>• > **Call Recordings\*<br>• settings for the<br>instance.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **CallRecordings**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| CallsPerInterval                | The number of voice calls, both inbound and outbound, received or placed per<br>second in the instance.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **VoiceCalls**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ChatsBreachingActiveChatQuota   | The total number of valid requests made to start a chat that exceeded the<br>concurrent active chats quota for the instance. For the total number of chats<br>requests that breach the quota, take a look at the Sum statistic.<br>For example, assume your contact center experiences the following volumes, and<br>your service quota is 2500 concurrent active chats:<br>• 0:00 : 2525 concurrent active chats. This is 25 over the quota.<br>• 0:04 : 2535 concurrent active chats. This is 35 over the quota.<br>• 0:10 : 2550 concurrent active chats. This is 50 over the quota.<br>ChatsBreachingActiveChatsQuota = 110: the total number of chats that exceeded<br>the quota between 0:00 and 0:10.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Chats**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ConcurrentActiveChats           | The number of [concurrent active<br>chats](amazon-connect-service-limits.md "amazon-connect-service-limits.md") in the instance at the time the data is displayed in the dashboard.<br>The value displayed for this metric is the number of concurrent active chats at the<br>time the dashboard is displayed, and not a sum for the entire interval of the<br>refresh interval set. All active chats are included, not only active chats that are<br>connected to agents.<br>While all statistics are available in CloudWatch for concurrent active chats, you<br>might be most interested in looking at the Maximum/Average statistic. The Sum<br>statistic isn't as useful here.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Chats**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ConcurrentActiveChatsPercentage | The percentage of the concurrent active chats service quota used in the<br>instance. This is calculated by:<br>• ConcurrentActiveChats / ConfiguredConcurrentActiveChatsLimit<br>Where ConfiguredConcurrentActiveChatsLimit is the Concurrent active chats per<br>instance configured for your instance.<br>Unit: Percent (Output displays as an integer. For example, 1% of chats is shown<br>as 1, not as 0.01.)<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Chats**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ConcurrentCalls                 | The number of concurrent active voice calls in the instance at the time the data<br>is displayed in the dashboard. The value displayed for this metric is the number of<br>concurrent active calls at the time the dashboard is displayed, and not a sum for<br>the entire interval of the refresh interval set. All active voice calls are<br>included, not only active calls that are connected to agents.<br>While all statistics are available in CloudWatch for concurrent voice calls you might<br>be most interested in looking at the Maximum/Average statistic. The Sum statistic<br>isn't as useful here.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **VoiceCalls**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ConcurrentCallsPercentage       | The percentage of the concurrent active voice calls service quota used in the<br>instance. This is calculated by:<br>• ConcurrentCalls / ConfiguredConcurrentCallsLimit<br>Unit: Percent (output displays as a decimal)<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **VoiceCalls**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ConcurrentEmails                | This is the total of all email contacts in an Amazon Connect instance in an active state.<br>An email contact in an active state includes:<br>• emails that are currently executing through a flow<br>• emails waiting in queue waiting to be assigned<br>• emails assigned to agents (either actively being worked on or in ACW<br>state)<br>• email replies or agent-initiated emails being composed by agents or<br>automated services<br>Example: 200 emails in queue + 10 emails assigned to 10 agents + 5 outbound<br>emails being sent by an agent (either a reply or agent-initiated) = 215 Concurrent<br>active emails in the instance<br>NoteData for ConcurrentEmails is sent to CloudWatch every 5 minutes.<br>The number of concurrent active<br>emails in the instance at the time the data is<br>displayed in the dashboard. The value displayed for this metric is the number of<br>concurrent active emails at the time the dashboard is displayed, and not a sum for<br>the entire interval of the refresh interval set. All active email are included, not<br>only active emails that are connected to agents.<br>While all statistics are available in CloudWatch for concurrent emails you might<br>be most interested in looking at the Maximum/Average statistic. The Sum statistic<br>isn't as useful here.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Email** |
| ConcurrentEmailsPercentage      | The percentage of concurrent active emails service quota used in the instance.<br>This is calculated by:<br>ConcurrentEmails / ConfiguredConcurrentEmailsLimit<br>Where ConfiguredConcurrentEmailsLimit is the [Concurrent active emails per instance](amazon-connect-service-limits.md#connect-quotas "amazon-connect-service-limits.md#connect-quotas") configured for your instance. We<br>recommend following the Amazon Connect [ongoing operations<br>management](plan-ahead-quotas.md#production-environment-go-live-quotas "plan-ahead-quotas.md#production-environment-go-live-quotas") approach of configuring alerts at 80% of quota limits to notify<br>you when to [request a quota<br>increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md").<br>NoteData for ConcurrentEmailsPercentage is sent to CloudWatch every 5<br>minutes.<br>While all statistics are available in CloudWatch for concurrent emails you might<br>be most interested in looking at the Maximum/Average statistic. The Sum statistic<br>isn't as useful here.<br>Unit: Percentage<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Email**                                                                                                                                                                                   |
| ConcurrentTasks                 | NoteData for ConcurrentTasks is sent to CloudWatch every 5 minutes.<br>The number of concurrent active tasks in the instance at the time the data is<br>displayed in the dashboard. The value displayed for this metric is the number of<br>concurrent active tasks at the time the dashboard is displayed, and not a sum for<br>the entire interval of the refresh interval set. All active tasks are included, not<br>only active tasks that are connected to agents.<br>While all statistics are available in CloudWatch for concurrent tasks you might be<br>most interested in looking at the Maximum/Average statistic. The Sum statistic isn't<br>as useful here.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Tasks**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ConcurrentTasksPercentage       | NoteData for ConcurrentTasksPercentage is sent to CloudWatch every 5<br>minutes.<br>The percentage of the concurrent active tasks service quota used in the<br>instance. This is calculated by:<br>• ConcurrentTasks / ConfiguredConcurrentTasksLimit<br>Where ConfiguredConcurrentTasksLimit is the [Concurrent tasks per instance](amazon-connect-service-limits.md "amazon-connect-service-limits.md")<br>configured for your instance.<br>Unit: Percentage<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Tasks**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ContactFlowErrors               | The number of times the error branch for a flow was run.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **ContactFlow**<br>• **ContactFlowName**: The name of your flow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ContactFlowFatalErrors          | The number of times a flow failed to execute due to a system error.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **ContactFlow**<br>• **ContactFlowName**: The name of your flow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| LongestQueueWaitTime            | The longest amount of time, in seconds, that a contact waited in a queue. This<br>is the length of time a contact waited in a queue during the refresh interval<br>selected in the CloudWatch dashboard, such as 1 minute or 5 minutes.<br>Unit: Seconds<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Queue**<br>• **QueueName**: The name of your queue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| MissedCalls                     | The number of voice calls that were missed by agents during the refresh interval<br>selected, such as 1 minute or 5 minutes. A missed call is one that is not answered<br>by an agent within 20 seconds.<br>To monitor the total missed calls in a given time period, take a look at the Sum<br>statistic in CloudWatch.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **VoiceCalls**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| MisconfiguredPhoneNumbers       | The number of calls that failed because the phone number is not associated with<br>a flow.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **VoiceCalls**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PublicSigningKeyUsage           | The number of times a flow security key (public signing key) was used to encrypt<br>customer input in a flow.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **SigningKeyId**: The ID of your signing key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| QueueCapacityExceededError      | The number of calls that were rejected because the queue was full.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Queue**<br>• **QueueName**: The name of your queue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| QueueSize                       | The number of contacts in the queue. The value reflects the number of contacts<br>in the queue at the time the dashboard is accessed, not for the duration of the<br>reporting interval.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Queue**<br>• **QueueName**: The name of your queue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SuccessfulChatsPerInterval      | The number of chats successfully started in the instance for the defined<br>interval.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Chats**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TasksBreachingConcurrencyQuota  | The total number of tasks that exceeded the concurrent tasks quota for the<br>instance. For the total number of tasks that breach the quota, take a look at the<br>Sum statistic.<br>For example, assume your contact center experiences the following volumes, and<br>your service quota is 2500 concurrent tasks:<br>• 0:00 : 2525 concurrent tasks. This is 25 over the quota.<br>• 0:04 : 2535 concurrent tasks. This is 35 over the quota.<br>• 0:10 : 2550 concurrent tasks. This is 50 over the quota.<br>TasksBreachingConcurrencyQuota = 110: the total number of tasks that exceeded<br>the quota between 0:00 and 0:10.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Tasks**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| TasksExpired                    | Tasks which have expired after being active for 7 days.<br>To monitor the total number of tasks that have expired in a given time period,<br>take a look at the Sum statistic in CloudWatch.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Tasks**<br>• **ContactId**: The ID of the task contact                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| TasksExpiryWarningReached       | Tasks that have been active for 6 days 22 hours and reached expiry warning<br>limit.<br>To monitor the total number of tasks that have reached expiry warning limit in a<br>given time period, take a look at the Sum statistic in CloudWatch.<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **Tasks**<br>• **ContactId**: The ID of the task contact                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ThrottledCalls                  | The number of voice calls that were rejected because the rate of calls per<br>second exceeded the maximum supported quota. To increase the supported rate of<br>calls, request an increase in the service quota for concurrent active calls per<br>instance.<br>To monitor the total throttled calls in a given time period, take a look at the<br>Sum statistic in CloudWatch.<br>Unit: Seconds<br>Unit: Count<br>Dimensions:<br>• **InstanceId**: The ID of your instance<br>• **MetricGroup**: **VoiceCalls**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ToInstancePacketLossRate        | The ratio of packet loss for calls in the instance, reported every 10 seconds.<br>Each data point is between 0 and 100. The ratio of packet loss for calls in the<br>instance appears as a percent between 0 and 1.<br>Unit: Percent<br>Dimensions:<br>• **Participant**: **Agent**<br>• **Type of Connection**: **WebRTC**<br>• **Instance ID**: The ID of your instance<br>• **Stream Type**: **Voice**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Amazon Connect CloudWatch metrics dimensions

In CloudWatch, a dimension is a name/value pair that uniquely identifies a metric. In the
dashboard, metrics are grouped by dimension. When you view metrics in the dashboard, only
metrics with data are displayed. If there is no activity during the refresh interval for which
there is a metric, then no data from your instance is displayed in the dashboard.

The following dimensions are used in the CloudWatch dashboard for Amazon Connect metrics.

### Flow metrics dimension

###### Note

Flow names must contain only the following characters in order for the names to be displayed
in CloudWatch: alphanumeric characters (0-9A-Za-z) . , - \_ / # : $ @ | & { } + ? % and
the space character.

Filters metric data by flow. Includes the following metrics:

- ContactFlowErrors
- ContactFlowFatalErrors
- PublicSigningKeyUsage

### Contact metrics dimension

Filters metric data by contacts. Includes the following metrics:

- TasksExpiryWarningReached
- TasksExpired

### Instance metrics dimension

Filters meta data by instance. Includes the following metrics:

- CallsBreachingConcurrencyQuota
- CallsPerInterval
- CallRecordingUploadError
- ChatsBreachingActiveChatQuota
- ConcurrentActiveChats
- ConcurrentActiveChatsPercentage
- ConcurrentCalls
- ConcurrentCallsPercentage
- ConcurrentEmails
- ConcurrentEmailsPercentage
- ConcurrentTasks
- ConcurrentTasksPercentage
- MisconfiguredPhoneNumbers
- MissedCalls
- SuccessfulChatsPerInterval
- TasksBreachingConcurrencyQuota
- ThrottledCalls

### Instance ID, Participant, Stream Type, Type of

Connection

Filters metric data by connection. Includes the following metrics:

- ToInstancePacketLossRate

### Queue metrics dimension

###### Note

Queue names must contain only the following characters in order for the names to be displayed
in CloudWatch: alphanumeric characters (0-9A-Za-z) . , - \_ / # : $ @ | & { } + ? % and
the space character.

Filters metric data by queue. Includes the following metrics:

- CallBackNotDialableNumber
- LongestQueueWaitTime
- QueueCapacityExceededError
- QueueSize

## Amazon Connect Voice ID metrics sent to CloudWatch

The `VoiceID` namespace includes the following metrics.

**RequestLatency**

The elapsed time for the request.

Frequency: 1 minute

Unit: Milliseconds

Dimension: API

**UserErrors**

The number of Error counts due to bad requests from user.

Frequency: 1 minute

Unit: Count

Dimension: API

**SystemErrors**

The number of Error counts due to internal service error.

Frequency: 1 minute

Unit: Count

Dimension: API

**Throttles**

The number of requests that are rejected due to exceeding the max rate allowed for
sending requests.

Frequency: 1 minute

Unit: Count

Dimension: API

**ActiveSessions**

The number of active sessions in the domain. Active sessions are sessions that are
in pending or ongoing status.

Frequency: 1 minute

Unit: Count

Dimension: Domain

**ActiveSpeakerEnrollmentJobs**

The number of active Batch Enrollment Jobs in the domain. Active Jobs are those
which are in Pending or InProgress status.

Frequency: 15 minutes

Unit: Count

Dimension: Domain

**ActiveFraudsterRegistrationJobs**

The number of active Batch Registration Jobs in the domain. Active Jobs are those
which are in Pending or InProgress status.

Frequency: 15 minutes

Unit: Count

Dimension: Domain

**Speakers**

The number of Speakers in the domain.

Frequency: 15 minutes

Unit: Count

Dimension: Domain

**Fraudsters**

The number of Fraudsters in the domain.

Frequency: 15 minutes

Unit: Count

Dimension: Domain

## Amazon Connect Voice ID metrics dimensions

The following dimensions are used in the CloudWatch dashboard for Amazon Connect Voice ID metrics. When
you view metrics in the dashboard, only metrics with data are displayed. If there is no
activity during the refresh interval for which there is a metric, then no data from your
instance is displayed in the dashboard.

### API metrics dimension

This dimension limits the data to one of the following Voice ID operations:

- DeleteFraudster
- EvaluateSession
- ListSpeakers
- DeleteSpeaker
- OptOutSpeaker

### Domain metrics dimension

The Voice ID domain where the enrollment, authentication or registration is conducted.

## Amazon AppIntegrations metrics sent to

CloudWatch

The `AWS/AppIntegrations` namespace includes the following metrics.

**RecordsDownloaded**

The number of records that were successfully downloaded as part of an AppFlow flow
execution for a data integration.

Frequency: 1 minute

Unit: Count

Valid Statistics: Maximum, Sum, Minimum, Average

**RecordsFailed**

The number of records that failed to download as part of an AppFlow flow execution
for a data integration.

Frequency: 1 minute

Unit: Count

Valid Statistics: Maximum, Sum, Minimum, Average

**DataDownloaded**

The number of bytes that were successfully downloaded as part of an AppFlow flow
execution for a data integration.

Frequency: 1 minute

Unit: Bytes

Valid Statistics: Maximum, Sum, Minimum, Average

**DataProcessingDuration**

The time it took to process and download data as part of a single AppFlow flow
execution for a data integration.

Frequency: 1 minute

Unit: Milliseconds

Valid Statistics: Maximum, Sum, Minimum, Average

**EventsReceived**

The number of events that were successfully emitted from your third-party source
application (Salesforce, Zendesk) and received on your event bus.

Frequency: 1 minute

Unit: Count

Valid Statistics: Maximum, Sum, Minimum, Average

**EventsProcessed**

The number of events that were successfully processed and forwarded to be evaluated
against the rules you configured on an event integration.

Frequency: 1 minute

Unit: Count

Valid Statistics: Maximum, Sum, Minimum, Average

**EventsThrottled**

The number of events that were throttled because the rate of emitting events
exceeded the maximum supported quota.

Frequency: 1 minute

Unit: Bytes

Valid Statistics: Maximum, Sum, Minimum, Average

**EventsFailed**

The number of events that failed to process due to malformed or unsupported
third-party events, and other processing errors .

Frequency: 1 minute

Unit: Bytes

Valid Statistics: Maximum, Sum, Minimum, Average

**EventProcessingDuration**

The time it took to successfully process and forward an event to be evaluated
against the rules you configured on an event integration.

Frequency: 1 minute

Unit: Milliseconds

Valid Statistics: Maximum, Sum, Minimum, Average

## Amazon AppIntegrations metric

dimensions

You can use the following dimensions to refine AppIntegrations [metrics](#appintegrations-metrics-cloudwatch "#appintegrations-metrics-cloudwatch").

| Dimension       | Description                             |
| --------------- | --------------------------------------- |
| AccountId       | AWS account ID                          |
| ClientId        | Service principal of the client         |
| IntegrationARN  | ARN of the event or data integration    |
| IntegrationType | DataIntegration or EventIntegration     |
| Region          | Region of the data or event integration |

## Amazon Connect Customer Profiles

metrics

The `AWS/CustomerProfiles` namespace includes the following metrics.

**Real-time export metrics sent to CloudWatch**

The two following metrics will be published to CloudWatch for every export task. These metrics
will provide information on your export stream tasks and will allow you to configure your
Kinesis streams based on your use case. In the case of being throttled, these metrics will
enable you to provision your Kinesis stream to ensure delivery to your destination.

**EventsProcessed**

Number of records successfully streamed into a Kinesis Stream.

Unit: Count

**EventsThrottled**

Number of PutRecord attempts that encountered throttling exception.

Unit: Count

## Amazon Connect Customer Profiles

metric dimensions

You can use the following dimensions to refine Customer Profiles [metrics](#customer-profiles-metrics-cloudwatch "#customer-profiles-metrics-cloudwatch").

| Dimension       | Description                                                                       |
| --------------- | --------------------------------------------------------------------------------- |
| DomainName      | Customer Profiles domain name                                                     |
| DestinationType | Type of destination. Available value is: Kinesis                                  |
| DestinationName | Name of destination. Kinesis Data Streaming name for DestinationType:<br>Kinesis. |

## Use CloudWatch metrics to calculate

concurrent call quota

###### Important

The **ConcurrentCallsPercentage** calculation information is not the
same as **ConcurrentTasksPercentage** and
**ConcurrentChatPercentage**.

- The metrics emitted for **ConcurrentCallsPercentage** are in
  decimal and not multiplied by 100. The metric represents a percentage of your total
  quota.
- For **ConcurrentTasksPercentage** and
  **ConcurrentChatPercentage** the value is multiplied by 100. That
  gives you your total quota.
- The metrics emitted are correct and there is no discrepancy in data.

Here's how to calculate your quota usage for concurrent calls.

With calls active in the system, look at **ConcurrentCalls** and
**ConcurrentCallsPercentage**. Calculate how much of your quota has been
used:

- (ConcurrentCalls / ConcurrentCallsPercentage)

For example, if **ConcurrentCalls** is 20 and
**ConcurrentCallsPercentage** is 50, your quota usage is calculated as
(20/0.5) = 40. Your total quota is 40 calls.

## Use CloudWatch metrics to calculate

concurrent active chats quota

Here's how to calculate your quota for concurrent active chats.

With chats active in the system, look at **ConcurrentActiveChats** and
**ConcurrentChatsPercentage**. Calculate the quota:

- (ConcurrentActiveChats / ConcurrentActiveChatsPercentage) \* 100

For example, if **ConcurrentActiveChats** is 1000 and
**ConcurrentActiveChatsPercentage** is 50, your quota is calculated as
(1000/50)\*100 = 2000. Your total quota is 2000 chats.

## Use CloudWatch metrics to calculate

concurrent task quota

Here's how to calculate your quota for concurrent tasks.

With tasks active in the system, look at **ConcurrentTasks** and
**ConcurrentTasksPercentage**. Calculate the quota:

- (ConcurrentTasks / ConcurrentTasksPercentage)\*100

For example, if **ConcurrentTasks** is 20 and
**ConcurrentTasksPercentage** is 50, your total quota is calculated as
(20/50)\*100= 40. Your total quota is 40 tasks.

## Use CloudWatch metrics to calculate

concurrent email quota

Here's how to calculate your quota for concurrent email.

With email active in the system, look at **ConcurrentEmails** and
**ConcurrentEmailsPercentage**. Calculate the quota:

- (ConcurrentEmails / ConcurrentEmailsPercentage)\*100

For example, if **ConcurrentEmails** is 20 and
**ConcurrentEmailsPercentage** is 50, your total quota is calculated as
(20/50)\*100= 40. Your total quota is 40 emails.
