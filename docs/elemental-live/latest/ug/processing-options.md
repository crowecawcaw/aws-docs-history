# SCTE-35 and SCTE-104 message

processing options

## The options

The processing possibilities for SCTE messages include the
following.

###### Automatically convert SCTE-104 messages

SCTE-104 messages in the input are automatically converted
to SCTE-35 messages during processing of the input. No setup
is required for this processing.

###### Line up SCTE Messages to use blanking and blackout of

output content

The “cue out” and “cue in” instructions in SCTE-35 messages
line up with specific content in the video, audio, and closed
captions streams. You can set up to blank out this content in
the output.

- The content for ad avails is blanked out using the Ad
  avail _blanking_
  feature.
- The content for other messages is blanked out using the
  _blackout_
  feature.

Your desired behavior must be set up in the event or
profile.

###### SCTE-35 passthrough

You can include SCTE-35 messages in the output data stream
in any TS output. Your desired behavior must be set up in the
event or profile.

###### Manifest decoration

You can set up SCTE messages with manifest decoration with
these options:

- HLS outputs can be set up so that their manifests
  include instructions that correspond to the original
  SCTE-35 message content.
- MS Smooth outputs can be set up to include these
  instructions in the sparse track.
- RTMP outputs can be set up to include these instructions
  in the data stream (because RTMP outputs do not have
  manifests).

###### Conditioning by a POIS

Optionally, SCTE-35 messages (including those converted
from SCTE-104) can be diverted to a POIS server for ESAM
conditioning. This conditioning is in addition to all the
other processing (manifest decoration, blanking and blackout,
and passthrough).

POIS and ESAM conditioning are described in [POIS conditioning](pois-conditioning.md "pois-conditioning.md").

###### Insert SCTE-35 messages into content during an

event

The Elemental Live REST API includes commands to insert
SCTE-35 messages into the content while the Elemental Live
event is running.

You can insert using the Elemental Live REST API. Elemental Live
makes no distinction between these messages and those that were
in the original input. So, for example, if manifest decoration is
enabled and you insert a message during encoding, that new
message is represented in the manifest.

## Default behavior of SCTE-35

and SCTE-104 messages

The default handling of SCTE-35 and SCTE-104 messages in
Elemental Live includes the following:

- No manifest decoration: You do not convert any SCTE-35
  messages to event information in any output manifests or
  data streams.
- No passthrough: You do not pass through SCTE-35 or
  SCTE-104 messages in any data stream outputs.
- No blanking: You do not blank out video content for any
  events: you leave the content as is.

If you desire the default behavior as described , you have the
information you need for processing SCTE messages and do not need
to read the remainder of this guide.

## About

timecode configuration and timers

The event or profile includes a timecode configuration field
that identifies the source for timecode stamps to be inserted in
the output. The source for these stamps might be a timecode
embedded in the input or might be a source external to the input
(for example, the system clock or a specified time). The
Timecode Config field is just after the
Inputs section on the event page of the web
interface.

Before starting the transcode, the transcoder gets the
timecode from the source.

After the initial sampling, Elemental Live calculates the
timecode of every frame and attaches it to the output. The
timecode stops advancing if there is no output. So, for example,
if the input fails at 10:55:03:009, the timecode at that point is
10:55:03:009. If the input restarts 3 seconds later, the timecode of
the next frame might be 10:55:03:012. The timecode will _not_ be 10:55:**06**:009.

Given the importance of accurate times with SCTE-35 messages,
ensure that the **Network Time Protocol
(NTP)** is configured on the node.
