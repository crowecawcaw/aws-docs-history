# Converting one HDR color space to another

You can convert video between the HDR10 color space and the HLG color
space, in either direction. In this case, Elemental Live makes the following
changes:

- It changes the pixel values, if necessary, to fit the colors into the
  different color space.
- It changes the color space metadata to identify the new color space.
- It applies the new brightness function to the video.
- If converting to HDR10, it calculates display metadata for the video.
  After the conversion, the video complies completely with the new color
  space. The color will be slightly different, but probably not more or less
  rich. The color will match the new brightness function.
