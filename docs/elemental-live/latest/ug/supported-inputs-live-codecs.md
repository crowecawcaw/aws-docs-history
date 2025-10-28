# Supported codecs

This table specifies the codecs that are supported for each input
media type that Elemental Live supports.

| Media Type                               | Video Codecs                                                       | Audio Codecs                                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| HLS                                      | H.264 H.265                                                        | AAC                                                                                                                            |
| MPTS                                     | H.264 H.265 MPEG-2                                                 | AAC Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos MPEG-1, layer II PCM                                        |
| RTMP                                     | H.264                                                              | AAC                                                                                                                            |
| RTSP                                     | H.264 H.265                                                        | AAC                                                                                                                            |
| Transport stream                         | H.264 H.265 J2K (only in a TS that is compliant with TR-01) MPEG-2 | AAC Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos MPEG-1, layer II PCM                                        |
| SDI                                      | Uncompressed                                                       | Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos Dolby E frames carried in PCM streams tagged with SMPTE-337 PCM |
| HDMI                                     | Uncompressed                                                       | Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos Dolby E frames carried in PCM streams tagged with SMPTE-337 PCM |
| SDI Quad-compliant SDI 2SI-compliant SDI | Uncompressed                                                       | Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos Dolby E frames carried in PCM streams tagged with SMPTE-337 PCM |
| Uncompressed SMPTE 2110                  | Uncompressed JPEG XS (starting with version 2.21.3)                | Dolby Digital Dolby Digital Plus PCM                                                                                           |
| Uncompressed SMPTE 2022-6                | Uncompressed                                                       | Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos PCM                                                             |
