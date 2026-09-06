

# Troubleshooting and monitoring Functions
<a name="monetization-functions-troubleshooting"></a>

This page helps you diagnose common function errors and monitor function performance in production. The troubleshooting section is organized by symptom — start with what you observe, then follow the cause and fix.

## Monitoring
<a name="monetization-functions-troubleshooting-monitoring"></a>

### CloudWatch metrics
<a name="monetization-functions-troubleshooting-cw-metrics"></a>

MediaTailor publishes metrics for function execution to Amazon CloudWatch. No opt-in is required.

**Hook-level metrics** — one data point per lifecycle hook execution:


| Metric | Description | Dimensions | 
| --- | --- | --- | 
| PreSessionInitHook.Invocations | Count of hook executions | ConfigurationName | 
| PreSessionInitHook.Errors | Count of hook errors | ConfigurationName | 
| PreSessionInitHook.Latency | Hook execution time (ms) | ConfigurationName | 
| PreAdsRequestHook.Invocations | Count of hook executions | ConfigurationName | 
| PreAdsRequestHook.Errors | Count of hook errors | ConfigurationName | 
| PreAdsRequestHook.Latency | Hook execution time (ms) | ConfigurationName | 

**Function-level metrics** — one data point per individual function execution:


| Metric | Description | Dimensions | 
| --- | --- | --- | 
| Function.Invocations | Count of function executions | ConfigurationName, FunctionId, FunctionType, HookType | 
| Function.Errors | Count of function errors | ConfigurationName, FunctionId, FunctionType, HookType | 
| Function.Latency | Function execution time (ms) | ConfigurationName, FunctionId, FunctionType, HookType | 

For more details on setting up alarms and working with these metrics, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md).

### Log events
<a name="monetization-functions-troubleshooting-log-events"></a>

MediaTailor emits log events for function execution. Error events are emitted by default. Completed and summary events are opt-in.


| Event type | Default / Opt-in | Log group | Description | 
| --- | --- | --- | --- | 
| PRE\_SESSION\_INIT\_HOOK\_SUMMARY | Opt-in | Manifest Log | Hook execution summary (success/error) | 
| PRE\_SESSION\_INIT\_HOOK\_ERROR | Default | Manifest Log | Hook failure with errorType and cause | 
| PRE\_SESSION\_INIT\_FUNCTION\_COMPLETED | Opt-in | Manifest Log | Individual function completed with input/output | 
| PRE\_SESSION\_INIT\_FUNCTION\_ERROR | Default | Manifest Log | Individual function failure | 
| PRE\_ADS\_REQUEST\_HOOK\_SUMMARY | Opt-in | ADS Interaction Log | Hook execution summary (success/error) | 
| PRE\_ADS\_REQUEST\_HOOK\_ERROR | Default | ADS Interaction Log | Hook failure with errorType and cause | 
| PRE\_ADS\_REQUEST\_FUNCTION\_COMPLETED | Opt-in | ADS Interaction Log | Individual function completed with input/output | 
| PRE\_ADS\_REQUEST\_FUNCTION\_ERROR | Default | ADS Interaction Log | Individual function failure | 

To enable opt-in log events, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md).

Use the `eventId` field to correlate hook-level and function-level events for the same execution.

The following Amazon CloudWatch Logs Insights query filters function error events by `eventId` to trace a single execution:

```
fields @timestamp, eventType, functionId, errorType, cause
| filter eventId = "5dc6f040-0f72-4e8c-a64e-25eeef62708c"
| sort @timestamp asc
```

## Troubleshooting
<a name="monetization-functions-troubleshooting-guide"></a>

When a function fails, MediaTailor logs an `errorType` field in the error event. Use this field to identify the class of failure:


| Error type | Description | 
| --- | --- | 
| SYNTAX\_ERROR | Expression failed to compile or encountered a runtime type error | 
| RESOURCE\_LIMIT\_ERROR | Expression exceeded CPU time, memory, or stack depth limits | 
| RESTRICTION\_ERROR | Expression used a blocked function, or input payload size limit exceeded | 
| TIMEOUT\_ERROR | Function execution exceeded its time limit | 
| VALIDATION\_ERROR | Output path targets a field not writable in the current hook's scope | 
| INTERNAL\_ERROR | Infrastructure failure unrelated to the function | 

The entries are organized by symptom and reference these error types where applicable.

### Expression returns null unexpectedly
<a name="monetization-functions-ts-null"></a>

**Symptom:** An output value you expected to be populated is `null` or missing from player parameters.

**Possible causes:**


| Cause | How to identify | Fix | 
| --- | --- | --- | 
| The input field does not exist at this lifecycle hook. | You referenced adsRequest.url in a PRE\_SESSION\_INITIALIZATION function. ADS request data is not available at session start. | Move the function to the PRE\_ADS\_REQUEST lifecycle hook, or use a different input field. See [Lifecycle hooks](monetization-functions-hooks.md). | 
| The input field is missing from the session data. | You referenced player\_params.campaign\_id, but the player did not pass that parameter at session initialization. | Use $exists() to check before accessing: {%$exists(player\_params.campaign\_id) ? player\_params.campaign\_id : 'default'%}. | 
| You wrote an object or array to player parameters or the ADS request. | These namespaces accept only strings, numbers, and booleans. Objects and arrays are filtered out. | Store complex data in temp.\* and extract strings, numbers, or booleans in a subsequent step. | 

### `RESOURCE_LIMIT_ERROR`: Stack overflow
<a name="monetization-functions-ts-stack-overflow"></a>

**Symptom:** The function fails with `errorType: "RESOURCE_LIMIT_ERROR"` and `cause: "Stack overflow error"`.

**Cause:** The expression exceeded the maximum stack depth of 100 levels. This typically happens with deeply nested conditional (if/then/else) expressions or complex variable assignments.

This means the expression has too many levels of nesting for MediaTailor to process.

**Fix:** Simplify the expression. Break complex logic into multiple output entries or multiple steps in a sequential executor.

### `RESOURCE_LIMIT_ERROR`: CPU timeout
<a name="monetization-functions-ts-cpu-timeout"></a>

**Symptom:** The function fails with `errorType: "RESOURCE_LIMIT_ERROR"` and `cause: "Expression evaluation timeout: Check for infinite loop"`.

**Cause:** The expression exceeded the 100 ms CPU time limit. This can happen with expressions that perform expensive computations over large data structures.

**Fix:** Reduce the complexity of the expression. If you are processing large arrays, consider moving that logic to an external service and calling it with an `HTTP_REQUEST` function.

### `RESTRICTION_ERROR`: Function not allowed
<a name="monetization-functions-ts-function-not-allowed"></a>

**Symptom:** The function fails with `errorType: "RESTRICTION_ERROR"` and `cause: "Function '<name>' is not allowed"`.

**Cause:** The expression calls a JSONata function that is not in the allowed list of 38 functions. Common examples include `$filter`, `$reduce`, `$eval`, `$split`, and `$join`.

**Fix:** Check the `cause` field for the blocked function name. Replace it with an allowed alternative. See [JSONata expression reference](monetization-functions-jsonata.md) for the full list of 38 allowed functions.

Commonly used allowed functions include `$string`, `$number`, `$substring`, `$contains`, and `$encodeUrlComponent`.

### `RESTRICTION_ERROR`: Expression too long
<a name="monetization-functions-ts-expression-too-long"></a>

**Symptom:** The function fails to create or update with `cause: "Expression length <actual> exceeds limit <limit>"`.

**Cause:** A single expression exceeds 1,000 characters.

**Fix:** Break the expression into smaller parts. Use multiple output entries, or split the logic across multiple steps in a sequential executor. Use variable binding (`:=`) to avoid repeating long subexpressions.

### HTTP error: Status code is null
<a name="monetization-functions-ts-status-null"></a>

**Symptom:** In an `HTTP_REQUEST` function's output, `response.statusCode` is `null`.

**Cause:** The external API was unreachable, the connection timed out, or a network error occurred. When this happens, MediaTailor sets `response.statusCode` to `null`, `response.body` to `null`, and `response.text` to `"Internal Error"`.

**Fix:** Always check `response.statusCode` before accessing response data:

```
{%response.statusCode = 200 ? response.body.value : 'default'%}
```

This expression checks whether the HTTP call returned a 200 status code. If it did, it uses the response value. Otherwise, it falls back to a default value.

If this happens frequently, check whether the external API is healthy. Consider increasing `RequestTimeoutMilliseconds` if the API is slow, or decreasing it if you want to fail fast.

### HTTP error: Response body is null
<a name="monetization-functions-ts-body-null"></a>

**Symptom:** `response.statusCode` is 200 but `response.body` is `null`.

**Cause:** The response body is either not valid JSON or exceeds 20,000 characters. MediaTailor only parses JSON responses up to 20,000 characters into `response.body`.

**Fix:** Use `response.text` as a fallback. The `response.text` field contains the raw response body truncated to 20,000 characters:

```
{%response.statusCode = 200 ? ($exists(response.body.id) ? response.body.id : $substring(response.text, 0, 100)) : 'error'%}
```

If the data you need is beyond the 20,000-character limit, consider asking the external API to return a smaller response (for example, by requesting specific fields).

### HTTP error: URL validation failure
<a name="monetization-functions-ts-url-validation"></a>

**Symptom:** The function fails at runtime with a message about the URL being malformed, using an invalid scheme, or exceeding the maximum length.

**Possible causes:**


| Cause | Fix | 
| --- | --- | 
| The URL does not use http or https. | Ensure the URL expression produces a URL starting with http:// or https://. | 
| The URL exceeds 2,048 characters after expression evaluation. | Shorten the URL. Move large parameter values to the request body using a POST method. | 
| The URL is malformed (not a valid URI). | Check the expression for missing or extra characters. Use $encodeUrlComponent() for query parameter values that may contain special characters. | 

### `VALIDATION_ERROR`
<a name="monetization-functions-ts-validation-error"></a>

**Symptom:** The function fails with `errorType: "VALIDATION_ERROR"`. This error can occur at authoring time (when you create or update the function) or at execution time (when the function runs during a session).

**Possible causes:**


| Cause | Example | Fix | 
| --- | --- | --- | 
| Output key targets a namespace not writable at the current hook. | Writing to adsRequest.url in a function attached to PRE\_SESSION\_INITIALIZATION. | Check which output namespaces are allowed at your lifecycle hook. PRE\_SESSION\_INITIALIZATION only allows player\_params.\*. Either move the function to the correct hook or change the output key. See [Lifecycle hooks](monetization-functions-hooks.md). | 
| Output key uses invalid characters. | An output key like player\_params.device type (with a space). Only letters, numbers, underscores, and hyphens are allowed. | Rename the output key to use only valid characters. For example, use player\_params.device\_type instead. | 
| Output key doesn't start with a valid prefix. | An output key like custom.myValue instead of player\_params.myValue or temp.myValue. | Use a valid output prefix: player\_params.\*, temp.\*, or adsRequest.\*. | 
| A JSONata expression has a syntax error. | A missing closing quote or incomplete conditional: {%session.id & %}. | Review the expression for missing quotes, unmatched parentheses, or unsupported operators like ?? or ?:. | 
| A required field is missing in an HTTP\_REQUEST function. | The URL field is empty or the method is not specified. | Ensure the URL and method fields are set. The method must be GET or POST. | 
| The URL built by the expression is invalid. | The evaluated URL uses an unsupported scheme like ftp://, exceeds 2,048 characters, or is malformed. | Verify the URL expression produces a valid http:// or https:// URL. Use $encodeUrlComponent() for query parameter values that may contain special characters. | 
| An HTTP header contains invalid characters or uses a restricted name. | A header value contains line breaks, or the header name is host or transfer-encoding. | Remove invalid characters from header values. Avoid restricted header names. See [HTTP request](monetization-functions-types-http-request.md) for header limits. | 

Check the `cause` field in the error log event — it identifies which field or expression failed validation.

### `INTERNAL_ERROR`
<a name="monetization-functions-ts-internal-error"></a>

**Symptom:** The function fails with `errorType: "INTERNAL_ERROR"`.

**Cause:** An infrastructure failure occurred that is unrelated to your function configuration.

**Fix:** Retry the request. If the error persists, contact AWS Support.