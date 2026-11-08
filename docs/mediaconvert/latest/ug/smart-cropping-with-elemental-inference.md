

# Configuring Smart cropping with AWS Elemental Inference
<a name="smart-cropping-with-elemental-inference"></a>

 The **Smart cropping** feature uses AI to infer the region of interest in the input video. Next, MediaConvert crops the video to the specified aspect ratio, keeping the region of interest in the center of the output. 

 A typical use case for **Smart cropping** is to convert a landscape video to a portrait video. For example, in a landscape video of a soccer game, **Smart cropping** infers a region containing the soccer ball and active players to be the region of interest. The video is then cropped (verticalized) to keep the ball and the players in the output video frame. Using Smart cropping reduces manual editing effort and increases delivery speed of multi-format video content 

 This guide shows you how to enable the **Smart cropping** feature in a MediaConvert job. For more information about using MediaConvert Smart features, see [Elemental Inference](elemental-inference.md). 

## Configuring a Smart cropping job
<a name="smart-cropping-setting-up-job"></a>

To enable **Smart cropping** in a MediaConvert job, perform the following steps:

1. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert).

1. In the navigation pane, choose **Jobs**. Then, choose **Create job**.

1. Add an output group. Then, add an output to the output group.

1.  In the output video encoding settings, set the desired width and height. Note: the width must be less than or equal to the height. 

1.  In the output video encoding settings, expand **Scaling**. Then, for **Scaling behavior**, select **Smart Cropping using Elemental Inference**. 

For details about setting up a MediaConvert job, see [Tutorial: Configuring job settings](setting-up-a-job.md). 