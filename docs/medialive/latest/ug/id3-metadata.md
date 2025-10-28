# Working with ID3 metadata

In MediaLive, you can include ID3 metadata in the following types of output groups:

- Archive
- CMAF Ingest
- HLS TS (transport stream)
- HLS MP4
- HLS audio-only. This is an [HLS MP4 output group that contains
  only audio encodes](audio-only.md "audio-only.md").
- MediaPackage
- UDP.
  The metadata is associated with individual outputs within the output group. You have control
  over the individual output where you want to include it. Typically, you include the metadata in
  an output if you know that a downstream system expects the metadata and is capable of
  interpreting it. You should obtain the requirements for ID3 metadata from a representative of
  the downstream system.

###### Topics

- [Different mechanisms for including metadata](id3-enable-result.md "id3-enable-result.md")
- [Passing through ID3 metadata](enable-passthrough-id3.md "enable-passthrough-id3.md")
- [Inserting ID3 timed metadata when creating the MediaLive
  channel](insert-timed-metadata.md "insert-timed-metadata.md")
- [Inserting ID3 metadata using the
  schedule](insert-id3-metadata-via-schedule.md "insert-id3-metadata-via-schedule.md")

###### Topics

- [Passing through ID3 metadata](enable-passthrough-id3.md "enable-passthrough-id3.md")
- [Inserting ID3 timed metadata when creating the MediaLive
  channel](insert-timed-metadata.md "insert-timed-metadata.md")
- [Inserting ID3 metadata using the
  schedule](insert-id3-metadata-via-schedule.md "insert-id3-metadata-via-schedule.md")
