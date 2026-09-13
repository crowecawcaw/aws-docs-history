

# SMPERF05-BP02 Select appropriate encoding settings for your content type and quality targets
<a name="smperf05-bp02"></a>

Choose encoding parameters matched to your content characteristics

(sports, animation, and talking heads) and validate output quality with objective metrics.

**Desired outcome:**
+ You have encoder settings chosen against content characteristics (sports, animation, and talking heads) rather than applied uniformly across the library.
+ Your codec and preset selections are validated against the target device fleet, so efficiency gains from newer codecs reach actual viewers.
+ You measure output quality with objective metrics (Video Multimethod Assessment Fusion (VMAF), peak signal-to-noise ratio (PSNR)) or subjective assessment at each rendition, not just average bit rate.

**Common anti-patterns:**
+ Using encoder presets without validating them against representative content (sports, animation, and film) that exposes different trade-offs.
+ Optimizing purely for average bit rate without measuring perceived quality through VMAF, PSNR, or subjective assessment.
+ Re-encoding previously encoded, lossy content without going back to the highest-quality source, compounding quality loss.

**Benefits of establishing this best practice:**
+ Higher VMAF scores at the same bit rate by tuning to content complexity
+ Lower bandwidth cost because content-aware settings avoid wasted bits on low-complexity scenes
+ Reduced encoding compute cost from selecting appropriate presets per content type
+ Consistent perceptual quality across renditions rather than consistent bit rate
+ Smaller stored file sizes for the VOD library without visible quality loss

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Encoding quality is determined by rate-distortion performance, not bit rate alone. Two files at the same bit rate can deliver different perceived quality. Codec, preset, content complexity, and bit-allocation strategy all matter. Because of this, you need to measure output quality rather than relying on bit rate as a proxy. VMAF and PSNR give objective scores per frame and per rendition. Subjective review catches the cases where the metrics disagree with human perception. The optimization game is also not the same for live and video on demand (VOD). VOD tolerates multi-pass analysis and content-aware encoding, which let the encoder rebalance bits across the whole title. Live runs single-pass with hard real-time deadlines. The knobs are group of pictures (GOP) length, lookahead, and scene-change handling, and each setting also affects the latency budget covered in low-latency delivery.

### Implementation steps
<a name="implementation-steps"></a>

1. **Analyze your content types and characteristics:** Understand the nature of your video content to inform encoding decisions.

1. **Select appropriate codecs based on use case and device support:** Use H.265/High Efficiency Video Coding (HEVC) for contribution feeds to optimize bandwidth, H.264/Advanced Video Coding (AVC) for broad device compatibility, and AOMedia Video 1 (AV1) for higher compression efficiency (20-30% additional savings over HEVC).

1. **Configure encoder settings based on content type:** Sports and action content requires higher bitrates and faster encoding presets, talking heads benefit from lower bitrates and quality-focused presets, and animation is optimized for flat colors and sharp edges.

1. **Use content-aware encoding features in AWS Elemental MediaConvert:** Use automated quality optimization capabilities.

1. **Implement quality testing and validation processes:** Verify encoding output meets quality standards.

1. **Monitor encoding efficiency and adjust settings based on results:** Continuously optimize encoder configurations.

1. **Consider using machine learning-based encoding optimization:** Explore ML-driven approaches for further efficiency gains.

1. **Plan codec migration strategy:** Consider device support timelines when planning codec transitions.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMPERF05-BP01 Optimize the number of adaptive bitrate renditions for your workload](smperf05-bp01.html)
+ [SMPERF06-BP01 Optimize processing, origination, delivery, and client for low latency](smperf06-bp01.html)

**Related documents**
+ [HLS Authoring Specification for Apple
+ [AWS Elemental MediaConvert User

**Related services**
+ [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)
+ [AWS Elemental MediaLive](https://aws.amazon.com/medialive/)