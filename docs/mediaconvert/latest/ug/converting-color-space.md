# Configuring color space conversion

The following procedure details how to configure a job to convert from one color space to another.

1. Confirm that MediaConvert supports the conversion that you want to do.
2. Set up your transcoding job as usual. For more information, see [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
3. On the **Create job** page, in the **Job** pane on the left, choose your HDR output.
4. At the bottom of the **Encoding settings** section on the
   right, choose **Preprocessors**.
5. Choose **Color corrector** to display the color correction
   settings.
6. For **Color space conversion**, choose the color space that
   you want for your output.
7. If you are converting to HDR 10, specify values for the
   **HDR master display information** settings.

These values don't affect the pixel values that are encoded in the video
stream. They are intended to help the downstream video player display content in
a way that reflects the intentions of the content creator.
