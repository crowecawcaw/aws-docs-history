# Setting up Smart Subtitles (console)

Follow these steps to enable Smart Subtitles in a channel using the MediaLive
console.

1. On the **Create channel** page, ensure that you have added
   at least one input attachment to the channel. An input attachment is required
   before you can add a Smart Subtitles caption selector.

If you want Smart Subtitles to transcribe a specific audio track, add an
audio selector to the input attachment before proceeding to the Elemental
Inference settings. 2. Navigate to the **Elemental Inference settings** section. 3. For **Elemental Inference feed**, select a feed that
contains a subtitling output. If you need to create a new feed, choose
**Create feed** at the top of the Elemental Inference
settings section. If you need to update an existing feed, choose
**Create or update the feed in Elemental Inference**
beneath the **Subtitling output** dropdown. For more information, see [Creating an Elemental Inference workflow](../../../elemental-inference/latest/userguide/elemental-inference-configuration.md "../../../elemental-inference/latest/userguide/elemental-inference-configuration.md") in the _AWS Elemental Inference user
guide_.
After creating or updating the feed, choose **Refresh** to
see the updated feed list.

If the input attachment has audio selectors, for **Audio selector
name**, select the audio selector that contains the audio you want
to transcribe. 4. Under **Smart Subtitles**, choose **Add Smart
Subtitles caption selector**. This adds a caption selector to the
input attachments. 5. Configure the caption selector:

    * **Caption selector name** – Enter a name
     for the caption selector (for example,
     `SmartSubtitlesSelector1`).
    * **Language code** – Choose the language of
     the audio in your source media. This must match the language
     configured on the subtitling output of the selected feed.
    * **Caption synchronization mode** – Choose
     how MediaLive synchronizes generated subtitles with the video
     output:




    	+ **Video aligned captions** (default)
    	 – MediaLive delays video to ensure captions are
    	 synchronized with audio and video.
    	+ **No video delay** – MediaLive does
    	 not delay video for caption alignment. Caption output timing
    	 is adjusted to align with video as captions become
    	 available.
    * **Subtitling output** – Select a subtitling
     output from the selected feed. If the feed does not have a subtitling
     output, update the feed in the Elemental Inference console to add one, then
     choose **Refresh** to update the list of
     outputs.

6. Create a captions output for the subtitles:

    1. In your output group (HLS, MediaPackage, MediaPackage V2, CMAF
     Ingest, or Microsoft Smooth), add a new output.
    2. Remove any video and audio encodes from this output so that it
     contains only captions.
    3. Add a captions description and set the destination format to
     **TTML** (for MediaPackage V2, CMAF Ingest, or
     Microsoft Smooth output groups) or **WebVTT** (for HLS
     or MediaPackage output groups).
    4. For **Caption selector name**, select the Smart
     Subtitles caption selector you created earlier.

###### Note

Before configuring Smart Subtitles, you must have an Elemental Inference feed with a
subtitling output. You can create the feed in one of the following ways:

- In the Elemental Inference console, create a feed and add a subtitling output.
- Using the AWS CLI. For instructions, see [Elemental Inference features using AWS CLI](elemental-inference-cli.md "elemental-inference-cli.md").
