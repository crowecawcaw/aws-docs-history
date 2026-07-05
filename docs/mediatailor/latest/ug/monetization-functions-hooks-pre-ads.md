# PRE\_ADS\_REQUEST

## When it fires

MediaTailor runs the function mapped to `PRE_ADS_REQUEST` once per ad break,
immediately before sending the request to the ADS. The function runs each time an ad
opportunity is encountered during manifest processing.

## Input

All fields from `PRE_SESSION_INITIALIZATION`, plus
`avail.*`, `scte.*`, `asset.*`, and `adsRequest.*` (url,
method, headers, body). For all available fields, see [Input field reference](monetization-functions-hooks.md#monetization-functions-hooks-input-ref "monetization-functions-hooks.md#monetization-functions-hooks-input-ref").

## Output namespace allowed

| Namespace         | Accepted types             | How the output is used                                                                                                                                                                                                                                                                                       |
| ----------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `player_params.*` | Strings, numbers, booleans | Overrides session player parameters for this ad break. Available<br>to the ADS request URL through [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md").                                                                                                                         |
| `session.*`       | Strings, numbers, booleans | Overrides session variables for this ad break. Available to the<br>ADS request URL through dynamic variable substitution.                                                                                                                                                                                    |
| `avail.*`         | Strings, numbers, booleans | Overrides avail variables for this ad break. Available to the ADS<br>request URL through dynamic variable substitution.                                                                                                                                                                                      |
| `scte.*`          | Strings, numbers, booleans | Overrides SCTE variables for this ad break. Available to the ADS<br>request URL through dynamic variable substitution.                                                                                                                                                                                       |
| `asset.*`         | Strings, numbers, booleans | Overrides asset metadata variables (from `EXT-X-ASSET`<br>tags) for this ad break. Available to the ADS request URL through<br>dynamic variable substitution. For more information about HLS ad<br>markers, see [HLS ad markers](hls-ad-markers.md "hls-ad-markers.md").                                     |
| `adsRequest.*`    | String                     | Overrides the ADS request for this ad break only. Supported<br>fields: `url`, `method`,<br>`headers.<name>`, `body`. The<br>`url` value is treated as a template and supports<br>[MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md") after the<br>function runs. Not persisted. |

###### Note

All output from the `PRE_ADS_REQUEST` hook are transient overrides
— they apply only to the current ad break's ADS request and are not
persisted to the session.

**Example — rewriting the ADS request:**

```
{
    "Output": {
        "adsRequest.url": "{%'https://ads.example.com/v1/vast?sid=' & session.id & '&genre=' & player_params.genre%}",
        "adsRequest.headers.X-Custom-Token": "{%player_params.auth_token%}"
    }
}
```

This replaces the ADS URL and adds a custom header for the current ad
break.

## Typical use cases

- Rewrite the ADS request URL to route traffic between different ad servers
  for A/B testing.
- Append enrichment data (audience segments, identity tokens) to the ADS
  request URL or headers.
- Conditionally modify ADS request parameters based on SCTE-35 signal data
  or avail index.

## Failure behavior

If a function attached to `PRE_ADS_REQUEST` fails for any reason,
MediaTailor discards the function's output and proceeds as if no function were attached.
The ADS request is sent using the original session and request parameters without
modification.
