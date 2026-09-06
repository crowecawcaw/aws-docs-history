

# Live supported codecs and input types
<a name="supported-inputs-live"></a>

The following sections describe supported input types, input codecs, and output codecs for live streaming content.

## Supported input types
<a name="supported-types-live"></a>

These are the input types that MediaPackage supports for live content.


| MediaPackage input type | Use case | 
| --- | --- | 
| HLS | Push an HLS stream from an external source or encoder (such as AWS Elemental MediaLive) using the HTTPS protocol.Additional requirements:+  Inputs must be over WebDAV and with digest authentication. <br />+  Media segments must not be encrypted. <br />+  Streams can contain either muxed video and audio tracks, or unmuxed tracks.  <br />+  The input must contain at least one video track. MediaPackage doesn't support inputs that contain no video track.  | 

## Supported input codecs
<a name="suported-inputs-codecs-live"></a>

These are the video, audio, and subtitles codecs that MediaPackage supports for source content streams.


| Media container | Video codecs | Audio codecs | Subtitles/captions format | 
| --- | --- | --- | --- | 
|  +  Video: TS <br />+  Audio: TS, AAC, AC3, or EC3   |  +  H.264 (AVC) <br />+  H.265 (HEVC) with HDR-10 support   |  +  AAC <br />+  Dolby Digital <br />+  Dolby Digital Plus   |  + WebVTT<br />+ CEA-608 and CEA-708 closed captions | 

## Supported output codecs
<a name="suported-outputs-codecs-live"></a>

These are the video, audio, and subtitles codecs that MediaPackage supports when delivering live content.


| Endpoint type | Manifest format | Media container | Video codecs | Audio codecs | Subtitles/captions format | 
| --- | --- | --- | --- | --- | --- | 
| Apple HLS | HLS |  +  Video: TS <br />+  Audio: TS or AAC   |  +  H.264 (AVC) <br />+  H.265 (HEVC) with HDR-10 support   |  +  AAC <br />+  Dolby Digital <br />+  Dolby Digital Plus   |  +  WebVTT <br />+  CEA-608 and CEA-708 closed captions   | 
| DASH-ISO | MPEG-DASH | MP4 |  +  H.264 (AVC) <br />+  H.265 (HEVC) with HDR-10 support   |  +  AAC <br />+  Dolby Digital <br />+  Dolby Digital Plus   |  +  EBU-TT <br />+  CEA-608 and CEA-708 closed captions   | 
| Microsoft Smooth | MSS | MP4 |  +  H.264 (AVC) <br />+  H.265 (HEVC) with HDR-10 support   |  +  AAC <br />+  Dolby Digital <br />+  Dolby Digital Plus   | DFXP | 
| CMAF | HLS | CMAF |  +  H.264 (AVC) <br />+  H.265 (HEVC) with HDR-10 support   |  +  AAC <br />+  Dolby Digital <br />+  Dolby Digital Plus   |  +  WebVTT <br />+  CEA-608 and CEA-708 closed captions   | 