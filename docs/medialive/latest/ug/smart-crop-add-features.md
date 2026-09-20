

# Adding more Elemental Inference features
<a name="smart-crop-add-features"></a>

In a MediaLive channel where Elemental Inference features are already set up, you can add more Elemental Inference features.

If you want to disable features rather than add them, see [Disabling some Elemental Inference features in a channel](smart-crop-disable-some.md) or [Disabling all Elemental Inference features in a channel](smart-crop-disable-all.md).

1. Make sure that you have room in the [enabled outputs quota](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas) for Elemental Inference. The list of quotas is sorted alphabetically. Look for quotas that don't start with "Request rate for".

   Keep in mind that each feature that you enable in a channel results in one Elemental Inference output.

1. **In MediaLive**, use `update-channel` to edit the channel. Make changes as described in the following table.


<table>
<thead>
  <tr><th>Feature to add</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td>Event clipping</td><td>There are no changes to make in the channel. But you must make a note of the value in <code>feedArn</code> in <code>InferenceSettings</code>.</td></tr>
  <tr><td>Smart crop</td><td>You can add smart crop for the first time or you can set up more video encodes for smart crop. In both cases, insert <code>Width</code>, <code>Height</code>, and <code>ScalingBehavior</code> in the applicable video encodes (video descriptions), as described and illustrated in <a href="smart-crop-procedure-cli-create.md">Setting up Elemental Inference features for the first time</a>.</td></tr>
  <tr><td>Smart Subtitles</td><td>Add <code>SmartSubtitleSourceSettings</code> caption selectors to input attachments, create caption descriptions referencing those selectors with a TTML or WebVTT destination, and add a captions-only output, as described in <a href="smart-crop-procedure-cli-create.md">Setting up Elemental Inference features for the first time</a>.</td></tr>
  <tr><td>Contextual metadata enrichment</td><td>Add <code>SCTE35_ELEMENTAL_INFERENCE_QUERY_PARAMS</code> to the <code>EnrichmentMethods</code> array in <code>InferenceSettings</code>.</td></tr>
</tbody>
</table>


1. When you save the channel, MediaLive performs the following actions:
   + If you are adding smart crop for the first time, MediaLive updates the feed in Elemental Inference to create a crop output in the feed.

1. **In the Elemental Inference**, use `update-feed` to update the feed. Make changes as described in the following table.


<table>
<thead>
  <tr><th>Feature to add</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td>Add event clipping</td><td>Create one output of type <code>ClippingConfig</code>.</td></tr>
  <tr><td>Add smart crop for the first time</td><td>There are no changes to make. Don't include an output in the feed. MediaLive won't use any feed you create, but any feed you create will count towards one or more Elemental Inference quotas.</td></tr>
  <tr><td>Extend smart crop to more channel outputs</td><td>There are no changes to make.</td></tr>
  <tr><td>Add Smart Subtitles</td><td>Use <code>update-feed</code> to add one output of type <code>SubtitlingConfig</code> with the appropriate <code>language</code> setting. Or if a subtitling output already exists, there are no changes to make.</td></tr>
  <tr><td>Add contextual metadata enrichment</td><td>Use <code>update-feed</code> to add one output of type <code>ContextualMetadataConfig</code>. Or if a contextual metadata output already exists, there are no changes to make.</td></tr>
</tbody>
</table>


1. When you are ready to start the channel, use `StartChannel` in MediaLive.