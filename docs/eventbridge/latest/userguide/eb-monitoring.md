# Monitoring Amazon EventBridge

EventBridge sends metrics to Amazon CloudWatch every minute for everything from the number of matched [events](eb-events.md "eb-events.md")
to the number of times a [target](eb-targets.md "eb-targets.md") is invoked by a [rule](eb-rules.md "eb-rules.md").

The following video reviews monitoring and auditing EventBridge behavior through CloudWatch:

###### Topics

- [EventBridge metrics](#eb-metrics "#eb-metrics")
- [Dimensions for EventBridge metrics](#eb-metrics-dimensions "#eb-metrics-dimensions")
- [Best practices for monitoring event delivery in Amazon EventBridge](eb-monitoring-events-best-practices.md "eb-monitoring-events-best-practices.md")
- [EventBridge is the evolution of Amazon CloudWatch Events](eb-cwe-now-eb.md "eb-cwe-now-eb.md")

## EventBridge metrics

The `AWS/Events` namespace includes the following metrics.

For the metrics that use Count as a unit, Sum and SampleCount tend to be the most
useful statistics.

Metrics that specify only the `RuleName` dimension refer to the default event bus.
Metrics that specify both the `EventBusName` and `RuleName` dimensions refer to a custom event bus.

| Metric                                 | Description                                                                                                                                                                                                                                                                                                                                  | Dimensions                              | Units        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ------------ |
| `DeadLetterInvocations`                | The number of times a rule’s target isn't invoked in response to<br>an event. This includes invocations that would result in running the<br>same rule again, causing an infinite loop.                                                                                                                                                       | RuleName                                | Count        |
| `Events`                               | The number of partner events ingested by EventBridge.                                                                                                                                                                                                                                                                                        | EventSourceName                         | Count        |
| `FailedInvocations`                    | The number of invocations that failed permanently. This doesn't<br>include invocations that are retried or invocations that succeeded<br>after a retry attempt. It also doesn't count failed invocations that<br>are counted in `DeadLetterInvocations`.<br>NoteEventBridge only sends this metric to CloudWatch if it isn't zero.           | RuleName                                | Count        |
| `Invocations`                          | The number of times a target is invoked by a rule in response to<br>an event. This includes successful and failed invocations, but<br>doesn't include throttled or retried attempts until they fail<br>permanently. It doesn't include<br>`DeadLetterInvocations`.<br>NoteEventBridge only sends this metric to CloudWatch if it isn't zero. | None, RuleName                          | Count        |
| `InvocationAttempts`                   | Number of times EventBridge attempted invoking a target.                                                                                                                                                                                                                                                                                     | EventBusName, None, RuleName            | Count        |
| `InvocationsCreated`                   | The total number of invocations created in response to each event.<br>This metric is often used to monitor utilization of the<br>**Invocations throttle limit in transactions per<br>second**<br>[EventBridge service quota](eb-quota.md#eb-limits "eb-quota.md#eb-limits").                                                                 | None                                    | Count        |
| `InvocationsFailedToBeSentToDlq`       | The number of invocations that couldn't be moved to a dead-letter<br>queue. Dead-letter queue errors occur due to permissions errors,<br>unavailable resources, or size limits.<br>NoteEventBridge only sends this metric to CloudWatch if it isn't zero.                                                                                    | RuleName                                | Count        |
| `IngestiontoInvocationCompleteLatency` | The time taken from event ingestion to completion of the first<br>invocation attempt.                                                                                                                                                                                                                                                        | EventBusName, None, RuleName            | Milliseconds |
| `IngestionToInvocationSuccessLatency`  | The time taken from event ingestion to successful target delivery, using the invocation end time as cutoff.<br>This metric is only emitted after the first successful delivery attempt to the target.                                                                                                                                        | EventBusName, None, RuleName            | Milliseconds |
| `IngestiontoInvocationStartLatency`    | The time to process events, measured from when an event is<br>ingested by EventBridge to the first invocation of a target.                                                                                                                                                                                                                   | EventBusName, None, RuleName            | Milliseconds |
| `InvocationsSentToDlq`                 | The number of invocations that are moved to a dead-letter<br>queue.<br>NoteEventBridge only sends this metric to CloudWatch if it isn't zero.                                                                                                                                                                                                | RuleName                                | Count        |
| `MatchedEvents`                        | If EventBusName or EventSourceName is specified, the number of events that matched with any rule.<br>If RuleName is specified, the number of events that matched with a specific rule.                                                                                                                                                       | EventBusName, EventSourceName, RuleName | Count        |
| `RetryInvocationAttempts`              | Number of times target invocation has been retried.<br>NoteEventBridge only sends this metric to CloudWatch if it isn't zero.                                                                                                                                                                                                                | EventBusName, None, RuleName            | Count        |
| `SuccessfulInvocationAttempts`         | Number of times target was successfully invoked.                                                                                                                                                                                                                                                                                             | EventBusName, None, RuleName            | Count        |
| `ThrottledRules`                       | The number of times rule execution was throttled. Invocations for<br>those rules may be delayed.<br>For more information, see **Invocations throttle limit in transactions per second**<br>in [EventBridge event bus quotas](eb-quota.md#eb-limits "eb-quota.md#eb-limits").                                                                 | EventBusName, None, RuleName            | Count        |
| `TriggeredRules`                       | The number of rules that have run and matched with any event.<br>You won't see this metric in CloudWatch until a rule is triggered.                                                                                                                                                                                                          | EventBusName, None, RuleName            | Count        |

### EventBridge PutEvents metrics

The `AWS/Events` namespace includes the following metrics pertaining to
the `PutEvents` API requests.

For the metrics that use Count as a unit, Sum and SampleCount tend to be the most
useful statistics.

| Metric                               | Description                                                                                   | Dimensions | Units        |
| ------------------------------------ | --------------------------------------------------------------------------------------------- | ---------- | ------------ |
| `PutEventsApproximateCallCount`      | Approximate number of received `PutEvents` requests.                                          | None       | Count        |
| `PutEventsApproximateFailedCount`    | Approximate number of failed `PutEvents` requests.                                            | None       | Count        |
| `PutEventsApproximateSuccessCount`   | Approximate number of successful `PutEvents` requests.                                        | None       | Count        |
| `PutEventsApproximateThrottledCount` | Number of `PutEvents` requests rejected due to<br>throttling.                                 | None       | Count        |
| `PutEventsEntriesCount`              | The number of event entries contained in a `PutEvents`<br>request.                            | None       | Count        |
| `PutEventsFailedEntriesCount`        | The number of event entries contained in a `PutEvents` request that<br>failed to be ingested. | None       | Count        |
| `PutEventsLatency`                   | The time taken per `PutEvents` request.                                                       | None       | Milliseconds |
| `PutEventsRequestSize`               | The size of the `PutEvents` request.                                                          | None       | Bytes        |

### EventBridge PutPartnerEvents metrics

The `AWS/Events` namespace includes the following metrics
pertaining to the `PutPartnerEvents` API requests.

###### Note

EventBridge only includes metrics pertaining to [PutPartnerEvents](../APIReference/API_PutPartnerEvents.md "../APIReference/API_PutPartnerEvents.md") requests in SaaS partner accounts that send events. For more information, see [Receiving events from a SaaS partner with Amazon EventBridge](eb-saas.md "eb-saas.md")

For the metrics that use Count as a unit, Sum and SampleCount tend to be the most
useful statistics.

| Metric                                      | Description                                                                                          | Dimensions | Units        |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------- | ------------ |
| `PutPartnerEventsApproximateCallCount`      | Approximate number of received `PutPartnerEvents` requests.                                          | None       | Count        |
| `PutPartnerEventsApproximateFailedCount`    | Approximate number of failed `PutPartnerEvents` requests.                                            | None       | Count        |
| `PutPartnerEventsApproximateThrottledCount` | Number of `PutPartnerEvents` requests rejected due to<br>throttling.                                 | None       | Count        |
| `PutPartnerEventsApproximateSuccessCount`   | Approximate number of successful `PutPartnerEvents`<br>requests.                                     | None       | Count        |
| `PutPartnerEventsEntriesCount`              | The number of event entries contained in a `PutPartnerEvents`<br>request.                            | None       | Count        |
| `PutPartnerEventsFailedEntriesCount`        | The number of event entries contained in a `PutPartnerEvents`<br>request that failed to be ingested. | None       | Count        |
| `PutPartnerEventsLatency`                   | The time taken per `PutPartnerEvents` request.                                                       | None       | Milliseconds |

## Dimensions for EventBridge metrics

EventBridge metrics have _dimensions_, or sortable attributes, which are
listed below.

| Dimension         | Description                                                 |
| ----------------- | ----------------------------------------------------------- |
| `EventBusName`    | Filters the available metrics by event bus name.            |
| `EventSourceName` | Filters the available metrics by partner event source name. |
| `RuleName`        | Filters the available metrics by rule name.                 |
