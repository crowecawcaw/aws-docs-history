This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Overlay File

Requirements

Set up the image files that you want to insert over your video as follows:

- **File type**: Use files with the extension
  `.png` or `.tga`.
- **Aspect ratio**: Use any aspect ratio; the
  aspect ratio of the overlay file doesn't need to match the aspect ratio of
  the underlying video.
- **Size in pixels**: Use any size. If the
  overlaid graphic is larger than the output video frame, the service crops
  the graphic at the edge of the frame.

###### Note

In jobs that scale the video resolution, whether your overlay scales
with your video depends on where you specify the graphic overlay. For
more information, see [Sizing Your Overlay to Account
for Scaling](about-overlay-scaling.md "about-overlay-scaling.md").
