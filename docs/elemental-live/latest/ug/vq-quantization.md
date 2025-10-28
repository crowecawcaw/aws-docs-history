# Quantization controls

## Description

This guide shows how quantization can improve video quality.
Quantization is a lossy data compression technique. The encoder includes
several quantization controls.

- **Adaptive Quantization** (**AQ**):

AQ can reduce _smear_ in high-motion
and sports content. It can also improve the video quality on areas that
are smooth surfaces.

Recommendation: We recommend that you set this parameter to
**Auto**.

- **Spatial AQ**:

Spatial AQ can improve video quality in video blocks where distortion
would be noticeable. Spatial AQ allocates more bits to those high-risk
areas, such as smooth textured blocks. It allocates slightly fewer bits to
blocks where distortion won't cause noticeable visual degradation, such as
complex textured blocks.

Keep in mind that spatial AQ isn't content aware. The blocks that
will receive fewer bits might belong to an object that is drawing the
viewer's attention at that moment. Removing bits at that specific scene
might not be ideal.

This parameter applies only when **Adaptive
Quantization** is set to **Low** or
higher.

Recommendation: Choose a low spatial AQ for homogenous content, such
as gaming and cartoons. Choose high or higher spatial AQ for content with
a wider variety of textures.

- **Temporal AQ**:

It applies fewer bits to areas within the frame that are complex in
nature and that are affected by motion. For example, text tickers on
newscasts and scoreboards on sports matches. The text characters are
highly complex (sharp edges) and they scroll across the screen. Temporal
AQ attempts to improve the readability by detecting motion of such complex
entities, thus removing possible trailing artifacts.

This parameter applies appears only when **Adaptive Quantization** is set to **Low** or
higher.

Recommendation: Temporal AQ should almost always be enabled. But keep
in mind that temporal AQ might remove bits from some relevant areas of the
frame. For example, if enabling temporal AQ on sports matches would make
the athletes faces and movements less clear, it might be better to turn it
off. On the other hand, for newscasts, you should definitely enable
temporal AQ. The parameter helps improve video quality because it removes
bits from the news presenters, who are moving less and therefore present
less complexity. It adds bits to text tickers that present more
comlexity.

- **Flicker AQ**: This parameter reduces
  flicker in the video. The parameter might prevent the abrupt change in
  detail that gives the effect of a flicker in the video.

This parameter applies only to H.264 and H.265, and only when
**Adaptive Quantization** is set to
**Low** or higher.

Recommendation: We recommend that you enable this parameter only when
I-frame pulsing is noticeable. Otherwise, let the encoder run its
macroblock optimizations freely.

- **Framing AQ**: Compresses the edges of
  the video slightly more than the center. The effect assigns more bits to
  the middle of the image, where the action and the viewer's attention are
  typically focused. When more bits are assigned, the video quality
  increases.

This parameter appears only when the output codec is MPEG-2, and when
**Adaptive Quantization** is set to
**Low** or higher.

Recommendation: For low bitrate encodes (for example, MPEG-2 1080i at
10 Mbps), we recommend that you enable this parameter.
The visual effect of framing quantization is
intentionally subtle.

- **Softness**: A higher softness value
  compresses high spatial frequencies more, which reduces bitrate
  allocation at the cost of image sharpness.

This parameter appears only when the output codec is H.264 or MPEG-2.

Recommendation: For low bitrate encodes (for example, MPEG-2 1080i at
10 Mbps), try values **24** and **32**.
Then test whether the parameter makes any difference to your
content.

## Location of parameters

This table shows where the parameters mentioned in this section are
located. The first column shows the location on the web interface. The
second column shows the location in the event XML.

| Location of parameter on web interface                 | Location of tag in XML                                                                                                                                                    |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Streams – Video > Advanced > Adaptive Quantization** | stream_assembly/video_description/`codec`/adaptive_quantization where `codec` is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings` |
| **Streams – Video > Advanced > Spatial AQ**            | stream_assembly/video_description/`codec`/spatial_aq where `codec` is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings`            |
| **Streams – Video > Advanced > Temporal AQ**           | stream_assembly/video_description/`codec`/temporal_aq where `codec` is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings`           |
| **Streams – Video > Advanced > Flicker AQ**            | stream_assembly/video_description/`codec`/flicker_aq where `codec` is one of the following: <br>• `h264_settings` <br>• `h265_settings`                                   |
| **Streams – Video > Advanced > Framing AQ**            | stream_assembly/video_description/mpeg2_settings/framing_aq                                                                                                               |
| **Streams – Video > Advanced > Softness**              | stream_assembly/video_description/`codec`/softness where `codec` is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings`                                    |
