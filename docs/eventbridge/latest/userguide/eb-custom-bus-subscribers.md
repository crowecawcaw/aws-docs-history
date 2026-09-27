

# Subscribing to events on a Custom Event Bus
<a name="eb-custom-bus-subscribers"></a>

A subscriber is one resource that says which events you want and where to send them. You create it with `CreateSubscriber`, naming the bus, the filters, and one target. It watches that bus, keeps the events that match its filters, optionally transforms each one, and delivers it to exactly one target. To fan an event out to several targets, create one subscriber for each target on the same bus.

EventBridge applies one subscriber create or delete at a time on a given bus, whichever account calls. A second `CreateSubscriber` or `DeleteSubscriber` on the same bus while one is in progress fails with `ConcurrentModificationException`; retry it. The create and delete rates in [Custom Event Bus quotas](eb-quota.md#eb-custom-bus-quotas) therefore apply per bus.

## Filtering which events reach the target
<a name="eb-custom-bus-subscribers-filter"></a>

`FilterConfiguration` holds a list of `Filters`. Each filter has a `Pattern`, in EventBridge event pattern syntax, and one `Scope`. You can have at most one filter per scope, and EventBridge delivers an event only if it matches every filter in the list. A subscriber without a `FilterConfiguration` receives every event on the bus.
+ `DATA`: matches the payload. Write the pattern against the shape described in [Event structure: data, metadata, and system metadata](eb-custom-bus-addressing.md).
+ `METADATA`: matches the key-value pairs a producer set with `PutRawEvents`, exact match only.
+ `SYSTEM_METADATA`: matches the fields EventBridge sets, such as `aws:Source` or `EventGroupId`.

For the pattern syntax, the scope rules, and examples, see [Filtering events for a subscriber](eb-custom-bus-filtering.md).

## Transforming the payload
<a name="eb-custom-bus-subscribers-transform"></a>

`Transformer.Type` selects what the target receives. A universal target does not use it; see [Universal targets for a Custom Event Bus](eb-custom-bus-universal-targets.md).
+ `RAW`, the default. The payload alone.
+ `WITH_METADATA`. The full event: `Data`, `Metadata`, and `SystemMetadata`.
+ `JSONATA`. The result of the JSONata expression in `JsonataConfiguration.Expression`, wrapped in `{% %}` delimiters, with the event available as `$events`.

EventBridge checks the syntax of an expression when you create the subscriber and evaluates it at delivery time. An expression that throws, or that produces no value, fails the delivery of that event. Test expressions against real events before you depend on them. For what `$events` holds, the extra functions, and the limits, see [Transforming events with JSONata](eb-custom-bus-transform.md).

## Delivering to one target
<a name="eb-custom-bus-subscribers-deliver"></a>

`InvokeConfiguration` carries the `TargetArn`, the `RoleArn` that EventBridge assumes to invoke the target, and at most one parameter block that matches the target type. Most parameter values accept a JSONata expression, so a value can come from the event. The following table lists the bespoke target types and their parameter block; each has its own page under [Targets for a Custom Event Bus subscriber](eb-custom-bus-targets.md).


| Target | Parameter block | 
| --- | --- | 
| Amazon SQS queue | SqsParameters | 
| Lambda function | LambdaParameters | 
| Kinesis stream | KinesisParameters | 
| Step Functions state machine | StepFunctionsParameters | 
| Amazon SNS topic | SnsParameters | 
| HTTP endpoint or API destination | HttpParameters | 
| Firehose stream | FirehoseParameters | 

An Custom Event Bus or a Custom Event Bus - Classic can also be the target: set the bus ARN as `TargetArn`. For a FIFO target such as an Amazon SQS FIFO queue, set the target's own deduplication identifier in the parameter block, for example `SqsParameters.MessageDeduplicationId`, to a per-message value derived from the event with a JSONata expression. A constant makes the target discard every message after the first.

A *universal target* invokes an AWS API action directly, with no function in between. Its ARN has the form `arn:aws:events:::aws-sdk:{{service}}:{{apiAction}}`, for example `arn:aws:events:::aws-sdk:dynamodb:putItem`, and its `UniversalTargetParameters.Input` holds the request as JSON or as a JSONata expression that produces it. For the naming rules, batching, and failure behavior, see [Universal targets for a Custom Event Bus](eb-custom-bus-universal-targets.md).

When you create the subscriber, EventBridge resolves the target type from the ARN and checks three things: that the parameter block matches the target type, that the ARN belongs to your account, and that every expression parses. Whether the target exists, whether the role can reach it, and whether the target's API accepts the values are checked at delivery, so confirm the first delivery at the target.

## Retries and dead-letter queues
<a name="eb-custom-bus-subscribers-retry"></a>

`RetryPolicy` sets how long EventBridge retries a failed delivery, by default 5 attempts within 300 seconds, and `OnFailureConfiguration.Arn` names the Amazon SQS queue that receives a record for each event that exhausted its retries. Set both when you create the subscriber. For the limits, the record format, and how to redrive, see [Retry policies and dead-letter queues](eb-custom-bus-retry.md).

## The delivery role
<a name="eb-custom-bus-subscribers-role"></a>

The role in `RoleArn` must belong to your account and trust the `events.amazonaws.com` service principal. Your caller needs `iam:PassRole` on the role to create the subscriber, or EventBridge denies the request before it checks the target ARN. The role's permissions policy needs two grants.
+ The action the target requires, for example `sqs:SendMessage` on a queue, `lambda:InvokeFunction` on a function, `sns:Publish` on a topic, or `kinesis:PutRecords` on a stream.
+ `sqs:SendMessage` on the dead-letter queue in `OnFailureConfiguration.Arn`. Without it, a failed delivery has nowhere to record itself, and those events are lost with no signal.

The following trust policy allows EventBridge to assume the role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": { "Service": "events.amazonaws.com" },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

The following permissions policy delivers to an Amazon SQS queue and dead-letters to a second queue.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "InvokeTheTarget",
            "Effect": "Allow",
            "Action": "sqs:SendMessage",
            "Resource": "arn:aws:sqs:us-east-1:111122223333:large-orders"
        },
        {
            "Sid": "WriteToTheDeadLetterQueue",
            "Effect": "Allow",
            "Action": "sqs:SendMessage",
            "Resource": "arn:aws:sqs:us-east-1:111122223333:large-orders-dlq"
        }
    ]
}
```

## Example: deliver large orders to a queue
<a name="eb-custom-bus-subscribers-example"></a>

The following command creates a subscriber that delivers orders over 500 to an Amazon SQS queue, for events published with `PutEvents`, and sends failures to a dead-letter queue.

```
aws eventsv2 create-subscriber \
    --name large-orders \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --filter-configuration '{
        "Filters": [
            { "Scope": "DATA", "Pattern": "{\"detail\":{\"total\":[{\"numeric\":[\">\",500]}]}}" }
        ]
    }' \
    --invoke-configuration '{
        "TargetArn": "arn:aws:sqs:us-east-1:111122223333:large-orders",
        "RoleArn": "arn:aws:iam::111122223333:role/EventBusDeliveryRole"
    }' \
    --on-failure-configuration '{ "Arn": "arn:aws:sqs:us-east-1:111122223333:large-orders-dlq" }'
```

## Troubleshooting: you published and nothing arrived at the target
<a name="eb-custom-bus-subscribers-nothing-arrived"></a>

A publish response says only that the bus accepted and stored the event; it never confirms delivery. Work through the following checks in order.

Symptom  
The publish call returned HTTP 200 with no failed entries, and the target has received nothing after several minutes.

Cause  
One of five things, in order of frequency: delivery is still being retried; the subscriber is `STOPPED` or revoked; the subscriber's `StartingPosition` is `LATEST` and the event was published before the subscriber existed; the filter is written for the other publish API and matches nothing; or the delivery role cannot reach the target or the dead-letter queue. `TargetInvocations` tells you which half of the problem you have. Datapoints on `TargetInvocations` with none on `EventsDelivered` mean that deliveries are attempted and fail. No datapoints on `TargetInvocations` while `FilterEvaluated` has them means that no delivery is attempted; check that the subscriber is `RUNNING`, and check `EventTransformationFailures`.

Solution  

1. Read the subscriber. `State` must be `RUNNING` and `Revoked` must be absent; it appears only when true. Note `StartingPosition` and the filters.

   ```
   aws eventsv2 describe-subscriber \
       --subscriber-arn arn:aws:events:us-east-1:111122223333:subscriber/large-orders/EXAMPLE1234567890abcdef
   ```

1. Read the subscriber's metrics in `AWS/EventsV2`. `FilterEvaluated` at zero means no event reached this subscriber: the producer published to another bus, or before the subscriber existed with `LATEST`. `FilterEvaluated` above zero with `FilterMatched` at zero means the filter matched nothing; see [Event structure: data, metadata, and system metadata](eb-custom-bus-addressing.md). When `FilterMatched` has datapoints and `EventsDelivered` does not, deliveries are failing, and which metric records the outcome depends on the subscriber: `EventsDropped` when no dead-letter queue is configured, `OnFailureDestinationDelivered` when the event reached the queue, and `OnFailureDestinationFailed` when it did not.

1. Turn on logs and reproduce. Set `LogConfiguration.Level` to `INFO` and `IncludePayload` to `FULL`, wire a log delivery, publish again, and read the `EVENT_DELIVERY_ATTEMPT` records. Each carries the target's own error code and message, and `details.target_input`, which is what EventBridge sent rather than what you meant to send. See [Observability for the Custom Event Bus: metrics, logs, and CloudTrail](eb-custom-bus-observability.md).

1. If the filter is the suspect, add a diagnostic subscriber on the same bus with no filter, `Transformer.Type` `WITH_METADATA`, and a queue you own as the target. It delivers each event exactly as EventBridge sees it, as `Data`, `Metadata`, and `SystemMetadata`. Then simplify your filter one condition at a time; the last condition you remove is the cause.

Verification  
Publish one event that should match and one that should not. The first arrives at the target and `EventsDelivered` increments by one; the second does not arrive and `FilterEvaluated` increments while `FilterMatched` does not.

**Note**  
A subscriber's metrics are available to the bus owner and to the subscriber's owner; its logs are delivered only to the subscriber's owner.