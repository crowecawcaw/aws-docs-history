

# SMPERF02-BP01 Start with the highest quality source reasonably obtainable
<a name="smperf02-bp01"></a>

Acquire the highest quality media source available so downstream

transcoding has maximum headroom.

**Desired outcome:**
+ You have source content acquired at the highest bit rate, resolution, and color space that is reasonably obtainable, giving downstream transcoding maximum headroom.
+ Your ingest pipeline validates source quality automatically and flags non-conforming content before it enters production workflows.
+ Your source masters are preserved in redundant storage so future format or quality upgrades don't require re-acquisition.

**Common anti-patterns:**
+ Accepting whatever bit rate or codec the content provider delivers without specifying quality requirements in contracts.
+ Storing only mezzanine sources and discarding original camera or source files, removing future re-encoding options.
+ Skipping quality validation on ingest, so corrupted or low-quality sources only surface after production encoding is complete.

**Benefits of establishing this best practice:**
+ Higher perceived quality in final renditions because the transcoder starts from better input
+ Better compression efficiency since codecs have cleaner signal to work with
+ Ability to re-encode for future formats without re-acquiring source material
+ Fewer visible artifacts compounding through multi-generation encoding
+ Room to support HDR and wider color spaces when device adoption grows

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

The quality of your source material sets a hard upper bound on what any downstream encode can produce. Every lossy encoding stage adds generation loss. Small artifacts accumulate because the codec can't know what the original looked like, only what the previous version looked like. A 10 Mbps H.264 source isn't the same as a lossless source file. Encode both to the same 5 Mbps High Efficiency Video Coding (HEVC) rendition, and the difference still shows. It becomes visible the first time someone re-encodes for a new format or a new codec. Bit rate is only one dimension. Color space and bit depth have the same constraint. Information that isn't captured at ingest can't be recovered later. A clip shot in Rec. 709 can be delivered in wider Rec. 2020 containers, but the pixels stay inside the narrower gamut. A 10-bit high dynamic range (HDR) source can be down-converted to 8-bit standard dynamic range (SDR) for legacy devices. An 8-bit SDR source can't be upgraded to HDR by any transcoder.

### Implementation steps
<a name="implementation-steps"></a>

1. **Define source content requirements:** Specify requirements for:
+ Resolution
+ Bit rate
+ Codec
+ Color space

1. **Negotiate with content providers:** Secure the highest quality sources available.

1. **Implement source quality validation:** Establish verification processes for incoming content.

1. **Establish source media storage strategy:** Configure appropriate redundancy for source content.

1. **Create backup and disaster recovery plans:** Protect source content against loss with redundant storage and cross-region replication.

1. **Monitor source quality metrics:** Establish quality baselines for ongoing measurement.

1. **Implement automated quality checks:** Set up automated validation for incoming content.

## Resources
<a name="resources"></a>

**Related documents**
+ [AWS Elemental MediaConnect User Guide](https://docs.aws.amazon.com/mediaconnect/latest/ug/what-is.html)
+ [AWS Elemental MediaLive User Guide - Inputs](https://docs.aws.amazon.com/medialive/latest/ug/inputs.html)
+ [Amazon S3 Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

**Related services**
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [AWS Elemental MediaConnect](https://aws.amazon.com/mediaconnect/)
+ [AWS Elemental MediaLive](https://aws.amazon.com/medialive/)