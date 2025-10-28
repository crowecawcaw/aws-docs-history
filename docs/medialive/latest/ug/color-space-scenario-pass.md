# Scenario A – Metadata is accurate

During assessment of the MediaLive input, you might have determined the following:

- The content is in one color space, the color space is supported, and the color
  space metadata is accurate.
- Or different portions of the content are in different color spaces, and the color
  space metadata is accurate for each portion.
  You have these options for handling the metadata in the output:

**Include the metadata**

Follow the procedure in [Set up inputs to correct metadata](color-space-input-setup.md "color-space-input-setup.md"), and set the key
fields as follows:

- **Color space** field – Set to **FOLLOW**
- **Color space usage** field – MediaLive ignores this field.
  During processing, MediaLive will read the metadata, in order to identify the color space.

**Remove the metadata**

You might have already decided to remove the color space metadata even though it is
accurate. For example, the color space might change frequently within the input, or
between one input and another. You know that there is a system downstream of MediaLive that
can't handle changes in the metadata.

You can still convert or pass through the color space. It is safe to convert the color
space because the metadata is reliable.

Follow the procedure in [Set up inputs to correct metadata](color-space-input-setup.md "color-space-input-setup.md"), and set the key
fields as follows:

- **Color space** field – Set to **FOLLOW**
- **Color space usage** field – MediaLive ignores this field.
  During processing, MediaLive will read the metadata, in order to identify the color space.
