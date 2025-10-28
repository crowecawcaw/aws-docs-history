# Converting a mixed color space to one color space

The video in your input or inputs might contain a mix of color spaces.
You can still set up to convert these color spaces to one color space.

In this case, Elemental Live makes the following changes to the pixel
values:

- For color spaces where it supports conversion, Elemental Live changes
  the pixel values to values that are appropriate to the new color space.
  See [the sections](color-space-conversion-results.md "color-space-conversion-results.md")
  that describe the other conversions.
- It doesn't change the pixel values for video in unsupported color
  spaces, or video that has no color space metadata. See [Handling of unsupported
  color spaces](color-space-conversions.md#color-space-unsupported-handling "color-space-conversions.md#color-space-unsupported-handling") for more information.
- It doesn't change the pixel values for Dolby Vision 8.1 video because
  Elemental Live doesn't read the color space metadata for Dolby Vision. On
  the input side, Elemental Live treats Dolby Vision 8.1 as an unknown color
  space.
- Keep in mind that Elemental Live [can't ingest Dolby Vision 5.0](color-space-conversions.md#color-space-dv5-handling "color-space-conversions.md#color-space-dv5-handling"),
  so the handling is irrelevant.
  Elemental Live makes the following changes to the metadata:

- If it converts the color space, it changes the color space metadata
  to identify the new color space. It applies the new brightness function to
  the video.
- If it leaves the color space unchanged, it also leaves the metadata
  unchanged.
