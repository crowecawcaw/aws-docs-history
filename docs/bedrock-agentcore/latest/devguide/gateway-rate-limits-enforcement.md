# Rate limit enforcement

This topic describes how the gateway evaluates and enforces rate limits at runtime, including interaction with other gateway features, throttled response formats, and observability.

## Interaction with gateway rules

The gateway evaluates rate limits **before** gateway rules. If a rate limit throttles a request, the request never reaches the rule evaluation stage.

## Stacking semantics

When multiple rate limits apply to a request, the gateway uses AND logic — all rate limits must pass for the request to proceed. If any single rate limit denies the request, the gateway throttles it.

## Entry matching and specificity

When a rate limit has multiple entries, the gateway selects the most specific matching entry for the resolved dimension values:

- An exact value match takes precedence over a `*` entry.
- The `*` value means "apply this rate to all values of this dimension" — it acts as a default entry.
- For multi-dimension rate limits, the gateway uses progressive trailing fallback: it first attempts a full exact match, then replaces trailing dimensions with `*` one at a time until a match is found.

The following example shows how entries are matched for a rate limit with `dimensionKeys: ["targetName", "toolName"]` when the resolved values are `["my-target", "readData"]`:

| Entry dimensions                                      | Matches?             | Why                                            |
| ----------------------------------------------------- | -------------------- | ---------------------------------------------- |
| `{"targetName": "my-target", "toolName": "readData"}` | Yes (checked first)  | Exact match on both dimensions. Most specific. |
| `{"targetName": "my-target", "toolName": "*"}`        | Yes (checked second) | Exact match on first dimension, `*` on second. |
| `{"targetName": "**", "toolName": "**"}`              | Yes (checked last)   | Default entry. Least specific.                 |

The first matching entry wins. If no entry matches (and no `*` default exists), the rate limit is skipped for that request.

## Evaluation order

The gateway evaluates rate limits in the following order:

1. The gateway evaluates rate limits with more dimension keys first (more specific limits take priority).
2. Within the same number of dimensions, the gateway evaluates rate limits with tighter (lower) rates first.
3. Evaluation short-circuits on the first denial — the gateway does not evaluate remaining rate limits.

## Interaction with service-managed limits

The gateway enforces both customer-defined rate limits and service-managed limits. The effective rate for any request is the minimum of both:

- The gateway evaluates customer-defined rate limits first.
- If the request passes customer limits, service-managed limits are evaluated.
- A denial from either source results in throttling.

## Throttled responses

When a request is throttled, the gateway returns a protocol-specific error response containing the `retryAfter` value in the response body.

**HTTP protocol:**

```
{
    "error": "Rate limit exceeded",
    "success": false,
    "limitKey": "rl-abc123/targetName=my-target",
    "metric": "requests",
    "retryAfter": 1
}
```

**MCP protocol (JSON-RPC):**

```
{
    "jsonrpc": "2.0",
    "id": "request-1",
    "error": {
        "code": -32003,
        "message": "Rate limit exceeded",
        "data": {
            "limitKey": "rl-abc123/targetName=my-target",
            "metric": "requests",
            "retryAfter": 1
        }
    }
}
```

**OpenAI-compatible protocol:**

```
{
    "error": {
        "message": "Rate limit exceeded",
        "type": "rate_limit_error",
        "code": "429",
        "limitKey": "rl-abc123/qualifiedModelId=anthropic.claude-3-sonnet",
        "metric": "tokens",
        "retryAfter": 60
    }
}
```

**Anthropic-compatible protocol:**

```
{
    "type": "error",
    "error": {
        "type": "rate_limit_error",
        "message": "Rate limit exceeded",
        "limitKey": "rl-abc123/qualifiedModelId=anthropic.claude-3-sonnet",
        "metric": "tokens",
        "retryAfter": 60
    }
}
```

The `retryAfter` field indicates how many seconds the caller should wait before retrying. Use this value directly in your client-side retry logic.

## Propagation timing

Rate limit changes (create, update, delete) propagate to the data plane within 30 seconds. During propagation:

- New rate limits are not enforced until propagation completes.
- Updated rate limits continue enforcing the previous configuration until the update propagates.
- Deleted rate limits continue enforcing until the deletion propagates.

## Fail-open behavior

The gateway uses fail-open semantics for rate limit evaluation. The following table describes behavior when the rate limit system encounters errors:

| Scenario                                | Decision              | Rationale                                              |
| --------------------------------------- | --------------------- | ------------------------------------------------------ |
| Rate limit service timeout              | Allow                 | Availability takes precedence over enforcement.        |
| Dimension key unresolvable from request | Skip (allow)          | The rate limit does not apply to this request type.    |
| Rate limit cache refresh failure        | Retry with stale data | Last known configuration is used until cache recovers. |

###### Important

Because of fail-open behavior, do not rely solely on rate limits as a security boundary. Use rate limits for traffic management and quality of service, and use authentication, authorization, and WAF rules for security enforcement.

## Tracing with OpenTelemetry spans

The gateway emits OpenTelemetry (OTEL) span attributes on the server span for every request where customer rate limits are evaluated. Use these attributes for debugging and monitoring.

| Attribute                                               | Description                                                                                                                                                                                       | Example                                                                  |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `aws.agentcore.gateway.throttle.customer.decision`      | The enforcement decision for this request.                                                                                                                                                        | `allowed` or `throttled`                                                 |
| `aws.agentcore.gateway.throttle.customer.limit_key`     | The `rateLimitId` of the rate limit that rejected the request. Only present when decision is `throttled`.                                                                                         | `per-target-rps`                                                         |
| `aws.agentcore.gateway.throttle.customer.metric`        | The metric type that was exhausted. Only present when decision is `throttled`.                                                                                                                    | `requests`                                                               |
| `aws.agentcore.gateway.throttle.customer.matched_entry` | Comma-separated resolved dimension values of the entry that triggered the throttle. Only present when decision is `throttled`.                                                                    | `my-target,alice`                                                        |
| `aws.agentcore.gateway.throttle.customer.evaluated`     | Ordered list of all rate limit buckets checked for this request. Each entry shows the rate limit ID, metric, and resolved dimension values. Present for both `allowed` and `throttled` decisions. | `["per-target-rps:requests:my-target", "per-caller-rpm:requests:alice"]` |

The `evaluated` attribute is useful for understanding which rate limits applied to a request, even when it was allowed. Each entry in the list follows the format `{rateLimitId}:{metric}:{resolvedDimVal1,dimVal2,…​}`.
