This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Using SWF Files for Motion Graphic Overlay with

AWS Elemental Server

With Shockwave Flash (SWF) files, the AWS Elemental encoder renders each frame of animation
during transcoding. SWF rendering is resource-intensive, so poorly optimized SWF assets may
significantly slow down transcoding time.

If your motion graphic overlay doesn't rely on any of the ActionScript abilities of Flash,
for example, performing squeezeback, then a SWF file may not be the best choice, especially at
high resolutions and/or high framerates. For more information about using the other supported
formats for motion graphic overlay, see [Including Inserted Images (Graphic Overlays) with
AWS Elemental Server](graphic-overlay.md "graphic-overlay.md").

For motion graphics that rely on ActionScript, follow the best practices outlined in this
document to create SWF files that are optimized to render with the least impact on encoder
system resources.

###### Topics

- [Minimize Your Flash Stage Size](#image-inserter-swf-adobe-flash-minimize-size "#image-inserter-swf-adobe-flash-minimize-size")
- [Optimize Flash Stage for
  Input](#image-inserter-swf-adobe-flash-optimize-input "#image-inserter-swf-adobe-flash-optimize-input")
- [Optimize Your Assets](#image-inserter-swf-adobe-flash-optimize-assets "#image-inserter-swf-adobe-flash-optimize-assets")
- [Sandbox the SWF File](#image-inserter-swf-adobe-flash-sandbox "#image-inserter-swf-adobe-flash-sandbox")
- [Do Not Embed Video](#image-inserter-swf-adobe-flash-do-not-embed-video "#image-inserter-swf-adobe-flash-do-not-embed-video")
- [Be Wary of Simulating
  Video in Flash](#image-inserter-swf-adobe-flash-be-wary-simulating "#image-inserter-swf-adobe-flash-be-wary-simulating")
- [Set Publish Target and
  Script](#image-inserter-swf-adobe-flash-set-publish-target "#image-inserter-swf-adobe-flash-set-publish-target")

## Minimize Your Flash Stage Size

If your overlay only takes up a small portion of the screen (such as a lower-third or
animated bug), size your Flash stage as small as possible to still contain the asset's
size/motion/movement. Position it within the underlying video in AWS Elemental Server
when setting up the event or job. For example, instead of putting a 40x40 animation on a
1280x720 Flash canvas, size your canvas down to 40x40 (or just slightly larger to capture any
dropshadow, embossing, and such).

To specify the position of the animation, go to the Motion Image Inserter portion of the
Global Processors section of the AWS Elemental event or job. Use the “Left” and “Top” fields
to specify the offset, in pixels, from the top left corner of the screen.

## Optimize Flash Stage for

Input

For best quality, the resolution and framerate of the animation should match those of the
underlying video. We particularly recommend against scaling down.

If the animation resolution and framerate cannot be changed, the AWS Elemental encoder
automatically adjusts the animation, but the quality of the animation may suffer.

## Optimize Your Assets

Be sure the assets in your Flash animation are optimized for the canvas.Don’t embed a
series of large images and scale them down to fit.Instead use images that are properly sized
before bringing them into Flash.

## Sandbox the SWF File

Test the SWF file in the sandbox environment before using it. In the sandbox testing
environment, the SWF file must not reference other resources on the filesystem or network,
which would slow down the rendering of the frames.

## Do Not Embed Video

The AWS Elemental motion graphic overlay feature does not have the ability to decode
video.

Therefore, you cannot embed video into your Flash animation.

## Be Wary of Simulating

Video in Flash

One way of simulating video in Flash is to include a sequence of images in the SWF
file.This mechanism is supported but not recommended. We strongly encourage use of the native
Flash animation components as Flash is optimized for those. Fall back to using sequences of
images only as a last resort and only for small subsections of the screen as Flash is more
reliable in those situations.

If you do use a sequence of images, it is especially important to optimize your
images—make sure they are small and simple, crop them down to the smallest possible area, and
keep them scaled 1:1 with the image canvas.

## Set Publish Target and

Script

Set your Publish Settings so that Target is Flash Player 11.1 and Script is set to
ActionScript 3.0. This is the only version that is supported.
