# MediaTailor parameter session behavior and

persistence

AWS Elemental MediaTailor processes parameters at session initialization and maintains them throughout
the session lifecycle. Understanding session behavior is crucial for implementing
dynamic parameter scenarios.

###### Session initialization methods

MediaTailor supports multiple methods for session initialization with parameters:

1. **Implicit session initialization:** Parameters
   included in the initial manifest request

```
GET /v1/master/123456789/originId/index.m3u8?manifest.auth_token=abc123&start=2024-08-26T10:00:00Z
```

2. **Explicit session initialization (POST):**
   Parameters provided in the request body

```
POST /v1/session/123456789/originId/index.m3u8
{
    "adsParams": {"param1": "value1"},
    "manifestParams": {"auth_token": "abc123"}
}
```

3. **Explicit session initialization (GET):**
   Parameters provided as query parameters

```
GET /v1/session/123456789/originId/index.m3u8?ads.param1=value1&manifestParams.auth_token=abc123
```

###### Parameter persistence and immutability

MediaTailor parameter behavior follows these rules:

- **One-time specification:** Parameters can only
  be specified once, at session initialization
- **Session-wide persistence:** Parameters are
  maintained throughout the entire session
- **Immutable after initialization:** Parameters
  cannot be modified after the session is created
- **Configuration alias resolution:** Aliases are
  resolved to actual values before forwarding to destinations

###### Parameter modification scenarios

To modify parameters during playback:

- **Create new session:** Initialize a new session
  with updated parameter values
- **Player transition:** Seamlessly transition the
  player to the new session
- **Parameter inheritance:** Carry forward
  unchanged parameters to maintain consistency

###### Example Modifying time-shift parameters

To change from a 1-hour window to a 2-hour window:

1. Current session:
   `start=2024-08-26T10:00:00Z&end=2024-08-26T11:00:00Z`
2. Create new session:
   `start=2024-08-26T10:00:00Z&end=2024-08-26T12:00:00Z`
3. Transition player to new session URL

###### Important

Multiple multivariant playlist requests for a single session do not update
parameters after the first request. Parameters remain immutable for the session
duration.
