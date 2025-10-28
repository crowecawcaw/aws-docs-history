# Passing through the color space

You can set up to _pass through_ the color space from
the source to a MediaLive output. You can set up to include or
remove the color space metadata. For passthrough to produce the
desired quality in the video output, the color space metadata must be accurate.

Here are the possible combinations for passthrough:

- Pass through the color space, pass through the color space metadata without
  correcting it (because you know that it is accurate).
- Pass through the color space, pass through the color space metadata after correcting
  it.
- Pass through the color space, remove the color space metadata without correcting it.
  You might want to remove the color space metadata because the downstream system can't
  handle it properly.

When MediaLive removes the metadata, the source still has a color space but it doesn't
have information that identifies the color space. Removing the metadata doesn't
necessarily degrade the color. Removing it might only mean that the downstream player
can't implement enhancements to make the color even richer.
**Default behavior**

The default behavior is to pass through the color space and pass through the uncorrected
color space metadata.
