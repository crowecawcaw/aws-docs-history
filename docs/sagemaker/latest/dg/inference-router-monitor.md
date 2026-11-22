

# Monitor inference routers with Amazon CloudWatch and AWS CloudTrail

Use Amazon CloudWatch metrics to track inference router traffic and destination health, and AWS CloudTrail to audit API calls. Your destination endpoints keep publishing their usual SageMaker AI metrics in their own account and AWS Region.

## CloudWatch metrics
<a name="inference-router-monitor-metrics"></a>

Inference routers publish OpenTelemetry metrics to CloudWatch in the router's Region. Query them with PromQL, for example in CloudWatch Query Studio. They don't appear in the `AWS/SageMaker` namespace. Request metrics go to the account of the caller that invoked the router. `destination.status` goes to the router owner's account.

Every metric name starts with `aws.sagemaker.inference_router.` The following table lists the inference router metrics.


| Metric | Description | 
| --- | --- | 
| `invocations` | Requests that got a final response. Failed requests have an `error.type`. | 
| `overhead.duration` | Time, in seconds, that the router adds to a real-time request: the total time minus the destination time. It includes network time between Regions and any failed attempts. | 
| `destination.duration` | Time, in seconds, that the destination takes to respond to a real-time request, including your model. | 
| `destination.status` | Health of each destination as the router sees it. The series for the current `aws.sagemaker.inference_router.destination.state` (`healthy`, `overloaded`, or `degraded`) is 1, and the others are 0. For the meaning of each state, see the following table. | 
| `async.placement.attempts`, `async.pickup_timeouts`, `async.failovers`, `async.terminations` | Asynchronous requests sent to a destination, not started within `MaxTimeInBacklogSeconds`, moved to another destination, and ended by the router. | 

The following table describes the health states in the `aws.sagemaker.inference_router.destination.state` attribute of the `destination.status` metric. A state doesn't tell you whether the cause is capacity or errors.


| State | Meaning | 
| --- | --- | 
| `healthy` | Health is normal. The router sends this destination its normal share of traffic. | 
| `overloaded`, `degraded` | Health is reduced (`overloaded`) or severely reduced (`degraded`). The router moves traffic away from the destination gradually. | 

Metrics have the following attributes, where they apply. Every attribute name except `error.type` starts with `aws.sagemaker.inference_router.`
+ `name`
+ `routing_target.name`
+ `destination.arn`
+ `destination.region`
+ `destination.state` (only on `destination.status`)
+ `destination.locality` (`local` or `cross_region`)
+ `invocation_mode` (`sync` or `async`)
+ `error.type`. For real-time requests: `invocation_model_error`, `invocation_4xx`, or `invocation_5xx`. For asynchronous requests, also `placement_unavailable`, `placement_rejected`, `placement_denied`, `placement_throttled`, `request_expired`, `destinations_exhausted`, or `routing_target_not_found`.

`destination.status` has only the `name`, `routing_target.name`, `destination.arn`, and `destination.state` attributes. Asynchronous submissions are counted in `invocations` with `invocation_mode` `async` and no destination.

The metrics don't count the following requests, so count them in your application:
+ Requests that the router throttled (`ThrottlingException`, 429).
+ Requests that fail the router's own authentication or authorization.
+ Requests to a router or routing target that doesn't exist.

A destination's errors, including `ThrottlingException` (400) and `AccessDeniedException` (403), are counted in `invocations` with `error.type` `invocation_4xx`. When the router retries a request on another destination, only the final response is counted. `overhead.duration` and `destination.duration` cover only successful responses and model errors.

The following PromQL query counts the invocations of each destination of a router.

```
sum by ("aws.sagemaker.inference_router.destination.arn") (
  sum_over_time({"aws.sagemaker.inference_router.invocations",
                 "aws.sagemaker.inference_router.name"="{{my-router}}"}[5m]))
```

The metrics are delta metrics published once a minute, so use `sum_over_time` instead of `rate`.

To be alerted, for example when a destination leaves the `healthy` state, create a CloudWatch alarm on a PromQL query over these metrics. For instructions on creating a CloudWatch alarm, see [Create a CloudWatch alarm based on a static threshold](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html) in the *CloudWatch User Guide*.

The following PromQL query returns the destinations that aren't healthy.

```
sum by ("aws.sagemaker.inference_router.destination.arn") (
  {"aws.sagemaker.inference_router.destination.status",
   "aws.sagemaker.inference_router.name"="{{my-router}}",
   "aws.sagemaker.inference_router.destination.state"!="healthy"}) > 0
```

The following queries are more examples. The first returns the share of real-time requests served outside the router's Region.

```
sum(sum_over_time({"aws.sagemaker.inference_router.invocations",
    "aws.sagemaker.inference_router.name"="{{my-router}}",
    "aws.sagemaker.inference_router.invocation_mode"="sync",
    "aws.sagemaker.inference_router.destination.locality"="cross_region"}[5m]))
/
sum(sum_over_time({"aws.sagemaker.inference_router.invocations",
    "aws.sagemaker.inference_router.name"="{{my-router}}",
    "aws.sagemaker.inference_router.invocation_mode"="sync"}[5m]))
```

The following query returns the error rate for each destination.

```
sum by ("aws.sagemaker.inference_router.destination.arn") (
  sum_over_time({"aws.sagemaker.inference_router.invocations",
    "aws.sagemaker.inference_router.name"="{{my-router}}",
    "error.type"!=""}[5m]))
/
sum by ("aws.sagemaker.inference_router.destination.arn") (
  sum_over_time({"aws.sagemaker.inference_router.invocations",
    "aws.sagemaker.inference_router.name"="{{my-router}}"}[5m]))
```

The following query counts server errors (`invocation_5xx`) by destination Region, so that you can see whether one Region is failing.

```
sum by ("aws.sagemaker.inference_router.destination.region") (
  sum_over_time({"aws.sagemaker.inference_router.invocations",
    "aws.sagemaker.inference_router.name"="{{my-router}}",
    "error.type"="invocation_5xx"}[5m]))
```

In the queries, replace {{my-router}} with the name of your inference router.

## CloudTrail logs
<a name="inference-router-monitor-cloudtrail"></a>

CloudTrail logs inference router management operations as management events, and `InvokeInferenceRouter` and `InvokeInferenceRouterAsync` as data events (resource type `AWS::SageMaker::InferenceRouter`). Requests that the router sends to a destination appear in the destination's account as `InvokeEndpoint` or `InvokeEndpointAsync` data events. For more information, see [Logging Amazon SageMaker AI API calls using AWS CloudTrail](logging-using-cloudtrail.md).