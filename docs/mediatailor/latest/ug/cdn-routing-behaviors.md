# Set up CDN routing behaviors for MediaTailor

This section explains how to set up your content delivery network (CDN) to route different
types of requests appropriately for AWS Elemental MediaTailor integration. Proper routing configuration
ensures that manifest requests, content segments, and ad segments are handled
correctly.

Configuring CDN routing behaviors is a critical step in creating an efficient content
delivery pipeline. By setting up specific routing rules for different content types, you can
optimize caching, improve delivery performance, and ensure personalized ad insertion works
correctly.

For advanced routing scenarios using dynamic variables and configuration aliases, see
[MediaTailor dynamic ad variables for ADS requests](variables.md "variables.md"). For information about preserving
query parameters across CDN routing, see [MediaTailor manifest query parameters](manifest-query-parameters.md "manifest-query-parameters.md").

###### Important

Failure to include CORS headers in either the cached object or on the CDN response to
viewers can cause playback failures.

## CDN routing behavior configuration

Set up your CDN to route different types of requests appropriately.

### Content segment routing

Content segment routing directs requests for your actual content segments to your
origin server. Like ad segment routing, content segment routing also requires proper
CORS configuration to ensure smooth playback in web-based players.

For detailed configuration guidance, see the CloudFront example at [Precedence 4: Content origin path
behavior](cf-comprehensive-configuration.md#cf-default-behavior "cf-comprehensive-configuration.md#cf-default-behavior"). This
example provides specific settings that you should follow for CloudFront or adapt
for other CDNs.

Key configuration requirements for content segment routing include:

- Use path patterns that match your content segment file extensions (like
  `*.ts`, `*.mp4`, or `*.m4s`)
- Route requests to your content origin (such as an Amazon S3 Bucket or MediaPackage
  endpoint)
- For optimal cache-hit ratio, include only query string parameters that
  cause your origin to modify the response in the cache key and forward the
  origin request
- Apply an appropriate cache policy with greater than 24-hour TTL
  values
- Include CORS response headers to your viewers

### Ad segment routing

Ad segment routing is critical for delivering personalized advertisements to
viewers. When configuring ad segment routing, you must implement proper CORS
(Cross-Origin Resource Sharing) handling to prevent issues that can cause playback
failures in web-based players.

For detailed configuration guidance, see the CloudFront example at [Precedence 0: Ad segments path
behavior](cf-comprehensive-configuration.md#cf-transcode-manage-behavior "cf-comprehensive-configuration.md#cf-transcode-manage-behavior"). This example provides specific
settings that you should follow for CloudFront or adapt for other CDNs.

Key configuration requirements for ad segment routing include:

- Use the path pattern `/tm/*` specifically for MediaTailor ad
  segments
- Route requests to
  `segments.mediatailor.``region``.amazonaws.com`
- For optimal cache-hit ratio, do not include any viewer request headers,
  cookies, or query string parameters in the cache key or in the origin
  request
- Apply an appropriate cache policy with greater than 24-hour TTL
  values
- Include CORS response headers to your viewers

### Manifest request routing

To route multivariant playlist, media playlist, and MPD requests to MediaTailor, use the
following general settings. For CloudFront configuration, see [Configuring manifest cache behavior](cloudfront-basic-setup.md#cf-manifest-behavior "cloudfront-basic-setup.md#cf-manifest-behavior").

1. In your CDN configuration interface, create behaviors for different
   manifest types.
2. Set path patterns to match multivariant playlist and media playlist file
   extensions (`*.m3u8` for HLS) and MPD file extensions
   (`*.mpd` for DASH).
3. Configure the origin setting in your CDN to point to your MediaTailor
   configuration endpoint.
4. For ad insertion, disable caching of personalized multivariant playlists,
   media playlists, and MPDs. Because ad insertion provides personalized
   manifests, your CDN shouldn't cache them. If a different playback device
   than the one intended receives a cached playlist or MPD, it could result in
   issues with playback or tracking. For comprehensive caching guidance
   including TTL recommendations for all content types, see [Caching optimization for CDN and MediaTailor
   integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").
5. Configure header forwarding for all headers. For minimum requirements, see
   [Required headers for MediaTailor CDN
   integration](cdn-configuration.md#cdn-required-headers "cdn-configuration.md#cdn-required-headers").
6. Enable query string forwarding to pass ad targeting parameters.

HLS multivariant playlist
HLS multivariant playlist requests follow these formats:

```
https://<`playback-endpoint`>/v1/index/<`hashed-account-id`>/<`origin-id`>/<`index`>.m3u8
```

Example:

```
https://777788889999.mediatailor.us-east-1.amazonaws.com/v1/master/a1bc06b59e9a570b3b6b886a763d15814a86f0bb/Demo/assetId.m3u8
```

HLS media playlist
HLS media playlist requests follow these formats:

```
https://<`playback-endpoint`>/v1/manifest/<`hashed-account-id`>/<`session-id`>/<`manifestNumber`>.m3u8
```

Player requests to
`https://CDN_Hostname/some/path/asset.m3u8` are
routed to the MediaTailor path
`https://mediatailor.us-west-2.amazonaws.com/v1/session/configuration/endpoint`
based on the keyword `*.m3u8` in the request.

Example:

```
https://777788889999.mediatailor.us-east-1.amazonaws.com/v1/manifest/a1bc06b59e9a570b3b6b886a763d15814a86f0bb/c240ea66-9b07-4770-8ef9-7d16d916b407/0.m3u8
```

DASH MPD
DASH MPD requests follow these formats:

```
https://<`playback-endpoint`>/v1/dash/<`hashed-account-id`>/<`origin-id`>/<`assetName`>.mpd
```

Player requests to
`https://CDN_Hostname/some/path/asset.mpd` are
routed to the MediaTailor path
`https://mediatailor.us-west-2.amazonaws.com/v1/dash/configuration/endpoint`
based on the keyword `*.mpd` in the request.

Example:

```
https://777788889999.mediatailor.us-east-1.amazonaws.com/v1/dash/a1bc06b59e9a570b3b6b886a763d15814a86f0bb/Demo/0.mpd
```

## CDN routing best practices

When configuring CDN routing behaviors, follow these best practices to ensure optimal
performance and reliability:

**Use specific path patterns**

Create specific path patterns that accurately match your content structure
to ensure proper routing.

**Prioritize behavior order**

In most CDNs, behaviors are evaluated in order. Place more specific
behaviors before more general ones.

**Test behavior patterns**

Verify that your path patterns correctly match the expected requests
before deploying to production.

**Document your configuration**

Maintain documentation of your CDN routing behaviors to facilitate
troubleshooting and future updates.

## Next steps

After configuring your CDN routing behaviors, the next step is to configure CDN
mapping in MediaTailor. See [Set up CDN mapping in MediaTailor](cdn-mapping-mediatailor.md "cdn-mapping-mediatailor.md") for instructions.
