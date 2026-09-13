

# SMPERF06-BP01 Optimize processing, origination, delivery, and client for low latency
<a name="smperf06-bp01"></a>

Implement low-latency optimizations across the entire streaming pipeline while carefully managing tradeoffs with quality and reliability.

**Desired outcome:**
+ You have glass-to-glass latency optimized across encoder, origin, content delivery network (CDN), and player, not through isolated tuning of one layer.
+ Your latency targets are set per use case (sports, news, and gaming) and balanced explicitly against quality and reliability trade-offs.
+ Your player is tuned with buffer settings that match the latency target so delivery-side optimization isn't wasted at the client.

**Common anti-patterns:**
+ Reducing segment length without matching encoder, packager, CDN, and player settings, so one slow hop negates the rest.
+ Defining latency targets in isolation from viewer experience research, chasing numbers that don't matter to the business.
+ Ignoring player buffer tuning, leaving the client as the bottleneck after encoder and delivery are optimized.

**Benefits of establishing this best practice:**
+ Lower glass-to-glass latency that keeps viewers in sync with the live moment
+ Ability to support interactive overlays, betting, and chat that depend on timing
+ Fewer viewer complaints during live sports where broadcast parity matters
+ Reduced rebuffer risk when latency reductions are paired with correct buffer tuning
+ Clear latency budget per hop, making it straightforward to diagnose regressions

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Glass-to-glass latency is the sum of delays across every hop in the pipeline, and reducing it requires understanding where the time goes. The viewer's delay is the sum of encoder, packager, origin, CDN, network, and player, each with its own floor. Tuning one hop without measuring the others can move the bottleneck rather than remove it, so measure delay at every hop before deciding where to invest. Two tools matter most. Common Media Application Format (CMAF) chunked transfer releases sub-segment bytes before a segment is complete and lets low-latency HTTP Live Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH) decouple latency from segment length. The second is a clear business reason for the target, since short groups of pictures (GOPs) and shallow buffers cost bit rate efficiency and rebuffer resilience in marginal networks.

### Implementation steps
<a name="implementation-steps"></a>

1. **Reduce media segment lengths:** Configure 1-2 second segments for low latency delivery.

1. **Optimize encoder settings for low latency:** Reduce lookahead buffer size, use faster encoding presets where quality permits, and minimize processing delays in the encoding pipeline.

1. **Configure origin for low-latency delivery:** Use AWS Elemental MediaPackage with low-latency HLS and enable chunked transfer encoding where supported.

1. **Optimize CDN configuration:** Use Amazon CloudFront with HTTP/3 support and configure appropriate cache behaviors for low latency.

1. **Tune client player settings:** Reduce initial buffer requirements, implement adaptive buffer management, and monitor latency metrics to optimize based on measurements.

1. **Balance latency requirements:** Evaluate trade-offs between latency, quality, and reliability for your specific use case.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMPERF03-BP01 Use a content delivery network and monitor your cache-hit-ratio](smperf03-bp01.html)
+ [SMPERF05-BP02 Select appropriate encoding settings for your content type and quality targets](smperf05-bp02.html)

**Related documents**
+ [How to Compete with Broadcast Latency Using Current Adaptive Bitrate Technologies](https://aws.amazon.com/blogs/media/how-to-compete-with-broadcast-latency-using-current-adaptive-bitrate-technologies-part-1/)
+ [How to configure a low-latency HLS workflow using AWS Media Services](https://aws.amazon.com/en/blogs/media/how-to-configure-a-low-latency-hls-workflow-using-aws-media-services/)

**Related services**
+ [AWS Elemental MediaLive](https://aws.amazon.com/medialive/)
+ [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)