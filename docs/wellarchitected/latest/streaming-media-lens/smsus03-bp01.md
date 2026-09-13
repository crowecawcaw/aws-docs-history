

# SMSUS03-BP01 Implement efficient encoding and delivery mechanisms
<a name="smsus03-bp01"></a>

Encode and deliver streaming media so that each viewer receives acceptable quality at the lowest practical bit rate. Encoding and delivery dominate the resource footprint of a streaming workload, because every avoidable bit is multiplied across millions of viewer sessions in transcode compute, network transfer, and client decode energy. Reducing bit rate to the minimum that delivers acceptable quality is the primary sustainability action in encoding and delivery.

**Desired outcome:**
+ Your encoding ladder allocates bit rate to each title and rendition based on content complexity and real viewing demand, not a fixed one-size-fits-all profile.
+ Renditions that viewers don't request are not produced or stored.
+ Codec and packaging choices are made per content tier, balancing compression efficiency against the compute cost of encoding and the device reach of the codec.

**Common anti-patterns:**
+ Applying a single fixed bit rate ladder to every title, so simple content (a static talk-show set) is encoded at the same bit rate as complex content (fast-motion sport) and wastes bits on the simple content.
+ Pre-encoding and storing every rendition for the entire catalog, including long-tail titles that are watched rarely or never, so storage and encode energy are spent on content nobody streams.
+ Adopting a more efficient codec across the whole catalog without checking device decode support, so a large share of viewers fall back to a less efficient codec and the extra encode compute is wasted.
+ Routing every lightweight personalization or redirect decision back to the origin instead of resolving it at the edge, adding origin compute and network round-trips to each request.

**Benefits of establishing this best practice:**
+ Lower network transfer and client decode energy, because fewer bits are delivered per viewing session across the audience.
+ Reduced transcode compute and storage, because renditions are matched to demand rather than produced speculatively.
+ Lower delivery cost that tracks the same reductions in bytes served and compute consumed.
+ Sustained efficiency as catalog and audience change, because encoding decisions are driven by measured complexity and demand rather than a static profile.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

The resource cost of streaming is dominated by delivery, not by any single encode. An encode happens once per rendition, but the resulting bits are then transferred and decoded once per viewing session, so a bit rate reduction on a popular title compounds across every viewer. This is why content-aware and per-title encoding matter. Allocating bit rate to the complexity of the content, rather than to a fixed ladder, removes bits that add no perceptible quality and that would otherwise be paid for in network and decode energy on every play. Quality-defined variable bit rate encoding expresses this directly by targeting a quality level and spending only the bit rate that level requires.

Codec choice is a genuine trade-off rather than a clear win, and treating it as one is the most common way this practice goes wrong. Newer codecs compress better, which lowers delivery energy, but they cost more compute to encode and require decode support on the viewer's device. The decision turns on the ratio of encodes to plays and on audience device reach. For a popular title watched millions of times on devices that decode the codec in hardware, the one-time encode cost is repaid many times over in delivery savings, while for a long-tail title or an audience without decode support, the extra encode compute and the fallback to an older codec can erase the benefit. Decide per content tier, not once for the whole catalog.

The same demand-driven logic governs whether to pre-package renditions or generate them just in time. Pre-packaging trades storage for low per-request compute and suits head content with predictable, high demand. Just-in-time packaging trades per-request compute for far less storage and suits the long tail, where producing and storing every rendition in advance wastes resources on content that is rarely streamed. Energy use isn't directly measurable per stream, so use resource proxies such as bytes delivered per viewing session, encoder compute hours, and cache hit ratio. Read account-level carbon impact per Region from the AWS Customer Carbon Footprint Tool, which publishes on a monthly cadence.

### Implementation steps
<a name="implementation-steps"></a>

1. **Adopt quality-defined, content-aware encoding:** Replace fixed-bit rate profiles with quality-defined variable bit rate (QVBR) encoding in AWS Elemental MediaConvert for on-demand content and AWS Elemental MediaLive for live content, targeting a consistent perceptual quality rather than a fixed bit rate. This spends bit rate only where content complexity requires it.

1. **Right-size the encoding ladder to real demand:** Review which renditions viewers actually request by device and network class, and remove ladder rungs that are rarely selected. Producing fewer renditions reduces both transcode compute and the storage those renditions occupy.

1. **Select codecs per content tier:** For high-demand titles streamed to devices with hardware decode support, encode with a higher-efficiency codec such as AOMedia Video 1 (AV1) or High Efficiency Video Coding (HEVC) to cut delivery bits. For long-tail titles or audiences without decode support, stay on a widely supported codec to avoid spending encode compute that doesn't pay back. Base the decision on the ratio of expected plays to encodes.

1. **Match packaging strategy to content popularity:** Pre-package renditions for predictable, high-demand head content, and use just-in-time packaging for long-tail content so that rarely watched titles don't consume storage for renditions that are seldom served.

1. **Resolve lightweight delivery logic at the edge:** Move header rewrites, redirects, and lightweight personalization to Amazon CloudFront Functions or Lambda@Edge so these decisions don't generate origin compute and network round-trips on every request.

1. **Measure efficiency with resource proxies:** Track the following metrics, and review them alongside the monthly account-level figures from the AWS Customer Carbon Footprint Tool to confirm that encoding and packaging changes reduce consumed resources rather than shifting them:
+ Bytes delivered per viewing session
+ Encoder compute hours per title
+ Content delivery network (CDN) cache hit ratio

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSUS05-BP01 Implement intelligent storage tiering and content lifecycle management](smsus05-bp01.html)
+ [SMSUS06-BP01 Optimize data flow and caching strategies](smsus06-bp01.html)

**Related documents**
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part I](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-i/)
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part II, Codecs and Implementation](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-ii-codecs-and-implementation/)

**Related services**
+ [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)
+ [AWS Elemental MediaLive](https://aws.amazon.com/medialive/)
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [Lambda@Edge](https://aws.amazon.com/lambda/edge/)