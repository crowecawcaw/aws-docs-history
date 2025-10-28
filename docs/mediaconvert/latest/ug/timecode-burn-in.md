# Burning in timecodes on the video

frames

The **Timecode burn-in** setting determines whether a given
output has visible timecodes inscribed into the video frames themselves. The
timecodes are not an overlay, but rather a permanent part of the video
frames.

###### To burn in timecodes in an output (console)

1.  On the **Create job** page, in the **Job** pane on the left, choose an output.
2.  Under **Stream settings**,
    **Preprocessors**, choose **Timecode
    burn-in**.
3.  Optionally, provide values for the **Prefix**,
    **Font size**, and **Position**
    settings. Even if you don't provide these values, timecodes are burned
    into your output using these default values:

        * **Prefix**: no prefix
        * **Font size**: **Extra Small
         (10)**
        * **Position**: **Top
         Center**

    For details about each of these settings, choose the
    **Info** link next to **Timecode
    burn-in**.

###### To burn in timecodes in an output (API, SDK, and AWS CLI)

1. In your JSON job specification, include the setting [TimecodeBurnin](../apireference/jobs.md#jobs-prop-videopreprocessor-timecodeburnin "../apireference/jobs.md#jobs-prop-videopreprocessor-timecodeburnin"). `TimecodeBurnin` is located in
   `Settings`, `OutputGroups`,
   `Outputs`, `VideoDescription`,
   `VideoPreprocessors`.
2. Optionally, provide values for the settings that are children of
   `TimecodeBurnin`. If you don't provide these values,
   timecodes are burned into your output using these default values:
   - `Prefix`: _no
     prefix_
   - `FontSize`: `10`
   - `Position`: `TOP_CENTER`
