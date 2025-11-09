# VOD outputs: Supported

codecs

This table specifies the codecs that are supported in output groups
that support VOD outputs.

Use this table if you identified a use case in [Output types for delivery to an AWS
service](cc-outputs-aws.md "cc-outputs-aws.md") or [Output types for delivery to
non-AWS destinations](cc-output-not-aws.md "cc-output-not-aws.md")
where your output is VOD output.

In the table, find the output group and container (if applicable)
for the user case that you identified. Then read across to identify the
video and audio codecs that are supported for that output group.

| Output group type | Container (if applicable) | Video Codecs                                                                                                                                                                | Audio Codecs                                                                                                                                                                                                                                      |
| ----------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Archive           | Raw (No container)        | Frame Capture (MJPEG)<br>H.264<br>H.265<br>MJPEG<br>MPEG2                                                                                                                   | AAC<br>AIFF<br>Dolby Digital<br>Dolby Digital Plus<br>Dolby Digital Plus with Atmos (converted)<br>Dolby Digital Plus with Atmos (as passthrough)<br>Archive output in TS and Raw container (no<br>container)<br>DTS Express<br>MPEG Audio<br>WAV |
| Archive           | Raw (No container)        | Uncompressed<br>For information about the 4CC codes that are<br>supported,<br>and the pixel formats for each 4CC code, see the<br>table below                               | AAC<br>AIFF<br>Dolby Digital<br>Dolby Digital Plus<br>Dolby Digital Plus with Atmos (converted)<br>Dolby Digital Plus ATMOS (as passthrough)<br>DTS Express<br>MPEG Audio<br>WAV                                                                  |
| Archive           | 3GPP                      | H.264                                                                                                                                                                       | AAC                                                                                                                                                                                                                                               |
| Archive           | MXF                       | MPEG-2                                                                                                                                                                      | WAV                                                                                                                                                                                                                                               |
| Archive           | MPEG-2 Transport Stream   | H.264<br>H.265<br>MPEG2                                                                                                                                                     | AAC<br>Dolby Digital<br>Dolby Digital Plus<br>Dolby Digital Plus with Atmos (converted)<br>Dolby Digital Plus ATMOS (as passthrough)<br>MPEG Audio                                                                                                |
| Archive           | MPEG-4 (.mp4)             | H.264<br>H.265                                                                                                                                                              | AAC<br>Dolby Digital<br>Dolby Digital Plus<br>Dolby Digital Plus with Atmos (converted)<br>Dolby Digital Plus ATMOS (as passthrough)<br>DTS Express                                                                                               |
| Archive           | MPEG-4 Flash (.f4v)       | H.264                                                                                                                                                                       | AAC                                                                                                                                                                                                                                               |
| Archive           | QuickTime                 | H.264<br>MPEG2<br>Apple ProRes<br>Uncompressed (For information about the 4CC codes<br>that are supported, and the pixel formats for each 4CC<br>code, see the table below) | AAC<br>AIFF<br>Dolby Digital<br>Dolby Digital Plus<br>Dolby Digital Plus with Atmos (converted)<br>Dolby Digital Plus ATMOS (as passthrough)<br>WAV                                                                                               |
| HLS               | Standard                  | H.264<br>H.265                                                                                                                                                              | AAC<br>Dolby Digital<br>Dolby Digital Plus<br>Dolby Digital Plus with Atmos (converted)<br>Dolby Digital Plus ATMOS (as passthrough)                                                                                                              |
| HLS               | fMP4                      | H.264<br>H.265                                                                                                                                                              | AAC<br>Dolby Digital<br>Dolby Digital Plus<br>Dolby Digital Plus with Atmos (converted)<br>Dolby Digital Plus ATMOS (as passthrough)                                                                                                              |
| Microsoft Smooth  |                           | H.264                                                                                                                                                                       | AAC<br>Dolby Digital<br>Dolby Digital Plus<br>Dolby Digital Plus ATMOS (as passthrough)                                                                                                                                                           |
| DASH              |                           | H.264<br>H.265                                                                                                                                                              | AAC<br>Dolby Digital<br>Dolby Digital Plus<br>Dolby Digital Plus with Atmos (converted)<br>Dolby Digital Plus ATMOS (as passthrough)                                                                                                              |

Use this table if you want to deliver uncompressed video in an
Archive output group. The table specifies the 4CC codes that are
supported for uncompressed video, and the pixel formats for each 4CC
code.

| 4CC Code for the video format | Pixel formats                  |
| ----------------------------- | ------------------------------ |
| YV12                          | 8-bit 4:2:0 planar             |
| I420                          | 8-bit 4:2:0 planar             |
| NV12                          | 8-bit 4:2:0 chroma interleaved |
| YV16                          | 8-bit 4:2:2 planar             |
| UYVY                          | 8-bit 4:2:2 planar             |
| YUYV                          | 8-bit 4:2:2 planar             |
| S210                          | 10-bit 4:2:2 packed            |
