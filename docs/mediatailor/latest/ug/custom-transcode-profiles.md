

# Custom transcode profiles
<a name="custom-transcode-profiles"></a>

A custom transcode profile (CTP) is an explicitly authored AWS Elemental MediaConvert job configuration that you register with MediaTailor. When a CTP is associated with a MediaTailor configuration, MediaTailor uses your defined settings to transcode every ad, bumper, and slate, giving you precise control over codecs, bitrates, audio normalization levels, segment lengths, PID values, sample rates, and more. Because a CTP completely overrides dynamic transcoding, you must explicitly configure all features you need, including trickplay features (I-frame manifests, thumbnails, and image streams), within the profile.

A CTP is designed to match a specific origin configuration. If the source content differs from the configuration the CTP was originally created for, ads might fail to transcode properly because of a `NO_VARIANT_MATCH` error. This occurs when the CTP outputs do not align with the variants present in the origin manifest. This applies to both live and VOD workflows. For example, VOD libraries that contain content from different sources or encoded with different encoding profiles (such as varying resolutions, bitrates, codecs, or segment lengths) might produce `NO_VARIANT_MATCH` errors if the CTP does not account for all variant combinations present across the library. If you need a single CTP to support multiple origins or a VOD library with mixed encoding profiles, a superset CTP can be created that encompasses the variants of all target origins. However, superset CTPs are subject to a hard limit of 36 video variants, which constrains how many origins or variant combinations can be accommodated with a single profile.

**Important**  
You must keep your CTP in sync any time you make changes to your encoder settings or take on new sources of VOD content. Failure to do so will result in `NO_VARIANT_MATCH` errors and ad transcoding failures. This includes changes such as adding or removing resolutions, adjusting bitrates, changing codecs, modifying segment lengths, or onboarding VOD content from new providers with different encoding profiles.

When updating your CTP, be aware of the following behavior.
+ Updating an existing CTP applies the new settings only to newly transcoded ads. Ads that were previously transcoded under the old CTP settings will not be retranscoded.
+ Creating a new CTP and associating it with your MediaTailor configuration will prompt MediaTailor to retranscode all ads using the new profile, ensuring full consistency across your ad inventory.

For this reason, when your encoder settings change or you onboard new content sources, as a best practice, create a new CTP rather than updating the existing one to ensure all ads, including previously transcoded ads, reflect the updated settings.

## When to use a custom transcode profile
<a name="ctp-when-to-use"></a>

Use a custom transcode profile when your workflows require one or more of the following.
+ A custom audio normalization target other than the MediaTailor default of -24 LKFS
+ Non-integer segment lengths (for example, 1.92 or 3.84)
+ Dolby Vision audio configurations
+ Specific PMT, video, or audio PID values required by downstream systems or players
+ Custom audio sample rates (for example, 44.1 kHz)
+ Bitrate matching beyond the 5% threshold supported by dynamic transcoding with a configuration flag
+ Custom pixel aspect ratios (PAR) – for example, 1:1 for square pixels or 40:33 for D1/DV NTSC widescreen
+ Specific named audio or subtitle tracks

## Getting started with custom transcode profiles
<a name="ctp-getting-started"></a>

Access to the MediaTailor Transcoding API, which is required to register a CTP, is restricted to allowlisted accounts. To get started, contact AWS Support using one of the following options.
+ **Request allowlist access** – To create and manage your own CTPs, contact AWS Support to request that your account be added to the allowlist. After your account is added to the allowlist, you have access to the Transcoding API to register and manage profiles in any AWS region where you have an existing MediaTailor configuration.
+ **Request CTP creation by AWS Support** – To have AWS Support generate and register a CTP on your behalf, contact AWS Support with a non-DRM-protected origin endpoint URL that MediaTailor can access. AWS Support will use this endpoint to analyze your origin configuration and generate an appropriate CTP for your account.

## Dynamic transcoding vs. custom transcode profiles
<a name="ctp-comparison"></a>

Use the following table to determine the right approach for your workflow.


**Dynamic transcoding vs. custom transcode profile comparison**  

| Consideration | Dynamic transcoding | Custom transcode profile | 
| --- | --- | --- | 
| Setup effort | None | Manually authored AWS Elemental MediaConvert job configuration | 
| Trickplay support (HLS and DASH) | Automatic | Must be explicitly configured in CTP | 
| Compact DASH manifests | Automatic | Must be explicitly configured in CTP | 
| CMAF format support | Automatic | Must be explicitly configured in CTP | 
| Origin change handling | Automatic | Manual CTP update required | 
| Multi-region complexity | None | Must be registered per region | 
| Audio normalization | -24 LKFS (default) | Fully configurable | 
| Bitrate matching | Up to 5% rounding via enableBitrateRounding flag (contact AWS Support to enable) | Explicitly configured in CTP to match origin bitrates | 
| Non-integer segment lengths | 2-second default; non-integer segment lengths not supported (contact AWS Support to enable calculateSegmentLength for automatic integer segment length calculation) | You must manually configure segment length to match origin | 
| Custom PID values | Not supported | Supported | 
| Dolby Vision audio | Not supported | Supported | 
| Custom audio sample rates | Not supported | Supported | 
| Multi-origin support | Automatic | Superset CTP required; limited to 36 video variants | 
| MediaTailor improvements | Automatic | Manual CTP updates required | 
| Best suited for | Standard codec matching, common bitrate profiles, trickplay, compact DASH | Specialized encoding requirements not met by dynamic transcoding | 