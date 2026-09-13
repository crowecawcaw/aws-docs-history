

# Set up contextual metadata enrichment
<a name="cm-enrichment-setup"></a>

To enable contextual metadata enrichment, add the enrichment method `SCTE35_ELEMENTAL_INFERENCE_QUERY_PARAMS` to the `EnrichmentMethods` array in the channel's `InferenceSettings`. This method requires no additional settings—the Elemental Inference feed ARN is already configured at the `InferenceSettings` level.

## Using the AWS CLI
<a name="cm-enrichment-setup-cli"></a>

Use `update-channel` (or `create-channel`) to add the `EnrichmentMethods` field to the `InferenceSettings` section of the channel's JSON:

```
{
  "InferenceSettings": {
    "FeedArn": "arn:aws:elemental-inference:us-west-2:111122223333:feed/abcdef123",
    "EnrichmentMethods": ["SCTE35_ELEMENTAL_INFERENCE_QUERY_PARAMS"]
  }
}
```

This enrichment method requires no additional settings. The `FeedArn` field must already contain a value.

**Note**  
The feed referenced by `FeedArn` must have a `ContextualMetadataConfig` output. If it does not, use the Elemental Inference `update-feed` command to add one before enabling this enrichment method. For instructions on creating or updating the feed, see [Setting up Elemental Inference features for the first time](smart-crop-procedure-cli-create.md).

## Using the MediaLive console
<a name="cm-enrichment-setup-console"></a>

With the MediaLive console, you can configure both the Elemental Inference feed and the enrichment setting from the same page.

1. On the **Create channel** or **Edit channel** page, under **AWS Elemental Inference settings**, set **State** to **ENABLED**.

1. If the channel does not already have a feed, use the feed configuration panel on this page to create or select one. Make sure the feed has a **Contextual Metadata** output.

1. In the **Contextual metadata** section, choose **Enable contextual metadata enrichment**.

1. Save the channel.

**Note**  
Make sure that the feed you selected has a contextual metadata output so downstream systems can retrieve the enrichment data.