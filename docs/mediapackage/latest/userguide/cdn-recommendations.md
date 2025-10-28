# CDN configuration recommendations

To configure your CDN distributions for delivering Apple HLS and low-latency HLS (LL-HLS) streams with MediaPackage,
we suggest using the following approach. Ensure that all your usual default parameters in
the CDN distribution configuration are compatible with the delivery of HLS and LL-HLS streams with MediaPackage.

## Honor MediaPackage 'cache-control: max-age' values

MediaPackage defines time-to-live (TTL) values for objects either statically or dynamically, depending on
the object type. The specific TTLs are listed below, and it's strongly recommended that you honor these
values and avoid overriding them at the CDN configuration level.

- Multivariant playlist (for both regular HLS and LL-HLS) - half the duration of the media segments
- Media playlists (regular HLS) - half the duration of the media segments
- Media playlists (LL-HLS) - 1 second
- TS media segments and init segments - 1209600 seconds (14 days)
- CMAF media segments and initialization segments - 1209600 seconds (14 days)

## Include specific query strings in your CDN cache

key

We recommend that you include the following query strings in the CDN cache key.

- `aws.manifestfilter`: used to customize the manifest contents,
  as described in [Manifest filtering](manifest-filtering.md "manifest-filtering.md").
- `aws.manifestsettings`: used to apply time-shifted settings to
  the manifest contents, as described in [Time-shifted viewing](time-shifted.md "time-shifted.md").
- `_HLS_msn` and `_HLS_part`: used to support LL-HLS
  playback request logic, as described in the _HTTP
  Live Streaming Documentation_ [Enabling Low-Latency HTTP Live
  Streaming (HLS)](https://developer.apple.com/documentation/http-live-streaming/enabling-low-latency-http-live-streaming-hls "https://developer.apple.com/documentation/http-live-streaming/enabling-low-latency-http-live-streaming-hls").

MediaPackage ignores all other query strings. Don't include them in the CDN forward
requests.

## Response timeout

LL-HLS uses the Blocking Requests mechanism for both playlists and media parts, which is
signaled through the `EXT-X-PRELOAD-HINT` tag. This mechanism puts the origin response on hold
until the object is fully available. Consequently, the CDN should also wait for the origin response,
and therefore, the response timeout value in your CDN distribution should be at least three times your parts duration.

## Forwarded HTTP headers

You may consider including the Origin header in your CDN forward requests to MediaPackage as the
only potentially necessary HTTP request header. In doing so, MediaPackage will respond with an
`access-control-allow-origin` header, using the value passed as the Origin header value. If the
Origin header is not included in the forward requests, MediaPackage will respond with an
`access-control-allow-origin: *` header. Choose the approach that best fits your CORS requirements.

## Forwarded cookies

MediaPackage doesn't consider any cookies that may be sent together with forward requests.
Therefore, it's advisable to exclude cookies from CDN forward requests.
