# Output

requirements

**Supported output types**

All color space types except Dolby Vision 8.1 can be set up in all MediaLive output group
types.

Dolby Vision 8.1 can be set up only in the following output group types:

- Archive
- CMAF Ingest
- HLS
- SRT caller
- UDP
  **Supported output codecs**

The following table specifies the supported video codecs for the output color spaces. A
value of Yes means that when the video output uses this codec, you can convert to the
specified color space.

| Output color space | AV1 | AVC (H.264) | HEVC (H.265) |
| ------------------ | --- | ----------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rec. 601           | Yes | Yes         | Yes          |
| Rec. 709           | Yes | Yes         | Yes          |
| HDR10              | Yes |             | Yes          |
| HLG                |     |             | Yes          |
| Dolby Vision 8.1   |     |             | Yes          | **Supported video profile for HDR10 or Dolby Vision 8.1 outputs** For HDR10 or Dolby Vision 8.1 outputs, the video profile must include the term _10BIT_. |
