# Converting the color space

You can set up to _convert_ the color space itself—to
change the pixels in the video. MediaLive can perform specific color space conversions.

MediaLive can convert only color spaces that it supports. See [Supported color space standards](color-space-standards.md "color-space-standards.md").

Here are the possible combinations for conversion:

- Convert the color space, and include color space metadata. MediaLive will convert the
  color space metadata to accurately describe the new color space.
- Convert the color space, but omit the color space metadata. You might want to remove
  the color space metadata because the downstream system can't handle it properly.

When MediaLive removes the metadata, the source still has a color space but it doesn't
have information that identifies the color space. Removing the metadata doesn't
necessarily degrade the color. Removing it might only mean that the downstream player
can't implement enhancements to make the color even richer.

###### Warning

If the content provider can't tell you what color space applies to the input, you
shouldn't try to convert the color space. Doing so might degrade the video quality. You
should pass through the color space. You should also remove the color space metadata, so
that the downstream system doesn't read information that might be inaccurate.

MediaLive converts from one color space to another based on the metadata in the source
content. MediaLive doesn't examine the video to try to determine whether it actually matches the
color space identified in the metadata.

## Supported types of conversion

The following table identifies the color spaces in the source that can be converted to
a specific color space in a MediaLive output.

| Any of these color spaces in the source                                                                                                          | Can be converted to this color space in the output |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| Rec. 709, HLG, HDR10                                                                                                                             | Rec. 601                                           |
| Rec. 601, HLG, HDR10                                                                                                                             | Rec. 709                                           |
| Rec. 601, Rec. 709, HLG                                                                                                                          | HDR10                                              |
| None. Conversion to HLG isn't supported                                                                                                          | HLG                                                |
| HDR10<br>If MediaLive encounters a portion of non-HDR10 content, it passes through the<br>color space and color space metadata for that portion, | Dolby Vision 8.1                                   |
