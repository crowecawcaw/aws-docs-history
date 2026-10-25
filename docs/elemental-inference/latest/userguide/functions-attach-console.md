

# Attaching a function using the console
<a name="functions-attach-console"></a>

You can add a function output when you create a feed, or to a feed that already exists.

1. On the **Create feed** page, or on the **Edit feed** page of an existing feed, in **AI features**, select **Function**. The console adds one function output. To add another, choose **Add function**.

1. Enter a **Name** for the output.

1. For **Function**, choose the function to run.

1. For **Trigger**, choose one of the following:
   + **Fixed interval** – then set **Invocation interval**, from 1 through 60 seconds.
   + **Per shot**, **Per scene**, or **Per clip**.

   The console offers only the triggers that the chosen function supports. A function that reads contextual metadata, for example, can't use a fixed interval, and defaults to **Per scene**. A function that reads clips defaults to **Per clip**.

1. Complete the settings that appear. The console shows only the settings for the context that the chosen function actually reads:
   + **Sampling mode** (**First frames**, **Evenly spaced**, or **Last frames**) and **Frame count**. To resize the frames, select **Resize frames** and enter a **Width** and **Height** in pixels. **Keep the native aspect ratio** is selected by default, so changing one value changes the other.
   + **Fragment sampling mode** and **Fragment count** – the equivalent settings for the video clip.
   + **Subtitle source**, **Contextual metadata source**, or **Clip source** – the output on this feed to read that context from. If the feed has exactly one output of the required kind, it is preselected. If the feed has none, the console tells you which output to add.

1. In **Access role**, specify the IAM role that Elemental Inference assumes to invoke the model. Choose **Use an existing role**, **Create a new role from template**, or **Use a custom role ARN**. A role that the console creates allows `bedrock:InvokeModel` on only the models that the feed's function outputs use. An access role is required for any feed that has a function output with a model target. See [Setting up the access role](functions-prerequisites-access-role.md).

1. Save the feed.

You can attach more than one function output to a feed, up to the quota for enabled function outputs per feed. Function outputs also count toward the quota for enabled outputs per feed. See [Quotas and limits for functions](functions-quotas.md).

To see results without writing any code, expand **Preview metadata** under the function output on the feed detail page. Choose a **Time range** and choose **Apply**. The table shows one row for each run, with its time and the value that the function produced. Preview requires the feed to be active and receiving media. For live content the window follows the live edge, a few seconds behind it; for video-on-demand content, turn on **Use a fixed start PTS** and enter a **Start PTS**.