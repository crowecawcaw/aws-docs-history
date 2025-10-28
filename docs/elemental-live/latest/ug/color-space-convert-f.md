# Converting one SDR color space to another

You can convert an SDR color space to another SDR color space. In this
case, Elemental Live makes the following changes:

- It changes pixels to values that represent the same color as the
  original values. The video now fits in the larger color space.
- It changes the color space metadata to identify the new color space.
- It applies the same brightness function to the video, because all the
  SDR color spaces use the same function.
  After the conversion, the video complies completely with the new color
  space.
