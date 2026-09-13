

# Verify that enrichment is working
<a name="cm-enrichment-verify"></a>

After you start the channel, you can verify that contextual metadata enrichment is working. Capture an output stream and inspect the SCTE-35 markers.

1. Capture a segment of the channel output that contains an ad break (cue-out).

1. Use a tool such as `tsduck` or a similar SCTE-35 parser to decode the SCTE-35 `splice_info_section` from the captured output.

1. Verify that the cue-out markers contain an additional `segmentation_descriptor` with `segmentation_type_id = 0x01` (Content Identification) and a `segmentation_upid_type = 0x0C` (MPU). The UPID carries the Elemental Inference query parameters.

For the complete binary format of the enrichment descriptor, see [AWSE SCTE-35 format](awse-scte35-format.md).