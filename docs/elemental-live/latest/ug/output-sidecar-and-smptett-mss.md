# Sidecar captions or

SMPTE-TT captions in MS Smooth

Follow this procedure if the format of the captions asset that you want to add is a
sidecar, as identified in [Step 4: Match formats to
categories](categories-captions.md "categories-captions.md"), or if the format is
SMPTE-TT for an MS Smooth output.

When you follow this procedure, you set up each captions asset in its own output
within the output group. When the event runs, the captions will be set up as sidecars in
the output package, except for SMPT-TT captions in MS Smooth, which will be set up as
streams in the output package.

###### To create captions (sidecar and SMPTE-TT)

1. On the web interface, on the **Event**
   screen, click the output group. (You should have already created
   this output group).
2. In the output group, choose **Add Output**.
   A new output appears, and by default this output has one stream.
   Make note of this stream. For example, **Stream
   2**.
3. In the **Streams** section (for example, in
   **Stream 2**), hover over
   **Video** and choose the **x**
   icon. Hover over **Audio** and choose the
   **x** icon. The stream is now empty.
4. Beside **Captions**, choose the
   **+** icon. The stream now contains one
   captions encode and no video or audio encodes.
5. Complete the fields as shown in the table after this
   procedure.
6. Repeat these steps to create more sidecar captions in this or
   another output group, as applicable.
7. When you are ready, save the event.

If the “Caption Stream Incompatible” message appears, see
["Caption
Stream Incompatible" message](output-embedded-and-more.md#embedded-caption-incompatible-message "output-embedded-and-more.md#embedded-caption-incompatible-message").

| Field                                  | Applicability                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Caption Source                         | All                             | Select the Caption Selector you created [earlier](create-caption-selectors.md "create-caption-selectors.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Destination Type                       | All                             | Select the caption type. This type must be valid for<br>your output type as per the relevant Supported Captions<br>table. See [Reference: Supported captions](supported-captions.md "supported-captions.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Optical Character Recognition Language | The Destination Type is WebVTT  | Complete this field only if the source captions in<br>the chosen Caption Selector are DVB-Sub or SCTE-27.<br>Specify the language of the captions in the source.<br>This captions conversion uses OCR (optical character<br>recognition) technology. You must identify the language<br>of the captions to ensure that Elemental Live chooses the<br>correct OCR library for the conversion. The library<br>speeds up conversion because it allows checking<br>character strings against a dictionary, instead of<br>recognizing words letter by letter. If you choose a<br>language that doesn’t match the language of the<br>captions, conversion accuracy will be poor.<br>Elemental Live ignores this field if you aren't<br>converting DVB-Sub or SCTE-27 captions to WebVTT.<br>For a list of languages supported with OCR<br>conversion, see [Reference: Languages supported<br>with OCR captions](captions-ocr-languages.md "captions-ocr-languages.md"). |
| Framerate                              | The Destination Type is SCC.    | Complete this field to ensure that the captions and<br>the video are synchronized in the output.<br>Specify a framerate that matches the framerate of<br>the associated video.<br>• If the video framerate is 23.97 or 24, choose<br>the corresponding option.<br>• If the video framerate is 29.97, choose 29.97<br>dropframe only if the video has the Video Insertion<br>and Drop Frame Timecode both.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Pass-style                             | The Destination Type is TTML    | Complete this field only if:<br>• The source caption type is TTML, or SMPTE-TT, or<br>CCF-TT.<br>• And the output is an Archive output.<br>Complete as follows:<br>• Check this box if you want the style (font,<br>position and so on) of the input captions to be<br>copied.<br>• Leave unchecked if you want a simplified caption<br>style. Some client players work best with a<br>simplified caption style.<br>(For other combinations of source caption types and<br>output caption type, the output is always<br>simplified.)                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Font style fields                      | The Destination Type is Burn-in | See the table in [Font styles for<br>Burn-in or DVB-Sub Captions](font-styles-for-burn-in-or-dvbsub.md "font-styles-for-burn-in-or-dvbsub.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Language                               | All                             | Complete if desired. This information may be useful<br>to or required by a downstream system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Description                            | All                             | Complete if desired. This information may be useful<br>to or required by a downstream system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## "Caption

Stream Incompatible" message

When you save the event, this validation message might appear:

Stream Caption Destination Type Is Incompatible With XX Output...

Typically, this error will occur because of the following scenario:

- You have two outputs – perhaps HLS and RTMP – that will have the same audio and
  video descriptions, which means you want them to share the same stream:
- You set up the HLS output group and add an Output and Stream 1. You add embedded
  captions.
- You then set up the RTMP output group and add an Output and associate that
  output with the existing Stream 1.
- The problem is that RTMP cannot contain embedded captions. Therefore, when you
  save the event, you will get the validation message.

The solution to this problem is:

- When you set up the RTMP output, instead of associating it with the existing
  Stream 1, create a new stream (Stream 2)
- In Stream 2, set up the video and audio to be identical to the video and audio
  in Stream 1.
- For the RTMP output, add the captions in the appropriate way.

The result: Assuming that you have set up the video and audio in both streams to be
identical, the encoder will notice that they are identical and will in fact encode the
video only once and the audio only once. So there will be no extra video encoding load
from creating separate streams.
