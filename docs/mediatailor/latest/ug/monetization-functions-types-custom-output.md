# Custom output

## When to use

Use `CUSTOM_OUTPUT` when your function logic is purely computational.
Common use cases include classifying devices based on user agent strings, selecting
ad decision server URLs with A/B testing logic, and reformatting player parameters
before they reach the ad decision server.

`CUSTOM_OUTPUT` functions are the fastest type because they evaluate
expressions in memory with no network calls. Choose this type whenever you can
accomplish your goal without contacting an external service.

## Configuration fields

A `CUSTOM_OUTPUT` function has two fields:

- **Runtime** — The expression language.
  Set this to `JSONATA`.
- **Output** — A map of key-value pairs.
  Each key is an output binding name (such as
  `player_params.device_type`), and each value is an expression
  that MediaTailor evaluates at runtime.

###### Note

Use `{%...%}` to wrap JSONata expressions in string fields. Values
without these delimiters are treated as static strings. For example,
`"{%session.id%}"` evaluates the expression, while
`"session.id"` is the literal text.

## Runtime behavior

When MediaTailor executes a `CUSTOM_OUTPUT` function, it evaluates every
expression in the output block against the current session state. All expressions see
the same input snapshot. The evaluated results become the function's outputs.

If any expression fails to evaluate, MediaTailor discards the entire function's output
and proceeds as if no function were attached. The function does not partially commit
results.

## Example: A/B traffic split

The following function randomly assigns each ad break to one of two ad decision server
URLs. It is designed for the `PRE_ADS_REQUEST` lifecycle hook.

```
{
    "FunctionId": "abTestAdsUrl",
    "FunctionType": "CUSTOM_OUTPUT",
    "CustomOutputConfiguration": {
        "Runtime": "JSONATA",
        "Output": {
            "adsRequest.url": "{%$random() < 0.5 ? 'https://ads.example.com/v1' : 'https://ads.example.com/v2'%}"
        }
    }
}
```

For a complete walkthrough of this example, see [Function examples](monetization-functions-examples.md "monetization-functions-examples.md").
