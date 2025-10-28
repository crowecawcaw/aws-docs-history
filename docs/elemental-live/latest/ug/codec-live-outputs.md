# Live outputs: Supported

codecs

This table specifies the audio codecs that are supported in output
groups that support live outputs.

Use this table if you identified a use case in [Output types for delivery to an AWS
service](cc-outputs-aws.md "cc-outputs-aws.md") or [Output types for delivery to
non-AWS destinations](cc-output-not-aws.md "cc-output-not-aws.md")
and your output is live output.

In the table, find the output group and container (if applicable)
for the user case that you identified. Then read across to identify the
video and audio codecs that are supported for that output group.

| Output group type | Container | Video Codecs                                    | Audio Codecs                                                                                                                                               |
| ----------------- | --------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DASH              |           | H.264 H.265                                     | AAC Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos (converted) Dolby Digital Plus with Atmos (as passthrough)                              |
| HLS               | Standard  | H.264 H.265                                     | AAC Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos (converted) Dolby Digital Plus with Atmos (as passthrough)                              |
| HLS               | fMP4      | H.264 H.265                                     | AAC Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos (converted) Dolby Digital Plus with Atmos (as passthrough)                              |
| Microsoft Smooth  |           | H.264                                           | AAC Dolby Digital Dolby Digital Plus with Atmos (as passthrough)                                                                                           |
| Reliable TS       |           | H.264 H.265 MPEG2                               | AAC Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos (converted) Dolby Plus with Atmos (as passthrough)                                      |
| RTMP              |           | H.264                                           | AAC                                                                                                                                                        |
| SMPTE 2110        |           | Uncompressed JPEG XS (Version 2.21.3 and later) | PCM Dolby Digital Dolby Digital Plus                                                                                                                       |
| UDP/TS            |           | H.264 H.265 MPEG2                               | AAC Dolby Digital Dolby Digital Plus Dolby Digital Plus with Atmos (converted) Dolby Digital Plus with Atmos (as passthrough) DTS Express MPEG-1, layer II |
