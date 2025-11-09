# Captions formats supported in

Microsoft Smooth outputs

In this table, look up your input container and captions type. Then read across to
find the caption formats that are supported in MediaLive in a Microsoft Smooth output, when
you have this input container and captions type.

| Source caption container                                                        | Source caption input        | Supported output captions   |
| ------------------------------------------------------------------------------- | --------------------------- | --------------------------- |
| CDI container                                                                   | ARIB                        | None                        |
| Embedded                                                                        | Burn-inEBU-TTSMPTE-TTTTML   |
| Teletext                                                                        | Burn-inEBU-TTSMPTE-TTTTML   |
| HLS container                                                                   | Embedded                    | Burn-inEBU-TT-DSMPTE-TTTTML |
| SCTE-20                                                                         | Burn-inEBU-TT-DSMPTE-TTTTML |
| Link container                                                                  | Embedded                    | Burn-inEBU-TT-DSMPTE-TTTTML |
| Teletext                                                                        | Burn-inSMPTE-TTTTML         |
| MP4 container                                                                   | Ancillary                   | Burn-inEBU-TT-DSMPTE-TTTTML |
| Embedded or Embedded+SCTE-20                                                    | Burn-inEBU-TT-DSMPTE-TTTTML |
| RTMP container                                                                  | Embedded                    | Burn-inEBU-TT-DSMPTE-TTTTML |
| MPEG-TS container (through MediaConnect or through<br>the RTP or SRT protocols) | ARIB                        | None                        |
| DVB-Sub                                                                         | SMPTE-TT                    |
| Embedded or Embedded+SCTE-20                                                    | Burn-inEBU-TT-DSMPTE-TTTTML |
| SCTE-20                                                                         | Burn-inEBU-TT-DSMPTE-TTTTML |
| SCTE-27                                                                         | Burn-in<br>SMPTE-TT         |
| Teletext                                                                        | Burn-inEBU-TT-DSMPTE-TTTTML |
| SMPTE 2110                                                                      | Embedded                    | Burn-inSMPTE-TTTTML         |
| Teletext                                                                        | Burn-inSMPTE-TTWebVTT       |
