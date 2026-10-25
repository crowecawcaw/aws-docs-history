

# A function produces no metadata
<a name="functions-troubleshooting-runtime"></a>

A run that fails writes nothing, so every runtime problem looks the same from `GetMetadata`: no item for that window, an empty `items` array, `ResourceNotFoundException`, or `MetadataUnavailableException` while no later run has succeeded. The **Preview metadata** section on the console's **Feed outputs** tab shows nothing for the same windows.

To find the cause, enable vended logs for the feed. A run that fails for one of the following reasons logs an `ERROR` record whose `detail.error_code` names the cause, and whose `detail` includes the `function_id`. Repeated failures with the same code are logged at most once every 5 seconds for each feed. For how to enable the logs and read a record, see [Monitoring AWS Elemental Inference with vended logs](monitoring-vended-logs.md).


| `error_code` | Cause and what to do | 
| --- | --- | 
| FUNCTION\_ROLE\_ACCESS\_DENIED | Elemental Inference couldn't assume the feed's access role. Check the role's trust policy. See [Trust policy](functions-prerequisites-access-role.md#functions-prerequisites-trust-policy). | 
| FUNCTION\_MODEL\_ACCESS\_DENIED | The model denied the invocation. Check that the access role allows bedrock:InvokeModel on the model, that you have access to the model in the feed's Region, and that no service control policy in your organization denies the call. An explicit deny in a service control policy can't be overridden by the role's permissions. See [Permissions policy](functions-prerequisites-access-role.md#functions-prerequisites-permissions-policy). | 
| FUNCTION\_MODEL\_THROTTLED | Your account's Amazon Bedrock quota for the model is exhausted. Lengthen the trigger interval, request a higher Amazon Bedrock quota, or use provisioned throughput. See [Costs and throughput](functions-costs.md). | 
| FUNCTION\_MODEL\_REQUEST\_INVALID | The model rejected the request body that the request expression built. Make the body match the request format of the model you chose. The log record doesn't include the model's message, because it can contain request content. A model that requires a data retention mode higher than your account's mode in the feed's Region also fails this way; see [Data retention](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html) in the Amazon Bedrock User Guide. | 
| FUNCTION\_MODEL\_TIMEOUT | The model didn't respond within the invocation timeout, about 18 seconds. Simplify the request, reduce the frame or fragment count, choose a faster model, or lengthen the trigger interval. | 
| FUNCTION\_MODEL\_ERROR | The model returned another error. detail.status\_code holds the HTTP status. Check the model's availability in your account, and its service health. | 
| FUNCTION\_REQUEST\_EXPRESSION\_INVALID | The request expression failed on this window's data. Check that it handles missing or empty context, such as a window with no speech. See [Expression limits and guardrails](functions-expressions-guardrails.md). | 
| FUNCTION\_RESPONSE\_EXPRESSION\_INVALID | The response expression failed on the model's response. Temporarily set the response expression to $ to see the whole response, then fix the expression. See [Response expressions](functions-expressions-response.md). | 
| FUNCTION\_MEDIA\_TOO\_LARGE | This window's frames or clip encoded larger than the model accepts in one request. Reduce the frame count, set a smaller frame size, or reduce the fragment count. | 

Some failures log nothing. The most common is a run that doesn't finish within about 20 seconds of the end of its window on a live feed. If the logs are empty, work through the following.


| Symptom | Likely cause | 
| --- | --- | 
| No metadata from any output on the feed, including the native ones. | The source isn't delivering media, or the feed isn't active. This isn't a function problem. See [Lifecycle of an AWS Elemental Inference workflow](monitor-inference-feed-lifecycle.md). | 
| Metadata appears intermittently. | Runs are taking close to the time limit, or your Amazon Bedrock throughput quota is throttling the calls. Lengthen the interval, choose a faster model, reduce the frame count, or use provisioned throughput. | 
| Metadata appears, but the value is a whole model response. | The function has no response expression, or the expression evaluated to its entire input. | 
| Metadata appears, but a field you expected is missing. | The response expression's path doesn't match the model's response shape. Temporarily set the response expression to $ to see the whole response, then fix the path. See [Response expressions](functions-expressions-response.md). | 
| contextTypes is empty, or missing a type you expected. | The request expression doesn't actually reference that media path, so Elemental Inference supplies nothing for it. Fix the expression and update the function; contextTypes is recomputed on every update. While a feed uses the function, an update can't change contextTypes. | 
| The frame or fragment settings don't appear on the console attachment form. | The form shows only the settings for the context that the function's contextTypes reports. An empty list means the expression references no media. | 
| Metadata stops at the same moment for every function on the feed. | Check whether the function outputs were disabled, or dropped by a feed update that resent an incomplete output list. | 

**Tip**  
To decide whether a problem is in the model call or in the feed, attach a passthrough function with the same trigger, such as one whose request expression is `{ "ok": true }`. A passthrough function needs no access role and invokes no model. If the feed is at its function-output quota, disable the original output first. If the passthrough function produces metadata, the feed and the trigger are working, and the problem is in the invocation or the response expression.

For a run that succeeds but returns an unexpected result, the item's `bedrockRequestId` identifies the model invocation. Include it when you contact AWS Support about the model's response. See [Reading function results](functions-metadata.md).

Function runs don't emit Amazon CloudWatch metrics to your account. For metrics that show whether a feed is processing at all, see [Monitoring AWS Elemental Inference with Amazon CloudWatch](monitoring-cloudwatch.md). For the events that a feed emits, see [Monitoring AWS Elemental Inference events in Amazon EventBridge](monitoring-events.md).