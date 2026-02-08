# Input and output

requirements

In order for MediaLive to lock pipelines, the following conditions must be in effect in
the channel. When pipeline locking isn't possible, processing continues. As soon as the
required conditions are again in effect, MediaLive starts to lock again.

## No support for HLS inputs

The channel can't include HLS inputs.

If the channel includes an HLS input, MediaLive stops attempting to lock pipelines in
the channel. Pipeline locking won't resume, even after the channel switches to
another input.

## Inputs must include embedded

timecode (source timecode method)

When you use the source timecode pipeline locking method (the default), the
input must include embedded timecode. These rules apply:

- When using the source timecode method, the input must have an embedded
  timecode. This requirement applies to both pipeline locking mode and
  epoch locking mode.
- For epoch-locking mode, the embedded timecode must be within 2 minutes of
  epoch time. If the timecode is off by more than 2 minutes, MediaLive considers
  that the source doesn't meet the requirements for pipeline locking.

MediaLive continually probes the current source for an embedded timecode. Whenever it
doesn't detect the timecode, it temporarily suspends the attempt to lock
pipelines.

## Requirements for

video aligned pipeline locking

When you use video aligned pipeline locking (**Pipeline locking
method** set to **VIDEO_ALIGNMENT**), embedded timecodes
are not required.

**Input requirements**

Certain input types are not compatible with video
alignment:

- File inputs (MP4_FILE, TS_FILE)
- HLS inputs (URL_PULL with HLS content)
- RTMP_PULL inputs

When an incompatible input type is active, video aligned pipeline locking runs
in "open loop" mode (unlocked) but continues processing. No validation error is
raised, which supports input switching workflows where some inputs may be
incompatible.

For all other input types, video aligned pipeline locking uses visual signature
comparison to synchronize the pipelines. Both pipelines must receive the same
video content for successful synchronization.

## Frame rate

requirements

The conversion between the input framerate (or framerates) and the desired output
framerate must be _simple_, which means that one of
these statements must apply:

- The output framerate must be a whole number multiple of the input
  framerate. For example, the input framerate might be 45 FPS, and the output
  framerate might be 90 FPS.
- The input framerate must be a whole number multiple of the output
  framerate. For example, the input framerate might be 60 FPS, and the output
  framerate might be 30 FPS.

MediaLive identifies the source input framerate when it switches to a new input, and
determines if a simple conversion applies. If it doesn't, MediaLive stops the attempt to
lock pipelines until the channel switches to the next input. Even if the source
input framerate changes in mid source (so that a simple conversion applies), MediaLive
doesn't start attempting to lock again.

Note that with these rules, it is possible for the framerates to be integers. For
example, if the input framerate is 29.97 FPS and the output framerate is 59.94
FPS.

Following are examples of _complex_ framerates.
You _can't_ use the input if one of these
combinations applies to your channel:

- This
  isn't supported: Input FPS is 59.4, output FPS is

60.

- This
  isn't supported: Input FPS is 45, output FPS is 60.
- This
  isn't supported: Input FPS is 29.97 FPS, output FPS is
  23.978.

## Epoch locking and SCTE

35

There are constraints for using epoch locking in an HLS or MediaPackage output
group.

**HLS output group**

It's not possible to enable SCTE 35 passthrough or manifest decoration in an HLS
output group in a channel that uses epoch locking. You will get a validation error
when you save the channel. You must decide how to resolve this conflict:

- Don't enable epoch locking in the entire channel: You can [set the mode](pipeline-locking-set-up.md#pipeline-locking-mode "pipeline-locking-set-up.md#pipeline-locking-mode") to regular pipeline
  locking in the entire channel, and keep SCTE 35 passthrough in the HLS
  output group.
- Disable SCTE 35 passthrough in the HLS output group: You can keep epoch
  locking but disable SCTE 35 passthrough and manifest decoration in the HLS
  output group. You can still enable SCTE 35 passthrough in other output
  groups.

**MediaPackage output group**

For a MediaPackage output group, constraints apply if the input includes SCTE 35
messages:

- When epoch locking isn't enabled in the channel, MediaLive automatically
  passes through any SCTE 35 messages from the input and automatically enables
  manifest decoration.
- When epoch locking is enabled, MediaLive automatically disables SCTE 35
  passthrough and manifest decoration in the MediaPackage output group.

You should decide which feature you want to keep. You can keep the SCTE 35
messages (in which case you must disable epoch locking in the entire channel). Or
you can enable epoch locking but lose passthrough of the SCTE 35 messages. Note that
there is no advantage to setting up the output as an HLS output group, because
similar constraints apply, as described above.
