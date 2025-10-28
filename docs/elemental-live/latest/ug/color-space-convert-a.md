# Converting an SDR color space to HDR

You can convert an SDR color space to HDR10 or HLG color space. In this
case, Elemental Live makes the following changes:

- It changes the pixel values, if necessary, to fit the colors into the
  different color space.
- It changes the color space metadata to identify the new color space.
- It applies the new brightness function to the video.
- If converting to HDR10, it calculates display metadata for the video.
  After the conversion, the video fits in the new color spaces, but the
  color is not any richer than before the conversion. However, the bright
  parts of the video are brighter, and the dark parts are darker.
