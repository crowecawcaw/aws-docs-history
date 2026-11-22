

# Supporting a new programming language for AWS Lambda Event Functions

You can support any programming language in Lambda by implementing a runtime interface client (RIC) and an associated bootstrap script for that language. You then include them, together with the language runtime, in a [customer-managed runtime](runtimes-customer-managed.md).

The runtime image has the structure that [Building runtime images](cmr-building-images.md) describes. The runtime must include the OS libraries, the language runtime, and the RIC. It can also include other components, such as SDKs and certificates.

You write the RIC in your chosen programming language. The RIC is the entry point for that language, and the bootstrap script starts it during a cold start. The RIC loads your function code and acts as the bridge between the Lambda service and your function handler. Some Lambda features require specific implementation in the RIC. For more information, see [Implementing response streaming in your runtime](#runtimes-custom-response-streaming) and [Supporting Lambda Managed Instances in your runtime](#runtimes-custom-managed-instances).

For languages that have a separate language runtime executable, the RIC is separate from your function code. Languages such as Go, Rust, C\+\+, and Swift compile to an executable binary. These languages still need a RIC, but you build it into the executable as a library, together with the function handler. This also applies to Java GraalVM Native Image and .NET NativeAOT, which also compile to an executable binary. Running the executable only requires an operating system environment. These functions typically use an OS-only runtime (the `provided` runtime family), although you can also use a customer-managed runtime to modify the OS or include additional components. For more information, see [OS-only runtimes](lambda-runtimes.md#runtimes-provided).

We recommend that you implement a new programming language as a customer-managed runtime. You can also include the language runtime, bootstrap script, and RIC in your function's deployment package (.zip file) or in a [Lambda layer](chapter-layers.md). This approach is called bring your own language (BYOL). With BYOL, you choose an OS-only runtime when you create the function. The RIC implementation is the same for both approaches.

**Note**  
Building a RIC is an advanced use case. To build a customer-managed runtime for a language that Lambda already supports, see [Building a runtime image from a Lambda base image](cmr-base-images.md). To use one of the open-source RICs that Lambda provides, see [Open-source repositories](runtimes-open-source.md).

The rest of this page describes how to build a RIC. For a tutorial that builds a runtime in Bash, see [Tutorial: Creating a Bash runtime](runtimes-walkthrough.md).

**Topics**
+ [Requirements](#runtimes-custom-build)
+ [Implementing response streaming in your runtime](#runtimes-custom-response-streaming)
+ [Supporting Lambda Managed Instances in your runtime](#runtimes-custom-managed-instances)
+ [Using the Lambda runtime API](runtimes-api.md)
+ [Tutorial: Creating a Bash runtime](runtimes-walkthrough.md)

## Requirements
<a name="runtimes-custom-build"></a>

Your RIC and bootstrap script must complete certain initialization and processing tasks. The RIC runs the function's setup code, reads the handler name from an environment variable, and reads invocation events from the Lambda runtime API. The RIC passes the event data to the function handler, and posts the response from the handler back to Lambda.

### Initialization tasks
<a name="runtimes-custom-initialization"></a>

The initialization tasks run once [per instance of the function](lambda-runtime-environment.md) to prepare the environment to handle invocations.
+ **Retrieve settings** – Read environment variables to get details about the function and environment.
  + `_HANDLER` – The location to the handler, from the function's configuration. The standard format is `{{file}}.{{method}}`, where `file` is the name of the file without an extension, and `method` is the name of a method or function that's defined in the file. For functions that use an OS-only runtime (BYOL), Lambda sets this variable. For customer-managed runtimes, Lambda doesn't set this variable. Instead, your bootstrap script sets it from the handler argument that Lambda passes to the image's `ENTRYPOINT`. For more information, see [How Lambda starts your runtime](cmr-building-images.md#cmr-building-images-startup).
  + `LAMBDA_TASK_ROOT` – The directory that contains the function code.
  + `AWS_LAMBDA_RUNTIME_API` – The host and port of the runtime API.

  For a full list of available variables, see [Defined runtime environment variables](configuration-envvars.md#configuration-envvars-runtime).
+ **Initialize the function** – Load the handler file and run any global or static code that it contains. Functions should create static resources like SDK clients and database connections once, and reuse them for multiple invocations.
+ **Handle errors** – If an error occurs, call the [initialization error](runtimes-api.md#runtimes-api-initerror) API and exit immediately.

Initialization counts towards billed execution time and timeout. When an execution triggers the initialization of a new instance of your function, you can see the initialization time in the logs and [AWS X-Ray trace](services-xray.md).

**Example log**  

```
REPORT RequestId: f8ac1208... Init Duration: 48.26 ms   Duration: 237.17 ms   Billed Duration: 300 ms   Memory Size: 128 MB   Max Memory Used: 26 MB
```

### Processing tasks
<a name="runtimes-custom-processing"></a>

While it runs, the RIC uses the [Lambda runtime API](runtimes-api.md) to manage incoming events and report errors. After completing initialization tasks, the RIC processes incoming events in a loop. In your RIC code, perform the following steps in order.
+ **Get an event** – Call the [next invocation](runtimes-api.md#runtimes-api-next) API to get the next event. The response body contains the event data. Response headers contain the request ID and other information.
+ **Propagate the tracing header** – Get the X-Ray tracing header from the `Lambda-Runtime-Trace-Id` header in the API response. Set the `_X_AMZN_TRACE_ID` environment variable locally with the same value. The X-Ray SDK uses this value to connect trace data between services.
+ **Create a context object** – Create an object with context information from environment variables and headers in the API response.
+ **Invoke the function handler** – Pass the event and context object to the handler.
+ **Handle the response** – Call the [invocation response](runtimes-api.md#runtimes-api-response) API to post the response from the handler.
+ **Handle errors** – If an error occurs, call the [invocation error](runtimes-api.md#runtimes-api-invokeerror) API.
+ **Cleanup** – Release unused resources, send data to other services, or perform additional tasks before getting the next event.

### Entrypoint
<a name="runtimes-custom-bootstrap"></a>

Your runtime's entry point is an executable file named `bootstrap`. The bootstrap file can be the RIC itself, for example a compiled binary. Or it can be a script that starts the language runtime and runs the RIC. For a customer-managed runtime, Lambda runs the executable that the image's `ENTRYPOINT` specifies, or `/var/runtime/bootstrap` if the image doesn't set one. For more information, see [How Lambda starts your runtime](cmr-building-images.md#cmr-building-images-startup).

For BYOL, the `ENTRYPOINT` of the OS-only runtime starts an initial bootstrap script that's included in the runtime. This script looks for your `bootstrap` file, first at the root of your function's deployment package, and then in the function's layers. If your `bootstrap` file doesn't exist or isn't executable, your function returns a `Runtime.InvalidEntrypoint` error when you invoke it.

Here's an example `bootstrap` file that uses a bundled version of Node.js to run a RIC written in JavaScript in a separate file named `runtime.js`.

**Example bootstrap**  

```
#!/bin/sh
    cd $LAMBDA_TASK_ROOT
    ./node-v11.1.0-linux-x64/bin/node runtime.js
```

## Implementing response streaming in your runtime
<a name="runtimes-custom-response-streaming"></a>

For [response streaming functions](configuration-response-streaming.md), the `response` and `error` endpoints have slightly modified behavior that lets the runtime stream partial responses to the client and return payloads in chunks. For more information about the specific behavior, see the following:
+ `/runtime/invocation/AwsRequestId/response` – Propagates the `Content-Type` header from the runtime to send to the client. Lambda returns the response payload in chunks by using HTTP/1.1 chunked transfer encoding. To stream the response to Lambda, the runtime must:
  + Set the `Lambda-Runtime-Function-Response-Mode` HTTP header to `streaming`.
  + Set the `Transfer-Encoding` header to `chunked`.
  + Write the response conforming to the HTTP/1.1 chunked transfer encoding specification.
  + Close the underlying connection after it has successfully written the response.
+ `/runtime/invocation/AwsRequestId/error` – The runtime can use this endpoint to report function or runtime errors to Lambda, which also accepts the `Transfer-Encoding` header. This endpoint can only be called before the runtime begins sending an invocation response.
+ Report midstream errors using error trailers in `/runtime/invocation/AwsRequestId/response` – To report errors that occur after the runtime starts writing the invocation response, the runtime can optionally attach HTTP trailing headers named `Lambda-Runtime-Function-Error-Type` and `Lambda-Runtime-Function-Error-Body`. Lambda treats this as a successful response and forwards the error metadata that the runtime provides to the client. 
**Note**  
To attach trailing headers, the runtime must set the `Trailer` header value at the beginning of the HTTP request. This is a requirement of the HTTP/1.1 chunked transfer encoding specification.
  + `Lambda-Runtime-Function-Error-Type` – The error type that the runtime encountered. This header consists of a string value. Lambda accepts any string, but we recommend a format of {{<category.reason>}}. For example, `Runtime.APIKeyNotFound`.
  + `Lambda-Runtime-Function-Error-Body` – Base64-encoded information about the error.

## Supporting Lambda Managed Instances in your runtime
<a name="runtimes-custom-managed-instances"></a>

These requirements apply to runtimes that you include with your function (BYOL) and to [customer-managed runtimes](runtimes-customer-managed.md).

Lambda Managed Instances use the same runtime API as functions that use the Lambda default capacity provider. However, there are key differences in how runtimes must be implemented to support the concurrent execution model of Managed Instances.

### Concurrent request handling
<a name="runtimes-custom-managed-instances-concurrency"></a>

The primary difference when building runtimes for Managed Instances is support for concurrent invocations. Unlike functions that use the Lambda default capacity provider, where the runtime processes one invocation at a time, Managed Instances can process multiple invocations simultaneously within a single execution environment.

Your runtime must:
+ **Support concurrent `/next` requests** – The runtime can make multiple simultaneous calls to the [next invocation](runtimes-api.md#runtimes-api-next) API, up to the limit specified by the `AWS_LAMBDA_MAX_CONCURRENCY` environment variable.
+ **Handle concurrent `/response` requests** – Multiple invocations can call the [invocation response](runtimes-api.md#runtimes-api-response) API simultaneously.
+ **Implement thread-safe request handling** – Ensure that concurrent invocations don't interfere with each other by properly managing shared resources and state.
+ **Use request IDs and invocation IDs correctly** – A request ID identifies the event; use it in the URL path. An invocation ID represents a single invocation attempt—a single request ID might result in multiple attempts, each with a unique invocation ID. Echo the invocation ID back on `/response` and `/error` calls. The header is optional—omitting it is accepted for backward compatibility. Lambda only rejects with `400 InvalidInvocationId` when the header is present but its value does not match.

### Implementation pattern
<a name="runtimes-custom-managed-instances-implementation"></a>

A typical implementation pattern for Managed Instances runtimes involves creating worker threads or processes to handle concurrent invocations:

1. **Read the concurrency limit** – At initialization, read the `AWS_LAMBDA_MAX_CONCURRENCY` environment variable to determine how many concurrent invocations to support.

1. **Create worker pool** – Initialize a pool of workers (threads, processes, or async tasks) equal to the concurrency limit.

1. **Worker processing loop** – Each worker independently:
   + Calls `/runtime/invocation/next` to get an invocation event
   + Invokes the function handler with the event data
   + Posts the response to `/runtime/invocation/AwsRequestId/response`
   + Repeats the loop

### Additional considerations
<a name="runtimes-custom-managed-instances-considerations"></a>
+ **Logging format** – Managed Instances only support JSON log format. Ensure your runtime respects the `AWS_LAMBDA_LOG_FORMAT` environment variable and only uses JSON format. For more information, see [Configuring JSON and plain text log formats](monitoring-cloudwatchlogs-logformat.md).
+ **Shared resources** – Be cautious when using shared resources like the `/tmp` directory with concurrent invocations. Implement proper locking mechanisms to prevent race conditions.

For more information about Lambda Managed Instances execution environments, see [Understanding the Lambda Managed Instances execution environment](lambda-managed-instances-execution-environment.md).