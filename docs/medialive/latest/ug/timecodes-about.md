# About timecodes and timestamps

MediaLive has timecodes for the input pipeline and the output pipeline. The two timecodes
are separate from each other.

**Input timecode**

MediaLive has features that work only if incoming frames include embedded timecodes. These
features include pipeline locking and watermarking. If an input doesn't have an embedded
timecode, MediaLive won't implement the feature. For example, with pipeline locking, the
pipelines won't get locked in a frame accurate way. (For more information about how the
timecode affects pipeline locking, see [Implementing pipeline locking](pipeline-lock.md "pipeline-lock.md").

The input timecode source is not configurable.

**Output timecode**

MediaLive implements SMPTE timecode, which means that MediaLive assigns a timecode of the
format `HH:MM:SS:FF` to each outgoing frame. The timecode rolls over at
midnight.

There are three ways to initialize the output timecode in a channel:

- Embedded (the default): Use the embedded timecode to initialize the output
  timecode. MediaLive uses the timecode in the first frame that it ingests in the
  input. If the input does not contain a timecode, MediaLive uses UTC.
- UTC: Initialize the output timecode to the UTC time at the moment that the
  first frame enters the output side of the pipeline.
- Zero-based: Initialize the output timecode to 00:00:00:00.
  The output timecode is used in features such as the PDT for an HLS output, and for the
  timecode for ID3 metadata that you might choose to include. You can also configure
  output to include the output timecode as metadata and/or to burn the output timecode
  into the video frame.

You can also configure output video to include the [output timecode as metadata](timecode-configure-metadata.md "timecode-configure-metadata.md"), and/or to
[burn the output timecode](timecode-configure-burnin.md "timecode-configure-burnin.md") into the
video frame.

**Timestamps**

MediaLive attaches a timestamp to all output content. Downstream systems use the timestamp
for synchronization. The timestamp is a value such as the number of 90 KHz clock
cycles.

Don't conflate timestamps and timecodes. They are different.
