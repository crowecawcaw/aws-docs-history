

# Disabling some Elemental Inference features in a channel
<a name="smart-crop-disable-some"></a>

Follow this procedure if you want to disable some Elemental Inference features in the MediaLive channel, but you want to keep at least one feature. For example:
+ Keep smart crop enabled in at least one output. 
+ Disable smart crop but keep event clipping enabled.

In this procedure, you disable a feature in the relevant MediaLive channel outputs. And you disable the output for that feature in the Elemental Inference feed.

**Topics**
+ [Make changes in MediaLive](#smart-crop-disable-some-eml)
+ [Make changes in Elemental Inference](#smart-crop-disable-some-inference)
+ [Result of disabling some features](#smart-crop-disable-result-partial)
+ [Re-enabling Elemental Inference features](#smart-crop-disable-partial-reenable)

## Make changes in MediaLive
<a name="smart-crop-disable-some-eml"></a>

Use `update-channel` to make changes in the JSON for the MediaLive channel.


|  If you want to disable...  |  Action  | 
| --- | --- | 
| Event clipping | There are no changes to make in the channel JSON. | 
| Smart crop in one or more outputs |  1.  Identify the video encodes (video descriptions) for the target outputs where you want to disable smart crop. For example, one target output might be the video encode (video description) named `high_resolution` in an output named `output_A` in the output group named `My_outputgroup`. <br />2.  In the JSON for each video description that you identified, change these parameters:   `Width` and `Height`: Set to values that are suitable when there is no Elemental Inference features occurring.   `ScalingBehavior`: Set to a value other than `SMART_CROP`.    <br />Smart crop is now disabled in these outputs.   | 
| Smart Subtitles |  1.  Remove the `SmartSubtitleSourceSettings` caption selectors from all input attachments. <br />2.  Remove or update any caption descriptions that reference those selectors. <br />3.  Remove the captions-only output (WebVTT or TTML) if it is no longer needed.   | 

See [Setting up Elemental Inference features for the first time](smart-crop-procedure-cli-create.md) for an example of the JSON as it appears *before *you make these changes.

**Note**  
Don't touch the `feedArn` parameter in the `InferenceSettings` section of the JSON.

## Make changes in Elemental Inference
<a name="smart-crop-disable-some-inference"></a>

Make changes in Elemental Inference as described in the following table.


|  Action  |  Action  | 
| --- | --- | 
| To disable event clipping | Use `UpdateFeed` to change the status parameter of the `OutputConfig` that is of type `ClippingConfig`. Change the status from `ENABLED` to `DISABLED`. | 
| To disable smart crop in all video outputs | Use UpdateFeed to change the status parameter of the OutputConfig that is of type CropConfig. Change the status from ENABLED to DISABLED.  | 
| To disable smart crop in some video outputs | There are no changes to make. Leave the status of CropConfig as ENABLED. | 
| To disable Smart Subtitles | Use UpdateFeed to change the status parameter of the OutputConfig that is of type SubtitlingConfig. Change the status from ENABLED to DISABLED. | 

## Result of disabling some features
<a name="smart-crop-disable-result-partial"></a>

Disabling some features changes the behavior of MediaLive and Elemental Inference as follows:
+ MediaLive continues to send the source video to Elemental Inference because there is still a `feedArn` parameter in the channel.
+ Elemental Inference continues to produce metadata for outputs that are enabled (which means that corresponding feature is enabled). But it stops producing metadata for outputs that are disabled.

  When an output is disabled, the following rules apply: 
  + You don't incur charges for a DISABLED output.
  + But you can still read the existing metadata in that output for the next 24 hours. After that time, the output remains disabled, but its metadata is deleted.

For example, if you previously had both event clipping and smart crop enabled, but you then disable event clipping, MediaLive continues to send the source video. Elemental Inference continues to produce event clipping metadata but it stops producing smart cropping metadata.

## Re-enabling Elemental Inference features
<a name="smart-crop-disable-partial-reenable"></a>

If a MediaLive channel currently has at least one Elemental Inference feature enabled, you can re-enable features that you previously disabled). Follow the procedure [Adding more Elemental Inference features](smart-crop-add-features.md), with this difference: instead of adding `OutputConfig` items, set the status of existing items to `ENABLED`.