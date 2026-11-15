

# While a preview runs
<a name="playground-preview-running"></a>

Closing or reloading the browser tab ends the preview before its results are saved. While a preview runs or saves, your browser asks you to confirm before you leave. You can go to other pages of the Elemental Inference console in the same tab while the preview runs.

Below the video, the page shows the preview's progress: **Preparing clip**, **Starting feed**, **Analyzing clip**, and **Collecting results**. Under **Preparing clip**, the **MediaConvert job** link opens the job in the MediaConvert console.

The video plays about 30 seconds behind the stream, so that results are ready as the video reaches them. You can switch the player between **16:9** and **9:16** views to see the smart crop, and turn on the player's captions to see the subtitles on the video. Beside the video, the console shows the results on four tabs:
+ **Smart Cropping** – Where the 9:16 window sits across the frame over time.
+ **Event Clipping** – Moments worth clipping, tagged with the events detected in them. Event clipping works on sports footage.
+ **Smart Subtitling** – Captions as the service transcribed them, in the language that you chose.
+ **Contextual Metadata** – Each scene and shot as it plays, whether it suits an ad, and its mood.

To play the video from a point, choose a row on a tab, or a point on its chart or timeline.

To end a preview early, choose **Stop preview**. The console deletes the feed, and cancels the MediaConvert job if it's still running. The partial results stay on the page, but they aren't saved.

When the preview finishes, the console does the following:
+ It shows a summary with the preview's **Status** (**Completed**, **Stopped**, or **Failed**), **Clip length**, and **Language**.
+ It saves the results to your output location.
+ If any feature's results couldn't be read, or saving fails, it shows **Results not saved**, and reopening the preview later won't show them. To save results, choose **Run again**.

**Run again** runs the same clip again and is charged again. If the new run saves its results, they replace the earlier ones. For charges, see [Pricing](playground-pricing.md). To reopen a saved preview later, see [Viewing job results](playground-job-details.md).