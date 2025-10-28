# Captions formats supported in

UDP,
SRT, or multiplex outputs

In this table, look up your input container and captions type. Then read across to
find the caption formats that are supported in MediaLive in an MPEG-TS streaming
output
or in an MPTS multiplex output, when you have this input container and captions type.

| Source caption container                                                     | Source caption input                                               | Supported output captions                                     |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| CDI container                                                                | ARIB                                                               | ARIB                                                          |
| Embedded                                                                     | Burn-inDVB-SubEmbeddedEmbedded+SCTE-20SCTE-20                      |                                                               | Teletext                     | Burn-in DVB-Sub Teletext                                           |
| HLS container                                                                | Embedded                                                           | Burn-inDVB-SubEmbeddedEmbedded+SCTE-20SCTE-20SCTE-20+Embedded |
| SCTE-20                                                                      | Burn-in DVB-Sub Embedded Embedded+SCTE-20 SCTE-20 SCTE-20+Embedded |                                                               | Link container               | Embedded                                                           | Burn-in DVB-Sub Embedded Embedded+SCTE-20 SCTE-20 SCTE-20+Embedded |
| Teletext                                                                     | Burn-inDVB-Sub                                                     |                                                               | MP4 container                | Ancillary                                                          | Burn-in DVB-Sub Embedded Embedded+SCTE-20 SCTE-20 SCTE-20+Embedded |
| Embedded or Embedded+SCTE-20                                                 | Burn-in DVB-Sub Embedded Embedded+SCTE-20 SCTE-20 SCTE-20+Embedded |                                                               | RTMP container               | Embedded                                                           | Burn-in DVB-Sub Embedded Embedded+SCTE-20 SCTE-20 SCTE-20+Embedded |
| MPEG-TS container (through MediaConnect or through the RTP or SRT protocols) | ARIB                                                               | ARIB                                                          |
| DVB-Sub                                                                      | Burn-in DVB-Sub                                                    |                                                               | Embedded or Embedded+SCTE-20 | Burn-in DVB-Sub Embedded Embedded+SCTE-20 SCTE-20 SCTE-20+Embedded |
| SCTE-20                                                                      | Burn-in DVB-Sub Embedded Embedded+SCTE-20 SCTE-20 SCTE-20+Embedded |                                                               | SCTE-27                      | None                                                               |
| Teletext                                                                     | Burn-in DVB-Sub Teletext                                           |
| SMPTE 2110                                                                   | Embedded                                                           | Burn-inEmbeddedEmbedded+SCTE-20SCTE-20SCTE-20+Embedded        |
| Teletext                                                                     | Burn-in DVB-Sub Teletext                                           |
