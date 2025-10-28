# Overview of graphic overlay

solutions

You can insert a graphic onto the video in an Elemental Live event
using the graphic overlay feature. There are two types of graphic overlay
available — static and motion.

###### Topics

- [Static overlay](#about-static-overlay "#about-static-overlay")
- [Motion graphic overlay](#about-motion-overlay "#about-motion-overlay")
- [Inserting both
  types of overlay](#supported-combinations-of-features "#supported-combinations-of-features")

## Static overlay

The static overlay feature lets you insert an image on the video at
a specified time and to display it for a specified duration.

The static overlay can be a BMP, PNG, or TGA file.

You can insert up to eight overlays through the web interface and
any number of overlays through the REST interface. The overlays are all
independent of each other, which means that they can be set up to all
appear on the underlying video at the same time (or not), and they can
be set up to physically overlap each other (or not). This feature
includes fade-in/fade-out capability and opacity.

For more information, see [Static graphic overlay](static-graphic-overlay.md "static-graphic-overlay.md").

## Motion graphic overlay

The motion graphic overlay feature lets you insert one animated
overlay on the underlying video at a specified time for a specified
duration.

You set up one overlay for the event. When the event is running, you
use the REST interface to modify the start time of the single overlay,
and to change the content. In this way, you achieve the effect of
several motion overlays played at different times in the event.

You can insert an animation in one of the following ways:

- HTML Files – You can use an HTML asset that you are
  continually publishing to a location outside of Elemental Live,
  and insert the asset into the video as an overlay. Use one of the
  following methods to control when the image appears:
  - You can let the authoring system control everything.
  - You can enter REST API commands to show or hide the
    image.
  - Your content provider can insert SCTE-35 messages to
    show and hide the image.

- MOV Files – Using a `.mov` file is a
  straightforward way to insert an animation onto the video of your
  event. You provide the file and set up your event to use it.
- Series of PNG Files – You can specify a series of
  `.png` files to be inserted one after the other to
  create an animation.

For more information, see [Insert a motion graphic overlay
in Elemental Live](motion-graphic-overlay.md "motion-graphic-overlay.md").

## Inserting both

types of overlay

You can insert both static overlays and one motion overlay onto the
underlying video.
