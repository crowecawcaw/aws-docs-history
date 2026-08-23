# Functions limits

This page lists the limits that apply to Functions. These limits are enforced
at authoring time (when you create or update a function) and at runtime (when the function
runs).

## Hook execution limits

| Hook                         | Limit                      | Value            |
| ---------------------------- | -------------------------- | ---------------- |
| `PRE_SESSION_INITIALIZATION` | Total timeout              | 2,000 ms         |
| `PRE_SESSION_INITIALIZATION` | Total `player_params` size | 1,000 characters |
| `PRE_ADS_REQUEST`            | Total timeout              | 2,000 ms         |

These timeouts cover the entire hook execution, including all function steps and HTTP
calls. If the hook exceeds its timeout, MediaTailor discards all output and proceeds as if no function were
attached.

Individual function timeouts (such as `RequestTimeoutMilliseconds` for
HTTP\_REQUEST functions) must fit within the hook's total timeout. For example, if
the hook timeout is 2,000 ms and an HTTP\_REQUEST function sets
`RequestTimeoutMilliseconds` to 2,000 ms, the function may time out
before completing if any processing occurs before or after the HTTP call.

The `player_params` total size includes the combined character count of
all output key names and values. For example, outputting
`player_params.deviceType = "mobile"` and
`player_params.region = "us-east-1"` counts `deviceType`,
`mobile`, `region`, and `us-east-1` toward the
1,000-character total.

## Expression limits

| Limit                   | Value            | Enforced at |
| ----------------------- | ---------------- | ----------- |
| CPU time per expression | 100 ms           | Runtime     |
| Stack depth             | 100              | Runtime     |
| Expression length       | 1,000 characters | Authoring   |

When an expression exceeds a limit at runtime, MediaTailor stops the expression and
records the error. For details on specific error types, see [Troubleshooting and
monitoring](monetization-functions-troubleshooting.md "monetization-functions-troubleshooting.md").

## Function composition limits

| Limit                                     | Value                                  |
| ----------------------------------------- | -------------------------------------- |
| Steps per sequential executor             | 1–10                                   |
| Children per concurrent executor          | 1–10                                   |
| Maximum concurrency (concurrent executor) | 1–2                                    |
| Default timeout (concurrent executor)     | 2,000 ms                               |
| Unique namespaces per concurrent executor | Required (validated at authoring time) |
| Maximum nesting depth                     | 2                                      |
| Total function executions per hook        | 20                                     |
| Output entries per function               | 20                                     |
| Circular references                       | Not allowed                            |

These limits are enforced at authoring time.

## HTTP request limits

| Limit               | Value                                                                    |
| ------------------- | ------------------------------------------------------------------------ |
| URL length          | 2,048 characters                                                         |
| Request body size   | 64 KB                                                                    |
| Header count        | 50                                                                       |
| Header name length  | 256 characters                                                           |
| Header value length | 8,192 characters                                                         |
| Request timeout     | 100–2,000 ms (customer-configurable via<br>`RequestTimeoutMilliseconds`) |
| Allowed URL schemes | `https`, `http`                                                          |
| Restricted headers  | `Host`, `Transfer-Encoding`,<br>`Content-Length`, `Connection`           |

URL length, body size, header count, and header size limits are enforced at authoring time. Request timeout and restricted headers are enforced at runtime.

If a function sets a restricted header, MediaTailor accepts the function configuration
at authoring time but drops the header when the HTTP request is sent during
execution.

## Response limits

| Limit                          | Value             |
| ------------------------------ | ----------------- |
| `response.body` maximum size   | 20,000 characters |
| `response.text` maximum length | 20,000 characters |

These limits are enforced at runtime.

## Output limits

| Limit                             | Value            |
| --------------------------------- | ---------------- |
| Output value max length (per key) | 1,000 characters |

These limits are enforced at runtime.

## Allowed JSONata functions

For the full list of allowed functions, see [JSONata expression
reference](monetization-functions-jsonata.md "monetization-functions-jsonata.md").

For help diagnosing errors related to these limits, see [Troubleshooting and
monitoring](monetization-functions-troubleshooting.md "monetization-functions-troubleshooting.md").
