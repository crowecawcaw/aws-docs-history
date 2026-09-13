

# Dynamic Multiview: Requirements and Limitations
<a name="dynamic-multiview-requirements"></a>

AWS Elemental MediaLive requires specific configuration to produce outputs that are Dynamic Multiview compatible. This section describes the primary ones, but MediaLive also includes validation errors returned when creating or updating a channel that helpfully indicate configuration mistakes. The multiview specific validations are activated by setting the `outputUsage` field under `MediaPackageV2DestinationSettings` to indicate one or more multiview usage types (for example, `MULTIVIEW_EQUAL_SIZE_VIEW`, `MULTIVIEW_PRIMARY_VIEW`, or `MULTIVIEW_SECONDARY_VIEW`).

## Destination and container
<a name="dynamic-multiview-req-destination"></a>

**MediaPackage V2 is required.** Multiview outputs must be delivered to a MediaPackage V2 channel. MediaPackage V1 destinations do not support multiview.

**CMAF Ingest outputs are required.** The outputs in the multiview output group must be CMAF Ingest outputs. HLS outputs to MediaPackage V2 are not sufficient for multiview.

**All source feeds must reach the same MediaPackage channel group.** A multiview can only be assembled from channels within one channel group. Each source feed is a separate MediaPackage channel in that group, fed by a separate MediaLive channel.

## Codec
<a name="dynamic-multiview-req-codec"></a>

Every video output that participates in multiview must be encoded as H.264 (AVC) or H.265 (HEVC). H.264 and H.265 can co-exist in the same multiview output group, but MediaPackage will only create multiview by combining views encoded with the same codec type.

## Group-wide participation
<a name="dynamic-multiview-req-participation"></a>

If any video-carrying output in the output group declares a multiview `outputUsage`, then **every** video-carrying output in that group must also declare one. Audio-only and caption-only outputs are exempt. If you need standalone, single-view video outputs from the same channel — a rendition that is not intended for multiview — put them in a separate output group.

## Encoder settings
<a name="dynamic-multiview-req-encoder"></a>

Participating video descriptions must use a specific set of encoder settings, and certain settings must match across all participating outputs of the same codec.

See [Dynamic Multiview: MediaLive Configuration Reference](dynamic-multiview-reference.md) for the full per-codec tables.

## SCTE-35
<a name="dynamic-multiview-req-scte35"></a>

The output group's SCTE-35 type must be `NONE` or `SCTE_35_WITHOUT_IDR`. `SCTE_35_WITHOUT_SEGMENTATION` is rejected, because it inserts an IDR frame at non-segment boundaries which is not multiview compatible.

## Frame rate
<a name="dynamic-multiview-req-framerate"></a>

Frame rate must be explicitly specified on participating outputs — frame rate cannot be initialized from the source as it can be for some encodes. Only encodes with the same frame rates can be combined by MediaPackage into a multiview output.

## Dimensions
<a name="dynamic-multiview-req-dimensions"></a>
+ H.264 / AVC: width and height must each be divisible by 16.
+ H.265 / HEVC: width and height must each be divisible by 32.
+ A secondary rendition's width and height must each be exactly half its primary's.