

# SMPERF01-BP01 Select origin technology appropriate for your workload
<a name="smperf01-bp01"></a>

Select origin technology that matches your streaming media workload's

characteristics and delivery requirements.

**Desired outcome:**
+ You have origin technology chosen against workload characteristics (live compared to video-on-demand (VOD), viewer count, geography, latency targets, and multi-protocol needs) rather than team familiarity or defaults.
+ Your architecture supports both pass-through and dynamic origin approaches where the workload justifies each, and the rationale for the choice is documented.
+ You can evolve the origin (add protocols, switch between pass-through and dynamic) without re-architecting the downstream content delivery network (CDN) and client stack.

**Common anti-patterns:**
+ Using a single origin type across live and VOD content, ignoring the performance and cost differences between the two workloads.
+ Applying pass-through origins to live workflows that require just-in-time packaging, DRM, or multi-protocol output.
+ Coupling origin decisions tightly to a specific CDN, making future CDN migration or a multi-CDN strategy difficult.

**Benefits of establishing this best practice:**
+ Lower delivery latency from selecting origins suited to the content type
+ Ability to scale origin capacity to match viewer demand spikes
+ Lower cost by avoiding over-provisioned or mismatched origin infrastructure
+ Fewer viewer-facing errors because of correctly placed packaging in the pipeline
+ Support for multiple streaming protocols without re-architecting

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Origin technology determines where packaging happens in the pipeline. A pass-through origin like Amazon S3 stores media that has already been packaged for delivery. It serves pre-built files without transforming them, so protocol, digital rights management (DRM), and manifest shape are all baked into what is stored. A dynamic origin like AWS Elemental MediaPackage packages at request time.

The same source asset can emit HTTP Live Streaming (HLS), Dynamic Adaptive Streaming over HTTP (DASH), or Common Media Application Format (CMAF) on demand. DRM can be inserted as the stream is assembled. That runtime flexibility costs compute and adds a component to the live path. It is also what separates a workflow that can add a new protocol in a week from one that has to re-encode the library.

Origin choice shapes CDN strategy as well. A multi-CDN setup routes through the origin, not around it. A dynamic origin with origin shield becomes a single caching point across CDN vendors. A pass-through origin is simpler but forces per-CDN packaging variants when clients need formats the stored files don't carry.

### Implementation steps
<a name="implementation-steps"></a>

1. **Analyze workload requirements:** Evaluate VOD and live needs, expected viewer count, and geographic distribution.

1. **Evaluate pass-through vs dynamic origin approaches:** Pass-through origins work well for limited client compatibility requirements and lowest latency, while dynamic origins support diverse client ecosystems and advanced features.

1. **Select appropriate origin technology:** Use AWS MediaPackage for live and VOD content with just-in-time packaging, AWS Elemental MediaPackage V2 for low-latency live workflows, and Amazon S3 for VOD content storage with high performance.

1. **Configure CDN integration:** Set up Amazon CloudFront for content delivery.

1. **Implement CMAF:** Use Common Media Application Format for multi-protocol support.

1. **Perform performance testing and optimization:** Validate the configuration meets performance requirements.

1. **Monitor cache hit ratios and origin performance metrics:** Establish ongoing monitoring for operational health.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMPERF03-BP01 Use a content delivery network and monitor your cache-hit-ratio](smperf03-bp01.html)
+ [SMPERF05-BP01 Optimize the number of adaptive bitrate renditions for your workload](smperf05-bp01.html)

**Related documents**
+ [Delivering Live Streaming Video with CloudFront and AWS Media Services](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/live-streaming.html)
+ [AWS Elemental MediaPackage User Guide](https://docs.aws.amazon.com/mediapackage/)

**Related services**
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)