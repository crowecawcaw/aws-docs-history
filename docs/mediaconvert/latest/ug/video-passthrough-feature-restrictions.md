# Video passthrough codec

support and job settings requirements

The following table shows which combinations of input video codec and output
container support video passthrough.

| Supported input video codec                                                                      | Supported output container                  |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| AVC (H.264)<br>HEVC (H.265)                                                                      | CMAF DASH (Common Media Application Format) |
| AVC (H.264)<br>HEVC (H.265)                                                                      | CMAF HLS (Common Media Application Format)  |
| AVC (H.264)<br>HEVC (H.265)                                                                      | DASH (Dynamic Adaptive Streaming over HTTP) |
| _No supported input video<br>codecs_                                                             | F4V (MPEG-4 Flash)                          |
| AVC (H.264)<br>HEVC (H.265)                                                                      | HLS (Apple HTTP Live Streaming)             |
| Apple ProRes<br>AVC (H.264)<br>AVC-Intra<br>DV/DVCPRO<br>HEVC (H.265)<br>JPEG 2000 (J2K)<br>VC-3 | MOV (Apple QuickTime)                       |
| AVC (H.264)<br>HEVC (H.265)                                                                      | MP4 (MPEG-4)                                |
| AVC (H.264)<br>HEVC (H.265)                                                                      | MPEG-TS (MPEG-2 Transport Stream)           |
| _No supported input video<br>codecs_                                                             | MSS (Microsoft Smooth Streaming             |
| Apple ProRes<br>AVC-Intra<br>DV/DVCPRO<br>JPEG 2000 (J2K)<br>VC-3                                | MXF (Material Exchange Format)              |
| _No supported input video<br>codecs_                                                             | WebM                                        |
| _No supported input video<br>codecs_                                                             | Y4M                                         |
| AVC (H.264)                                                                                      | No container                                |

Additionally, jobs you create with video passthrough have the following
requirements.

**Inputs**

If you specify multiple inputs, each of your input's encoding
attributes must exactly match, including video codec, frame size,
profile, frame rate, and color space.

**Input clips**

(Optional) MediaConvert supports input clipping for I-frame only video codecs
when you use video passthrough. These include Apple
ProRes, AVC-Intra, DV/DVCPRO,
JPEG 2000 (J2K), and VC-3.

**Output container**

When you create MXF outputs from I-frame only inputs, MediaConvert supports
the following input frame rates: 23.976, 24, 25, 29.97, 50, 59.94,
60

**Frame rate**

You must keep the default setting, **Follow source**.
You cannot specify a different output frame rate than your input.

**Audio codec**

(Optional) MediaConvert supports audio encoding when you use video
passthrough.

**Dolby Digital passthrough**

(Optional) MediaConvert supports **Dolby
Digital passthrough** when you use video
passthrough.

If you specify multiple inputs, each of your input's Dolby
Digital streams must have identical encoding attributes.

**Captions**

(Optional) MediaConvert supports sidecar formats when you use video
passthrough.
