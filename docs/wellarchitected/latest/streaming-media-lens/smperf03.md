

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

## Common issues to watch for
<a name="smperf03-issues"></a>
+ Tracking bandwidth but not cache hit ratio.
+ Default cache-control headers that cause either over-caching of dynamic content or under-caching of static content.
+ Caching live manifests as long as segments, causing stale playback.
+ Full-distribution invalidation instead of path-targeted invalidation.