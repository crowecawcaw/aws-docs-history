# Configuring the handling in the

input

You must decide what you need to do with _color
space metadata_ in the input. You might need to clean up the
metadata to ensure that Elemental Live handles the color space correctly in
the output.

###### Important

Keep in mind that the handling on the input side of the event is about
changing the color space metadata, not changing the color space itself. It
is about changing the metadata to correctly identify the color space in the
input, in preparation for planned handling in the outputs.

The conversion of the video to a different color space occurs in [Configuring color space handling in each
output](hdr-output.md "hdr-output.md").

If you plan to _pass through_ the color
space to the outputs, you should do one of the following:

- Clean up the color space metadata, if the content provider tells you
  that it is missing or inaccurate.
- Leave the metadata as is, if the color space metadata is
  correct.
  If you plan to _convert_ the color
  space in the outputs, you should do one of the following:

- Clean up the color space metadata, if the content provider
  tells you that it is missing or inaccurate.
- Leave the metadata as is, if the color space metadata is
  correct.
  If you plan to remove the metadata, there is no need to work with the
  color space metadata in the input.

The following table specifies the handling that is available for color
spaces in the input.

| Color space             | Elemental Live can correct the color space metadata |
| ----------------------- | --------------------------------------------------- |
| 601                     | Yes                                                 |
| 709                     | Yes                                                 |
| SDR 2020                | Yes                                                 |
| HDR10                   | Yes                                                 |
| HLG                     | Yes                                                 |
| Dolby Vision 5.0        | No                                                  |
| Dolby Vision 8.1        | No                                                  |
| Unsupported color space | No                                                  |

To decide how to handle the color space metadata, use the following
three steps.

###### Topics

- [Step 1: Decide on the input handling](color-space-input-procedure.md "color-space-input-procedure.md")
- [Step 2: Choose a clean-up
  scenario](color-space-cleanup-scenarios.md "color-space-cleanup-scenarios.md")
- [Step 3: Set up each input](color-space-event-input-setup.md "color-space-event-input-setup.md")
