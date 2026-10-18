

# Troubleshooting Lambda Web Functions
<a name="web-functions-troubleshooting"></a>

Start with the resource state, the HTTP response, and the logs for the request. Web Functions expose separate state for the function, revision, endpoint, and each Region of a `MultiRegion` or `PerRegion` endpoint. A failure in one resource does not always change the state of the others.

**Note**  
Before you run the diagnostic commands in this topic, make sure that you have AWS CLI access and permission to call the Lambda Web Function `get-*` operations.

## Collect diagnostic information
<a name="web-functions-troubleshooting-first-steps"></a>

1. Get the Web Function, revision, and endpoint. Record each `state`, `stateReason`, `updateStatus`, and `updateStatusReason` value.

   ```
   aws lambda-web get-web-function \
       --function-name {{my-web-app}}
   
   aws lambda-web get-web-function-revision \
       --function-name {{my-web-app}} \
       --revision-id {{revision-id}}
   
   aws lambda-web get-web-function-endpoint \
       --function-name {{my-web-app}} \
       --endpoint-name {{prod}}
   ```

   Replace {{my-web-app}} with your function name, {{revision-id}} with the revision to inspect, and {{prod}} with your endpoint name.

1. Send a request and record the status code and response headers.

   ```
   curl --include https://{{endpoint-domain}}/{{path}}
   ```

   The `lambda-web-request-id` header identifies the request. When present, the `lambda-web-logstream` header identifies the Amazon CloudWatch Logs log stream that handled the request, and the `lambda-web-error-type` header identifies a platform error.

1. Review application and system logs in the centralized log group in the Web Function's home Region. For log group names and correlation guidance, see [Web Function logs in Amazon CloudWatch Logs](web-functions-logging.md).

1. For `MultiRegion` and `PerRegion` endpoints, inspect every entry in `regionalEndpoints`. A successful endpoint-level state does not mean that the most recent update succeeded in every Region.

## Deployment and startup issues
<a name="web-functions-troubleshooting-deployment"></a>


| Symptom | What to check | Resolution | 
| --- | --- | --- | 
| A revision is Failed | The revision's stateReason, the referenced Amazon S3 object version, bucket policy, execution role, runtime, and AWS KMS key. | Correct the underlying configuration and create a new revision. Revisions are immutable, and a failed revision does not return to Active. | 
| The endpoint is Active, but requests fail during application startup | System and application logs for entry-file errors, dependency errors, or a server that never listens on AWS\_LAMBDA\_HTTP\_ENDPOINT. | Run the packaged application locally, verify the entry file and production dependencies, and listen on the exact host and port that Lambda provides. Deploy the correction as a new revision. | 
| An endpoint update fails | updateStatusReason on the endpoint and, for MultiRegion and PerRegion endpoints, on each Regional entry. | Correct the reported dependency or Regional failure, then call UpdateWebFunctionEndpoint again to retry the update. | 
| does not have s3:GetObject on create-web-function-revision | The code is read from Amazon S3, and either the bucket policy or the caller's identity policy lacks read access. | Grant s3:GetObject and s3:GetObjectVersion in both the bucket policy (for the Lambda service) and the caller's identity policy. | 
| AccessDenied on get-web-function-endpoint | The IAM policy Resource does not include the endpoint. | Include web-function/{{name}}/\* in the policy Resource. | 

To avoid repeat deployment failures, validate configuration and startup in a test revision before you create a production revision.

## CLI and package errors
<a name="web-functions-troubleshooting-cli-package"></a>


| Error or symptom | Cause | Resolution | 
| --- | --- | --- | 
| invalid choice: lambda-web | The installed AWS CLI predates Web Function commands. | Update the AWS CLI and verify that aws lambda-web help lists the Web Function operations. | 
| Unknown parameter: BuildConfig | The request uses PascalCase member names. | Use the camelCase request members shown in this guide, such as buildConfig, codeConfig, and serviceConfig. | 
| Cannot find module '/var/task/index.js' | The required entry file is missing from the archive root. | Put index.js at the root of the deployment package. Include every file and production dependency that it imports. | 
| ERR\_MODULE\_NOT\_FOUND for an application file | The archive omits a source or built file imported by index.js. | Inspect the archive with unzip -l, add the missing file, and create a new revision. | 
| Application.TimeoutListenError, or HTTP 502 on the first request | The application listens on a loopback-only address, such as 127.0.0.1 or localhost, or on a port other than the one in AWS\_LAMBDA\_HTTP\_ENDPOINT. | Parse AWS\_LAMBDA\_HTTP\_ENDPOINT and listen on that exact host and port. | 
| EMFILE or too many open files | The application leaks sockets, files, or database connections across concurrent requests. | Close per-request handles, bound connection pools, and monitor open handles under sustained concurrency. | 
| JavaScript heap out of memory | The application reached the default V8 heap limit, which is lower than the execution environment's 2 GB memory limit, or concurrent requests exhausted the remaining environment memory. | Check for retained objects and unbounded caches, and reduce concurrency. If the application requires a larger heap, set a larger V8 heap limit with --max-old-space-size in NODE\_OPTIONS. Leave memory for buffers, native allocations, and the runtime. | 
| Dependency Cannot find module / ERR\_MODULE\_NOT\_FOUND at runtime | node\_modules was not included in the deployment package. | Install production dependencies and include them in the package: run npm ci --omit=dev, then confirm with unzip -l function.zip. | 
| Static files return HTTP 404 | The application resolves file paths relative to the working directory, or the files were not packaged. | Resolve paths from the module directory (\_\_dirname in CommonJS, or import.meta.dirname in ES modules), and confirm the files are in the package with unzip -l. | 
| ESM import errors, such as "Cannot use import statement outside a module" | package.json does not declare the module type. | Add "type": "module" to package.json, or use CommonJS consistently. | 

## HTTP request failures
<a name="web-functions-troubleshooting-http"></a>


| Response | Common cause | Resolution | 
| --- | --- | --- | 
| HTTP 400 | The client used an unsupported HTTP method or sent a request that the endpoint could not process. | Use a supported method and review the request headers and limits in [HTTP requests and responses](web-functions-http.md). | 
| HTTP 403 | An `IamAuth` request failed authorization for one of the following reasons:+ The request is unsigned.<br />+ The request omits the required content hash header.<br />+ The request has an invalid signature.<br />+ The caller doesn't have permission. For cross-account calls, either the identity policy or resource-based policy might be missing. | Confirm that the request includes the required X-Amz-Content-SHA256 header, review the signature, and verify lambda:InvokeWebFunctionEndpoint in the required identity and resource policies. For signing requirements, see [Signing requests](web-functions-endpoint-access-control.md#web-functions-endpoint-access-control-signing). For permission requirements, see [Granting invoke permission to a principal](web-functions-endpoint-access-control.md#web-functions-endpoint-access-control-iam-grant). | 
| HTTP 404 | The application does not define the requested route, or the client is using an obsolete endpoint domain. The Host header might also not match the endpoint domain. If you configure a front door such as Amazon CloudFront to forward the viewer's Host header to the origin, Lambda returns this error with lambda-web-error-type set to Platform.InvalidEndpoint. | Verify the current domainName, request path, and application routes. Use lambda-web-error-type and logs to distinguish a platform response from an application response. | 
| HTTP 409 | The endpoint is not Active, or the endpoint resolved to a revision that is not Active. | Inspect the revision and endpoint states. If the endpoint is Pending, wait and retry; if it is Failed, create a new endpoint. For revisions, remove failed or inactive revisions from the endpoint weights, and create a replacement revision when needed. | 
| HTTP 429 | One of the following occurred:+ The request exceeded an endpoint rate limit.<br />+ The endpoint ran out of environment capacity.<br />+ The account reached a Regional request or vCPU limit.<br />+ Too many execution environments were initializing at the same time for the endpoint. | Read the lambda-web-error-type header to identify which limit applied. See [Web Function error types](#web-functions-troubleshooting-error-types). Review the throttle metrics (EndpointRequestThrottles, AccountRequestThrottles, EndpointActiveEnvironmentThrottles, and AccountActiveVCPUArm64Throttles), active-capacity metrics, endpoint settings, and applied account limits. Concurrent initialization throttling (Platform.EndpointConcurrentInitThrottle) does not increment a throttle metric. Retry only idempotent requests, using backoff and jitter. | 
| HTTP 502 | Your application failed before it began serving requests, Lambda could not prepare the execution environment for your Web Function, or your application returned an invalid response. | Use lambda-web-error-type and system logs to identify the cause. See [Web Function error types](#web-functions-troubleshooting-error-types). | 
| HTTP 503 | The application crashed while handling a request, the endpoint is disabled, or Lambda could not obtain capacity or reach the application. | Use lambda-web-error-type, when present, and application and system logs to identify the cause. See [Web Function error types](#web-functions-troubleshooting-error-types). A 503 without lambda-web-error-type can indicate temporary load shedding or an internal error. In either case, retry idempotent requests with backoff and jitter. | 
| HTTP 504 | The application did not respond within the revision timeout (Runtime.RequestTimeout). | Check the revision's timeoutSeconds and downstream latency. | 
| Other HTTP 5xx | The application returned a 5xx status, or Lambda encountered an internal error (no lambda-web-error-type header). | Use the request ID, the log-stream header, application logs, and system logs to identify the source, and check process health. | 
| Request hangs or times out on a large upload; logs show 0 bytes received | The handler began writing the response while the request body was still arriving. The Web Function request path is half-duplex: Lambda forwards the full request body before it delivers your application's response. | Read the request body fully before you write the response. Bodies under about 1 MB fit socket buffers and can mask this. | 

## Request header limits
<a name="web-functions-troubleshooting-header-limits"></a>

Two limits apply to request headers. Lambda limits the header block to 128 KiB and rejects larger requests before they reach your function. The Node.js HTTP server in your function also limits the number of header lines it accepts. Both return HTTP 431 Request Header Fields Too Large, as shown in the following table. For the platform limits, see [Header limits](web-functions-http.md#web-functions-http-header-limits).


| Symptom | Cause | Resolution | 
| --- | --- | --- | 
| HTTP 431 with lambda-web-error-type: Platform.HeaderTooLarge. No invocation and no application log entry. | The request head exceeds 131,072 bytes (128 KiB), measured on the full request head as the client sends it. | Reduce the size of the request headers. This limit cannot be raised. | 
| HTTP 431 with lambda-web-request-id and lambda-web-logstream but no lambda-web-error-type. The handler does not run. | The request has more than 1,000 header lines as received by the Node.js server, including the headers that Lambda adds. | Raise server.maxHeadersCount in your server code, or reduce the number of header lines the client sends. | 

The size limit counts every byte of the request head as the client sends it. This includes the request line, every header line (including `Host` and any headers the client library adds), and the line terminators. Headers that Lambda adds do not count toward the size limit.

When a request exceeds the size limit, Lambda rejects it before it reaches your function, so the request produces no invocation and no application log entry. The `lambda-web-error-type` response header identifies the cause.

The Node.js count limit counts header lines, not distinct header names. A header that is repeated three times counts three times. As a result, a request that accumulates `x-forwarded-for` or tracing headers through a chain of proxies can reach the limit. No single header needs to look unusual for this to happen. The limit is measured on the request your function receives, which includes the headers Lambda adds. As a result, a client sending slightly fewer than 1,000 header lines can reach it. When that happens, the request reaches your execution environment, and the Node.js server rejects it during parsing. Your handler does not run. The response carries the `lambda-web-request-id` and `lambda-web-logstream` headers, but it does not carry the `lambda-web-error-type` header.

If your application must accept more header lines than the Node.js default allows, raise the Node.js limit in your server code. Set `server.maxHeadersCount` to the number of header lines to accept, or set it to `0` to disable the Node.js count check. The 128 KiB size limit still applies.

```
const server = http.createServer(handler);
server.maxHeadersCount = 2000;
server.listen(port, host);
```

You do not need to change the Node.js header size limit. The managed Node.js runtimes set it to match the platform limit, so the platform limit applies to header size. You cannot raise the platform limit from application code.

To stay within the limits, move bulk state out of headers and into the request body, trim cookies, and collapse redundant proxy and tracing headers before the request reaches the endpoint. If a CloudFront distribution sits in front of the endpoint, forward only the headers your application needs in the origin request policy.

## Web Function error types
<a name="web-functions-troubleshooting-error-types"></a>

When a request to a Web Function endpoint fails, Lambda returns a `lambda-web-error-type` response header that identifies what went wrong. The value uses the format `<Prefix>.<ErrorReason>`: the prefix tells you where the error occurred, and the reason specifies the cause.


| Prefix | Where the error occurred | 
| --- | --- | 
| Platform. | Lambda's platform layer, which routes and validates requests, checks permissions, and enforces limits. | 
| Runtime. | The managed runtime that loads and runs your function. | 
| Application. | Your function code. | 

For example, `Runtime.RequestTimeout` means the managed runtime reported that your function did not respond within its configured timeout, and `Application.InitCodeError` means your own initialization code threw an error.

Lambda includes the `lambda-web-error-type` header when the error was caused by the request itself or by your function, its configuration, or its code. Lambda omits the header for internal service errors and for authorization failures, so that no detail is revealed to an unauthorized caller. A value indicates a problem on the path between the Lambda platform and your function. On the request path, the error identifies where the request failed. On the response path, use the value together with your application telemetry to understand what happened.


| Error type | Description | 
| --- | --- | 
| Platform.MalformedRequest | Lambda could not parse the request, or the request line or method was not accepted. | 
| Platform.MissingHostHeader | The request did not include a Host header, so Lambda could not resolve the target endpoint. | 
| Platform.InvalidEndpoint | The Host header did not resolve to a valid, existing endpoint. | 
| Platform.HeaderTooLarge | The request's header section exceeded the Lambda header size limit. | 
| Platform.DisallowedHeader | The request contained a header that Lambda does not accept. Lambda returns HTTP 400. | 
| Platform.UnsupportedHttpVersion | The request used an HTTP version other than HTTP/1.1, which Web Functions require. | 
| Platform.CannotAssumeRole | Lambda could not assume your function's execution role. | 
| Platform.KMSDecryptionError | Lambda could not use the configured AWS KMS key to decrypt your environment variables or other data required to initialize your function. | 
| Platform.InvalidNetworkConfiguration | A VPC networking resource that your function depends on is invalid. To find the cause, see [Networking and connectivity issues](#web-functions-troubleshooting-networking). | 
| Platform.RevisionNotActive | The function revision targeted by the request is not in the Active state. The revision may still be activating or may have failed to activate. Check the revision's state; if activation is still in progress, retry after a short delay. | 
| Platform.EndpointNotActive | The endpoint is not in the Active state. The endpoint may still be provisioning or may be otherwise unavailable. Check the endpoint's state; if it is still being created, retry after a short delay. | 
| Platform.EndpointDisabled | The endpoint's rateLimit is 0, so Lambda rejects all requests with HTTP 503. Set rateLimit to a nonzero value to resume traffic. | 
| Platform.AccountDisabled | Web Function invocations are disabled for the account. Lambda returns HTTP 403. Contact AWS Support. | 
| Platform.AccountRequestThrottle | The account-level request rate quota was exceeded. | 
| Platform.EndpointRequestThrottle | The endpoint's request rate quota was exceeded. | 
| Platform.AccountActiveVCPUArm64Throttle | The account's active vCPU quota was reached. | 
| Platform.EndpointMaxEnvThrottle | The endpoint's maximum environments limit was reached. | 
| Platform.EndpointConcurrentInitThrottle | Too many execution environments were initializing at the same time for the endpoint. Retry with exponential backoff. | 
| Runtime.RequestTimeout | Your function did not return a response within its configured timeout. | 
| Runtime.OutOfMemory | Your function exceeded its memory limit and the process was stopped. | 
| Runtime.Unreachable | The runtime process crashed, exited, or refused the connection. | 
| Runtime.Exit | The runtime process exited between requests. | 
| Runtime.ExitError | The runtime process exited with an error. | 
| Runtime.InvalidResponse | The runtime's response headers exceeded the read buffer. | 
| Runtime.OriginRequestError | The application process failed while handling a request. Check the application logs for details. | 
| Runtime.ImportCodeError | The runtime could not import or resolve your entry point, for example a missing module or a bad path. | 
| Runtime.InitTimeout | Your function exceeded the init timeout while provisioning sandbox. | 
| Application.InitCodeError | Your initialization code threw an error before the function began serving requests. | 
| Application.TimeoutListenError | Your initialization code did not start listening on the port before the initialization deadline. | 

For the throttling metrics that identify which limit applied (for the `Platform.AccountRequestThrottle`, `Platform.EndpointRequestThrottle`, `Platform.AccountActiveVCPUArm64Throttle`, and `Platform.EndpointMaxEnvThrottle` error types), see [Regional usage and throttling metrics](web-functions-monitoring-metrics.md#web-functions-monitoring-metrics-usage).

## Logs or metrics are missing
<a name="web-functions-troubleshooting-logs"></a>
+ Verify that the execution role can create log groups and streams and put log events for both the destination log group and its `.local` companion.
+ Look in the centralized log group in the home Region. Do not build diagnostics that depend on temporary replica-Region or `.local` log groups.
+ Set `systemLogLevel` to `DEBUG` when you need `platform.requestComplete`.
+ Allow for telemetry delivery delay after creating or updating resources. Do not treat the temporary absence of a metric or log event as proof that a request did not run.
+ Remember that metrics are sparse. Configure alarms to treat missing error metrics as not breaching where appropriate.

If no application logs appear at all, the execution role might lack Amazon CloudWatch Logs permissions. Attach the `AWSLambdaBasicExecutionRole` managed policy to the execution role, or grant `logs:CreateLogGroup`, `logs:CreateLogStream`, and `logs:PutLogEvents`. For the required permissions, see [Execution role](web-functions-permissions.md#web-functions-permissions-execution-role).

## Code storage and encryption issues
<a name="web-functions-troubleshooting-storage-encryption"></a>

Missing or inaccessible Amazon S3 object version  
Confirm that the bucket still has versioning enabled, the exact object version exists, and both the caller and Lambda service principal have the required read permissions. If an active revision loses access to its pinned object version, create a new revision that references an available version. For details, see [Deploying Web Function code from Amazon S3](web-functions-code-s3.md).

AWS KMS access failure  
Check the caller permissions, key policy, encryption context, key state, and the Lambda service principal's `kms:Decrypt` permission. For `MultiRegion` and `PerRegion` endpoints, verify that a replica of the multi-Region AWS KMS key exists and is usable in every target Region. For details, see [Encryption at rest for Web Functions](web-functions-encryption.md).

## Issues with `MultiRegion` and `PerRegion` endpoints
<a name="web-functions-troubleshooting-multi-region"></a>

Use the `regionalEndpoints` field to identify the affected Region. Compare its `stateReason` and `updateStatusReason` with the healthy Regions. Check Regional quotas, AWS KMS key replicas, runtime availability, and the revision's replication state. After correcting the cause, repeat the endpoint update. For the replication model, see [Multi-Region deployment](web-functions-endpoint-replication.md).

For a `MultiRegion` endpoint, latency-based routing (which directs requests to the Region with the lowest measured latency) doesn't guarantee that every request goes to the lowest-latency Region. Test from the affected client location and inspect the application logs to determine which Region handled the request. For a `PerRegion` endpoint, also verify your external DNS or front-door routing configuration.

## Networking and connectivity issues
<a name="web-functions-troubleshooting-networking"></a>

Most connectivity problems come from a serving revision that has no connector reference or references an older connector version, or from connector subnets, security groups, or routes that block the traffic.

Use the following sequence to isolate a connectivity problem:

1. Run `get-web-function-endpoint`. Check the automatic deployment mode and confirm which revision or revisions receive traffic.

1. Run `get-web-function-revision` for each serving revision. Confirm that its state is `Active` and that it references the expected connector version.

1. Run `aws lambda-core get-network-connector --identifier` with the connector ARN from the revision's `egressNetworkConnectorArn`. Confirm that `State` is `ACTIVE` and, if the connector has been updated, that `LastUpdateStatus` is `Successful`. Otherwise, use `StateReasonCode` or `LastUpdateStatusReasonCode` to identify the cause, such as `InsufficientRolePermissions`, `InvalidSubnet`, or `SubnetOutOfIPAddresses`.

1. Test the destination by IP address to separate network reachability from DNS resolution.

1. Check the connector subnet routes, destination security groups, and network ACLs.

1. Review VPC Flow Logs on the connector subnets.

Common symptoms include the following.


| Symptom | Check | 
| --- | --- | 
| Public internet works, but VPC resources don't | The serving revision has no connector reference. | 
| VPC access works for some requests | The endpoint is routing to two revisions with different connector configurations. | 
| A connector update has no effect | The serving revision references an older connector version. | 
| Public access stops after adding a connector | The connector subnets don't have the required NAT or IPv6 route. | 
| One VPC destination times out | The destination security group, route table, or network ACL blocks the connection. | 
| Flow Logs contain no matching records | Traffic didn't enter the VPC. Recheck the serving revision and connector reference. | 
| Private names fail but direct IP connections work | Check VPC DNS attributes and private hosted zone associations. | 
| IPv4 works but IPv6 fails | Check for a DualStack connector version, IPv6 routes, and IPv6 security rules. | 
| The serving revision is Active but the function cannot reach private VPC resources | The serving revision does not set an egress network connector (egressNetworkConnectorArn). Read the field with get-web-function-revision; if it is empty, create a revision that sets egressNetworkConnectorArn. For details, see [Configuring networking for AWS Lambda Web Functions](web-functions-networking.md). | 

There is no interactive access to a Web Function execution environment. Use application logs, endpoint response headers, resource state fields, CloudWatch metrics, and VPC Flow Logs to diagnose failures.

## Prepare an escalation bundle
<a name="web-functions-troubleshooting-support"></a>

If the preceding checks do not identify the cause, collect the following information before opening an AWS Support case. This lets the support engineer correlate the control-plane operation, Regional deployment, request, and telemetry:
+ The AWS account ID, home Region, function name, revision ID, endpoint name, endpoint type, and target Regions.
+ The UTC timestamp and request path for representative failures, together with the HTTP status, `lambda-web-request-id`, `lambda-web-logstream`, and `lambda-web-error-type` response headers.
+ The function, revision, endpoint, and Regional `state`, `stateReason`, `updateStatus`, and `updateStatusReason` values.
+ Relevant centralized application and system log events, throttle and capacity metrics, and the approximate traffic rate when the issue occurred.
+ The AWS CLI version and a redacted copy of the management request. Remove credentials, application secrets, tokens, and sensitive request data.

## Related information
<a name="web-functions-troubleshooting-related"></a>
+ [Configuring networking for AWS Lambda Web Functions](web-functions-networking.md)
+ [Monitoring Lambda Web Functions](web-functions-monitoring.md)