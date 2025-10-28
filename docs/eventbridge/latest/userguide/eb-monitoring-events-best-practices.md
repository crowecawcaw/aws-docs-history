# Best practices for monitoring event delivery in Amazon EventBridge

To ensure that the business logic in your event-driven applications executes reliably,
it is essential to monitor your event delivery behavior. EventBridge provides metrics that
enable you to monitor, detect, and mitigate issues early to ensure reliable event
delivery. These metrics include:

- Counter-based metrics, such as `InvocationAttempts`,
  `SuccessfulInvocationAttempts`,
  `RetryInvocationAttempts` and `FailedInvocations`, to
  enable you to observe target throttling, and calculate error rates.
- Latency-based metrics, such as `IngestionToInvocationSuccessLatency`, to provide
  insights into event delivery and delays.
  These metrics allow you to monitor the health of your event-driven architectures, and
  to understand and mitigate event delivery issues caused by underperforming, undersized,
  or unresponsive targets. For example, a permanently under-scaled or throttled target can
  lead to excessive retries, delays in event delivery, and permanent delivery
  failures.

We recommend you combine multiple metrics to get a holistic overview, and closely
monitor them. Setting up appropriate alarms and dashboards enables you to address
persistent issues early.

For information on specific metrics, see [EventBridge metrics](eb-monitoring.md#eb-metrics "eb-monitoring.md#eb-metrics").

## Detecting event delivery failures

EventBridge includes metrics you can configure to report target invocations--that is, event delivery attempts--per rule.

We recommend you monitor the following metrics at the rule level:

- `InvocationAttempts` to observe the total number of times EventBridge attempts to invoke
  the target, including event delivery retries.
- `SuccessfulInvocationAttempts` for the number of invocation attempts where EventBridge successfully delivered the event to the target.
- `RetryInvocationAttempts` for the number attempts that represent event
  delivery retries.

An increase in `RetryInvocationAttempts` may be an early
indication of an undersized target.

In addition, since increased retry attempts can be a first sign of delivery
issues, we also recommend creating a single metric that tracks the percentage of
successful target invocations to all target invocations. For example, in CloudWatch you
can use metric math to create such a metric, called
`SuccessfulInvocationRate`, using the following formula:

`SuccessfulInvocationRate` = `SuccessfulInvocationAttempts` / `InvocationAttempts`

Then, depending on your requirements, you can configure CloudWatch Alarms to create
notifications when a certain threshold is hit.

Although an occasional decrease of `SuccessfulInvocationRate` due to temporary traffic spikes or invocation errors can be considered normal, a constant mismatch is an indication of a misconfigured target and needs to be addressed as part of the shared responsibility model.

For more information on metric math, see [Using math
expressions with CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md "../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md") in the _Amazon CloudWatch User
Guide_.

By default, EventBridge retries delivering an event for 24 hours and up to 185 times.
After EventBridge exhausts these retry attempts, EventBridge either drops the event, or sends it
to a dead-letter queue if one has been specified. For more information, see [Retrying event delivery](eb-rule-retry-policy.md "eb-rule-retry-policy.md"). To
avoid losing events if they fail to be delivered, we recommend you configure a
dead-letter queue for each rule target. For more information, For more information,
see [Using dead-letter queues](eb-rule-dlq.md "eb-rule-dlq.md").

Events that EventBridge fails to deliver to the specified target are reported in the
`FailedInvocations` metric and the `InvocationsSentToDlq`
metric if you have configured a dead-letter queue for the target. If your
application is experiencing a large number of `FailedInvocations` or
`InvocationsSentToDlq` reports, we recommend you investigate if the
target is properly scaled and able to receive the given traffic.

## Detecting event delivery delays

EventBridge also provides a metric that lets you observe the end-to-end latency--the time it takes from event ingestion to successful delivery to the target. This can be achieved with the `IngestionToInvocationSuccessLatency` metric. This metric surfaces effects from retries and delayed delivery, for example due to timeouts and slow responses from targets. `IngestionToInvocationSuccessLatency` includes the time the target takes to successfully respond to event delivery. This allows you to monitor the end-to-end latency between EventBridge and your target, and detect performance variations and degradations of targets, even when there is no target throttling or errors.
