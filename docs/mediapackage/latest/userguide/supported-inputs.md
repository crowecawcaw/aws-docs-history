# Supported inputs and outputs

This section describes the input types, input codecs, and output codecs that
AWS Elemental MediaPackage supports for live content.

###### Topics

- [Supported input types](#supported-types-live "#supported-types-live")
- [Supported input codecs](#suported-inputs-codecs-live "#suported-inputs-codecs-live")
- [Supported output codecs](#suported-outputs-codecs-live "#suported-outputs-codecs-live")
  The following sections describe supported input types and codecs for live streaming
  content.

## Supported input types

Use the following input types to push streams from an external source or encoder
(such as AWS Elemental MediaLive) using the HTTPS protocol:

- HLS
- CMAF

For information about CMAF ingest, see [CMAF ingest](cmaf-ingest.md "cmaf-ingest.md").

The following are additional input requirements:

- You must define a channel policy to enable content to flow into your channel
  from sources outside of your account.
- Media segments must not be encrypted.
- Streams can contain either muxed video and audio tracks, or unmuxed tracks.
- The input must contain at least one video track. MediaPackage doesn't support inputs
  that contain no video track.

## Supported input codecs

These are the video, audio, and subtitles codecs that MediaPackage supports for
source content streams.

| Input type    | Media container                                   | Video codecs                                                                                   | Audio codecs                                                                                   | Subtitles/captions format                              |
| ------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HLS           | <br>• Video: TS <br>• Audio: TS, AAC, AC3, or EC3 | <br>• H.264 (AVC) <br>• H.265 (HEVC) with HDR-10 or Dolby Vision Profile 8.1 support           | <br>• AAC <br>• Dolby Digital <br>• Dolby Digital Plus                                         | <br>• WebVTT <br>• CEA-608 and CEA-708 closed captions |
| CMAF          | CMAF                                              | <br>• H.264 (AVC) <br>• H.265 (HEVC) with HDR-10 or Dolby Vision Profile 8.1 support <br>• AV1 | <br>• AAC <br>• Dolby Digital <br>• Dolby Digital Plus                                         | <br>• TTML <br>• CEA-608 and CEA-708 closed captions   | ## Supported output codecs These are the video, audio, and subtitles codecs that MediaPackage supports when delivering live content. ###### Note The AV1 video codec is supported only with CMAF endpoint types. If you configure a TS endpoint on a channel with AV1 streams those streams won't show up on the endpoint. |
| Endpoint type | Manifest format                                   | Media container                                                                                | Video codecs                                                                                   | Audio codecs                                           | Subtitles/captions format                                                                                                                                                                                                                                                                                                  |
| ---           | ---                                               | ---                                                                                            | ---                                                                                            | ---                                                    | ---                                                                                                                                                                                                                                                                                                                        |
| TS            | HLS                                               | <br>• Video: TS <br>• Audio: TS or AAC                                                         | <br>• H.264 (AVC) <br>• H.265 (HEVC) with HDR-10 or Dolby Vision Profile 8.1 support           | <br>• AAC <br>• Dolby Digital <br>• Dolby Digital Plus | <br>• WebVTT                                                                                                                                                                                                                                                                                                               |
| CMAF          | HLS                                               | CMAF                                                                                           | <br>• H.264 (AVC) <br>• H.265 (HEVC) with HDR-10 or Dolby Vision Profile 8.1 support <br>• AV1 | <br>• AAC <br>• Dolby Digital <br>• Dolby Digital Plus | <br>• WebVTT <br>• CEA-608 and CEA-708 closed captions                                                                                                                                                                                                                                                                     |
| CMAF          | DASH                                              | CMAF                                                                                           | <br>• H.264 (AVC) <br>• H.265 (HEVC) with HDR-10 or Dolby Vision Profile 8.1 support <br>• AV1 | <br>• AAC <br>• Dolby Digital <br>• Dolby Digital Plus | <br>• TTML <br>• CEA-608 and CEA-708 closed captions                                                                                                                                                                                                                                                                       |
