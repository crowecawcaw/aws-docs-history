# Color space conversion

If you want your output video to use a different color space than your input video,
use color space conversion. Set up color space conversion in the output **Color
corrector** settings.

MediaConvert supports the following input color spaces: Rec. 601, Rec. 709, HDR10, HLG 2020, P3DCI, and P3D65.

## Supported color space

conversions

Your input color space is set by your input video or by the values that you set
for **Color space** and **Color space usage** in
your input settings. For more information about the input color space settings, see
[Replacing inaccurate or
missing HDR metadata](replacing-inaccurate-or-missing-hdr-metadata.md "replacing-inaccurate-or-missing-hdr-metadata.md").

For information about how to convert the color space, see [Color space conversion](converting-the-color-space.md "converting-the-color-space.md").

MediaConvert supports the following color space conversions:

- From any supported HDR format to any other supported HDR format
- From any supported SDR color space to any other supported SDR color
  space
- From any supported SDR color space to any supported HDR format

###### Note

Converting from SDR to HDR doesn't upgrade the dynamic range of the
video content itself. Therefore, the output is formatted as HDR but
looks the same as it would if you created it as an SDR output.

- From any supported HDR format to any supported SDR color space

###### Note

When professional color graders convert an asset from HDR to SDR, they
make artistic decisions about where to map colors from the larger space
that don't exist in the smaller space. There is no standard formula to
map these values automatically. The tone mapping technology that
MediaConvert uses to do automatic conversion from HDR to SDR
approximates the outcome of manually regrading from HDR to SDR. This
automatic conversion works well with most content, but we recommend that
you review your outputs to confirm the tone mapping results.
