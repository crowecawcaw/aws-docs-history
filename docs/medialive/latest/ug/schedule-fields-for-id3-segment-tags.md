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

| Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Action type**   | **HLS ID3 Segment Tagging**. Choose this<br>option to insert in HLS or MediaPackage<br>outputs.**ID3 Segment Tagging**.<br>Choose this option to insert in CMAF Ingest<br>outputs.                                                                                                                                                                                                                                                                                                                                     |
| **Action name**   | A name for the segment tag.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Start type**    | **Fixed\*<br>• or<br>**Immediate\*\*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Date and time** | If the **Start type\*<br>• is<br>**Fixed\*\*, specify the UTC start time<br>for the ID3 segment tag. The time should be at least 15<br>seconds in the future.<br>Note that the time is the wall clock time, not the<br>timecode in the input.                                                                                                                                                                                                                                                                          |
| **Tag**           | Complete this field if the content of the tag is free text.<br>Enter the `value` for a `TXXX` field<br>inside the ID3 tag. MediaLive creates an ID3 tag with a single TXXX<br>field and inserts the tag in every segmenThe content can<br>include MediaLive [variable data](variable-data-identifiers.md "variable-data-identifiers.md"). In the following example, the<br>content consists of the date and time, and the current<br>segment number. The tag contents will be different in each<br>segment.`$dt$-$sn$` |
| **ID3**           | Complete this field if the content of the tag is ID3<br>metadata. Enter the content encoded as base64. The metadata must<br>be fully formed ID3 metadata (including both a header and a<br>frame, as per the ID3 specification).                                                                                                                                                                                                                                                                                       |
