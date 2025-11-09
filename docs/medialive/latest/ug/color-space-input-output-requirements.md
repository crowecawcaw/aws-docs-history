# Input and output

requirements

###### Topics

- [Supported inputs](#color-space-supported-inputs "#color-space-supported-inputs")
- [Supported output types](#color-space-supported-outputs "#color-space-supported-outputs")
- [Supported output codecs](#color-space-supported-output-codecs "#color-space-supported-output-codecs")

## Supported inputs

MediaLive can work with the supported color space in all [supported types of input](inputs-supported-formats.md "inputs-supported-formats.md") with the following
notes:

- Handling Elemental Link inputs: MediaLive can't read the color space metadata in a
  source from an AWS Elemental Link device. The workaround when you set up the input is to specify
  the color space that applies, as described in [Scenario B – Metadata can be corrected with
  force](color-space-scenario-correct.md "color-space-scenario-correct.md").
- Converting to Dolby Vision 8.1:

      + The video source must be HD or 4K resolution. In other words, the source must
       be 1080p or better.
      + The video source must be HDR10. If MediaLive encounters a portion of non-HDR10
       content, it passes through the color space and color space metadata for that
       portion,
      + The video source can't be a file. This means that the source can't be a VOD
       asset in an MP4 file or a VOD asset in a transport stream.

  These constraints are stipulated by Dolby Vision 8.1, and relate to the minimal
  video quality required to produce Dolby Vision 8.1 outputs that meet the Dolby Vision
  8.1 standard.

## Supported output types

All color space types except Dolby Vision 8.1 can be set up in all MediaLive output group
types.

Dolby Vision 8.1 can be set up only in the following output group types:

- Archive
- CMAF Ingest
- HLS
- UDP

## Supported output codecs

The following table specifies the supported codecs for the MediaLive output color spaces.

| Output color space | AV1 | AVC (H.264) | HEVC (H.265) |
| ------------------ | --- | ----------- | ------------ |
| Rec. 601           |     | Yes         | Yes          |
| Rec. 709           |     | Yes         | Yes          |
| HDR10              |     |             | Yes          |
| HLG                |     |             | Yes          |
| Dolby Vision 8.1   |     |             | Yes          |

**Supported video profile for HDR10 or Dolby Vision 8.1
outputs**

For HDR10 or Dolby Vision 8.1 outputs, the video profile must include the term
_10BIT_.
