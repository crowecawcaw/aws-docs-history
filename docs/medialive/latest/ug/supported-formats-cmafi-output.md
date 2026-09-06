# Captions formats supported in CMAF Ingest outputs

In this table, look up your input container and captions type. Then read across to
find the caption formats that are supported in MediaLive when you have this input container
and captions type, and produce these outputs:

- CMAF Ingest output
- MediaPackage output with a CMAF Ingest container

###### Note

You can also produce subtitles without a caption source in your input.
Enable the Smart Subtitles feature, which uses AWS Elemental Inference to generate
TTML or WebVTT subtitles from the audio. For more information, see [Smart Subtitles using Elemental Inference](elemental-inference-automatic-subtitling.md "elemental-inference-automatic-subtitling.md").

| Source caption container                                                                                          | Source caption input         | Supported output captions |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------- |
| CDI container                                                                                                     | Embedded                     | Burn-in<br>TTML<br>WebVTT |
| Teletext                                                                                                          | TTML<br>WebVTT               |
| HLS container                                                                                                     | Embedded                     | Burn-inTTMLWebVTT         |
| SCTE-20                                                                                                           | Burn-in<br>TTML<br>WebVTT    |
| Link container                                                                                                    | Embedded                     | Burn-inTTMLWebVTT         |
| Teletext                                                                                                          | Burn-inTTMLWebVTT            |
| MP4 container                                                                                                     | Ancillary                    | Burn-inTTMLWebVTT         |
| Embedded or Embedded+SCTE-20                                                                                      | Burn-inTTMLWebVTT            |
| RTMP container                                                                                                    | Embedded                     | Burn-inTTMLWebVTT         |
| MPEG-TS container (through MediaConnect or through<br>the RTP or SRT protocols)                                   | Embedded or Embedded+SCTE-20 | Burn-inTTMLWebVTT         |
| SCTE-20                                                                                                           | Burn-inTTMLWebVTT            |
| Teletext                                                                                                          | Burn-inTTMLWebVTT            |
| SMPTE 2110                                                                                                        | Embedded                     | Burn-inTTMLWebVTT         |
| Teletext                                                                                                          | Burn-inTTMLWebVTT            |
| All input containers(Smart Subtitles generates subtitles from the source audio, not from captions in the source.) | Smart Subtitles              | TTMLWebVTT                |
