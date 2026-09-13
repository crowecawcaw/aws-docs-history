

# SMSUS06-BP01 Optimize data flow and caching strategies
<a name="smsus06-bp01"></a>

Move streaming media as few times and as short a distance as possible. Every transfer of media data carries transfer energy and often triggers duplicate downstream processing, so a workload that copies content across Regions, re-fetches from origin on every request, or shuttles intermediate files between processing stages consumes resources out of proportion to the value delivered.

**Desired outcome:**
+ Content is served to viewers from caches close to them, so repeated requests don't return to the origin.
+ Processing pipelines keep data within a single Region where the architecture allows, avoiding cross-Region transfer of large media files.
+ Intermediate file movement between processing stages is minimized rather than treated as costless.

**Common anti-patterns:**
+ Serving media directly from the origin on every request instead of caching at the edge, so identical content is transferred and processed repeatedly.
+ Spreading a transcode pipeline across Regions so large intermediate files are copied between Regions at each stage.
+ Re-fetching or re-transferring whole assets when only a small portion has changed, instead of updating incrementally.
+ Reading frequently accessed metadata from a database on every request rather than caching it, adding repeated query load and data movement.

**Benefits of establishing this best practice:**
+ Lower network transfer energy, because content is served from nearby caches rather than repeatedly from the origin.
+ Reduced origin compute, because cache hits remove load from origin servers.
+ Less cross-Region transfer, because processing keeps large media files within a Region where possible.
+ Lower repeated query and transfer load, because hot metadata is served from memory.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

The resource cost of data movement scales with both distance and repetition, and streaming amplifies both. A single popular asset can be requested millions of times, so serving it from a content delivery network cache close to viewers, rather than returning to the origin each time, removes both the repeated transfer over long distances and the repeated origin compute. Cache hit ratio is one of the most significant efficiency metrics in a streaming workload. Each percentage point of additional hit rate is transfer and origin work that doesn't happen.

Within the processing pipeline, the equivalent waste is moving large intermediate files further than necessary. Media files are large, and a transcode pipeline that spreads stages across Regions copies those files between Regions at each hand-off, paying transfer energy for data that could have stayed local. Keeping a processing workflow within a single Region where the resilience requirement allows removes that cross-Region movement entirely. Multi-Region designs exist for availability and disaster recovery, so confine single-Region processing to workflows where that availability requirement doesn't apply rather than forcing it everywhere.

Caching costs storage and memory, so it carries its own overhead, but for content read far more often than it changes the saving in repeated transfer and compute dwarfs the cost of holding the cache. Apply the same logic to metadata. Hot metadata served from an in-memory cache avoids repeated database queries and the data movement they generate. Energy use isn't measurable per transfer, so use resource proxies such as cache hit ratio, cross-Region transfer bytes, and origin egress. Read account-level carbon impact per Region from the AWS Customer Carbon Footprint Tool, which publishes monthly.

### Implementation steps
<a name="implementation-steps"></a>

1. **Cache delivery at the edge:** Serve media through Amazon CloudFront with cache behaviors tuned to content stability, and enable Origin Shield to collapse origin requests. Target and monitor a high cache hit ratio, because each cache hit removes both long-distance transfer and origin compute.

1. **Keep processing within a single Region:** Design transcode and packaging pipelines so media files stay within one Region wherever the resilience requirement allows, avoiding cross-Region copies of large intermediate files.

1. **Reduce intermediate file movement:** Streamline transcode workflows to minimize the number of intermediate file copies between stages, and colocate processing stages so hand-offs don't cross Region or account boundaries unnecessarily.

1. **Cache hot metadata in memory:** Use Amazon ElastiCache to serve frequently accessed metadata (catalog, manifests, and entitlement lookups) from memory rather than querying the database on every request.

1. **Update content incrementally:** Where assets change in part rather than whole, use delta or incremental update mechanisms so only the changed portion is transferred rather than the entire asset.

1. **Measure data-movement efficiency:** Track the following metrics, and review against the monthly account-level figures from the AWS Customer Carbon Footprint Tool to confirm changes are reducing data movement rather than relocating it.
+ Cache hit ratio
+ Cross-Region transfer bytes
+ Origin egress

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSUS01-BP01 Optimize regional distribution of streaming workloads](smsus01-bp01.html)
+ [SMSUS05-BP01 Implement intelligent storage tiering and content lifecycle management](smsus05-bp01.html)

**Related documents**
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part I](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-i/)
+ [Amazon CloudFront caching](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio-explained.html)

**Related services**
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
+ [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)