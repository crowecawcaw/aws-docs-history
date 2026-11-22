

# Lambda Managed Instances runtimes

Lambda Event Functions on Lambda Managed Instances support both `.zip` file archive and container image deployment packages, which use the Open Container Initiative (OCI) format. To reduce startup time for large container images, see [Lazy-load container images with Seekable OCI (SOCI)](lambda-managed-instances-seekable-oci.md).

Lambda processes requests differently when using Lambda Managed Instances. Instead of handling requests sequentially in each execution environment, Lambda Managed Instances process multiple requests concurrently within each execution environment. This change in execution model means that Lambda Event Functions using Lambda Managed Instances need to consider thread safety, state management, and context isolation. These concerns don't arise in the Lambda (default) single-concurrency model. In addition, the multi-concurrency implementation varies between runtimes.

## Supported languages
<a name="lambda-managed-instances-supported-runtimes"></a>

Lambda Managed Instances can be used with the following programming languages and runtimes:
+ **Java:** Java 21 and later.
+ **Python:** Python 3.13 and later.
+ **Node.js:** Node.js 22 and later.
+ **.NET:** .NET 8 and later.
+ **Rust:** Supported using the OS-only runtime `provided.al2023` and later.
+ **Customer-managed runtimes:** Supported when the runtime declares support for Lambda Managed Instances. You can use a customer-managed runtime to run other languages, or your own builds of supported languages, on Lambda Managed Instances. For more information, see [Lambda Managed Instances](cmr-building-images.md#cmr-building-images-managed-instances).

## Language-specific considerations
<a name="lambda-managed-instances-runtime-considerations"></a>

Each programming language implements multi-concurrency differently. You need to understand how multi-concurrency is implemented in your chosen programming language to apply the appropriate concurrency best practices.

**Java**

Uses a single process with OS threads for concurrency. Multiple threads execute the handler method simultaneously, requiring thread-safe handling of state and shared resources.

**Python**

Uses multiple Python processes where each concurrent request runs in a separate process. This protects against most concurrency issues, though care is required for shared resources such as the `/tmp` directory.

**Node.js**

Uses [worker threads](https://nodejs.org/api/worker_threads.html) with asynchronous execution. Concurrent requests are distributed across worker threads, and each worker thread can also handle concurrent requests asynchronously, requiring safe handling of state and shared resources.

**.NET**

Uses .NET Tasks with asynchronous processing of multiple concurrent requests. Requires safe handling of state and shared resources.

**Rust**

Uses a single process with async tasks powered by [Tokio](https://tokio.rs/). The handler must be `Clone` \+ `Send`.

**Customer-managed runtimes**

The runtime publisher implements multi-concurrency. For the concurrency model and how to handle state safely, see the runtime publisher's documentation. For the requirements that a runtime must meet, see [Supporting Lambda Managed Instances in your runtime](runtimes-custom.md#runtimes-custom-managed-instances).

## Next steps
<a name="lambda-managed-instances-runtime-next-steps"></a>

For detailed information about each runtime, see the following topics:
+ [Java runtime for Lambda Managed Instances](lambda-managed-instances-java-runtime.md)
+ [Node.js runtime for Lambda Managed Instances](lambda-managed-instances-nodejs-runtime.md)
+ [Python runtime for Lambda Managed Instances](lambda-managed-instances-python-runtime.md)
+ [.NET runtime for Lambda Managed Instances](lambda-managed-instances-dotnet-runtime.md)
+ [Rust support for Lambda Managed Instances](lambda-managed-instances-rust.md)
+ [Customer-managed runtimes](runtimes-customer-managed.md)