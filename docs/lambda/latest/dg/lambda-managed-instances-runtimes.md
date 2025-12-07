# Lambda Managed Instances runtimes

Lambda processes requests differently when using Lambda Managed Instances. Instead of handling requests sequentially in each execution environment, Lambda Managed Instances process multiple requests concurrently within each execution environment. This change in execution model means that functions using Lambda Managed Instances need to consider thread safety, state management, and context isolation, concerns which do not arise in the Lambda (default) single-concurrency model. In addition, the multi-concurrency implementation varies between runtimes.

## Supported runtimes

The following runtimes support Lambda Managed Instances:

- **Java:** Java 21 and later.
- **Python:** Python 3.13 and later.
- **Node.js:** Node.js 22 and later.
- **.NET:** .NET 8 and later.

## Runtime-specific considerations

Each runtime implements multi-concurrency differently. You need to understand how multi-concurrency is implemented in your chosen programming language to apply the appropriate concurrency best practices.

**Java**

Uses a single process with OS threads for concurrency. Multiple threads execute the handler method simultaneously, requiring thread-safe handling of state and shared resources.

**Python**

Uses multiple Python processes where each concurrent request runs in a separate process. This protects against most concurrency issues, though care is required for shared resources such as the `/tmp` directory.

**Node.js**

Uses [worker threads](https://nodejs.org/api/worker_threads.html "https://nodejs.org/api/worker_threads.html") with asynchronous execution. Concurrent requests are distributed across worker threads, and each worker thread can also handle concurrent requests asynchronously, requiring safe handling of state and shared resources.

**.NET**

Uses .NET Tasks with asynchronous processing of multiple concurrent requests. Requires safe handling of state and shared resources.

## Next steps

For detailed information about each runtime, see the following topics:

- [Java runtime for Lambda Managed Instances](lambda-managed-instances-java-runtime.md "lambda-managed-instances-java-runtime.md")
- [Node.js runtime for Lambda Managed Instances](lambda-managed-instances-nodejs-runtime.md "lambda-managed-instances-nodejs-runtime.md")
- [Python runtime for Lambda Managed Instances](lambda-managed-instances-python-runtime.md "lambda-managed-instances-python-runtime.md")
- [.NET runtime for Lambda Managed Instances](lambda-managed-instances-dotnet-runtime.md "lambda-managed-instances-dotnet-runtime.md")
