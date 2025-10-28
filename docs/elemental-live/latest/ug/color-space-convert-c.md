# Converting an HDR color space to SDR

You can convert HDR10 or HLG video to an SDR color space. In this case,
Elemental Live makes the following changes:

- It changes the pixel values, if necessary, to fit the colors into the
  smaller color space.
- It changes the color space metadata to identify the new color space.
- It applies the new brightness function to the video.
- It removes any display metadata because the SDR color spaces don't
  include display metadata.
  After the conversion, the video complies completely with the new color
  space. The color will be less rich. The color will match the new brightness
  function.
