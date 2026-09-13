

# SMCOST01-BP02 Optimize content delivery using edge caching and just-in-time packaging
<a name="smcost01-bp02"></a>

Content delivery is typically the largest cost component for organizations streaming to large audiences. A 60-minute video streamed to 1,000 concurrent viewers can generate over 2,700 GB of data transfer per hour. Reducing how often content is fetched from origin and how much content needs to be stored in multiple formats directly reduces this cost while improving viewer experience through lower latency.

**Desired outcome:**
+ You have cache hit ratios above 95% for media segment requests because cache behaviors are tuned to content immutability characteristics.
+ You have removed multiplicative storage costs by serving multiple output formats from a single stored source through just-in-time packaging.
+ You have selected delivery price classes that match your actual audience geography rather than paying for global edge coverage you don't use.

**Common anti-patterns:**
+ Serving all content requests directly from the origin without edge caching, resulting in high data transfer costs and unnecessary origin load.
+ Pre-packaging content in every protocol and DRM combination at encoding time, multiplying storage costs by the number of format variants.
+ Configuring a single cache behavior with short TTLs for all content types, treating immutable video segments the same as frequently-updating manifests.
+ Forwarding unnecessary request headers to the origin, fragmenting the cache into separate entries for requests that should share a response.

**Benefits of establishing this best practice:**
+ Origin egress costs decrease because cached content at edge locations absorbs the majority of viewer requests without reaching origin.
+ Storage costs drop because a single stored format serves all output protocols through on-the-fly packaging rather than pre-computed variants.
+ Per-viewer delivery cost decreases as audience scales because cache population is amortized across all viewers requesting the same content.
+ Viewer experience improves because edge-served content has lower latency and fewer buffering events than origin-served content.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Streaming media has a property that most web content doesn't: segments are immutable once created. A video segment file never changes after encoding. This means segments can be cached aggressively with long TTLs and served indefinitely without cache validation. Manifests (HLS playlists, DASH MPDs) are the opposite. For live streams, manifests update every segment duration to advertise new segments. For VOD, manifests are stable. Treating these two content types identically in cache configuration wastes either freshness (stale manifests) or cache efficiency (short-lived segment entries).

Each unique combination of request attributes that a CDN forwards to origin creates a separate cache entry. Forwarding headers that vary per-viewer (device type, accept-encoding, cookies) fragments the cache so that the same segment is fetched from origin repeatedly for different header combinations. The result is low cache hit ratios despite high request volume. Minimizing forwarded headers to only those the origin needs for content selection is one of the highest-impact optimizations available.

Geographically distributed audiences cause a related problem. Each edge location independently populates its cache from origin, so the same content may be fetched once per edge location. An additional centralized caching layer between edge locations and origin consolidates these requests into a single origin fetch regardless of how many edge locations request the content. This is particularly valuable for live streams where every edge location needs the same new segments within seconds of each other.

The cost of supporting multiple output formats compounds quickly. An organization serving HLS, DASH, and CMAF with two DRM schemes stores six to ten copies of every piece of content. Just-in-time packaging removes this multiplication by storing content once and transforming it into the requested format at delivery time. CMAF further reduces the footprint by enabling a single set of media segments to serve both HLS and DASH players without repackaging. The trade-off is that packaging compute replaces storage cost, but for most audience sizes the compute cost is far lower than storing and invalidating multiple format variants.

Price class selection is an often-overlooked lever. Serving content from all global edge locations costs more per GB than serving from a subset. Organizations with audiences concentrated in specific regions (North America and Europe, for example) can reduce delivery costs by 20-40% by selecting a targeted price class that excludes regions where they have no viewers.

### Implementation steps
<a name="implementation-steps"></a>

1. **Configure content-type-aware cache behaviors:** Create separate [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html) cache behaviors for media segments (`.ts`, `.m4s`, `.mp4`) with TTLs of 24 hours or more for VOD and segment duration for live. Create a separate behavior for manifests (`.m3u8`, `.mpd`) with TTLs of 1-3 seconds for live streams and longer for VOD. Set a default behavior for other assets with appropriate TTLs.

1. **Minimize forwarded headers and query strings:** Configure [CloudFront origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html) to forward only headers required by your origin for content selection. Don't forward `Accept-Encoding` unless your origin serves pre-compressed content. Each unnecessary forwarded header multiplies cache fragmentation.

1. **Enable a centralized caching layer for origin consolidation:** Enable [CloudFront Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html) in the Region closest to your origin. This additional caching layer consolidates requests from multiple edge locations into a single origin request per piece of content, reducing origin load for geographically distributed audiences.

1. **Configure just-in-time packaging from a single stored format:** Set up [AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is.html) endpoints for each required output format (HLS, DASH, or CMAF). Store content in a single intermediate format and let MediaPackage transform it on demand. Enable CMAF packaging where player compatibility allows to serve both HLS and DASH from a single segment set. Configure DRM encryption at the packaging layer rather than at encoding time.

1. **Select the price class that matches your audience distribution:** Choose the [CloudFront Price Class](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html) that covers your actual viewer geography. Use Price Class 100 (North America and Europe) or Price Class 200 (adding Asia-Pacific) for regionally concentrated audiences. Use Price Class All only when serving a truly global audience.

1. **Monitor cache performance and origin load:** Track cache hit ratio in the CloudFront console and set [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms for drops below your target threshold. Monitor origin request rates separately. Spikes in origin requests indicate cache misses from misconfiguration, TTL expiry storms, or new content without sufficient pre-warming.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMCOST01-BP01 Implement lifecycle management for media assets](smcost01-bp01.html)
+ [SMCOST03-BP02 Optimize encoder settings based on content type](smcost03-bp02.html)

**Related documents**
+ [Video on demand and live streaming video with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/on-demand-streaming-video.html)
+ [CloudFront Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html)
+ [Controlling origin requests](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html)

**Related examples**
+ [Live Streaming on AWS](https://aws.amazon.com/solutions/implementations/live-streaming-on-aws/)
+ [Video on Demand on AWS](https://aws.amazon.com/solutions/implementations/video-on-demand-on-aws/)

**Related services**
+ [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
+ [AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is.html)
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)