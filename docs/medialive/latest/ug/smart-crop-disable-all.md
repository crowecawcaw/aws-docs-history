

# Disabling all Elemental Inference features in a channel
<a name="smart-crop-disable-all"></a>

Follow this procedure to disable all Elemental Inference features in a MediaLive channel. 

In this procedure, you disable a feature in the relevant MediaLive channel outputs. And you disable the output for that feature in the Elemental Inference feed.

**Topics**
+ [Make changes in MediaLive](#smart-crop-disable-all-eml)
+ [Result of changes to the MediaLive channel](#smart-crop-disable-all-result-global)

## Make changes in MediaLive
<a name="smart-crop-disable-all-eml"></a>

Use `update-channel` to make changes in the MediaLive channel.

1. In the `InferenceSettings` section of the JSON, remove the `feedARN` line.

1. Make changes to remove the special configuration that applies to each feature that is enabled.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/smart-crop-disable-all.html)

See [Setting up Elemental Inference features for the first time](smart-crop-procedure-cli-create.md) for an example of the JSON as it appears before you make these changes.

## Result of changes to the MediaLive channel
<a name="smart-crop-disable-all-result-global"></a>

When you save the changes to the channel, MediaLive takes these actions, in this order:
+ MediaLive uses `associate-feed` in Elemental Inference to disable all the outputs in the feed. It does this because it detects that there is no `feedArn` parameter in the channel.

  After an output is disabled, you can still read the existing metadata in the output for the next 24 hours. After that time, the output remains disabled, but its metadata is deleted.
+ MediaLive uses `disassociate-feed` to disassociate the channel (the resource) from the feed. It does this because it detects that there are no enabled outputs in the feed. 
+ When the resource is disassociated from the feed, Elemental Inference automatically sets the status of the feed to `Archived`. 

When you start the channel, MediaLive and Elemental Inference behave differently:
+ There is no `feedArn` parameter in the channel, so MediaLive stops sending the source video to Elemental Inference. (It doesn't put media.)
+ All the outputs are disabled, so Elemental Inference stops generating metadata for each feature. 

These changes affect the charges that you incur:
+ You don't incur charges for the feed because all the outputs are disabled.

**Re-enabling Elemental Inference features** 

The feed has been set to `Archived`, so you can't re-enable any Elemental Inference features. Instead, you must [set up the features ](smart-crop-procedure-cli-create.md)again. 