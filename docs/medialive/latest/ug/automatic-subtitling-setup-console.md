# Setting up Smart Subtitles (console)

Follow these steps to enable Smart Subtitles in a channel using the MediaLive
console.

1. On the **Create channel** page, navigate to the
   **Smart Subtitles** section under Elemental Inference
   settings.
2. Choose **Add Smart Subtitles caption selector**.
3. For **Caption selector name**, enter a name for the caption
   selector (for example, `SmartSubtitlesSelector1`).
4. For **Language code**, choose the language of the audio in
   your source media.
5. Create a captions output for the subtitles:
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

Before configuring Smart Subtitles, you must create an Elemental Inference feed with a
subtitling output. You can create the feed in one of the following ways:

- In the MediaLive console, choose **Create new feed** in the
  Elemental Inference settings section. A side panel opens where you can
  configure the feed name, enable subtitling, and set the language
  code.
- In the Elemental Inference console, create a feed and add a subtitling output.
- Using the AWS CLI. For instructions, see [Elemental Inference features using AWS CLI](elemental-inference-cli.md "elemental-inference-cli.md").
