# Configuring color space handling in each

output

After you have set up each input in the event, you must configure the
outputs for the desired handling of color space. You can do the
following:

- Convert the color space in the content to a different color space in
  the output. See [Color space
  standards](color-space-standards.md "color-space-standards.md") for the supported
  conversions.
- Remove the color space metadata. Elemental Live doesn't touch the color
  space itself, it only removes the color space metadata.

You might choose to remove the color space metadata in situations such
as the following:

    + The pixel data and color space data in the input is incorrect, so
     that the downstream player can't use it to enhance the color.
    + The color space (and its metadata) changes frequently within the
     input, or between one input and another, and you know that there is a
     system downstream of AWS Elemental Live that can't handle changes in the metadata.

Keep in mind that removing metadata doesn't necessarily make the color
poorer. Removing it might only mean that the downstream player can't
implement enhancements to make the color even richer.

- Pass the color space metadata and the color space through to the
  output.
  You can set up each output with different color space handling. For
  example, you can create one output that passes through the original color
  space, and another that converts it.

###### Note

Elemental Live converts from one color space to another based on the
metadata in the content. Elemental Live doesn't examine the video to try to
determine whether it actually matches the color space identified in the
metadata. Therefore, to successfully convert, the metadata must be as
accurate as possible. To correct the metadata, see [Configuring the handling in the
input](hdr-input-handling.md "hdr-input-handling.md").

###### Topics

- [Passing through color space](colorspace-output-passthrough.md "colorspace-output-passthrough.md")
- [Converting color space: Procedure A](colorspace-output-procedure.md "colorspace-output-procedure.md")
- [Converting color space: Procedure B](colorspace-output-hdr10.md "colorspace-output-hdr10.md")
- [Removing color space metadata](colorspace-output-remove.md "colorspace-output-remove.md")
