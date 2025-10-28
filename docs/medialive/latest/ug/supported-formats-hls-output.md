# Captions formats supported in HLS or

MediaPackage outputs

In this table, look up your input container and captions type. Then read across to
find the caption formats that are supported in MediaLive when you have this input container
and captions type, and produce these outputs:

- HLS output
- MediaPackage output with an HLS container

| Source caption container                                                     | Source caption input  | Supported output captions |
| ---------------------------------------------------------------------------- | --------------------- | ------------------------- | ---------------------------- | --------------------- |
| CDI container                                                                | ARIB                  | None                      |
| Embedded                                                                     | Burn-inEmbeddedWebVTT |                           | Teletext                     | Teletext              |
| HLS container                                                                | Embedded              | Burn-inEmbeddedWebVTT     |
| SCTE-20                                                                      | Burn-inEmbeddedWebVTT |
| Link container                                                               | Embedded              | Burn-inEmbeddedWebVTT     |
| Teletext                                                                     | Burn-inWebVTT         |
| MP4 container                                                                | Ancillary             | Burn-inEmbeddedWebVTT     |
| Embedded or Embedded+SCTE-20                                                 | Burn-inEmbeddedWebVTT |
| RTMP container                                                               | Embedded              | Burn-inEmbeddedWebVTT     |
| MPEG-TS container (through MediaConnect or through the RTP or SRT protocols) | ARIB                  | None                      |
| DVB-Sub                                                                      | Burn-inWebVTT         |                           | Embedded or Embedded+SCTE-20 | Burn-inEmbeddedWebVTT |
| SCTE-20                                                                      | Burn-inEmbeddedWebVTT |                           | SCTE-27                      | Burn-inWebVTT         |
| Teletext                                                                     | Burn-inWebVTT         |
| SMPTE 2110                                                                   | Embedded              | Burn-inWebVTT             |
| Teletext                                                                     | Burn-inWebVTT         |
