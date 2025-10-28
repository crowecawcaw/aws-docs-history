# Inserting ID3 timed metadata when creating the MediaLive

channel

When you create or edit the channel, you can set up the following types of output groups
so that MediaLive inserts a timestamp at a regular interval.

- CMAF Ingest
- HLS TS
- HLS MP4
- HLS audio-only
- UDP.
  With this mechanism, MediaLive inserts the first ID3 metadata shortly after the output starts
  and then at the specified interval for as long as the channel is running. If you restart the
  channel, the insertion restarts.

###### Note

This section assumes that you are familiar with creating or editing a channel, as
described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

## Inserting in CMAF Ingest outputs

Follow this procedure for a CMAF Ingest output group.

1. Display the **Create channel** or **Edit channel**
   page, then select the CMAF Ingest output group that you want to set up.
2. Set **ID3 Behavior**: Select **ENABLED**.
3. Go to **Additional Settings**. Set the following fields:
   - **Timed Metadata Behavior**: Set to
     **ENABLED**.
   - **Timed Metadata ID3 Frame**: Select **PRIV**
     or **TDRL**
   - **Timed metadata ID3 period**: Specify the frequency for the
     metadata, in seconds.

## Inserting in HLS TS outputs

Follow this procedure for an HLS output that is set up with Standard containers (which
always contain a transport stream).

1. Display the **Create channel** or **Edit channel**
   page, then select the HLS output group that you want to set up. Scroll down and expand
   the **ID3** section.
2. Complete the following fields:
   - **Timed metadata ID3 frame**: Select the type of frame for the
     output — **PRIV** or **TDRL**.
   - **Timed metadata ID3 period**: Specify the frequency for the
     metadata, in seconds.

   We recommend that you set the period to half the segment length. To verify the
   segment length, in the **HLS output group**, expand the
   **Manifests and Segments** section, and look at **Segment
   Length**.

3. If you haven't already enabled ID3 metadata insertion in the output or outputs, do
   so now: Select the output where you want to include ID3 metadata. Select
   **Container Settings**, then **PID
   Settings**.
4. Complete the following fields:
   - **Timed Metadata Behavior**: Select
     **PASSTHROUGH**.
   - **Timed Metadata PIDs**: Enter the PID where you want to insert
     the ID3 metadata in this output. Or leave empty to use the default, which is PID
   502.

## Inserting in HLS MP4 outputs

Follow this procedure for an HLS output group that is set up with fMP4 containers. The
metadata will be included in the emsg event.

1. Display the **Create channel** or **Edit channel**
   page, then select the HLS output group that you want to set up. Scroll down and expand
   the **ID3** section. Complete the following fields:
   - **Timed metadata ID3 frame**: Select the type of frame for the
     output — **PRIV** or **TDRL**.
   - **Timed metadata ID3 period**: Specify the frequency for the
     metadata, in seconds.

   We recommend that you set the period (interval) to half the segment length. To
   verify the segment length, in the **HLS output group**, expand the
   **Manifests and Segments** section, and look at **Segment
   Length**.

2. If you haven't already enabled ID3 metadata insertion in the output or outputs, do
   so now: Select the output where you want to include ID3 metadata, and set the following
   field:
   - **Timed Metadata Behavior**: Select
     **PASSTHROUGH**.

## Inserting in HLS audio-only outputs

Follow this procedure for an HLS audio-only output group . The metadata will be
included in the emsg event.

1. Display the **Create channel** or **Edit channel**
   page, then select the HLS output group that you want to set up. Scroll down and expand
   the **ID3** section. Complete the following fields:
   - **Timed metadata ID3 frame**: Select the type of frame for the
     output — **PRIV** or **TDRL**.
   - **Timed metadata ID3 period**: Specify the frequency for the
     metadata, in seconds.

   We recommend that you set the period (interval) to half the segment length. To
   verify the segment length, in the **HLS output group**, expand the
   **Manifests and Segments** section, and look at **Segment
   Length**.

2. If you haven't already enabled ID3 metadata insertion in the output or outputs, do
   so now: Select the output where you want to include ID3 metadata. Set the following
   field:
   - **Timed Metadata Behavior**: Select
     **PASSTHROUGH**.

## Inserting in UDP outputs

Follow this procedure for a UDP output.

1. Display the **Create channel** or **Edit channel**
   page, then select the UDP output group you want to set up. Scroll down to the
   **UDP settings** section. Complete the following fields:
   - **Timed metadata ID3 frame type**: Select the type of frame for
     the output — **PRIV** or **TDRL**.
   - **Timed metadata ID3 period**: Specify the frequency for the
     metadata, in seconds.

2. If you haven't already enabled ID3 metadata insertion in the output or outputs, do
   so now: Select the output where you want to include ID3 metadata.
3. Go to **Network Settings**, then **PID Settings**.
4. Complete the following fields:
   - **Timed Metadata Behavior**: Select
     **PASSTHROUGH**.
   - **Timed Metadata PIDs**: Enter the PID where you want to insert
     the ID3 metadata in this output. Or leave empty to use the default, which is PID
   502.
