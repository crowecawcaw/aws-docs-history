# MediaTailor service variables for session control

AWS Elemental MediaTailor reserves the `aws.` query parameter namespace for service
variables that control session-level behavior. Unlike `ads.` parameters
(which are forwarded to the ADS) and `manifest.` parameters (which are
appended to the personalized manifest URLs), `aws.` parameters are consumed
directly by MediaTailor and are not forwarded to the origin server or the ADS.

## Supported parameters

The following table lists the `aws.*` parameters you can use to
control session-level behavior.

| Parameter                        | Type               | Values                                                             | Default                  | Description                                                                                                                                                                                    |
| -------------------------------- | ------------------ | ------------------------------------------------------------------ | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aws.startTime`                  | ISO 8601 timestamp | For example, `2026-06-17T10:00:00Z`                                | Not set (live-edge join) | Starts the session at a specific point in the DVR window.<br>MediaTailor resolves the timestamp to the nearest segment boundary and<br>emits `EXT-X-START:TIME-OFFSET` in the HLS<br>manifest. |
| `aws.preroll`                    | String enum        | `enabled`, `disabled`<br>(case-insensitive)                        | `enabled`                | Controls whether pre-roll ad insertion occurs for the session.<br>When `disabled`, pre-roll is suppressed even if the<br>playback configuration has a<br>`LivePreRollConfiguration`.           |
| `aws.overlayAvails`              | String enum        | `on`, `off` (case-insensitive)                                     | `on`                     | Controls whether overlay (non-linear) ad avails are processed<br>for the session. When `off`, overlay ad markers in<br>the source manifest are ignored and no overlay ads are<br>inserted.     |
| `aws.logMode`                    | String enum        | `DEBUG`, `DISABLED`                                                | `DISABLED`               | Enables verbose debug logging for the session. When set to<br>`DEBUG`, MediaTailor emits detailed session logs to<br>CloudWatch Logs for troubleshooting.                                      |
| `aws.availSuppressionMode`       | String enum        | `OFF`, `BEHIND_LIVE_EDGE`,<br>`AFTER_LIVE_EDGE` (case-insensitive) | `OFF`                    | Controls whether ad avails are suppressed based on their<br>position relative to the live edge.                                                                                                |
| `aws.availSuppressionValue`      | Time duration      | HH:MM:SS format (for example,<br>`00:00:10`)                       | Not set                  | The time window for avail suppression. Required when<br>`availSuppressionMode` is<br>`BEHIND_LIVE_EDGE` or<br>`AFTER_LIVE_EDGE`.                                                               |
| `aws.availSuppressionFillPolicy` | String enum        | `FULL_AVAIL_ONLY`, `PARTIAL_AVAIL`<br>(case-insensitive)           | `FULL_AVAIL_ONLY`        | When mode is `AFTER_LIVE_EDGE`, controls whether<br>partially-suppressed avails are filled.                                                                                                    |

## aws.startTime

When `aws.startTime` is set, MediaTailor starts the session at the
segment boundary nearest the specified program date-time.

###### Usage

Pass `aws.startTime` as a query parameter in the manifest
request:

```
GET /v1/master/{hashed-account-id}/{origin-id}/{asset}.m3u8?aws.startTime=2026-06-17T10:00:00Z
```

Or in explicit session initialization, pass it as a top-level field without
the `aws.` prefix:

```
POST /v1/session/{hashed-account-id}/{origin-id}/{asset}.m3u8

{
    "startTime": "2026-06-17T10:00:00Z"
}
```

###### Requirements

The following requirements apply to `aws.startTime`:

- The source manifest must contain
  `EXT-X-PROGRAM-DATE-TIME` (PDT) on segments. Without
  PDT, `aws.startTime` cannot resolve and is ignored.
- Applies to HLS live sessions only (both SSAI and SGAI).

###### Behavior

The following table describes how `aws.startTime` behaves in
different scenarios:

| Scenario                                       | Result                                                   |
| ---------------------------------------------- | -------------------------------------------------------- |
| Timestamp within DVR window                    | Start at nearest segment boundary, emit<br>`EXT-X-START` |
| Timestamp older than DVR window                | Clamp to 3×targetDuration from window head               |
| Timestamp within 3×targetDuration of live edge | Treat as live-edge join (no<br>`EXT-X-START`)            |
| Timestamp at or after live edge                | Normal live-edge join                                    |
| Malformed or not ISO 8601                      | Ignored – fall back to live-edge join, error<br>logged   |
| Manifest has no PDT                            | Ignored – fall back to live-edge join, error<br>logged   |
| Parameter omitted                              | Default: normal live-edge join                           |

###### Clamping behavior

If the start point ages out of the DVR window mid-session,
`EXT-X-START` is clamped to 3×targetDuration from the
window head. The 3×targetDuration buffer aligns with RFC 8216
§6.3.3 player buffering recommendations.

###### Example Manifest output with aws.startTime

When a player initializes a session with
`aws.startTime=2026-06-17T10:00:00Z` and the resolved offset
is 120 seconds from the live edge, MediaTailor emits:

```
#EXTM3U
#EXT-X-TARGETDURATION:6
#EXT-X-START:TIME-OFFSET=-120.120,PRECISE=YES
#EXT-X-MEDIA-SEQUENCE:500
#EXT-X-PROGRAM-DATE-TIME:2026-06-17T09:58:00.000Z
#EXTINF:6.006,
segment500.ts
#EXTINF:6.006,
segment501.ts
...
```

The `TIME-OFFSET=-120.120` tells the player to begin playback
120 seconds behind the live edge, at the segment boundary nearest the
requested start time.

###### Limitations

The following limitations apply:

- You cannot change this parameter after session
  initialization.
- Requires `EXT-X-PROGRAM-DATE-TIME` in the source
  manifest.
- `EXT-X-START` is a player hint – MediaTailor cannot
  guarantee all players honor it.

## aws.preroll

When `aws.preroll=disabled`, MediaTailor suppresses pre-roll ad
insertion for the session even if the playback configuration has a
`LivePreRollConfiguration`.

###### Usage

Pass `aws.preroll` as a query parameter in the manifest
request:

```
GET /v1/master/{hashed-account-id}/{origin-id}/{asset}.m3u8?aws.preroll=disabled
```

Or in explicit session initialization, pass it as a top-level field without
the `aws.` prefix:

```
POST /v1/session/{hashed-account-id}/{origin-id}/{asset}.m3u8

{
    "preroll": "disabled"
}
```

###### Requirements

The following requirements apply to `aws.preroll`:

- The playback configuration must have a
  `LivePreRollConfiguration` for this parameter to have
  any effect. If no pre-roll is configured, setting this parameter has
  no effect.
- Applies to HLS live sessions (both SSAI and SGAI).

###### Behavior

The following table describes how `aws.preroll` behaves:

| Value                  | Result                                |
| ---------------------- | ------------------------------------- |
| `enabled` (or omitted) | Pre-roll inserted as usual            |
| `disabled`             | Pre-roll suppressed for this session  |
| Invalid value          | Logged as error, treated as `enabled` |

###### Limitations

You cannot change this parameter after session initialization.

## aws.overlayAvails

When `aws.overlayAvails=off`, MediaTailor ignores overlay (non-linear)
ad markers in the source manifest and does not insert overlay ads for the
session.

###### Usage

Pass `aws.overlayAvails` as a query parameter in the manifest
request:

```
GET /v1/master/{hashed-account-id}/{origin-id}/{asset}.m3u8?aws.overlayAvails=off
```

###### Requirements

The following requirements apply to
`aws.overlayAvails`:

- The source manifest must contain overlay ad markers (for example,
  SCTE-35 events with overlay segmentation type) for this parameter to
  have any effect.
- Applies to HLS and DASH, live and VOD sessions (both SSAI and
  SGAI).

###### Behavior

The following table describes how `aws.overlayAvails`
behaves:

| Value             | Result                                                       |
| ----------------- | ------------------------------------------------------------ |
| `on` (or omitted) | Overlay avails are processed and ads inserted as<br>usual    |
| `off`             | Overlay ad markers are ignored, no overlay ads<br>inserted   |
| Invalid value     | Logged as error, treated as not specified (default:<br>`on`) |

###### Limitations

You cannot change this parameter after session initialization.

## aws.logMode

When `aws.logMode=DEBUG`, MediaTailor enables verbose debug logging for
the session. Debug logs are emitted to CloudWatch Logs and provide detailed
information about manifest personalization, ad decision server requests, and
session state – useful for troubleshooting ad insertion issues.

###### Usage

Pass `aws.logMode` as a query parameter in the manifest
request:

```
GET /v1/master/{hashed-account-id}/{origin-id}/{asset}.m3u8?aws.logMode=DEBUG
```

###### Requirements

The following requirements apply to `aws.logMode`:

- The playback configuration must have logging enabled
  (`PercentEnabled > 0` or
  `EnabledLoggingStrategies` configured) for debug logs to
  be emitted.
- Debug logging is rate-limited per customer to prevent excessive log
  volume.

###### Behavior

The following table describes how `aws.logMode`
behaves:

| Value                   | Result                                                                |
| ----------------------- | --------------------------------------------------------------------- |
| `DEBUG`                 | Verbose debug logs emitted for the session                            |
| `DISABLED` (or omitted) | Normal logging behavior (based on playback configuration<br>settings) |
| Invalid value           | Error thrown, session initialization fails                            |

###### Limitations

The following limitations apply:

- You cannot change this parameter after session
  initialization.
- Values are case-sensitive (`DEBUG`, not
  `debug`).

## aws.availSuppressionMode

Controls whether ad avails are suppressed based on their position relative to
the live edge. Use this to skip ad breaks that fall within a time window behind
or after the live edge – for example, to avoid filling ad breaks that
viewers have already passed when joining a live stream mid-event.

###### Usage

Pass avail suppression parameters as query parameters in the manifest
request:

```
GET /v1/master/{hashed-account-id}/{origin-id}/{asset}.m3u8?aws.availSuppressionMode=BEHIND_LIVE_EDGE&aws.availSuppressionValue=00:00:10
```

This parameter works with two companion parameters:

- `aws.availSuppressionValue` – The time window
  (required when mode is not `OFF`)
- `aws.availSuppressionFillPolicy` – Controls partial
  fill behavior (only applies to `AFTER_LIVE_EDGE`
  mode)

###### Requirements

The following requirements apply to avail suppression parameters:

- Applies to HLS and DASH live sessions.
- `aws.availSuppressionValue` must be provided in
  `HH:MM:SS` format when mode is
  `BEHIND_LIVE_EDGE` or
  `AFTER_LIVE_EDGE`.
- `aws.availSuppressionFillPolicy` is only valid when mode
  is `AFTER_LIVE_EDGE`.

###### Mode behavior

The following table describes the effect of each suppression mode:

| Mode               | Effect                                                                                 |
| ------------------ | -------------------------------------------------------------------------------------- |
| `OFF` (or omitted) | No avail suppression – all ad breaks are filled<br>normally                            |
| `BEHIND_LIVE_EDGE` | Suppress ad breaks that start within the specified time<br>window behind the live edge |
| `AFTER_LIVE_EDGE`  | Suppress ad breaks that start after the specified time<br>window from the live edge    |

###### Fill policy (AFTER\_LIVE\_EDGE only)

The following table describes the fill policy behavior when mode is
`AFTER_LIVE_EDGE`:

| Fill policy                 | Effect                                                                     |
| --------------------------- | -------------------------------------------------------------------------- |
| `FULL_AVAIL_ONLY` (default) | Only fill avails that are completely outside the suppression<br>window     |
| `PARTIAL_AVAIL`             | Fill the portion of an avail that extends beyond the<br>suppression window |

###### Example Avail suppression example

The following request suppresses ad breaks within 10 seconds behind the
live edge:

```
GET /v1/master/{hashed-account-id}/{origin-id}/{asset}.m3u8?aws.availSuppressionMode=BEHIND_LIVE_EDGE&aws.availSuppressionValue=00:00:10
```

###### Limitations

The following limitations apply:

- You cannot change this parameter after session
  initialization.
- `aws.availSuppressionValue` must not be provided when mode
  is `OFF`.
- Invalid time format in `aws.availSuppressionValue` causes
  mode to fall back to `OFF`.
