# Supported input captions, within sidecar files

The following tables show the captions formats you can create in your
outputs when your input captions are in a sidecar format. _Sidecar
captions_ are captions that you provide as a separate input file from your
video.

To see whether MediaConvert supports your captions workflow, go to the table for your video
output container. MediaConvert doesn't support every possible file extension for each sidecar
format.

###### Topics

- [Sidecar captions supported in CMAF output
  container](#sidecar-cmaf-output-container "#sidecar-cmaf-output-container")
- [Sidecar captions supported in DASH output
  container](#sidecar-dash-output-container "#sidecar-dash-output-container")
- [Sidecar captions supported in HLS output
  container](#sidecar-hls-output-container "#sidecar-hls-output-container")
- [Sidecar captions supported in Microsoft Smooth
  Streaming (MSS) output container](#sidecar-mss-output-container "#sidecar-mss-output-container")
- [Sidecar captions supported in MP4 output
  container](#sidecar-mp4-output-container "#sidecar-mp4-output-container")
- [Sidecar captions supported in MPEG2-TS
  File output container](#sidecar-mpeg2-ts-output-container "#sidecar-mpeg2-ts-output-container")
- [Sidecar captions supported in MXF output
  container](#sidecar-mxf-output-container "#sidecar-mxf-output-container")
- [Sidecar captions supported in QuickTime
  output container](#sidecar-quicktime-output-container "#sidecar-quicktime-output-container")
- [Sidecar captions
  supported with File output groups](#sidecar-captions-supported-as-standalone-file-in-output "#sidecar-captions-supported-as-standalone-file-in-output")

## Sidecar captions supported in CMAF output

container

The following table lists supported output captions formats for this output container when your input captions are in a sidecar format. _Sidecar_ captions are captions that are in a separate file from your video.

| Input captions format | Supported file extensions | Supported output captions formats |
| --------------------- | ------------------------- | --------------------------------- |
| IMSC1 text profile    | .xml                      | IMSC (as sidecar .fmp4)<br>WebVTT |
| SCC                   | .scc                      | IMSC (as sidecar .fmp4)<br>WebVTT |
| SMI                   | .smi                      | IMSC (as sidecar .fmp4)<br>WebVTT |
| SMPTE-TT              | .ttml, .xml, .dfxp        | IMSC (as sidecar .fmp4)<br>WebVTT |
| SRT                   | .srt                      | IMSC (as sidecar .fmp4)<br>WebVTT |
| EBU STL               | .stl                      | IMSC (as sidecar .fmp4)<br>WebVTT |
| TTML                  | .ttml, .xml, .dfxp        | IMSC (as sidecar .fmp4)<br>WebVTT |
| WebVTT                | .vtt                      | IMSC (as sidecar .fmp4)<br>WebVTT |

## Sidecar captions supported in DASH output

container

The following table lists supported output captions formats for this output container when your input captions are in a sidecar format. _Sidecar_ captions are captions that are in a separate file from your video.

| Input captions format | Supported file extensions | Supported output captions formats                                                                                  |
| --------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| IMSC1 text profile    | .xml                      | Burn in<br>IMSC (as sidecar .fmp4)<br>IMSC (as sidecar .xml)<br>TTML (as sidecar .fmp4)<br>TTML (as sidecar .ttml) |
| SCC                   | .scc                      | Burn in<br>IMSC (as sidecar .fmp4)<br>IMSC (as sidecar .xml)<br>TTML (as sidecar .fmp4)<br>TTML (as sidecar .ttml) |
| SMI                   | .smi                      | Burn in<br>IMSC (as sidecar .fmp4)<br>IMSC (as sidecar .xml)<br>TTML (as sidecar .fmp4)<br>TTML (as sidecar .ttml) |
| SMPTE-TT              | .ttml, .xml, .dfxp        | Burn in<br>IMSC (as sidecar .fmp4)<br>IMSC (as sidecar .xml)<br>TTML (as sidecar .fmp4)<br>TTML (as sidecar .ttml) |
| SRT                   | .srt                      | Burn in<br>IMSC (as sidecar .fmp4)<br>IMSC (as sidecar .xml)<br>TTML (as sidecar .fmp4)<br>TTML (as sidecar .ttml) |
| EBU STL               | .stl                      | Burn in<br>IMSC (as sidecar .fmp4)<br>IMSC (as sidecar .xml)<br>TTML (as sidecar .fmp4)<br>TTML (as sidecar .ttml) |
| TTML                  | .ttml, .xml, .dfxp        | Burn in<br>IMSC (as sidecar .fmp4)<br>IMSC (as sidecar .xml)<br>TTML (as sidecar .fmp4)<br>TTML (as sidecar .ttml) |
| WebVTT                | .vtt                      | Burn in<br>IMSC (as sidecar .fmp4)<br>IMSC (as sidecar .xml)<br>TTML (as sidecar .fmp4)<br>TTML (as sidecar .ttml) |

## Sidecar captions supported in HLS output

container

The following table lists supported output captions formats for this output container when your input captions are in a sidecar format. _Sidecar_ captions are captions that are in a separate file from your video.

| Input captions format | Supported file extensions | Supported output captions formats                                               |
| --------------------- | ------------------------- | ------------------------------------------------------------------------------- |
| IMSC1 text profile    | .xml                      | Burn in<br>WebVTT                                                               |
| SCC                   | .scc                      | Burn in<br>Embedded<br>Embedded plus SCTE-20<br>SCTE-20 plus embedded<br>WebVTT |
| SMI                   | .smi                      | Burn in<br>WebVTT                                                               |
| SMPTE-TT              | .ttml, .xml, .dfxp        | Burn in<br>WebVTT                                                               |
| SRT                   | .srt                      | Burn in<br>WebVTT                                                               |
| EBU STL               | .stl                      | Burn in<br>WebVTT                                                               |
| TTML                  | .ttml, .xml, .dfxp        | Burn in<br>WebVTT                                                               |
| WebVTT                | .vtt                      | Burn in<br>WebVTT                                                               |

## Sidecar captions supported in Microsoft Smooth

Streaming (MSS) output container

The following table lists supported output captions formats for this output container when your input captions are in a sidecar format. _Sidecar_ captions are captions that are in a separate file from your video.

| Input captions format | Supported file extensions | Supported output captions formats |
| --------------------- | ------------------------- | --------------------------------- |
| IMSC1 text profile    | .xml                      | Burn in<br>TTML                   |
| SCC                   | .scc                      | Burn in<br>TTML                   |
| SMI                   | .smi                      | Burn in<br>TTML                   |
| SMPTE-TT              | .ttml, .xml, .dfxp        | Burn in<br>TTML                   |
| SRT                   | .srt                      | Burn in<br>TTML                   |
| EBU STL               | .stl                      | Burn in<br>TTML                   |
| TTML                  | .ttml, .xml, .dfxp        | Burn in<br>TTML                   |
| WebVTT                | .vtt                      | Burn in<br>TTML                   |

## Sidecar captions supported in MP4 output

container

The following table lists supported output captions formats for this output container when your input captions are in a sidecar format. _Sidecar_ captions are captions that are in a separate file from your video.

| Input captions format | Supported file extensions | Supported output captions formats                                     |
| --------------------- | ------------------------- | --------------------------------------------------------------------- |
| IMSC1 text profile    | .xml                      | Burn in                                                               |
| SCC                   | .scc                      | Burn in<br>Embedded<br>Embedded plus SCTE-20<br>SCTE-20 plus embedded |
| SMI                   | .smi                      | Burn in                                                               |
| SMPTE-TT              | .ttml, .xml, .dfxp        | Burn in<br>TTML                                                       |
| SRT                   | .srt                      | Burn in                                                               |
| EBU STL               | .stl                      | Burn in                                                               |
| TTML                  | .ttml, .xml, .dfxp        | Burn in                                                               |
| WebVTT                | .vtt                      | Burn in                                                               |

## Sidecar captions supported in MPEG2-TS

File output container

The following table lists supported output captions formats for this output container when your input captions are in a sidecar format. _Sidecar_ captions are captions that are in a separate file from your video.

| Input captions format | Supported file extensions | Supported output captions formats                                                            |
| --------------------- | ------------------------- | -------------------------------------------------------------------------------------------- |
| IMSC1 text profile    | .xml                      | Burn in<br>Teletext<br>DVB-Sub                                                               |
| SCC                   | .scc                      | Burn in<br>DVB-Sub<br>Embedded<br>Embedded plus SCTE-20<br>SCTE-20 plus embedded<br>Teletext |
| SMI                   | .smi                      | Burn in<br>DVB-Sub                                                                           |
| SMPTE-TT              | .ttml, .xml, .dfxp        | Burn in<br>Teletext<br>DVB-Sub                                                               |
| SRT                   | .srt                      | Burn in<br>Teletext                                                                          |
| EBU STL               | .stl                      | Burn in<br>Teletext<br>DVB-Sub                                                               |
| TTML                  | .ttml, .xml, .dfxp        | Burn in<br>Teletext<br>DVB-Sub                                                               |
| WebVTT                | .vtt                      | Burn in<br>Teletext<br>DVB-Sub                                                               |

## Sidecar captions supported in MXF output

container

The following table lists supported output captions formats for this output container when your input captions are in a sidecar format. _Sidecar_ captions are captions that are in a separate file from your video.

| Input captions format | Supported file extensions | Supported output captions formats                                                 |
| --------------------- | ------------------------- | --------------------------------------------------------------------------------- |
| IMSC1 text profile    | .xml                      | Burn in<br>Teletext                                                               |
| SCC                   | .scc                      | Burn in<br>Embedded<br>Embedded plus SCTE-20<br>SCTE-20 plus embedded<br>Teletext |
| SMI                   | .smi                      | Burn in                                                                           |
| SMPTE-TT              | .ttml, .xml, .dfxp        | Burn in                                                                           |
| SRT                   | .srt                      | Burn in<br>Teletext                                                               |
| EBU STL               | .stl                      | Burn in<br>Teletext                                                               |
| TTML                  | .ttml, .xml, .dfxp        | Burn in<br>Teletext                                                               |
| WebVTT                | .vtt                      | Burn in<br>Teletext                                                               |

## Sidecar captions supported in QuickTime

output container

The following table lists supported output captions formats for this output container when your input captions are in a sidecar format. _Sidecar_ captions are captions that are in a separate file from your video.

| Input captions format | Supported file extensions | Supported output captions formats                                     |
| --------------------- | ------------------------- | --------------------------------------------------------------------- |
| IMSC1 text profile    | .xml                      | Burn in                                                               |
| SCC                   | .scc                      | Burn in<br>Embedded<br>Embedded plus SCTE-20<br>SCTE-20 plus embedded |
| SMI                   | .smi                      | Burn in                                                               |
| SMPTE-TT              | .ttml, .xml, .dfxp        | Burn in                                                               |
| SRT                   | .srt                      | Burn in                                                               |
| EBU STL               | .stl                      | Burn in                                                               |
| TTML                  | .ttml, .xml, .dfxp        | Burn in                                                               |
| WebVTT                | .vtt                      | Burn in                                                               |

## Sidecar captions

supported with File output groups

The following table lists standalone sidecar output captions formats that MediaConvert
supports with outputs in the **File** output group.
_Sidecar_ captions are captions that are in a separate file from your video.

When you set up these output captions in your job, choose **No
container** (`RAW`) for **Container**, under
**Output settings**. In your JSON job specification, specify it this
way:

```
 {
            "ContainerSettings": {
              "Container": "RAW"
            },
```

###### Note

You can create sidecar captions outputs only as part of a job that also generates a video
output.

| Input captions format | Supported file extensions | Supported output captions formats                              |
| --------------------- | ------------------------- | -------------------------------------------------------------- |
| IMSC1 text profile    | .xml                      | IMSC (as sidecar .xml)<br>IMSC<br>SRT<br>SMI<br>TTML<br>WebVTT |
| SCC                   | .scc                      | IMSC (as sidecar .xml)<br>SCC<br>SRT<br>SMI<br>TTML<br>WebVTT  |
| SMI                   | .smi                      | IMSC (as sidecar .xml)<br>SRT<br>SMI<br>TTML<br>WebVTT         |
| SMPTE-TT              | .ttml, .xml, .dfxp        | IMSC (as sidecar .xml)<br>SRT<br>SMI<br>TTML<br>WebVTT         |
| SRT                   | .srt                      | IMSC (as sidecar .xml)<br>IMSC<br>SRT<br>SMI<br>TTML<br>WebVTT |
| EBU STL               | .stl                      | IMSC (as sidecar .xml)<br>SRT<br>SMI<br>TTML<br>WebVTT         |
| TTML                  | .ttml, .xml, .dfxp        | IMSC (as sidecar .xml)<br>SRT<br>SMI<br>TTML<br>WebVTT         |
| WebVTT                | .vtt                      | IMSC (as sidecar .xml)<br>SRT<br>SMI<br>TTML<br>WebVTT         |
