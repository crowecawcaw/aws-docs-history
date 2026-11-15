

# ADVCOST06-BP03 Pre-cache creative assets at the CDN edge to avoid redundant origin fetches
<a name="advcost06-bp03"></a>

 Innovative ad formats (such as interactive overlays, shoppable ads, and 360 video) have larger creative payloads than standard ads. Fetching the same creative from origin on every impression wastes bandwidth and increases latency. CDN edge caching and pre-fetching avoids redundant origin fetches. 

 **Desired outcome:** 
+  Innovative format creatives are cached at CDN edge locations with TTLs aligned to campaign flight dates. 
+  CloudFront cache hit rate exceeds 90% for frequently served rich-media creatives. 
+  Pre-fetching during SGAI ad break preparation delivers creatives with no perceptible latency. 

 **Common anti-patterns:** 
+  Fetching rich-media creative assets (interactive overlays, shoppable ads, 360 video) from origin on every impression without CDN caching, so redundant origin egress and transfer costs scale linearly with impression volume for the same creative served repeatedly. 
+  Setting cache TTLs too short relative to campaign flight dates, which causes unnecessary cache evictions and origin refetches for creatives that remain unchanged throughout the campaign. 
+  Setting cache TTLs too long, which serves stale creatives after mid-flight updates and wastes CDN storage on expired assets. 
+  Delivering large innovative format payloads synchronously at ad break time without pre-fetching during the SGAI preparation phase, which introduces playback latency that degrades interactive engagement rates and viewer experience for premium ad formats. 
+  Treating all creative formats with the same caching strategy regardless of creative size and frequency, which fails to prioritize aggressive edge caching for high-impression rich-media creatives where the per-fetch origin cost is much higher than standard display ads. 
+  Caching creative assets at the CDN edge without also caching creative metadata and decision parameters at the application layer, so origin calls for ad selection logic continue on every impression even when the creative asset itself is cached. 

 **Benefits of establishing this best practice:** 
+  Avoid redundant origin fetches for frequently served rich-media creatives 
+  Reduced per-impression latency improves interactive ad engagement rates 
+  Pre-fetching during SGAI preparation delivers creatives with no perceptible latency 
+  Aligned cache TTLs help avoid stale creatives and wasted storage 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Innovative ad formats (interactive overlays, shoppable ads, 360-degree video) have creative payloads far larger than standard video ads. When the same creative serves thousands or millions of impressions during a campaign flight, fetching it from origin on every impression produces redundant data transfer costs that scale linearly with impression volume. 

 CDN edge caching avoids these transfer costs from growing with each impression. After the first fetch populates the edge cache, [CloudFront](https://aws.amazon.com/cloudfront/) serves later requests for the same creative from the edge location closest to the viewer, and origin egress drops to near zero for high-impression creatives. Cache hit rates above 90% are achievable for rich-media creatives that serve repeatedly during a campaign, but only when cache TTLs match campaign flight dates. 

 Pre-fetching lowers the latency viewers experience at the ad break. SGAI ad breaks have a preparation phase before the viewer reaches the break position. During that window, pull creative assets into the edge cache instead of waiting for the first viewer request to trigger a cache miss. For interactive formats where engagement depends on responsiveness, even a few hundred milliseconds of fetch latency can reduce interaction rates. 

 Caching happens at two layers, each handling a different part of the request. CDN edge caching handles the creative asset itself (video segments, overlay assets, and interactive components). Application-layer caching in [ElastiCache](https://aws.amazon.com/elasticache/) handles creative metadata (VAST URLs, dimensions, format capabilities, and targeting parameters). Without metadata caching, every impression still requires an origin call for ad selection logic even when the creative asset is already at the edge. Use both caching layers to avoid redundant origin traffic. 

 High-impression rich-media creatives benefit most because their per-fetch origin cost is large and their frequency is high. Standard display ads with small assets and low repeat rates might not justify the operational complexity of pre-fetching and TTL management. Tier caching strategy by format payload size and expected impression volume. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure CloudFront cache behaviors with campaign-flight TTLs:** Set Cache-Control: max-age headers on innovative format creative assets to the campaign end date. Configure CloudFront Origin Shield to consolidate origin requests when creatives are accessed from multiple edge locations. 

1.  **Pre-fetch during SGAI ad preparation:** When MediaTailor prepares an SGAI ad break, trigger Lambda-based CloudFront cache warming for selected creative assets before the viewer reaches the break position. This populates the edge cache before demand arrives. 

1.  **Monitor cache hit ratio per creative format:** Create CloudFront real-time log dashboards showing cache hit ratio per creative format type. Set alarms when hit ratio drops below 90%. Investigate cache misses caused by TTL misconfiguration or unexpected creative URL patterns. 

1.  **Configure ElastiCache for creative metadata caching:** Cache creative metadata (VAST URLs, dimensions, and format capabilities) in ElastiCache to avoid repeated lookups from the ad decisioning database on each impression. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST06-BP04 Use device capability filtering to avoid wasted spend on unsupported formats](advcost06-bp04.md) 

 **Related services:** 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 