# VOD supported codecs and input types

The following sections describe supported input types, input codecs, and output codecs for file-based video
on demand (VOD) content.

## Supported input types

These are the input types that MediaPackage supports for VOD content.

| MediaPackage input type | Use case                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HLS                     | Pull an HLS stream set from an Amazon S3 bucket, with or without a<br>secure connection.Additional requirements:<br>• Media segments must not be encrypted.<br>• Streams can contain either muxed video and audio<br>tracks, or unmuxed tracks.<br>• The input must contain at least one video track.<br>MediaPackage doesn't support inputs that contain no<br>video track.                                                                                                                                                 |
| SMIL                    | Pull an MP4 stream set referenced by a .smil manifest from an<br>Amazon S3 bucket, with or without a secure connection. For<br>information about the .smil manifest, see [Requirements for .smil manifests](supported-inputs-vod-smil.md "supported-inputs-vod-smil.md").Additional<br>requirements:<br>• MP4 container must not be fragmented.<br>• Media segments must not be encrypted.<br>• Streams can contain either muxed video and audio<br>tracks, or only video tracks.<br>• Streams must have an equal time base. |

## Supported input codecs

These are the video, audio, and subtitles codecs that MediaPackage supports for
file-based source content.

| Input type | Media container                              | Video codecs                                        | Audio codecs                                     | Subtitles/captions format                         |
| ---------- | -------------------------------------------- | --------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------- |
| HLS        | • Video: TS<br>• Audio: TS, AAC, AC3, or EC3 | • H.264 (AVC)<br>• H.265 (HEVC) with HDR-10 support | • AAC<br>• Dolby Digital<br>• Dolby Digital Plus | • WebVTT<br>• CEA-608 and CEA-708 closed captions |
| SMIL       | MP4 (non-fragmented)                         | • H.264 (AVC)<br>• H.265 (HEVC) with HDR-10 support | • AAC<br>• Dolby Digital<br>• Dolby Digital Plus | SRT                                               |

## Supported output codecs

These are the video, audio, and subtitles codecs that MediaPackage supports for
delivering VOD content.

| Endpoint type    | Manifest format | Media container                              | Video codecs                                        | Audio codecs                                     | Subtitles/captions format                         |
| ---------------- | --------------- | -------------------------------------------- | --------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------- |
| Apple HLS        | HLS             | • Video: TS<br>• Audio: TS, AAC, AC3, or EC3 | • H.264 (AVC)<br>• H.265 (HEVC) with HDR-10 support | • AAC<br>• Dolby Digital<br>• Dolby Digital Plus | • WebVTT<br>• CEA-608 and CEA-708 closed captions |
| DASH-ISO         | MPEG-DASH       | MP4                                          | • H.264 (AVC)<br>• H.265 (HEVC) with HDR-10 support | • AAC<br>• Dolby Digital<br>• Dolby Digital Plus | • EBU-TT<br>• CEA-608 and CEA-708 closed captions |
| Microsoft Smooth | MSS             | MP4                                          | • H.264 (AVC)<br>• H.265 (HEVC) with HDR-10 support | • AAC<br>• Dolby Digital<br>• Dolby Digital Plus | DFXP                                              |
| CMAF             | HLS             | CMAF                                         | • H.264 (AVC)<br>• H.265 (HEVC) with HDR-10 support | • AAC<br>• Dolby Digital<br>• Dolby Digital Plus | • WebVTT<br>• CEA-608 and CEA-708 closed captions |
