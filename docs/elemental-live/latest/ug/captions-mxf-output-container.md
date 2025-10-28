# Supported source captions

and output captions in an MXF output container

To read this table, find the type of container and captions from your
input. The supported caption formats for this _output_ container are then shown in the last column.

| Source input container | Source caption format | Supported output captions |
| ---------------------- | --------------------- | ------------------------- | -------- | ----------------- |
| HLS Container          | Embedded              | Burn-in, Embedded         |
| SCTE-20                | Burn-in               | Embedded                  |
| MP4 Container          | Embedded              | Burn-in, Embedded         |
| SCTE-20                | Burn-in, Embedded     |
| MXF Container          | Embedded              | Burn-in, Embedded         |
| Ancillary Data         | Burn-in, Embedded     |                           | Teletext | Burn-in           |
| QuickTime Container    | Embedded              | Burn-in, Embedded         |
| Ancillary Data         | Burn-in               | Embedded                  |
| Raw Container          | SRT                   | Burn-in                   |
| SMI                    | Burn-in               |                           | TTML     | Burn-in           |
| STL                    | Burn-in               |                           | SCC      | Burn-in, Embedded |
| RTMP Container         | Embedded              | Burn-in, Embedded         |
| SDI Container          | Embedded              | Burn-in, Embedded         |
| Teletext               | Burn-in               |                           | ARIB     | None              |
| MPEG2-TS Container     | Embedded              | Burn-in, Embedded         |
| SCTE-20                | Burn-in, Embedded     |                           | Teletext | Burn-in           |
| ARIB                   | None                  |                           | DVB-Sub  | Burn-in           |
| SCTE-27                | Burn-in               |
