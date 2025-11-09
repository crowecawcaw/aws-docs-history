# Supported codecs by output type

The following table lists the video and audio codecs that each type of MediaLive output
container (output group) supports.

| Container (output group)      | Video codecs                          | Audio codecs                                                                                                      |
| ----------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Archive                       | H.264 (AVC)H.265 (HEVC)               | AAC<br>Dolby Digital (AC3)<br>Dolby Digital Plus (EAC3)<br>Dolby Digital Plus with Atmos<br>MPEG-1 Layer II (MP2) |
| CMAF Ingest                   | AV1H.265 (AVC)H.265 (HEVC)            | AAC<br>Dolby Digital (AC3)<br>Dolby Digital Plus (EAC3)<br>Dolby Digital Plus with Atmos                          |
| Frame Capture                 | JPEG                                  | None. A Frame capture output doesn't include audio.                                                               |
| HLS with a standard container | H.264 (AVC)H.265 (HEVC)               | AAC<br>Dolby Digital (AC3)<br>Dolby Digital Plus (EAC3)<br>Dolby Digital Plus with Atmos                          |
| HLS with an fMP4 container    | H.264 (AVC)<br>H.265 (HEVC)           | AAC<br>Dolby Digital (AC3)<br>Dolby Digital Plus (EAC3)<br>Dolby Digital Plus with Atmos                          |
| MediaPackage                  | H.264 (AVC)<br>H.265 (HEVC)           | AAC<br>Dolby Digital (AC3)<br>Dolby Digital Plus (EAC3)<br>Dolby Digital Plus with Atmos                          |
| Microsoft Smooth              | H.264 (AVC)<br>H.265 (HEVC)           | AAC<br>Dolby Digital (AC3)<br>Dolby Digital Plus (EAC3)                                                           |
| Multiplex                     | H.264 (AVC)<br>H.265 (HEVC)<br>MPEG-2 | AAC<br>Dolby Digital (AC3)<br>Dolby Digital Plus (EAC3)<br>Dolby Digital Plus with Atmos                          |
| RTMP or RTMPS                 | H.264 (AVC)                           | AAC                                                                                                               |
| SRT caller                    | H.264 (AVC)<br>H.265 (HEVC)           | AAC<br>Dolby Digital (AC3)<br>Dolby Digital Plus (EAC3)<br>Dolby Digital Plus with Atmos<br>MPEG-1 Layer II (MP2) |
| UDP                           | H.264 (AVC)<br>H.265 (HEVC)           | AAC<br>Dolby Digital (AC3)<br>Dolby Digital Plus (EAC3)<br>Dolby Digital Plus with Atmos<br>MPEG-1 Layer II (MP2) |
