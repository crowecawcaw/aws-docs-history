# Handling of metadata when

converting

When you set up in MediaLive to convert the color space, you can set up to include or omit the color
space metadata.

- Include color space metadata. MediaLive will convert the color space metadata to
  accurately describe the new color space.
- Omit the color space metadata. You might want to remove the color space metadata
  because the downstream system can't handle it properly.

When MediaLive removes the metadata, the source still has a color space but it doesn't
have information that identifies the color space. Removing the metadata doesn't
necessarily degrade the color. Removing it might only mean that the downstream player
can't implement enhancements to make the color even richer.
