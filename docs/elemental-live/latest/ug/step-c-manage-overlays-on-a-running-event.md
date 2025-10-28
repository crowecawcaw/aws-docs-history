# Step

C: Manage overlays on a running event

Once the event has started, you can work with static overlays only via the REST
API. You cannot work with static overlays on a running event via the web interface.

Change the static overlay or overlays on a running event:

1. If you did not set the `<enable_rest>` element to
   `true` when you created the event, modify the event (PUT Event)
   and set this value. For the location of this element, see [Modify
   static overlay on a running event](modify-static-overlay-on-a-running-event.md "modify-static-overlay-on-a-running-event.md").
2. Send the Modify Static Overlay command (see [Using the REST
   API for static overlays](using-the-rest-api-for-static-overlays.md "using-the-rest-api-for-static-overlays.md")) to make the desired
   change to the static overlays in the event.

###### Runtime REST commands change the event XML

When you send REST commands during an event, the event XML is permanently changed. Any data sent via the REST call goes into the XML.

For example, you might put a scoreboard overlay on your event during a sporting
event. If you do not send a REST call to deactivate the overlay once the game has
ended, the scoreboard will appear again at the same time the next day.

Therefore, make sure to do one of the following:

- If you plan to run the event (event A) again with different video
  content but with the same graphic overlays, make sure to export your XML for
  re-use before starting the event. Then create a new event (event B) using
  the exported XML. Do not start event A again.
- If you are running a 24/7 channel and you do not want your overlay to
  recur, remember to send a REST command to set <activate> to false once
  the overlay has run. This will delete the entire <insertable_images>
  element from the event XML.

You could also specify an absolute start time for each overlay by using
the ISO 8601 UTC time format to specify an absolute time and date for the
overlay. The overlays will not run again the next day.

## Options for insertion - which outputs are affected

You can insert static overlays in one of the following places in the running
event. These places are the same as the places when inserting in a new event or
modifying a non-running event.

- In an individual input. The input must be currently running or be in the
  future.

If you include a start time in the XML body, that start time must fall
within the scope of the specified input. It must correspond to a time that
is valid for that input. For example, if the input runs from 1:00 p.m. to
2:00 p.m. by the clock, the start time must correspond to a clock time
between 1:00 p.m. and 2:00 p.m., otherwise the insertion will be ignored.
The start time can be in the past, so long as it is within the scope of the
input; in this case, the overlay will be inserted immediately.

- In all outputs.

If you include a start time in the XML body, the overlay will be inserted
at that at start time. If that start time is in the past, the overlay will
be inserted immediately.

- n the outputs associated with one stream assembly.

If you include a start time in the XML body, the overlay will be inserted
at that at start time. If that start time is in the past, the overlay will
be inserted immediately.

## Types of

changes

###### Add an overlay in a layer

You can add an overlay in a layer. For example, if you did not fill all 8
layers when creating the event, you can add more static overlays, up to a total
of 8 for the event. Or if you already deleted a layer (as described below), you
can fill it with a new static overlay.

You must enter a Modify Static Overlay command ([Create or modify a non-running event with static graphic
overlay](create-or-modify-a-non-running-event-with-static-graphic-overlay.md "create-or-modify-a-non-running-event-with-static-graphic-overlay.md"))
and include the following tags in the XML body:

- layer: The (unused) layer where you want to add the static overlay.
- activate: Set to true. Note that this tag is not part of the XML body for
  creating the event.
- Other tags: Set all other tags as desired to specify the content and its
  characteristics, start time and duration.

###### Modify an existing overlay

You can modify the existing content in a layer. You can do the
following:

- Change a static overlay that has not yet run.
- Change a static overlay that is currently running. The static overlay
  will change in mid-stream.
- Change a static overlay that has run in order to re-use the layer.

You can change the static overlay’s start time or duration. Or you can change
its position. Or you can change the actual overlay that runs.

You must enter a Modify Static Overlay command ([Create or modify a non-running event with static graphic
overlay](create-or-modify-a-non-running-event-with-static-graphic-overlay.md "create-or-modify-a-non-running-event-with-static-graphic-overlay.md"))
and include the following tags in the XML body:

- layer: The layer whose static overlay you want to modify.
- activate: Set to true. Note that this tag is not part of the XML body for
  creating the event.
- Other tags: Set all other tags as desired to specify the content and its
  characteristics, start time and duration. Only the tags you specify will be
  changed.

###### Delete an overlay

You can delete the existing content in a layer. If the static overlay has
not yet run, it will not run. If the static overlay is currently running, it
will be removed. If the static overlay has already run, there is not really any
need to delete the content.

You must enter a Modify Static Overlay command ([Create or modify a non-running event with static graphic
overlay](create-or-modify-a-non-running-event-with-static-graphic-overlay.md "create-or-modify-a-non-running-event-with-static-graphic-overlay.md"))
and include the following tags in the XML body:

- layer: The layer to delete.
- activate: Set to false. Note that this tag is not part of the XML body
  for creating the event.
