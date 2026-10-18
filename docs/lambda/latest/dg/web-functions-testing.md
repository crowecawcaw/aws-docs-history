

# Testing Lambda Web Functions
<a name="web-functions-testing"></a>

Web Functions run standard HTTP servers, so you can test most application behavior locally with your framework's normal tools. Cloud tests are still required to validate IAM authorization, Amazon S3 and AWS Key Management Service (AWS KMS) access, Web Function lifecycle states, scaling, telemetry, and multi-Region behavior.

## Recommended test layers
<a name="web-functions-testing-strategy"></a>

The following table describes each test layer, what it validates, and where it runs.


| Test layer | What it validates | Where it runs | 
| --- | --- | --- | 
| Unit | Business logic, validation, authorization decisions, serialization, and error handling. | Local development and build environments. | 
| HTTP integration | Routes, middleware, headers, streaming, timeouts, graceful disconnects, and framework behavior. | Against a locally running production server. | 
| Package | Entry file, production dependencies, archive layout, startup, and the server's use of AWS\_LAMBDA\_HTTP\_ENDPOINT. | From the exact archive that the deployment pipeline uploads. | 
| Cloud integration | IAM, bucket policies, keys, lifecycle states, endpoint behavior, telemetry, and downstream AWS service calls. | In an isolated AWS account or test environment. | 
| Load and resilience | Concurrency safety, latency, throttling, downstream limits, rollback, and Regional failure behavior. | In a production-like cloud environment with explicit cost and traffic controls. | 

## Run the HTTP server locally
<a name="web-functions-testing-local"></a>

Use a local fallback for `AWS_LAMBDA_HTTP_ENDPOINT`, as shown in the [Minimal Express application](web-functions-samples.md#web-functions-samples-express). You can also set the variable explicitly to test the same startup path used by Lambda:

```
AWS_LAMBDA_HTTP_ENDPOINT=127.0.0.1:3000 node index.js
```

Send requests with your normal HTTP client and verify status codes, response bodies, headers, request validation, authentication middleware, timeouts, streaming, and client disconnect handling.

Run concurrent requests during local integration tests. Check for global request state, shared mutable caches, duplicate initialization, file name collisions, and event-loop blocking.

## Test the deployment package
<a name="web-functions-testing-package"></a>

1. Install dependencies from the committed lock file and create the archive using the same commands as the deployment pipeline.

1. Extract the archive into a clean directory. Run the application from that directory without access to development dependencies or untracked source files.

1. Verify that the configured entry file exists at the expected path and starts the HTTP server.

1. Record the archive checksum and the Amazon S3 object version ID used by the revision. Use those values to identify the exact artifact under test.

Web Functions run on Arm64. When a package contains native dependencies, build and test those dependencies for Linux Arm64 rather than reusing artifacts from an x86-64 development computer. For example, you can install production dependencies in an Arm64 container:

```
docker run --rm --platform linux/arm64 \
    --volume "$PWD":/app \
    --workdir /app \
    node:24 \
    npm ci --omit=dev
```

## Test in an isolated cloud environment
<a name="web-functions-testing-cloud"></a>

1. Upload the tested archive to a versioned Amazon S3 bucket and create a revision that references the resulting object version.

1. Poll the revision until it becomes `Active` or `Failed`. Fail the test with the reported `stateReason` instead of waiting indefinitely.

1. Create or update a test endpoint. Poll both `state` and `updateStatus`. For `MultiRegion` and `PerRegion` endpoints, verify every Regional status.

1. Send requests to the endpoint and verify the application response, `lambda-web-request-id`, logs, metrics, and expected downstream side effects.

1. Delete the endpoint, function, test objects, log groups, and other test resources when the test completes.

## Test authorization and exposure
<a name="web-functions-testing-security"></a>
+ For `IamAuth`, verify that unsigned requests fail, permitted principals succeed, denied principals fail, and cross-account access requires both identity and resource policies.
+ For `ApplicationManaged`, test missing, expired, malformed, and insufficient application credentials. Test authorization separately from authentication.
+ Test browser preflight requests, allowed and denied origins, credentialed requests, and security headers when browsers call the endpoint.
+ When a front door protects the endpoint, verify that direct origin requests are denied and that only the expected front-door identity or network path can invoke it.

## Test concurrency, scaling, and throttling
<a name="web-functions-testing-load"></a>
+ Increase load gradually while recording latency, 4xx and 5xx responses, throttles, active environments, and downstream utilization.
+ Test the configured `rateLimit`, `maxEnvironments`, and `maxConcurrencyPerEnvironment` independently. Use the `lambda-web-error-type` response header (`Platform.EndpointRequestThrottle`, `Platform.AccountRequestThrottle`, `Platform.EndpointMaxEnvThrottle`, `Platform.AccountActiveVCPUArm64Throttle`, or `Platform.EndpointConcurrentInitThrottle`) to confirm which limit produced each HTTP 429 response. Record HTTP 503 responses that have no `lambda-web-error-type` header separately. These responses can indicate temporary load shedding or an internal error. For details, see [Web Function error types](web-functions-troubleshooting.md#web-functions-troubleshooting-error-types).
+ Test traffic bursts and cold starts, not only steady-state throughput.
+ Use unique test data and idempotency keys. Do not retry non-idempotent requests automatically during a load test.
+ Set explicit traffic, duration, and cost limits before starting a load test. Coordinate tests that can affect shared account quotas or downstream systems.

## Test deployments and rollback
<a name="web-functions-testing-deployments"></a>

In a test environment, deploy two revisions and exercise the same weighted routing procedure used in production. Verify that your logs or custom metrics can attribute requests to each revision. Trigger the rollback conditions deliberately, restore all traffic to the previous revision, and confirm that its code object and dependencies remain available.

For a `MultiRegion` or `PerRegion` endpoint, test a partial update failure and confirm that your deployment automation detects the failed Regional status. Test the recovery action and repeat the endpoint update after correcting the cause.