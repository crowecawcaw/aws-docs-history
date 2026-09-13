

# Get ready
<a name="cm-enrichment-get-ready"></a>

**Important**  
Turn on the Elemental Inference feed output and the channel-level enrichment configuration together. If you create a feed with a `ContextualMetadataConfig` output without enabling `EnrichmentMethods` on the channel (or vice versa), the feature does not work as expected.  
The feed must also be associated with your channel.

## AWS Elemental Inference feed requirements
<a name="cm-enrichment-get-ready-feed"></a>

This feature requires an AWS Elemental Inference feed with a `ContextualMetadataConfig` output. The feed must be associated with the MediaLive channel. If the channel already has a feed for another Elemental Inference feature (such as smart crop or event clipping), add a contextual metadata output to the existing feed. Otherwise, create a new feed with a contextual metadata output.

For instructions on setting up the feed, see [Setting up Elemental Inference features for the first time](smart-crop-procedure-cli-create.md).

## Output requirements
<a name="cm-enrichment-get-ready-output"></a>

This feature is supported on channels using output groups that support SCTE-35 passthrough. For each output where you want enriched markers to appear, enable SCTE-35 passthrough; some output types require this explicit configuration.

For more information about supported output types and how SCTE-35 processing applies to each, see [Supported features by output type](processing-applicability-by-output-type.md).