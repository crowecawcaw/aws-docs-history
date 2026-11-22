

# Lambda Function state events in Amazon EventBridge

AWS Lambda sends an event to Amazon EventBridge each time an Event Function version changes state as a result of a customer action, such as creating, updating, publishing, or deleting the function. You can use these events to see when a new version is ready to invoke, when a code or configuration update finishes, or when a create, publish, or update operation fails, without polling [GetFunction](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunction.html).

You don't need to turn anything on in Lambda to get these events, and you don't need to opt in or change permissions. Events are delivered to the default event bus of the AWS account that owns the function, in the function's AWS Region. Use EventBridge rules to respond to lifecycle events. Rules can match on fields such as the function ARN (which includes the version), the `detail-type` or the `state`. Each matched event can then go to targets such as AWS Step Functions, AWS Lambda, Amazon Simple Notification Service or Amazon Simple Queue Service. Lambda doesn't charge for these events, and EventBridge doesn't charge for events delivered to the default bus. For details about creating a rule using the enhanced builder, see [EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the Amazon EventBridge User Guide.

The AWS account that owns the function always receives the event, even when a role from another account made the API call. To send events to another account, or to a central monitoring account, create a rule in the owner account that forwards them.

## Event types
<a name="monitoring-eventbridge-function-state-types"></a>

Each event's `detail-type` names the transition. All events are published with `"source": "aws.lambda"`.


| **Detail Type** | **When it's sent** | 
| --- | --- | 
| Event Function Version Activating | State becomes Pending after [CreateFunction](https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunction.html) or [PublishVersion](https://docs.aws.amazon.com/lambda/latest/api/API_PublishVersion.html). | 
| Event Function Version Activated | State becomes Active and the version can be invoked. | 
| Event Function Version Activation Failed | State becomes Failed. | 
| Event Function Version Active Non Invocable | The $LATEST version of a Lambda Managed Instances function becomes ActiveNonInvocable. Publish a version to get one you can invoke. | 
| Event Function Version Updating | LastUpdateStatus becomes InProgress. | 
| Event Function Version Updated | LastUpdateStatus becomes Successful. | 
| Event Function Version Update Failed | LastUpdateStatus becomes Failed. | 
| Event Function Version Deactivating | State becomes Deactivating. This state applies only to Lambda Managed Instances, through the PutFunctionScalingConfig API. | 
| Event Function Version Deactivated | State becomes Deactivated. This state applies only to Lambda Managed Instances, through the PutFunctionScalingConfig API. | 
| Event Function Version Deleting | State becomes Deleting. Sent only for asynchronous deletes (Lambda Managed Instances and durable functions), when deletion of the whole function or of a published version starts. | 
| Event Function Version Deleted | Deletion of the whole function or of a published version finishes. Sent for both asynchronous deletes (after the Deleting event) and synchronous deletes. | 

During an update, `State` stays `Active` and invocations keep using the previous code and configuration until the update finishes. If you only check `State`, a failed update looks like a success. Use the `Updated` and `Update Failed` events to tell them apart.

## Deletion events
<a name="monitoring-eventbridge-function-state-deletion"></a>

The deletion events Lambda sends depend on whether the function is deleted synchronously or asynchronously.

Lambda deletes on-demand functions synchronously. When you call [DeleteFunction](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteFunction.html), the deletion finishes as part of the call, so Lambda sends only an `Event Function Version Deleted` event. Lambda deletes Lambda Managed Instances functions and durable functions asynchronously. For these functions, Lambda first sends an `Event Function Version Deleting` event when the deletion starts. It then sends an `Event Function Version Deleted` event when the deletion finishes.

When you delete the whole function by its name or unqualified ARN, Lambda sends one `Deleting` event and one `Deleted` event for the function, each with the unqualified function ARN in `resources`. Lambda doesn't send separate events for each published version. When you delete a specific version, the events carry that version's qualified ARN.

**Note**  
Each event has its own `revisionId`, except for the `Event Function Version Deleting` and `Event Function Version Deleted` events from the same deletion, which share the same `revisionId`.

## Example event
<a name="monitoring-eventbridge-function-state-example"></a>

```json
{
  "version": "0",
  "id": "7bf73129-1428-4cd3-a780-95db273d1602",
  "detail-type": "Event Function Version Activated",
  "source": "aws.lambda",
  "account": "111122223333",
  "time": "2026-09-26T18:43:48Z",
  "region": "us-east-1",
  "resources": ["arn:aws:lambda:us-east-1:111122223333:function:my-fn:1"],
  "detail": {
    "action": "CreateFunction",
    "state": "Active",
    "lastUpdateStatus": "Successful",
    "revisionId": "8f3b1c2a-4e5d-4a6b-9c8d-1e2f3a4b5c6d"
  }
}
```

The `resources` field contains the qualified function ARN, which includes the version, so you can filter events for a specific version. When you delete the whole function by its name or unqualified ARN, the deletion events carry the unqualified function ARN, and Lambda doesn't send separate events for each version. For details, see [Deletion events](#monitoring-eventbridge-function-state-deletion).

The `time` field shows when the state changed, not when Lambda sent the event. The `action` field names the API call that started the change: `CreateFunction`, `PublishVersion`, `UpdateFunctionCode`, `UpdateFunctionConfiguration`, `DeleteFunction`, `PutRuntimeManagementConfig` or `PutFunctionScalingConfig`. The `state`, `stateReason`, `stateReasonCode`, `lastUpdateStatus` and `lastUpdateStatusReasonCode` fields use the same values that [GetFunction](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunction.html) returns. Lambda leaves out any of these fields that have no value.

## Example: run a function when a version becomes ready
<a name="monitoring-eventbridge-function-state-tutorial"></a>

1. Create a rule that matches the `Event Function Version Activated` event.

   ```bash
   aws events put-rule --name lambda-fn-activated \
     --event-pattern '{"source":["aws.lambda"],"detail-type":["Event Function Version Activated"]}'
   ```

1. Grant EventBridge permission to invoke the target function, so the function can be invoked as soon as you add it as a target.

   ```bash
   aws lambda add-permission --function-name on-fn-ready --statement-id eb-fn-activated \
     --action lambda:InvokeFunction --principal events.amazonaws.com \
     --source-arn arn:aws:events:us-east-1:111122223333:rule/lambda-fn-activated
   ```

1. Add the function as the rule's target. From then on, matching events go to the function.

   ```bash
   aws events put-targets --rule lambda-fn-activated \
     --targets 'Id=1,Arn=arn:aws:lambda:us-east-1:111122223333:function:on-fn-ready'
   ```

## Delivery behavior
<a name="monitoring-eventbridge-function-state-delivery"></a>

Lambda delivers each event to EventBridge at least once, so you may get duplicates. Use `revisionId` to remove duplicates within the same `detail-type`. Events can arrive out of order, even for the same version. Compare the event's `time`, or call [GetFunction](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunction.html) when you need the current state.