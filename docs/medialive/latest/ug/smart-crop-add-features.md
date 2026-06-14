# Adding more Elemental Inference features

In a MediaLive channel where Elemental Inference features are already set up, you can add more Elemental Inference
features.

If you want to disable features rather than add them, see [Disabling some Elemental Inference features in a channel](smart-crop-disable-some.md "smart-crop-disable-some.md") or [Disabling all Elemental Inference features in a channel](smart-crop-disable-all.md "smart-crop-disable-all.md").

1. Make sure that you have room in the [enabled outputs quota](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas") for Elemental Inference. The list of quotas is sorted
   alphabetically. Look for quotas that don't start with "Request rate for".

Keep in mind that each feature that you enable in a channel results in one
Elemental Inference output. 2. **In MediaLive**, use `update-channel` to
edit the channel. Make changes as described in the following table.

| Feature to add  | Action                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Event clipping  | There are no changes to make in the channel. But you must<br>make a note of the value in `feedArn` in<br>`InferenceSettings`.                                                                                                                                                                                                                                                                             |
| Smart crop      | You can add smart crop for the first time or you can set up<br>more video encodes for smart crop. In both cases, insert<br>`Width`, `Height`, and<br>`ScalingBehavior` in the applicable video<br>encodes (video descriptions), as described and illustrated<br>in [Setting up Elemental Inference features for the first time](smart-crop-procedure-cli-create.md "smart-crop-procedure-cli-create.md"). |
| Smart Subtitles | Add `SmartSubtitleSourceSettings` caption<br>selectors to input attachments, create caption descriptions<br>referencing those selectors with a TTML or WebVTT destination,<br>and add a captions-only output, as described in [Setting up Elemental Inference features for the first time](smart-crop-procedure-cli-create.md "smart-crop-procedure-cli-create.md").                                      |

3. When you save the channel, MediaLive performs the following actions:

   - If you are adding smart crop for the first time, MediaLive updates the
     feed in Elemental Inference to create a crop output in the feed.

4. **In the Elemental Inference**, use `update-feed`
   to update the feed. Make changes as described in the following table.

| Feature to add                            | Action                                                                                                                                                                                               |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add event clipping                        | Create one output of type<br>`ClippingConfig`.                                                                                                                                                       |
| Add smart crop for the first time         | There are no changes to make. Don't include an output in the<br>feed. MediaLive won't use any feed you create, but any feed you<br>create will count towards one or more Elemental Inference quotas. |
| Extend smart crop to more channel outputs | There are no changes to make.                                                                                                                                                                        |
| Add Smart Subtitles                       | Use `update-feed` to add one output of type<br>`SubtitlingConfig` with the appropriate<br>`language` setting. Or if a subtitling output<br>already exists, there are no changes to make.             |

5. When you are ready to start the channel, use `StartChannel` in
   MediaLive.
