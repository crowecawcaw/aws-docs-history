

# All captions except sidecar or SMPTE-TT in MS Smooth
<a name="output-embedded-and-more"></a>

Follow this procedure if the format of the captions asset that you want to add belongs to the category of embedded, burn-in, or object. You will set up the captions and video and audio in the same output.

**To create captions (*not* sidecar or SMPTE-TT)**

1. On the web interface, on the **Event** screen, click the appropriate output group.

1. If you have already set up this output group with video and audio, find the outputs where you want to add the captions. Or if you have not set up with video and audio, create a new output in this output group; you can set up the captions now and you can set up the video and audio later.

1. Go to the output, then go to the stream that is associated with that output. For example, go to Stream 1.

1. Click the \+ beside **Caption** to add a Caption section.

1. Complete the fields that appear for the selected format. For details about a field, choose the Info link beside the field. 


<table>
<thead>
  <tr><th>Field</th><th>Applicability</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Caption Source</td><td>All formats</td><td>Select the Caption Selector that you created when you specified the input captions.</td></tr>
  <tr><td>Destination Type</td><td>All formats</td><td>Select the caption type.</td></tr>
  <tr><td>Pass Style Information</td><td>If Destination Type is CCF-TT or TTML.<br />And if the source caption type is an Embedded combination (Embedded, Embedded+SCTE-20, SCTE-20+Embedded), or Teletext, or TTML, or SMPTE-TT, or CCF-TT.</td><td>The choices are:<ul><li> Check this box if you want the style (font, position and so on) of the input captions to be copied. </li><li> Leave unchecked if you want a simplified caption style. Some client players work best with a simplified caption style. </li></ul><br />(For other combinations of source caption types and output caption type, the output is always simplified.)</td></tr>
  <tr><td>Font style fields</td><td>Destination type is Burn-in or DVB-Sub</td><td>For tips about font styles in DVB-Sub or burn-in, see <a href="font-styles-for-burn-in-or-dvbsub.md">Font Styles for Burn-in or DVB-Sub Output</a>.</td></tr>
  <tr><td>Language</td><td>All captions except not for embedded-to-embedded or teletext-to-teletext.</td><td>Complete if desired. This information may be useful to or required by a downstream system.<br />For embedded-to-embedded or teletext-to-teletext, leave as Undefined.</td></tr>
  <tr><td>Description</td><td>All captions except not for embedded-to-embedded.</td><td>This field is auto-completed after you specify the language.</td></tr>
  <tr><td>Use ID3 as Caption Content</td><td>Destination type is TTML<br />And if this stream is associated with an MS Smooth output.</td><td>Leave unchecked.<br />This field applies only when wrapping TTML captions in ID3; see <a href="output-ttml-in-id3.md">TTML captions wrapped in ID3 data</a>.</td></tr>
</tbody>
</table>


1. If the output format is embedded and the output group is HLS, you can include captions language information in the manifest. You perform this setup in the output settings (separate from the captions encode). See [Set up the HLS Manifest (embedded captions)](set-up-the-hls-manifest.md).

1. If the output format is ARIB or DVB-Sub or SCTE-27, you must perform some extra setup in the output settings (separate from the captions encode). See [PIDS for ARIB output](complete-the-pids-for-arib.md) or [PIDs for DVB-Sub output](complete-the-pids-for-dvb-sub.md) or [PIDs for teletext output](complete-the-pids-for-teletext.md).

1. You now have a captions encode that is fully defined.

1. Repeat these steps to create captions, as applicable.

1. Go to the output group and output that this stream belongs to. Set the Stream field in that output to match the stream you created. 

1. When you are ready, save the event. 

   If the “Caption Stream Incompatible” message appears, see ["Caption Stream Incompatible" message](#embedded-caption-incompatible-message).

## "Caption Stream Incompatible" message
<a name="embedded-caption-incompatible-message"></a>

When you save the event, this validation message might appear:

Stream Caption Destination Type Is Incompatible With XX Output...

Typically, this error will occur because of the following scenario:
+ You have two outputs – perhaps HLS and DASH – that will have the same audio and video descriptions, which means you want them to share the same stream:
+ You set up the HLS output group and add an Output and Stream 1. You add embedded captions.
+ You then set up the DASH output group and add an Output and associate that output with the existing Stream 1.
+ The problem is that DASH cannot contain embedded captions. Therefore, when you save the event, you will get the validation message.

The solution to this problem is:
+ When you set up the DASH output, instead of associating it with the existing Stream 1, create a new stream (Stream 2)
+ In Stream 2, set up the video and audio to be identical to the video and audio in Stream 1.
+ For the DASH output, add the captions in the appropriate way.

The result: Assuming that you have set up the video and audio in both streams to be identical, the encoder will notice that they are identical and will in fact encode the video only once and the audio only once. So there will be no extra video encoding load from creating separate streams.