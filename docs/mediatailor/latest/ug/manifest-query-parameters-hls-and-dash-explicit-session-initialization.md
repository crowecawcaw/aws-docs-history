# MediaTailor HLS and DASH explicit session initialization

AWS Elemental MediaTailor includes the `manifestParams` as query parameters in the
multivariant playlist and tracking URLs in the response when the client makes an
explicit session initialization request.

###### Session initialization methods

For explicit session initialization, you can use either POST with request body or
GET with query parameters:

1. **POST with Request Body:**

```
POST /v1/session/`111122223333`/`originId`/index.m3u8
{
    "adsParams": {"param1": "value1", "param2": "value2", "param3": "value3"},
    "manifestParams": {"test": "123"}
}
```

2. **GET with Query Parameters:**

```
GET /v1/session/`111122223333`/`originId`/index.m3u8?ads.param1=value1&ads.param2=value2&manifestParams.test=123
```

###### Example session initialization request

```
POST /v1/session/``111122223333``/`originId`/index.m3u8
{
    "adsParams": {
        "param1": "value1",
        "param2": "value2",
        "param3": "value3"
    },
    "manifestParams": {
        "test": "123"
    },
    "reportingMode": "client"
}
```

###### Example manifest and tracking response

```
{
    "manifestUrl": "/v1/master/``111122223333``/`originId`/index.m3u8?aws.sessionId=`session`&test=123",
    "trackingUrl": "/v1/tracking/``111122223333``/`originId`/`session`?test=123"
}
```

Manifest responses for the session have the specific `manifestParams` in
MediaTailor URLs similar to the previously described implicit session-initialization
workflows. The key difference is that manifest parameters for explicit session
initialization don't start with `manifest.`.

Manifest query parameters are immutable and you can only set them on session
initialization. If a client makes multiple multivariant playlist requests for a single
session, MediaTailor doesn't update the manifest query parameters after the first
request.

###### Parameter processing flow

You can only specify parameters once, at initialization time. Configuration
aliases resolve to actual values before forwarding. For example:
`player_params.ad_type=customized` resolves to
`ad_type=abc12345` based on the ConfigurationAliases
configuration.
