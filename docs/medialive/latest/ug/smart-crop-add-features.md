

# Adding more Elemental Inference features
<a name="smart-crop-add-features"></a>

In a MediaLive channel where Elemental Inference features are already set up, you can add more Elemental Inference features.

If you want to disable features rather than add them, see [Disabling some Elemental Inference features in a channel](smart-crop-disable-some.md) or [Disabling all Elemental Inference features in a channel](smart-crop-disable-all.md).

1. Make sure that you have room in the [enabled outputs quota](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas) for Elemental Inference. The list of quotas is sorted alphabetically. Look for quotas that don't start with "Request rate for".

   Keep in mind that each feature that you enable in a channel results in one Elemental Inference output.

1. **In MediaLive**, use `update-channel` to edit the channel. Make changes as described in the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/smart-crop-add-features.html)

1. When you save the channel, MediaLive performs the following actions:
   + If you are adding smart crop for the first time, MediaLive updates the feed in Elemental Inference to create a crop output in the feed.

1. **In the Elemental Inference**, use `update-feed` to update the feed. Make changes as described in the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/smart-crop-add-features.html)

1. When you are ready to start the channel, use `StartChannel` in MediaLive.