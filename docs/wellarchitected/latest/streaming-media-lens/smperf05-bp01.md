

# SMPERF05-BP01 Optimize the number of adaptive bit rate renditions for your workload
<a name="smperf05-bp01"></a>

Size your adaptive bit rate (ABR) ladder to your target devices, network

conditions, and content type rather than copying a default template.

**Desired outcome:**
+ You have an ABR ladder sized to your target devices, network conditions, and content type, not copied from a default template.
+ Your renditions are spaced 1.5–2× apart so players jump meaningfully between renditions without oscillating.
+ You review and retune the ladder regularly as codecs, devices, and observed viewer bandwidth change.

**Common anti-patterns:**
+ Copying a default ABR ladder from a tutorial without adapting it to the content's bit rate characteristics or target devices.
+ Packing too many renditions at small bit rate increments, causing players to switch frequently and visibly.
+ Reusing the same rendition set for H.264, High Efficiency Video Coding (HEVC), and AOMedia Video 1 (AV1) assets instead of taking advantage of newer codecs' better quality at lower bitrates.

**Benefits of establishing this best practice:**
+ Viewers land on the right rendition faster because the ladder fits real device capabilities
+ Lower encoding and storage cost from dropping renditions no one selects
+ Fewer visible quality switches because adequate spacing reduces player oscillation
+ Better bandwidth utilization since renditions map to observed network conditions
+ Room to add codec-specific ladders (HEVC, AV1) without inflating the total rendition count

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

The ABR ladder feeds the player's rendition-selection algorithm. Players watch measured throughput and buffer level, then pick the rendition whose bit rate fits with margin. If two adjacent renditions are too close together, the player oscillates between them as throughput fluctuates, and viewers see visible quality flips. The 1.5–2x spacing rule exists for a functional reason. It leaves enough throughput headroom for the player to commit to a choice. Below that spacing, any gain from extra renditions is eaten by switching behavior.

A single ladder also has to carry the whole device mix. A 4K TV wastes nothing on 240p renditions, and a phone never reaches the 20 Mbps top rendition, but both are watching the same stream. Removing low renditions to save encoding cost hurts mobile startup time, because the player needs a fast first segment to begin playback. Removing high renditions caps what connected-TV viewers can see. Per-device manifests can narrow the ladder per device type but add complexity most teams should avoid until single-ladder economics demand it.

### Implementation steps
<a name="implementation-steps"></a>

1. **Analyze your target audience and device environment:** Understand the devices and network conditions your viewers use.

1. **Determine maximum bit rate:** Base this on your highest quality requirements.

1. **Create ABR ladder with 1.5-2x bit rate steps between renditions:** Space renditions so quality jumps are visible without causing excessive switching.

1. **Consider specific requirements:** Connected TV needs high-resolution renditions, while mobile benefits from lower resolution options.

1. **Implement Auto ABR with AWS Elemental MediaConvert:** Use content-aware optimization for efficient encoding.

1. **Consider codec-specific ladder optimization:** Tailor ladders for HEVC and AV1 codec characteristics.

1. **Test ABR ladder performance across different devices and networks:** Validate the ladder works well across your target environment.

1. **Monitor client switching behavior and adjust ladder as needed:** Track rendition switches and optimize spacing.

1. **Regularly review and optimize based on usage patterns:** Continuously refine the ladder based on real-world data.

## Resources
<a name="resources"></a>

**Related documents**
+ [AWS Elemental MediaConvert User Guide: Automated ABR](https://docs.aws.amazon.com/mediaconvert/latest/ug/auto-abr.html)
+ [Creating a job with automated ABR](https://docs.aws.amazon.com/mediaconvert/latest/ug/creating-an-automated-abr-stack.html)
+ [Apple HLS Authoring Specification for Apple Devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices)

**Related services**
+ [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/)
+ [AWS Elemental MediaLive](https://aws.amazon.com/medialive/)