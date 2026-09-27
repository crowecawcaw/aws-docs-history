

# Example 5: Origin audience routing
<a name="monetization-functions-examples-origin-routing"></a>

## Scenario
<a name="monetization-functions-examples-origin-routing-scenario"></a>

A broadcaster serves a linear channel from a channel assembly origin that uses program rules to deliver alternate content to different audiences. Viewers in certain postal codes must receive a regional blackout feed. The player sends the viewer's postal code as a `zip` query parameter. The broadcaster wants MediaTailor to translate it into the origin's `aws.mediatailor.channel.audienceId` query parameter on every manifest request, without exposing the audience logic to the player.

## Configuration
<a name="monetization-functions-examples-origin-routing-config"></a>

**Map postal code to audience (CUSTOM\_OUTPUT):**

```
{
    "FunctionId": "zipAudienceRouting",
    "FunctionType": "CUSTOM_OUTPUT",
    "CustomOutputConfiguration": {
        "Runtime": "JSONATA",
        "Output": {
            "manifest.aws.mediatailor.channel.audienceId": "{% player_params.zip in ['02101', '02102', '02108', '02110'] ? 'blackout' : 'allowed' %}"
        }
    }
}
```

The output key uses the `manifest.` namespace, so MediaTailor removes the prefix and appends the remainder, `aws.mediatailor.channel.audienceId`, as a query parameter on requests to the origin. The audience identifiers `blackout` and `allowed` must match the audiences defined in the channel's program rules. For more information, see [Defining audience cohorts and alternate content with Program Rules](working-with-program-rules.md).

## Function mapping
<a name="monetization-functions-examples-origin-routing-mapping"></a>

```
{
    "FunctionMapping": {
        "PRE_SESSION_INITIALIZATION": "zipAudienceRouting"
    }
}
```

## What happens when the function runs
<a name="monetization-functions-examples-origin-routing-runtime"></a>

1. A viewer starts a playback session with `?zip=02101` on the session initialization request.

1. MediaTailor runs the `PRE_SESSION_INITIALIZATION` lifecycle hook and runs `zipAudienceRouting`. The function reads `player_params.zip`, finds it in the blackout list, and writes `blackout` to `manifest.aws.mediatailor.channel.audienceId`.

1. MediaTailor stores the value as a manifest query parameter on the session. Every request that MediaTailor makes to the origin for this session includes `?aws.mediatailor.channel.audienceId=blackout`, and the origin returns the blackout feed.

1. A viewer whose postal code is not in the list receives `audienceId=allowed` and the regular feed. A viewer who sends no `zip` parameter also receives `allowed`, because `player_params.zip` is undefined and the `in` test evaluates to false.

**Tip**  
If the player also sends `manifest.aws.mediatailor.channel.audienceId` as a query parameter, the function's value takes precedence, so viewers cannot select their own audience by editing the URL.

For more information, see [Custom output](monetization-functions-types-custom-output.md), [Pre-session initialization](monetization-functions-hooks-pre-session.md), and [MediaTailor manifest query parameters](manifest-query-parameters.md).