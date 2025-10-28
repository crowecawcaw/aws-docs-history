# Result when passing through color

space

Read this section if you set up one or more MediaLive outputs to [pass through the color space](colorspace-output-setup.md#colorspace-output-setup-passthrough "colorspace-output-setup.md#colorspace-output-setup-passthrough"). The
following table shows how MediaLive handles each type of color space that it encounters in the
source.

| Color space that MediaLive encounters                                                            | How MediaLive handles the color space                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content in any color space that MediaLive supports                                               | Doesn't touch the color space or brightness (the pixel values) in the output. Passes through any of the three sets of metadata that are present.                                                      |
| Content in a color space that MediaLive supports, but that isn't supported for the output codec. | This conversion isn't supported. After conversion, the color map of the content will be completely wrong.                                                                                             |
| Content marked with unknown or an unsupported color space                                        | Doesn't touch the color space or brightness (the pixel values) in the output. Leaves the content as marked with the unknown color space. Passes through any brightness metadata and display metadata. |
| Content with no color space metadata                                                             | Doesn't touch the color space or brightness (the pixel values) in the output. Leaves the content as unmarked (no color space metadata).                                                               |
