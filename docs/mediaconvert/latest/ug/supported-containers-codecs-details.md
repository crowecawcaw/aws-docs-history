# Supported containers and codecs

reference tables

The following sections provide reference tables for containers and codecs that
MediaConvert supports.

To use these tables, first find the container or codec using the links following this
introduction. For containers, the tables provide details for which video or audio codecs are
supported, and whether they're supported for inputs or outputs. For codecs, the tables
provide details for which containers are supported, for inputs and outputs as well. Note
that inputs or outputs labeled like _Audio-only input_ or
_Audio-only output_ refer to support for audio-only
workflows. For more information, see [Creating audio-only outputs](audio-only.md "audio-only.md").

For quick reference tables that show which input formats MediaConvert supports, see [Supported input formats](reference-codecs-containers-input.md "reference-codecs-containers-input.md").

For quick reference tables that show which output formats MediaConvert supports, see
[Supported output formats](reference-codecs-containers.md "reference-codecs-containers.md").

**Containers**

[3G2](#container-3g2-3gp "#container-3g2-3gp") | [3GP](#container-3g2-3gp "#container-3g2-3gp") | [ASF](#container-asf-wmv-wma "#container-asf-wmv-wma") | [AVI](#container-avi "#container-avi") | [CMAF](#container-cmaf "#container-cmaf") | [DASH](#container-dash "#container-dash") | [F4V](#container-flash "#container-flash") | [FLV](#container-flash "#container-flash") | [GIF](#container-gif "#container-gif") | [HLS](#container-hls "#container-hls") | [IMF](#container-imf "#container-imf") | [Matroska](#container-matroska "#container-matroska") | [MOV](#container-mov "#container-mov") | [MP3](#container-mp3 "#container-mp3") | [MP4](#container-mp4 "#container-mp4") | [MPEG-1](#container-mpeg-1 "#container-mpeg-1") | [MPEG-PS](#container-mpeg-ps "#container-mpeg-ps") | [MPEG-TS](#container-mpeg-ts "#container-mpeg-ts") | [MSS](#container-mss "#container-mss") | [MXF](#container-mxf "#container-mxf") | [OGG](#container-ogg "#container-ogg") | [WAV](#container-wav "#container-wav") | [WebM](#container-webm "#container-webm") | [WMA](#container-asf-wmv-wma "#container-asf-wmv-wma") | [WMV](#container-asf-wmv-wma "#container-asf-wmv-wma") | [Y4M](#container-y4m "#container-y4m") | [No container](#container-none "#container-none")

**Codecs**

[AAC](#codec-aac "#codec-aac") | [AIFF](#codec-aiff "#codec-aiff") |
[AMR-NB](#codec-amr "#codec-amr") | [AMR-WB](#codec-amr "#codec-amr") | [Apple ProRes](#codec-apple-prores "#codec-apple-prores") |
[AV1](#codec-av1 "#codec-av1") | [AVC
(H.264)](#codec-avc "#codec-avc") | [AVC-Intra](#codec-avc-intra "#codec-avc-intra") | [Canopus HQ](#codec-canopus-hq "#codec-canopus-hq") | [Dolby Atmos](#codec-atmos "#codec-atmos") | [Dolby Digital (AC3)](#codec-ac3 "#codec-ac3") |
[Dolby Digital Plus (EAC3)](#codec-eac3 "#codec-eac3") | [Dolby E](#codec-dolby-e "#codec-dolby-e") | [DV/DVCPRO](#codec-dv-dvcpro "#codec-dv-dvcpro") | [DV25](#codec-dv25-dv50 "#codec-dv25-dv50") | [DV50](#codec-dv25-dv50 "#codec-dv25-dv50") | [DVCPro HD](#codec-dvcpro-hd "#codec-dvcpro-hd") | [DivX/Xvid](#codec-divx "#codec-divx") | [FLAC](#codec-flac "#codec-flac") | [GIF](#codec-gif "#codec-gif") | [GSM](#codec-gsm "#codec-gsm") | [H.261](#codec-h261 "#codec-h261") | [H.262](#codec-h262 "#codec-h262") | [H.263](#codec-h263 "#codec-h263") | [HEVC (H.265)](#codec-hevc "#codec-hevc") | [J2K](#codec-j2k "#codec-j2k") | [MJPEG](#codec-mjpeg "#codec-mjpeg") | [MP3](#codec-mp3 "#codec-mp3") | [MPEG-1](#codec-mpeg1 "#codec-mpeg1") |
[MPEG-2](#codec-mpeg2 "#codec-mpeg2") | [MPEG-4 Part 2](#codec-mpeg-4-part-2 "#codec-mpeg-4-part-2") | [MPEG Audio](#codec-mpeg-audio "#codec-mpeg-audio") | [Opus](#codec-opus-vorbis "#codec-opus-vorbis") | [Panasonic
P2](#codec-p2 "#codec-p2") | [PCM](#codec-pcm "#codec-pcm") | [QuickTime RLE](#codec-quicktime-rle "#codec-quicktime-rle") | [Sony XDCAM](#codec-xdcam "#codec-xdcam") | [Sony XDCAM MPEG-4 Proxy](#codec-xdcam-mp4 "#codec-xdcam-mp4") | [VC-1](#codec-vc1 "#codec-vc1") |
[VC-3](#codec-vc3 "#codec-vc3") | [Vorbis](#codec-opus-vorbis "#codec-opus-vorbis") | [VP8](#codec-vp8 "#codec-vp8") | [VP9](#codec-vp9 "#codec-vp9") | [WMA](#codec-wma "#codec-wma") |
[WMA2](#codec-wma "#codec-wma") | [WMA
Pro](#codec-wma-pro "#codec-wma-pro") | [XAVC](#codec-xavc "#codec-xavc")

###### Topics

- [Supported containers](#containers "#containers")
- [Supported codecs](#codecs "#codecs")

## Supported containers

This section contains reference tables for input and output containers that
MediaConvert supports. The tables show the container, support on the input or output
side, and video or audio codec support in the container. For more information about the
codec, or to see codec support in other containers, choose the codec link.

**3G2, 3GP**

| Container  | Input / Output     | Supported video codec                                                                                                                           | Supported audio codec                                                                                    |
| ---------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| 3G2<br>3GP | Input              | [AVC (H.264)](#codec-avc "#codec-avc")<br>[H.263](#codec-h263 "#codec-h263")<br>[MPEG-4 part<br>2](#codec-mpeg-4-part-2 "#codec-mpeg-4-part-2") | [AAC](#codec-aac "#codec-aac")<br>[AMR-NB](#codec-amr "#codec-amr")<br>[AMR-WB](#codec-amr "#codec-amr") |
| Output     | _Not<br>supported_ | _Not<br>supported_                                                                                                                              |

**ASF, WMV, WMA (Advanced Systems
Format)**

| Container         | Input / Output      | Supported video codec           | Supported audio codec                                                                                           |
| ----------------- | ------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| ASFWMV            | Input               | [VC-1](#codec-vc1 "#codec-vc1") | [WMA](#codec-wma "#codec-wma")<br>[WMA2](#codec-wma "#codec-wma")<br>[WMA Pro](#codec-wma-pro "#codec-wma-pro") |
| Output            | _Not<br>supported_  | _Not<br>supported_              |
| WMA               | Audio-only input    | _Not<br>applicable_             | [WMA](#codec-wma "#codec-wma")<br>[WMA2](#codec-wma "#codec-wma")<br>[WMA Pro](#codec-wma-pro "#codec-wma-pro") |
| Audio-only output | _Not<br>applicable_ | _Not<br>supported_              |

**AVI (Audio Video Interleave)**

| Container | Input / Output     | Supported video codec                                                                                                                                                                                        | Supported audio codec                                                                                                                                                                                                                                                                              |
| --------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AVI       | Input              | [Canopus<br>HQ](#codec-canopus-hq "#codec-canopus-hq")<br>[DivX/Xvid](#codec-divx "#codec-divx")<br>[DV/DVCPRO](#codec-dv-dvcpro "#codec-dv-dvcpro")<br>[MJPEG](#codec-mjpeg "#codec-mjpeg")<br>Uncompressed | [Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[Dolby E](#codec-dolby-e "#codec-dolby-e")<br>[MP3](#container-mp3 "#container-mp3")<br>[MPEG<br>Audio](#codec-mpeg-audio "#codec-mpeg-audio")<br>[PCM](#codec-pcm "#codec-pcm") |
| Output    | _Not<br>supported_ | _Not<br>supported_                                                                                                                                                                                           |

**CMAF (Common Media
Application Format)**

| Container | Input / Output                                                                                                                                          | Supported video codec                                                                                                                            | Supported audio codec |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| CMAF DASH | Input                                                                                                                                                   | _Not<br>supported_                                                                                                                               | _Not<br>supported_    |
| Output    | [AV1](#codec-av1 "#codec-av1")<br>[AVC (H.264)](#codec-avc "#codec-avc")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc")<br>[VP9](#codec-vp9 "#codec-vp9") | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3") |
| CMAF HLS  | Input                                                                                                                                                   | _Not<br>supported_                                                                                                                               | _Not<br>supported_    |
| Output    | [AV1](#codec-av1 "#codec-av1")<br>[AVC (H.264)](#codec-avc "#codec-avc")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc")<br>[VP9](#codec-vp9 "#codec-vp9") | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3") |

###### Note

For HLS output codec recommendations from Apple, see: [https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices "https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices").

**DASH (Dynamic Adaptive Streaming over
HTTP)**

| Container         | Input / Output                                                                                                                                                                            | Supported video codec                                                                                                                                                                                                | Supported audio codec |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| DASH              | Input                                                                                                                                                                                     | _Not<br>supported_                                                                                                                                                                                                   | _Not<br>supported_    |
| Output            | [AV1](#codec-av1 "#codec-av1")<br>[AVC (H.264)](#codec-avc "#codec-avc")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc")<br>[VP8](#codec-vp8 "#codec-vp8")<br>[VP9](#codec-vp9 "#codec-vp9") | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")                                                                     |
| Audio-only input  | _Not<br>supported_                                                                                                                                                                        | _Not<br>supported_                                                                                                                                                                                                   |
| Audio-only output | _Not applicable_                                                                                                                                                                          | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[Dolby Digital Plus JOC<br>(Atmos)](#codec-atmos "#codec-atmos") |

For information about CMAF DASH, see [CMAF
containers](#container-cmaf "#container-cmaf").

**FLV, F4V (MPEG-4 Flash)**

| Container  | Input / Output | Supported video codec                                                           | Supported audio codec          |
| ---------- | -------------- | ------------------------------------------------------------------------------- | ------------------------------ |
| FLV<br>F4V | Input          | [AVC (H.264)](#codec-avc "#codec-avc")<br>[H.263](#codec-h263 "#codec-h263")    | [AAC](#codec-aac "#codec-aac") |
| F4V        | Output         | [AVC (H.264)](#codec-avc "#codec-avc")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2") | [AAC](#codec-aac "#codec-aac") |

**GIF**

| Container | Input / Output                 | Supported video codec          |
| --------- | ------------------------------ | ------------------------------ |
| GIF       | Input                          | [GIF](#codec-gif "#codec-gif") |
| Output    | [GIF](#codec-gif "#codec-gif") |

**HLS (Apple HTTP Live Streaming)**

| Container         | Input / Output                                                                      | Supported video codec                                                                                                                            | Supported audio codec                                                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| HLS               | Input                                                                               | [AVC (H.264)](#codec-avc "#codec-avc")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")                     | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3") |
| Output            | [AVC (H.264)](#codec-avc "#codec-avc")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc") | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3") |
| Audio-only input  | _Not<br>applicable_                                                                 | _Not<br>supported_                                                                                                                               |
| Audio-only output | _Not<br>applicable_                                                                 | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")                                                              |

For more information about HLS inputs and input requirements, see [HLS input requirements](using-hls-inputs.md "using-hls-inputs.md").

For information about CMAF HLS, see [CMAF
containers](#container-cmaf "#container-cmaf").

###### Note

When outputting HEVC in an HLS container, we recommend using a CMAF
output group for the widest player compatibility. For more details, see
[https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices "https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices").

**IMF (Interoperable Master Format)**

| Container | Input / Output     | Supported video codec                                                                                         | Supported audio codec          |
| --------- | ------------------ | ------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| IMF       | Input              | [Apple<br>ProRes](#codec-apple-prores "#codec-apple-prores")<br>[JPEG 2000<br>(J2K)](#codec-j2k "#codec-j2k") | [PCM](#codec-pcm "#codec-pcm") |
| Output    | _Not<br>supported_ | _Not<br>supported_                                                                                            |

Specify your input IMF by providing the path to your Composition Playlist
(CPL). If the CPL is in an incomplete IMP, also specify any supplemental
IMPs.

For information about using IMF inputs to create Dolby Vision outputs, see
[Dolby
Vision input format support and job setting requirements](dolby-vision-job-limitations-and-requirements.md "dolby-vision-job-limitations-and-requirements.md").

**Matroska**

| Container         | Input / Output     | Supported video codec                                                                                                                                                                 | Supported audio codec                                                                                                                                                                                                                                                                                                                           |
| ----------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Matroska          | Input              | [AVC (H.264)](#codec-avc "#codec-avc")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")<br>[MPEG-4 part<br>2](#codec-mpeg-4-part-2 "#codec-mpeg-4-part-2")<br>[VC-1](#codec-vc1 "#codec-vc1") | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[FLAC](#codec-flac "#codec-flac")<br>[Opus](#codec-opus-vorbis "#codec-opus-vorbis")<br>[PCM](#codec-pcm "#codec-pcm")<br>[WMA](#codec-wma "#codec-wma")<br>[WMA2](#codec-wma "#codec-wma") |
| Output            | _Not<br>supported_ | _Not<br>supported_                                                                                                                                                                    |
| Audio-only input  | _Not applicable_   | [FLAC](#codec-flac "#codec-flac")<br>[OPUS](#codec-opus-vorbis "#codec-opus-vorbis")                                                                                                  |
| Audio-only output | _Not applicable_   | _Not supported_                                                                                                                                                                       |

**MOV (Apple QuickTime)**

| Container                                                    | Input / Output                                                                  | Supported video codec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Supported audio codec                                                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| MOV                                                          | Input                                                                           | [Apple<br>ProRes](#codec-apple-prores "#codec-apple-prores")<br>[AVC (H.264)](#codec-avc "#codec-avc")<br>[AVC-Intra](#codec-avc-intra "#codec-avc-intra")<br>[DivX/Xvid](#codec-divx "#codec-divx")<br>[DV/DVCPRO](#codec-dv-dvcpro "#codec-dv-dvcpro")<br>[H.261](#codec-h261 "#codec-h261")<br>[H.262](#codec-h262 "#codec-h262")<br>[H.263](#codec-h263 "#codec-h263")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc")<br>[JPEG 2000<br>(J2K)](#codec-j2k "#codec-j2k")<br>[MJPEG](#codec-mjpeg "#codec-mjpeg")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")<br>[MPEG-4 part<br>2](#codec-mpeg-4-part-2 "#codec-mpeg-4-part-2")<br>[QuickTime<br>RLE](#codec-quicktime-rle "#codec-quicktime-rle")<br>Uncompressed | [AAC](#codec-aac "#codec-aac")<br>[MP3](#container-mp3 "#container-mp3")<br>[PCM](#codec-pcm "#codec-pcm") |
| Output                                                       | [AVC (H.264)](#codec-avc "#codec-avc")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2") | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[WAV](#codec-pcm "#codec-pcm")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Apple<br>ProRes](#codec-apple-prores "#codec-apple-prores") | [AIFF](#codec-aiff "#codec-aiff")                                               |
| Audio-only input                                             | _Not<br>applicable_                                                             | [PCM](#codec-pcm "#codec-pcm")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Audio-only output                                            | _Not<br>applicable_                                                             | _Not<br>supported_                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

MOV inputs must be self-contained. References to external files are not
supported.

For information about using MOV inputs to create Dolby Vision outputs, see
[Dolby
Vision input format support and job setting requirements](dolby-vision-job-limitations-and-requirements.md "dolby-vision-job-limitations-and-requirements.md").

**MP3 (MPEG-1 Layer 3)**

| Container                      | Input / Output                 | Supported audio codec          |
| ------------------------------ | ------------------------------ | ------------------------------ |
| [MP3](#codec-mp3 "#codec-mp3") | Audio-only input               | [MP3](#codec-mp3 "#codec-mp3") |
| Audio-only output              | [MP3](#codec-mp3 "#codec-mp3") |

MediaConvert does not read ID3 metadata or tags from MP3 inputs.

**MP4 (MPEG-4)**

| Container         | Input / Output                                                                                                        | Supported video codec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Supported audio codec                                                                                                                                                                                                                                                                        |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MP4               | Input                                                                                                                 | [AV1](#codec-av1 "#codec-av1")<br>[AVC (H.264)](#codec-avc "#codec-avc")<br>[AVC-Intra](#codec-avc-intra "#codec-avc-intra")<br>[DivX/Xvid](#codec-divx "#codec-divx")<br>[H.261](#codec-h261 "#codec-h261")<br>[H.262](#codec-h262 "#codec-h262")<br>[H.263](#codec-h263 "#codec-h263")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc")<br>[JPEG 2000<br>(J2K)](#codec-j2k "#codec-j2k")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")<br>[MPEG-4 part<br>2](#codec-mpeg-4-part-2 "#codec-mpeg-4-part-2")<br>[VC-1](#codec-vc1 "#codec-vc1")<br>[VP9](#codec-vp9 "#codec-vp9")<br>Uncompressed | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[FLAC](#codec-flac "#codec-flac")<br>[PCM](#codec-pcm "#codec-pcm")<br>[WMA](#codec-wma "#codec-wma")<br>[WMA2](#codec-wma "#codec-wma") |
| Output            | [AV1](#codec-av1 "#codec-av1")<br>[AVC (H.264)](#codec-avc "#codec-avc")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc") | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Audio-only input  | _Not<br>applicable_                                                                                                   | [AAC](#codec-aac "#codec-aac")<br>[FLAC](#codec-flac "#codec-flac")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Audio-only output | _Not<br>applicable_                                                                                                   | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")                                                                                                                                                                                                                                                                                                                                                                                                                                        |

MediaConvert doesn't support fragmented MP4 initialization segments. Your
MP4 input must be self-contained.

**MPEG-1 (MPEG-1 System Stream)**

| Container | Input / Output     | Supported video codec                                                      | Supported audio codec                                                                                                                                                                                                                                                          |
| --------- | ------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| MPEG-1    | Input              | [MPEG-1](#codec-mpeg1 "#codec-mpeg1")[MPEG-2](#codec-mpeg2 "#codec-mpeg2") | [AAC](#codec-aac "#codec-aac")<br>[AIFF](#codec-aiff "#codec-aiff")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[MPEG Audio](#codec-mpeg-audio "#codec-mpeg-audio")<br>[PCM](#codec-pcm "#codec-pcm") |
| Output    | _Not<br>supported_ | _Not<br>supported_                                                         |

**MPEG-PS (MPEG Program Stream)**

| Container | Input / Output     | Supported video codec                 | Supported audio codec                                  |
| --------- | ------------------ | ------------------------------------- | ------------------------------------------------------ |
| MPEG-PS   | Input              | [MPEG-2](#codec-mpeg2 "#codec-mpeg2") | [MPEG<br>audio](#codec-mpeg-audio "#codec-mpeg-audio") |
| Output    | _Not<br>supported_ | _Not<br>supported_                    |

**MPEG-TS (MPEG-2 Transport Stream)**

| Container         | Input / Output                                                                                                               | Supported video codec                                                                                                                                                                                                           | Supported audio codec                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MPEG-TS           | Input                                                                                                                        | [AVC (H.264)](#codec-avc "#codec-avc")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")<br>[VC-1](#codec-vc1 "#codec-vc1")                                                                 | [AAC](#codec-aac "#codec-aac")<br>[AIFF](#codec-aiff "#codec-aiff")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[Dolby E](#codec-dolby-e "#codec-dolby-e")<br>[MPEG<br>Audio](#codec-mpeg-audio "#codec-mpeg-audio")<br>[PCM](#codec-pcm "#codec-pcm")<br>[WMA](#codec-wma "#codec-wma")<br>[WMA2](#codec-wma "#codec-wma") |
| Output            | [AVC (H.264)](#codec-avc "#codec-avc")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2") | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")<br>[PCM/WAV](#codec-pcm "#codec-pcm") |
| Audio-only input  | _Not<br>applicable_                                                                                                          | [MPEG-2](#codec-mpeg2 "#codec-mpeg2")<br>[PCM](#codec-pcm "#codec-pcm")                                                                                                                                                         |
| Audio-only output | _Not<br>applicable_                                                                                                          | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")                                       |

**MSS (Microsoft Smooth Streaming)**

| Container | Input / Output                         | Supported video codec                                                                                                                            | Supported audio codec |
| --------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| MSS       | Input                                  | _Not<br>supported_                                                                                                                               | _Not<br>supported_    |
| Output    | [AVC (H.264)](#codec-avc "#codec-avc") | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3") |

**MXF (Material Exchange Format)**

| Container                             | Input / Output                                                                                                                                                         | Supported video codec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | MXF Profile                        | Supported audio codec                                                                                                                                                                                         |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MXF                                   | Input                                                                                                                                                                  | [Apple<br>ProRes](#codec-apple-prores "#codec-apple-prores")<br>[AVC (H.264)](#codec-avc "#codec-avc")<br>[AVC-Intra](#codec-avc-intra "#codec-avc-intra")<br>[DV/DVCPRO](#codec-dv-dvcpro "#codec-dv-dvcpro")<br>[DV25](#codec-dv25-dv50 "#codec-dv25-dv50")<br>[DV50](#codec-dv25-dv50 "#codec-dv25-dv50")<br>[DVCPro<br>HD](#codec-dvcpro-hd "#codec-dvcpro-hd")<br>[JPEG 2000<br>(J2K)](#codec-j2k "#codec-j2k")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")<br>[Panasonic P2](#codec-p2 "#codec-p2")<br>[Sony XDCam](#codec-xdcam "#codec-xdcam")<br>[Sony XDCam MPEG-4<br>Proxy](#codec-xdcam-mp4 "#codec-xdcam-mp4")<br>Uncompressed | _Not<br>applicable_                | [AAC](#codec-aac "#codec-aac")<br>[AIFF](#codec-aiff "#codec-aiff")<br>[Dolby E](#codec-dolby-e "#codec-dolby-e")<br>[MPEG<br>Audio](#codec-mpeg-audio "#codec-mpeg-audio")<br>[PCM](#codec-pcm "#codec-pcm") |
| Output                                | [AVC (H.264)](#codec-avc "#codec-avc")<br>[AVC-Intra](#codec-avc-intra "#codec-avc-intra")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")<br>[VC-3](#codec-vc3 "#codec-vc3") | Generic OP1a                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [PCM/WAV](#codec-pcm "#codec-pcm") |
| [MPEG-2](#codec-mpeg2 "#codec-mpeg2") | XDCAM RDD9                                                                                                                                                             |
| [MPEG-2](#codec-mpeg2 "#codec-mpeg2") | D10 (SMPTE-386)                                                                                                                                                        |
| [XAVC](#codec-xavc "#codec-xavc")     | Sony XAVC (RDD32)                                                                                                                                                      |

MediaConvert does not support MXF inputs with OP1b profiles.

For more information about creating MXF outputs, see [Creating MXF outputs](mxf.md "mxf.md").

For information about using MXF inputs to create Dolby Vision outputs, see
[Dolby
Vision input format support and job setting requirements](dolby-vision-job-limitations-and-requirements.md "dolby-vision-job-limitations-and-requirements.md").

**OGG (Ogg Vorbis Audio)**

| Container         | Input / Output                                                                         | Supported audio codec                                                                                                                     |
| ----------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| OGG               | Audio-only input                                                                       | [FLAC](#codec-flac "#codec-flac")<br>[Opus](#codec-opus-vorbis "#codec-opus-vorbis")<br>[Vorbis](#codec-opus-vorbis "#codec-opus-vorbis") |
| Audio-only output | [FLAC](#codec-flac "#codec-flac")<br>[Vorbis](#codec-opus-vorbis "#codec-opus-vorbis") |

**WAV (Waveform Audio File Format)**

| Container         | Input / Output                 | Supported audio codec                                            |
| ----------------- | ------------------------------ | ---------------------------------------------------------------- |
| WAV               | Audio-only input               | [GSM](#codec-gsm "#codec-gsm")<br>[PCM](#codec-pcm "#codec-pcm") |
| Audio-only output | [PCM](#codec-pcm "#codec-pcm") |

**WebM**

| Container | Input / Output                                                   | Supported video codec                                                                                | Supported audio codec                                                                                |
| --------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| WebM      | Input                                                            | [VP8](#codec-vp8 "#codec-vp8")<br>[VP9](#codec-vp9 "#codec-vp9")                                     | [Opus](#codec-opus-vorbis "#codec-opus-vorbis")<br>[Vorbis](#codec-opus-vorbis "#codec-opus-vorbis") |
| Output    | [VP8](#codec-vp8 "#codec-vp8")<br>[VP9](#codec-vp9 "#codec-vp9") | [Opus](#codec-opus-vorbis "#codec-opus-vorbis")<br>[Vorbis](#codec-opus-vorbis "#codec-opus-vorbis") |

**Y4M**

| Container | Input / Output | Supported video codec | Supported audio codec |
| --------- | -------------- | --------------------- | --------------------- |
| Y4M       | Input          | _Not<br>supported_    | _Not<br>supported_    |
| Output    | Uncompressed   | _Not<br>supported_    |

MediaConvert supports uncompressed Y4M outputs with I420, I422, or I444
four character codes (FOURCCs).

**No container**

| Container         | Input / Output                                                                                                                                                                                                                                                                             | Supported video codec                                                                                                                                                                                                                                                                                                                           | Supported audio codec |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| No container      | Video-only input                                                                                                                                                                                                                                                                           | [DV/DVCPRO](#codec-dv-dvcpro "#codec-dv-dvcpro")<br>[AVC (H.264)](#codec-avc "#codec-avc")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc")<br>[MPEG-1](#container-mpeg-1 "#container-mpeg-1")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")                                                                                                             | _Not<br>applicable_   |
| Video-only output | [AVC-Intra](#codec-avc-intra "#codec-avc-intra")<br>[AVC (H.264)](#codec-avc "#codec-avc")<br>[GIF](#codec-gif "#codec-gif")<br>[HEVC (H.265)](#codec-hevc "#codec-hevc")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")<br>[VC-3](#codec-vc3 "#codec-vc3")<br>[XAVC](#codec-xavc "#codec-xavc") | _Not<br>applicable_                                                                                                                                                                                                                                                                                                                             |
| Audio-only input  | _Not applicable_                                                                                                                                                                                                                                                                           | [AAC](#codec-aac "#codec-aac")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[FLAC](#codec-flac "#codec-flac")<br>[GSM](#codec-gsm "#codec-gsm")<br>[PCM](#codec-pcm "#codec-pcm")                                                                                       |
| Audio-only output | _Not applicable_                                                                                                                                                                                                                                                                           | [AAC](#codec-aac "#codec-aac")<br>[AIFF](#codec-aiff "#codec-aiff")<br>[Dolby Digital<br>(AC3)](#codec-ac3 "#codec-ac3")<br>[Dolby Digital Plus<br>(EAC3)](#codec-eac3 "#codec-eac3")<br>[FLAC](#codec-flac "#codec-flac")<br>[MPEG-2](#codec-mpeg2 "#codec-mpeg2")<br>[MP3](#container-mp3 "#container-mp3")<br>[PCM](#codec-pcm "#codec-pcm") |

## Supported codecs

This section contains reference tables for input and output codecs that MediaConvert
supports. The tables show the codec, support on the input or output side, and container
support for the codec. For more information about the container, or to see container
support for other codecs, choose the container link.

**AAC (Advanced Audio Codec)**

| Audio codec       | Input / Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Supported container                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AAC               | Input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [3G2](#container-3g2-3gp "#container-3g2-3gp")<br>[3GP](#container-3g2-3gp "#container-3g2-3gp")<br>[HLS](#container-hls "#container-hls")<br>[MPEG-4<br>Flash](#container-flash "#container-flash")<br>[Matroska](#container-matroska "#container-matroska")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-1](#container-mpeg-1 "#container-mpeg-1")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MXF](#container-mxf "#container-mxf") |
| Output            | [CMAF DASH](#container-cmaf "#container-cmaf")<br>[CMAF HLS](#container-cmaf "#container-cmaf")<br>[DASH](#container-dash "#container-dash")<br>[HLS](#container-hls "#container-hls")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-4<br>Flash](#container-flash "#container-flash")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MSS](#container-mss "#container-mss")<br>[No<br>container](#container-none "#container-none") |
| Audio-only input  | [MP4](#container-mp4 "#container-mp4")<br>[No<br>container](#container-none "#container-none")                                                                                                                                                                                                                                                                                                                                                                                               |
| Audio-only output | [DASH](#container-dash "#container-dash")<br>[HLS](#container-hls "#container-hls")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MP4](#container-mp4 "#container-mp4")<br>[No<br>container](#container-none "#container-none")                                                                                                                                                                                                                                                  |

For information about what output AAC profiles, coding modes, sample rates
, and bitrates MediaConvert supports, see [AAC output reference tables](aac-support.md "aac-support.md").

**AIFF**

| Audio codec       | Input / Output                                                                                 | Supported container                                                                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| AIFF              | Input                                                                                          | [MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MPEG-1](#container-mpeg-1 "#container-mpeg-1")<br>[MXF](#container-mxf "#container-mxf") |
| Output            | [MOV](#container-mov "#container-mov")<br>[No<br>container](#container-none "#container-none") |
| Audio-only input  | _Not<br>supported_                                                                             |
| Audio-only output | [No<br>container](#container-none "#container-none")                                           |

**AMR-NB, AMR-WB**

| Audio codec      | Input / Output     | Supported container                                                                              |
| ---------------- | ------------------ | ------------------------------------------------------------------------------------------------ |
| AMR-NB<br>AMR-WB | Input              | [3G2](#container-3g2-3gp "#container-3g2-3gp")<br>[3GP](#container-3g2-3gp "#container-3g2-3gp") |
| Output           | _Not<br>supported_ |

**Apple ProRes**

| Video codec  | Input / Output                         | Supported container                                                                                                        | Supported formats                                                                                                             |
| ------------ | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Apple ProRes | Input                                  | [IMF](#container-imf "#container-imf")<br>[MOV](#container-mov "#container-mov")<br>[MXF](#container-mxf "#container-mxf") | Apple ProRes 4444 XQ<br>Apple ProRes 4444<br>Apple ProRes 422 HQ<br>Apple ProRes 422<br>Apple ProRes LT<br>Apple ProRes Proxy |
| Output       | [MOV](#container-mov "#container-mov") |

For more information about Apple ProRes formats, see [https://support.apple.com/en-us/HT202410](https://support.apple.com/en-us/HT202410 "https://support.apple.com/en-us/HT202410").

You can also passthrough Apple ProRes inputs to MXF and MOV output
containers. For more information, see: [Video passthrough codec
support and job settings requirements](video-passthrough-feature-restrictions.md "video-passthrough-feature-restrictions.md")

###### Note

To preserve 4:4:4 chroma subsampling in your Apple ProRes outputs:

- You cannot include any of the following Preprocessors:
  **Dolby Vision**,
  **HDR10+**, or **Noise
  reducer**.
- You must use the Duplicate Drop as the frame rate conversion
  algorithm (when using frame rate conversion).
- You cannot mix RGB and non RGB inputs.
- You cannot mix 4:4:4 inputs with other non-4:4:4 inputs.
- You can only use the NexGuard File Maker preprocessor.

**AV1**

| Video codec | Input / Output                                                                                                                                                                         | Supported container                    |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| AV1         | Input                                                                                                                                                                                  | [MP4](#container-mp4 "#container-mp4") |
| Output      | [CMAF DASH](#container-cmaf "#container-cmaf")<br>[CMAF HLS](#container-cmaf "#container-cmaf")<br>[DASH](#container-dash "#container-dash")<br>[MP4](#container-mp4 "#container-mp4") |

###### Note

For HLS output codec recommendations from Apple, see [https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices "https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices").

**AVC (H.264)**

| Video codec | Input / Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Supported container                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AVC (H.264) | Input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [3G2](#container-3g2-3gp "#container-3g2-3gp")<br>[3GP](#container-3g2-3gp "#container-3g2-3gp")<br>[MPEG-4<br>Flash](#container-flash "#container-flash")<br>[HLS](#container-hls "#container-hls")<br>[Matroska](#container-matroska "#container-matroska")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") |
| Output      | [CMAF DASH](#container-cmaf "#container-cmaf")<br>[CMAF HLS](#container-cmaf "#container-cmaf")<br>[DASH](#container-dash "#container-dash")<br>[F4V](#container-flash "#container-flash")<br>[HLS](#container-hls "#container-hls")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MSS](#container-mss "#container-mss")<br>[MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") |

You can also passthrough AVC inputs to most output containers. For more
information, see: [Video passthrough codec
support and job settings requirements](video-passthrough-feature-restrictions.md "video-passthrough-feature-restrictions.md")

**AVC-Intra**

| Video codec | Input / Output                                                                                 | Supported container                                                                                                        | Supported formats                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| AVC-Intra   | Input                                                                                          | [MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MXF](#container-mxf "#container-mxf") | AVC-Intra 50<br>AVC-Intra 100<br>AVC-Intra 200<br>AVC-Intra 2K4:2:2<br>AVC-Intra 4K4:2:2 |
| Output      | [MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") | AVC-Intra 50<br>AVC-Intra 100<br>AVC-Intra 200<br>AVC-Intra 2K4:2:2<br>AVC-Intra 4K4:2:2                                   |

MediaConvert only supports YUV AVC-Intra inputs, it does not support RGB
AVC-Intra inputs.

You can also passthrough AVC-Intra inputs to MXF and MOV output
containers. For more information, see: [Video passthrough codec
support and job settings requirements](video-passthrough-feature-restrictions.md "video-passthrough-feature-restrictions.md")

**Canopus HQ**

| Video codec | Input / Output     | Supported container                    |
| ----------- | ------------------ | -------------------------------------- |
| Canopus HQ  | Input              | [AVI](#container-avi "#container-avi") |
| Output      | _Not<br>supported_ |

**Dolby Digital (AC3)**

| Audio codec         | Input / Output                                                                                                                                                                                                                                                                                                                                                                                                                     | Supported container                                                                                                                                                                                                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dolby Digital (AC3) | Input                                                                                                                                                                                                                                                                                                                                                                                                                              | [AVI](#container-avi "#container-avi")<br>[HLS](#container-hls "#container-hls")<br>[Matroska](#container-matroska "#container-matroska")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-1](#container-mpeg-1 "#container-mpeg-1")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts") |
| Output              | [CMAF DASH](#container-cmaf "#container-cmaf")<br>[CMAF HLS](#container-cmaf "#container-cmaf")<br>[DASH](#container-dash "#container-dash")<br>[HLS](#container-hls "#container-hls")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MSS](#container-mss "#container-mss")<br>[No<br>container](#container-none "#container-none") |
| Audio-only input    | [No<br>container](#container-none "#container-none")                                                                                                                                                                                                                                                                                                                                                                               |
| Audio-only output   | [DASH](#container-dash "#container-dash")<br>[HLS](#container-hls "#container-hls")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[No<br>container](#container-none "#container-none")                                                                                                                                                                                        |

**Dolby Digital Plus (EAC3)**

| Audio codec               | Input / Output                                                                                                                                                                                                                                                                                                                                                                        | Supported container                                                                                                                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dolby Digital Plus (EAC3) | Input                                                                                                                                                                                                                                                                                                                                                                                 | [AVI](#container-avi "#container-avi")<br>[HLS](#container-hls "#container-hls")<br>[Matroska](#container-matroska "#container-matroska")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-1](#container-mpeg-1 "#container-mpeg-1")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts") |
| Output                    | [CMAF DASH](#container-cmaf "#container-cmaf")<br>[CMAF HLS](#container-cmaf "#container-cmaf")<br>[HLS](#container-hls "#container-hls")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MSS](#container-mss "#container-mss")<br>[No<br>container](#container-none "#container-none") |
| Audio-only input          | [No<br>container](#container-none "#container-none")                                                                                                                                                                                                                                                                                                                                  |
| Audio-only output         | [DASH](#container-dash "#container-dash")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[No<br>container](#container-none "#container-none")                                                                                                                                                                                     |

**Dolby Digital Plus JOC (Atmos)**

For more information, see [Dolby Atmos](dolby-atmos.md "dolby-atmos.md").

**Dolby E**

| Audio codec | Input / Output     | Supported container                                                                                                                                                                            |
| ----------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dolby E     | Input              | [AVI](#container-avi "#container-avi")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") |
| Output      | _Not<br>supported_ |

**DV/DVCPRO**

| Video codec | Input / Output     | Supported container                                                                                                                                                                |
| ----------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DV/DVCPRO   | Input              | [AVI](#container-avi "#container-avi")<br>[MOV](#container-mov "#container-mov")<br>[MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") |
| Output      | _Not<br>supported_ |

You can also passthrough DV/DVCPRO inputs to MXF and MOV output
containers. For more information, see: [Video passthrough codec
support and job settings requirements](video-passthrough-feature-restrictions.md "video-passthrough-feature-restrictions.md")

**DV25, DV50**

| Video codec | Input / Output     | Supported container                    |
| ----------- | ------------------ | -------------------------------------- |
| DV25DV50    | Input              | [MXF](#container-mxf "#container-mxf") |
| Output      | _Not<br>supported_ |

**DVCPro HD**

| Video codec | Input / Output     | Supported container                    |
| ----------- | ------------------ | -------------------------------------- |
| DVCPro HD   | Input              | [MXF](#container-mxf "#container-mxf") |
| Output      | _Not<br>supported_ |

**DivX/Xvid**

| Video codec | Input / Output     | Supported container                                                                                                        |
| ----------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| DivX/Xvid   | Input              | [AVI](#container-avi "#container-avi")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4") |
| Output      | _Not<br>supported_ |

**FLAC**

| Audio codec       | Input / Output                                                                                                                                                                                                                              | Supported container                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| FLAC              | Input                                                                                                                                                                                                                                       | [Matroska](#container-matroska "#container-matroska")<br>[MP4](#container-mp4 "#container-mp4") |
| Output            | _Not<br>supported_                                                                                                                                                                                                                          |
| Audio-only input  | [Matroska](#container-matroska "#container-matroska")<br>[MP4](#container-mp4 "#container-mp4")<br>[OGA](#container-ogg "#container-ogg")<br>[OGG](#container-ogg "#container-ogg")<br>[No<br>container](#container-none "#container-none") |
| Audio-only output | [OGG](#container-ogg "#container-ogg")<br>[No<br>container](#container-none "#container-none")                                                                                                                                              |

**GSM**

| Audio codec       | Input / Output                                                                                 | Supported container                                                                            |
| ----------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| GSM               | Input                                                                                          | [WAV](#container-wav "#container-wav")<br>[No<br>container](#container-none "#container-none") |
| Output            | _Not<br>supported_                                                                             |
| Audio-only input  | [WAV](#container-wav "#container-wav")<br>[No<br>container](#container-none "#container-none") |
| Audio-only output | _Not<br>supported_                                                                             |

**GIF**

| Video codec | Input / Output                                       | Supported container                    |
| ----------- | ---------------------------------------------------- | -------------------------------------- |
| GIF         | Input                                                | [GIF](#container-gif "#container-gif") |
| Output      | [No<br>container](#container-none "#container-none") |

**H.261**

| Video codec | Input / Output     | Supported container                                                              |
| ----------- | ------------------ | -------------------------------------------------------------------------------- |
| H.261       | Input              | [MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4") |
| Output      | _Not<br>supported_ |

**H.262**

| Video codec | Input / Output     | Supported container                                                              |
| ----------- | ------------------ | -------------------------------------------------------------------------------- |
| H.262       | Input              | [MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4") |
| Output      | _Not<br>supported_ |

**H.263**

| Video codec | Input / Output     | Supported container                                                                                                                                                                                                                            |
| ----------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H.263       | Input              | [3G2](#container-3g2-3gp "#container-3g2-3gp")<br>[3GP](#container-3g2-3gp "#container-3g2-3gp")<br>[MPEG-4<br>Flash](#container-flash "#container-flash")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4") |
| Output      | _Not<br>supported_ |

**HEVC (H.265)**

| Video codec  | Input / Output                                                                                                                                                                                                                                                                                                                                                                           | Supported container                                                                                                                                                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HEVC (H.265) | Input                                                                                                                                                                                                                                                                                                                                                                                    | [HLS](#container-hls "#container-hls")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[No<br>container](#container-none "#container-none") |
| Output       | [CMAF HLS](#container-cmaf "#container-cmaf")<br>[CMAF DASH](#container-cmaf "#container-cmaf")<br>[DASH](#container-dash "#container-dash")<br>[HLS](#container-hls "#container-hls")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[No<br>container](#container-none "#container-none") |

###### Note

When outputting HEVC in an HLS container, we recommend using a CMAF
output group for the widest player compatibility. For more details, see
[https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices "https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices").

You can also passthrough HEVC inputs to supported output containers. For more
information, see: [Video passthrough codec
support and job settings requirements](video-passthrough-feature-restrictions.md "video-passthrough-feature-restrictions.md")

**JPEG 2000 (J2K)**

| Video codec     | Input / Output  | Supported container                                                                                                                                          |
| --------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| JPEG 2000 (J2K) | Input           | [IMF](#container-imf "#container-imf")<br>[MOV](#container-mov "#container-mov")[MP4](#container-mp4 "#container-mp4")[MXF](#container-mxf "#container-mxf") |
| Output          | _Not supported_ |

You can also passthrough J2K inputs to MXF and MOV output containers. For
more information, see: [Video passthrough codec
support and job settings requirements](video-passthrough-feature-restrictions.md "video-passthrough-feature-restrictions.md")

**MJPEG (Motion JPEG)**

| Video codec | Input / Output     | Supported container                                                              |
| ----------- | ------------------ | -------------------------------------------------------------------------------- |
| MJPEG       | Input              | [AVI](#container-avi "#container-avi")<br>[MOV](#container-mov "#container-mov") |
| Output      | _Not<br>supported_ |

**MP3 (MPEG-1 Layer 3)**

| Audio codec       | Input / Output                                       | Supported container                                                              |
| ----------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------- |
| MP3               | Input                                                | [AVI](#container-avi "#container-avi")<br>[MOV](#container-mov "#container-mov") |
| Output            | [MOV](#container-mov "#container-mov")               |
| Audio-only input  | [MP3](#container-mp3 "#container-mp3")               |
| Audio-only output | [No<br>container](#container-none "#container-none") |

**MPEG-1**

| Video codec | Input / Output     | Supported container                                                                                     |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------------------- |
| MPEG-1      | Input              | [MPEG-1](#container-mpeg-1 "#container-mpeg-1")<br>[No<br>container](#container-none "#container-none") |
| Output      | _Not<br>supported_ |

**MPEG-2 (MPEG-1 Layer II )**

| Video codec  | Input / Output                                                                                                                                                                                                                                           | Supported container                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MPEG-2 Video | Input                                                                                                                                                                                                                                                    | [HLS](#container-hls "#container-hls")<br>[Matroska](#container-matroska "#container-matroska")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-1](#container-mpeg-1 "#container-mpeg-1")<br>[MPEG-PS](#container-mpeg-ps "#container-mpeg-ps")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") |
| Output       | [MOV](#container-mov "#container-mov")<br>[MPEG-4<br>Flash](#container-flash "#container-flash")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") |

| Audio codec       | Input / Output                                                                                             | Supported container                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| MPEG-2 Audio      | Audio-only input                                                                                           | [MPEG-TS](#container-mpeg-ts "#container-mpeg-ts") |
| Audio-only output | [MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[No<br>container](#container-none "#container-none") |

**MPEG-4 Part 2**

| Video codec   | Input / Output  | Supported container                                                                                                                                                                                                                           |
| ------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MPEG-4 Part 2 | Input           | [3G2](#container-3g2-3gp "#container-3g2-3gp")<br>[3GP](#container-3g2-3gp "#container-3g2-3gp")<br>[Matroska](#container-matroska "#container-matroska")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4") |
| Output        | _Not supported_ |

**MPEG Audio**

| Audio codec | Input / Output     | Supported container                                                                                                                                                                                                                             |
| ----------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MPEG Audio  | Input              | [AVI](#container-avi "#container-avi")<br>[MPEG-1](#container-mpeg-1 "#container-mpeg-1")<br>[MPEG-PS](#container-mpeg-ps "#container-mpeg-ps")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MXF](#container-mxf "#container-mxf") |
| Output      | _Not<br>supported_ |

**Opus, Vorbis**

| Audio codec       | Input / Output                                                                                                                            | Supported container                                                                                                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Opus<br>Vorbis    | Input                                                                                                                                     | [Matroska](#container-matroska "#container-matroska")<br>[OGA](#container-ogg "#container-ogg")<br>[OGG](#container-ogg "#container-ogg")<br>[WebM](#container-webm "#container-webm") |
| Output            | [WebM](#container-webm "#container-webm")                                                                                                 |
| Audio-only input  | [Matroska](#container-matroska "#container-matroska")<br>[OGA](#container-ogg "#container-ogg")<br>[OGG](#container-ogg "#container-ogg") |
| Audio-only output | [OGG](#container-ogg "#container-ogg")                                                                                                    |

**Panasonic P2**

| Video codec  | Input / Output     | Supported container                    |
| ------------ | ------------------ | -------------------------------------- |
| Panasonic P2 | Input              | [MXF](#container-mxf "#container-mxf") |
| Output       | _Not<br>supported_ |

**PCM**

| Audio codec       | Input / Output                                                                                                                                                                                 | Supported container                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PCM               | Input                                                                                                                                                                                          | [AVI](#container-avi "#container-avi")<br>[IMF](#container-imf "#container-imf")<br>[Matroska](#container-matroska "#container-matroska")<br>[MOV](#container-mov "#container-mov")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-1](#container-mpeg-1 "#container-mpeg-1")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") |
| Output            | [MOV](#container-mov "#container-mov")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") |
| Audio-only input  | [MOV](#container-mov "#container-mov")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[WAV](#container-wav "#container-wav")                                                         |
| Audio-only output | [WAV](#container-wav "#container-wav")<br>[No<br>container](#container-none "#container-none")                                                                                                 |

**Quicktime RLE (Quicktime Animation)**

| Video codec   | Input / Output     | Supported container                    |
| ------------- | ------------------ | -------------------------------------- |
| Quicktime RLE | Input              | [MOV](#container-mov "#container-mov") |
| Output        | _Not<br>supported_ |

**Sony XDCAM**

| Video format | Input / Output                         | Supported container                    |
| ------------ | -------------------------------------- | -------------------------------------- |
| Sony XDCAM   | Input                                  | [MXF](#container-mxf "#container-mxf") |
| Output       | [MXF](#container-mxf "#container-mxf") |

**Sony XDCAM MPEG-4 Proxy**

| Video format | Input / Output     | Supported container                    |
| ------------ | ------------------ | -------------------------------------- |
| Sony XDCAM   | Input              | [MXF](#container-mxf "#container-mxf") |
| Output       | _Not<br>supported_ |

**VC-1**

| Video codec | Input / Output     | Supported container                                                                                                                                                                                                                                                       |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VC-1        | Input              | [ASF](#container-asf-wmv-wma "#container-asf-wmv-wma")<br>[Matroska](#container-matroska "#container-matroska")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[WMV](#container-asf-wmv-wma "#container-asf-wmv-wma") |
| Output      | _Not<br>supported_ |

**VC-3**

| Video codec | Input / Output                                                                                 | Supported container                    |
| ----------- | ---------------------------------------------------------------------------------------------- | -------------------------------------- |
| VC-3        | Input                                                                                          | [MXF](#container-mxf "#container-mxf") |
| Output      | [MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") |

You can also passthrough VC-3 inputs to MXF and MOV output containers. For
more information, see: [Video passthrough codec
support and job settings requirements](video-passthrough-feature-restrictions.md "video-passthrough-feature-restrictions.md")

**VP8**

| Video codec | Input / Output                                                                         | Supported container                       |
| ----------- | -------------------------------------------------------------------------------------- | ----------------------------------------- |
| VP8         | Input                                                                                  | [WebM](#container-webm "#container-webm") |
| Output      | [DASH](#container-dash "#container-dash")<br>[WebM](#container-webm "#container-webm") |

**VP9**

| Video codec | Input / Output                                                                                                                                                                            | Supported container                                                                 |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| VP9         | Input                                                                                                                                                                                     | [MP4](#container-mp4 "#container-mp4")<br>[WebM](#container-webm "#container-webm") |
| Output      | [CMAF DASH](#container-cmaf "#container-cmaf")<br>[CMAF HLS](#container-cmaf "#container-cmaf")<br>[DASH](#container-dash "#container-dash")<br>[WebM](#container-webm "#container-webm") |

**WMA, WMA2**

| Audio codec       | Input / Output                                                                                                                                                             | Supported container                                                                                                                                                                                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WMA<br>WMA2       | Input                                                                                                                                                                      | [ASF](#container-asf-wmv-wma "#container-asf-wmv-wma")<br>[Matroska](#container-matroska "#container-matroska")<br>[MP4](#container-mp4 "#container-mp4")<br>[MPEG-TS](#container-mpeg-ts "#container-mpeg-ts")<br>[WMV](#container-asf-wmv-wma "#container-asf-wmv-wma") |
| Output            | _Not<br>supported_                                                                                                                                                         |
| Audio-only input  | [ASF](#container-asf-wmv-wma "#container-asf-wmv-wma")<br>[WMA](#container-asf-wmv-wma "#container-asf-wmv-wma")<br>[WMV](#container-asf-wmv-wma "#container-asf-wmv-wma") |
| Audio-only output | _Not supported_                                                                                                                                                            |

**WMA Pro**

| Video codec       | Input / Output                                                                                                                                                             | Supported container                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| WMA Pro           | Input                                                                                                                                                                      | [ASF](#container-asf-wmv-wma "#container-asf-wmv-wma")<br>[WMV](#container-asf-wmv-wma "#container-asf-wmv-wma") |
| Output            | _Not<br>supported_                                                                                                                                                         |
| Audio-only input  | [ASF](#container-asf-wmv-wma "#container-asf-wmv-wma")<br>[WMA](#container-asf-wmv-wma "#container-asf-wmv-wma")<br>[WMV](#container-asf-wmv-wma "#container-asf-wmv-wma") |
| Audio-only output | _Not<br>supported_                                                                                                                                                         |

**XAVC**

| Format | Input / Output | Supported container                                                                            | Supported XAVC profiles                                                           |
| ------ | -------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| XAVC   | Output         | [MXF](#container-mxf "#container-mxf")<br>[No<br>container](#container-none "#container-none") | XAVC HD<br>XAVC HD Intra CBG<br>XAVC 4K<br>XAVC 4K Intra CBG<br>XAVC 4K Intra VBR |

For more information about the XAVC format, see: [https://pro.sony/ue_US/technology/xavc](https://pro.sony/ue_US/technology/xavc "https://pro.sony/ue_US/technology/xavc").

XAVC inputs are supported, as they are a subset of [MXF](#container-mxf "#container-mxf") containers with [AVC (H.264)](#codec-avc "#codec-avc") video codecs.
