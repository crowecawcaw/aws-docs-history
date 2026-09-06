

# Handling a straightforward color space conversion
<a name="color-space-simplified"></a>

You can control how MediaLive takes the color space and color space metadata in a video source and manipulates it in the video output. You can set up each output video encode to convert or pass through the color space, and to include or omit the color space metadata.

All video belongs to a specific color space. The color space defines the range of color for the video. Video can include color space metadata that provides information about the color space. When metadata is missing, the video still has a color space, but it is impossible for MediaLive to manipulate the color space.

**Default behavior**

The default behavior is to pass through the color space and pass through the color space metadata.

**Topics**
+ [Determine if this section applies to your channel](#color-space-simplified-which-section)
+ [Color space versus video resolution](color-space-vs-resolution.md)
+ [General information about color space](about-color-metadata-simplified.md)
+ [Passing through the color space](color-space-simplified-options-passthrough.md)
+ [Converting the color space](color-space-simplified-options-convert.md)
+ [Configuring the inputs](color-space-simplified-setup-input.md)
+ [Configuring color space handling in each output](color-space-simplified-output-handling.md)
+ [Results for different color space handling](colorspace-simplified-output-results.md)
+ [Reference: Location of fields](colorspace-simplified-fields.md)

## Determine if this section applies to your channel
<a name="color-space-simplified-which-section"></a>

In this guide there are two sections about handling color space — this *straightforward handling* section, and [Handling complex color space conversions](color-space.md). 

The current section provides procedures you can follow if the input color spaces and color space metadata are all *clean*. The procedures in this section are shorter than those in the other section. 

To determine if your content meets the requirements for these procedures, read the following table. Each row in the table describes a different scenario that this *straightforward handling* section covers. Find the scenario that applies to your content. If none of these scenarios applies to you, then you must you must read [Handling complex color space conversions](color-space.md).



- **You are passing through the color space in every output.**
  - **Characteristics of color space:** The color space can be any color space. It doesn't have to be a color space that MediaLive can to convert from or can convert to. 
  - **Characteristics of metadata in input:** The color space metadata must either be correct, or you must be prepared to remove it from the output.

- **You are converting the color space in at least one output. You might be passing through the color space in other outputs. **
  - **Characteristics of color space:** If converting, the color space or color spaces must be one of the color spaces that MediaLive [can convert](color-space-simplified-supported-conversions.md). The color space can change within one source, but it must meet the requirement. / **Characteristics of metadata in input:** The color space metadata must be present and must match the color space.
  - **Characteristics of color space:** If passing through, the source color space can be any color space. It doesn't have to be a color space that MediaLive can convert from or can convert to.  / **Characteristics of metadata in input:** The color space metadata must either be correct, or you must be prepared to remove it from the output.

- **You are converting the color space in at least one output, and you are using 3D LUTs files.**
  - **Characteristics of color space:** If converting, the color space or color spaces must be one of the color spaces that MediaLive [can convert](color-space-simplified-supported-conversions.md). The color space can change within one source, but it must meet the requirement.  / **Characteristics of metadata in input:** The color space metadata must be present and must match the color space.We assume that if you are using 3D LUTs files, the content is well formed. Use of 3D LUTs files is documented only in this section. (It isn't documented in [Handling complex color space conversions](color-space.md).)
  - **Characteristics of color space:** If passing through, the color space can be any color space. It doesn't have to be a color space that MediaLive can convert from or can convert to.  / **Characteristics of metadata in input:** The color space metadata must either be correct, or you must be prepared to remove it from the output.

