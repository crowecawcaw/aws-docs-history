# MediaTailor CDN integration and

parameter routing

AWS Elemental MediaTailor manifest query parameters enable sophisticated CDN integration scenarios.
You can use them for dynamic routing, authorization, and load balancing.

###### CDN routing use cases

Common CDN integration scenarios that benefit from manifest query parameters
include the following:

- **Geographic routing:** Route requests to
  region-specific MediaTailor endpoints based on viewer location
- **Token-based authorization:** Pass authorization
  tokens through the CDN to MediaTailor for secure content access
- **Load balancing:** Distribute traffic across
  multiple MediaTailor endpoints using CDN routing logic
- **A/B testing:** Route different user segments to
  different MediaTailor configurations for testing
- **Device-specific optimization:** Route requests
  based on device type or capabilities

###### Parameter preservation across CDN layers

MediaTailor ensures that manifest query parameters are preserved across multiple CDN
layers and request types:

1. **Initial request:** Parameters are extracted
   from the session initialization request
2. **Manifest generation:** Parameters are applied
   to all relevant URLs in the manifest
3. **Segment requests:** Parameters are included in
   all segment URLs for consistent CDN behavior
4. **Ad insertion:** Parameters are preserved during
   ad insertion and segment replacement

###### Example CDN authorization flow

The following example demonstrates a complete CDN authorization flow using
manifest query parameters:

1. Client requests manifest with authorization token:

```
GET https://cdn.example.com/mediatailor/v1/master/123456789/originId/index.m3u8?manifest.auth_token=jwt_token_here&manifest.user_id=12345
```

2. CDN forwards request to MediaTailor with parameters:

```
GET https://mediatailor.amazonaws.com/v1/master/123456789/originId/index.m3u8?manifest.auth_token=jwt_token_here&manifest.user_id=12345
```

3. MediaTailor generates manifest with parameters applied to all URLs:

```
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=2665212
../../../manifest/123456789/originId/session/0.m3u8?auth_token=jwt_token_here&user_id=12345
```

4. Subsequent segment requests include parameters for CDN
   authorization:

```
GET https://cdn.example.com/mediatailor/segment/123456789/originId/session/0/1?auth_token=jwt_token_here&user_id=12345
```
