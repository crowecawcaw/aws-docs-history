# Setting up captions in outputs

The location of the captions in a job depends on your output captions format: Your
captions might be in the same output as your video, a separate output in the same output
group as your video, or in an entirely separate output group. How you set up multiple
captions tracks also depends on the output captions format.

For a full list of supported input and output captions, see [Captions reference tables](captions-support-tables.md "captions-support-tables.md").

For information about how to set up captions in your input, see [Setting up input captions](including-captions.md "including-captions.md").

The following procedure shows how to set up captions for different outputs.

###### To set up captions for different outputs

1. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert "https://console.aws.amazon.com/mediaconvert").
2. Choose **Create job**.
3. Set up your input, output groups, and outputs for video and audio, as
   described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md")
   and [Creating outputs](output-settings.md "output-settings.md").
4. Create input captions selectors as described in [Creating input captions selectors](including-captions.md#create-input-caption-selectors "including-captions.md#create-input-caption-selectors").
5. Determine where in your job to specify the captions. This choice depends on
   the output captions format. Consult the relevant topic below to look this
   up.
6. In the left pane of the **Create job** page, choose the
   appropriate output from the list of outputs.
7. Under **Encoding settings**, choose **Add
   caption**. This displays a captions settings area under
   **Encoding settings**.
8. If your output captions format requires a separate group of captions settings
   for each track in the output, choose **Add captions** again
   until you have one captions group for each track. To determine whether you need
   one captions settings group for all tracks or one for each track, see the
   relevant topic below.
9. Under **Encoding settings**, choose **Captions
   1** from the list.
10. Under **Captions source**, choose a captions selector. This
    selects the track or tracks that you associated with the selector when you set
    up your input, so that AWS Elemental MediaConvert will include those captions in this
    output.
11. Under **Destination type**, choose an output captions format.
    Check [Supported input captions, within video containers](captions-support-tables-by-container-type.md "captions-support-tables-by-container-type.md") to ensure that
    you are choosing a supported format.
12. Provide values for any additional fields as described in the relevant topic
    below.

###### Details by output captions format

- [CEA/EIA-608 and CEA/EIA-708 (embedded)
  output captions](embedded-output-captions.md "embedded-output-captions.md")
- [DVB-Sub output captions](dvb-sub-output-captions.md "dvb-sub-output-captions.md")
- [IMSC, TTML, and WebVTT (sidecar)
  output captions](ttml-and-webvtt-output-captions.md "ttml-and-webvtt-output-captions.md")
- [SCC, SRT, and SMI (sidecar) output
  captions](scc-srt-output-captions.md "scc-srt-output-captions.md")
- [Teletext output captions](teletext-output-captions.md "teletext-output-captions.md")
- [Burn-in output captions](burn-in-output-captions.md "burn-in-output-captions.md")
- [Settings for accessibility captions](accessibility-captions.md "accessibility-captions.md")
