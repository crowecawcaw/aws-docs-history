

# Contextual metadata enrichment
<a name="elemental-inference-cm-enrichment"></a>

In an AWS Elemental MediaLive channel, you can enable contextual metadata enrichment. This feature embeds AWS Elemental Inference query parameters into outgoing SCTE-35 cue-out markers. When enabled, MediaLive appends additional segmentation descriptors to SCTE-35 cue-out messages. Downstream consumers can then query Elemental Inference for contextual metadata. Examples of downstream consumers include ad-decision systems such as AWS Elemental MediaTailor.

**Important**  
The PTS and timebase values in these splice descriptors might differ from the PTS format that your output uses. Downstream systems must use these values only to query the Elemental Inference `GetMetadata` API.

For the binary format of the enrichment descriptors, see [AWSE SCTE-35 format](awse-scte35-format.md).

**Topics**
+ [Get ready](cm-enrichment-get-ready.md)
+ [Set up contextual metadata enrichment](cm-enrichment-setup.md)
+ [Modify or disable contextual metadata enrichment](cm-enrichment-modify.md)
+ [How enrichment works](cm-enrichment-behavior.md)
+ [Verify that enrichment is working](cm-enrichment-verify.md)