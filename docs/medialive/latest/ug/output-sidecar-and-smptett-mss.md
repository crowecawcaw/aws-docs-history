# Create sidecar or SMPTE-TT captions

encodes

Follow this procedure if the format of the captions asset that you want to add in the
MediaLive channel is [a sidecar](categories-captions.md "categories-captions.md"), or if the format is
SMPTE-TT for a Microsoft Smooth output group.

You set up the captions and video in the same output.

1. In the **Create channel** or **Edit channel** page
   for the channel, in the **Channel** panel, find the output group where
   you want to set up captions.
2. Create a new output in this output group.
3. In the output, go to the **Stream settings** and choose
   **Add caption**, then **Create a new caption
   encode**. Captions fields appear.
4. Complete the following fields:
   - **Captions description name**: Enter a name that is unique in
     the channel, for example, `Embedded`.
   - **Captions selector name**: Select the captions selector that
     you created when you [created the
     captions selectors in the input](identify-captions-in-the-input.md "identify-captions-in-the-input.md"). Specify the selector that identifies the
     captions asset that is the source for the captions in this output.
   - **Captions settings**: Choose the captions format for the
     output captions. Depending on the format, more fields appear.

5. Choose **Additional settings**. More fields appear. See the table
   after this procedure for information about which fields to complete for each
   format.
6. You now have a captions encode that is fully defined. Repeat these steps to create
   more captions in this output group.

| Field                                                       | Topic                                          | Applicable formats | Description                                                                                                                                      |
| ----------------------------------------------------------- | ---------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Style Control, Fill Line Gap, Font Family, Copyright Holder | Captions style                                 | EBU-TT-D           | See [Font styles for EBU-TT-D](ebu-tt-font-styles.md "ebu-tt-font-styles.md")                                                                    |
| Style Control                                               | Captions style                                 | TTML, Web-VTT      | See [Font styles for TTML](ttml-font-styles.md "ttml-font-styles.md") or [Font styles for WebVTT](webvtt-font-styles.md "webvtt-font-styles.md") |
| Language code, Language description                         | Language information for this specific caption | All formats        | Optional. For information, choose the **Info** link next to each field.                                                                          |
| Accessibility, Caption DASH Roles, DVB DASH accessibility   | Accessibility data                             | All formats        | [Including accessibility data in captions in MediaLive](captions-accessibility.md "captions-accessibility.md")                                   |
| PIDs                                                        | PID assignment                                 | Teletext           | [PIDs for Teletext](complete-the-pids-for-teletext.md "complete-the-pids-for-teletext.md") ,                                                     |
