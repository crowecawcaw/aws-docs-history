

# Setting up with the MediaLive console
<a name="smart-crop-console-create"></a>

You set up the smart crop feature in one or more video outputs of a MediaLive channel. In each video output where you want the feature, you set the video scaling to SMART\_CROP. You must have an Elemental Inference feed selected in the channel's Elemental Inference settings. If the feed already has a cropping output, MediaLive uses it. If not, MediaLive creates a cropping output on the feed automatically when you save the channel. For information about creating a feed, see [ Creating an Elemental Inference workflow](https://docs.aws.amazon.com/elemental-inference/latest/userguide/elemental-inference-configuration) in the *AWS Elemental Inference user guide*.

You can set up smart crop in a new MediaLive channel that you are creating. Or you can update an existing channel to include smart crop.

This section describes how to set up smart crop using the MediaLive console. For information about setting up using an AWS API, see [Elemental Inference features using AWS CLI](elemental-inference-cli.md).

**Note**  
The information in this section assumes that you are familiar with the general steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md). 

**Topics**
+ [Step A: Enable smart crop](#smart-crop-procedure-a)
+ [Step B: Review the setup](#smart-crop-procedure-b)
+ [Step C: Save or update the channel](#smart-crop-procedure-c)

## Step A: Enable smart crop
<a name="smart-crop-procedure-a"></a>

You must enable smart crop in the applicable video outputs. 

1. If you plan to update an existing feed, make sure that you have room in the [enabled outputs quota](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas) for Elemental Inference. The list of quotas is sorted alphabetically. Look for quotas that don't start with "Request rate for".

   Keep in mind that each feature that you enable in a channel results in one Elemental Inference output.

1. On the **Create channel** or **Edit channel page**, navigate to the **Elemental Inference settings** section. For **Elemental Inference feed**, select a feed from the dropdown. If you need to create a feed, see [ Creating an Elemental Inference workflow](https://docs.aws.amazon.com/elemental-inference/latest/userguide/elemental-inference-configuration) in the *AWS Elemental Inference user guide*.

1. In the **Output groups** section of the channel, find an output group and one of the outputs that contains the video. Display the **Stream settings** section, and choose the **Video** section. 
   + Complete the **Width** and **Height** fields to specify the resolution. Set the resolution to the crop that you want MediaLive to apply to the video. For example, 720 x 1600.
   + Open **Scaling settings**, then set **Scaling behavior** to **SMART\_CROP**. 

1. Repeat the previous step in more video outputs, in this output group and other output groups. Remember that you don't have to set up smart crop in every output group, or in every video output in one output group.

## Step B: Review the setup
<a name="smart-crop-procedure-b"></a>

1. On the **Create channel** or **Edit channel page**, choose **AWS Elemental Inference settings**. The **Smart crop** section automatically expands to show a list of output groups and their video outputs. 
   + Video outputs that are set up for smart crop (smart crop is enabled) appear with the slider enabled. The output is *smart-crop-enabled*
   + Output groups that have *all* their video outputs with smart crop enabled appear with the slider enabled. This output group is smart-crop-enabled.
   + Output groups don't appear with the slider enabled if that contain a mix of enabled and disabled video outputs.

1. You can adjust the configuration:

   Move the slider to enable any output or output group. In the applicable video outputs, MediaLive automatically sets the **Scaling behavior** setting to **Smart crop**. However, you probably still need to view the video output in the Streams settings to change the video width and height, to set the aspect ratio and resolution. If you don't set the width and height, the output might be pillar boxed or letter boxed.

   You can move the slider to disable any output or output group. In the applicable video outputs, MediaLive automatically sets **Scaling behavior** setting to **Default**. However, you probably still need to view the video output in the Streams settings to change the video width and height (the aspect ratio).

When you change the configuration, MediaLive performs the appropriate changes in Elemental Inference. 

## Step C: Save or update the channel
<a name="smart-crop-procedure-c"></a>

Save the channel. If the selected feed does not already have a cropping output, MediaLive automatically creates one. MediaLive associates the feed with the channel.

You can start the channel. When the channel is running, MediaLive delivers the source stream to Elemental Inference and then retrieves metadata from Elemental Inference that describes the region of interest in each video frame. In each video output where smart crop is set up, MediaLive crops the video to the new region of interest. MediaLive then continues with regular processing to encode the video. 