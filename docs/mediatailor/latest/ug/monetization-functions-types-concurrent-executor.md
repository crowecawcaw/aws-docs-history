# Concurrent executor

## When to use

A `CONCURRENT_EXECUTOR` runs a set of child functions in parallel up to
a maximum concurrency, then combines their outputs after all children complete.

Use `CONCURRENT_EXECUTOR` when your logic requires multiple independent
operations that don't depend on each other's results. Common use cases include
making parallel HTTP calls to different enrichment services, running independent
data lookups simultaneously, and reducing total latency by overlapping network
requests.

## Configuration fields

A `CONCURRENT_EXECUTOR` function has the following fields:

- **Runtime** – The expression language.
  Set this to `JSONATA`.
- **FunctionList** – A list of 1 to 10
  children to run in parallel. Each entry specifies the
  `FunctionId` of the function to run. Optionally, you can add a
  `RunCondition` expression to control whether the child runs or
  is skipped. You can also add an `Alias` to give the child a
  unique name within the executor.
- **Output** – Defines the values to
  produce after all children complete. Each entry maps an output key (such as
  `player_params.device_type`) to an expression that can reference
  data produced by any child in the executor.
- **MaxConcurrency** – The maximum number
  of children that can run simultaneously. Valid range:
  `1`–`2`. Default: `2`.
- **TimeoutMilliseconds** (required) –
  The maximum time for the entire executor to complete. If the executor
  exceeds this timeout, MediaTailor discards all output from the executor. Default:
  `2000`.

## Parallel execution and data flow

MediaTailor starts children concurrently. When the function list has more entries than
`MaxConcurrency`, MediaTailor starts additional children as running ones
complete. The number of simultaneously running children stays at or below the
concurrency limit.

Each child's result is stored under its namespace—the explicit
`Alias`, or the child's `FunctionId` if no alias is set.
After all children complete, the executor's `Output` expressions can
reference any child's results using the path
`function.<namespace>.<path>`.

###### Note

Namespaces must be unique across all children in the executor. MediaTailor validates
this requirement at authoring time.

## Per-child run conditions

Each child in the executor has an optional `RunCondition` field. This
field contains an expression that returns `true` or `false`.
MediaTailor evaluates the `RunCondition` expression immediately before
starting that child.

If the `RunCondition` expression evaluates to `false`, MediaTailor
skips the child entirely. If the `RunCondition` field is omitted, the
child always runs.

```
{ "FunctionId": "fetchDevice", "RunCondition": "{%session.player_params.device_id != null%}" }
```

With this mechanism, you can conditionally include children. For example, you can skip a
device lookup when the device ID is not present in the session.

## How the output block works

The output block on a `CONCURRENT_EXECUTOR` controls what the executor
produces after all children complete. Each entry maps an output key to an expression
that can reference any child's results using
`{%function.<namespace>.<path>%}`.

For example, if a child has an alias of `fetchUser` and writes to
`temp.user`, the executor's output expression can reference it as
`{%function.fetchUser.temp.user%}`.

## Timeout configuration

The `TimeoutMilliseconds` field sets a deadline for the entire
executor. This timeout covers all children, including any HTTP calls made by
functions. If the executor exceeds the timeout, MediaTailor discards all output from the
executor and proceeds as if no function were attached.

Individual `HTTP_REQUEST` functions still respect their own
`RequestTimeoutMilliseconds` setting. The executor timeout acts as an
outer boundary that caps the total execution time.

## Example: Parallel enrichment calls

This example calls two enrichment APIs in parallel and combines their results into
player parameters. It uses two HTTP\_REQUEST functions orchestrated by a
CONCURRENT\_EXECUTOR.

###### Child 1 – User profile (`fetchUserProfile`)

```
{
    "FunctionId": "fetchUserProfile",
    "FunctionType": "HTTP_REQUEST",
    "HttpRequestConfiguration": {
        "Runtime": "JSONATA",
        "Url": "{%'https://enrichment.example.com/user/' & session.player_params.user_id%}",
        "Headers": {},
        "Output": {
            "temp.user_segment": "{%response.body.segment%}"
        }
    }
}
```

###### Child 2 – Device info (`fetchDeviceInfo`)

```
{
    "FunctionId": "fetchDeviceInfo",
    "FunctionType": "HTTP_REQUEST",
    "HttpRequestConfiguration": {
        "Runtime": "JSONATA",
        "Url": "{%'https://enrichment.example.com/device/' & session.player_params.device_id%}",
        "Headers": {},
        "Output": {
            "temp.device_category": "{%response.body.category%}"
        }
    }
}
```

###### Executor (`parallelEnrichment`)

```
{
    "FunctionId": "parallelEnrichment",
    "FunctionType": "CONCURRENT_EXECUTOR",
    "ConcurrentExecutorConfiguration": {
        "Runtime": "JSONATA",
        "MaxConcurrency": 2,
        "TimeoutMilliseconds": 1500,
        "FunctionList": [
            {
                "FunctionId": "fetchUserProfile",
                "Alias": "userCall"
            },
            {
                "FunctionId": "fetchDeviceInfo",
                "Alias": "deviceCall",
                "RunCondition": "{%session.player_params.device_id != null%}"
            }
        ],
        "Output": {
            "player_params.user_segment": "{%function.userCall.temp.user_segment%}",
            "player_params.device_category": "{%function.deviceCall.temp.device_category%}"
        }
    }
}
```

In this example:

1. MediaTailor starts both children concurrently (MaxConcurrency is 2).
2. The `deviceCall` child only runs if `device_id` is
   present (RunCondition).
3. After both calls complete (within 1500 ms), the Output block writes the
   combined results to `player_params`.
4. If the 1500 ms timeout is exceeded, MediaTailor discards all output and proceeds
   without the enrichment data.
