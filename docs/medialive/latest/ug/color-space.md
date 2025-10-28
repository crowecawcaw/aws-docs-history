# Handling complex color space conversions

###### Important

Read [Which section to read](#color-space-which-section "#color-space-which-section") to determine if you should read this
section.

You can control how MediaLive takes the color space and color space metadata in a video
source and manipulates it in the video output. You can set up each output video encode
to convert or pass through the color space, and to include or omit the color space metadata.

All video belongs to a specific color space. The color space defines the range of color for
the video. Video can include color space metadata. This metadata provides information about the
color space. When the color space metadata is missing, the video still has a color space, but it
is impossible for a video processor such as MediaLive to manipulate the color space.

You can control how MediaLive takes the color space and color space metadata in a video
source and manipulates it in the video output. You can set up each output video encode to
convert or pass through the color space, and to include or omit the color space metadata.

**Default behavior**

The default behavior is to pass through the color space and pass through the color space
metadata.

###### Topics

- [Which section to read](#color-space-which-section "#color-space-which-section")
- [Options for handling color space](color-space-handling-options.md "color-space-handling-options.md")
- [General information about color space](about-color-metadata.md "about-color-metadata.md")
- [General procedure for handling color
  space](color-space-general-procedure.md "color-space-general-procedure.md")
- [Assess the color spaces in the sources](color-space-assess-inputs.md "color-space-assess-inputs.md")
- [Handling color space metadata in the
  inputs](color-space-input-handling.md "color-space-input-handling.md")
- [Configuring color space handling in each
  output](color-space-output-handling.md "color-space-output-handling.md")
- [Results for different color space
  handling](colorspace-output-results.md "colorspace-output-results.md")
- [Reference: Location of fields](colorspace-fields.md "colorspace-fields.md")

## Which section to read

There are two sections in this guide about handling color space in MediaLive — this section, and the
section [Handling a straightforward color space
conversion](color-space-simplified.md "color-space-simplified.md").

Read the requirements in [Determine if this section applies to
your channel](color-space-simplified.md#color-space-simplified-which-section "color-space-simplified.md#color-space-simplified-which-section") in [Handling a straightforward color space
conversion](color-space-simplified.md "color-space-simplified.md"). If your content doesn't meet all those requirements,
then follow the procedures in this section instead.

This section provides procedures for dealing with complicated situations that include the
following:

- Assessing the accuracy of the color space metadata in content.
- Cleaning up the metadata in content.

- Content that is one input, where the color space switches within the input.
- Converting content that is a combination of supported and unsupported color
  spaces.

These requirements often apply to content that is a VOD file that you are converting to a
live stream. The VOD file might have been created by stitching together several different
sources, each with a different color space. It might contain older content with an unknown
color space and/or with missing or inaccurate metadata.
