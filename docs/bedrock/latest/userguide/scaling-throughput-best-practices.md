

# Scaling and throughput best practices
<a name="scaling-throughput-best-practices"></a>

This topic explains how throughput limits and scheduling work across Amazon Bedrock endpoints and provides best practices for scaling your generative AI applications.

## Amazon Bedrock endpoints
<a name="scaling-endpoints"></a>

Amazon Bedrock supports two endpoints for inference:
+ `bedrock-mantle.{region}.api.aws` — Supports the OpenAI-compatible Chat Completions and Responses APIs, and the Anthropic Messages API.
+ `bedrock-runtime.{region}.amazonaws.com` — Supports the Bedrock-native InvokeModel and Converse APIs, the OpenAI-compatible Chat Completions and Responses APIs, and the Anthropic Messages API.

For most new applications, start with `bedrock-runtime`. Use `bedrock-mantle` when you need capabilities that are available only on that endpoint, such as server-side tools, background inference, Projects, Workspaces, or a model that is available only on `bedrock-mantle`. You can use both endpoints in the same application. For a complete comparison, see [Endpoints supported by Amazon Bedrock](endpoints.md).

### Why the two endpoints behave differently
<a name="scaling-endpoint-differences"></a>

Both endpoint surfaces use the same underlying inference engine, but their quota accounting and capacity options differ. [`bedrock-runtime`](endpoints.md) uses per-model token quotas and, for some models, requests-per-minute (RPM) quotas. [`bedrock-mantle`](endpoints.md) does not enforce RPM quotas and uses separate input-token and output-token quotas for models that have published quotas. Other models on `bedrock-mantle` might not have per-account quotas exposed in Service Quotas, but their throughput is still governed by internal service capacity.

A quota is an upper bound, not a guarantee that every on-demand request will be served immediately. During periods of high demand, requests can be queued or receive transient capacity errors. Design your application to bound concurrency, queue work, and retry transient errors without creating a retry surge.

## `bedrock-mantle` endpoint: throughput and quotas
<a name="scaling-mantle-quotas"></a>

The `bedrock-mantle` endpoint has the following quota behavior:
+ Models with published quotas have separate per-model, per-Region input-tokens-per-minute and output-tokens-per-minute quotas.
+ The endpoint does not enforce RPM quotas. Two workloads with the same RPM can consume very different amounts of capacity, so plan and rate-limit by tokens and concurrency instead of RPM alone.
+ When a request is admitted, the input-token check includes the input tokens plus the requested `max_tokens` value. After the response completes, the unused part of that reservation is replenished. Set `max_tokens` no higher than your application needs.
+ Models without published TPM quotas do not currently have per-account TPM quotas exposed in Service Quotas. This does not mean that throughput is unlimited; internal service capacity and transient rate limiting still apply.
+ Batch inference and Provisioned Throughput are available only through `bedrock-runtime`. Service-tier and model support varies by model.

Default values and your account's allocations can vary by model, Region, and usage history. For current values, quota evaluation details, and the AWS Support process for requesting an increase, see [Quotas for the bedrock-mantle endpoint](quotas-mantle.md). See the applicable [Models at a glance](model-cards.md) for model-specific endpoint, service-tier, and feature support.

## `bedrock-runtime` endpoint: throughput and quotas
<a name="scaling-runtime-quotas"></a>

The `bedrock-runtime` endpoint has the following quota behavior:
+ Per-model, per-Region token quotas count input and output tokens together. Output tokens consume quota according to a model-specific burndown rate.
+ Some models also have RPM quotas, while other models are governed only by token quotas. Check the quotas that apply to the exact model and inference profile that you use.
+ Per-minute and per-day token quotas are shared across the inference APIs that call the same model on this endpoint. Allocations for `bedrock-runtime` and `bedrock-mantle` are independent.
+ Custom inference profiles, batch inference, and Provisioned Throughput have separate quotas and are available only through `bedrock-runtime`.

For current quota values, token-burndown details, and the quota-increase process, see [Quotas for the bedrock-runtime endpoint](quotas-runtime.md). See the applicable [Models at a glance](model-cards.md) for model-specific endpoint, service-tier, and feature support.

## Understanding HTTP error responses
<a name="scaling-http-errors"></a>

HTTP 429  
A 429 response means that the request was not admitted. Inspect the API-specific error type rather than relying on the HTTP status alone. A `ThrottlingException` or rate-limit error generally means that the request exceeded an account quota or a service rate limit. Some runtime operations also use HTTP 429 for `ModelNotReadyException`. On `bedrock-mantle`, check input and output TPM usage and the request's `max_tokens` value; the endpoint does not have an RPM quota. On `bedrock-runtime`, check combined token quotas and RPM, if the model has an RPM quota.

HTTP 503  
A 503 response means that the service is temporarily unable to handle the request because of high demand or a capacity constraint. It does not indicate that you exceeded an account quota. Retry transient responses with exponential backoff and jitter. If the response persists, stop increasing traffic, reduce concurrency, and consider a different Region or cross-Region inference when supported.

HTTP 529 (`overloaded_error`)  
Some model APIs return 529 when the model is temporarily unable to process the request because of high demand or insufficient serving capacity. Treat it as a transient capacity error. If the response includes a `Retry-After` header, wait for at least that duration before retrying, and add jitter so that clients do not retry simultaneously.

For API-specific causes and resolution steps, see [Troubleshooting Amazon Bedrock API Error Codes](troubleshooting-api-error-codes.md).

## Recommended error handling
<a name="scaling-error-handling"></a>

### Transient errors
<a name="scaling-transient-errors"></a>

Retry only errors that are safe to retry, such as transient throttling and capacity errors. If the service returns a `Retry-After` header, honor it. Otherwise, implement exponential backoff with random jitter:
+ Start with a short delay (for example, 1 second).
+ Increase the delay after each retry and cap the maximum delay to fit your application's latency budget.
+ Add random jitter and avoid synchronized retries across workers.
+ Use a bounded retry budget that fits your application's latency objective. For example, limit the operation to six total attempts: the initial request and up to five retries.

Most AWS SDKs and popular HTTP libraries provide built-in support for this pattern. Retry-setting names differ: botocore's `total_max_attempts` includes the initial request, while the OpenAI and Anthropic SDKs' `max_retries` counts only retries. The following examples therefore use different numeric values to provide the same example six-attempt budget.

**Example Retry configuration for `bedrock-runtime` (AWS SDK / boto3)**  

```
import boto3
from botocore.config import Config

config = Config(retries={"total_max_attempts": 6, "mode": "standard"})
client = boto3.client("bedrock-runtime", config=config)
```

**Example Retry configuration for `bedrock-mantle` (OpenAI SDK)**  

```
from openai import OpenAI

client = OpenAI(
    api_key=api_key,
    base_url=f"https://bedrock-mantle.{region}.api.aws/v1",
    max_retries=5,
)
```

**Example Retry configuration for `bedrock-mantle` (Anthropic SDK)**  

```
import anthropic

client = anthropic.Anthropic(
    api_key=api_key,
    base_url=f"https://bedrock-mantle.{region}.api.aws/anthropic",
    max_retries=5,
)
```

Configure connection and read timeouts separately from retries, based on the model and operation's documented maximum inference duration. A timeout that is shorter than a valid long-running inference request can cause avoidable retries and duplicate work.

### Sustained capacity errors
<a name="scaling-sustained-errors"></a>

If you receive persistent 503 or 529 errors, retries alone can amplify load. The service might be experiencing a temporary capacity constraint, or the workload might exceed the capacity currently available for the model and Region. Take the following steps:
+ Stop the ramp and return to the last stable request rate and concurrency level.
+ Use bounded client-side concurrency, rate limiting, and request queues.
+ Defer or shed lower-priority requests until capacity recovers.
+ For `bedrock-runtime`, use cross-Region inference when the model supports it. For predictable, sustained workloads, evaluate [Provisioned Throughput](prov-throughput.md).
+ If the problem continues, check the AWS Health Dashboard and contact AWS Support with request IDs and UTC timestamps.

## Ramping up throughput
<a name="scaling-ramp-up"></a>

On-demand capacity can vary by model, Region, and time. Not all requests within a quota are guaranteed to succeed during periods of high demand, so ramp gradually when launching a workload, changing models or Regions, or making a large traffic increase. This is especially important for `bedrock-mantle` models that do not have a published per-account quota.

### Recommended ramp-up procedure
<a name="scaling-ramp-procedure"></a>

1. Estimate the target token rate and concurrency for each endpoint, model, and Region. For `bedrock-mantle`, track input and output tokens separately and include the requested `max_tokens` value in the input-token admission estimate.

1. Begin at a known stable baseline below the target. If you do not have a baseline, start with a small representative load instead of sending the full target volume.

1. Hold each level long enough to observe request success, 429/503/529 errors, latency percentiles, token consumption, concurrency, and queue depth.

1. Increase one controlled step at a time. Change only one major load dimension at a time so that you can identify the cause of a regression.

1. If throttling, capacity errors, or latency rise beyond your threshold, pause the ramp, honor any `Retry-After` header, and return to the last stable level.

1. Continue until you reach the target, and repeat the validation for every model and Region that will receive production traffic.

Choose the step size and observation period from your workload's latency and traffic pattern. Do not use RPM as the only control signal: request token sizes and response lengths can change capacity consumption substantially even when RPM stays constant.

For `bedrock-mantle` quota increases, follow [Requesting a quota increase](quotas-mantle.md#quotas-mantle-increase). For `bedrock-runtime`, follow [Requesting a quota increase](quotas-runtime.md#quotas-runtime-increase).

## Additional best practices
<a name="scaling-additional-best-practices"></a>
+ Use feature flags to gradually transition traffic between models rather than switching all traffic at once.
+ Spread large workloads across multiple minutes and consider time-of-day patterns to avoid peak usage periods.
+ Test with representative distributions of input size, output size, latency, and concurrency. Avoid sending a sudden burst of test requests.
+ Use token-aware client-side rate limiting, bounded concurrency, and bounded queues. An RPM-only limiter does not protect against changes in request size.
+ For asynchronous, high-volume offline jobs, use [batch inference](batch-inference.md) on `bedrock-runtime`.
+ For supported models and non-time-sensitive requests that can tolerate variable latency, consider the [Flex service tier](service-tiers-inference.md).

## Regional availability and cross-Region inference
<a name="scaling-regional-availability"></a>

On-demand capacity is Regional and can vary across Regions. If your workload targets a single Region, it can encounter capacity errors during periods of high demand. With [`bedrock-runtime`](endpoints.md), use [Global cross-Region inference](global-cross-region-inference.md) when the model and your data-residency requirements support it. If you implement your own Regional failover, verify model availability in every target Region and apply bounded retries so that failover does not create a traffic surge.

## Getting help
<a name="scaling-getting-help"></a>
+ **Throughput planning** — Estimate peak input and output tokens, response latency, concurrency, and queueing tolerance for each model and Region. Include workload-specific headroom, and contact your AWS account team for large or business-critical launches.
+ **Performance optimization** — Monitor prompt size, generated tokens, `max_tokens`, latency percentiles, and cache usage when supported. Optimize prompts and output limits to avoid reserving or consuming unnecessary tokens.
+ **Support escalation** — When opening an AWS Support case, include the endpoint, Region, model or inference profile ID, HTTP status and API error type, request IDs, UTC timestamps, token rate, request rate, concurrency, and your scaling timeline.

## Summary of recommendations
<a name="scaling-summary"></a>


| Scenario | Recommendation | 
| --- | --- | 
| General workloads | Start with bedrock-runtime. Use bedrock-mantle for capabilities or models that require it. See [Endpoints supported by Amazon Bedrock](endpoints.md). | 
| Transient 429, 503, or 529 errors | Inspect the API error type. For retryable errors, honor Retry-After and retry with exponential backoff and jitter within a bounded retry budget. | 
| Sustained capacity errors | Stop ramping, return to the last stable level, bound concurrency and queues, defer lower-priority work, and use cross-Region inference where supported. | 
| Quota planning | Use separate input and output TPM for bedrock-mantle. Use combined token quotas, token burndown, and RPM where applicable for bedrock-runtime. | 
| Large offline processing | Use [batch inference](batch-inference.md) for asynchronous jobs. Use the [Flex service tier](service-tiers-inference.md) for supported, non-time-sensitive requests that can tolerate variable latency. | 