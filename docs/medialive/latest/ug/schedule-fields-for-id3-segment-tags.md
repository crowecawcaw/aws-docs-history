# Fields for ID3 segment

tags

This table shows the fields that apply for an action to
insert
ID3 metadata in every
segment.
There are two options for inserting the metadata:

- The **tag** option, to insert metadata as plain
  text.
- The **ID3** option, to insert metadata as
  base64.
  For
  details about the types of output groups that support each option, see the table
  in [Different mechanisms for including metadata](id3-enable-result.md "id3-enable-result.md").

| Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Action type**   | **HLS ID3 Segment Tagging**. Choose this option to insert in HLS or MediaPackage outputs.**ID3 Segment Tagging**. Choose this option to insert in CMAF Ingest outputs.                                                                                                                                                                                                                                                                                                                            |
| **Action name**   | A name for the segment tag.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Start type**    | **Fixed** or **Immediate**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Date and time** | If the **Start type** is **Fixed**, specify the UTC start time for the ID3 segment tag. The time should be at least 15 seconds in the future. Note that the time is the wall clock time, not the timecode in the input.                                                                                                                                                                                                                                                                           |
| **Tag**           | Complete this field if the content of the tag is free text. Enter the `value` for a `TXXX` field inside the ID3 tag. MediaLive creates an ID3 tag with a single TXXX field and inserts the tag in every segmenThe content can include MediaLive [variable data](variable-data-identifiers.md "variable-data-identifiers.md"). In the following example, the content consists of the date and time, and the current segment number. The tag contents will be different in each segment.`$dt$-$sn$` |
| **ID3**           | Complete this field if the content of the tag is ID3 metadata. Enter the content encoded as base64. The metadata must be fully formed ID3 metadata (including both a header and a frame, as per the ID3 specification).                                                                                                                                                                                                                                                                           |
