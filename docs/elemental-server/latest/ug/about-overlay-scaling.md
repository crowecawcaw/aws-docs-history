This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Sizing Your Overlay to Account for

Scaling

In jobs that scale the video resolution, whether your overlay scales with your
video depends on where you specify the graphic overlay. Global and input overlays
scale with the video; stream overlays do not.

For example, suppose that the input video for your job is 1080 x 1920 and you
specify three outputs at 720 x 1280, 480 x 640, and 360 x 480. You want your square
logo to be 10% of the width of your frames. You would provide overlay images at the
following resolutions:

- For a motion graphic overlay or an input graphic overlay, provide a 108 x
  108 image. AWS Elemental Server appropriately sizes each overlay on each
  output.
- For a stream graphic overlay on your 720 x 1280 output, provide a 72 x
  72 image.
- For a stream graphic overlay on your 480 x 640 output, provide a 48 x 48
  image.
- For a stream graphic overlay on your 360 x 480 output, provide a 36 x 36
  image.
