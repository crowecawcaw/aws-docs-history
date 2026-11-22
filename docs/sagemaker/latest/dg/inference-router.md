

# Route requests across AWS Regions with cross-Region inference routing

Cross-Region inference routing in Amazon SageMaker AI lets your application call one API for a model that you host in more than one AWS Region or AWS account. A router sends each request to a destination that's healthy and has capacity.

An inference router is a Regional SageMaker AI resource that you invoke instead of an endpoint. You add one or more *routing targets* to it. A routing target represents one model, and lists the *destinations* that can serve it. A destination is a SageMaker AI endpoint or inference component, in your account or in another account, in any AWS Region in the same AWS partition as the router. On each request you name the routing target, and the router sends the request to one of its destinations.

You still deploy your models and manage their capacity. The router doesn't change your endpoints, inference components, or their autoscaling.

## When to use an inference router
<a name="inference-router-when"></a>
+ You deploy the same model in more than one Region and want one API to call, instead of choosing a Region in your application.
+ You want requests to move to another Region when an endpoint is overloaded or failing, and to move back when it recovers. For example, if your endpoint in `us-west-2` can't add GPU instances during a traffic spike, the router serves the overflow from your endpoint in `us-east-1`.
+ You want to use capacity that another AWS account shares with you. For more information, see [Route requests to endpoints in other AWS accounts](inference-router-cross-account.md).

## Considerations
<a name="inference-router-considerations"></a>

Consider the following before you use an inference router:
+ The router runs in one Region. If the router's Region is impaired, calls to that router fail, even if destinations in other Regions are healthy.
+ You can't restrict an individual request to specific Regions. A routing target can send any request to any of its destinations, so only add destinations in Regions where requests are allowed to go. For a pattern, see [Keep requests within allowed Regions](inference-router-security.md#inference-router-security-data-residency).
+ Every destination in a routing target must serve the same model, with the same request and response format.
+ A router's destinations can be in any Region in the router's partition, not only in Regions where you can create a router. You can use a destination in an opt-in Region only if the account that owns it has enabled that Region.
+ You can't place another Region ahead of the router's Region. You can't set weights or health thresholds.
+ You can't use response streaming.
+ You can't use `TargetVariant`, `TargetModel`, `InferenceComponentName`, or stateful sessions (`SessionId`).
+ The router checks a destination's mode only when you create or update the router. If a destination endpoint later changes mode, remove it from the routing target, or move it to a routing target of the matching mode.
+ Model execution timeout increases for your account don't apply through an inference router. Your model has up to 60 seconds to respond to a real-time request. For longer-running models, use `InvokeInferenceRouterAsync`.
+ The runtime endpoint supports HTTP/1.1 only. HTTP/2 isn't supported. Callers that use the AWS SDKs or the AWS CLI aren't affected.
+ If your client stops reading a response for 60 seconds, the router closes the connection. This limit is separate from the model's 60-second limit.
+ If the router doesn't receive the full request body within 300 seconds of accepting the request, it returns `RequestTimeoutException` (408).

## Pricing
<a name="inference-router-pricing"></a>

There is no additional charge for cross-Region inference routing. You pay standard Amazon SageMaker AI pricing for the endpoints and inference components that serve your requests, whether a request reaches them directly or through an inference router. When a destination belongs to another AWS account, that account pays for its endpoint or inference component. Inference routers publish metrics to Amazon CloudWatch, and you pay standard CloudWatch rates for those metrics and for the queries that you run on them.

## Tools and Regions
<a name="inference-router-tools"></a>

You can create and manage inference routers with the AWS CLI, the AWS SDKs, and AWS CloudFormation (resource types `AWS::SageMaker::InferenceRouter` and `AWS::SageMaker::EndpointPolicy`; see [Set up cross-account access with AWS CloudFormation](inference-router-cross-account.md#inference-router-cloudformation)). The SageMaker AI console doesn't support inference routers. You manage routers with the `sagemaker` client, and invoke them with a separate runtime service, SageMaker AI Inference Router Runtime (`sagemaker-inference-router-runtime` in the AWS CLI and the SDKs), not with `sagemaker-runtime`. Its endpoint is `inferencerouter-runtime.sagemaker.{{region}}.amazonaws.com`. To call a router from your Amazon VPC without crossing the internet, see [Invoke inference routers through an interface VPC endpoint](inference-router-security.md#inference-router-privatelink). For the AWS Regions where inference routers are available, and their service endpoints, see [SageMaker AI endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html) in the *AWS General Reference*.

Asynchronous routing (`InvokeInferenceRouterAsync`) isn't available in Asia Pacific (New Zealand), Asia Pacific (Jakarta), Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Europe (Milan), Israel (Tel Aviv), and Canada West (Calgary).

## How the router chooses a destination
<a name="inference-router-how"></a>

The Region where you create the router is its *local Region*. The router sends requests only to destinations whose `RoutingStatus` is `Routable`, and uses local destinations first.

The router measures each destination's health from the requests it serves, including requests that don't come through the router. The following lower a destination's health:
+ Server errors from SageMaker AI or from your model container (5xx).
+ Throttling by the endpoint's instances, for example when the endpoint is at capacity.
+ Timeouts, for example a model that takes longer than 60 seconds.

When a local destination's health drops, the router moves part of its traffic to healthy destinations in other Regions. The lower its health, the more traffic moves. Traffic moves gradually, and moves back gradually when the destination recovers. The router spreads the traffic that it moves across the healthy destinations in other Regions. The order of your destinations decides only which destination the router retries a request on, and which destination it tries when none is `Routable`.

The following don't move traffic:
+ Slow responses that succeed. If your endpoint slows down under load without returning errors, the router keeps sending it traffic. Configure autoscaling so that the endpoint adds instances before it starts to throttle.
+ Errors caused by the request, such as validation errors and 4xx errors from your model.
+ Requests over a destination's `CrossRegionTrafficConfig` limit. The router retries them on another destination.

The router retries a failed request once on another destination when the destination didn't run your model, for example when it throttled the request. It doesn't retry timeouts, or errors that occur after your model starts responding. If no destination is `Routable`, the router still tries one destination. If none can be tried, you get a `ServiceUnavailableException`. For time limits, see [Quotas and limits](#inference-router-quotas).

Each response tells you which destination served the request (`X-Amzn-SageMaker-Invoked-Routed-Resource-Arn`) and why it was chosen (`X-Amzn-SageMaker-Invoked-Routing-Reason`). The following table describes the routing reasons that you see in each response.


| Routing reason | Meaning | 
| --- | --- | 
| `local-preferred` | The request went to a healthy destination in the local Region. | 
| `capacity-available` | No local destination could take the request, so the request went to one of two or more destinations in other Regions that could. | 
| `failover` | The router moved the request away from local destinations because they were overloaded or returning errors. You also see this reason when the router can't assess destination health, and when no destination is healthy and the router tries one anyway. | 
| `only-healthy` | No local destination could take the request, and exactly one destination in another Region could. | 

The following table describes the `RoutingStatus` values that `DescribeInferenceRouter` returns for each destination.


| `RoutingStatus` | Meaning | 
| --- | --- | 
| `Routable` | The destination is serving and the router can send it requests. A routable destination can still be overloaded. | 
| `Unroutable` | The destination can't serve requests, for example because it's being created or has failed, or because it's in service but has no capacity and no way to get any. A destination in your account that doesn't exist is also `Unroutable`. | 
| `Unknown` | SageMaker AI couldn't check the destination, for example because you aren't allowed to describe it, or the check was throttled or timed out. The destination might be serving. | 

To track destination health over time, use the `destination.status` metric. For more information, see [CloudWatch metrics](inference-router-monitor.md#inference-router-monitor-metrics).

## Set a cross-Region traffic cap on an endpoint
<a name="inference-router-cross-region-limit"></a>

To keep an endpoint's capacity for requests from its own AWS Region, you can limit the requests per second that inference routers in other Regions send to it. Set `CrossRegionTrafficConfig` in the endpoint configuration:
+ `MaxInvocationsPerSecondPerInstance` – the invocations per second that one instance can serve.
+ `MaxCrossRegionPercentPerEndpoint` – the percentage of that capacity that requests from inference routers in other Regions can use.

The limit is the percentage of `MaxInvocationsPerSecondPerInstance` multiplied by the number of `InService` instances, so it grows and shrinks with the endpoint. All production variants and inference components of the endpoint share it. For example, the following endpoint configuration limits requests from inference routers in other Regions to 25 per second on an endpoint with two instances.

```bash
aws sagemaker create-endpoint-config \
    --endpoint-config-name {{my-endpoint-config}} \
    --production-variants file://{{production-variants.json}} \
    --cross-region-traffic-config MaxInvocationsPerSecondPerInstance=50,MaxCrossRegionPercentPerEndpoint=25
```

A request over the limit fails with a `ThrottlingException` (400), and the router retries it once on another destination. Requests from the endpoint's own Region and direct calls to the endpoint aren't counted. `CreateEndpointConfig` rejects `CrossRegionTrafficConfig` together with `AsyncInferenceConfig` or a serverless variant.

## Plan capacity in other Regions
<a name="inference-router-standby"></a>

The router doesn't add capacity. It moves traffic to destinations in other Regions only while they're healthy, so they need room for the traffic that moves.
+ Keep at least one instance in service in each real-time standby endpoint, and configure autoscaling on it, for example on `InvocationsPerInstance`.
+ Size the standby for the traffic that you expect to move. If its instances throttle, the router sends it less traffic and moves requests to other healthy destinations, if any.
+ To protect a standby's own Regional traffic, set `CrossRegionTrafficConfig` on it. The limit grows with its `InService` instances.
+ An asynchronous standby can scale to zero instances. A request waits up to `MaxTimeInBacklogSeconds` at a destination before it moves, so set it longer than the time the standby takes to scale out.

## Quotas and limits
<a name="inference-router-quotas"></a>

The following limits apply to inference routers and can't be changed:
+ Routing targets per router: 20
+ Destinations per routing target: 10
+ Endpoint policy size: 20,480 characters
+ Real-time request payload: 6 MB. A larger request body returns HTTP 413.
+ Real-time model time: your model has up to 60 seconds to respond to each request, the same limit as `InvokeEndpoint`. If an attempt fails with an error that the router retries, such as throttling, the router tries one more destination, and your model again has up to 60 seconds there. Timeouts aren't retried. Set your client read timeout to at least 170 seconds so that it covers a retry. For models that take longer, use `InvokeInferenceRouterAsync`.

For asynchronous request limits, see [Invoke asynchronously](inference-router-async.md#inference-router-async-invoke).

The following quota applies per AWS account per AWS Region:
+ Inference routers: 5

The following invoke rates apply per AWS account per AWS Region by default. To request a higher rate, contact AWS Support.
+ `InvokeInferenceRouter`: 10,000 requests per second
+ `InvokeInferenceRouterAsync`: 100 requests per second

To request an increase in the router quota, see [Amazon SageMaker AI endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html) in the *AWS General Reference*, or the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas).

**Topics**
+ [When to use an inference router](#inference-router-when)
+ [Considerations](#inference-router-considerations)
+ [Pricing](#inference-router-pricing)
+ [Tools and Regions](#inference-router-tools)
+ [How the router chooses a destination](#inference-router-how)
+ [Set a cross-Region traffic cap on an endpoint](#inference-router-cross-region-limit)
+ [Plan capacity in other Regions](#inference-router-standby)
+ [Quotas and limits](#inference-router-quotas)
+ [Get started with inference routers](inference-router-get-started.md)
+ [Route requests to endpoints in other AWS accounts](inference-router-cross-account.md)
+ [Route asynchronous inference requests through an inference router](inference-router-async.md)
+ [Security and data protection for inference routers](inference-router-security.md)
+ [Monitor inference routers with Amazon CloudWatch and AWS CloudTrail](inference-router-monitor.md)
+ [Troubleshoot inference routers](inference-router-troubleshoot.md)