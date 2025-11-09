This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Encoding – Quantization Controls

## Description

- **Adaptive Quantization** (**AQ**):
  Allows the encoder to vary compression within a frame to improve subjective visual quality.
  It can distribute bits to provide more data to areas of a frame that are more complex for the
  encoding process. It can also reduce "smear" in high motion and sports content.

Note that although it may seem counter-intuitive, areas of solid color are considered
more complex as human perception is more likely to notice small variations in smooth surfaces
or gradients as opposed to more varied areas. For this reason, with **Adaptive Quantization**, more bits are allocated to smooth surfaces to minimize
the perceptual variation between frames.

- **Framing Quantization**: An extension of **Adaptive Quantization** that compresses the edges of the video slightly
  more than the center. The effect shifts bits, and thus quality, from the boundary of the
  image to the middle of the image, where the action and viewers' attention is typically
  focused. This field appears only when the output codec is MPEG-2.
- **Softness**: Adjusts the quantization matrices used in the
  encoder, which determine the relative compression of high vs. low spatial frequency
  components of the video. Higher softness settings compress high frequencies more, reducing
  bitrate at the cost of image sharpness. This field appears only when the output codec is
  H.264 or MPEG-2.

## Recommendations

- **Adaptive Quantization**: For high bitrate outputs, we
  recommendthat you always set **Adaptive Quantization** to
  "low." For moderate bitrate outputs, our recommendation is "medium." For low bitrate outputs,
  our recommendation is "high" to "medium" or "high" for h.264 content. We generally recommend
  "high " , but, particular for low bitrate use cases, this setting can result in some use
  cases having too many bits be distributed to complex areas of the picture, resulting in more
  noticeable, lower quality in less complex areas. In those cases, "medium " may be more
  appropriate.
- **Framing Quantization**: For low bitrate encodes, we
  recommend using **Framing Quantization** (e.g. MPEG-2 1080i at
  10 Mbps) and set based on subjective tuning at values between 1.0 and 2.0. . (Note: The
  visual effect of framing quantization is intentionally subtle.)
- **Softness** For low bitrate encodes softness can be used
  (e.g. MPEG-2 1080i at 10 Mbps) and set based on subjective tuning at values between 24 and

32.

## Location of Fields

| Location of Field on Web Interface                    | Location of Tag in XML                                                                                                                                                                        |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Streams – Video > Advanced > Adaptive<br>Quantization | stream_assembly/video_description/`codec`/adaptive_quantization<br>where `codec` is one of the following:<br>• `h264_settings`<br>• `vc1_settings`<br>• `mpeg2_settings`<br>• `h265_settings` |
| Streams – Video > Advanced > Framing<br>Quantization  | stream_assembly/video_description/`codec`/framing_quantization<br>where `codec` is:<br>`meg2_settings`                                                                                        |
| Streams – Video > Advanced > Softness                 | stream_assembly/video_description/`codec`/softness<br>where `codec` is one of the following:<br>• `h264_settings`<br>• `mpeg2_settings`                                                       |
