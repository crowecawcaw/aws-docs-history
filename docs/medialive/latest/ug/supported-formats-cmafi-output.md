# Captions formats supported in CMAF

Ingest outputs

In this table, look up your input container and captions type. Then read across to
find the caption formats that are supported in MediaLive when you have this input container
and captions type, and produce these outputs:

- CMAF Ingest output
- MediaPackage output with a CMAF Ingest container

| Source caption container                                                        | Source caption input         | Supported output captions |
| ------------------------------------------------------------------------------- | ---------------------------- | ------------------------- |
| CDI container                                                                   | Embedded                     | Burn-in<br>TTML           |
| Teletext                                                                        | TTML                         |
| HLS container                                                                   | Embedded                     | Burn-inTTML               |
| SCTE-20                                                                         | Burn-in<br>TTML              |
| Link container                                                                  | Embedded                     | Burn-inTTML               |
| Teletext                                                                        | Burn-inTTML                  |
| MP4 container                                                                   | Ancillary                    | Burn-inTTML               |
| Embedded or Embedded+SCTE-20                                                    | Burn-inTTML                  |
| RTMP container                                                                  | Embedded                     | Burn-inTTML               |
| MPEG-TS container (through MediaConnect or through<br>the RTP or SRT protocols) | Embedded or Embedded+SCTE-20 | Burn-inTTML               |
| SCTE-20                                                                         | Burn-inTTML                  |
| Teletext                                                                        | Burn-inTTML                  |
| SMPTE 2110                                                                      | Embedded                     | Burn-inTTML               |
| Teletext                                                                        | Burn-inTTML                  |
