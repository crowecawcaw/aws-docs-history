

# Lambda Web Function runtimes
<a name="web-functions-runtimes"></a>

Lambda Web Functions run your HTTP server code using managed runtimes. Your application must start an HTTP server that listens on the host and port specified by the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable. Lambda Web Functions currently support Node.js. By default, the runtime loads `index.js` at the root of the deployment package. To use a different entry file, set the `AWS_LAMBDA_NODEJS_ENTRYPOINT` environment variable. For details, see [Environment variables](web-functions-revisions-env-vars.md).

## Supported Node.js versions
<a name="web-functions-runtimes-versions"></a>


| Runtime identifier | Node.js version | Status | 
| --- | --- | --- | 
| nodejs24.x | Node.js 24 | Supported | 

Specify the runtime identifier in the `runtimeConfig` section when you create a revision. For example:

```
"runtimeConfig": { "runtime": "nodejs24.x" }
```

The `nodejs24.x` Web Function runtime follows the same deprecation cycle as the corresponding Lambda Event Functions runtime. For deprecation dates and the deprecation process, see [Runtime deprecation policy](lambda-runtimes.md#runtime-support-policy).

## Automatic runtime patching
<a name="web-functions-runtimes-patching"></a>

Lambda automatically patches the Node.js runtime with security updates and bug fixes. Patching applies to the underlying runtime layer and does not change your application code. Your revision's `runtime` identifier (for example, `nodejs24.x`) always resolves to the latest patched version of that major runtime.

**Note**  
Runtime management controls are not supported for Web Functions. You cannot pin to a specific patch version or disable automatic patching. Lambda always uses the latest patched version of the runtime you specified.

For more information about how Lambda manages runtime updates, see [Understanding how Lambda manages runtime version updates](runtimes-update.md).

## Supported web frameworks
<a name="web-functions-runtimes-frameworks"></a>

You can use any Node.js web framework that starts an HTTP server. Popular frameworks include:
+ Express
+ Next.js
+ Fastify
+ Koa

You don't need the AWS Lambda Web Adapter or another event-to-HTTP adapter. Your application handles HTTP requests directly using the framework's standard routing and middleware. Some frameworks, such as Next.js in standalone mode, read their own environment variables for the listen address. For these frameworks, use an `index.js` entry file that sets those variables from `AWS_LAMBDA_HTTP_ENDPOINT` before it starts the server. For details, see [Environment variables](web-functions-revisions-env-vars.md). For a complete application, see [Minimal Express application](web-functions-samples.md#web-functions-samples-express).

## Node.js execution model
<a name="web-functions-runtimes-execution-model"></a>

Node.js uses an event-driven execution model. By default, Node.js runs your JavaScript code on a single main thread, and I/O operations (network calls, file system access) are non-blocking and event-driven. Your application can create additional threads with the `worker_threads` module if it needs them. This model has important implications for Web Functions:

**Concurrency through async I/O**  
Your server handles multiple concurrent requests by using asynchronous operations (`async`/`await`, Promises, callbacks). While one request waits for a database response, the event loop serves other requests. This is why Web Functions can handle many concurrent requests in a single environment without multiple threads.

**Avoid blocking the event loop**  
CPU-intensive synchronous operations (large JSON parsing, complex computations, synchronous file reads) block the event loop and prevent all other requests from being processed. If your application performs CPU-heavy work, offload it to worker threads or reduce `maxConcurrencyPerEnvironment` to limit the impact.

**Request isolation**  
Because all requests share the same process and event loop, avoid storing per-request state in global variables. Use request-scoped middleware context (such as Express `req`/`res` objects) to isolate request data.

For guidance on configuring `maxConcurrencyPerEnvironment` based on your application's I/O and CPU characteristics, see [Scaling behavior for Lambda Web Functions](web-functions-scaling.md).

## Memory and the Node.js heap
<a name="web-functions-runtimes-memory"></a>

Each execution environment has 2 GB of memory. The following applies to the Node.js V8 heap:
+ The default heap is 1,024 MB.
+ To use a larger heap, set `NODE_OPTIONS` in the revision's environment variables, for example `NODE_OPTIONS=--max-old-space-size=1536` (the value is in MB).
+ A value that you set in `NODE_OPTIONS` replaces the default. If you set only `--max-old-space-size`, Lambda doesn't set `--max-semi-space-size`, and Node.js uses its own default for it.
+ The heap, buffers, native allocations, the runtime, and concurrent requests must all fit within the 2 GB of environment memory.

## How Lambda routes requests to your application
<a name="web-functions-runtimes-port"></a>

Web Function endpoints accept HTTPS traffic only, on port 443. Plain HTTP is not served, so you don't need to redirect HTTP to HTTPS or configure TLS in your application.

Lambda terminates TLS at the endpoint and forwards each request to your application's HTTP server inside the execution environment. Your application serves plain HTTP on the address that Lambda provides; you never handle certificates or TLS configuration in your code.

Lambda chooses the host and port that your server must listen on. Lambda communicates the address to your application through the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable, in `host:port` format. Use this variable, which Lambda sets, to determine where your server listens. Your application must read the variable at startup:

```
const [host, port] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || 'localhost:3000').split(':');
app.listen(port, host);
```

Lambda does not set the variable on your local computer. The fallback address applies only when the variable is unset, so it is used only in local runs. To use a different local address, set `AWS_LAMBDA_HTTP_ENDPOINT` yourself. For an example, see [Run the HTTP server locally](web-functions-testing.md#web-functions-testing-local).

Lambda adds a `lambda-web-request-id` header to every request that it forwards to your application, and returns the same value as a response header, so you can correlate a client request with your application logs.

Lambda routes web requests to the address specified by `AWS_LAMBDA_HTTP_ENDPOINT`. If your server listens on a different host or port, requests do not reach your application.

Your server must begin listening within 10 seconds of startup, and each request it serves is bound by the revision's `timeoutSeconds` setting. For the startup and shutdown sequence, see [Execution environment lifecycle](web-functions-env-lifecycle.md). For how to configure `timeoutSeconds`, see [Managing Web Function revisions](web-functions-revisions.md).