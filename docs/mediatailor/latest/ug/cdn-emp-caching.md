# Optimize CDN caching for MediaTailor and MediaPackage content

delivery

AWS Elemental MediaTailor requires proper content delivery network (CDN) caching configuration for optimal
performance when using AWS Elemental MediaPackage as your content origin. MediaPackage provides
specific cache-control headers that tell your content delivery network how long to cache different types of
content. Following these recommendations ensures smooth playback and efficient content
delivery.

This topic focuses specifically on optimizing caching behavior to maximize performance and
minimize costs. Before implementing advanced caching optimization, ensure you have completed
the basic content delivery network integration setup. If you haven't set up your basic integration yet, start
with [Integrate MediaTailor with MediaPackage and CDN](mediapackage-integration.md "mediapackage-integration.md") .

## MediaPackage cache-control headers

MediaPackage sets specific TTL values for different content types to optimize caching behavior:

**Multivariant playlists (HLS and LL-HLS)**

TTL: Half the duration of the media segments

Reason: These playlists change as new segments become available, so they need frequent updates

**Media playlists (regular HLS)**

TTL: Half the duration of the media segments

Reason: Similar to multivariant playlists, these update as content progresses

**Media playlists (LL-HLS)**

TTL: 1 second

Reason: Low-latency streaming requires very frequent updates

**TS media segments and init segments**

TTL: 1209600 seconds (14 days)

Reason: Media segments don't change once created, so they can be cached for extended periods

**CMAF media segments and initialization segments**

TTL: 1209600 seconds (14 days)

Reason: Like TS segments, these are immutable once created

For comprehensive TTL recommendations across all MediaTailor workflows and additional caching optimization strategies, see [Caching optimization for CDN and MediaTailor
integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").

## Configure CDN cache policies

Proper cache policy configuration is essential for optimal performance and cost
efficiency. Different types of content (manifests, segments, initialization files) have
different caching requirements. Using separate cache behaviors allows you to optimize
caching for each content type, improving cache hit ratios and reducing origin load.
Without proper cache policies, you might experience unnecessary origin requests,
increased costs, and poor playback performance.

To properly honor MediaPackage cache-control headers and optimize caching:

1. Open your CloudFront distribution settings in the CloudFront console.
2. Create separate cache behaviors for different content types:
   - Manifest requests (\*.m3u8, \*.mpd)
   - Media segments (\*.ts, \*.mp4, \*.m4s)
   - Initialization segments

3. For each cache behavior, create or select a cache policy with these
   settings:
   - Enable "Origin Cache-Control Headers" option
   - Set "Origin request policy" to forward necessary headers
   - Configure query string forwarding based on content type

### Manifest cache behavior

For manifest requests (\*.m3u8, \*.mpd):

- **Path pattern**: \*.m3u8 and \*.mpd
- **Cache policy**: Honor origin cache-control
  headers
- **Query strings**: Forward specific
  parameters (see [Optimize query string forwarding](#cdn-query-string-optimization "#cdn-query-string-optimization"))
- **Headers**: Forward all headers (for minimum
  requirements, see [Required headers for MediaTailor CDN
  integration](cdn-configuration.md#cdn-required-headers "cdn-configuration.md#cdn-required-headers"))

### Media segment cache behavior

For media segments (\*.ts, \*.mp4, \*.m4s):

- **Path pattern**: \*.ts, \*.mp4, \*.m4s
- **Cache policy**: Honor origin cache-control
  headers (14-day TTL)
- **Query strings**: None (segments don't use
  query parameters)
- **Compression**: Enable for improved delivery
  performance

## Optimize query string forwarding

Query string optimization is critical for cache efficiency because unnecessary query
parameters create multiple cache variations for the same content. Each unique query
parameter combination creates a separate cache entry, which reduces cache hit ratios and
increases origin requests. By forwarding only the query strings that MediaPackage actually
uses, you maximize cache efficiency while maintaining full functionality.

Configure your CDN to forward only the query strings that MediaPackage uses, improving cache
efficiency:

**Essential query strings**

`start` and `end` - For time-shifted viewing
windows

`time_delay` - For applying time delay on manifest
contents

`_HLS_msn`, `_HLS_m`, and `_HLS_part` -
For LL-HLS playback requests

**Feature-specific query strings**

`aws.manifestfilter` - For [manifest filtering](cdn-emp-manifest-filtering.md "cdn-emp-manifest-filtering.md")

###### Important

Do not include any other query strings in your cache key. MediaPackage ignores
unrecognized parameters, and including them reduces cache efficiency by creating
unnecessary cache variations.

## Performance optimization techniques

These optimizations are configured on your CDN (such as CloudFront), not in MediaPackage or MediaTailor.
Implement these additional optimizations to maximize cache performance:

### Origin shield

Origin shield provides an additional caching layer between your CDN edge locations
and MediaPackage endpoints. This reduces the number of requests that reach your MediaPackage
endpoints, which can improve performance and reduce costs, especially during traffic
spikes or when cache hit ratios are lower than optimal. Origin shield is
particularly beneficial for live streaming where multiple edge locations might
request the same content simultaneously.

Enable origin shield to reduce load on your MediaPackage endpoints:

1. In your CloudFront distribution, enable Origin Shield for your MediaPackage
   origin.
2. Select an origin shield region close to your MediaPackage endpoint.
3. This creates an additional caching layer that reduces requests to
   MediaPackage.

### Compression configuration

Enable compression for text-based responses:

- Enable compression for manifest files (\*.m3u8, \*.mpd)
- Do not compress media segments (already compressed)
- Ensure all headers are forwarded to MediaPackage (for minimum requirements, see
  [Required headers for MediaTailor CDN
  integration](cdn-configuration.md#cdn-required-headers "cdn-configuration.md#cdn-required-headers"))

## Monitor cache performance

Track these key metrics to ensure optimal cache performance:

**Cache hit ratio**

Target: 90% or greater for media segments, 70% or greater for
manifests

Low ratios might indicate incorrect TTL settings or unnecessary query
parameters

**Origin request volume**

Monitor requests reaching MediaPackage endpoints

High volumes might indicate caching issues

**Cache key variations**

Review cache key patterns to identify unnecessary variations

Too many variations reduce cache efficiency

After implementing these cache optimizations, set up monitoring to track their
effectiveness. For guidance on monitoring cache hit ratios, origin request patterns, and
other key performance metrics, see [Monitor performance for MediaPackage, CDN, and MediaTailor
integrations](cdn-emp-monitoring.md "cdn-emp-monitoring.md"). If you observe poor cache performance or
unexpected origin requests, see [Troubleshoot MediaPackage, CDN, and MediaTailor
integrations](cdn-emp-troubleshooting.md "cdn-emp-troubleshooting.md") for troubleshooting steps.
