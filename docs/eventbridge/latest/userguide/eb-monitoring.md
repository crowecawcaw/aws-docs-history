

# Monitoring Amazon EventBridge
<a name="eb-monitoring"></a>

EventBridge sends metrics to Amazon CloudWatch every minute for everything from the number of matched [events](eb-events.md) to the number of times a [target](eb-targets.md) is invoked by a [rule](eb-rules.md).

 The following video reviews monitoring and auditing EventBridge behavior through CloudWatch:




**Best-effort CloudWatch metrics delivery**  
CloudWatch metrics are delivered on a best-effort basis. Most EventBridge operations result in a data point being sent to CloudWatch. The completeness and timeliness of metrics are not guaranteed. A data point for a given minute might be delayed before being available through CloudWatch, or it might not be delivered at all. CloudWatch metrics give you an idea of the nature of activity in near-real time. They are not meant to be a complete accounting of all operations.

**Topics**
+ [EventBridge metrics](#eb-metrics)
+ [Dimensions for EventBridge metrics](#eb-metrics-dimensions)
+ [Best practices for monitoring event delivery in Amazon EventBridge](eb-monitoring-events-best-practices.md)
+ [EventBridge is the evolution of Amazon CloudWatch Events](eb-cwe-now-eb.md)

## EventBridge metrics
<a name="eb-metrics"></a>

The `AWS/Events` namespace includes the following metrics.

For the metrics that use Count as a unit, Sum and SampleCount tend to be the most useful statistics.

Metrics that specify only the `RuleName` dimension refer to the default event bus. Metrics that specify both the `EventBusName` and `RuleName` dimensions refer to a custom event bus. 


| Metric | Description | Dimensions | Units | 
| --- | --- | --- | --- | 
|  DeadLetterInvocations  | The number of times a rule’s target isn't invoked in response to an event. This includes invocations that would result in running the same rule again, causing an infinite loop. | RuleName | Count | 
|  Events  | The number of partner events ingested by EventBridge. | EventSourceName | Count | 
|  FailedInvocations  | The number of invocations that failed permanently. This doesn't include invocations that are retried or invocations that succeeded after a retry attempt. It also doesn't count failed invocations that are counted in `DeadLetterInvocations`. EventBridge only sends this metric to CloudWatch if it isn't zero.  | RuleName | Count | 
|  Invocations  | The number of times a target is invoked by a rule in response to an event. This includes successful and failed invocations, but doesn't include throttled or retried attempts until they fail permanently. It doesn't include `DeadLetterInvocations`. EventBridge only sends this metric to CloudWatch if it isn't zero.  | None, RuleName | Count | 
| InvocationAttempts | Number of times EventBridge attempted invoking a target. | EventBusName, None, RuleName | Count | 
|  InvocationsCreated  | The total number of invocations created in response to each event. <br />This metric is often used to monitor utilization of the **Invocations throttle limit in transactions per second** [EventBridge service quota](eb-quota.md#eb-limits). | None | Count | 
|  InvocationsFailedToBeSentToDlq  | The number of invocations that couldn't be moved to a dead-letter queue. Dead-letter queue errors occur due to permissions errors, unavailable resources, or size limits. EventBridge only sends this metric to CloudWatch if it isn't zero.  | RuleName | Count | 
|  IngestiontoInvocationCompleteLatency  | The time taken from event ingestion to completion of the first invocation attempt.  | EventBusName, None, RuleName | Milliseconds | 
| IngestionToInvocationSuccessLatency | The time taken from event ingestion to successful target delivery, using the invocation end time as cutoff.<br />This metric is only emitted after the first successful delivery attempt to the target. | EventBusName, None, RuleName | Milliseconds | 
|  IngestiontoInvocationStartLatency  | The time to process events, measured from when an event is ingested by EventBridge to the first invocation of a target.  | EventBusName, None, RuleName | Milliseconds | 
|  InvocationsSentToDlq  | The number of invocations that are moved to a dead-letter queue. EventBridge only sends this metric to CloudWatch if it isn't zero.  | RuleName | Count | 
|  MatchedEvents  | If EventBusName or EventSourceName is specified, the number of events that matched with any rule. If RuleName is specified, the number of events that matched with a specific rule. | EventBusName, EventSourceName, RuleName | Count | 
| RetryInvocationAttempts | Number of times target invocation has been retried.EventBridge only sends this metric to CloudWatch if it isn't zero. | EventBusName, None, RuleName | Count | 
| SuccessfulInvocationAttempts | Number of times target was successfully invoked. | EventBusName, None, RuleName | Count | 
|  ThrottledRules  | The number of times rule execution was throttled. Invocations for those rules may be delayed.<br />For more information, see **Invocations throttle limit in transactions per second** in [EventBridge event bus quotas](eb-quota.md#eb-limits). | EventBusName, None, RuleName | Count | 
|  TriggeredRules  | The number of rules that have run and matched with any event.<br />You won't see this metric in CloudWatch until a rule is triggered. | EventBusName, None, RuleName | Count | 
|  EventBusEncryptionStarted  | The number of times a re-encryption operation has started for an event bus. Updating the event bus configuration triggers a re-encryption of the static configuration stored by EventBridge. | EventBusName | Count | 
|  EventBusEncryptionCompleted  | The number of times a re-encryption operation has completed successfully for an event bus. Updating the event bus configuration triggers a re-encryption of the static configuration stored by EventBridge. | EventBusName | Count | 
|  EventBusEncryptionFailed  | The number of times a re-encryption operation has failed for an event bus. Updating the event bus configuration triggers a re-encryption of the static configuration stored by EventBridge. EventBridge only sends this metric to CloudWatch if it isn't zero.  | EventBusName | Count | 

### EventBridge PutEvents metrics
<a name="eb-metrics-putevents"></a>

The `AWS/Events` namespace includes the following metrics pertaining to the `[PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)` API requests.

For the metrics that use Count as a unit, Sum and SampleCount tend to be the most useful statistics.


| Metric | Description | Dimensions | Units | 
| --- | --- | --- | --- | 
| PutEventsApproximateCallCount | Approximate number of received `[PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)` requests. | None | Count | 
|  PutEventsApproximateFailedCount  | Approximate number of failed `[PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)` requests. | None | Count | 
|  PutEventsApproximateSuccessCount  | Approximate number of successful `[PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)` requests. | None | Count | 
|  PutEventsApproximateThrottledCount  | Number of `[PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)` requests rejected due to throttling. | None | Count | 
| PutEventsEntriesCount | The number of event entries contained in a `[PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)` request. | None | Count | 
| PutEventsFailedEntriesCount | The number of event entries contained in a `[PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)` request that failed to be ingested. | None | Count | 
|  PutEventsLatency  | The time taken per `[PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)` request. | None | Milliseconds | 
|  PutEventsRequestSize  | The size of the `[PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)` request. | None | Bytes | 

### EventBridge PutPartnerEvents metrics
<a name="eb-metrics-putpartnerevents"></a>

The `AWS/Events` namespace includes the following metrics pertaining to the `[PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html)` API requests.

**Note**  
EventBridge only includes metrics pertaining to [PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html) requests in SaaS partner accounts that send events. For more information, see [Receiving events from a SaaS partner with Amazon EventBridge](eb-saas.md)

For the metrics that use Count as a unit, Sum and SampleCount tend to be the most useful statistics.


| Metric | Description | Dimensions | Units | 
| --- | --- | --- | --- | 
| PutPartnerEventsApproximateCallCount | Approximate number of received `[PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html)` requests. | None | Count | 
|  PutPartnerEventsApproximateFailedCount  | Approximate number of failed `[PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html)` requests. | None | Count | 
|  PutPartnerEventsApproximateThrottledCount  | Number of `[PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html)` requests rejected due to throttling. | None | Count | 
|  PutPartnerEventsApproximateSuccessCount  | Approximate number of successful `[PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html)` requests. | None | Count | 
| PutPartnerEventsEntriesCount | The number of event entries contained in a `[PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html)` request. | None | Count | 
| PutPartnerEventsFailedEntriesCount | The number of event entries contained in a `[PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html)` request that failed to be ingested. | None | Count | 
|  PutPartnerEventsLatency  | The time taken per `[PutPartnerEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPartnerEvents.html)` request. | None | Milliseconds | 

## Dimensions for EventBridge metrics
<a name="eb-metrics-dimensions"></a>

EventBridge metrics have *dimensions*, or sortable attributes, which are listed below.


|  Dimension  |  Description  | 
| --- | --- | 
|  EventBusName  | Filters the available metrics by event bus name. | 
|  EventSourceName  | Filters the available metrics by partner event source name. | 
|  RuleName  | Filters the available metrics by rule name. | 