# MediaTailor protocol-specific

parameter behavior

AWS Elemental MediaTailor handles manifest query parameters differently for HLS and DASH protocols.
Each protocol type has specific application locations and processing methods.

###### HLS vs DASH parameter handling comparison

The following table compares how MediaTailor handles manifest query parameters across
HLS and DASH protocols:

| Aspect                | HLS Behavior                                       | DASH Behavior                                                                 |
| --------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------- |
| Parameter application | Applied directly to manifest URLs and segment URLs | Applied to Location elements, SegmentTemplate attributes, and segment<br>URLs |
| Manifest hierarchy    | Multivariant playlist → Media playlists→ Segments  | MPD → Periods → AdaptationSets → Representations                              |
| Initialization URLs   | Applied to HLS init URLs when present              | Applied to SegmentTemplate initialization attributes                          |
| Session handling      | Parameters preserved across playlist updates       | Parameters included in MPD Location element for session<br>continuity         |
| Ad segment handling   | Applied to ad segment URLs in media playlists      | Applied to ad period SegmentTemplate media attributes                         |

###### Parameter application locations

MediaTailor applies manifest query parameters to the following locations:

## HLS parameter application

For HLS streams, MediaTailor applies manifest query parameters to:

- **Multivariant playlist URLs:** Parameters
  are appended to media playlist references
- **Media playlist URLs:** Parameters are
  included in segment URLs within media playlists
- **Content segment URLs:** All content
  segments include the manifest query parameters
- **Ad segment URLs:** Ad segments receive
  parameters for CDN routing and authorization
- **HLS initialization URLs:** Init segments
  include parameters when present in the stream
- **Slate segment URLs:** Slate content
  includes parameters for consistent CDN behavior

###### Example HLS parameter application example

Given the session initialization:

```
GET /v1/master/123456789/originId/index.m3u8?manifest.auth_token=abc123&manifest.region=us-west
```

The multivariant playlist includes parameters in media playlist
references:

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=2665212,RESOLUTION=960x540
../../../manifest/123456789/originId/session/0.m3u8?auth_token=abc123&region=us-west
```

The media playlist includes parameters in segment URLs:

```
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-TARGETDURATION:7
#EXTINF:6.006,
https://origin.com/segment1.ts?auth_token=abc123&region=us-west
#EXTINF:6.006,
../../../../segment/123456789/originId/session/0/2?auth_token=abc123&region=us-west
```

## DASH parameter application

For DASH streams, MediaTailor applies manifest query parameters to:

- **MPD Location elements:** The Location
  element includes parameters for manifest refresh requests
- **SegmentTemplate initialization
  attributes:** Init segment URLs include parameters
- **SegmentTemplate media attributes:** Media
  segment URL templates include parameters
- **Content segment URLs:** All content
  segments generated from templates include parameters
- **Ad segment URLs:** Ad period segments
  include parameters for CDN integration
- **Server-side reporting redirects:** 302
  redirects to ad segments preserve parameters

###### Example DASH parameter application example

Given the session initialization:

```
GET /v1/dash/123456789/originId/index.mpd?manifest.auth_token=abc123&manifest.region=us-west
```

The DASH manifest includes parameters in multiple locations:

```
<MPD>
    <Location>https://mediatailor.com/v1/dash/123456789/originId/index.mpd?auth_token=abc123&region=us-west&aws.sessionId=session</Location>
    <Period>
        <AdaptationSet>
            <Representation>
                <SegmentTemplate
                    initialization="init.mp4?auth_token=abc123&region=us-west"
                    media="segment_$Number$.mp4?auth_token=abc123&region=us-west"/>
            </Representation>
        </AdaptationSet>
    </Period>
</MPD>
```
