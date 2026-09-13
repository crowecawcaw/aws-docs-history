

# Modify or disable contextual metadata enrichment
<a name="cm-enrichment-modify"></a>

You can modify or disable contextual metadata enrichment using the AWS CLI or the MediaLive console.

## Using the AWS CLI
<a name="cm-enrichment-modify-cli"></a>

To disable contextual metadata enrichment, use `update-channel` to remove `SCTE35_ELEMENTAL_INFERENCE_QUERY_PARAMS` from the `EnrichmentMethods` array, set `EnrichmentMethods` to an empty array, or remove the `EnrichmentMethods` field from `InferenceSettings` entirely:

```
{
  "InferenceSettings": {
    "FeedArn": "arn:aws:elemental-inference:us-west-2:111122223333:feed/abcdef123",
    "EnrichmentMethods": []
  }
}
```

When the array is empty or the field is absent, MediaLive does not enrich SCTE-35 markers.

## Using the MediaLive console
<a name="cm-enrichment-modify-console"></a>

1. On the **Edit channel** page, under **AWS Elemental Inference settings**, go to the **Contextual metadata** section.

1. Clear the **Enable contextual metadata enrichment** option.

1. Save the channel.