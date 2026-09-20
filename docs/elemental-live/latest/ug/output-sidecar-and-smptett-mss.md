

# Sidecar captions or SMPTE-TT captions in MS Smooth
<a name="output-sidecar-and-smptett-mss"></a>

Follow this procedure if the format of the captions asset that you want to add is a sidecar, as identified in [Step 4: Match formats to categories](categories-captions.md), or if the format is SMPTE-TT for an MS Smooth output.

When you follow this procedure, you set up each captions asset in its own output within the output group. When the event runs, the captions will be set up as sidecars in the output package, except for SMPT-TT captions in MS Smooth, which will be set up as streams in the output package.

**To create captions (sidecar and SMPTE-TT)**

1. On the web interface, on the **Event** screen, click the output group. (You should have already created this output group).

1. In the output group, choose **Add Output**. A new output appears, and by default this output has one stream. Make note of this stream. For example, **Stream 2**.

1. In the **Streams** section (for example, in **Stream 2**), hover over **Video** and choose the **x** icon. Hover over **Audio** and choose the **x** icon. The stream is now empty. 

1. Beside **Captions**, choose the **\+** icon. The stream now contains one captions encode and no video or audio encodes.

1. Complete the fields as shown in the table after this procedure.

1. Repeat these steps to create more sidecar captions in this or another output group, as applicable.

1. When you are ready, save the event.

   If the “Caption Stream Incompatible” message appears, see ["Caption Stream Incompatible" message](output-embedded-and-more.md#embedded-caption-incompatible-message).


<table>
<thead>
  <tr><th>Field</th><th>Applicability</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Caption Source</td><td>All</td><td>Select the Caption Selector you created <a href="create-caption-selectors.md">earlier</a>.</td></tr>
  <tr><td>Destination Type</td><td>All</td><td>Select the caption type. This type must be valid for your output type as per the relevant Supported Captions table. See <a href="supported-captions.md">Reference: Supported captions</a>.</td></tr>
  <tr><td>Optical Character Recognition Language</td><td>The Destination Type is WebVTT</td><td>Complete this field only if the source captions in the chosen Caption Selector are DVB-Sub or SCTE-27. <br />Specify the language of the captions in the source. This captions conversion uses OCR (optical character recognition) technology. You must identify the language of the captions to ensure that Elemental Live chooses the correct OCR library for the conversion. The library speeds up conversion because it allows checking character strings against a dictionary, instead of recognizing words letter by letter. If you choose a language that doesn’t match the language of the captions, conversion accuracy will be poor. <br />Elemental Live ignores this field if you aren't converting DVB-Sub or SCTE-27 captions to WebVTT.<br />For a list of languages supported with OCR conversion, see <a href="captions-ocr-languages.md">Reference: Languages supported with OCR captions</a>.</td></tr>
  <tr><td>Framerate</td><td>The Destination Type is SCC.</td><td>Complete this field to ensure that the captions and the video are synchronized in the output.<br />Specify a framerate that matches the framerate of the associated video.<ul><li> If the video framerate is 23.97 or 24, choose the corresponding option. </li><li> If the video framerate is 29.97, choose 29.97 dropframe only if the video has the Video Insertion and Drop Frame Timecode both. </li></ul></td></tr>
  <tr><td>Pass-style</td><td>The Destination Type is TTML</td><td>Complete this field only if:<ul><li> The source caption type is TTML, or SMPTE-TT, or CCF-TT. </li><li> And the output is an Archive output. </li></ul><br />Complete as follows:<ul><li> Check this box if you want the style (font, position and so on) of the input captions to be copied. </li><li> Leave unchecked if you want a simplified caption style. Some client players work best with a simplified caption style. </li></ul><br />(For other combinations of source caption types and output caption type, the output is always simplified.)</td></tr>
  <tr><td>Font style fields</td><td>The Destination Type is Burn-in</td><td>See the table in <a href="font-styles-for-burn-in-or-dvbsub.md">Font styles for Burn-in or DVB-Sub Captions</a>.</td></tr>
  <tr><td>Language</td><td>All</td><td>Complete if desired. This information may be useful to or required by a downstream system.</td></tr>
  <tr><td>Description</td><td>All</td><td>Complete if desired. This information may be useful to or required by a downstream system.</td></tr>
</tbody>
</table>


## "Caption Stream Incompatible" message
<a name="sidecar-caption-incompatible-message"></a>

When you save the event, this validation message might appear:

Stream Caption Destination Type Is Incompatible With XX Output...

Typically, this error will occur because of the following scenario:
+ You have two outputs – perhaps HLS and RTMP – that will have the same audio and video descriptions, which means you want them to share the same stream:
+ You set up the HLS output group and add an Output and Stream 1. You add embedded captions.
+ You then set up the RTMP output group and add an Output and associate that output with the existing Stream 1.
+ The problem is that RTMP cannot contain embedded captions. Therefore, when you save the event, you will get the validation message.

The solution to this problem is:
+ When you set up the RTMP output, instead of associating it with the existing Stream 1, create a new stream (Stream 2)
+ In Stream 2, set up the video and audio to be identical to the video and audio in Stream 1.
+ For the RTMP output, add the captions in the appropriate way.

The result: Assuming that you have set up the video and audio in both streams to be identical, the encoder will notice that they are identical and will in fact encode the video only once and the audio only once. So there will be no extra video encoding load from creating separate streams.