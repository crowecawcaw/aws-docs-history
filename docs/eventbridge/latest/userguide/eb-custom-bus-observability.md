

# Observability for the Custom Event Bus: metrics, logs, and CloudTrail
<a name="eb-custom-bus-observability"></a>

Three sources tell you what a bus and its subscribers are doing. Amazon CloudWatch metrics in the `AWS/EventsV2` namespace are on for every subscriber; to alarm when deliveries fail, alarm on `OnFailureDestinationDelivered` or `EventsDropped`, or on `EventDeliveryAttempts` minus `EventsDelivered` with metric math. Subscriber logs record each delivery attempt as a JSON record; they are off until you set `LogConfiguration.Level` on the subscriber. AWS CloudTrail records the API calls that create and change buses, subscribers, and event sources.

## Metrics
<a name="eb-custom-bus-observability-metrics"></a>

Subscriber metrics carry two dimensions, `EventBus` and `Subscriber`, each holding the resource ARN. When the subscriber belongs to a different account from the bus, EventBridge also emits the metric with `EventBus` and `SubscriberAccount` so that the bus owner can see consumption per account. The following table lists the metrics.


| Metric | Unit | Meaning | 
| --- | --- | --- | 
| FilterEvaluated | Count | Events evaluated against the subscriber's filters | 
| FilterMatched | Count | Events that matched every filter | 
| EventDeliveryAttempts | Count | Delivery attempts, counted per event. Subtract EventsDelivered to count failed attempts | 
| TargetInvocations | Count | Calls made to the target; one call can carry a batch of events | 
| RetryInvocationAttempts | Count | Emitted only on a retry, valued as the retry depth: the second attempt is 1, the third is 2. The sample count is the number of retries | 
| EventsDelivered | Count | Events the target accepted | 
| EgressBytes | Bytes | Bytes delivered to the target | 
| EventTransformationFailures | Count | Events whose Transformer or universal-target Input expression failed | 
| IngestionToInvocationStartTime | Milliseconds | Time from the event's arrival on the bus to the start of the target call. Not emitted when the attempt failed before calling the target | 
| IngestionToInvocationEndTime | Milliseconds | Time from the event's arrival on the bus to the end of the target call | 
| OnFailureDestinationDelivered | Count | Records written to the dead-letter queue | 
| OnFailureDestinationFailed | Count | Records that could not be written to the dead-letter queue | 
| EventsDropped | Count | Events that exhausted retries with no dead-letter queue to record them | 
| ApproximateBacklogAge | Milliseconds | Age of the oldest event the subscriber has not yet delivered | 
| SubscriberLogRecordsDropped | Count | Log records that could not be written, because log delivery is best effort | 

Your account's bus count is also reported in the `AWS/Usage` namespace as `ResourceCount` with `Service` `EventBridge` and a `Resource` value that begins with `EventsV2/`, so you can alarm as you approach the bus quota. For the quotas, see [Custom Event Bus quotas](eb-quota.md#eb-custom-bus-quotas).

## Publish metrics
<a name="eb-custom-bus-observability-publish-metrics"></a>

Every `PutEvents` and `PutRawEvents` call also produces metrics in the `AWS/EventsV2` namespace, so you can alarm on throttled or failed publish calls for a bus, for example on `PublishEventsApproximateThrottledCallCount` with the `EventBus` dimension set to `orders`. The bus owner's account receives every publish metric. An account that publishes to a bus it does not own also receives them, in its own account, for its own calls.


| Metric | Unit | Meaning | 
| --- | --- | --- | 
| PublishEventsApproximateCallCount | Count | Publish calls received | 
| PublishEventsApproximateSuccessCallCount | Count | Publish calls that returned HTTP 200 | 
| PublishEventsApproximateFailedCallCount | Count | Publish calls that returned an error | 
| PublishEventsApproximateThrottledCallCount | Count | Publish calls rejected with ThrottlingException | 
| PublishEventsEntryCount | Count | Entries in the publish calls | 
| PublishEventsFailedEntriesCount | Count | Entries that failed inside an accepted call, reported in the response as failed entries | 
| PublishEventsIngressBytes | Bytes | Bytes of event payload stored. Absent, rather than 0, for calls that stored nothing. Trends with the ingress line item on your bill, which rounds each entry up to a whole KB. | 

The dimensions depend on the metric and on who published.
+ Every metric is published with the `EventBus` dimension alone: the totals for the bus.
+ For events that arrive through an event source, the count metrics are also published with `EventBus` and `EventSource`, so you can see one source's share. `PublishEventsIngressBytes` has no `EventSource` breakdown.
+ `PublishEventsIngressBytes` is also published to the bus owner with `EventBus` and `PublisherAccount`, so a bus owner can see how many bytes each publishing account stored.

## Subscriber logs
<a name="eb-custom-bus-observability-logs"></a>

A subscriber can record what happened to each event it tried to deliver. Logging is per subscriber and off when you create one, so a new subscriber records nothing until you set `LogConfiguration`. Each record is a JSON document with a `message_type` that says what it describes.
+ `SUBSCRIBER_MATCHED`: an event matched the subscriber's filters and entered delivery.
+ `EVENT_DELIVERY_ATTEMPT`: one attempt to invoke the target, with its outcome, attempt count, and duration. This is the record the rest of this section describes.
+ `EVENT_TRANSFORMATION_FAILURE`: the `Transformer` or universal-target `Input` expression failed for an event, with the error.
+ `ON_FAILURE_DESTINATION_DELIVERY_ATTEMPT`: one attempt to write a record to the dead-letter queue.

Log delivery is best effort. A record that cannot be written is counted in the `SubscriberLogRecordsDropped` metric rather than retried indefinitely. When the bus is encrypted with a customer managed key, EventBridge encrypts the payload fields of each record under that key before it leaves EventBridge, so a destination account that cannot use the key sees the record without them. A replayed event's record carries `details.delivery_type` `REPLAY`; a live event's carries `LIVE`.

### The two settings that produce a record
<a name="eb-custom-bus-observability-configuration"></a>

Two independent settings must both exist before you can read a single record.

1. **The subscriber's log level.** `LogConfiguration.Level` decides which records EventBridge emits. It defaults to `OFF`, which emits none.

1. **A CloudWatch Logs delivery.** Records reach you through the Amazon CloudWatch Logs vended log delivery mechanism, which pairs the subscriber with a destination you own. Without it, records have nowhere to land and no log group appears on its own.

Make both settings before you start diagnosing a delivery problem rather than after. Only subscribers have a log configuration. Buses and event sources have none, so you turn logging on one subscriber at a time. `LogConfiguration` has two members.

`Level`  
The minimum level of a record. Records below it are not emitted. `OFF`, the default, emits nothing. `ERROR` emits failed delivery attempts only. `INFO` emits every delivery attempt, including the ones that succeeded.

`IncludePayload`  
Whether a record carries your event payload. `ON_ERROR_ONLY`, the default, carries it on failure records only. `FULL` carries it on every record. See [Payloads in log records](#eb-custom-bus-observability-payload).

You can set `LogConfiguration` when you create a subscriber, or later with `UpdateSubscriber`. An update takes effect without recreating the subscriber. Neither the create response nor the update response echoes the field back, so confirm the stored value with `DescribeSubscriber`, which does return it.

### Turn on logging for one subscriber
<a name="eb-custom-bus-observability-setup"></a>

The following steps record every delivery attempt for one existing subscriber and deliver the records to a CloudWatch Logs log group in the same account. The first command is an EventBridge call, and the rest are CloudWatch Logs calls. Start by raising the subscriber's log level. `INFO` records successes as well as failures, which is what tells you whether an event was delivered at all.

```
aws eventsv2 update-subscriber \
    --subscriber-arn arn:aws:events:us-east-1:111122223333:subscriber/large-orders/EXAMPLE1234567890abcdef \
    --log-configuration '{ "Level": "INFO", "IncludePayload": "FULL" }'
```

Next, create the destination log group. The name must begin with `/aws/vendedlogs/`. CloudWatch Logs manages the delivery resource policy for you only under that prefix; for a log group outside it you must manage that policy yourself.

```
aws logs create-log-group \
    --log-group-name /aws/vendedlogs/large-orders-delivery
```

Create a delivery source. Its `--resource-arn` is the subscriber ARN, which is what makes the source produce that subscriber's records. Set `--log-type` to match the level you configured: `INFO_LOGS` for `Level` `INFO`, or `ERROR_LOGS` for `Level` `ERROR`.

```
aws logs put-delivery-source \
    --name large-orders-source \
    --resource-arn arn:aws:events:us-east-1:111122223333:subscriber/large-orders/EXAMPLE1234567890abcdef \
    --log-type INFO_LOGS
```

Create a delivery destination naming the log group. The response contains the destination ARN, which the next command needs.

```
aws logs put-delivery-destination \
    --name large-orders-destination \
    --delivery-destination-configuration destinationResourceArn=arn:aws:logs:us-east-1:111122223333:log-group:/aws/vendedlogs/large-orders-delivery
```

Finally, pair the source with the destination. Use the destination ARN from the previous response.

```
aws logs create-delivery \
    --delivery-source-name large-orders-source \
    --delivery-destination-arn {{destination-arn}}
```

Records now appear in the log group. They arrive later than the delivery itself, because the log pipeline batches them, so allow for that lag when you read a log group just after publishing. Three properties of this wiring decide how far it stretches. A destination is a log group, an Amazon S3 bucket, or an Amazon Data Firehose stream, and the commands above are the same for each: only `destinationResourceArn` changes. One delivery pairs exactly one source with exactly one destination, so sending a subscriber's records to a second destination takes a second delivery. The destination can be in a different account from the subscriber, and in that case the destination account must call `PutDeliveryDestinationPolicy` on the destination to allow the delivery, which is how a central account collects records for subscribers it does not own.

### Reading a delivery record
<a name="eb-custom-bus-observability-records"></a>

EventBridge emits one record per delivery attempt per event. Four fields are at the top level. `message_type` is `EVENT_DELIVERY_ATTEMPT` for a delivery attempt; the other types are listed at the start of this section. `resource_arn` is the ARN of the subscriber that made the attempt, which is how you separate subscribers that share one log group. `log_level` is the level of the record itself: a successful attempt is `INFO`, and a failed attempt is `ERROR`, which is why `Level` `ERROR` still records failures. `details` is an object holding the delivery state, and it holds the fields you build queries and alarms on.

`outcome` and `attempt_count`  
`SUCCESS` or `FAILURE` for this attempt, and which attempt it was, so retries are countable.

`terminal_kind`  
Present on the one record that says how the event ended: `EVENTS_DELIVERED`, `ON_FAILURE_DESTINATION_DELIVERED`, or `EVENTS_DROPPED` when retries ran out and no on-failure destination was configured.

`target_arn` and `target_properties`  
The target the attempt was made against, and the target parameters the subscriber resolved for this event. `target_properties` is omitted when the subscriber configures no parameters.

`ingestion_to_start_latency_ms` and `ingestion_to_complete_latency_ms`  
Milliseconds from event ingestion to the start and to the end of this attempt.

`target_input`  
The bytes sent to the target, verbatim. This is a payload field; see [Payloads in log records](#eb-custom-bus-observability-payload).

`event_detail`, `event_metadata`, and `event_system_metadata`  
The event as EventBridge held it. `event_system_metadata` carries the identifiers you correlate records by. `event_detail` appears only when it differs from `target_input`, which is the case when the subscriber has a transformer.

To diagnose a delivery that never arrived, read the subscriber's records in this order. `outcome` says whether EventBridge reached the target at all. `attempt_count` says whether it is still retrying, because an event with no `terminal_kind` record has not finished. `terminal_kind` says how it ended, and separates an event that dead-lettered from one that was dropped. `target_arn`, `target_properties`, and `target_input` say what was sent and where, which is where a transformer or target parameter problem shows up. A failure is visible in the record as soon as the attempt fails, so you do not have to wait for the retries to run out. For the full procedure, see [Troubleshooting: you published and nothing arrived at the target](eb-custom-bus-subscribers.md#eb-custom-bus-subscribers-nothing-arrived).

### Payloads in log records
<a name="eb-custom-bus-observability-payload"></a>

`IncludePayload` controls two fields and no others: `details.target_input` and `details.event_detail`. Every other field is emitted whichever value you choose, so a subscriber that keeps payloads out of its records still reports the outcome, the target, the attempt count, and the latencies. `FULL` embeds the payload in every record, including the records for successful deliveries. `ON_ERROR_ONLY`, the default, embeds it in failure records only, and omits both fields from a record for a successful delivery.

**Important**  
A log record that carries a payload carries your data. With `FULL`, the log group holds a copy of every event body the subscriber delivered, and anyone who can read the log group can read those bodies. Use `FULL` while you are debugging a subscriber, then return it to `ON_ERROR_ONLY`. That limits both the exposure and the volume you store.

## API calls in AWS CloudTrail
<a name="eb-custom-bus-observability-cloudtrail"></a>

Subscriber logs record deliveries, not the calls you make to configure them. AWS CloudTrail records the management API calls, so a change to a bus, a subscriber, or an event source is auditable from your trail rather than from a log group. For how EventBridge integrates with CloudTrail, see [Logging Amazon EventBridge API calls using AWS CloudTrail](logging-using-cloudtrail.md).