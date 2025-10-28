# Fields for ID3

metadata

This table shows the fields that apply for an action to
perform a
one-time
insertion
of
ID3
metadata.
MediaLive
inserts the metadata as base64.

| Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Action type**   | **HLS Timed Metadata**. Choose this option to insert in HLS or MediaPackage outputs.**Timed Metadata**. Choose this option to insert in CMAF Ingest outputs.                                                                                                                                                                                                                                                                                             |
| **Action name**   | A name for the metadata item. You might want to design a convention for naming ID3 metadata items, such as `id3_metadata-<UTC time>`.                                                                                                                                                                                                                                                                                                                    |
| **Start type**    | **Fixed** or **Immediate**.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Date and time** | If the **Start type** is **Fixed**, specify the UTC start time for the ID3 metadata item. The time should be at least 15 seconds in the future. Note that the time is the wall clock time, not the timecode in the input.                                                                                                                                                                                                                                |
| **ID3**           | Enter the ID3 metadata encoded as base64. The metadata must be fully formed ID3 metadata (including both a header and a frame, as per the ID3 2.4.0 specification). The content of the `value` property can include MediaLive [variable data](variable-data-identifiers.md "variable-data-identifiers.md"). MediaLive will examine the contents of the base64 and perform substitutions. For example, MediaLive will change `$dt$` to the date and time. |
