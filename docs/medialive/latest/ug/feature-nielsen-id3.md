# Converting Nielsen watermarks to ID3

If one or more inputs in a channel includes Nielsen watermarks in the audio, you have the
option of setting up the channel to convert those watermarks to ID3 metadata. These watermarks
are part of the measurement and analytics capabilities supported by Nielsen.

This option applies only in the following scenario:

- One or more inputs in your channel includes Nielsen watermarks in the audio.
- Your channel has at least one output group that can include the Nielsen ID3 tag:
  - Archive output group
  - CMAF Ingest output group
  - HLS output group. The output must be a standard output (not an audio-only output)For
    example, an HLS output group.

- You know that at least some of your playback devices implement the Nielsen SDK. This SDK
  provides functionality to handle the ID3 tags.
  Converting the watermarks to ID3 tags doesn't remove the original watermarks. Outputs where
  you include the ID3 tags will contain both the watermark and the ID3 tags. Outputs that don't
  include the ID3 tags will contain only the watermark.

You can't remove the watermarks from the audio, but if your playback devices don't implement
the Nielsen SDK, the devices simply ignore the watermarks.

###### Note

Do not confuse this feature with the ability to [insert ID3
metadata](id3-metadata.md "id3-metadata.md") in outputs.

###### To set up watermarks as ID3 tags

1. On the **Create channel** page, in the **General
   settings** section, in the **Nielsen Configuration** pane,
   choose **Enable Nielsen configuration**.
2. Set the fields as follows:
   - **Nielsen PCM to ID3 tagging**: Choose
     **ENABLED**.
   - **Distributor ID**: Optionally, enter the distributor ID that you
     obtained from Nielsen. If you enter an ID here, it is added to the ID3 metadata along
     with the source ID (SID) that is always in the source watermark.

3. Go to the output group and output where you want to include the ID3 tags..

(If the output group is **MediaPackage**, you don't have to set up the
output. The ID3 tags are always passed through, if the output is a standard output.)

| Output group    | Section                  | Instruction                                                                                                                                                                |
| --------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Archive**     | **Output settings**      | Choose **PID settings**. In **Nielsen ID3**, choose **PASSTHROUGH**.                                                                                                       |
| **CMAF Ingest** | **CMAF Ingest settings** | In **Nielsen ID3 Behavior**, choose **PASSTHROUGH**.                                                                                                                       |
| **HLS**         | **Output settings**      | The contain must be a standard HLS container. Verify the value in the **HLS Settings** field.Choose **PID settings**. In **Nielsen ID3 behavior**, choose **PASSTHROUGH**. |
| **UDP**         | **Output settings**      | Choose **Network settings**, then choose **PID settings**. In **Nielsen ID3**, choose **PASSTHROUGH**.                                                                     |
