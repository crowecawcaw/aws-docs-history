This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Including Inserted Images (Graphic Overlays) with

AWS Elemental Server

The image inserter (graphic overlay) feature lets you insert a still image or motion graphic at a
specified time and display it as an overlay on the underlying video for a specified
duration. With still overlays, you can specify fade-in and fade-out times and adjust the
opacity.

You can set up an output with both a motion graphic overlay and still overlays. For
example, you might include a motion graphic logo in the corner of the video frame throughout
the duration of the video and a still image HDR indicator for only the portions of the file
that are HDR. Each overlay is independent of the others, with its own settings for opacity,
fade-in and fade-out times, position on the frame, and the length of time that it is on the
video. You can set up overlays so that they all appear on the underlying video at the same
time and physically overlap each other.

You can use up to one motion overlay and 100 still overlays
per job.

###### Topics

- [Still Image Inserter (Graphic Overlay) in
  AWS Elemental Server](setting-up-a-graphic-overlay.md "setting-up-a-graphic-overlay.md")
- [Motion Image Inserter (Graphic Overlay) in
  AWS Elemental Server](motion-graphic-overlay.md "motion-graphic-overlay.md")
