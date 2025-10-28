# MediaTailor parameter routing for ADS and

origins

AWS Elemental MediaTailor routes query parameters to different destinations based on their prefix and
purpose. Understanding parameter routing is essential for implementing origin-specific
functionality like time-shifted viewing with MediaPackage.

###### Parameter routing rules

MediaTailor uses the following routing rules for query parameters:

- **Origin parameters (no prefix):** Parameters
  without a specific prefix are passed through to the origin server for
  origin-specific functionality
- **ADS parameters (`ads.` prefix):**
  Parameters prefixed with `ads.` are sent to the Ad Decision
  Server
- **Manifest parameters (`manifest.`
  prefix):** Parameters prefixed with `manifest.` are used
  for CDN routing and authorization

###### Example Parameter routing example

The following session initialization demonstrates parameter routing:

```
POST /v1/session/123456789/originId/index.m3u8
{
    "adsParams": {
        "param1": "value1",
        "param2": "value2"
    },
    "manifestParams": {
        "auth_token": "abc123"
    }
}
```

In this example:

- `param1` and `param2` are sent to the ADS
- `auth_token` is used for CDN routing and authorization
- Parameters without prefixes would be passed to the origin server

## Origin server parameter behavior

Parameters passed to origin servers enable origin-specific functionality such as
time-shifted viewing, content filtering, and authentication.

###### Common origin parameter use cases

Origin parameters are commonly used for:

- **Time-shifted viewing:**
  `start` and `end` parameters for MediaPackage time-shifted
  content
- **Content authentication:** Authentication
  tokens required by the origin server
- **Content filtering:** Parameters that
  control which content variants are returned
- **Origin-specific features:** Any parameters
  that the origin server uses for content processing

###### Important

Parameters are processed at session initialization and maintained throughout
the session. To modify parameters like time-shift windows, you must create a new
session with updated values.
