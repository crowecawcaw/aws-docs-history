# How MediaLive uses the SMPTE 2038 stream

If you set up to prefer SMPTE 2038 in an input, MediaLive uses the data according to the
following rules.

**Captions**

You might [set up the input with captions
selectors](identify-captions-in-the-input.md "identify-captions-in-the-input.md") that specify **ARIB**, **Embedded**,
or **Teletext**. In this case, MediaLive first looks for the specified type of
captions in the SMPTE 2038 stream. If MediaLive doesn't find the captions there, it looks in
other locations in the stream.

Regardless of where MediaLive finds the captions, MediaLive extracts them, and processes them in
the usual way, according to how you set up for [captions in the output](create-captions-encodes.md "create-captions-encodes.md").

**Timecode**

When an input includes a SMPTE 2038 stream, MediaLive first looks for a SMPTE 12M timecode
in the SMPTE 2038 stream. If MediaLive doesn't find the timecode there, it looks for a timecode
embedded directly in the video stream. MediaLive associates the SMPTE 12M timecode with the
closest video frame.

For information about how MediaLive uses the timecode, see [How the output timecode works at runtime](timecode-configure-source.md#timecode-runtime "timecode-configure-source.md#timecode-runtime") .

**Ad avail messages**

If you prefer SMPTE 2038 in an input, MediaLive extracts any SCTE 104 messages it finds,
then immediately converts them to SCTE 35 messages. You can then handle the messages as you
would handle SCTE 35 messages from any source. For more information, see [Processing SCTE 35 messages](scte-35-message-processing.md "scte-35-message-processing.md").

**KLV metadata**

If you prefer SMPTE 2038 in an input, MediaLive extracts any KLV data that it
finds.

You can choose to pass through the KLV metadata in one or more of the following output
groups. MediaLive wraps the KLV in a SMPTE 2038 stream.

- Archive
- MediaPackage
- HLS (with a TS container)
- UDP/TS
  The setup steps follow.
