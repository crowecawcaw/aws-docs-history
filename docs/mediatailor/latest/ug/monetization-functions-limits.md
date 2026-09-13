

# Functions limits
<a name="monetization-functions-limits"></a>

This page lists the limits that apply to Functions. These limits are enforced at authoring time (when you create or update a function) and at runtime (when the function runs).

## Hook execution limits
<a name="monetization-functions-limits-hook"></a>


| Hook | Limit | Value | 
| --- | --- | --- | 
| PRE\_SESSION\_INITIALIZATION | Total timeout | 2,000 ms | 
| PRE\_SESSION\_INITIALIZATION | Total player\_params size | 1,000 characters | 
| PRE\_ADS\_REQUEST | Total timeout | 2,000 ms | 
| POST\_ADS\_RESPONSE | Total timeout | 2,000 ms | 
| POST\_ADS\_RESPONSE | Input payload size | 128 KB | 
| POST\_ADS\_RESPONSE | Output size | 256 KB | 
| PRE\_MANIFEST\_INSERTION | Total timeout | 2,000 ms | 
| PRE\_MANIFEST\_INSERTION | Input payload size | 128 KB | 
| PRE\_MANIFEST\_INSERTION | Output size | 256 KB | 
| PRE\_MANIFEST\_INSERTION | Injected ads per invocation | 10 | 
| Request-path hooks combined (per request) | Shared execution budget | 2,000 ms | 

These timeouts cover the entire hook execution, including all function steps and HTTP calls. If the hook exceeds its timeout, MediaTailor discards all output and proceeds as if no function were attached.

In addition to each hook's own timeout, the `PRE_ADS_REQUEST`, `POST_ADS_RESPONSE`, and `PRE_MANIFEST_INSERTION` hooks that run within a single request share a combined execution budget of 2,000 ms. Time spent by an earlier hook reduces the budget available to later hooks in the same request, and a hook's effective timeout is the smaller of its own timeout and the remaining budget. If the budget is exhausted before a hook starts, MediaTailor skips that hook entirely and continues processing the request. `PRE_SESSION_INITIALIZATION` runs during session initialization and is not part of the combined budget.

The input payload size limit applies to the serialized JSON input that MediaTailor builds for the `POST_ADS_RESPONSE` and `PRE_MANIFEST_INSERTION` hooks. If the input exceeds 128 KB, MediaTailor skips the hook invocation for that request. The output size limit caps the total serialized size that a function can write to the hook's writable namespace; output that exceeds 256 KB is discarded.

Individual function timeouts (such as `RequestTimeoutMilliseconds` for HTTP\_REQUEST functions) must fit within the hook's total timeout. For example, if the hook timeout is 2,000 ms and an HTTP\_REQUEST function sets `RequestTimeoutMilliseconds` to 2,000 ms, the function may time out before completing if any processing occurs before or after the HTTP call.

The `player_params` total size includes the combined character count of all output key names and values. For example, outputting `player_params.deviceType = "mobile"` and `player_params.region = "us-east-1"` counts `deviceType`, `mobile`, `region`, and `us-east-1` toward the 1,000-character total.

## Expression limits
<a name="monetization-functions-limits-expression"></a>


| Limit | Value | Enforced at | 
| --- | --- | --- | 
| CPU time per expression | 100 ms | Runtime | 
| Stack depth | 100 | Runtime | 
| Expression length | 1,000 characters | Authoring | 

When an expression exceeds a limit at runtime, MediaTailor stops the expression and records the error. For details on specific error types, see [Troubleshooting and monitoring](monetization-functions-troubleshooting.md).

## Function composition limits
<a name="monetization-functions-limits-composition"></a>


| Limit | Value | 
| --- | --- | 
| Steps per sequential executor | 1–10 | 
| Children per concurrent executor | 1–10 | 
| Maximum concurrency (concurrent executor) | 1–2 | 
| Default timeout (concurrent executor) | 2,000 ms | 
| Unique namespaces per concurrent executor | Required (validated at authoring time) | 
| Maximum nesting depth | 2 | 
| Total function executions per hook | 20 | 
| Output entries per function | 20 | 
| Circular references | Not allowed | 

These limits are enforced at authoring time.

## HTTP request limits
<a name="monetization-functions-limits-http"></a>


| Limit | Value | 
| --- | --- | 
| URL expression length | 25,000 characters | 
| URL length (after evaluation) | 2,048 characters | 
| Body expression length | 100,000 characters | 
| Request body size (after evaluation) | 64 KB | 
| Header count | 50 | 
| Header name length | 256 characters | 
| Header value length | 8,192 characters | 
| Request timeout | 100–2,000 ms (customer-configurable via RequestTimeoutMilliseconds) | 
| Allowed URL schemes | https, http | 
| Restricted headers | Host, Transfer-Encoding, Content-Length, Connection | 

Expression length limits and header limits are enforced at authoring time, when you create or update the function. The evaluated URL and body size limits, the request timeout, and restricted headers are enforced at runtime, after MediaTailor evaluates the expressions. A URL expression that is accepted at authoring time can still exceed the evaluated URL limit at runtime, in which case the request is not sent.

If a function sets a restricted header, MediaTailor accepts the function configuration at authoring time but drops the header when the HTTP request is sent during execution.

## Response limits
<a name="monetization-functions-limits-response"></a>


| Limit | Value | 
| --- | --- | 
| response.body maximum size | 20,000 characters | 
| response.text maximum length | 20,000 characters | 

These limits are enforced at runtime.

## Output limits
<a name="monetization-functions-limits-output"></a>


| Limit | Value | 
| --- | --- | 
| Output value max length (per key) | 1,000 characters | 

These limits are enforced at runtime.

## Allowed JSONata functions
<a name="monetization-functions-limits-jsonata"></a>

For the full list of allowed functions, see [JSONata expression reference](monetization-functions-jsonata.md).

For help diagnosing errors related to these limits, see [Troubleshooting and monitoring](monetization-functions-troubleshooting.md).