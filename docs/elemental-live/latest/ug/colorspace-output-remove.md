# Removing color space metadata

Follow this procedure in each output where you want to remove the color
space metadata.

You might choose to remove the color space metadata in situations such
as the following:

- The pixel data and color space data in the input is incorrect, so
  that the downstream player can't use it to enhance the color.
- The color space (and its metadata) changes frequently within the
  input, or between one input and another, and you know that there is a
  system downstream of AWS Elemental Live that can't handle changes in the metadata.
  Keep in mind that removing metadata doesn't necessarily make the color
  poorer. Removing it might only mean that the downstream player can't
  implement enhancements to make the color even richer.

###### Note

This section assumes that you are familiar with creating or editing an
event.

###### To set up each output

1. On the **Event** page, in the **Output
   groups** section, choose the output group, and choose the output
   that contains the video.
2. Open the **Advanced** section. More fields
   appear.
3. Set **Insert Color Metadata** to unchecked.
4. Scroll down to the **Preprocessors** section and
   turn on **Color Corrector**. More fields appear.
5. Set **Color Space Conversion** to
   **None**, which means you don't want to convert the
   color space.
   The following table shows how Elemental Live handles each type of color
   space it encounters.

| Color space metadata that Elemental Live encounters                                                                                                   | How Elemental Live handles the color space                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content in any color space that Elemental Live supports Content with no color space metadata Content with unknown or unsupported color space metadata | It doesn't touch the color space or brightness (the pixel values) in the output.It removes all the metadata. The output won't contain any color space metadata, brightness metadata, or display metadata. |
