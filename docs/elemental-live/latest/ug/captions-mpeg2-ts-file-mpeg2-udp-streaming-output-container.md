# Supported source captions and output captions in MPEG2-TS or

MPEG2-UDP

The table provides information about captions in an MPEG2-TS file
output container or MPEG2-UDP streaming output container.

To read this table, find the type of container and captions from your
input. The supported caption formats for this _output_ container are then shown in the last column.

| Source input container | Source caption format                                          | Supported output captions                                      |
| ---------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | ------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| HLS Container          | Embedded                                                       | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |
| SCTE-20                | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |                                                                | MP4 Container | Embedded                                                       | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |
| SCTE-20                | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |                                                                | MXF Container | Embedded                                                       | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |
| Ancillary Data         | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |                                                                | Teletext      | Burn-in, DVB-Sub, Teletext                                     |
| QuickTime Container    | Embedded                                                       | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |
| Ancillary Data         | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |
| Raw Container          | SRT                                                            | Burn-in, DVB-Sub                                               |
| SMI                    | Burn-in, DVB-Sub                                               |                                                                | TTML          | Burn-in, DVB-Sub                                               |
| STL                    | Burn-in, DVB-Sub                                               |                                                                | SCC           | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |
| RTMP Container         | Embedded                                                       | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |
| SDI Container          | Embedded                                                       | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |
| Teletext               | Burn-in, DVB-Sub, Teletext                                     |                                                                | ARIB          | ARIB                                                           |
| MPEG2-TS Container     | Embedded                                                       | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |
| SCTE-20                | Burn-in, DVB-Sub, Embedded, Embedded+SCTE-20, SCTE-20+Embedded |                                                                | Teletext      | Burn-in, DVB-Sub, Teletext                                     |
| ARIB                   | ARIB                                                           |                                                                | DVB-Sub       | Burn-in, DVB-Sub                                               |
| SCTE-27                | Burn-in, DVB-Sub                                               |
