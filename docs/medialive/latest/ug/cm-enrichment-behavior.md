

# How enrichment works
<a name="cm-enrichment-behavior"></a>

When contextual metadata enrichment is enabled, MediaLive monitors incoming SCTE-35 messages for cue-out markers. These include a `splice_insert` with `out_of_network_indicator = 1`, or a `time_signal` with a cue-out `segmentation_descriptor`. When MediaLive detects a cue-out marker, it appends an additional `segmentation_descriptor` to the descriptor loop. This descriptor uses the `format_identifier` value `"AWSE"` in its MPU UPID. It carries the Elemental Inference query parameters that downstream systems need.

MediaLive passes existing descriptors in the original SCTE-35 message through unchanged. MediaLive does not modify non-cue-out messages (such as cue-ins and `splice_null`).

For the full binary format specification, see [AWSE SCTE-35 format](awse-scte35-format.md).