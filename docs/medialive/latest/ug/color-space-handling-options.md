# Options for handling color space

All video belongs to a specific color space. The color space defines the range of color
for the video. Video can include color space metadata. This metadata provides information
about the color space. When the color space metadata is missing, the video still has a color
space, but it is impossible for a video processor such as MediaLive to manipulate the color
space.

You can control how MediaLive takes the color space and color space metadata in a
video source and manipulates it in the video output.

You can set up each output video encode to handle the color space in different
ways:

| Option                   | Handling of color space | Handling of color space metadata     |
| ------------------------ | ----------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pass through and include | Pass through            | Pass through (corrected or original) |
| Pass through and remove  | Pass through            | Remove                               |
| Convert and include      | Convert                 | Generate new color space metadata    |
| Convert and remove       | Convert                 | Remove                               | **Scope of handling in outputs** You can set up each output in the channel for different handling. For example, you can set up one output to convert the color space to HDR10, set up one output to convert to HLG, and set up another output to pass through the color space. For more information, see [Passing through the color space](color-space-options-passthrough.md "color-space-options-passthrough.md") and [Converting the color space](color-space-options-convert.md "color-space-options-convert.md") . |
