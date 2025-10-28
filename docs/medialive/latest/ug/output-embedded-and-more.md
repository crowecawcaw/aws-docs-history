# Create embedded or object captions

encodes

Follow this procedure if the format of the captions asset that you want to add belongs
to the category of embedded, burn-in, or object. You set up
the captions and video and audio in the same MediaLive output.

1. In the **Create channel** or **Edit channel** page
   for the channel, in the **Channel** panel, find the output group where
   you want to set up captions.
2. If you have already set up outputs in this output group with video (and possibly
   audio), find the outputs where you want to add the captions. Or create a new output in
   this output group.
3. In the output, go to the **Stream settings** and choose
   **Add caption**, then **Create a new caption
   encode**. Captions fields appear..
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

Complete the fields that appear for the selected format. For details about a field,
choose the Info link beside the field. 6. You now have a captions encode that is fully defined. Repeat these steps to create
more captions in this output or in another output, or in another output group.

| Field                                                     | Topic                                          | Applicable formats | For more information, see this section                                                                                                                                  |
| --------------------------------------------------------- | ---------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font, Positioning, Font Style                             | Captions style                                 | Burn-in, DVB-Sub   | [Font styles for Burn-in or DVB-Sub](font-styles-for-burn-in.md "font-styles-for-burn-in.md")                                                                           |
| Language code, Language description                       | Language information for this specific caption | All formats        | Optional. For information, choose the **Info** link next to each field.                                                                                                 |
| Accessibility, Caption DASH Roles, DVB DASH accessibility | Accessibility data                             | All formats        | [Including accessibility data in captions in MediaLive](captions-accessibility.md "captions-accessibility.md")                                                          |
| PIDs                                                      | PID assignment                                 | ARIB, DVB-Sub      | [PIDs for ARIB](complete-the-pids-for-arib.md "complete-the-pids-for-arib.md"), [PIDs for DVB-Sub](complete-the-pids-for-dvb-sub.md "complete-the-pids-for-dvb-sub.md") |
| Captions language mappings                                | Tags in manifest                               | HLS                | [Language information in HLS manifests](set-up-the-hls-manifest.md "set-up-the-hls-manifest.md")                                                                        |
