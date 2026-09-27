

# Lambda function target
<a name="eb-custom-bus-target-lambda"></a>

To deliver to a Lambda function, set `TargetArn` to the function ARN, optionally with an alias or version, and add `LambdaParameters`. The function receives a JSON array holding the events in the batch, one element per event, even when the batch holds one event.

## Parameters
<a name="eb-custom-bus-target-lambda-parameters"></a>


| Parameter | What it sets | 
| --- | --- | 
| InvocationType | EVENT invokes asynchronously and treats a successful Invoke as delivered. REQUEST\_RESPONSE waits for the function to return and treats a function error as a failed delivery | 
| Qualifier | A function version or alias, if not part of the ARN | 
| DurableExecutionName | The name of a durable execution, for functions that use durable execution | 
| TenantId | The tenant identifier passed to a multi-tenant function | 
| InvocationTimeoutSeconds | How long EventBridge waits for the call, 1 to 30 seconds, default 30 | 

## Delivery role
<a name="eb-custom-bus-target-lambda-role"></a>

The role needs `lambda:InvokeFunction` on the function, including its alias or version if you name one.

## Batching and payload
<a name="eb-custom-bus-target-lambda-batching"></a>

One `Invoke` carries the whole batch as a JSON array. Set `BatchConfiguration.MaxBatchSize` to 1 if the function expects one event per invocation. See [Batching deliveries to a target](eb-custom-bus-batching.md).