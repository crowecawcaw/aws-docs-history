

# Sequential executor
<a name="monetization-functions-types-sequential-executor"></a>

## When to use
<a name="monetization-functions-types-sequential-executor-when"></a>

A `SEQUENTIAL_EXECUTOR` runs a series of functions one at a time, in order. Each step can use the results of the steps before it.

Use `SEQUENTIAL_EXECUTOR` when your logic requires multiple steps that depend on each other's results. Common use cases include fetching identity data and then using it to retrieve audience segments, running a classification step and then conditionally calling different external services based on the result, and building complex ad request URLs from multiple data sources.

## Configuration fields
<a name="monetization-functions-types-sequential-executor-fields"></a>

A `SEQUENTIAL_EXECUTOR` function has the following fields:
+ **Runtime** — The expression language. Set this to `JSONATA`.
+ **FunctionList** — An ordered list of 1 to 10 steps. Each step specifies the `FunctionId` of the function to run. Optionally, you can add a `RunCondition` expression to control whether the step runs or is skipped.
+ **Output** — Defines the values to produce after all steps complete. Each entry maps an output key (such as `player_params.envelope`) to an expression that can reference data produced by any step in the sequence. If omitted, all output from the individual functions in the sequence is used.
+ **TimeoutMilliseconds** (required) — The maximum time for the entire sequence to complete. If the sequence exceeds this timeout, MediaTailor discards all output from the sequence.

## Ordered execution and data flow
<a name="monetization-functions-types-sequential-executor-data-flow"></a>

MediaTailor runs each step in the sequence from first to last. After each step completes, the values it produces are merged into a running set of results. Subsequent steps can access the original session data plus all values produced by earlier steps.

Temporary data is the primary mechanism for passing data between steps. When a function writes to a `temp.*` key, the next step can read that value. Player parameters and ad request fields written by earlier steps are also visible to later steps.

**Note**  
Temporary data accepts any data type, including objects and arrays. Player parameters and ad request fields accept only strings, numbers, booleans, and null).

## Per-step run conditions
<a name="monetization-functions-types-sequential-executor-run-conditions"></a>

Each step in the sequence has an optional `RunCondition` field. This field contains an expression that returns `true` or `false`. MediaTailor evaluates the `RunCondition` expression immediately before running that step.

If the `RunCondition` expression evaluates to `false`, MediaTailor skips the step entirely and moves to the next one. If the `RunCondition` field is omitted, the step always runs.

```
{ "FunctionId": "retryFetch", "RunCondition": "{%temp.statusCode = 500%}" }
```

This mechanism lets you build conditional pipelines. For example, you can run an identity fetch in step 1, then conditionally run a segment lookup in step 2 only if step 1 returned a valid identity.

## How the output block works
<a name="monetization-functions-types-sequential-executor-output"></a>

The output block on a `SEQUENTIAL_EXECUTOR` controls what the sequence produces after all steps complete:
+ **Output block present** — MediaTailor evaluates the expressions in the output block against the final accumulated state and saves only those outputs. Any outputs produced by earlier steps that are not referenced in the sequential output block are discarded.
+ **Output block absent** — MediaTailor saves all accumulated outputs from all steps directly.

**Tip**  
Omit the output block when you want every function's output to pass through. Add an output block when you need to filter, rename, or transform the accumulated results before saving them.

## Timeout configuration
<a name="monetization-functions-types-sequential-executor-timeout"></a>

The `TimeoutMilliseconds` field sets a deadline for the entire sequence. This timeout covers all steps, including any HTTP calls made by functions. If the sequence exceeds the timeout, MediaTailor discards all output from the sequence and proceeds as if no function were attached.

Individual `HTTP_REQUEST` functions still respect their own `RequestTimeoutMilliseconds` setting. The sequence timeout acts as an outer boundary that caps the total execution time.

## Example: Retry on HTTP failure
<a name="monetization-functions-types-sequential-executor-example"></a>

This example calls an identity API and automatically retries if the first call returns a server error. It uses two HTTP\_REQUEST functions orchestrated by a SEQUENTIAL\_EXECUTOR.

**Step 1 — Primary fetch (`fetchIdentity`):**

```
{
    "FunctionId": "fetchIdentity",
    "FunctionType": "HTTP_REQUEST",
    "HttpRequestConfiguration": {
        "Runtime": "JSONATA",
        "MethodType": "GET",
        "Url": "{%'https://identity.example.com/v1/resolve?ip=' & session.client_ip%}",
        "Headers": {
            "Accept": "application/json"
        },
        "RequestTimeoutMilliseconds": 1000,
        "Output": {
            "temp.statusCode": "{%response.statusCode%}",
            "temp.envelope": "{%response.statusCode = 200 ? response.body.envelope : null%}"
        }
    }
}
```

**Step 2 — Retry on failure (`retryIdentity`):**

```
{
    "FunctionId": "retryIdentity",
    "FunctionType": "HTTP_REQUEST",
    "HttpRequestConfiguration": {
        "Runtime": "JSONATA",
        "MethodType": "GET",
        "Url": "{%'https://identity-fallback.example.com/v1/resolve?ip=' & session.client_ip%}",
        "Headers": {
            "Accept": "application/json"
        },
        "RequestTimeoutMilliseconds": 1000,
        "Output": {
            "temp.statusCode": "{%response.statusCode%}",
            "temp.envelope": "{%response.statusCode = 200 ? response.body.envelope : null%}"
        }
    }
}
```

**Sequence (`identityWithRetry`):**

```
{
    "FunctionId": "identityWithRetry",
    "FunctionType": "SEQUENTIAL_EXECUTOR",
    "SequentialExecutorConfiguration": {
        "Runtime": "JSONATA",
        "TimeoutMilliseconds": 2000,
        "FunctionList": [
            { "FunctionId": "fetchIdentity" },
            { "FunctionId": "retryIdentity", "RunCondition": "{%temp.statusCode >= 500%}" }
        ],
        "Output": {
            "player_params.envelope": "{%temp.envelope%}"
        }
    }
}
```

**How it works:**

1. `fetchIdentity` calls the identity API and writes the status code and envelope to `temp.*`.

1. If the status code is 500 or higher, the `RunCondition` on step 2 evaluates to `true` and `retryIdentity` runs. It overwrites `temp.statusCode` and `temp.envelope` with the retry response.

1. If the first call succeeded, step 2 is skipped.

1. The sequence Output block writes `temp.envelope` to `player_params.envelope`.