

# Step Functions state machine target
<a name="eb-custom-bus-target-sfn"></a>

To start a state machine, set `TargetArn` to the state machine ARN and add `StepFunctionsParameters`. EventBridge starts one execution per batch, and the execution input is a JSON array of the batch's events, so a `Name` expression must not depend on a single event's fields.

## Parameters
<a name="eb-custom-bus-target-sfn-parameters"></a>


| Parameter | What it sets | 
| --- | --- | 
| InvocationType | EVENT calls StartExecution. REQUEST\_RESPONSE calls StartSyncExecution, which only an Express state machine supports, and treats a failed execution as a failed delivery | 
| Name | The execution name. Must be unique per execution; omit it to let Step Functions generate one | 
| TraceHeader | The AWS X-Ray trace header to propagate | 
| InvocationTimeoutSeconds | How long EventBridge waits for the call, 1 to 30 seconds, default 30 | 

## Delivery role
<a name="eb-custom-bus-target-sfn-role"></a>

The role needs `states:StartExecution` on the state machine, or `states:StartSyncExecution` for `REQUEST_RESPONSE`.

## Batching and payload
<a name="eb-custom-bus-target-sfn-batching"></a>

One execution per batch. Set `BatchConfiguration.MaxBatchSize` to 1 for one execution per event. See [Batching deliveries to a target](eb-custom-bus-batching.md).