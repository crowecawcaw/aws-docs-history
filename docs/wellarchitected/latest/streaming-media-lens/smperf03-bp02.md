

# SMPERF03-BP02 Optimize cache-control headers for your content
<a name="smperf03-bp02"></a>

Set cache-control headers at the origin so each content type (live

manifests, live segments, video on demand (VOD)) is cached for the right duration.

**Desired outcome:**
+ You have cache-control headers set at the origin for every content type, with live manifests, live segments, and VOD treated differently.
+ Your live manifests are cached for at most half a segment duration so viewers receive fresh manifests without overloading the origin.
+ You have a documented invalidation runbook for the rare occasions when cached content must be pulled quickly.

**Common anti-patterns:**
+ Leaving default cache-control headers on the origin and relying on content delivery network (CDN) fallback behavior, which differs across providers.
+ Caching live manifests as long as live segments, leaving viewers stuck on stale manifests after a format change.
+ Setting `no-cache` on live segments to avoid stale content, collapsing the entire cache benefit at the edge.

**Benefits of establishing this best practice:**
+ Higher cache-hit-ratio because TTLs match how often content actually changes
+ Fresh manifests for live viewers without overloading the origin
+ Fewer origin requests, reducing both cost and origin error risk
+ Faster segment delivery from edge when segments carry long TTLs
+ Documented invalidation path for the rare cases when cached content must be pulled

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Cache-control headers for streaming require different time to live (TTL) values for manifests and segments because of how HTTP Live Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH) work. In HLS and DASH, the live manifest URL doesn't change, yet its contents update every few seconds as new segments are published. A segment URL is the opposite. It is published once and never rewritten. Headers must reflect this asymmetry. Manifests get a short TTL so viewers pick up the latest segment list. Segments get a long TTL because their bytes are immutable for the life of the content.

### Implementation steps
<a name="implementation-steps"></a>

1. **Configure origin to send appropriate Cache-Control headers:** Set the following:
+ Live manifest caching to half segment length or less
+ Live segment caching to maximum DVR window duration
+ VOD content caching to 86,400 seconds or maximum possible

1. **Configure CDN to respect origin cache headers:** Confirm Amazon CloudFront honors the cache directives from your origin rather than applying its own defaults.

1. **Implement cache invalidation runbook:** Create documented procedures for content updates requiring cache invalidation.

1. **Monitor cache performance and adjust headers as needed:** Continuously evaluate and tune caching behavior based on observed metrics.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMPERF03-BP01 Use a content delivery network and monitor your cache-hit-ratio](smperf03-bp01.html)

**Related documents**
+ [Managing How Long Content Stays in an Edge
+ [Increasing Cache Hit

**Related services**
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)