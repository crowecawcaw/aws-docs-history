

# Universal targets for a Custom Event Bus
<a name="eb-custom-bus-universal-targets"></a>

A *universal target* invokes an AWS API action directly from a subscriber, with no function in between. Instead of naming a queue, topic, or function as the target, you name the service and the API action, and you write the API request that EventBridge sends, either as fixed JSON or as a JSONata expression that builds the request from the event. A subscriber can write an item to a DynamoDB table, put an object in an Amazon S3 bucket, publish to an Amazon SNS topic, or start a Step Functions execution without a Lambda function in the path.

## The target ARN
<a name="eb-custom-bus-universal-targets-arn"></a>

A universal target's `TargetArn` has a fixed form with no Region and no account:

```
arn:aws:events:::aws-sdk:{{service}}:{{apiAction}}
```
+ {{service}} is the AWS SDK service identifier, which is not always the service's familiar name. For example, Step Functions is `sfn`, not `states`. Examples that work: `sqs`, `sns`, `s3`, `dynamodb`, `bedrockagentcore`.
+ {{apiAction}} is the API action name in camelCase with a lowercase first letter: `putItem`, not `PutItem`. EventBridge looks the name up exactly as you wrote it in its index of actions, which is in camelCase, so `PutItem` is rejected by `CreateSubscriber` with the message *The api PutItem is not valid for the service dynamodb*. The same message means the action does not exist for that service.

For example, `arn:aws:events:::aws-sdk:dynamodb:putItem` invokes DynamoDB `PutItem`, and `arn:aws:events:::aws-sdk:sns:publish` invokes Amazon SNS `Publish`.

## Actions that are not supported
<a name="eb-custom-bus-universal-targets-unsupported"></a>

Two kinds of action cannot be the target of a subscriber, and `CreateSubscriber` rejects them with a message that says the API, or the whole service, is not supported.
+ Actions that read rather than change state, such as those whose names begin with `get`, `list`, or `describe`. An event carries something that happened, so a target action must change state. EventBridge keeps a list of blocked action names and services and can add to it, for example when an action does not behave as a target should, so an action that was accepted once is not guaranteed forever; treat the create-time message as the authority.
+ The EventBridge publish actions, `eventbridge:putEvents` and `eventbridge:putPartnerEvents`. To deliver events to another event bus, set the bus ARN as the `TargetArn`; a Custom Event Bus and a Custom Event Bus - Classic are both supported as targets in their own right. See [Event bus target: bus to bus](eb-custom-bus-target-bus.md).

## Parameters
<a name="eb-custom-bus-universal-targets-parameters"></a>

A universal target requires `InvokeConfiguration.UniversalTargetParameters`. `CreateSubscriber` rejects a subscriber that omits it, or that supplies a different parameter block such as `SqsParameters`. The message says `UniversalTargetParameters` is expected. Shape the request through `Input`; a universal-target subscriber does not use the subscriber's `Transformer`, so put any JSONata transformation in `Input`.

`Input` (required)  
The API request, as a JSON string or as a JSONata expression wrapped in `{% %}` that produces the request. Use the member names from the target API's own reference; for Amazon SQS `SendMessage` that is `QueueUrl` and `MessageBody`. Up to 262,144 characters.  
A fixed JSON `Input` is checked when you create the subscriber against the fields the API requires, and a missing field is rejected by name. A JSONata `Input` is checked for syntax only, because its result depends on the event, so a request that the target API rejects surfaces at delivery time instead.

`InvocationTimeoutSeconds`  
How long EventBridge waits for one API call, from 1 to 30 seconds. The default is 30. This must be a literal integer; a JSONata expression is not accepted here.

The delivery role in `RoleArn` needs the IAM action for the API you invoke, such as `dynamodb:PutItem`, and `sqs:SendMessage` on the dead-letter queue. For the role's trust policy and the rest of its permissions, see [Access control for the Custom Event Bus](eb-custom-bus-access.md).

## Batching and the `$events` array
<a name="eb-custom-bus-universal-targets-batching"></a>

EventBridge makes one API call per batch, not one per event. `BatchConfiguration` sets the batch: `MaxBatchSize` from 1 to 500, and `MaxBatchWindowInSeconds` from 0 to 300. A batch closes when it reaches the size or when the window elapses, whichever comes first.

In a JSONata `Input`, `$events` is the batch: an array of the events in it. With a batch size of 1, `$events.Data.orderId` yields the one event's value. With a larger batch, address the array explicitly, for example with `$map` and `$join`, or the expression produces an array where the API expects a string and the delivery fails.

Set `MaxBatchSize` to 1 and `MaxBatchWindowInSeconds` to 0 to make one API call for each event. Do this whenever `Input` is fixed JSON, because a fixed request is identical for every event in the batch and the batch produces a single call.

## Example: one DynamoDB item per event
<a name="eb-custom-bus-universal-targets-example"></a>

The following subscriber writes one item to a DynamoDB table for each event published with `PutRawEvents`, taking the partition key from the event's `orderId` field. The delivery role needs `dynamodb:PutItem` on the table.

```
aws eventsv2 create-subscriber \
    --name orders-to-dynamodb \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --invoke-configuration '{
        "TargetArn": "arn:aws:events:::aws-sdk:dynamodb:putItem",
        "RoleArn": "arn:aws:iam::111122223333:role/EventBusDeliveryRole",
        "UniversalTargetParameters": {
            "Input": "{% { \"TableName\": \"orders\", \"Item\": { \"pk\": { \"S\": $events.Data.orderId }, \"total\": { \"N\": $string($events.Data.total) } } } %}"
        }
    }' \
    --batch-configuration MaxBatchSize=1,MaxBatchWindowInSeconds=0 \
    --on-failure-configuration '{ "Arn": "arn:aws:sqs:us-east-1:111122223333:orders-to-dynamodb-dlq" }'
```

For an event published with `PutEvents`, the same fields are under `detail`: `$events.Data.detail.orderId`. See [Event structure: data, metadata, and system metadata](eb-custom-bus-addressing.md).

## When the API call fails
<a name="eb-custom-bus-universal-targets-failures"></a>

When you create the subscriber, EventBridge checks the ARN's shape, that the action exists and is not blocked, and that a fixed `Input` carries the action's required fields and, for a JSONata `Input`, that the expression parses. It does not check that the resource named in the request exists or that the delivery role can call the action. Those failures happen at delivery, and every delivery failure is retried under the subscriber's `RetryPolicy`, by default up to 5 attempts within 300 seconds. When a limit is reached, EventBridge writes a record to the dead-letter queue whose `errorCode` names the last failure. The codes a universal target produces most often:
+ `CUSTOMER_VALIDATION`: the target API rejected the request, for example a missing required field or a value out of range. The record carries the target API's own error message.
+ `ACCESS_DENIED`: EventBridge could not assume the delivery role, or the role is not allowed to call the action on the resource. The record says which, in an EventBridge message that names the role or the resource.
+ `RESOURCE_NOT_FOUND`: the table, topic, or other resource named in the request does not exist.
+ `INPUT_TRANSFORMATION_FAILURE`: the JSONata expression in `Input` threw an error or produced no value.
+ `THROTTLING`: the target API throttled the call. `REQUEST_TOO_LARGE`: the request exceeded the action's size limit; lower `MaxBatchSize`. `EXECUTION_TIMEOUT`: the call did not return within the timeout.

For the full list of error codes, the message each carries, and how to redrive, see [Retry policies and dead-letter queues](eb-custom-bus-retry.md). Turn on subscriber logs to see each attempt and the exact request sent; see [Observability for the Custom Event Bus: metrics, logs, and CloudTrail](eb-custom-bus-observability.md).