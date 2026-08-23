# Pre-session initialization

## When it fires

MediaTailor runs the function mapped to `PRE_SESSION_INITIALIZATION` once,
at the start of a new playback session. The function runs before MediaTailor constructs
the initial manifest response.

## Input

`session.*`, `player_params.*`, and
`event.*`. For all available fields, see [Input field reference](monetization-functions-hooks.md#monetization-functions-hooks-input-ref "monetization-functions-hooks.md#monetization-functions-hooks-input-ref").

## Output namespace allowed

| Namespace         | Accepted types             |
| ----------------- | -------------------------- |
| `player_params.*` | Strings, numbers, booleans |

Values written to `player_params.*` are persisted to the session. They
are available:

- As input at the `PRE_ADS_REQUEST` lifecycle hook via
  `player_params.*`
- In ADS request URLs through [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md") (for example,
  `[player_params.deviceType]`)
- For the lifetime of the session across all ad breaks

###### Note

The total serialized size of all
`player_params` output keys and values must not exceed 1,000 characters.
If the total exceeds this limit, the function output is discarded. For more
information, see [Functions limits](monetization-functions-limits.md "monetization-functions-limits.md").

## Typical use cases

- Fetch identity or audience data from an external service and store it in
  player parameters for use in later ADS requests.
- Classify the device type based on the user agent and write the
  classification to a player parameter.
- Set default player parameter values that downstream ad break processing
  relies on.
- Store values in player parameters that are included in the ADS URL through
  [MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md").

## Failure behavior

If a function attached to `PRE_SESSION_INITIALIZATION` fails for any
reason, MediaTailor discards the function's output and proceeds as if no function were
attached. The session starts normally without the function's player parameter
values.
