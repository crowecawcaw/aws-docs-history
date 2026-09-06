

# Supported containers and codecs reference tables
<a name="supported-containers-codecs-details"></a>

The following sections provide reference tables for containers and codecs that MediaConvert supports. 

To use these tables, first find the container or codec using the links following this introduction. For containers, the tables provide details for which video or audio codecs are supported, and whether they're supported for inputs or outputs. For codecs, the tables provide details for which containers are supported, for inputs and outputs as well. Note that inputs or outputs labeled like *Audio-only input* or *Audio-only output* refer to support for audio-only workflows. For more information, see [Creating audio-only outputs](audio-only.md).

For quick reference tables that show which input formats MediaConvert supports, see [Supported input formats](reference-codecs-containers-input.md).

For quick reference tables that show which output formats MediaConvert supports, see [Supported output formats](reference-codecs-containers.md).

**Containers**  
 [3G2](#container-3g2-3gp) \| [3GP](#container-3g2-3gp) \| [ASF](#container-asf-wmv-wma) \| [AVI](#container-avi) \| [CMAF](#container-cmaf) \| [DASH](#container-dash) \| [F4V](#container-flash) \| [FLV](#container-flash) \| [GIF](#container-gif) \| [HLS](#container-hls) \| [IMF](#container-imf) \| [Matroska](#container-matroska) \| [MOV](#container-mov) \| [MP3](#container-mp3) \| [MP4](#container-mp4) \| [MPEG-1](#container-mpeg-1) \| [MPEG-PS](#container-mpeg-ps) \| [MPEG-TS](#container-mpeg-ts) \| [MSS](#container-mss) \| [MXF](#container-mxf) \| [OGG](#container-ogg) \| [WAV](#container-wav) \| [WebM](#container-webm) \| [WMA](#container-asf-wmv-wma) \| [WMV](#container-asf-wmv-wma) \| [Y4M](#container-y4m) \| [No container](#container-none) 

**Codecs**  
 [AAC](#codec-aac) \| [AIFF](#codec-aiff) \| [AMR-NB](#codec-amr) \| [AMR-WB](#codec-amr) \| [Apple ProRes](#codec-apple-prores) \| [AV1](#codec-av1) \| [AVC (H.264)](#codec-avc) \| [AVC-Intra](#codec-avc-intra) \| [Canopus HQ](#codec-canopus-hq) \| [Dolby Atmos](#codec-atmos) \| [Dolby Digital (AC3)](#codec-ac3) \| [Dolby Digital Plus (EAC3)](#codec-eac3) \| [Dolby E](#codec-dolby-e) \| [DV/DVCPRO](#codec-dv-dvcpro) \| [DV25](#codec-dv25-dv50) \| [DV50](#codec-dv25-dv50) \| [DVCPro HD](#codec-dvcpro-hd) \| [DivX/Xvid](#codec-divx) \| [FLAC](#codec-flac) \| [GIF](#codec-gif) \| [GSM](#codec-gsm) \| [H.261](#codec-h261) \| [H.262](#codec-h262) \| [H.263](#codec-h263) \| [HEVC (H.265)](#codec-hevc) \| [J2K](#codec-j2k) \| [MJPEG](#codec-mjpeg) \| [MP3](#codec-mp3) \| [MPEG-1](#codec-mpeg1) \| [MPEG-2](#codec-mpeg2) \| [MPEG-4 Part 2](#codec-mpeg-4-part-2) \| [MPEG Audio](#codec-mpeg-audio) \| [Opus](#codec-opus-vorbis) \| [Panasonic P2](#codec-p2) \| [PCM](#codec-pcm) \| [QuickTime RLE](#codec-quicktime-rle) \| [Sony XDCAM](#codec-xdcam) \| [Sony XDCAM MPEG-4 Proxy](#codec-xdcam-mp4) \| [VC-1](#codec-vc1) \| [VC-3](#codec-vc3) \| [Vorbis](#codec-opus-vorbis) \| [VP8](#codec-vp8) \| [VP9](#codec-vp9) \| [WMA](#codec-wma) \| [WMA2](#codec-wma) \| [WMA Pro](#codec-wma-pro) \| [XAVC](#codec-xavc) 

**Topics**
+ [Supported containers](#containers)
+ [Supported codecs](#codecs)

## Supported containers
<a name="containers"></a>

This section contains reference tables for input and output containers that MediaConvert supports. The tables show the container, support on the input or output side, and video or audio codec support in the container. For more information about the codec, or to see codec support in other containers, choose the codec link.

**3G2, 3GP**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**ASF, WMV, WMA (Advanced Systems Format)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**AVI (Audio Video Interleave)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**CMAF (Common Media Application Format)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
For HLS output codec recommendations from Apple, see: [https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices).

**DASH (Dynamic Adaptive Streaming over HTTP)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
For information about CMAF DASH, see [CMAF containers](#container-cmaf).

**FLV, F4V (MPEG-4 Flash)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**GIF**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**HLS (Apple HTTP Live Streaming)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
For more information about HLS inputs and input requirements, see [HLS input requirements](using-hls-inputs.md).  
For information about CMAF HLS, see [CMAF containers](#container-cmaf).  
When outputting HEVC in an HLS container, we recommend using a CMAF output group for the widest player compatibility. For more details, see [https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices).

**IMF (Interoperable Master Format)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
Specify your input IMF by providing the path to your Composition Playlist (CPL). If the CPL is in an incomplete IMP, also specify any supplemental IMPs.  
For information about using IMF inputs to create Dolby Vision outputs, see [Dolby Vision input format support and job setting requirements](dolby-vision-job-limitations-and-requirements.md).

**Matroska**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**MOV (Apple QuickTime)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
MOV inputs must be self-contained. References to external files are not supported.  
For information about using MOV inputs to create Dolby Vision outputs, see [Dolby Vision input format support and job setting requirements](dolby-vision-job-limitations-and-requirements.md).

**MP3 (MPEG-1 Layer 3)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
MediaConvert does not read ID3 metadata or tags from MP3 inputs.

**MP4 (MPEG-4)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
MediaConvert doesn't support fragmented MP4 initialization segments. Your MP4 input must be self-contained.   
For information about creating MV-HEVC stereoscopic video outputs in MP4 containers, see [Creating MV-HEVC spatial video outputs with AWS Elemental MediaConvert](mv-hevc-spatial-video.md).

**MPEG-1 (MPEG-1 System Stream)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**MPEG-PS (MPEG Program Stream)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**MPEG-TS (MPEG-2 Transport Stream)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**MSS (Microsoft Smooth Streaming)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**MXF (Material Exchange Format)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
MediaConvert does not support MXF inputs with OP1b profiles.  
For more information about creating MXF outputs, see [Creating MXF outputs](mxf.md).  
For information about using MXF inputs to create Dolby Vision outputs, see [Dolby Vision input format support and job setting requirements](dolby-vision-job-limitations-and-requirements.md).

**OGG (Ogg Vorbis Audio)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**WAV (Waveform Audio File Format)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**WebM**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**Y4M**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
MediaConvert supports uncompressed Y4M outputs with I420, I422, or I444 four character codes (FOURCCs).

**No container**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

## Supported codecs
<a name="codecs"></a>

This section contains reference tables for input and output codecs that MediaConvert supports. The tables show the codec, support on the input or output side, and container support for the codec. For more information about the container, or to see container support for other codecs, choose the container link.

**AAC (Advanced Audio Codec)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
For information about what output AAC profiles, coding modes, sample rates , and bitrates MediaConvert supports, see [AAC output reference tables](aac-support.md).

**AIFF**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**AMR-NB, AMR-WB**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**Apple ProRes**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
For more information about Apple ProRes formats, see [https://support.apple.com/en-us/HT202410](https://support.apple.com/en-us/HT202410).  
You can also passthrough Apple ProRes inputs to MXF and MOV output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)  
To preserve 4:4:4 chroma subsampling in your Apple ProRes outputs:   
+ You cannot include any of the following Preprocessors: **Dolby Vision**, **HDR10\+**, or **Noise reducer**.
+ You must use the Duplicate Drop as the frame rate conversion algorithm (when using frame rate conversion).
+ You cannot mix RGB and non RGB inputs. 
+ You cannot mix 4:4:4 inputs with other non-4:4:4 inputs. 
+ You can only use the NexGuard File Maker preprocessor.

**AV1**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
For HLS output codec recommendations from Apple, see [https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices).

**AVC (H.264)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
You can also passthrough AVC inputs to most output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**AVC-Intra**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
MediaConvert only supports YUV AVC-Intra inputs, it does not support RGB AVC-Intra inputs.  
You can also passthrough AVC-Intra inputs to MXF and MOV output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**Canopus HQ**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**Dolby Digital (AC3)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**Dolby Digital Plus (EAC3)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**Dolby Digital Plus JOC (Atmos)**  
For more information, see [Dolby Atmos](dolby-atmos.md). 

**Dolby E**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**DV/DVCPRO**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
You can also passthrough DV/DVCPRO inputs to MXF and MOV output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**DV25, DV50**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**DVCPro HD**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**DivX/Xvid**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**FLAC**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**GSM**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**GIF**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**H.261**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**H.262**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**H.263**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**HEVC (H.265)**  <a name="codec-hevc"></a>    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
When outputting HEVC in an HLS container, we recommend using a CMAF output group for the widest player compatibility. For more details, see [https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices).
You can also passthrough HEVC inputs to supported output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**JPEG 2000 (J2K)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
You can also passthrough J2K inputs to MXF and MOV output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**MJPEG (Motion JPEG)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**MP3 (MPEG-1 Layer 3)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**MPEG-1**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**MPEG-2 (MPEG-1 Layer II )**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**MPEG-4 Part 2**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**MPEG Audio**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**Opus, Vorbis**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**Panasonic P2**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**PCM**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**Quicktime RLE (Quicktime Animation)**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**Sony XDCAM**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**Sony XDCAM MPEG-4 Proxy**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**VC-1**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**VC-3**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
You can also passthrough VC-3 inputs to MXF and MOV output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**VP8**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**VP9**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**WMA, WMA2**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**WMA Pro**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)

**XAVC**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/mediaconvert/latest/ug/supported-containers-codecs-details.html)
For more information about the XAVC format, see: [https://pro.sony/ue\_US/technology/xavc](https://pro.sony/ue_US/technology/xavc).  
XAVC inputs are supported, as they are a subset of [MXF](#container-mxf) containers with [AVC (H.264)](#codec-avc) video codecs.

****  