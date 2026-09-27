

# Updating, pausing, and resuming a subscriber
<a name="eb-custom-bus-update"></a>

`UpdateSubscriber` changes a subscriber in place. A top-level member you omit keeps its stored value; a configuration object you supply replaces the stored object whole, so to change one filter, pass the complete `FilterConfiguration` with every filter you want to keep. To pause a subscriber, pass `--state STOPPED`; to resume, pass `--state RUNNING` with a `--resume-position`.

## What you can change
<a name="eb-custom-bus-update-properties"></a>

The following request replaces the subscriber's whole `InvokeConfiguration`, so it names the role and every target parameter the subscriber must keep. `TargetArn` is not part of the update; a subscriber's target cannot change.

```
{
    "SubscriberArn": "arn:aws:events:us-east-1:111122223333:subscriber/large-orders/EXAMPLEabcdef1234567890",
    "InvokeConfiguration": {
        "RoleArn": "arn:aws:iam::111122223333:role/NewSubscriberTargetRole",
        "SqsParameters": {
            "MessageGroupId": "{% $events.Data.customerId %}"
        }
    }
}
```

The following table lists each member of the request and what supplying it does.


| Request member | Effect | 
| --- | --- | 
| Description | Replaces the description. An empty or blank value clears it. | 
| State | Moves the subscriber between RUNNING and STOPPED; see [Pausing and resuming](#eb-custom-bus-update-pause) | 
| ResumePosition | Where a STOPPED to RUNNING transition resumes | 
| InvokeConfiguration | Replaces the delivery role and the target parameters. TargetArn stays as it is. | 
| FilterConfiguration | Keeps, clears, or replaces the whole filter configuration; see [Updating filters](#eb-custom-bus-update-filters) | 
| BatchConfiguration | Replaces the whole batching configuration | 
| Transformer | Replaces the whole transformer. Set Type to RAW to remove a metadata or JSONata transformer. | 
| RetryPolicy | Replaces the whole retry policy. An omitted member takes its default: 5 retry attempts, 300 seconds, and RetryStrategy ALL, the only value, which retries every failure category. | 
| OnFailureConfiguration | Replaces the whole on-failure configuration. Send {} to remove the destination; with no destination, an event is dropped when its retries are exhausted. | 
| LogConfiguration | Replaces the whole logging configuration. Send {} to restore the defaults, Level OFF and IncludePayload ON\_ERROR\_ONLY, which turns delivery logging off. | 

`Name`, `EventBusArn`, `Type`, `StartingPosition`, `PointInTimeConfiguration`, and `TargetArn` identify the subscriber or fix its starting point and cannot be changed; tags change through `TagResource` and `UntagResource`. The update response carries the subscriber's identity, state, starting position, and `LastModifiedTime`; read the configuration back with `DescribeSubscriber`.

An update never moves the subscriber's position on the bus: it does not rewind, skip, or replay. To re-deliver past events under a new configuration, create a new subscriber with a starting position instead; see [Replaying retained events to a subscriber](eb-custom-bus-replay.md).

## Troubleshooting: an update cleared settings you did not change
<a name="eb-custom-bus-update-cleared"></a>

An update replaces each configuration object you supply as a whole; see [What you can change](#eb-custom-bus-update-properties).

Symptom  
After an update, a filter, log setting, retry limit, or retention period you did not touch is back at its default, and no error was returned.

Cause  
An update leaves an omitted top-level member unchanged but replaces a supplied block whole. An update that passes `FilterConfiguration`, `LogConfiguration`, `RetryPolicy`, or `StorageConfiguration` to change one field clears the block's other fields. An event source updated without its `Pattern` comes back with no pattern, which widens it to every event.

Solution  
Read the resource, modify the whole block, write the whole block back, then read it again. The read-back is the only confirmation, because create and update responses do not echo every field.  

```
aws eventsv2 describe-subscriber --subscriber-arn "$SUBSCRIBER_ARN" --query 'LogConfiguration'

aws eventsv2 update-subscriber --subscriber-arn "$SUBSCRIBER_ARN" \
    --log-configuration '{ "Level": "INFO", "IncludePayload": "FULL" }'

aws eventsv2 describe-subscriber --subscriber-arn "$SUBSCRIBER_ARN" --query 'LogConfiguration'
```

Verification  
The second describe shows every field of the block with the values you intended.

## Updating filters
<a name="eb-custom-bus-update-filters"></a>

To replace the filters, pass a `FilterConfiguration` whose `Filters` list holds every filter the subscriber should have; EventBridge combines filters for different scopes with AND. To remove every filter, pass `FilterConfiguration` as `{}`.


| Request | Result | 
| --- | --- | 
| FilterConfiguration omitted | The stored filters stay | 
| FilterConfiguration is {} | Every stored filter is removed | 
| Filters is a non-empty list | The list is validated and replaces the whole filter configuration | 
| Filters is an empty list, or Language is given without Filters | InvalidInputException; a supplied FilterConfiguration must contain at least one filter | 

Filter changes are limited to 24 per subscriber in any rolling 24 hours. Only a change to the set of scopes and patterns counts; re-submitting an identical `FilterConfiguration` does not. The 25th change fails with `FILTER_CHANGE_LIMIT_EXCEEDED`. This limit is not a Service Quota and cannot be raised, so a design that rewrites filters continuously should instead publish the varying value into the event and filter on it once.

## Which configuration an already matched event uses
<a name="eb-custom-bus-update-inflight"></a>

EventBridge matches an event to a subscriber and delivers it at different times, and it records which version of the filters matched each event. An update that changes what the filters match creates a new filter version, and EventBridge stores the transformer and target parameters with it. An event matched before the change is delivered with the old transformer and target parameters; an event matched after it uses the new ones. The same holds after a subscriber stops and resumes.


| Filter update | Creates a new filter version | 
| --- | --- | 
| Changing a pattern | Yes | 
| Changing which scopes have a filter | Yes | 
| Adding the first filter | Yes | 
| Clearing all filters | Yes, when filters were stored | 
| Reordering equivalent filters | No | 
| Changing only Language | No | 

So when a filter and a transformer or target parameter form one behavior, change them in the same request. The following request pairs a new `DATA` filter with the transformer written for it, so no event is delivered with a mismatched pair.

```
{
    "SubscriberArn": "arn:aws:events:us-east-1:111122223333:subscriber/large-orders/EXAMPLEabcdef1234567890",
    "FilterConfiguration": {
        "Filters": [
            { "Scope": "DATA", "Pattern": "{\"type\":[\"priority\"]}" }
        ]
    },
    "Transformer": {
        "Type": "JSONATA",
        "JsonataConfiguration": {
            "Expression": "{% {\"version\": 2, \"event\": $events.Data} %}"
        }
    }
}
```

An update that changes only the transformer or the target parameters creates no filter version. Once it propagates, the new configuration applies to events that are still waiting for delivery and to later retry attempts. The delivery role, retry policy, on-failure destination, batching, and logging configuration always take the latest propagated values, whatever version matched the event. Because EventBridge can evaluate the transformer and target parameters again for a retry, a time-dependent or nondeterministic JSONata function such as `$now()` can produce a different result on each attempt; do not assume a retried request carries identical bytes.

`UpdateSubscriber` stores the change before it returns, and the delivery components pick it up after a propagation delay, during which events can still use the previous configuration. `DescribeSubscriber` confirms what is stored, not that every component has switched. After an update, publish a test event and check the target payload before you rely on the new behavior.

Only one subscriber create or delete runs at a time on a bus, across every account that uses it; a concurrent call fails with `ConcurrentModificationException`. Retry it.

## Pausing and resuming
<a name="eb-custom-bus-update-pause"></a>

A subscriber delivers only while its `State` is `RUNNING`. Set it to `STOPPED` to pause; events continue to accumulate on the bus, bounded by retention. When you set it back to `RUNNING`, `ResumePosition` decides what happens to the backlog.
+ `LAST_PROCESSED`, the default: continue from where delivery stopped, so every event published while the subscriber was stopped is delivered, oldest first.
+ `LATEST`: skip the backlog and deliver only events published from now on. A subscriber that is replaying cannot use it: an open-ended replay is still catching up, and a bounded replay never reaches live events.

```
aws eventsv2 update-subscriber \
    --subscriber-arn arn:aws:events:us-east-1:111122223333:subscriber/large-orders/EXAMPLEabcdef1234567890 \
    --state STOPPED

aws eventsv2 update-subscriber \
    --subscriber-arn arn:aws:events:us-east-1:111122223333:subscriber/large-orders/EXAMPLEabcdef1234567890 \
    --state RUNNING \
    --resume-position LAST_PROCESSED
```

`ResumePosition` is accepted only on the call that moves the state from `STOPPED` to `RUNNING`. On that call EventBridge first makes the subscriber's delivery endpoint discoverable again; if that step fails, the call returns `InternalException`, nothing is saved, and the subscriber stays `STOPPED`, so retry the request. A subscriber that the bus owner has revoked does not deliver in either state; see [Revoking a subscriber or an event source](eb-custom-bus-access-revoke.md).

## Errors an update can return
<a name="eb-custom-bus-update-errors"></a>

EventBridge validates the updated configuration against the subscriber's stored target type, so an `SqsParameters` block on a subscriber whose target is a Lambda function is rejected.


| Condition | Error | 
| --- | --- | 
| The subscriber does not exist | ResourceNotFoundException | 
| The subscriber is revoked | InvalidStateException | 
| The request has more than one target parameter block | InvalidInputException | 
| The target parameters do not match the stored target type | InvalidInputException | 
| The transformer is not supported for the target | InvalidInputException | 
| A JSONata expression is invalid | InvalidInputException | 
| A batching value is outside the target's limits | InvalidInputException | 