

# Starting a preview
<a name="playground-preview-start"></a>

1. Open the Elemental Inference console at [https://console.aws.amazon.com/elemental-inference/](https://console.aws.amazon.com/elemental-inference/).

1. In the navigation pane, choose **Playground**, and then choose **Create job**.

1. Under **Features**, choose **All features**.

1. Under **Input settings**, for **Input S3 URI**, enter the Amazon S3 URI of an MP4 file, or choose **Browse** to select one. **Browse** lists only buckets in the console's current AWS Region. To use a bucket in another Region, enter its URI.

1. Choose the part of the video to preview. A preview must be 5 seconds to 5 minutes long.
   + If the video is 5 minutes or shorter, you can leave **Start time** and **End time** blank to preview the whole video.
   + If the video is longer than 5 minutes, the console fills in the first 5 minutes. Change **Start time** and **End time** (HH:MM:SS) to preview another part.
   + If your browser can't read the video's length, **End time** is required.

1. For **Spoken language**, choose the language spoken in the video. Smart subtitles use this language.

1. Under **Output settings**, for **Destination**, enter the Amazon S3 folder URI where the preview's segments and results are written, or choose **Browse**.

1. Under **Service role**, if the service role doesn't exist yet, choose **Create service role**. If it exists but doesn't cover the buckets you selected, choose **Update role permissions**.

1. Choose **Start preview**. The preview page opens and the preview starts. Keep this browser tab open until the preview finishes. A preview takes longer than the clip itself: the console waits for MediaConvert's first segments and for the feed to start, streams the clip in real time, and then collects the last results. If this tab is already running a preview, the console asks you to confirm. The new preview stops that one, and its results aren't saved.