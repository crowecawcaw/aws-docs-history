

# Best practices for Lambda Web Functions
<a name="web-functions-best-practices"></a>

## Secure every endpoint
<a name="web-functions-best-practices-security"></a>

Every endpoint is reachable from the internet, so how you authenticate callers, put a front door in place, and scope permissions determines who can reach your application and what it can access. Use the following practices:
+ Every endpoint is reachable from the internet, whatever its authentication type. With `ApplicationManaged`, Lambda does not authenticate requests, so any client that knows the domain can call your application. Implement authentication, authorization, input validation, request-size checks, and abuse protection in the application or in a front door.
+ Use `IamAuth` when callers can sign requests and IAM policies provide the required authorization model. Scope resource policies to specific endpoint ARNs and principals.
+ Put Amazon CloudFront or Amazon API Gateway in front of an endpoint when you need a custom domain, AWS WAF inspection, caching, or centralized edge controls. Restrict the origin so clients cannot bypass the front door. With CloudFront, use an `IamAuth` endpoint and origin access control (OAC), as described in [CloudFront integration](web-functions-endpoint-access-control.md#web-functions-endpoint-access-control-cloudfront). With other front doors, the endpoint remains directly reachable, so verify a shared secret or token in the application.
+ Use a dedicated execution role with least-privilege permissions. Separate the deployment identity, code uploader, Lambda service principal, execution role, and endpoint caller permissions.
+ Do not put secrets in deployment packages or logs. Load secrets at runtime from an appropriate secret store, cache them only as long as needed, and redact sensitive request fields.

## Retain immutable deployment artifacts
<a name="web-functions-best-practices-artifacts"></a>
+ Enable versioning on the code bucket and record the object version ID for every deployment.
+ Do not overwrite or delete object versions used by active or rollback revisions. Keep Lambda service-principal access for as long as a revision references the object.
+ Build deployment packages in a repeatable pipeline. Install production dependencies from a lock file, exclude development files, and test the exact archive before upload.
+ Build native dependencies for Arm64. A native module built for x86\_64 does not run in the Web Function execution environment.
+ Use separate buckets, prefixes, roles, or accounts when environments have different trust or retention requirements.

## Design for concurrent requests
<a name="web-functions-best-practices-runtime"></a>
+ Keep request-specific data in request scope. Do not store credentials, customer data, response objects, or mutable per-request state in global variables.
+ Use asynchronous I/O. Synchronous CPU or file-system work blocks the Node.js event loop and delays every in-flight request in the environment.
+ Use `worker_threads` for CPU-intensive work that should use multiple vCPUs, or lower `maxConcurrencyPerEnvironment` to reduce contention.
+ Account for the Node.js heap separately from environment memory. The environment has 2 GB, while the default V8 heap is 1,024 MB. If you raise the heap with `--max-old-space-size` in `NODE_OPTIONS`, leave memory for buffers, native modules, the runtime, and concurrent requests.
+ Reuse initialized clients and connection pools across requests, but validate stale connections and bound cache growth. Persist required state outside the execution environment.
+ Keep outbound connections alive so that requests to databases and other dependencies reuse them instead of opening a new connection each time. Node.js enables keep-alive by default in its global HTTP agent. If you create your own agent or configure an SDK client, keep keep-alive enabled. Also handle connections that the remote side closes while they are idle.
+ Use unique names for temporary files and remove them when they are no longer needed. Multiple requests share the environment's 512 MB `/tmp` file system, and files can persist across requests until the environment is removed.

## Keep startup predictable
<a name="web-functions-best-practices-startup"></a>
+ Start the HTTP server promptly and listen on the exact value of `AWS_LAMBDA_HTTP_ENDPOINT`.
+ Keep the package small and remove unused production dependencies.
+ Initialize only the resources needed before the server can accept traffic. Perform optional work lazily, but prevent concurrent requests from duplicating expensive initialization.
+ Handle `SIGTERM` for cleanup that finishes within 1 second, but do not rely on shutdown callbacks to persist required data.

## Set limits from measured behavior
<a name="web-functions-best-practices-scaling"></a>
+ Load test with the same application dependencies and downstream services used in production. Increase concurrency until latency, CPU consumption, memory, or downstream capacity becomes the binding constraint.
+ Use `maxConcurrencyPerEnvironment` to bound per-process contention, `maxEnvironments` to bound horizontal scale, and `rateLimit` to protect downstream dependencies from request bursts.
+ Check applied account and Regional limits before performance tests and launches. Endpoint configuration cannot create capacity beyond an account limit.
+ Retry HTTP 429 responses and HTTP 503 responses that have no `lambda-web-error-type` header. Use backoff and jitter, and retry only when the operation is idempotent. Use idempotency keys or application-level deduplication for writes.

## Deploy with explicit verification and rollback
<a name="web-functions-best-practices-deployment"></a>
+ Use manual revision weights for production endpoints. Keep automatic latest revision deployment for development environments where immediate rollout is acceptable.
+ Wait until the new revision is `Active` and the endpoint update is complete before you evaluate it. For `MultiRegion` and `PerRegion` endpoints, verify the update status in every Region.
+ Use application logs or custom metrics that include the revision identifier during canary deployments. Service-vended metrics do not include a revision dimension.
+ Before you shift traffic, define the metrics that a new revision must meet and how long you observe them (bake criteria), and the thresholds that trigger a rollback. Preserve the previous revision's code object version, key access, and configuration until the rollback window ends. Lambda automatically deletes the oldest revisions that no endpoint routes to when a Web Function exceeds its revision limit, so keep the rollback revision on an endpoint (for example, a test endpoint) or be ready to recreate it from the same object version. For details, see [Revision limits and automatic cleanup](web-functions-revisions.md#web-functions-revisions-limits).

## Build an operational baseline
<a name="web-functions-best-practices-observability"></a>
+ Emit structured application logs with request ID, revision ID, route, status code, duration, and the identifiers needed to diagnose downstream failures. Do not log credentials, tokens, or sensitive request bodies.
+ Alarm on 5xx responses and throttles, and monitor executed requests, active environments, and account capacity. Configure sparse error metrics to treat missing data appropriately.
+ Use the response request ID and log-stream headers to correlate client failures with logs. Enable DEBUG system logs only while you need the additional events.
+ Record management operations and endpoint invocation data events in AWS CloudTrail when your audit requirements need them.

## Operate MultiRegion and PerRegion endpoints as distributed systems
<a name="web-functions-best-practices-multi-region"></a>
+ Make application data, secrets, keys, and downstream dependencies available in every Region that can receive traffic.
+ Test partial deployment failures and Regional dependency failures. Do not assume that all Regions run the same revision until every Regional update reports success.
+ After every endpoint update, check `updateStatus` for each entry in `regionalEndpoints`. Replication can fail in some Regions while it succeeds in others. As a result, an update can be partly applied. Retry or roll back before you treat the deployment as complete.
+ For `PerRegion` endpoints, test your external DNS or front-door failover independently from the Web Function deployment.
+ Centralize operational views in the home Region, but keep a recovery path for telemetry delays or disruptions.