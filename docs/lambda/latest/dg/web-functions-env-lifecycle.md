

# Execution environment lifecycle
<a name="web-functions-env-lifecycle"></a>

An execution environment is an isolated compute instance that runs your HTTP server. AWS Lambda creates execution environments for your Lambda Web Function when traffic arrives. It routes requests to active environments and removes environments that are no longer needed. Understanding this lifecycle helps you optimize startup performance and write code that handles initialization and shutdown correctly.

## Lifecycle phases
<a name="web-functions-env-lifecycle-phases"></a>

Each execution environment moves through the following phases:

![The three execution environment phases: Initialize, Ready, and Shut down.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-environment-lifecycle.png)



| Phase | What happens | Request handling | 
| --- | --- | --- | 
| Initialization | Lambda loads your code, prepares the runtime, and starts your HTTP server process. Your server must begin listening on the address in AWS\_LAMBDA\_HTTP\_ENDPOINT within 10 seconds. | The environment cannot serve requests during initialization. | 
| Ready | Your HTTP server is listening and the environment is available to receive requests. Lambda routes incoming requests to this environment. | The environment accepts requests up to the maxConcurrencyPerEnvironment limit. | 
| Shutdown | Lambda stops routing new requests to the environment, lets in-flight requests finish on a best-effort basis, sends SIGTERM, and then terminates the environment. | No new requests are routed to the environment. In-flight requests can continue, but completion is not guaranteed. After SIGTERM, the process has up to 1 second to finish cleanup. Process state is lost. | 

## Initialization (cold start)
<a name="web-functions-env-lifecycle-init"></a>

When Lambda creates a new execution environment, the initialization phase includes these steps:

1. Lambda loads the code from your .zip deployment package.

1. Lambda sets up the runtime environment (including Node.js and your environment variables).

1. Lambda starts your application process.

1. Your HTTP server begins listening at the host and port specified by the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable. It must begin listening within 10 seconds.

1. Lambda detects that your server is listening and marks the environment as ready.

A cold start occurs when Lambda must create a new environment to handle a request because there are no available environments. The first request after a cold start experiences additional latency from the initialization phase. Subsequent requests to the same environment do not incur this cost.

To reduce cold start impact:
+ Minimize your deployment package size. Smaller packages load faster.
+ Reduce server startup time. Defer heavy initialization (such as loading large data files) to after the server begins listening. Lambda routes requests to the environment as soon as the server listens, so make request handlers that depend on the deferred work wait for it to finish, for example by awaiting a shared promise.
+ Use lazy initialization for database connections and external service clients. Establish connections on first request rather than at startup.

## Scale-down and shutdown
<a name="web-functions-env-lifecycle-shutdown"></a>

Lambda monitors your endpoint's environment utilization and removes unneeded environments, for example when traffic decreases. Before removing an environment, Lambda uses the following shutdown sequence:

1. Lambda stops routing new requests to the environment.

1. Lambda allows in-flight requests to finish on a best-effort basis.

1. Lambda sends `SIGTERM`. The process has up to 1 second to finish cleanup before Lambda terminates it and removes the environment.

When there is no traffic, Lambda scales your Web Function to zero environments. The next request after a scale-to-zero period triggers a new cold start.

If your application needs to perform cleanup during shutdown, handle `SIGTERM`. Cleanup must finish within 1 second. Do not rely on shutdown callbacks being executed, because Lambda can't guarantee a graceful shutdown in all failure modes, for example an underlying hardware failure.

The following example handles `SIGTERM`:

```
process.on('SIGTERM', () => {
  // Finish short cleanup, such as flushing buffered logs, within 1 second.
  process.exit(0);
});
```

## Environment reuse
<a name="web-functions-env-lifecycle-reuse"></a>

Lambda reuses execution environments across multiple requests to avoid repeated cold starts. A single environment can serve thousands of requests during its lifetime. This means:
+ **Global state persists** – Variables, caches, and connections that your server initializes at startup persist across requests. You can use this for in-memory caching or connection pooling.
+ **File system state persists** – Files that your code writes to the local file system (such as `/tmp`) persist until Lambda removes the environment.
+ **No guaranteed lifetime** – Lambda can remove an environment at any time. Do not rely on an environment lasting for a specific duration. Persist important data to an external store such as DynamoDB or Amazon S3.

## Concurrent request handling
<a name="web-functions-env-lifecycle-concurrency"></a>

Each Web Function execution environment handles multiple concurrent HTTP requests. The `maxConcurrencyPerEnvironment` setting on the revision controls the maximum number of simultaneous requests per environment.

Because your server handles multiple requests concurrently, your code must be safe for concurrent use:
+ Do not store per-request state in global variables. Use request-scoped variables or middleware context instead.
+ Guard shared mutable state, such as caches or counters, that you modify across `await` boundaries. Requests interleave on the event loop. If a read-modify-write sequence spans an asynchronous operation, another in-flight request can read or change the state before the sequence finishes.
+ Be aware that Node.js uses a single-threaded event loop. CPU-intensive synchronous operations block all concurrent requests in that environment. Use asynchronous I/O and avoid blocking the event loop.

For more information about concurrency settings and optimization, see [Scaling behavior for Lambda Web Functions](web-functions-scaling.md).