# Assess the color spaces in the sources

1. Speak to the content provider of each input. Obtain the following information:
   - The names of the color spaces that apply to the content.
   - Whether each input consists of only one color space or several color
     spaces.
   - Whether the color space metadata is accurate. (You will use this information in
     the [next section](color-space-input-procedure.md "color-space-input-procedure.md").)

2. Read the following information to determine if there are reasons not to pass through
   or not to convert the color space.

###### Topics

- [Unknown color space](#color-space-unknown "#color-space-unknown")
- [Restrictions on passthrough](#color-space-restrictions-passthrough "#color-space-restrictions-passthrough")
- [Restrictions on conversion](#color-space-restrictions-conversion "#color-space-restrictions-conversion")

## Unknown color space

If the content provider can't tell you what color space applies to the input, you
shouldn't try to convert the color space. Doing so might degrade the video quality.

You might be able to pass through the color space. In this case, you should remove the
color space metadata, so that the downstream system doesn't read information that might be
inaccurate.

## Restrictions on passthrough

**Passthrough of supported color spaces**

MediaLive can pass through color spaces that it supports.

**Passthrough of unsupported color spaces**

MediaLive might be able to pass through color spaces that it doesn't support. Any of the
following might apply:

- MediaLive might be able to ingest the input, and to pass through the color space
  and the color space metadata.
- Or it might ingest the input but produce unacceptable output.
- Or it might fail to ingest the input, so that the event follows the input loss
  behavior routine (for example, it might display a slate in the output).

**Passthrough and the output codec**

Even if MediaLive supports the color space that you want to pass through, there might be a
restriction because of the output codec.

If you want to pass through the color space in even one output, then every input in the
channel must be in color spaces that are supported by the codec for the output. For
information about codecs, see [Supported output codecs](color-space-input-output-requirements.md#color-space-supported-output-codecs "color-space-input-output-requirements.md#color-space-supported-output-codecs").

For example, you have an output where you want to pass through the color space. You want
to encode that output with H.264. Assume that one of the channel inputs includes content in
Dolby Vision 8.1. However, the Dolby Vision color space (from the input) can't be included in
H.264. MediaLive will accept the configuration, but the portions of the output in the unsupported
color space will be degraded.

The workaround is to choose an output codec that is supported by all the color spaces in
all the inputs.

Note how the rule for passthrough in a channel is based on the color space for all the
inputs.

## Restrictions on conversion

Even if MediaLive supports conversion to a specific color space, there might be a
restriction because of the output codec.

If you want to convert to a specific color space in an output, then the codec you set in
that output must support that color space.

For example, you have an output where you want to encode with H.264, and you want to
convert all the source color spaces to HDR10. However, HDR10 can't be included in H.264.
MediaLive won't let you configure in this way. When you choose H.264, the option for HDR10 is
removed from the field where you specified the output color space.

The workaround is to choose an output codec (H.265) that is supported with the color
space conversion.

Note how the rule for conversion in a channel is based on the color space and codec for
the individual output.
