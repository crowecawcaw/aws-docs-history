# Configuring Dolby Atmos passthrough

AWS Elemental MediaConvert can create Dolby Digital Plus with Atmos outputs by either encoding
audio in 9.1.6, 7.1.4, or 5.1.4 PCM mono channels, or by passing through already encoded Dolby Digital
Plus with Atmos content.

You set up your job to pass through Dolby Digital Plus with Atmos content in the same
way that you pass through Dolby Digital and Dolby Digital Plus content.

###### To set up a Dolby Atmos job, passing through finished audio content

1. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert "https://console.aws.amazon.com/mediaconvert").
2. Choose **Create job**.
3. Set up your input audio and video as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
4. Set up your output groups, outputs, and video output selectors as described in
   [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md") and
   [Creating outputs](output-settings.md "output-settings.md"). Choose supported containers as
   listed in [Supported output formats](reference-codecs-containers.md "reference-codecs-containers.md").
5. Create audio output selectors as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md") and [Creating outputs](output-settings.md "output-settings.md").

Set them up as follows:

    1. In the **Job** pane on the left, choose an output
     that includes audio.
    2. In the **Encoding settings** section, choose
     **Audio 1**.
    3. For **Audio codec**, choose **Passthrough**.
