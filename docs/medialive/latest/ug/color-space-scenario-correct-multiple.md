# Scenario D – Metadata can't be

corrected

During assessment of the MediaLive input, you might have determined the following:

- Different portions of the content are in different color spaces. All those color
  spaces are supported.

- The metadata is inaccurate for more than one color space. (Compare this to
  scenario C, where the metadata is inaccurate only for one color space.)
  Or you might have determined the following:

- The content provider can't provide accurate information about the color space or
  its metadata.
  You have this option for handling the metadata in the output:

**Remove the metadata**

There is no way to clean up this content because MediaLive can correct the metadata for
only one color space. In this scenario, the metadata is inaccurate in different types of
color space.

You can't force the color space metadata. For example, you can't force it to Rec. 601,
because sometimes will correctly identify the accompanying color space, but sometimes it
won't. Inaccurate metadata will result in an inaccurate conversion (if you convert the
color space in the output), or in an inferior viewing experience (if you pass through the
color space in the output).

Follow the procedure in [Set up inputs to correct metadata](color-space-input-setup.md "color-space-input-setup.md"), and set the key
fields as follows:

- **Color space** field – Set to **FOLLOW**
- **Color space usage** field – MediaLive ignores this field.
  During processing, MediaLive won't read the metadata.

You won't be able to convert the color space in any outputs, even for other inputs
that have correct color space metadata.
