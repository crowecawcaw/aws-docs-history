# Smart crop video using Elemental Inference

In an AWS Elemental MediaLive channel, you can enable the smart crop feature in order to set up one or
more outputs with an aspect ratio that is different from the source aspect ratio. A typical
use case is to create vertical video from a landscape video.

MediaLive uses AWS Elemental Inference to crop the video frames to an aspect ratio that you specify.

Elemental Inference analyzes the source content to detect the region of interest. For example, consider
the source video of a soccer game. Elemental Inference infers the location of the region of interest when
the ball is moving. Elemental Inference will typically infer that the soccer ball and the players around
the ball are that region of interest.

MediaLive obtains information about the region of interest from Elemental Inference and crops and scales
the video.

###### Topics

- [Pricing](#smart-crop-pricing "#smart-crop-pricing")
- [Source requirements](#smart-crop-source-requirements "#smart-crop-source-requirements")
- [Output specifications](#smart-crop-output-requirements "#smart-crop-output-requirements")
- [Setting up smart crop using the MediaLive console](#smart-crop-procedure-console "#smart-crop-procedure-console")
- [Modifying the smart crop configuration](#smart-crop-modify-delete "#smart-crop-modify-delete")

## Pricing

There is a charge for running a channel that has the smart crop feature enabled. To
stop this charge, you must disable the feature [in all outputs in the channel](#smart-crop-modify-delete "#smart-crop-modify-delete"). For information on charges for using this
feature, see [https://aws.amazon.com/elemental-inference/pricing/](https://aws.amazon.com/elemental-inference/pricing/ "https://aws.amazon.com/elemental-inference/pricing/").

###### Note

When you enable smart crop in a standard-class MediaLive channel, there is a separate
but identical charge for each pipeline in the channel.

## Source requirements

- Input type: All supported types. The input must be live input, not a file
  input.
- Input codec: All supported codecs
- Input resolution: All supported resolutions.
- Aspect ratio: Any aspect ratio
- Dynamic image overlays: We recommend that the source doesn’t include image
  overlays because movement in the overlay might include movement that Elemental Inference will
  incorrectly start to track.
- Static image overlays and burned-in captions: We recommend that the source
  doesn’t include static image overlays or burned-in captions because the smart
  crop might cut them off awkwardly.
- Smart crop is supported in channels that implement input switching and/or
  input failover.
- Smart crop isn't supported in MediaLive Anywhere channels.

## Output specifications

- Output types: All supported types.
- Output codec: All supported codecs.
- Aspect ratio: Any aspect ratio, and any orientation (portrait or
  landscape).
- Resolution: All supported resolutions.
- Shared encodes: You might choose not to share encodes in a channel that you
  set up for smart crop because if you enable smart crop in one of the outputs
  that shares an encode, MediaLive automatically enables it in the other output that
  shares the encode. If you are setting up smart crop in an existing channel with
  shared encodes, see [Sharing a video encode](create-video-share.md "create-video-share.md") for information about
  how to uncouple the outputs.
- You can't enable AFD in any video outputs where smart crop is enabled.
- You can't insert dynamic image overlays in a channel where smart crop is
  enabled.

## Setting up smart crop using the MediaLive console

###### Note

The information in this section assumes that you are familiar with the general
steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

### How smart crop works

You set up the smart crop feature in individual video outputs by setting the video
scaling to SMART_CROP. You can set up smart crop in one or more video outputs in the
channel. When you save the channel, MediaLive automatically creates a _feed_ resource in Elemental Inference, in your AWS account. MediaLive
creates an association between the feed and each output that uses smart crop.

When you start the channel, MediaLive
delivers
the source stream to Elemental Inference and then retrieves metadata from Elemental Inference that describes
the region of interest. In each video output where smart crop is set up, MediaLive crops
the video in the channel to the new region of interest. MediaLive continues with regular
processing to encode the video.

### Step A: Enable smart crop

You must enable smart crop in the applicable video outputs.

1. On the **Create channel** or **Edit channel
   page**, choose **AWS Elemental Inference
   settings**.
2. In **State**, choose **Enabled**.
   Sections for each Elemental Inference feature appear.
3. In the **Output groups** section of the channel, find an
   output group and one of the output that contains the video. Display the
   **Stream settings** section, and choose the
   **Video** section.
   - Complete the **Width** and
     **Height** fields to match the crop that you
     want MediaLive to apply.
   - Open **Scaling settings**, then set
     **Scaling behavior** to
     **SMART_CROP**.

4. Repeat the previous step in more video outputs, in this output group and
   other output groups. Remember that you don't have to set up smart crop in
   every output group, or in every video output in one output group.

### Step B: Review the setup

1. On the **Create channel** or **Edit channel
   page**, choose **AWS Elemental Inference
   settings**. The **Smart crop** section
   automatically expands to show a list of output groups and their video
   outputs appears.
   - Video outputs that are set up for smart crop (smart crop is
     enabled) appear with the slider enabled. The output is _smart-crop-enabled_
   - Output groups that have _all_
     their video outputs with smart crop enabled appear with the slider
     enabled. This output group is smart-crop-enabled.
   - Output groups don't appear with the slider enabled if that contain
     a mix of enabled and disabled video outputs.

2. You can adjust the configuration:

Move the slider to enable any output or output group. In the applicable
video outputs, MediaLive automatically sets **Scaling
behavior** setting to **Smart crop**. However,
you probably still need to view the video output in the Streams settings to
change the video width and height (the aspect ratio). If you don't set the
width and height, the output might be pillar boxed or letter boxed.

You can move the slider to disable any output or output group. In the
applicable video outputs, MediaLive automatically sets **Scaling
behavior** setting to **Default**. However,
you probably still need to view the video output in the Streams settings to
change the video width and height (the aspect ratio).

## Modifying the smart crop configuration

You can modify the existing smart crop configuration in a channel as follows:

**To disable smart crop in all outputs in the
channel**

1. On the **Create channel** or **Edit channel
   page**, choose **AWS Elemental Inference
   settings**. The **Smart crop** section is
   automatically expanded to show a list of output groups and their video outputs.
2. Choose the appropriate action:
   - If smart crop is the only Elemental Inference feature that is enabled on this page:
     in **State**, choose
     **Disabled**.
   - Otherwise, in the **Smart crop** section, move the
     slider for every output group to disabled (gray).

**To disable smart crop in individual outputs**

1. On the **Create channel** or **Edit channel
   page**, in the **Output groups** section, select
   the output that contains the video.
2. Display the **Stream settings** section, and choose the
   **Video** section.
   - Adjust the values in the **Width** and
     **Height** fields.
   - Open **Scaling settings**, then set **Scaling
     behavior** to a value other than
     **SMART_CROP**.
