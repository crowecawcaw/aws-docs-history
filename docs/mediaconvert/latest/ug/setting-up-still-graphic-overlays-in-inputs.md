# Configuring input overlays

Because you are setting up an input overlay, set up image insertion in each input
where you want the service to overlay imagess on your video. The overlays that you
specify appear in every output. For information about setting up an overlay that
appears on only specific outputs, see [Choosing between input and output overlays](choosing-between-input-overlay-and-output-overlay.md "choosing-between-input-overlay-and-output-overlay.md").

When don't specify overlay start time and duration, the service puts the overlay
on the entire part of the output that corresponds to the input.

###### To set up a still image overlay in an output

1.  Open the AWS Elemental MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert "https://console.aws.amazon.com/mediaconvert").
2.  Specify your input files, as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
3.  For each input that you want to have a image overlay, do the
    following:

        1. On the **Create job** page, in the **Job** pane on the left, under **Inputs**, choose the
         appropriate input.
        2. In the **Image inserter** section to the right
         of the **Job** pane, choose
         **Add image**, and then specify the
         overlay settings.


        For **Image location**, specify an input file
         that is stored in Amazon S3 or on an HTTP(S) server. For Amazon S3 inputs, you
         can specify the URI directly or choose **Browse**
         to select from your Amazon S3 buckets. For HTTP(S) inputs, provide the
         URL to your input file. For more information, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

    For details about the more complex input image overlay settings, see the
    following topics:

[Sizing overlays](about-overlay-scaling.md "about-overlay-scaling.md")

[Layering overlays](using-multiple-overlays.md "using-multiple-overlays.md")
