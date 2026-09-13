

# Content delivery
<a name="smperf03"></a>

CDN configuration and cache strategy determine whether viewers are served from nearby edge locations or generate repeated requests back to origin. Cache hit ratio is the primary performance and efficiency metric for delivery.


| SMPERF03: How do you use caching to improve content delivery performance? | 
| --- | 
| [SMPERF03-BP01 Use a content delivery network and monitor your cache-hit-ratio](smperf03-bp01.md) | 
| [SMPERF03-BP02 Optimize cache-control headers for your content](smperf03-bp02.md) | 

## Capability intent
<a name="smperf03-intent"></a>
+ A CDN is in front of every origin with cache hit ratio tracked per content type.
+ Cache-control headers are set per content type (live manifests, segments, and VOD assets).
+ Origin shield collapses redundant requests from multiple edge locations.
+ Invalidation is targeted rather than full-distribution.

## Maturity levels
<a name="smperf03-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | A CDN is in place but cache-control headers are defaults. Cache hit ratio isn't measured. | 
| 2 | Emerging | Bandwidth is tracked, but cache hit ratio isn't broken out per content type. Invalidation is full-distribution when issues arise. | 
| 3 | Defined | Cache-control headers are tuned per content type (manifests compared to segments compared to VOD), cache hit ratio is monitored, and origin shield is configured. | 
| 4 | Proactive | Cache hit ratio is tracked per content type with alerts on regression. Invalidation is path-targeted and automated for known failure scenarios. | 
| 5 | Optimized | Cache strategy is continuously refined from real traffic patterns, origin load is minimal, and invalidation is surgical with no measurable viewer impact. | 

## Common issues to watch for
<a name="smperf03-issues"></a>
+ Tracking bandwidth but not cache hit ratio.
+ Default cache-control headers that cause either over-caching of dynamic content or under-caching of static content.
+ Caching live manifests as long as segments, causing stale playback.
+ Full-distribution invalidation instead of path-targeted invalidation.