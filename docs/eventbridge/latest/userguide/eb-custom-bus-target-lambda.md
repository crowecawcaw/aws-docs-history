

# Lambda function target
<a name="eb-custom-bus-target-lambda"></a>

To deliver to a Lambda function, set `TargetArn` to the function ARN, optionally with an alias or version, and add `LambdaParameters`. The shape of the payload depends on `BatchConfiguration.MaxBatchSize`. With `MaxBatchSize` set to 1, the function receives the event as a single JSON object. With any other value, or with no `BatchConfiguration`, the function receives a JSON array holding the events in the batch, one element per event, even when the batch holds one event.

## Parameters
<a name="eb-custom-bus-target-lambda-parameters"></a>


| Parameter | What it sets | 
| --- | --- | 
| InvocationType | EVENT invokes asynchronously and treats a successful Invoke as delivered. REQUEST\_RESPONSE waits for the function to return and treats a function error as a failed delivery. After a successful EVENT invoke, delivery to the function's code is governed by Lambda's asynchronous queue, which is at-least-once. For ordered processing on a FIFO subscriber, use REQUEST\_RESPONSE. | 
| Qualifier | A function version or alias, if not part of the ARN | 
| DurableExecutionName | The name of a durable execution, for functions that use durable execution | 
| TenantId | The tenant identifier passed to a multi-tenant function | 
| InvocationTimeoutSeconds | How long EventBridge waits for the call, 1 to 30 seconds, default 30 | 

## Delivery role
<a name="eb-custom-bus-target-lambda-role"></a>

The role needs `lambda:InvokeFunction` on the function, including its alias or version if you name one.

## Batching and payload
<a name="eb-custom-bus-target-lambda-batching"></a>

One `Invoke` carries the whole batch as a JSON array. Set `BatchConfiguration.MaxBatchSize` to 1 if the function expects one event per invocation; the function then receives that event as a single JSON object rather than a one-element array. See [Batching deliveries to a target](eb-custom-bus-batching.md).