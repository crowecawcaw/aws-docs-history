

# Dynamic transcoding
<a name="dynamic-transcoding"></a>

Dynamic transcoding is the default ad transcoding behavior in MediaTailor. When an ad, bumper, or slate needs to be transcoded, MediaTailor automatically inspects the origin manifest and derives transcoding settings at runtime, without any configuration on your part.

## What dynamic transcoding handles
<a name="dynamic-transcoding-handles"></a>

Dynamic transcoding automatically handles the following for HLS and DASH workflows.
+ **Standard codec matching** – MediaTailor matches the codec profile of the origin stream. Note that codec level matching is not guaranteed.
+ **Audio normalization** – MediaTailor automatically applies audio normalization to transcoded ads using a default target level of -24 LKFS. This ensures that ad audio levels are consistent with your origin content without any additional configuration. If your workflow requires a custom audio normalization target other than the default of -24 LKFS, a custom transcode profile is required.
+ **Standard segment length matching** – By default, MediaTailor transcodes ads using 2-second segments. If your player requires segment length matching, you can enable the `calculateSegmentLength` flag, which causes MediaTailor to automatically calculate the correct segment length by analyzing the first 10 segments from the origin and selecting the most common duration as the segment length. This flag is disabled by default and must be enabled by AWS Support. Contact AWS Support to request activation of `calculateSegmentLength` for your account or specific configurations.
+ **Standard WebVTT subtitles** – For HLS workflows, MediaTailor preserves subtitle group references in the personalized multivariant playlist when WebVTT subtitles are present in the origin manifest. During ad segments, MediaTailor inserts blank WebVTT segments to maintain subtitle track continuity, because ad creatives typically do not include subtitle tracks. For DASH workflows, MediaTailor requires that subtitle adaptation sets in the origin manifest be segmented (like video and audio). Ad periods constructed by MediaTailor only contain the adaptation sets provided by the ad creative; because ad creatives typically do not include subtitle tracks, the ad periods will not contain a subtitle AdaptationSet. Content periods retain their subtitle adaptation sets as normal.
+ **CMAF format support** – MediaTailor detects whether an HLS origin stream uses CMAF (fMP4) segments or standard TS segments and transcodes ads to match accordingly. For DASH, CMAF packaging is supported transparently, as DASH inherently uses ISO-BMFF (fMP4) as its container format. No additional configuration is required for either protocol.
**Note**  
MediaTailor does not support HLS streams using HVC1 (HEVC) as the codec with TS segments. Per HLS Authoring Specification for Apple Devices, section 1.5, the container format for HEVC video must be fMP4. HLS streams using HEVC must therefore use CMAF with fragmented MP4 segments.
+ **Trickplay personalization** – MediaTailor automatically transcodes advertisements with trickplay variants and associated image streams (including I-frame manifests, thumbnails, and image streams) for both HLS and DASH, matching origin content specifications. A custom transcode profile is no longer required for this capability.
+ **Compact DASH manifests** – MediaTailor automatically supports compact DASH manifests, which elevate the SegmentTemplate element from individual Representation elements to the AdaptationSet level, reducing overall manifest size and improving delivery efficiency. A custom transcode profile is no longer required for this capability.

## When dynamic transcoding might not be sufficient
<a name="dynamic-transcoding-limitations"></a>

Dynamic transcoding handles the majority of ad transcoding scenarios. However, there are some cases where additional configuration or a custom transcode profile might be needed.
+ **Bitrate matching** – Dynamic transcoding does not guarantee precise bitrate matching by default. If your workflow requires ad bitrates to closely align with origin bitrates, you can enable the `enableBitrateRounding` flag, which allows for up to 5% bitrate rounding to better match origin values. This flag must be enabled by AWS Support. Contact AWS Support to request activation of `enableBitrateRounding` for your account or specific configurations. If your workflow requires bitrate matching beyond 5%, a custom transcode profile is required.
+ A custom audio normalization target other than the MediaTailor default of -24 LKFS
+ Non-integer segment lengths (for example, 1.92s or 3.84s)
+ Dolby Vision audio
+ Specific PMT, video, or audio PID values required by downstream systems or players
+ Custom audio sample rates (for example, 44.1 kHz)
+ Custom pixel aspect ratios (PAR) – for example, 1:1 for square pixels or 40:33 for D1/DV NTSC widescreen
+ Specific named audio tracks or subtitle tracks