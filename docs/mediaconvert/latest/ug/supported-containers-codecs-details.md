

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


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">3G2<br />3GP</td><td>Input</td><td><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-h263">H.263</a><br /><a href="#codec-mpeg-4-part-2">MPEG-4 part 2</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-amr">AMR-NB</a><br /><a href="#codec-amr">AMR-WB</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**ASF, WMV, WMA (Advanced Systems Format)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">ASFWMV</td><td>Input</td><td><a href="#codec-vc1">VC-1</a></td><td><a href="#codec-wma">WMA</a><br /><a href="#codec-wma">WMA2</a><br /><a href="#codec-wma-pro">WMA Pro</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
  <tr><td rowspan="2">WMA</td><td>Audio-only input</td><td><i>Not applicable</i></td><td><a href="#codec-wma">WMA</a><br /><a href="#codec-wma">WMA2</a><br /><a href="#codec-wma-pro">WMA Pro</a></td></tr>
  <tr><td>Audio-only output</td><td><i>Not applicable</i></td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**AVI (Audio Video Interleave)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">AVI</td><td>Input</td><td><a href="#codec-canopus-hq">Canopus HQ</a><br /><a href="#codec-divx">DivX/Xvid</a><br /><a href="#codec-dv-dvcpro">DV/DVCPRO</a><br /><a href="#codec-mjpeg">MJPEG</a><br />Uncompressed</td><td><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-dolby-e">Dolby E</a><br /><a href="#container-mp3">MP3</a><br /><a href="#codec-mpeg-audio">MPEG Audio</a><br /><a href="#codec-pcm">PCM</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**CMAF (Common Media Application Format)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">CMAF DASH</td><td>Input</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
  <tr><td>Output</td><td><a href="#codec-av1">AV1</a><br /><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-hevc">HEVC (H.265)</a><br /><a href="#codec-vp9">VP9</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a></td></tr>
  <tr><td rowspan="2">CMAF HLS</td><td>Input</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
  <tr><td>Output</td><td><a href="#codec-av1">AV1</a><br /><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-hevc">HEVC (H.265)</a><br /><a href="#codec-vp9">VP9</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a></td></tr>
</tbody>
</table>

For HLS output codec recommendations from Apple, see: [https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices).

**DASH (Dynamic Adaptive Streaming over HTTP)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">DASH</td><td>Input</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
  <tr><td>Output</td><td><a href="#codec-av1">AV1</a><br /><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-hevc">HEVC (H.265)</a><br /><a href="#codec-vp8">VP8</a><br /><a href="#codec-vp9">VP9</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a></td></tr>
  <tr><td>Audio-only input</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
  <tr><td>Audio-only output</td><td><i>Not applicable</i></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-atmos">Dolby Digital Plus JOC (Atmos)</a></td></tr>
</tbody>
</table>

For information about CMAF DASH, see [CMAF containers](#container-cmaf).

**FLV, F4V (MPEG-4 Flash)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td>FLV<br />F4V</td><td>Input</td><td><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-h263">H.263</a></td><td><a href="#codec-aac">AAC</a></td></tr>
  <tr><td>F4V</td><td>Output</td><td><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-mpeg2">MPEG-2</a></td><td><a href="#codec-aac">AAC</a></td></tr>
</tbody>
</table>


**GIF**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">GIF</td><td>Input</td><td><a href="#codec-gif">GIF</a></td></tr>
  <tr><td>Output</td><td><a href="#codec-gif">GIF</a></td></tr>
</tbody>
</table>


**HLS (Apple HTTP Live Streaming)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">HLS</td><td>Input</td><td><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-hevc">HEVC (H.265)</a><br /><a href="#codec-mpeg2">MPEG-2</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a></td></tr>
  <tr><td>Output</td><td><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-hevc">HEVC (H.265)</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a></td></tr>
  <tr><td>Audio-only input</td><td><i>Not applicable</i></td><td><i>Not supported</i></td></tr>
  <tr><td>Audio-only output</td><td><i>Not applicable</i></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a></td></tr>
</tbody>
</table>

For more information about HLS inputs and input requirements, see [HLS input requirements](using-hls-inputs.md).  
For information about CMAF HLS, see [CMAF containers](#container-cmaf).  
When outputting HEVC in an HLS container, we recommend using a CMAF output group for the widest player compatibility. For more details, see [https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices).

**IMF (Interoperable Master Format)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">IMF</td><td>Input</td><td><a href="#codec-apple-prores">Apple ProRes</a><br /><a href="#codec-j2k">JPEG 2000 (J2K)</a></td><td><a href="#codec-pcm">PCM</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
</tbody>
</table>

Specify your input IMF by providing the path to your Composition Playlist (CPL). If the CPL is in an incomplete IMP, also specify any supplemental IMPs.  
For information about using IMF inputs to create Dolby Vision outputs, see [Dolby Vision input format support and job setting requirements](dolby-vision-job-limitations-and-requirements.md).

**Matroska**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">Matroska</td><td>Input</td><td><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-mpeg2">MPEG-2</a><br /><a href="#codec-mpeg-4-part-2">MPEG-4 part 2</a><br /><a href="#codec-vc1">VC-1</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-flac">FLAC</a><br /><a href="#codec-opus-vorbis">Opus</a><br /><a href="#codec-pcm">PCM</a><br /><a href="#codec-wma">WMA</a><br /><a href="#codec-wma">WMA2</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
  <tr><td>Audio-only input</td><td><i>Not applicable</i></td><td><a href="#codec-flac">FLAC</a><br /><a href="#codec-opus-vorbis">OPUS</a></td></tr>
  <tr><td>Audio-only output</td><td><i>Not applicable</i></td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**MOV (Apple QuickTime)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="5">MOV</td><td>Input</td><td><a href="#codec-apple-prores">Apple ProRes</a><br /><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-avc-intra">AVC-Intra</a><br /><a href="#codec-divx">DivX/Xvid</a><br /><a href="#codec-dv-dvcpro">DV/DVCPRO</a><br /><a href="#codec-h261">H.261</a><br /><a href="#codec-h262">H.262</a><br /><a href="#codec-h263">H.263</a><br /><a href="#codec-hevc">HEVC (H.265)</a><br /><a href="#codec-j2k">JPEG 2000 (J2K)</a><br /><a href="#codec-mjpeg">MJPEG</a><br /><a href="#codec-mpeg2">MPEG-2</a><br /><a href="#codec-mpeg-4-part-2">MPEG-4 part 2</a><br /><a href="#codec-quicktime-rle">QuickTime RLE</a><br />Uncompressed</td><td><a href="#codec-aac">AAC</a><br /><a href="#container-mp3">MP3</a><br /><a href="#codec-pcm">PCM</a></td></tr>
  <tr><td rowspan="2">Output</td><td><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-mpeg2">MPEG-2</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-pcm">WAV</a></td></tr>
  <tr><td><a href="#codec-apple-prores">Apple ProRes</a></td><td><a href="#codec-aiff">AIFF</a></td></tr>
  <tr><td>Audio-only input</td><td><i>Not applicable</i></td><td><a href="#codec-pcm">PCM</a></td></tr>
  <tr><td>Audio-only output</td><td><i>Not applicable</i></td><td><i>Not supported</i></td></tr>
</tbody>
</table>

MOV inputs must be self-contained. References to external files are not supported.  
For information about using MOV inputs to create Dolby Vision outputs, see [Dolby Vision input format support and job setting requirements](dolby-vision-job-limitations-and-requirements.md).

**MP3 (MPEG-1 Layer 3)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2"><a href="#codec-mp3">MP3</a></td><td>Audio-only input</td><td><a href="#codec-mp3">MP3</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#codec-mp3">MP3</a></td></tr>
</tbody>
</table>

MediaConvert does not read ID3 metadata or tags from MP3 inputs.

**MP4 (MPEG-4)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">MP4</td><td>Input</td><td><a href="#codec-av1">AV1</a><br /><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-avc-intra">AVC-Intra</a><br /><a href="#codec-divx">DivX/Xvid</a><br /><a href="#codec-h261">H.261</a><br /><a href="#codec-h262">H.262</a><br /><a href="#codec-h263">H.263</a><br /><a href="#codec-hevc">HEVC (H.265)</a><br /><a href="#codec-j2k">JPEG 2000 (J2K)</a><br /><a href="#codec-mpeg2">MPEG-2</a><br /><a href="#codec-mpeg-4-part-2">MPEG-4 part 2</a><br /><a href="#codec-vc1">VC-1</a><br /><a href="#codec-vp9">VP9</a><br />Uncompressed</td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-flac">FLAC</a><br /><a href="#codec-pcm">PCM</a><br /><a href="#codec-wma">WMA</a><br /><a href="#codec-wma">WMA2</a></td></tr>
  <tr><td>Output</td><td><a href="#codec-av1">AV1</a><br /><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-hevc">HEVC (H.265)</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a></td></tr>
  <tr><td>Audio-only input</td><td><i>Not applicable</i></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-flac">FLAC</a></td></tr>
  <tr><td>Audio-only output</td><td><i>Not applicable</i></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a></td></tr>
</tbody>
</table>

MediaConvert doesn't support fragmented MP4 initialization segments. Your MP4 input must be self-contained.   
For information about creating MV-HEVC stereoscopic video outputs in MP4 containers, see [Creating MV-HEVC spatial video outputs with AWS Elemental MediaConvert](mv-hevc-spatial-video.md).

**MPEG-1 (MPEG-1 System Stream)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">MPEG-1</td><td>Input</td><td><a href="#codec-mpeg1">MPEG-1</a><br /><a href="#codec-mpeg2">MPEG-2</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-aiff">AIFF</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-mpeg-audio">MPEG Audio</a> <br /><a href="#codec-pcm">PCM</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**MPEG-PS (MPEG Program Stream)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">MPEG-PS</td><td>Input</td><td><a href="#codec-mpeg2">MPEG-2</a></td><td><a href="#codec-mpeg-audio">MPEG audio</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**MPEG-TS (MPEG-2 Transport Stream)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">MPEG-TS</td><td>Input</td><td><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-hevc">HEVC (H.265)</a><br /><a href="#codec-mpeg2">MPEG-2</a><br /><a href="#codec-vc1">VC-1</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-aiff">AIFF</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-dolby-e">Dolby E</a><br /><a href="#codec-mpeg-audio">MPEG Audio</a><br /><a href="#codec-pcm">PCM</a><br /><a href="#codec-wma">WMA</a><br /><a href="#codec-wma">WMA2</a></td></tr>
  <tr><td>Output</td><td><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-hevc">HEVC (H.265)</a><br /><a href="#codec-mpeg2">MPEG-2</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-mpeg2">MPEG-2</a><br /><a href="#codec-pcm">PCM/WAV</a></td></tr>
  <tr><td>Audio-only input</td><td><i>Not applicable</i></td><td><a href="#codec-mpeg2">MPEG-2</a><br /><a href="#codec-pcm">PCM</a></td></tr>
  <tr><td>Audio-only output</td><td><i>Not applicable</i></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-mpeg2">MPEG-2</a></td></tr>
</tbody>
</table>


**MSS (Microsoft Smooth Streaming)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">MSS</td><td>Input</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
  <tr><td>Output</td><td><a href="#codec-avc">AVC (H.264)</a></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a></td></tr>
</tbody>
</table>


**MXF (Material Exchange Format)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>MXF Profile</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="5">MXF</td><td>Input</td><td><a href="#codec-apple-prores">Apple ProRes</a><br /><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-avc-intra">AVC-Intra</a><br /><a href="#codec-dv-dvcpro">DV/DVCPRO</a><br /><a href="#codec-dv25-dv50">DV25</a><br /><a href="#codec-dv25-dv50">DV50</a><br /><a href="#codec-dvcpro-hd">DVCPro HD</a><br /><a href="#codec-j2k">JPEG 2000 (J2K)</a><br /><a href="#codec-mpeg2">MPEG-2</a><br /><a href="#codec-p2">Panasonic P2</a><br /><a href="#codec-xdcam">Sony XDCam</a><br /><a href="#codec-xdcam-mp4">Sony XDCam MPEG-4 Proxy</a><br />Uncompressed</td><td><i>Not applicable</i></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-aiff">AIFF</a><br /><a href="#codec-dolby-e">Dolby E</a><br /><a href="#codec-mpeg-audio">MPEG Audio</a><br /><a href="#codec-pcm">PCM</a></td></tr>
  <tr><td rowspan="4">Output</td><td><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-avc-intra">AVC-Intra</a><br /><a href="#codec-mpeg2">MPEG-2</a><br /><a href="#codec-vc3">VC-3</a></td><td>Generic OP1a</td><td rowspan="4"><a href="#codec-pcm">PCM/WAV</a></td></tr>
  <tr><td><a href="#codec-mpeg2">MPEG-2</a></td><td>XDCAM RDD9</td></tr>
  <tr><td><a href="#codec-mpeg2">MPEG-2</a></td><td>D10 (SMPTE-386)</td></tr>
  <tr><td><a href="#codec-xavc">XAVC</a></td><td>Sony XAVC (RDD32)</td></tr>
</tbody>
</table>

MediaConvert does not support MXF inputs with OP1b profiles.  
For more information about creating MXF outputs, see [Creating MXF outputs](mxf.md).  
For information about using MXF inputs to create Dolby Vision outputs, see [Dolby Vision input format support and job setting requirements](dolby-vision-job-limitations-and-requirements.md).

**OGG (Ogg Vorbis Audio)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">OGG</td><td>Audio-only input</td><td><a href="#codec-flac">FLAC</a><br /><a href="#codec-opus-vorbis">Opus</a><br /><a href="#codec-opus-vorbis">Vorbis</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#codec-flac">FLAC</a><br /><a href="#codec-opus-vorbis">Vorbis</a></td></tr>
</tbody>
</table>


**WAV (Waveform Audio File Format)**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">WAV</td><td>Audio-only input</td><td><a href="#codec-gsm">GSM</a><br /><a href="#codec-pcm">PCM</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#codec-pcm">PCM</a></td></tr>
</tbody>
</table>


**WebM**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">WebM</td><td>Input</td><td><a href="#codec-vp8">VP8</a><br /><a href="#codec-vp9">VP9</a></td><td><a href="#codec-opus-vorbis">Opus</a><br /><a href="#codec-opus-vorbis">Vorbis</a></td></tr>
  <tr><td>Output</td><td><a href="#codec-vp8">VP8</a><br /><a href="#codec-vp9">VP9</a></td><td><a href="#codec-opus-vorbis">Opus</a><br /><a href="#codec-opus-vorbis">Vorbis</a></td></tr>
</tbody>
</table>


**Y4M**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">Y4M</td><td>Input</td><td><i>Not supported</i></td><td><i>Not supported</i></td></tr>
  <tr><td>Output</td><td>Uncompressed</td><td><i>Not supported</i></td></tr>
</tbody>
</table>

MediaConvert supports uncompressed Y4M outputs with I420, I422, or I444 four character codes (FOURCCs).

**No container**  


<table>
<thead>
  <tr><th>Container</th><th>Input / Output</th><th>Supported video codec</th><th>Supported audio codec</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">No container</td><td>Video-only input</td><td><a href="#codec-dv-dvcpro">DV/DVCPRO</a><br /><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-hevc">HEVC (H.265)</a><br /><a href="#container-mpeg-1">MPEG-1</a><br /><a href="#codec-mpeg2">MPEG-2</a></td><td><i>Not applicable</i></td></tr>
  <tr><td>Video-only output</td><td><a href="#codec-avc-intra">AVC-Intra</a><br /><a href="#codec-avc">AVC (H.264)</a><br /><a href="#codec-gif">GIF</a><br /><a href="#codec-hevc">HEVC (H.265)</a><br /><a href="#codec-mpeg2">MPEG-2</a><br /><a href="#codec-vc3">VC-3</a><br /><a href="#codec-xavc">XAVC</a></td><td><i>Not applicable</i></td></tr>
  <tr><td>Audio-only input</td><td><i>Not applicable</i></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-flac">FLAC</a><br /><a href="#codec-gsm">GSM</a><br /><a href="#codec-pcm">PCM</a></td></tr>
  <tr><td>Audio-only output</td><td><i>Not applicable</i></td><td><a href="#codec-aac">AAC</a><br /><a href="#codec-aiff">AIFF</a><br /><a href="#codec-ac3">Dolby Digital (AC3)</a><br /><a href="#codec-eac3">Dolby Digital Plus (EAC3)</a><br /><a href="#codec-flac">FLAC</a><br /><a href="#codec-mpeg2">MPEG-2</a><br /><a href="#container-mp3">MP3</a><br /><a href="#codec-pcm">PCM</a></td></tr>
</tbody>
</table>


## Supported codecs
<a name="codecs"></a>

This section contains reference tables for input and output codecs that MediaConvert supports. The tables show the codec, support on the input or output side, and container support for the codec. For more information about the container, or to see container support for other codecs, choose the container link.

**AAC (Advanced Audio Codec)**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">AAC</td><td>Input</td><td><a href="#container-3g2-3gp">3G2</a><br /><a href="#container-3g2-3gp">3GP</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-flash">MPEG-4 Flash</a><br /><a href="#container-matroska">Matroska</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-1">MPEG-1</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mxf">MXF</a></td></tr>
  <tr><td>Output</td><td><a href="#container-cmaf">CMAF DASH</a><br /><a href="#container-cmaf">CMAF HLS</a><br /><a href="#container-dash">DASH</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-flash">MPEG-4 Flash</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mss">MSS</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Audio-only input</td><td><a href="#container-mp4">MP4</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#container-dash">DASH</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-none">No container</a></td></tr>
</tbody>
</table>

For information about what output AAC profiles, coding modes, sample rates , and bitrates MediaConvert supports, see [AAC output reference tables](aac-support.md).

**AIFF**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">AIFF</td><td>Input</td><td><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mpeg-1">MPEG-1</a><br /><a href="#container-mxf">MXF</a></td></tr>
  <tr><td>Output</td><td><a href="#container-mov">MOV</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Audio-only input</td><td><i>Not supported</i></td></tr>
  <tr><td>Audio-only output</td><td><a href="#container-none">No container</a></td></tr>
</tbody>
</table>


**AMR-NB, AMR-WB**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">AMR-NB<br />AMR-WB</td><td>Input</td><td><a href="#container-3g2-3gp">3G2</a><br /><a href="#container-3g2-3gp">3GP</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**Apple ProRes**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th><th>Supported formats</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">Apple ProRes</td><td>Input</td><td><a href="#container-imf">IMF</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mxf">MXF</a></td><td rowspan="2">Apple ProRes 4444 XQ<br />Apple ProRes 4444<br />Apple ProRes 422 HQ<br />Apple ProRes 422<br />Apple ProRes LT<br />Apple ProRes Proxy</td></tr>
  <tr><td>Output</td><td><a href="#container-mov">MOV</a></td></tr>
</tbody>
</table>

For more information about Apple ProRes formats, see [https://support.apple.com/en-us/HT202410](https://support.apple.com/en-us/HT202410).  
You can also passthrough Apple ProRes inputs to MXF and MOV output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)  
To preserve 4:4:4 chroma subsampling in your Apple ProRes outputs:   
+ You cannot include any of the following Preprocessors: **Dolby Vision**, **HDR10\+**, or **Noise reducer**.
+ You must use the Duplicate Drop as the frame rate conversion algorithm (when using frame rate conversion).
+ You cannot mix RGB and non RGB inputs. 
+ You cannot mix 4:4:4 inputs with other non-4:4:4 inputs. 
+ You can only use the NexGuard File Maker preprocessor.

**AV1**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">AV1</td><td>Input</td><td><a href="#container-mp4">MP4</a></td></tr>
  <tr><td>Output</td><td><a href="#container-cmaf">CMAF DASH</a><br /><a href="#container-cmaf">CMAF HLS</a><br /><a href="#container-dash">DASH</a><br /><a href="#container-mp4">MP4</a></td></tr>
</tbody>
</table>

For HLS output codec recommendations from Apple, see [https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices).

**AVC (H.264)**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">AVC (H.264)</td><td>Input</td><td><a href="#container-3g2-3gp">3G2</a><br /><a href="#container-3g2-3gp">3GP</a><br /><a href="#container-flash">MPEG-4 Flash</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-matroska">Matroska</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Output</td><td><a href="#container-cmaf">CMAF DASH</a><br /><a href="#container-cmaf">CMAF HLS</a><br /><a href="#container-dash">DASH</a><br /><a href="#container-flash">F4V</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mss">MSS</a><br /><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td></tr>
</tbody>
</table>

You can also passthrough AVC inputs to most output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**AVC-Intra**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th><th>Supported formats</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">AVC-Intra</td><td>Input</td><td><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mxf">MXF</a></td><td>AVC-Intra 50<br />AVC-Intra 100<br />AVC-Intra 200<br />AVC-Intra 2K4:2:2<br />AVC-Intra 4K4:2:2</td></tr>
  <tr><td>Output</td><td><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td><td>AVC-Intra 50<br />AVC-Intra 100<br />AVC-Intra 200<br />AVC-Intra 2K4:2:2<br />AVC-Intra 4K4:2:2</td></tr>
</tbody>
</table>

MediaConvert only supports YUV AVC-Intra inputs, it does not support RGB AVC-Intra inputs.  
You can also passthrough AVC-Intra inputs to MXF and MOV output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**Canopus HQ**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">Canopus HQ</td><td>Input</td><td><a href="#container-avi">AVI</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**Dolby Digital (AC3)**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">Dolby Digital (AC3)</td><td>Input</td><td><a href="#container-avi">AVI</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-matroska">Matroska</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-1">MPEG-1</a><br /><a href="#container-mpeg-ts">MPEG-TS</a></td></tr>
  <tr><td>Output</td><td><a href="#container-cmaf">CMAF DASH</a><br /><a href="#container-cmaf">CMAF HLS</a><br /><a href="#container-dash">DASH</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mss">MSS</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Audio-only input</td><td><a href="#container-none">No container</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#container-dash">DASH</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-none">No container</a></td></tr>
</tbody>
</table>


**Dolby Digital Plus (EAC3)**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">Dolby Digital Plus (EAC3)</td><td>Input</td><td><a href="#container-avi">AVI</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-matroska">Matroska</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-1">MPEG-1</a><br /><a href="#container-mpeg-ts">MPEG-TS</a></td></tr>
  <tr><td>Output</td><td><a href="#container-cmaf">CMAF DASH</a><br /><a href="#container-cmaf">CMAF HLS</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mss">MSS</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Audio-only input</td><td><a href="#container-none">No container</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#container-dash">DASH</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-none">No container</a></td></tr>
</tbody>
</table>


**Dolby Digital Plus JOC (Atmos)**  
For more information, see [Dolby Atmos](dolby-atmos.md). 

**Dolby E**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">Dolby E</td><td>Input</td><td><a href="#container-avi">AVI</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**DV/DVCPRO**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">DV/DVCPRO</td><td>Input</td><td><a href="#container-avi">AVI</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>

You can also passthrough DV/DVCPRO inputs to MXF and MOV output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**DV25, DV50**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">DV25DV50</td><td>Input</td><td><a href="#container-mxf">MXF</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**DVCPro HD**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">DVCPro HD</td><td>Input</td><td><a href="#container-mxf">MXF</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**DivX/Xvid**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">DivX/Xvid</td><td>Input</td><td><a href="#container-avi">AVI</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**FLAC**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">FLAC</td><td>Input</td><td><a href="#container-matroska">Matroska</a><br /><a href="#container-mp4">MP4</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
  <tr><td>Audio-only input</td><td><a href="#container-matroska">Matroska</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-ogg">OGA</a><br /><a href="#container-ogg">OGG</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#container-ogg">OGG</a><br /><a href="#container-none">No container</a></td></tr>
</tbody>
</table>


**GSM**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">GSM</td><td>Input</td><td><a href="#container-wav">WAV</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
  <tr><td>Audio-only input</td><td><a href="#container-wav">WAV</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Audio-only output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**GIF**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">GIF</td><td>Input</td><td><a href="#container-gif">GIF</a></td></tr>
  <tr><td>Output</td><td><a href="#container-none">No container</a></td></tr>
</tbody>
</table>


**H.261**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">H.261</td><td>Input</td><td><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**H.262**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">H.262</td><td>Input</td><td><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**H.263**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">H.263</td><td>Input</td><td><a href="#container-3g2-3gp">3G2</a><br /><a href="#container-3g2-3gp">3GP</a><br /><a href="#container-flash">MPEG-4 Flash</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**HEVC (H.265)**  <a name="codec-hevc"></a>


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">HEVC (H.265)</td><td>Input</td><td><a href="#container-hls">HLS</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Output</td><td><a href="#container-cmaf">CMAF HLS</a><br /><a href="#container-cmaf">CMAF DASH</a><br /><a href="#container-dash">DASH</a><br /><a href="#container-hls">HLS</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-none">No container</a></td></tr>
</tbody>
</table>

When outputting HEVC in an HLS container, we recommend using a CMAF output group for the widest player compatibility. For more details, see [https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices).
You can also passthrough HEVC inputs to supported output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**JPEG 2000 (J2K)**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">JPEG 2000 (J2K)</td><td>Input</td><td> <a href="#container-imf">IMF</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mxf">MXF</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>

You can also passthrough J2K inputs to MXF and MOV output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**MJPEG (Motion JPEG)**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">MJPEG</td><td>Input</td><td><a href="#container-avi">AVI</a><br /><a href="#container-mov">MOV</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**MP3 (MPEG-1 Layer 3)**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">MP3</td><td>Input</td><td><a href="#container-avi">AVI</a><br /><a href="#container-mov">MOV</a></td></tr>
  <tr><td>Output</td><td><a href="#container-mov">MOV</a></td></tr>
  <tr><td>Audio-only input</td><td><a href="#container-mp3">MP3</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#container-none">No container</a></td></tr>
</tbody>
</table>


**MPEG-1**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">MPEG-1</td><td>Input</td><td><a href="#container-mpeg-1">MPEG-1</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**MPEG-2 (MPEG-1 Layer II )**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">MPEG-2 Video</td><td>Input</td><td><a href="#container-hls">HLS</a><br /><a href="#container-matroska">Matroska</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-1">MPEG-1</a><br /><a href="#container-mpeg-ps">MPEG-PS</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Output</td><td><a href="#container-mov">MOV</a><br /><a href="#container-flash">MPEG-4 Flash</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td></tr>
</tbody>
</table>



<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">MPEG-2 Audio</td><td>Audio-only input</td><td><a href="#container-mpeg-ts">MPEG-TS</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-none">No container</a></td></tr>
</tbody>
</table>


**MPEG-4 Part 2**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">MPEG-4 Part 2</td><td>Input</td><td><a href="#container-3g2-3gp">3G2</a><br /><a href="#container-3g2-3gp">3GP</a><br /><a href="#container-matroska">Matroska</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**MPEG Audio**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">MPEG Audio</td><td>Input</td><td><a href="#container-avi">AVI</a><br /><a href="#container-mpeg-1">MPEG-1</a><br /><a href="#container-mpeg-ps">MPEG-PS</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mxf">MXF</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**Opus, Vorbis**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">Opus<br />Vorbis</td><td>Input</td><td><a href="#container-matroska">Matroska</a><br /><a href="#container-ogg">OGA</a><br /><a href="#container-ogg">OGG</a><br /><a href="#container-webm">WebM</a></td></tr>
  <tr><td>Output</td><td><a href="#container-webm">WebM</a></td></tr>
  <tr><td>Audio-only input</td><td><a href="#container-matroska">Matroska</a><br /><a href="#container-ogg">OGA</a><br /><a href="#container-ogg">OGG</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#container-ogg">OGG</a></td></tr>
</tbody>
</table>


**Panasonic P2**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">Panasonic P2</td><td>Input</td><td><a href="#container-mxf">MXF</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**PCM**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">PCM</td><td>Input</td><td><a href="#container-avi">AVI</a><br /><a href="#container-imf">IMF</a><br /><a href="#container-matroska">Matroska</a><br /><a href="#container-mov">MOV</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-1">MPEG-1</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Output</td><td><a href="#container-mov">MOV</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td></tr>
  <tr><td>Audio-only input</td><td><a href="#container-mov">MOV</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-wav">WAV</a></td></tr>
  <tr><td>Audio-only output</td><td><a href="#container-wav">WAV</a><br /><a href="#container-none">No container</a></td></tr>
</tbody>
</table>


**Quicktime RLE (Quicktime Animation)**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">Quicktime RLE</td><td>Input</td><td><a href="#container-mov">MOV</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**Sony XDCAM**  


<table>
<thead>
  <tr><th>Video format</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">Sony XDCAM</td><td>Input</td><td><a href="#container-mxf">MXF</a></td></tr>
  <tr><td>Output</td><td><a href="#container-mxf">MXF</a></td></tr>
</tbody>
</table>


**Sony XDCAM MPEG-4 Proxy**  


<table>
<thead>
  <tr><th>Video format</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">Sony XDCAM</td><td>Input</td><td><a href="#container-mxf">MXF</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**VC-1**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">VC-1</td><td>Input</td><td><a href="#container-asf-wmv-wma">ASF</a><br /><a href="#container-matroska">Matroska</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-asf-wmv-wma">WMV</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**VC-3**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">VC-3</td><td>Input</td><td><a href="#container-mxf">MXF</a></td></tr>
  <tr><td>Output</td><td><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td></tr>
</tbody>
</table>

You can also passthrough VC-3 inputs to MXF and MOV output containers. For more information, see: [Video passthrough codec support and job settings requirements](video-passthrough-feature-restrictions.md)

**VP8**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">VP8</td><td>Input</td><td><a href="#container-webm">WebM</a></td></tr>
  <tr><td>Output</td><td><a href="#container-dash">DASH</a><br /><a href="#container-webm">WebM</a></td></tr>
</tbody>
</table>


**VP9**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">VP9</td><td>Input</td><td><a href="#container-mp4">MP4</a><br /><a href="#container-webm">WebM</a></td></tr>
  <tr><td>Output</td><td><a href="#container-cmaf">CMAF DASH</a><br /><a href="#container-cmaf">CMAF HLS</a><br /><a href="#container-dash">DASH</a><br /><a href="#container-webm">WebM</a></td></tr>
</tbody>
</table>


**WMA, WMA2**  


<table>
<thead>
  <tr><th>Audio codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">WMA<br />WMA2</td><td>Input</td><td><a href="#container-asf-wmv-wma">ASF</a><br /><a href="#container-matroska">Matroska</a><br /><a href="#container-mp4">MP4</a><br /><a href="#container-mpeg-ts">MPEG-TS</a><br /><a href="#container-asf-wmv-wma">WMV</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
  <tr><td>Audio-only input</td><td><a href="#container-asf-wmv-wma">ASF</a><br /><a href="#container-asf-wmv-wma">WMA</a><br /><a href="#container-asf-wmv-wma">WMV</a></td></tr>
  <tr><td>Audio-only output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**WMA Pro**  


<table>
<thead>
  <tr><th>Video codec</th><th>Input / Output</th><th>Supported container</th></tr>
</thead>
<tbody>
  <tr><td rowspan="4">WMA Pro</td><td>Input</td><td><a href="#container-asf-wmv-wma">ASF</a><br /><a href="#container-asf-wmv-wma">WMV</a></td></tr>
  <tr><td>Output</td><td><i>Not supported</i></td></tr>
  <tr><td>Audio-only input</td><td><a href="#container-asf-wmv-wma">ASF</a><br /><a href="#container-asf-wmv-wma">WMA</a><br /><a href="#container-asf-wmv-wma">WMV</a></td></tr>
  <tr><td>Audio-only output</td><td><i>Not supported</i></td></tr>
</tbody>
</table>


**XAVC**  


<table>
<thead>
  <tr><th>Format</th><th>Input / Output</th><th>Supported container</th><th>Supported XAVC profiles</th></tr>
</thead>
<tbody>
  <tr><td>XAVC</td><td>Output</td><td><a href="#container-mxf">MXF</a><br /><a href="#container-none">No container</a></td><td>XAVC HD<br />XAVC HD Intra CBG<br />XAVC 4K<br />XAVC 4K Intra CBG<br />XAVC 4K Intra VBR</td></tr>
</tbody>
</table>

For more information about the XAVC format, see: [https://pro.sony/ue\_US/technology/xavc](https://pro.sony/ue_US/technology/xavc).  
XAVC inputs are supported, as they are a subset of [MXF](#container-mxf) containers with [AVC (H.264)](#codec-avc) video codecs.

****  