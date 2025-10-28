# Configuring output overlays

Because you're setting up an output overlay, set up image insertion in each output
where you want the service to overlay images on your video. For information about
setting up an overlay that appears on all outputs, or on portions that correspond to
only one input, see [Choosing between input and output overlays](choosing-between-input-overlay-and-output-overlay.md "choosing-between-input-overlay-and-output-overlay.md").

If you don't specify overlay start time and duration, the service puts the overlay
on the entire output.

###### To set up a still image overlay in an output

1.  Open the AWS Elemental MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert "https://console.aws.amazon.com/mediaconvert").
2.  Set up your output groups and outputs for video and audio, as described in
    [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md") and
    [Creating outputs](output-settings.md "output-settings.md").
3.  For each output that you want to have a image overlay, do the
    following:

        1. On the **Create job** page, in the **Job** pane on the left, under **Output groups**, choose the
         appropriate output.
        2. Under **Encoding** settings, under the
         **Video** tab, find the
         **Preprocessors** section.
        3. Choose **Image inserter**. This displays an
         **Add image** button.
        4. For each image overlay that you want to include in the output,
         choose **Add image**, and then specify the overlay
         settings.


        For **Image location**, specify an input file
         that is stored in Amazon S3 or on an HTTP(S) server. For Amazon S3 inputs, you
         can specify the URI directly or choose **Browse**
         to select from your Amazon S3 buckets. For HTTP(S) inputs, provide the
         URL to your input file. For more information, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

    For details about the more complex output image overlay settings, see the
    following topics:

[Sizing overlays](about-overlay-scaling.md "about-overlay-scaling.md")

[Layering overlays](using-multiple-overlays.md "using-multiple-overlays.md")
