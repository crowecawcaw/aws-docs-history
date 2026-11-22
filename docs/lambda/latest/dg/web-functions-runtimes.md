

# Lambda Web Function runtimes

Lambda Web Functions use managed language runtimes. Select the runtime that matches your application code when you create a revision. The runtime identifier is immutable for that revision.

## Available runtimes
<a name="web-functions-runtimes-versions"></a>

**Note**  
The `python3.15` runtime is in **public preview**. Preview runtimes are not covered by the Lambda SLA or Technical Support, and should not be used for production workloads.  
The purpose of preview runtimes is to gather feedback from customers, partners, and upstream language communities prior to General Availability, while breaking changes are still possible. You can provide feedback through the dedicated [Python runtime support for Lambda Web Functions issue on the GitHub website](https://github.com/aws/aws-lambda-roadmap/issues/102).


| Runtime identifier | Language version | Status | 
| --- | --- | --- | 
| nodejs24.x | Node.js 24 | Supported | 
| nodejs26.x | Node.js 26 | Supported | 
| python3.15 | Python 3.15 | Preview | 

Specify the runtime identifier in the `runtimeConfig` section when you create a revision. For example:

```json
"runtimeConfig": { "runtime": "python3.15" }
```

Each Web Function runtime follows the same deprecation cycle as the corresponding Lambda Event Functions runtime. For deprecation dates and the deprecation process, see [Runtime deprecation](runtime-support-policy.md).

## Automatic runtime patching
<a name="web-functions-runtimes-patching"></a>

Lambda automatically patches managed Web Function runtimes with security updates and bug fixes. Patching applies to the underlying runtime layer and does not change your application code. Your revision's `runtime` identifier always resolves to the latest patched version of that major runtime.

**Note**  
Runtime management controls are not supported for Web Functions. You cannot pin to a specific patch version or disable automatic patching. Lambda always uses the latest patched version of the runtime that you specify.  
Web Functions also don't use the [Two-phase runtime version rollout](runtimes-update.md#runtime-management-two-phase) that applies to Lambda Event Functions. A new patched runtime version reaches your Web Function in a single rollout, and a revision never remains on an earlier patch version.

For more information about how Lambda manages runtime updates, see [Understanding how Lambda manages runtime updates](runtimes-update.md).

## Request routing and TLS
<a name="web-functions-runtimes-port"></a>

Web Function endpoints accept HTTPS traffic only, on port 443. Plain HTTP is not served, so you don't need to redirect HTTP to HTTPS or configure TLS in your application.

Lambda terminates TLS at the endpoint and forwards each request to the HTTP server in the execution environment. The server returns your application's response to Lambda, which returns it to the client.

Lambda adds a `lambda-web-request-id` header to every request and returns the same value as a response header, so you can correlate a client request with your application logs.

Each request is bound by the revision's `timeoutSeconds` setting. For the startup and shutdown sequence, see [Execution environment lifecycle](web-functions-env-lifecycle.md). For how to configure `timeoutSeconds`, see [Managing Web Function revisions](web-functions-revisions.md).

## Language-specific considerations
<a name="web-functions-runtimes-language-specific"></a>

For application and concurrency guidance, see the topic for your language:
+ [Building Lambda Web Functions with Node.js](web-functions-nodejs.md)
+ [Building Lambda Web Functions with Python](web-functions-python.md)