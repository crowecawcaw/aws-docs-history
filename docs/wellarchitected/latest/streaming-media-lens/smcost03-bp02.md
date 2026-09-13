

# SMCOST03-BP02 Optimize encoder settings based on content type
<a name="smcost03-bp02"></a>

Traditional encoding allocates the same target bit rate regardless of content complexity. Low-complexity content receives more bits than it needs while complex content may not receive enough. Content-aware encoding analyzes source complexity and allocates bits accordingly, delivering equivalent perceptual quality at lower average bitrates. The bit rate reduction translates directly to proportional savings in CDN delivery cost for every viewer session.

**Desired outcome:**
+ You have encoding configurations that target consistent perceptual quality rather than fixed bit rate, resulting in lower average bitrates across your content catalog without quality regression.
+ You have ABR ladders optimized per content category so that each rendition delivers value to the viewers who select it, and no renditions exist that are never selected.
+ You have evaluated codec options against your audience device support and content volume to select the encoding format that minimizes total cost (encoding plus delivery).

**Common anti-patterns:**
+ Applying identical encoding settings to all content regardless of complexity, over-allocating bit rate to low-complexity content while under-allocating to complex content.
+ Using constant bit rate (CBR) encoding for all content types instead of variable bit rate modes that allocate bits based on scene complexity.
+ Maintaining a fixed ABR ladder across all content without analyzing whether viewers actually select every rendition or whether content complexity warrants the same bit rate at each rung.
+ Ignoring codec evolution because of deployment inertia, continuing to deliver all content in older codecs when newer options would reduce delivery cost for supported devices.

**Benefits of establishing this best practice:**
+ Average bit rate decreases across the content catalog because quality-based encoding uses only the bits necessary to achieve the target quality for each frame.
+ Delivery costs decrease proportionally because lower average bit rate means fewer bytes transferred per viewer session through the CDN.
+ Viewer experience remains consistent because the encoder targets quality rather than bit rate, adapting to content complexity automatically.
+ Storage costs decrease for VOD because encoded outputs at lower average bit rate consume less storage while maintaining the same quality.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Quality-Defined Variable bit rate (QVBR) is the primary lever for content-aware bit rate optimization in AWS media services. Unlike CBR, which maintains a fixed bit rate regardless of content, or basic VBR, which varies bit rate within a range without a quality target, QVBR targets a specific perceptual quality level and uses only the bit rate required to achieve it. For low-complexity content (news anchor, static presentation), QVBR may use 30-50% less bit rate than the configured maximum. For complex content (sports, action sequences), it uses bit rate up to the maximum ceiling. The net effect across a diverse content catalog is significantly lower average bit rate with consistent quality.

QVBR quality levels map to viewing contexts. Level 8-10 suits primary screens (television, large display) where quality expectations are highest. Level 7 suits PC and tablet viewing where screen size and viewing distance reduce quality sensitivity. Level 6 suits smartphone delivery where small screen size masks compression artifacts. Setting the max bit rate as a ceiling per output stops any single complex scene from consuming excessive bandwidth. The configured maximum should reflect the bit rate where your rate-quality analysis shows diminishing returns for that content category and viewing context.

ABR ladder design is the second optimization axis. A traditional fixed ladder allocates the same set of bit rate rungs to all content. Per-title encoding (for VOD) analyzes each piece of content and generates a custom ladder optimized for that content's complexity characteristics. A low-complexity talking-head video might need only three rungs where a complex action film needs six. For live encoding, per-title analysis isn't feasible in real-time, but content-type-specific templates achieve a similar effect. A sports template allocates higher bitrates per rung than a news template. Player analytics reveal which renditions viewers actually select. Renditions that analytics show are never or rarely selected represent wasted encoding compute and storage.

Codec selection is a total-cost decision, not just an encoding-cost decision. Newer codecs (H.265/HEVC, AV1) achieve 30-50% bit rate savings over H.264/AVC at equivalent quality but require more encoding compute per minute of output. H.265 typically requires 2-4x the compute of H.264. The trade-off calculation is: higher one-time encoding cost compared to lower ongoing per-viewer delivery cost. For content with large audiences, the delivery savings far exceed the encoding cost increase because encoding happens once but delivery happens for every viewer. For long-tail content with low viewership, the additional encoding cost may not be recovered through delivery savings.

Encoder optimization isn't a one-time configuration. Encoder software updates improve compression efficiency. A new encoder version may achieve the same VMAF score at 5-15% lower bit rate than the previous version. Re-evaluating encoding settings after updates, and re-encoding high-traffic catalog content with improved encoders, captures these gains. Track average bit rate per content category over time. It should decrease as optimizations are applied and encoder versions improve.

### Implementation steps
<a name="implementation-steps"></a>

1. **Configure QVBR rate control in encoding jobs:** Set rate control mode to QVBR in [AWS Elemental MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/video-encode-ratecontrol.html) or [AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/cbr-vbr-qvbr.html). Configure quality level appropriate for the viewing context (8-10 for primary screen, 7 for PC/tablet, 6 for mobile). Set max bit rate as a ceiling based on rate-quality curve saturation points from your quality assessment data.

1. **Optimize ABR ladder per content category:** For VOD, evaluate per-title encoding or automated ABR ladder generation that adapts rung count and bit rate allocation to content complexity. For live, create content-type-specific channel templates (sports, news, and entertainment) with bit rate allocations that match the complexity characteristics of each category. Review player analytics to identify and remove renditions that are never selected.

1. **Evaluate codec options against audience and volume:** Assess H.265/HEVC and AV1 device support across your audience using player telemetry data. Calculate total cost (encoding compute plus delivery) for each codec option at your content volume and audience size. Deploy newer codecs for content categories where the delivery savings exceed the additional encoding cost and where sufficient device support exists.

1. **Enable spatial and temporal adaptive quantization:** Activate adaptive quantization features in your encoder configuration for content with varying motion levels and detail density. These features allocate bits more efficiently within and across frames, reducing bit rate for static regions while preserving quality for complex regions.

1. **Track bit rate trends and re-evaluate after encoder updates:** Monitor average bit rate per content category over time using [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) metrics or encoding job metadata. After encoder software updates, re-encode representative test content and compare bit rate and quality against previous versions. Re-encode high-traffic catalog titles when newer encoder versions demonstrate meaningful compression efficiency improvements.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMCOST03-BP01 Implement comprehensive video quality assessment](smcost03-bp01.html)
+ [SMCOST01-BP02 Optimize content delivery using edge caching and just-in-time packaging](smcost01-bp02.html)

**Related documents**
+ [AWS Quality-Defined Variable Bitrate (QVBR)](https://aws.amazon.com/media/tech/quality-defined-variable-bitrate-qvbr/)
+ [Rate control mode in MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/video-encode-ratecontrol.html)
+ [CBR, VBR, and QVBR rate control in MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/cbr-vbr-qvbr.html)

**Related examples**
+ [Video on Demand on AWS](https://aws.amazon.com/solutions/implementations/video-on-demand-on-aws/)

**Related services**
+ [AWS Elemental MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/what-is.html)
+ [AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html)
+ [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)