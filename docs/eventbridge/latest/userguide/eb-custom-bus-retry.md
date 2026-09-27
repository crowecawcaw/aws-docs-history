

# Retry policies and dead-letter queues
<a name="eb-custom-bus-retry"></a>

When a target call fails, EventBridge retries it until one of the two limits in `RetryPolicy` is reached, by default 5 attempts or 300 seconds, then writes a record to the Amazon SQS queue in `OnFailureConfiguration.Arn`. Set both when you create the subscriber: without a dead-letter queue, an event that exhausts its retries is dropped, and the only trace is the `EventsDropped` metric.

## Retry limits
<a name="eb-custom-bus-retry-policy"></a>

Delivery stops at whichever limit is reached first.


| Limit | Range | Default | 
| --- | --- | --- | 
| MaxRetryAttempts | 0 to 185 | 5 | 
| MaxEventAgeInSeconds | 60 to 86,400 | 300 | 

The defaults are shorter than a Custom Event Bus - Classic target's 24 hours and 185 attempts. A migrated design that relied on a day of retries must set `MaxEventAgeInSeconds` to 86,400 explicitly; otherwise events that fail during a target outage longer than 5 minutes go to the dead-letter queue instead of being delivered late. For a FIFO subscriber, a failing event blocks the later events in its group for as long as it is retried, so a long retry window trades order for latency.

## The dead-letter record
<a name="eb-custom-bus-retry-record"></a>

The record is a JSON document, not the event. The following example shows one record for two events that failed together in one batch.

```
{
    "version": "1.0",
    "busArn": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef",
    "subscriberArn": "arn:aws:events:us-east-1:111122223333:subscriber/large-orders/EXAMPLEabcdef1234567890",
    "targetArn": "arn:aws:sqs:us-east-1:111122223333:large-orders",
    "errorCode": "ACCESS_DENIED",
    "errorMessage": "The delivery role is not authorized to perform sqs:SendMessage on the target.",
    "exhaustedRetryCondition": "MaximumEventAgeInSeconds",
    "retryAttempts": 4,
    "failedMessages": [
        { "eventId": "a1b2c3d4-...", "eventGroupId": "order-1001", "deduplicationId": null, "timestamp": "2026-09-16T18:40:12Z", "targetRequestId": "..." },
        { "eventId": "e5f6a7b8-...", "eventGroupId": "order-1001", "deduplicationId": null, "timestamp": "2026-09-16T18:40:13Z", "targetRequestId": "..." }
    ]
}
```

Every failure that reaches the queue was retried first: there is no delivery failure that skips `RetryPolicy`. Failures inside EventBridge itself are retried by EventBridge without limit and never produce a record. The following table lists the codes a record can carry. `errorMessage` is truncated to 1,024 characters.


| `errorCode` | What failed | `errorMessage` | 
| --- | --- | --- | 
| CUSTOMER\_VALIDATION | The target API rejected the request (a 4xx response): a bad value, a missing field, a malformed body | The target API's own message | 
| ACCESS\_DENIED | EventBridge could not assume the delivery role, the role is not allowed to call the target, or the target's AWS KMS key denied access | EventBridge could not assume {{role}}. Check that the role exists and that its trust policy allows the EventBridge service principal to assume it. or EventBridge could not access {{resource}}. Check that it exists and that its policy allows the EventBridge service principal access. | 
| RESOURCE\_NOT\_FOUND | The target, or its AWS KMS key, does not exist | The could not access message above, or the generic message | 
| INPUT\_TRANSFORMATION\_FAILURE | The Transformer or universal-target Input expression threw or produced no value | The expression error | 
| THROTTLING | The target throttled the call | The generic message | 
| EXECUTION\_TIMEOUT | The target did not respond within InvocationTimeoutSeconds | The generic message | 
| REQUEST\_TOO\_LARGE | The request exceeded the target's size limit; lower MaxBatchSize | The generic message | 
| PARTIAL\_BATCH\_FAILURE | The target accepted part of a batch and rejected the rest; the record's failedMessages lists only the rejected events | The generic message | 
| RESOURCE\_CONFLICT | The target reported a conflict, for example a name already in use | The generic message | 
| KMS\_INVALID\_STATE | The target's AWS KMS key is disabled or pending deletion | The generic message | 
| SFN\_TYPE\_NOT\_SUPPORTED | REQUEST\_RESPONSE was used with a Standard state machine, which does not support synchronous execution | The generic message | 
| COMPUTE\_EXECUTION\_ERROR | A REQUEST\_RESPONSE function or execution ran and reported an error | The generic message | 
| INVOCATION\_DEPENDENCY\_INTERNAL | The target returned a server error (a 5xx response) | The generic message | 
| LOOP\_DETECTED | The event, or an event derived from it, already passed through the target bus; see [Loop detection](eb-custom-bus-target-bus.md#eb-custom-bus-target-bus-loops) | The generic message | 
| INTERNAL\_SERVER\_ERROR | A failure inside EventBridge while making the call that still exhausted the retries | The generic message | 

The generic message is *The delivery failed. Use this record's error code and request id when investigating, and contact AWS Support if the failure persists.* EventBridge uses it wherever passing the underlying message through could expose another service's internals, so for those codes the `errorCode` and `targetRequestId` are the facts to work from, together with the `EVENT_DELIVERY_ATTEMPT` log records, which carry the request that was sent. The same values arrive as Amazon SQS message attributes (`ERROR_CODE`, `ERROR_MESSAGE`, `SUBSCRIBER_ARN`, `TARGET_ARN`, `BUS_ARN`, `EXHAUSTED_RETRY_CONDITION`, `RETRY_ATTEMPTS`), so a consumer can route on them without parsing the body. For a FIFO subscriber, use a FIFO queue as the dead-letter queue; EventBridge sets each record's `MessageGroupId` from the events' `EventGroupId`, so records for one group stay in order.

The delivery role needs `sqs:SendMessage` on the queue. Without it, the `OnFailureDestinationFailed` metric counts each record that could not be written, and those events are lost.

## Redriving events from the dead-letter queue
<a name="eb-custom-bus-retry-redrive"></a>

The queue holds records, not events, so you redrive by replaying the events from the bus. The events must still be within the bus's retention period.

1. Read the records and collect every `failedMessages[].eventId`, plus the earliest and latest `timestamp`.

1. Fix the cause the `errorCode` names: the role's policy, the target, or the expression.

1. Create a subscriber on the same bus with the same target and role, a `POINT_IN_TIME` starting position whose `StartingPoint` is the earliest timestamp and whose `EndPoint` is the latest, and a `SYSTEM_METADATA` filter on the identifiers.

1. When the subscriber has delivered the events, delete it and delete the records from the queue.

```
aws eventsv2 create-subscriber \
    --name redrive-2026-09-16 \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --starting-position POINT_IN_TIME \
    --point-in-time-configuration '{ "PointType": "TIMESTAMP", "StartingPoint": "2026-09-16T18:40:00Z", "EndPoint": "2026-09-16T18:41:00Z" }' \
    --filter-configuration '{ "Filters": [ { "Scope": "SYSTEM_METADATA", "Pattern": "{\"aws:EventId\":[\"a1b2c3d4-...\",\"e5f6a7b8-...\"]}" } ] }' \
    --invoke-configuration '{ "TargetArn": "arn:aws:sqs:us-east-1:111122223333:large-orders", "RoleArn": "arn:aws:iam::111122223333:role/EventBusDeliveryRole" }'
```

The replayed events arrive with `aws:DeliveryType` `REPLAY`, so a consumer can tell them from live traffic.