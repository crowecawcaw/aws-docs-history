# Working with color space

You can control how Elemental Live handles the color space in a video
source. You can set up an event to perform one of these actions on the color
space:

- You can set up to _pass through_ the
  color space. Elemental Live doesn't touch the color space or the color space
  metadata.

In this case, you might need to adjust the color space metadata in the
input. For example, you might want to do this if you know that the color
space metadata is incorrect or missing.

- You can set up to _remove_ the color
  space metadata, because you aren't interested in including it in the
  outputs. Elemental Live doesn't touch the color space but it removes the
  metadata.
- You can set up to _convert_ the color
  space itself—to change the pixels in the video.Elemental Live changes both
  the color space and the color space metadata.
  You can set up each output in the event for different handling. For
  example, you can set up one output to remove the color space metadata, one to
  convert it to a different color space, and another to convert it to a second
  different color space.

By default, Elemental Live doesn't convert the color space (in the output)
or change the color space metadata (in the input). It passes through the
source color space and metadata to the output.

###### Topics

- [Color space versus video
  resolution](color-space-vs-resolution.md "color-space-vs-resolution.md")
- [General information about color
  space](about-color-metadata.md "about-color-metadata.md")
- [Configuring the handling in the
  input](hdr-input-handling.md "hdr-input-handling.md")
- [Configuring color space handling in each
  output](hdr-output.md "hdr-output.md")
- [The results of different types of conversions](color-space-conversion-results.md "color-space-conversion-results.md")
- [Location of HDR
  fields on the web interface](hdr-location-of-fields-on-the-web-interface.md "hdr-location-of-fields-on-the-web-interface.md")
- [Location of HDR fields in
  the XML](hdr-location-of-fields-in-the-xml.md "hdr-location-of-fields-in-the-xml.md")
