# Inserting ID3 metadata using the

schedule

You can create actions in the channel schedule to insert ID3 metadata in one or more
outputs. There are two types of ID3 metadata actions:

- Timed metadata, to insert metadata once, at a specified time.
- ID3 segment tag action: To insert metadata in every segment. There are two options for
  this action — tag option and ID3 option. For more information, see the table below.

## Supported output groups

The following table specifies which output groups support inserting metadata using the
schedule, and which schedule mechanisms each output group supports. Find the mechanism in
the first column, then read across the row.

| Mechanism                                                 | CMAF Ingest | HLS TS    | HLS MP4   | HLS audio-only | MediaPackage |
| --------------------------------------------------------- | ----------- | --------- | --------- | -------------- | ------------ |
| One-time insertion, using the schedule                    | Supported   | Supported | Supported |                | Supported    |
| Segment insertion with the tag option, using the schedule | Supported   | Supported | Supported | Supported      | Supported    |
| Segment insertion with the ID3 option, using the schedule | Supported   |           |           | Supported      |              |

## Comparison of different schedule

actions

This table describes the main differences between the three mechanisms for inserting ID3
metadata using the schedule. Find the mechanism in the first column, then read across the
row.

| Mechanism                                | One time or repeat?                                                                                                                                                                                          | You provide plain text or base64?                                                                                                                      | Which frame type?              |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| ID3 timed metadata                       | One-time<br>At the start time of the action, MediaLive inserts the ID3 metadata in the<br>applicable outputs, as a one-time event.                                                                           | Base64<br>You provide a fully formed ID3 metadata item (including both a header and a<br>frame, as per the ID3 specification) and encode it as base64. | A frame type that you specify. |
| ID3 segment tags that use the tag option | RepeatAt the start time of the action, MediaLive starts inserting ID3 tags in<br>every segment in the applicable outputs. It continues to insert in every segment,<br>typically for the life of the channel. | Clear text<br>You provide only the value for the TXXX field inside the ID3 tag. You specify<br>this value as clear text.                               | A TXXX                         |
| ID3 segment tags that use the ID3 option | RepeatAt the start time of the action, MediaLive starts inserting ID3 tags in<br>every segment in the applicable outputs. It continues to insert in every segment,<br>typically for the life of the channel. | Base64<br>You provide a fully formed ID3 metadata item (including both a header and a<br>frame, as per the ID3 specification) and encode it as base64. | A frame type that you specify. |

## Step 1: Set up for insertion

Before you can insert ID3 metadata using the schedule, you must enable ID3 metadata
insertion in the appropriate output groups.

###### Note

This section assumes that you are familiar with creating or editing a channel, as
described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

### Inserting in CMAF Ingest

outputs

1. Display the **Create channel** or **Edit
   channel** page, then select the CMAF Ingest output group that you want to
   set up.
2. Set **ID3 Behavior**: Select **ENABLED**.

### Inserting in HLS TS outputs

1. Display the **Create channel** or **Edit
   channel** page, then select the output group where you want to enable ID3
   metadata.
2. Complete this step only if you plan to insert segments using the tag option. In
   the output group section, scroll down and expand the **ID3** section.
   Complete the following field:
   - **HLS ID3 segment tagging**: Set to
     **ENABLED**.

3. Select the output where you want to include ID3 metadata. Go to
   **Container Settings**, then **PID Settings**.
   Complete the following fields:
   - **Timed Metadata Behavior**: Select
     **PASSTHROUGH**.
   - **Timed Metadata PIDs**: Enter the PID where you want to
     insert the ID3 metadata in this output. Or leave empty to use the default, which
     is PID 502.

### Inserting in HLS MP4

outputs

1. Display the **Create channel** or **Edit
   channel** page, then select the output group where you want to enable ID3
   metadata.
2. Complete this step only if you plan to insert segments using the tag option. In
   the output group section, scroll down and expand the **ID3** section.
   Complete the following field:
   - **HLS ID3 segment tagging**: Set to
     **ENABLED**.

3. Select the output where you want to include ID3 metadata. Set the following
   field:
   - **Timed Metadata Behavior**: Select
     **PASSTHROUGH**.

Note that with an MP4 output, the metadata will be inserted in the emsg. You don't
need to configure this information.

### Inserting in HLS audio-only

outputs

1. Display the **Create channel** or **Edit
   channel** page, then select the output group where you want to enable ID3
   metadata.
2. In the output group section, scroll down and expand the **ID3**
   section. Complete the following field:
   - **HLS ID3 segment tagging**: Set to
     **ENABLED**.

### Inserting in MediaPackage

outputs

You don't need to enable insertion in MediaPackage outputs because ID3 metadata is
enabled by default. This default behavior includes insertion of metadata using the
schedule. MediaLive inserts the metadata in PID 502.

## Step 2: Create actions in the

schedule

After you have enabled ID3 metadata insertion in the appropriate output groups, you can
create actions in the schedule.

You can create actions at any time — before starting the channel or when the channel is
running. When the channel is running, MediaLive starts to insert the tag content specified in
the action or actions. The same content is inserted in all the outputs where you have
enabled insertion.

For more information, see the following:

- [How ID3 metadata actions work](x-actions-in-schedule-id3.md "x-actions-in-schedule-id3.md")
- [How ID3
  segment tag actions work](x-actions-in-schedule-id3-segment-tag.md "x-actions-in-schedule-id3-segment-tag.md")
