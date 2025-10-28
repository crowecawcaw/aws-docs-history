# Converting HDR10 to Dolby Vision 5.0 or 8.1

You can convert video in the HDR10 color space to Dolby Vision 5.0 or
8.1.

If you convert the video to Dolby Vision 5.0, video players that are
Dolby Vision-compliant will be able to play it. If you convert the video to
Dolby Vision 8.1, video players that are Dolby Vision-compliant and video
players that are HDR10-compliant will be able to play it.

When you convert a suitable video to Dolby Vision, Elemental Live makes
the following changes:

- It doesn't change the pixel values, because HDR10 and Dolby Vision
  both use the same color space.
- It changes the color space metadata to identify the new color space.
- It applies the new brightness function to the video.
- It calculates the Dolby Vision display metadata for the video.
  After the conversion, the video fits in the new color spaces, but the
  color is not any richer than before the conversion, because the color space
  hasn't changed. However, the bright parts of the video are brighter, and the
  dark parts are darker.
