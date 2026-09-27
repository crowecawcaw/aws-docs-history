

# Pre-session initialization
<a name="monetization-functions-hooks-pre-session"></a>

## When it fires
<a name="monetization-functions-hooks-pre-session-when"></a>

MediaTailor runs the function mapped to `PRE_SESSION_INITIALIZATION` once, at the start of a new playback session. The function runs before MediaTailor constructs the initial manifest response.

## Input
<a name="monetization-functions-hooks-pre-session-input"></a>

`session.*`, `player_params.*`, and `event.*`. For all available fields, see [Input field reference](monetization-functions-hooks.md#monetization-functions-hooks-input-ref).

## Output namespace allowed
<a name="monetization-functions-hooks-pre-session-output"></a>


| Namespace | Accepted types | How the output is used | 
| --- | --- | --- | 
| player\_params.\* | Strings, numbers, booleans | Persisted to the session as player parameters. See [Player parameters (player\_params.\*)](#monetization-functions-hooks-pre-session-output-player-params). | 
| manifest.\* | Strings | Persisted to the session as manifest query parameters and applied to manifest, segment, and origin request URLs for the lifetime of the session. See [Manifest query parameters (manifest.\*)](#monetization-functions-hooks-pre-session-output-manifest). | 
| aws.\* | Strings | Sets MediaTailor service variables that control session-level behavior, such as aws.startTime and aws.preroll. Only the parameters listed in [Service variables (aws.\*)](#monetization-functions-hooks-pre-session-output-aws) are accepted. | 

For the `player_params.*`, `manifest.*`, and `aws.*` namespaces, a value written by the function takes precedence over a player-supplied query parameter with the same name. Values the function does not set are unchanged.

### Player parameters (player\_params.\*)
<a name="monetization-functions-hooks-pre-session-output-player-params"></a>

Values written to `player_params.*` are persisted to the session. They are available:
+ As input at the `PRE_ADS_REQUEST` lifecycle hook via `player_params.*`
+ In ADS request URLs through [MediaTailor dynamic ad variables for ADS requests](variables.md) (for example, `[player_params.deviceType]`)
+ For the lifetime of the session across all ad breaks

**Note**  
The total serialized size of all `player_params` output keys and values must not exceed 1,000 characters. If the total exceeds this limit, the function output is discarded. For more information, see [Functions limits](monetization-functions-limits.md).

### Manifest query parameters (manifest.\*)
<a name="monetization-functions-hooks-pre-session-output-manifest"></a>

Writing `manifest.{{name}}` in the function output has the same effect as the player including `manifest.{{name}}={{value}}` as a query parameter on the session initialization request. MediaTailor removes the `manifest.` prefix and appends `{{name}}={{value}}` to the manifest and segment URLs it generates for the session. MediaTailor also appends it to the manifest requests it makes to your content origin. For the full list of URLs that receive manifest query parameters, see [MediaTailor manifest query parameters](manifest-query-parameters.md).

Use this namespace for a value that must reach your content origin or content delivery network (CDN). This is useful when the value is computed at session start rather than supplied by the player. For example, a function can read a player-supplied `player_params.zip` and write `manifest.aws.mediatailor.channel.audienceId` so that an MediaTailor channel assembly origin receives `?aws.mediatailor.channel.audienceId={{value}}` on every manifest request. For a complete example, see [Example 5: Origin audience routing](monetization-functions-examples-origin-routing.md).

The part of the key after `manifest.` must consist of one or more segments of letters, digits, and underscores separated by periods (for example, `manifest.token` or `manifest.aws.mediatailor.channel.audienceId`). Other characters are rejected when you create or update the function. Values are subject to the same character rules as player-supplied manifest query parameters; see [MediaTailor parameter character restrictions and URL-encoding](manifest-query-parameters-character-restrictions.md).

### Service variables (aws.\*)
<a name="monetization-functions-hooks-pre-session-output-aws"></a>

The function can set the same `aws.*` service variables that a player can supply as query parameters at session initialization. MediaTailor applies the function's value before it constructs the session, so the value affects the entire session exactly as the equivalent query parameter would. The following parameters are accepted:
+ `aws.startTime`, `aws.preroll`, `aws.overlayAvails`, `aws.logMode`, `aws.availSuppressionMode`, `aws.availSuppressionValue`, and `aws.availSuppressionFillPolicy`. For values and behavior, see [MediaTailor service variables for session control](variables-service.md).
+ `aws.insertionMode`, `aws.reportingMode`, and `aws.guidedPrefetchMode`. For values and behavior, see [MediaTailor server-guided ad insertion overview and implementation](server-guided.md) and [MediaTailor server-side ad tracking and reporting](ad-reporting-server-side.md).
+ `aws.adSignalingEnabled`. See [Ad ID decoration](ad-id-decoration.md).
+ `aws.streamId`. See [Prefetching ads](prefetching-ads.md).

Values are strings and must use the same format as the corresponding query parameter (for example, `"aws.preroll": "disabled"`). If a value cannot be parsed, MediaTailor ignores that parameter and keeps the session's existing value; the rest of the function output is still applied. Keys outside this list are rejected when you create or update the function.

## Typical use cases
<a name="monetization-functions-hooks-pre-session-use-cases"></a>
+ Fetch identity or audience data from an external service and store it in player parameters for use in later ADS requests.
+ Classify the device type based on the user agent and write the classification to a player parameter.
+ Set default player parameter values that downstream ad break processing relies on.
+ Store values in player parameters that are included in the ADS URL through [MediaTailor dynamic ad variables for ADS requests](variables.md).
+ Compute a manifest query parameter from player input, such as mapping a viewer's postal code to an audience identifier that your content origin or CDN reads on every manifest request.
+ Set session-level service variables, such as disabling pre-roll for returning viewers or choosing a start time, without requiring the player to send the corresponding `aws.*` query parameters.

## Failure behavior
<a name="monetization-functions-hooks-pre-session-failure"></a>

If a function attached to `PRE_SESSION_INITIALIZATION` fails for any reason, MediaTailor discards the function's output and proceeds as if no function were attached. The session starts normally without the function's player parameter, manifest query parameter, and service variable values. The session uses only what the player supplied at session initialization.