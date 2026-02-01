# Configuring the start time for the output

timecode

You can configure the start time for the output timecode that MediaLive includes in output
encodes.

###### Note

This procedure assumes that you are familiar with creating or editing a channel,
as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

1.  On the **Create Channel** page, in the **General
    settings** section, choose **Timecode
    configuration**.
2.  In **Source**, choose the option for initializing the
    timecode in the output:
    - **EMBEDDED** – Use the timecode embedded in the
      source video.

    MediaLive looks for the timecode in the source video, as follows:

        + AV1 – A timecode inserted in a metadata OBU of type
         timecode (METADATA\_TYPE\_TIMECODE), in accordance with section
         5.8.3 of the AOM AV1 specification
         (https://aomediacodec.github.io/av1-spec/)
        + H.264 – A timecode inserted in an SEI message of type
         pic\_timing, in accordance with section D.1.2 of ISO/IEC
         14496-10-2005
        + H.265 – A timecode inserted in an SEI message of type
         timecode, in accordance with section D.2.26 of ITU-T
         H.265


        + MPEG-2 – A timecode inserted in each GOP header, in
         accordance with section 6.2.2.6 of ISO/IEC 13818-2-2000
         (R2006)

    - **SYSTEMCLOCK**– Use the UTC time.
    - **ZEROBASED** – Use 00:00:00:00.

3.  (Optional) In **Sync threshold**, enter a threshold (in
    frames) for synchronizing the output timecode to the input timecode. For
    information about this field, see [About the synchronization threshold](#timecode-sync "#timecode-sync").

## How the output timecode works at runtime

**Initial channel start or restart**

When you start the channel, the channel establishes the start timecode for the
output pipeline:

- The channel samples the input timecode, if you set up the start time to
  reference the embedded timecode. If MediaLive doesn't find an embedded timecode
  in the source, it falls back to UTC.
- Or it sets the timecode to the current UTC time.
- Or it sets the timecode to 00:00:00:00.

The channel generates a new timecode for each output frame that it produces.

**Input switches**

When the channel switches to a different input, MediaLive doesn't reinitialize the
timecode. Therefore, the output timecode isn't disrupted by an [input switch](scheduled-input-switching.md "scheduled-input-switching.md").

**Pausing and unpausing**

If you pause the channel, MediaLive continues to encode frames, which it immediately
discards. But because MediaLive continues to encode, the timecodes continue to
increment. Therefore, when you unpause, there will be a timecode discontinuity in
the output.

## About the synchronization threshold

The timecode **Sync threshold** field synchronizes the output
timecode with the input timecode. Drift can occur in several ways. For example,
processing issues can occur that cause MediaLive to drop or repeat frames to compensate.
Or there might be discontinuities in the input timecode stream.

**Purpose of synchronization**

Synchronization is useful if it is important for your workflow that the output
timecode (that MediaLive generates) match the original input timecode.

- Matching might be important if you know that the downstream system must
  identify specific frames.

Typically, the downstream system has already identified these frames based
on the original input timecode. Therefore, the output timecode must match
the original input timecode, in order for the downstream system to find the
desired frame.

- Matching isn't important if the main purpose of the output timecode is
  simply to uniquely identify each output frame.

**How synchronization works**

After the input timecode and the output timecode have drifted apart by the
specified number of frames, MediaLive inserts a discontinuity in the output timecode
sequence, and sets the output timecode to match the current input timecode.

The main drawbacks of synchronizing are that it introduces timecode
discontinuities into the metadata, and that it can't guarantee that each output
timecode is unique.
