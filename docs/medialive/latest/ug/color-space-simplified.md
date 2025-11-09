# Handling a straightforward color space

conversion

You can control how MediaLive takes the color space and color space metadata in a video
source and manipulates it in the video output. You can set up each output video encode to
convert or pass through the color space, and to include or omit the color space metadata.

All video belongs to a specific color space. The color space defines the range of color for
the video. Video can include color space metadata that provides information about the color
space. When metadata is missing, the video still has a color space, but it is impossible for
MediaLive to manipulate the color space.

**Default behavior**

The default behavior is to pass through the color space and pass through the color space
metadata.

###### Topics

- [Determine if this section applies to
  your channel](#color-space-simplified-which-section "#color-space-simplified-which-section")
- [Color space versus video resolution](color-space-vs-resolution.md "color-space-vs-resolution.md")
- [General information about color
  space](about-color-metadata-simplified.md "about-color-metadata-simplified.md")
- [Passing through the color
  space](color-space-simplified-options-passthrough.md "color-space-simplified-options-passthrough.md")
- [Converting the color space](color-space-simplified-options-convert.md "color-space-simplified-options-convert.md")
- [Configuring the inputs](color-space-simplified-setup-input.md "color-space-simplified-setup-input.md")
- [Configuring color space handling in
  each output](color-space-simplified-output-handling.md "color-space-simplified-output-handling.md")
- [Results for different color space
  handling](colorspace-simplified-output-results.md "colorspace-simplified-output-results.md")
- [Reference: Location of fields](colorspace-simplified-fields.md "colorspace-simplified-fields.md")

## Determine if this section applies to

your channel

In this guide there are two sections about handling color space — this _straightforward handling_ section, and [Handling complex color space conversions](color-space.md "color-space.md").

The current section provides procedures you can follow if the input color spaces and color
space metadata are all _clean_. The procedures in this
section are shorter than those in the other section.

To determine if your content meets the requirements for these procedures, read the
following table. Each row in the table describes a different scenario that this _straightforward handling_ section covers. Find the scenario that
applies to your content. If none of these scenarios applies to you, then you must you must
read [Handling complex color space conversions](color-space.md "color-space.md").

| Type of handling in the channel                                                                                                                              | Characteristics of color space                                                                                                                                                                                                                                                                           | Characteristics of metadata in input                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| You are passing through the color space in every output.                                                                                                     | The color space can be any color space. It doesn't have to be a color space that<br>MediaLive can to convert from or can convert to.                                                                                                                                                                     | The color space metadata must either be correct, or you must be prepared to<br>remove it from the output.                                                                                                                                                                                                               |
| You are converting the color space in at least one output. You might<br>be passing through the color space in other outputs.                                 | If converting, the color space or color spaces must be one of the color spaces<br>that MediaLive [can<br>convert](color-space-simplified-supported-conversions.md "color-space-simplified-supported-conversions.md"). The color space can change within one source, but it must meet<br>the requirement. | The color space metadata must be present and must match the color space.                                                                                                                                                                                                                                                |
| If passing through, the source color space can be any color space. It doesn't<br>have to be a color space that MediaLive can convert from or can convert to. | The color space metadata must either be correct, or you must be prepared to<br>remove it from the output.                                                                                                                                                                                                |
| You are converting the color space in at least one output, and you<br>are using 3D LUTs files.                                                               | If converting, the color space or color spaces must be one of the color spaces<br>that MediaLive [can<br>convert](color-space-simplified-supported-conversions.md "color-space-simplified-supported-conversions.md"). The color space can change within one source, but it must meet<br>the requirement. | The color space metadata must be present and must match the color space.We<br>assume that if you are using 3D LUTs files, the content is well formed. Use of 3D<br>LUTs files is documented only in this section. (It isn't documented in [Handling complex color space conversions](color-space.md "color-space.md").) |
| If passing through, the color space can be any color space. It doesn't have to be<br>a color space that MediaLive can convert from or can convert to.        | The color space metadata must either be correct, or you must be prepared to<br>remove it from the output.                                                                                                                                                                                                |
