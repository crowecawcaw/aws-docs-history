# Two options: global overlay and per-output

overlay

There are two options for inserting and removing image overlays in a MediaLive channel — the
global option and the per-output option.

- Global image overlay: Insert a static image overlay in every output in every output
  group. The action is called Static Image Activate.

- Per-outputs image overlay: Insert a static image overlay into the running channel,
  only in specific outputs in specific output groups. The action is called Static Image
  Output Activate.
  In one channel, you can combine the global action and the per-output option in the same
  channel. For example, you can insert image X globally (in all outputs) and insert image Y only
  in output A. Output A will have both image X and image Y. All other outputs will have only
  image X.

###### Topics

- [How MediaLive handles a global image](#image-overlay-global-about "#image-overlay-global-about")
- [How MediaLive handles a per-output
  image](#image-overlay-per-output-about "#image-overlay-per-output-about")
- [Image layers and inserting images](#image-overlay-layers "#image-overlay-layers")
- [Removing images](#image-overlay-remove "#image-overlay-remove")
- [Properties of the image](#image-overlay-properties "#image-overlay-properties")

## How MediaLive handles a global image

MediaLive inserts the image before it sets the resolution in the video. In this way, the
image gets resized as MediaLive resizes the video frame to obtain the specified resolution. The
output image and video frame can resized to be smaller (a lower resolution) or larger (a
higher resolution).

The global option works well when you want to use the same image in every video output,
and you want that image to take up the same proportion of the video frame in every video
output. When you prepare the image, you make sure that it takes up the desired proportion of
the source video. For example, you might want its height to be 10% of the height of the
underlying video. After MediaLive sets the video resolution, the image is still the same
proportion of the underlying video. For example, the image takes up approximately 10% of the
height of an output 720p video frame and approximately 10% of the height of an output 4K
video frame.

## How MediaLive handles a per-output

image

MediaLive sets the resolution of the video, and then it overlays the image. This means that
the image doesn't get resized, it retains its absolute size.

The per-output option is useful if you want to overlay different images in different
outputs. For example, you might want to insert one logo in the video in one output group,
and another logo in the video in another output group.

The per-output option is also useful if you want to insert an image without resizing it.
For example, if you want the image to have the same absolute size in every output in an ABR
stack. The image is the same absolute size on a 720p video frame as it is on a 4K video
frame. Therefore, you can use the same image file in all the outputs.

You might also want the image to have the same relative size in a group of outputs that
have have different resolutions. For example, you want every image to take up 10% of the
height. In this case, you must prepare separate files for each output, and create separate
insert actions in the different outputs.

## Image layers and inserting images

An image always exists in a layer. There are 8 global layers for the global option, and
8 per-output layers for the per-output option. A layer can contain only one image.

The layers are ordered. Layer 0 is at the bottom and layer 7 at the top.

The per-output layers are all on top of the global layers. This means that from the
bottom, the layers are global layers 0 to 7, then per-output layers 0 to 7. Keep this layer
order in mind if you plan to overlap images.

## Removing images

There are two actions to deactivate (remove) an image, one to remove from a global
layer, and one to remove from the per-outputs layer in specific outputs.

The global action removes the image from the specified layer and from all
outputs.

The per-output action is more flexible. For example, you might insert image X in
per-output layer 4 in outputs A and B. You might then insert image Y in per-output layer 4
in output C. You can then enter a deactivate action that removes the image from per-output
layer 4 in outputs A and C. Image X in output A will be removed, and image Y in output C
will be removed. Image X in output B will still exist.

## Properties of the image

**Start time and duration**

You can configure each image overlay with a start time and duration.

**Positioning**

You can insert the image overlay at any position on the video frame, relative to the X
axis and Y axis of the video frame. You can position images so that they overlap each other.

**Opacity and fade**

You can configure with an opacity and with fade-in and fade-out.

**Input insertion and overlays**

You might insert image overlays in a channel where you are also performing input
switching (to ingest different inputs). Keep in mind that the handling for input switches
and image overlays is completely decoupled. In other words, you don't have to worry that
when MediaLive switches to a different input, the currently active image overlays will
disappear. They won't disappear.
