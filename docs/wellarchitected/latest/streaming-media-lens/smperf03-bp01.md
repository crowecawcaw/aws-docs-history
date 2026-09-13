

# SMPERF03-BP01 Use a content delivery network and monitor your cache-hit-ratio
<a name="smperf03-bp01"></a>

Deploy a content delivery network (CDN) in front of your streaming

origins and monitor cache-hit-ratio per content type to protect the origin and reduce viewer latency.

**Desired outcome:**
+ You have a CDN in front of every streaming origin, absorbing viewer load at the edge and protecting the origin from traffic spikes.
+ Your cache-hit-ratio is tracked per content type (live manifests, live segments, video on demand (VOD)) and alerts fire when it drifts below targets.
+ Your time-to-first-byte for viewers is dominated by edge delivery, not origin fetches.

**Common anti-patterns:**
+ Tracking overall CDN bandwidth but not cache-hit-ratio, hiding origin shield failures until costs spike.
+ Invalidating the entire distribution when only a handful of objects need refreshing, instead of targeting specific paths.
+ Running without an origin shield, forcing every edge miss to hit the origin directly.

**Benefits of establishing this best practice:**
+ Lower time-to-first-byte because viewers fetch from nearby edge caches
+ Less load and lower cost on origin infrastructure during traffic spikes
+ Ability to scale to large concurrent audiences without origin bottlenecks
+ Faster playback start and fewer mid-stream stalls for geographically distributed viewers
+ Clear cost signal when cache-hit-ratio drops, enabling proactive capacity planning

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

A single aggregate cache-hit-ratio (CHR) number masks important differences between content classes. The 95% overall CHR on a CDN dashboard can hide different per-class behavior. Live manifests might run at 40% hits. Segments might run at 99%. Segments dominate the average because they are requested far more often. Manifest latency affects every viewer directly because the player must fetch a fresh manifest before it can request the next segment. CHR has to be broken down by content class before it becomes a signal worth acting on. CHR also correlates directly with origin cost. At a live event, a one-point drop in segment CHR can multiply origin bandwidth by ten. Every miss fans out to a distinct origin fetch. When you treat CHR as a capacity-planning input alongside a performance metric, drops in CHR can trigger cost alerts before they become billing surprises.

### Implementation steps
<a name="implementation-steps"></a>

1. **Deploy Amazon CloudFront as your CDN solution:** Set up CloudFront distributions for your streaming content.

1. **Configure cache behaviors for different content types:** Set the following:
+ Live manifests to half segment length or less
+ Live segments to 21,600 seconds or max digital video recorder (DVR) window
+ VOD content to 86,400 seconds or longest possible

1. **Enable CloudFront monitoring and metrics:** Activate monitoring for visibility into CDN performance.

1. **Monitor cache hit ratio, origin latency, and HTTP error rates:** Track key performance indicators for cache effectiveness.

1. **Set up CloudWatch alarms for cache performance thresholds:** Configure alerts to detect performance degradation.

1. **Optimize cache-control headers from origin:** Verify the origin sends appropriate caching directives for each content type.

1. **Implement cache invalidation procedures:** Establish processes for invalidating stale content when needed.

1. **Monitor and minimize negative caching for live content:** Reduce the impact of error responses being cached.

## Resources
<a name="resources"></a>

**Related documents**
+ [Increase the proportion of requests served from CloudFront caches (cache hit ratio)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html)
+ [Use Amazon CloudFront Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html)
+ [Amazon CloudFront for Media: CloudFront configuration best practices](https://docs.aws.amazon.com/whitepapers/latest/amazon-cloudfront-media/cloudfront-configuration-best-practices.html)

**Related services**
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)