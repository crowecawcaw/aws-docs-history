

# Troubleshoot inference routers

Use this topic to resolve errors from inference routers. For known limitations, see [Considerations](inference-router.md#inference-router-considerations).

The following table lists the errors that `InvokeInferenceRouter` can return and what to do about each.


| Error | What to do | 
| --- | --- | 
| `ValidationException` (400) | Check the router name, the routing target name, and the request. Don't retry. | 
| HTTP 413, with no error code | The request body is over 6 MB. Reduce the payload. Don't retry. | 
| `RequestTimeoutException` (408) | The router didn't receive the full request body within 300 seconds of accepting the request, for example because of a very slow upload. Retry the request. | 
| `AccessDeniedException` (403) | Check that the caller can invoke the router and every destination. Don't retry. | 
| `ThrottlingException` (429) | You exceeded the router's request rate. Retry with exponential backoff. To request a higher rate, contact AWS Support. | 
| `ModelError` (424) | Your model returned an error. See `OriginalStatusCode`, `OriginalMessage`, and the destination's logs. | 
| `ModelNotReadyException` (429) | The destination isn't ready to serve the model, for example an inference component with no copies. Retry later. | 
| `ServiceUnavailableException` (503) | No destination could serve the request, or a destination didn't respond, or a destination in another account denied the request (for example, its endpoint policy doesn't allow the caller). Check the destinations in `DescribeInferenceRouter` and their metrics. If the response arrives quickly (within a few seconds of your request), retry with exponential backoff. If the response arrives after about a minute, your model may have run, so check the destination's logs before you retry. | 
| `InternalFailure` (500), `InternalDependencyException` (530) | Retry with exponential backoff. The AWS SDKs and the AWS CLI do this by default. | 

`InvokeInferenceRouterAsync` can also return `RequestTimeoutException` (408). Handle it as described in the preceding table.

The router passes back errors from a destination with the destination's status code and error code. To see which destination returned an error, check the `X-Amzn-SageMaker-Invoked-Routed-Resource-Arn` response header (`InvokedRoutedResourceArn` in the SDKs). When a destination doesn't respond, the router returns its own `ServiceUnavailableException` (503) without the routed resource and routing reason headers.

Use the error code and the status code together to tell throttling errors apart:
+ `ThrottlingException` with status 429 – the router throttled the request because you exceeded the router's request rate.
+ `ThrottlingException` with status 400 – a destination throttled the request, for example because of its `CrossRegionTrafficConfig` limit, and the router passed the error back. The routed resource ARN names the destination.

## Configure client retries
<a name="inference-router-troubleshoot-retries"></a>

The router retries some failures once on another destination. Configure your SDK client for at most 2 attempts with the standard retry mode. In Boto3, set `retries={"total_max_attempts": 2, "mode": "standard"}` in the client `Config`. In the AWS CLI, set the `AWS_MAX_ATTEMPTS` environment variable to `2`. For time limits and the client read timeout, see [Quotas and limits](inference-router.md#inference-router-quotas).

## Common issues
<a name="inference-router-troubleshoot-common"></a>

A destination's `RoutingStatus` is `Unknown`  
Add `sagemaker:DescribeEndpoint` (and `sagemaker:DescribeInferenceComponent` for inference components) to your IAM policy. For a destination in another account, also add it to the endpoint policy. If the check was throttled or timed out, call `DescribeInferenceRouter` again later.

A destination's `RoutingStatus` is `Unroutable`  
The destination can't serve requests. Check that it exists in your account, that it's `InService`, and that it has capacity or can scale to get capacity.

`PutEndpointPolicy` fails with a missing condition  
A statement that grants another account an invoke action needs a `sagemaker:SourceInferenceRouterArn` condition. For more information about the required condition, see [Endpoint policy rules](inference-router-cross-account.md#inference-router-endpoint-policy-rules).

`CreateInferenceRouter` fails with `ResourceLimitExceeded`  
You have reached the router quota for the AWS Region. Delete unused routers or request an increase. For more information, see [Quotas and limits](inference-router.md#inference-router-quotas).

The router sends requests to another Region  
Check the `X-Amzn-SageMaker-Invoked-Routing-Reason` response header and the `destination.status` metric to see why. For the meaning of each routing reason, see [How the router chooses a destination](inference-router.md#inference-router-how).

Requests didn't move to another Region  
Check the `destination.status` metric and the routing reason header. Common causes:  
+ The local destination is slow but isn't returning errors, throttling, or timing out. Slow successful responses don't move traffic. Scale the endpoint, or lower the target value of its autoscaling policy so that it scales out sooner.
+ The errors are caused by the requests, such as 4xx errors from your model. These would fail in every Region, so they don't move traffic.
+ No destination in another Region is healthy and `Routable`. Check the other destinations' `destination.status` and `RoutingStatus`. A destination in another account whose `RoutingStatus` is `Unknown` gets traffic only when no destination is `Routable`; see the `Unknown` entry in this topic.
+ The other destination limits requests from other Regions with `CrossRegionTrafficConfig`. Requests over the limit return `ThrottlingException` (400), and the router retries them on another destination. Raise the limit or the destination's capacity.
+ Traffic moves gradually. After errors start, it takes about a minute or more before traffic moves, and only part of it moves while the local destination still serves some requests successfully.
+ For asynchronous requests, a request moves only if the destination doesn't start it within `MaxTimeInBacklogSeconds`. A request that has started doesn't move.

An asynchronous request returns an `InferenceId`, but no output or failure object appears  
The destination couldn't read the input or write the output. Check that the input, output, and failure buckets are in the router's Region and owned by the router's account, and that the destination's execution role has the permissions in [Permissions for asynchronous requests](inference-router-async.md#inference-router-async-permissions). If the destination's VPC reaches Amazon S3 through a gateway endpoint, it can reach buckets only in its own Region. Give it another route to Amazon S3, such as a NAT gateway. For a destination in another account, ask the endpoint owner to check the endpoint's logs.