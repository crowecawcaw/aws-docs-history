# Passing through color space

You can pass through any color space that Elemental Live supports,
except for Dolby Vision 5.0. You can pass through both color spaces that
Elemental Live supports, and color spaces that it doesn't support, so long as
the output type supports the passed-through color space standard.

###### Note

This section assumes that you are familiar with creating or editing an
event.

###### To set up each output

Follow this procedure in each output.

1. On the **Event** page, in the **Output
   groups** section, choose the output group, and choose the output
   that contains the video.
2. Open the **Advanced** section. More fields
   appear.
3. Leave **Insert Color Metadata** checked. You should
   never remove the color metadata if you are passing through the color
   space.
4. Scroll down to the **Preprocessors** section and
   turn on **Color Corrector**. More fields appear.
5. Set **Color Space Conversion** to
   **None**, which means you don't want to convert the
   color space.
   The following table shows how Elemental Live handles each type of color
   space that it encounters. Each row in the table describes a different
   handling.

| Color space metadata that Elemental Live encounters       | How Elemental Live handles the color space                                                                                                                                                                     |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content in any color space that Elemental Live supports   | It doesn't touch the color space or brightness (the pixel values) in the output. It passes through any of the three sets of metadata that are present.                                                         |
| Content marked with unknown or an unsupported color space | It doesn't touch the color space or brightness (the pixel values) in the output. It leaves the content as marked with the unknown color space. It passes through any brightness metadata and display metadata. |
| Content with no color space metadata                      | It doesn't touch the color space or brightness (the pixel values) in the output. It leaves the content as unmarked (no color space metadata).                                                                  |
