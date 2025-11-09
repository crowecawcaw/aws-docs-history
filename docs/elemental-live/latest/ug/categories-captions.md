# Step 4: Match formats to

categories

There are different procedures to follow to create captions encodes in the output. The
correct procedure depends on the "category" that the output captions belong to. There are
five categories of captions, described in the following table.

On the list of outputs that you have created, make a note of the category that each
captions option belongs to.

| Format of output captions | Category of this format                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ancillary+Embedded        | The captions in ancillary format are in the ancillary data in the stream. The<br>embedded captions are embedded in the video. To choose Ancillary+Embedded,<br>choose **Embedded\*<br>• as the **Destination Type\*<br>• (in the [procedure](output-embedded-and-more.md "output-embedded-and-more.md")).<br>Elemental Live will automatically produce both Ancillary and embedded. |
| ARIB                      | Object                                                                                                                                                                                                                                                                                                                                                                              |
| Burn-in                   | Burn-in                                                                                                                                                                                                                                                                                                                                                                             |
| DVB-Sub                   | Object                                                                                                                                                                                                                                                                                                                                                                              |
| Embedded                  | Embedded                                                                                                                                                                                                                                                                                                                                                                            |
| Embedded+SCTE-20          | Embedded                                                                                                                                                                                                                                                                                                                                                                            |
| RTMP CaptionInfo          | Object                                                                                                                                                                                                                                                                                                                                                                              |
| RTMP CuePoint             | Object                                                                                                                                                                                                                                                                                                                                                                              |
| SCC                       | Sidecar                                                                                                                                                                                                                                                                                                                                                                             |
| SCTE-20+Embedded          | Embedded                                                                                                                                                                                                                                                                                                                                                                            |
| SCTE-27                   | Object                                                                                                                                                                                                                                                                                                                                                                              |
| SMI                       | Sidecar                                                                                                                                                                                                                                                                                                                                                                             |
| SMPTE-TT                  | Sidecar when in Archive                                                                                                                                                                                                                                                                                                                                                             |
| SMPTE-TT                  | Stream when in MS Smooth                                                                                                                                                                                                                                                                                                                                                            |
| SRT                       | Sidecar                                                                                                                                                                                                                                                                                                                                                                             |
| teletext                  | Object                                                                                                                                                                                                                                                                                                                                                                              |
| TTML wrapped in ID3 data  | Wrapped in ID3 data                                                                                                                                                                                                                                                                                                                                                                 |
| TTML                      | Sidecar                                                                                                                                                                                                                                                                                                                                                                             |
| WebVTT                    | Sidecar                                                                                                                                                                                                                                                                                                                                                                             |

For example, your list of outputs might now look like this:

- MS Smooth output with TTML captions (sidecar) in Czech.
- MS Smooth output with TTML captions (sidecar) in Polish.
- HLS output with WebVTT captions (sidecar) in Czech.
- HLS output with WebVTT captions (sidecar) in Polish.

## Captions embedded in video

The captions are carried inside the video encode, which is itself in an output in the
output group. Only one captions asset ever exists within that video encode. That single
asset might contain captions for several languages.

## Captions object

The captions are in their own "captions encode" in an output in the output group. They
are not part of the video encode. However, they are in the same output as their
corresponding video and audio encodes. There might be several captions encodes in the
output, for example, for different languages.

## Sidecar

The captions are each in their own output in the output group, separate from the
output that contains the video and audio. Each captions output contains only one captions
asset (file), meaning that it is a "captions-only" output. The output group might contain
several "captions-only" outputs, for example, one for each language in the output
group.

## TTML captions wrapped in ID3

data

The captions are converted to TTML and included in ID3 data. (The other way to
produce TTML output is as a sidecar.)

## SMPTE-TT in MS Smooth

The captions are handled as a separate stream in MS Smooth.

Note that SMPTE-TT captions for other package types are handled as sidecars. However,
for both sidecar handling and stream handling, the [procedure for setting up](output-sidecar-and-smptett-mss.md "output-sidecar-and-smptett-mss.md") SMPTE-TT
captions in the output is identical. Elemental Live will package the SMPTE-TT captions
correctly for the package type.

## Burn-in

Here, the captions are converted into text and then overlaid on the picture directly
in the video encode. Strictly speaking, once the overlay occurs, these are not really
captions because they are indistinguishable from the video.
