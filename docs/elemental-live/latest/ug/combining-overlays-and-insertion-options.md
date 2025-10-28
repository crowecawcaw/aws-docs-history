# Combining

overlays and insertion options

You can set up the event to insert a static overlay in more than one way. For
example, you can insert a static overlay in one layer in the Input section and insert a
static overlay in another layer in the Global Processors section.

**Examples**

- Example 1 – You want to insert a static overlay at a specific time and
  run it for 10 seconds. You want the static overlay to be placed in the lower right
  corner of the video frame. You want the static overlay to be 50% opaque and to
  fade in from nothing to full 50% opacity over 2 seconds, then to fade out to
  nothing starting 2 seconds before the end of the insertion.

You can implement this use case via the web interface or the REST API.

- Example 2 – You want to insert 2 static overlays so that they both
  appear on the video frame either at the same time, or with some overlap. You want
  the display of the static overlays to slightly overlap, so that one static overlay
  appears in a location and then while that static overlay is still showing, another
  static overlay appears in a specified location. If the locations overlap either
  partially or completely, you want to be able to specify which static overlay
  appears on top.

When you want to insert between 1 and 8 static overlays, you can implement this
use case via the web interface or the REST API.

- Example 3 – You want to insert 20 static overlays over the duration of
  the video. Some of the static overlays repeat, while some are unique. Some of them
  appear at the same time as others – up to 8 static overlays can appear at the same
  time.

When you want to insert more than 8 static overlays, you must use the REST API.

- Example 4 – You want the same static overlay to appear repeatedly over
  the duration of the video, either in the same location each time or in different
  locations. This use case is simply a variation of use cases 2 or 3 with the same
  static overlay being used each time.
