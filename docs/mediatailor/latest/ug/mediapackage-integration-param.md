# MediaTailor and MediaPackage time-shifted viewing

integration

AWS Elemental MediaTailor can pass time-shifted viewing parameters to MediaPackage origins to enable
startover and catch-up viewing functionality. This integration allows viewers to start
watching live content from earlier points in time.

###### MediaPackage time-shifted viewing parameters

MediaPackage supports the following time-shifted viewing parameters that can be passed
through MediaTailor:

- `start`: Epoch or ISO 8601 timestamp defining the beginning of the
  time-shifted manifest
- `end`: Epoch or ISO 8601 timestamp defining the end of the
  time-shifted manifest
- `time_delay`: Delay content availability by specified
  seconds
- `manifest_window_seconds`: Request a manifest shorter than the
  configured window

###### Example MediaTailor session initialization with MediaPackage time-shifted parameters

The following example shows how to initialize a session with time-shifted viewing
parameters:

```
GET /v1/master/123456789/originId/index.m3u8?start=2024-08-26T10:00:00Z&end=2024-08-26T11:00:00Z
```

Or using explicit session initialization:

```
POST /v1/session/123456789/originId/index.m3u8
{
    "adsParams": {
        "param1": "value1"
    }
}
```

With additional query parameters:

```
?start=2024-08-26T10:00:00Z&end=2024-08-26T11:00:00Z
```

###### Parameter behavior during sessions

Time-shifted viewing parameters have specific behavior characteristics:

- **Session initialization:** Parameters are
  processed when the session is created
- **Parameter persistence:** Parameters remain
  associated with the session throughout playback
- **Immutable after initialization:** Parameters
  cannot be changed during an active session
- **New session required:** To modify time-shift
  windows, create a new session with updated parameter values

###### MediaPackage startover window requirements

For time-shifted viewing to work with MediaPackage, ensure the following:

1. Configure a startover window on your MediaPackage endpoint (up to 24 hours)
2. Ensure your CDN forwards the necessary query parameters to MediaPackage
3. Use consistent playback windows across player sessions for better CDN
   caching
4. Verify that start and end times fall within the configured startover
   window

###### Important

When using time-shifted viewing, use consistent playback windows across player
sessions rather than generating unique start or end times for each viewer. This
yields better caching at the CDN and avoids potential throttling.

For complete information about MediaPackage time-shifted viewing configuration and
parameters, see [Time-shifted viewing with
AWS Elemental MediaPackage](../../../mediapackage/latest/ug/time-shifted.md "../../../mediapackage/latest/ug/time-shifted.md") in the _AWS Elemental MediaPackage User Guide_.
