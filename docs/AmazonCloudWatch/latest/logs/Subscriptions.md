# Real-time processing of log data with subscriptions

You can use subscriptions to get access to a real-time feed of log events from CloudWatch Logs and
have it delivered to other services such as an Amazon Kinesis stream, an Amazon Data Firehose stream, or
AWS Lambda for custom processing, analysis, or loading to other systems. When log events are
sent to the receiving service, they are base64 encoded and compressed with the gzip
format.

You can also use CloudWatch Logs centralization to replicate log data from multiple accounts and
regions into a central location. For more information, see [Cross-account cross-Region log centralization](CloudWatchLogs_Centralization.md "CloudWatchLogs_Centralization.md").

To begin subscribing to log events, create the receiving resource, such as a Amazon Kinesis Data Streams stream,
where the events will be delivered. A subscription filter defines the filter pattern to use
for filtering which log events get delivered to your AWS resource, as well as information
about where to send matching log events to. Log events are sent to the receiving resource
soon after being ingested, usually less than three minutes.

###### Note

If a log group with a subscription uses log transformation, the filter pattern is
compared to the transformed versions of the log events. For more information, see [Transform logs during ingestion](CloudWatch-Logs-Transformation.md "CloudWatch-Logs-Transformation.md").

You can create subscriptions at the account level and at the log group level. Each account
can have one account-level subscription filter per Region. Each log group can have up to two
subscription filters associated with it.

###### Note

If the destination service returns a retryable error such as a throttling exception or
a retryable service exception (HTTP 5xx for example), CloudWatch Logs continues to retry delivery
for up to 24 hours. CloudWatch Logs doesn't try to re-deliver if the error is a non-retryable
error, such as AccessDeniedException or ResourceNotFoundException. In these cases the
subscription filter is disabled for up to 10 minutes, and then CloudWatch Logs retries sending
logs to the destination. During this disabled period, logs are skipped.

CloudWatch Logs also produces CloudWatch metrics about the forwarding of log events to subscriptions. For
more information, see [Monitoring with CloudWatch metrics](CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md "CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md").

You can also use a CloudWatch Logs subscription to stream log data in near real time to an Amazon OpenSearch Service
cluster. For more information, see [Streaming CloudWatch Logs data to
Amazon OpenSearch Service](CWL_OpenSearch_Stream.md "CWL_OpenSearch_Stream.md").

Subscriptions are supported only for log groups in the Standard log class. For more
information about log classes, see [Log classes](CloudWatch_Logs_Log_Classes.md "CloudWatch_Logs_Log_Classes.md").

###### Note

Subscription filters might batch log events to optimize transmission and reduce the
amount of calls made to the destination. Batching is not guaranteed but is used when
possible.

For batch processing and analysis of log data on a schedule, consider using [Automating log analysis with scheduled queries](ScheduledQueries.md "ScheduledQueries.md"). Scheduled queries run
CloudWatch Logs Insights queries automatically and deliver results to destinations such as Amazon S3 buckets
or Amazon EventBridge event buses.

###### Note

Subscription filters ensure at least one time delivery of events, while duplicate events may occasionally occur.

###### Contents

- [Concepts](subscription-concepts.md "subscription-concepts.md")
- [Log group-level subscription filters](SubscriptionFilters.md "SubscriptionFilters.md")
- [Account-level subscription filters](SubscriptionFilters-AccountLevel.md "SubscriptionFilters-AccountLevel.md")
- [Cross-account cross-Region subscriptions](CrossAccountSubscriptions.md "CrossAccountSubscriptions.md")
- [Confused deputy prevention](Subscriptions-confused-deputy.md "Subscriptions-confused-deputy.md")
- [Log recursion prevention](Subscriptions-recursion-prevention.md "Subscriptions-recursion-prevention.md")
