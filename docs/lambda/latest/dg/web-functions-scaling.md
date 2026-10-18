

# Scaling behavior for Lambda Web Functions
<a name="web-functions-scaling"></a>

Lambda scales your Web Function's endpoint automatically as traffic arrives. It scales in two dimensions:
+ **Number of environments** – Lambda adds more execution environments, up to `maxEnvironments`.
+ **Concurrent requests per environment** – Each environment handles multiple requests at once. Lambda manages a dynamic per-environment concurrency limit based on your resource usage. You control the upper bound of this dynamic limit using `maxConcurrencyPerEnvironment`. For more information, see [Dynamic per-environment concurrency limit](#web-functions-scaling-dynamic-concurrency).

You can also set `rateLimit` on an endpoint to limit its request arrival rate. This is an optional setting and is applied before requests reach your environments.

An endpoint scales from zero. When there is no traffic, Lambda runs no environments. This page explains an endpoint's scaling settings, the related account quotas, and how to choose values that optimize cost or performance.

## Execution environments
<a name="web-functions-scaling-environments"></a>

An execution environment is an isolated compute instance that runs your HTTP server. Each environment has its own memory, file system, and process space. For how Lambda initializes, reuses, and shuts down an execution environment, see [Execution environment lifecycle](web-functions-env-lifecycle.md).

Lambda creates and removes environments automatically based on traffic:
+ When traffic increases, Lambda creates additional environments to meet the traffic demand.
+ When traffic decreases, Lambda drains underutilized environments and removes them.
+ When there is no traffic, Lambda removes all environments. The endpoint scales to zero.

There is no minimum or reserved-environment setting. An endpoint always scales from zero as traffic arrives. To avoid cold starts for small traffic increases, Lambda automatically scales up execution environments ahead of demand to maintain spare capacity (headroom) for incoming traffic. When environments are underutilized, Lambda scales them down, including to zero.

## Dynamic per-environment concurrency limit
<a name="web-functions-scaling-dynamic-concurrency"></a>

The dynamic per-environment concurrency limit is a Lambda-managed limit on the number of requests that a single execution environment handles at the same time. Based on your function's resource usage, Lambda automatically adjusts this limit to optimize efficiency and performance. Lambda scales up new environments when existing environments are close to their limit. When the limit prevents all existing environments from accepting more requests, requests queue, waiting for the next available environment.

For a new Web Function, Lambda sets a conservative starting limit and quickly adjusts it based on the function's resource usage. For more information about how the limit changes while handling load, see [Dynamic concurrency limit of a new Web Function](#web-functions-scaling-examples-dynamic-limit).

You don't configure the dynamic limit directly. Instead, you can apply an upper bound to it by setting `maxConcurrencyPerEnvironment` on the revision. Lambda's dynamic limit can be lower than this value, but never exceeds it. For example, if you set `maxConcurrencyPerEnvironment` to 32, Lambda routes at most 32 concurrent requests to any environment, even if the environment has capacity for more.

Most applications can rely on the dynamic limit without changing `maxConcurrencyPerEnvironment`. For guidance on when to change it, see [Choosing scaling settings](#web-functions-scaling-optimization).

## Scaling settings
<a name="web-functions-scaling-settings"></a>

Three settings control how Lambda scales your Web Function. You configure each setting on either the endpoint or the revision.


| Setting | Configured on | Valid range | Default | Description | 
| --- | --- | --- | --- | --- | 
| maxConcurrencyPerEnvironment | Revision | 1–128 | 64 | The upper bound of the Lambda-managed dynamic per-environment concurrency limit. Lambda adjusts the actual per-environment concurrency automatically, so most applications can rely on the dynamic limit without changing this value. | 
| maxEnvironments | Endpoint | Optional. 2–10,000 | None | Constrains the number of execution environments for the endpoint in each AWS Region. Controls horizontal scale. Endpoint environment scaling is always bounded by available account vCPU quota, even if maxEnvironments is not set. | 
| rateLimit | Endpoint | Optional. 0–10,000 | None | Limits the endpoint's request arrival rate, in requests per second, in each AWS Region. Values up to 1,000 must be a multiple of 100, and values above 1,000 must be a multiple of 1,000. A value of 0 blocks all traffic. Requests above the effective rate limit receive an HTTP 429 (Too Many Requests) response. When not set, the endpoint's arrival rate is limited by the account per-endpoint rate quota. | 

`maxEnvironments` and `rateLimit` are optional endpoint properties. You can update them without creating a new revision. By default, neither is set. A large `maxEnvironments` does not guarantee that the endpoint can scale that far. Environment scaling is always bounded by the account's regional vCPU quota. A `rateLimit` of 0 blocks all traffic. For details, see [Throttling](#web-functions-scaling-throttling). Endpoint request rate is always bounded by the account's request rate quota, even when `rateLimit` is not set. For the quotas, see the next section.

To change `maxEnvironments` or `rateLimit`, run `aws lambda-web update-web-function-endpoint` with the `--scaling-config` or `--throttle-config` parameter, for example `--scaling-config '{"maxEnvironments": 50}'` or `--throttle-config '{"rateLimit": 8000}'`. Omit a parameter to keep its current value. To clear a value that you set, pass an empty object, such as `--scaling-config '{}'`. For more information, see [Updating an endpoint](web-functions-endpoints.md#web-functions-endpoint-update). `maxConcurrencyPerEnvironment` is a revision setting. To change it, create a new revision. Whether the new revision receives traffic depends on the endpoint's auto-deployment mode. For more information, see [Creating a revision](web-functions-revisions.md#web-functions-revisions-create).

## Account quotas
<a name="web-functions-scaling-quotas"></a>

These quotas apply per AWS Region. They always apply in addition to your optionally configured endpoint limits.
+ Per-endpoint rate limit – 10,000 requests per second (RPS).
+ Account total rate limit – 100,000 RPS across all endpoints in the Region.
+ Account vCPU limit – 2,000 vCPUs across all endpoints in the Region. Each execution environment consumes 2 vCPUs, so this quota bounds the total number of environments per AWS Region across the account.

For the current quota values and how to request an increase, see [Lambda Web Functions](gettingstarted-limits.md#web-functions-quotas).

## How scaling settings interact
<a name="web-functions-scaling-interaction"></a>

These three scaling settings operate independently to determine your endpoint's scale. Except for account quotas, each endpoint scales independently, even endpoints belonging to the same Web Function.

Total concurrency capacity  
You can think of the endpoint's peak number of in-flight requests as roughly `maxEnvironments` times the dynamic per-environment concurrency limit that Lambda currently allows. The most the endpoint can handle at once is `maxEnvironments` × `maxConcurrencyPerEnvironment`. It reaches that number only when it runs `maxEnvironments` environments and each one handles `maxConcurrencyPerEnvironment` requests. If `maxEnvironments` is not set, the endpoint scales to meet demand, up to the account vCPU quota.

Total request rate limit  
`rateLimit` limits requests per second, independently of concurrency capacity. Lambda returns HTTP 429 for requests above the rate limit, even when environments have capacity to serve them.

Scaling up  
Before all environments reach the dynamic concurrency limit, Lambda scales up more environments, up to `maxEnvironments`. An endpoint stops scaling up when it reaches `maxEnvironments` or the account vCPU quota. If an endpoint is unable to scale up, and all existing environments are fully utilized, Lambda immediately throttles new requests with an HTTP 429 (Too Many Requests) response. Lambda does not queue throttled requests. If a new execution environment is initializing, requests queue instead of being throttled immediately.

Temporary overshoot  
During revision weight changes, internal fleet cycling, and other operational events, Lambda might temporarily exceed `maxEnvironments` to prioritize availability. This overshoot is brief, and Lambda returns to the configured limit automatically. You do not have to budget headroom for these operational events when you choose `maxEnvironments`.

**Example: capacity calculation**  
You configure the following settings for your Web Function:  
+ `maxEnvironments` = 10
+ `maxConcurrencyPerEnvironment` = 64
+ `rateLimit` = 8000
These settings limit concurrency (requests in flight at once) and request rate (requests accepted per second) separately. With up to 10 environments and up to 64 concurrent requests each, the endpoint can serve at most about 640 concurrent requests (10 × 64). The dynamic limit is often lower, so sustained concurrency is usually less. Which limit the endpoint reaches first depends on how long each request takes.    
Concurrency-bound endpoint  
Suppose that each request takes 200 ms, for example because it waits on a database query. With 640 requests in flight, the endpoint completes at most about 3,200 requests per second (640 ÷ 0.2 s), which is below the 8,000 RPS `rateLimit`. When all 10 environments are fully utilized, Lambda throttles new requests with HTTP 429. To serve more traffic, increase `maxEnvironments`.  
Request-rate-bound endpoint  
Suppose that each request takes 10 ms. At 8,000 requests per second, about 80 requests are in flight (8,000 × 0.01 s), well below 640. Lambda returns HTTP 429 for requests above 8,000 RPS, even though environments have capacity to serve them. To accept more requests, increase `rateLimit`, up to the 10,000 RPS per-endpoint quota.

## Throttling
<a name="web-functions-scaling-throttling"></a>

When the incoming request rate exceeds the `rateLimit` setting, Lambda returns an HTTP 429 (Too Many Requests) response for excess requests. The rate limit applies to the endpoint as a whole in each AWS Region.

Lambda also returns an HTTP 429 response when all environments are fully utilized, either because the endpoint reached `maxEnvironments` or the account reached its vCPU quota. For more information, see [How scaling settings interact](#web-functions-scaling-interaction).

Lambda can also return HTTP 429 with the `Platform.EndpointConcurrentInitThrottle` error type when too many execution environments are initializing at the same time. This throttle doesn't increment a throttle metric. For the metrics that the other throttle types increment, see [Using CloudWatch metrics with Lambda Web Functions](web-functions-monitoring-metrics.md).

When an endpoint's `rateLimit` is 0, Lambda returns HTTP 503 (Service Unavailable) instead of HTTP 429, with the `lambda-web-error-type` header `Platform.EndpointDisabled`. Lambda can also return HTTP 503 when it sheds load to protect the service. Retry a 503 that has no `lambda-web-error-type` header with backoff and jitter. A 503 with `Platform.EndpointDisabled` continues until you set `rateLimit` to a nonzero value.

Lambda measures the rate limit on a per-second basis. Brief bursts above the limit might be accepted. Sustained traffic above the limit results in throttling.

When your application receives HTTP 429 responses, implement exponential backoff with jitter in your client code to retry throttled requests.

## Scaling up and scaling down
<a name="web-functions-scaling-lifecycle"></a>

### Scale up
<a name="web-functions-scaling-scale-up"></a>

When traffic increases and existing environments approach the dynamic per-environment concurrency limit, Lambda creates additional execution environments. Each new environment initializes before it serves requests. For the initialization steps and the startup time limit, see [Initialization (cold start)](web-functions-env-lifecycle.md#web-functions-env-lifecycle-init).

While a new environment initializes, Lambda routes requests to existing environments that have available capacity. When no environment has capacity, the request waits while Lambda initializes a new one (a cold start). Lambda returns HTTP 429 only when one of the limits in [Throttling](#web-functions-scaling-throttling) applies, such as `maxEnvironments` or the account vCPU quota.

### Scale down
<a name="web-functions-scaling-scale-down"></a>

When traffic decreases, Lambda identifies underutilized environments and removes them. Lambda drains an environment before removing it. It stops routing new requests to the environment, lets in-flight requests finish on a best-effort basis, and sends `SIGTERM`. For details, see [Execution environment lifecycle](web-functions-env-lifecycle.md).

Lambda scales down to zero environments when there is no traffic. The next request after that starts a new environment (a cold start).

## Choosing scaling settings
<a name="web-functions-scaling-optimization"></a>

Consider the following when you choose values for endpoint `rateLimit`, endpoint `maxEnvironments`, and revision `maxConcurrencyPerEnvironment`.

Choosing `rateLimit`  
The default value is none, which means an endpoint's request rate is constrained by both the 10,000 per-endpoint RPS quota and 100,000 account RPS quota. Consider setting a `rateLimit` value when you want to limit how much an endpoint can claim from your account RPS quota, which is shared by all of your endpoints.  
Setting a `rateLimit` may also be helpful to limit total traffic to downstream dependencies.

Choosing `maxEnvironments`  
The default value is none, which means an endpoint's environment count is only constrained by the account vCPU quota. Consider setting a `maxEnvironments` value when you want to limit how much an endpoint can claim from your account vCPU quota, which is shared by all of your endpoints.  
When setting a `maxEnvironments` value, consider monitoring the endpoint's environment count so you are alerted when it is close to your `maxEnvironments` limit, and take action to avoid throttling for an application that has organic growth over time.  
Setting a low value of `maxEnvironments` can help limit the cost of running environments for your endpoint. Consider using a low value for non-critical hobby projects.

Choosing `maxConcurrencyPerEnvironment`  
A revision's `maxConcurrencyPerEnvironment` is the upper bound to Lambda's managed dynamic per-environment concurrency limit. The default value is 64, and most users should not have to select an optimal value.  
For memory-bound applications, setting `maxConcurrencyPerEnvironment` lower than the default can help achieve more predictable behavior.  
For CPU-bound applications, setting `maxConcurrencyPerEnvironment` lower than the default may reduce CPU contention and improve steady state latency of warm environments, but may also result in more frequent cold starts. Setting `maxConcurrencyPerEnvironment` higher than the default will likely have no effect if Lambda's managed dynamic concurrency limit is limiting traffic to the environment.  
For I/O-bound applications, setting `maxConcurrencyPerEnvironment` higher than the default may improve per-environment utilization and lower cost.

Monitor the following CloudWatch metrics to determine if your scaling settings are appropriate. For metric definitions, see [Using CloudWatch metrics with Lambda Web Functions](web-functions-monitoring-metrics.md).
+ `EndpointRequestThrottles` and `AccountRequestThrottles` – If `EndpointRequestThrottles` is consistently greater than zero, increase `rateLimit`, up to the per-endpoint quota of 10,000 RPS. `AccountRequestThrottles` increments when the account reaches its request-rate quota in the Region. To reduce these throttles, request a quota increase, or lower `rateLimit` on other endpoints.
+ `EndpointActiveEnvironmentThrottles` and `AccountActiveVCPUArm64Throttles` – These metrics increment when `maxEnvironments` or the account vCPU quota prevents additional scale-out. To reduce these throttles, increase `maxEnvironments` or request a vCPU quota increase.
+ `EndpointActiveEnvironments` and `EnvironmentConcurrentRequests` – If active environments approach `maxEnvironments`, or concurrent requests per environment stay near `maxConcurrencyPerEnvironment`, increase the relevant setting.
+ Application latency – Measure latency with an application metric, from structured logs, or with your front door's latency measurements. If latency increases as per-environment concurrency rises, reduce `maxConcurrencyPerEnvironment` to reduce per-environment contention and spread the load across more environments.

## Scaling for MultiRegion and PerRegion endpoints
<a name="web-functions-scaling-multi-region"></a>

For Web Functions with **MultiRegion** or **PerRegion** endpoints, the scaling settings apply independently in each AWS Region where the endpoint operates.

Each Region creates and manages its own pool of execution environments. Traffic in one Region does not consume the scaling capacity of another Region.

## Scaling examples
<a name="web-functions-scaling-examples"></a>

Lambda scales your endpoint to maintain headroom above its current load. Headroom is the difference between incoming request load and the total request load that warm execution environments can serve. It absorbs small traffic increases without waiting for new environments to start. Capacity increases in steps, because each new environment adds capacity only after it finishes initializing. When the endpoint reaches a limit, capacity stops growing, and Lambda throttles requests that exceed what the endpoint can accept.

The following examples show how the endpoint handles a traffic burst, how the dynamic per-environment concurrency limit changes during load tests on a new Web Function, and how the endpoint behaves when load reaches each type of limit. The charts illustrate general behavior and are not drawn to scale.

### Handling a traffic burst
<a name="web-functions-scaling-examples-burst"></a>

When load grows gradually, headroom absorbs the increase while Lambda scales up new environments in the background. When load rises faster than headroom can absorb, the warm environments can't handle all incoming requests. Lambda starts new environments to handle the load above headroom, and those requests wait for the new environments to cold start. After the new environments are ready, Lambda restores headroom above the new load.

![Chart of incoming load rising gently, then sharply. The RPS supported by warm environments rises in steps. Headroom absorbs the gentle rise. During the sharp rise, requests above warm capacity wait on cold starts.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-scaling-burst.png)


### Dynamic concurrency limit of a new Web Function
<a name="web-functions-scaling-examples-dynamic-limit"></a>

The dynamic per-environment concurrency limit starts conservatively for a new Web Function. As the function handles traffic, Lambda learns from its resource usage and adjusts the limit. Lambda remembers what it learned when the function scales to zero, so environments that start later benefit from earlier traffic.

The following charts show the first load test on a new Web Function. Incoming load rises quickly to a steady request rate and holds it. The dynamic concurrency limit starts low, increases as Lambda adjusts it based on the function's resource usage, and levels off below `maxConcurrencyPerEnvironment`.

![Charts of a first load test. Load holds steady while the concurrency limit starts low and levels off.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-scaling-load-test-first.png)


Because Lambda remembers what it learned from prior traffic, later load tests on the same Web Function don't start conservatively.

The following charts show a later load test on the same Web Function. Incoming load rises to the same steady request rate, and the dynamic concurrency limit starts at the level Lambda learned in the prior run.

![Charts of a later load test. Load holds steady while the concurrency limit starts at the level learned in the prior run.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-scaling-load-test-later.png)


Because the limit starts conservatively, the first load test on a new Web Function might use more execution environments than later runs. To measure the performance your function can expect under steady traffic, run the load test more than once and use the results from later runs.

### Reaching the per-endpoint request rate limit
<a name="web-functions-scaling-examples-rate"></a>

The request rate limit caps how much load the endpoint can accept, so capacity doesn't grow past it. As load approaches the per-endpoint rate quota or your `rateLimit` setting, headroom shrinks. When load exceeds the limit, Lambda returns HTTP 429 for requests above it. To accept more requests, increase `rateLimit`, up to the per-endpoint rate quota.

![Chart of the RPS supported by warm environments rising in steps with load up to the per-endpoint request rate limit, then staying flat. Headroom narrows as load rises, and requests above the limit are throttled.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-scaling-rps-limit.png)


### Reaching maxEnvironments
<a name="web-functions-scaling-examples-max-environments"></a>

In this example, `maxEnvironments` is lower than the request rate limit. When the endpoint reaches `maxEnvironments`, Lambda stops adding execution environments. Load can keep growing, so headroom shrinks. When load exceeds what the environments can handle, Lambda throttles new requests with HTTP 429, even though the request rate is still below the rate limit. To allow more capacity, increase `maxEnvironments`.

![Chart of the RPS supported by warm environments rising in steps up to maxEnvironments, below the request rate limit, then staying flat. Headroom narrows as load rises, and requests above that capacity are throttled.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-scaling-max-environments.png)


### Reaching the account vCPU quota
<a name="web-functions-scaling-examples-vcpu"></a>

All endpoints in an account share the vCPU quota in each AWS Region. Environments used by other endpoints reduce how far this endpoint can scale. In this example, the vCPU quota available to the endpoint is lower than both its `maxEnvironments` setting and its request rate limit. When the account reaches the quota, Lambda stops adding environments and throttles requests that exceed the available capacity, even though the endpoint hasn't reached its own limits. To allow more capacity, request a vCPU quota increase.

![Chart of the RPS supported by warm environments rising in steps up to the vCPU quota available to the endpoint. The maxEnvironments setting and request rate limit are both higher. Requests above the quota are throttled.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-scaling-vcpu-quota.png)
