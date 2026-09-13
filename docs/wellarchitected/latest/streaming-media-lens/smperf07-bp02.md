

# SMPERF07-BP02 Implement ad prefetching to optimize ad decision server performance and improve fill rates
<a name="smperf07-bp02"></a>

Prefetch ad inventory ahead of predictable ad breaks to reduce real-time load on the ad decision server and improve fill rates.

**Desired outcome:**
+ You have an ad prefetching layer that proactively fills inventory ahead of predictable ad breaks, reducing real-time load on the ad decision server (ADS).
+ Your prefetching respects targeting rules and campaign expiry so prefetched inventory stays valid at serve time.
+ You measure prefetch success through fill-rate improvements and ADS load reduction, not just cache hit count.

**Common anti-patterns:**
+ Prefetching aggressively without campaign-level expiry controls, serving expired or retargeted ads at viewer playback time.
+ Measuring prefetch success by cache hit count alone, ignoring fill-rate improvement and ADS load reduction.
+ Building prefetching as bespoke code per ad campaign rather than as a reusable capability across campaigns.

**Benefits of establishing this best practice:**
+ Lower real-time load on the ADS during concurrent-viewer spikes and live events
+ Higher fill rates because inventory is resolved before the ad break arrives
+ Faster ad break start since prefetched responses avoid round-trip latency to the ADS
+ Continued ad delivery during brief ADS outages because prefetched inventory is already local
+ Ability to scale to large live audiences without linearly scaling ADS capacity
+ Reusable prefetching framework that works across campaigns without per-campaign engineering

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Ad prefetching differs from HTTP caching in an important way. A cache holds a bytewise-identical response that any viewer can use. A prefetched ad is tied to a targeting profile and a campaign state that can change before the viewer sees it. The campaign can run out of budget, get replaced for legal reasons, or expire in its flight window. If prefetching is treated like an HTTP cache, stale ads go live. This also creates a measurement problem. A cache hit on expired inventory counts as a miss from the business perspective because the ad can't be served. Useful metrics are fill rate and ADS load reduction, not cache hit count. Prefetching also forces an early architectural choice. Per-viewer prefetch fetches inventory matched to each session's targeting profile, which is precise but expensive at scale. Population prefetch builds a pool per region or per content and draws from it when a viewer arrives, which is cheaper but looser on targeting. Most real systems blend the two. This choice belongs at the framework level rather than being made per campaign. Systems that bolt custom prefetch logic on top of the ad stack for each new brief pay the engineering cost every time. A reusable prefetching capability avoids that accumulation.

### Implementation steps
<a name="implementation-steps"></a>

1. **Analyze content and viewing patterns:** Identify predictable ad break patterns in live and video on demand (VOD) content, analyze viewer behavior and content popularity metrics, and determine optimal prefetching timing based on content characteristics.

1. **Implement intelligent prefetching algorithms:**
+ Develop prefetching logic based on content metadata and viewer patterns
+ Configure prefetching triggers for different content types (live events, popular VOD)
+ Implement adaptive prefetching based on real-time demand and ADS performance

1. **Set up prefetched ad storage and management:** Configure distributed caching infrastructure for prefetched ads, implement ad expiration and refresh mechanisms, and set up geographic distribution of prefetched ad inventory.

1. **Optimize prefetching strategies:** Configure prefetching depth based on content duration and ad break frequency, implement priority-based prefetching for high-value or time-sensitive campaigns, and balance prefetching aggressiveness with storage and bandwidth costs.

1. **Integrate with ad decision workflows:** Configure fallback mechanisms between prefetched and real-time ad requests, implement ad targeting validation for prefetched inventory, and set up real-time ad decisioning for non-prefetchable scenarios.

1. **Monitor and optimize performance:**
+ Track prefetching hit rates and storage utilization
+ Monitor ADS load reduction and response time improvements
+ Analyze fill rate improvements and revenue impact
+ Implement automated optimization based on performance metrics

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMPERF07-BP01 Implement Server-Side Ad Insertion (SSAI) for seamless viewer experience](smperf07-bp01.html)
+ [SMPERF03-BP01 Use a content delivery network and monitor your cache-hit-ratio](smperf03-bp01.html)

**Related documents**
+ [AWS Elemental MediaTailor User Guide](https://docs.aws.amazon.com/mediatailor/)
+ [Amazon CloudFront Caching Best Practices](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html)
+ [Optimizing Video Ad Delivery with AWS Media Services](https://aws.amazon.com/blogs/media/)

**Related services**
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/)
+ [Amazon ElastiCache](https://aws.amazon.com/elasticache/)