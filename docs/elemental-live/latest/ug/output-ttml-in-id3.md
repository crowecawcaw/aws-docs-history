# TTML captions wrapped in ID3

data

Follow this procedure to produce an output that includes TTML captions wrapped in ID3
data. This format is supported only in an MSS output. Unlike unwrapped TTML captions
(which you create as described in [Sidecar captions or
SMPTE-TT captions in MS Smooth](output-sidecar-and-smptett-mss.md "output-sidecar-and-smptett-mss.md")), these
captions are included as an ID3 object in the same stream as the video.

###### To produce TTML captions wrapped in ID3 data

1. On the web interface, on the Event screen, click the appropriate output group.
2. In the output group, go to the output where you want to add captions.
3. Identify the stream that is associated with that output. In this example, there
   are two outputs; the first is associated with stream 1, the second is associated with
   stream 2.
4. Go to that Stream section. For example, go to Stream 1.
5. Click the + beside Caption to add a Caption section.
6. Complete the fields as shown in the table that follows this procedure.
7. Repeat these steps to add more captions for this output. For example, to add
   captions in another language.
8. Go to the MSS output group and output that this stream belongs to. Set the Stream
   field in that output to match the stream you created. For example:
9. When you are ready, save the event.

If the “Caption Stream Incompatible” message appears, see ["Caption
Stream Incompatible" message](output-sidecar-and-smptett-mss.md#sidecar-caption-incompatible-message "output-sidecar-and-smptett-mss.md#sidecar-caption-incompatible-message").

| Field                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Caption Source             | Select the Caption Selector you created when [specifying the input captions](create-caption-selectors.md "create-caption-selectors.md").                                                                                                                                                                                                                                                                                                                                                       |
| Destination Type           | Select the caption type. This type must be valid for your output type as per the relevant Supported Captions table.                                                                                                                                                                                                                                                                                                                                                                            |
| Pass Style Information     | Applicable only if the source caption type is an Embedded combination (Embedded, Embedded+SCTE-20, SCTE-20+Embedded), or Teletext, or TTML, or SMPTE-TT, or CCF-TT. The choices are: <br>• Check this box if you want the style (font, position and so on) of the input captions to be copied. <br>• Leave unchecked if you want a simplified caption style. Some client players work best with a simplified caption style. (For other source caption types, the output is always simplified.) |
| Language                   | Complete if desired. This information may be useful to or required by a downstream system.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Description                | This field is automatically completed after you specify the language.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Use ID3 as Caption Content | Check this field, to insert the TTML captions into ID3 data.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
