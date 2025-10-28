# Step A: Choose the method for show/hide

You must speak to the operator of the authoring system and decide
how the overlay will be controlled. There are several
options.

## Authoring system

control

The authoring system might set up the asset so that it
controls how and when the motion overlay appears. In the output
video, the overlay is always present, but sometimes it contains
no content. For example, the authoring system might set up so
that when the motion overlay shouldn't appear on the video, the
overlay is present but contains no content (it is transparent).

Your role is to set up in Elemental Live so that the event
shows the overlay as soon as the event starts. You never hide the
overlay. You (the Elemental Live operator) don't have to
coordinate with the operator of the authoring system.

It is the job of the authoring system to make sure that the
asset shows content sometimes and appears as transparent (no
content) at other times.

## REST API control

The authoring system might set up the asset with the
expectation that you (the Elemental Live operator) will show and
hide the overlay at the appropriate times.

Elemental Live continually pulls the asset from the authoring
system.

Your role is to enter REST API commands to show and hide the
overlay. You (the Elemental Live operator) and the operator of the
authoring system must coordinate the schedule for showing
overlays.

## SCTE 35 control

The authoring system might set up the asset with the
expectation that the source content includes specific SCTE 35
messages that Elemental Live reads to know when to show or hide
the overlay.

You have no role in showing or hiding the overlay.

Instead, the overlay is controlled as follows. Elemental Live
is continually pulls the asset from the authoring system. In
addition, Elemental Live automatically shows or hides the overlay
when it encounters the SCTE 35 messages.

To use this method, the content must already contain the
appropriate SCTE 35 messages. You can't use Elemental Live to
insert these messages.

The authoring system, the content provider (who must insert
the SCTE 35 messages in the content), and you (the Elemental Live
operator) must coordinate the SCTE 35 messages and the
schedule.

Elemental Live reacts to well-formed SCTE 35 messages of type
`time_signal`. The message must include the
following tags:

- `segmentation_type_id`: Provider Overlay
  Placement Opportunity Start (0x38) or Provider Overlay
  Placement Opportunity End (type 0x39).
- `segmentation_duration_flag`: true or
  false
- `segmentation_duration`: Must be included if
  the `segmentation_duration_flag` is true.
