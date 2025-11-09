# Captions formats supported in RTMP

outputs

In this table, look up your input container and captions type. Then read across to
find the caption formats that are supported in MediaLive in an RTMP output, when you have
this input container and captions type.

| Source caption container                                                        | Source caption input               | Supported output captions                                                 |
| ------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------- |
| CDI container                                                                   | ARIB                               | None                                                                      |
| Embedded                                                                        | Burn-inEmbeddedRTMP<br>CaptionInfo |
| Teletext                                                                        | None                               |
| HLS container                                                                   | Embedded                           | Burn-inEmbeddedRTMP<br>CaptionInfo                                        |
| SCTE-20                                                                         | Embedded                           |
| Link container                                                                  | Embedded                           | Burn-inEmbeddedRTMP<br>CaptionInfo                                        |
| Teletext                                                                        | None                               |
| MP4 container                                                                   | Ancillary                          | Burn-inEmbeddedRTMP<br>CaptionInfo                                        |
| Embedded or Embedded+SCTE-20                                                    | Burn-inEmbeddedRTMP<br>CaptionInfo |
| RTMP container                                                                  | Embedded                           | Burn-inEmbeddedRTMP<br>CaptionInfo                                        |
| MPEG-TS container (through MediaConnect or through<br>the RTP or SRT protocols) | ARIB                               | None                                                                      |
| DVB-Sub                                                                         | Burn-in                            |
| Embedded or Embedded+SCTE-20                                                    | Burn-inEmbeddedRTMP<br>CaptionInfo |
| SCTE-20                                                                         | EmbeddedRTMP CaptionInfo           |
| SCTE-27                                                                         | Burn-in                            |
| Teletext                                                                        | None                               |
| SMPTE 2110                                                                      | Embedded                           | Burn-inRTMP<br>CaptionInfoEmbeddedEmbedded+SCTE-20SCTE-20SCTE-20+Embedded |
| Teletext                                                                        | None                               |
