# Different mechanisms for including metadata

You can include metadata in the following ways.

- Passthrough — Pass through metadata that is already present in the source input. You
  set up to include this metadata when you create or modify the channel.
- Timestamp — Insert a timestamp at a regular interval. You set up to include this
  metadata when you create or modify the channel. See [Inserting ID3 timed metadata when creating the MediaLive
  channel](insert-timed-metadata.md "insert-timed-metadata.md")
- One-time insertion — Insert metadata once, at a specified time. You insert this
  metadata by creating an action in the channel schedule. See [Inserting ID3 metadata using the
  schedule](insert-id3-metadata-via-schedule.md "insert-id3-metadata-via-schedule.md").
- Segment insertion — Insert metadata in every segment. You insert this metadata by
  creating an action in the channel schedule. You insert the action as plain text, using the
  tag option, or as base64, using the ID3 option. See [Inserting ID3 metadata using the
  schedule](insert-id3-metadata-via-schedule.md "insert-id3-metadata-via-schedule.md").
  The different mechanisms are supported in specific types of output groups. You set up each
  output group separately. In the following table,
  read across each row to
  identify the mechanisms that are supported for the specified type of output group.
  If a cell is empty, then the output group doesn't support that
  mechanism.

|                | Passthrough | Timestamp | One-time insertion | Segment insertion<br>(tag<br>option) | Segment insertion<br>(ID3<br>option) |
| -------------- | ----------- | --------- | ------------------ | ------------------------------------ | ------------------------------------ |
| Archive        | Supported   |           |                    |                                      |                                      |
| CMAF Ingest    | Supported   | Supported | Supported          |                                      | Supported                            |
| HLS TS         | Supported   | Supported | Supported          | Supported                            |                                      |
| HLS MP4        | Supported   | Supported | Supported          | Supported                            |                                      |
| HLS audio-only |             | Supported |                    | Supported                            | Supported                            |
| MediaPackage   | Supported   |           | Supported          | Supported                            |                                      |
| UDP            | Supported   | Supported |                    |                                      |                                      |

## Scope of the insertion

You configure each mechanism separately, and you configure each mechanism at the output
level. You can configure one group of outputs with one mechanism, and another group or an
overlapping group with another mechanism. Each mechanism as its own scope. In the following
table, read across each row to determine the scope of the mechanism.

| Mechanism                                                 | First condition                                             | Second condition                    | Third condition                                                |
| --------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------- | -------------------------------------------------------------- |
| Passthrough                                               | All the outputs where you have enabled metadata passthrough | And that support passthrough        |                                                                |
| Timestamp                                                 | All the outputs where you have enabled metadata passthrough | And that support timestamp          | And where you have configured the output group for timestamp   |
| One-time insertion, using the schedule                    | All the outputs where you have enabled metadata passthrough | And that support one-time insertion |                                                                |
| Segment insertion with the tag option, using the schedule | All the outputs where you have enabled metadata passthrough | And that support segment tags       | And where you have enabled segment tagging in the output group |
| Segment insertion with the ID3 option, using the schedule | All the outputs where you have enabled metadata passthrough | And that are audio-only outputs     | And where you have enabled segment tagging in the output       |

## Frames, ID3 tags, PIDs

The metadata is inserted into a specific ID3 frame (for example, TXXX). The frame is
inserted in an ID3 tag. The ID3 tag goes in a PID (for a TS output) or the emsg event (for
an MP4 output).

**Supported types of ID3 frames**

Different mechanisms support different types of ID3 frames.

| Mechanism                                                 | Type of frame                                                                      |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Passthrough                                               | MediaLive passes through any frame type, including **PRIV\*<br>• or<br>**TDRL\*\*. |
| Timestamp                                                 | You specify the frame type: **PRIV\*<br>• or<br>**TDRL\*\*                         |
| One-time insertion, using the schedule                    | You specify the frame type. All ID3 frame types are supported.                     |
| Segment insertion with the tag option, using the schedule | A TXXX                                                                             |
| Segment insertion with the ID3 option, using the schedule | Any frame type. You specify the frame type.                                        |

**PID for the ID3 tag**

With TS output groups, all the mechanisms for ID3 metadata insert the ID3 tag in the
same PID. The default is 502, but you have the option to override the default in any output
group.
