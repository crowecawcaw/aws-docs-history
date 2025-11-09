# Captions formats supported in

UDP,
SRT, or multiplex outputs

In this table, look up your input container and captions type. Then read across to
find the caption formats that are supported in MediaLive in an MPEG-TS streaming
output
or in an MPTS multiplex output, when you have this input container and captions type.

| Source caption container                                                        | Source caption input                                                              | Supported output captions                                                         |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| CDI container                                                                   | ARIB                                                                              | ARIB                                                                              |
| Embedded                                                                        | Burn-inDVB-SubEmbeddedEmbedded+SCTE-20SCTE-20                                     |
| Teletext                                                                        | Burn-in<br>DVB-Sub<br>Teletext                                                    |
| HLS container                                                                   | Embedded                                                                          | Burn-inDVB-SubEmbeddedEmbedded+SCTE-20SCTE-20SCTE-20+Embedded                     |
| SCTE-20                                                                         | Burn-in<br>DVB-Sub<br>Embedded<br>Embedded+SCTE-20<br>SCTE-20<br>SCTE-20+Embedded |
| Link container                                                                  | Embedded                                                                          | Burn-in<br>DVB-Sub<br>Embedded<br>Embedded+SCTE-20<br>SCTE-20<br>SCTE-20+Embedded |
| Teletext                                                                        | Burn-inDVB-Sub                                                                    |
| MP4 container                                                                   | Ancillary                                                                         | Burn-in<br>DVB-Sub<br>Embedded<br>Embedded+SCTE-20<br>SCTE-20<br>SCTE-20+Embedded |
| Embedded or Embedded+SCTE-20                                                    | Burn-in<br>DVB-Sub<br>Embedded<br>Embedded+SCTE-20<br>SCTE-20<br>SCTE-20+Embedded |
| RTMP container                                                                  | Embedded                                                                          | Burn-in<br>DVB-Sub<br>Embedded<br>Embedded+SCTE-20<br>SCTE-20<br>SCTE-20+Embedded |
| MPEG-TS container (through MediaConnect or through<br>the RTP or SRT protocols) | ARIB                                                                              | ARIB                                                                              |
| DVB-Sub                                                                         | Burn-in<br>DVB-Sub                                                                |
| Embedded or Embedded+SCTE-20                                                    | Burn-in<br>DVB-Sub<br>Embedded<br>Embedded+SCTE-20<br>SCTE-20<br>SCTE-20+Embedded |
| SCTE-20                                                                         | Burn-in<br>DVB-Sub<br>Embedded<br>Embedded+SCTE-20<br>SCTE-20<br>SCTE-20+Embedded |
| SCTE-27                                                                         | None                                                                              |
| Teletext                                                                        | Burn-in<br>DVB-Sub<br>Teletext                                                    |
| SMPTE 2110                                                                      | Embedded                                                                          | Burn-inEmbeddedEmbedded+SCTE-20SCTE-20SCTE-20+Embedded                            |
| Teletext                                                                        | Burn-in<br>DVB-Sub<br>Teletext                                                    |
