

# Configuring Smart subtitling with AWS Elemental Inference
<a name="smart-subtitling-with-elemental-inference"></a>

 The **Smart subtitling** feature uses AI to generate captions from audio. Using Smart subtitling reduces manual captioning effort and increases delivery speed of your video content. 

 This guide shows you how to enable the **Smart subtitling** feature in a MediaConvert job. For more information about using MediaConvert Smart features, see [Elemental Inference](elemental-inference.md). 

## Configuring a Smart subtitling job
<a name="smart-subtitling-setting-up-job"></a>

To enable **Smart subtitling** in a MediaConvert job, perform the following steps:

1. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert).

1. In the navigation pane, choose **Jobs**. Then, choose **Create job**.

1. Add an output group. Then, add an output to the output group.

1. In the output encoding settings, choose **Add captions**.

1.  In the caption output encoding settings, for **Captions source**, select **Smart subtitle**. 

1.  Select a **Destination type** that is compatible with your output video codec. For supported combinations, refer to [Captions support tables](captions-support-tables.md). 

1. Select an **Audio source name**.

1. Select a **Language** matching the language of your audio source.

For details about setting up a MediaConvert job, see [Tutorial: Configuring job settings](setting-up-a-job.md). 