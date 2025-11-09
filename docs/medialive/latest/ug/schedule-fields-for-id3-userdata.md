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

| Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Action type**   | **HLS Timed Metadata**. Choose this option<br>to insert in HLS or MediaPackage outputs.**Timed<br>Metadata**. Choose this option to insert in<br>CMAF Ingest outputs.                                                                                                                                                                                                                                                                                                            |
| **Action name**   | A name for the metadata item. You might want to design a<br>convention for naming ID3 metadata items, such as<br>`id3_metadata-<UTC time>`.                                                                                                                                                                                                                                                                                                                                      |
| **Start type**    | **Fixed\*<br>• or<br>**Immediate\*\*.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Date and time** | If the **Start type\*<br>• is<br>**Fixed\*\*, specify the UTC start time<br>for the ID3 metadata item. The time should be at least 15<br>seconds in the future.<br>Note that the time is the wall clock time, not the<br>timecode in the input.                                                                                                                                                                                                                                  |
| **ID3**           | Enter the ID3 metadata encoded as base64. The metadata<br>must be fully formed ID3 metadata (including both a header<br>and a frame, as per the ID3 2.4.0 specification).<br>The content of the `value` property can include<br>MediaLive [variable<br>data](variable-data-identifiers.md "variable-data-identifiers.md"). MediaLive will examine the contents of the<br>base64 and perform substitutions. For example, MediaLive will<br>change `$dt$` to the date and<br>time. |
