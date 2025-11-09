# Passing through ID3 metadata

You can set up one or more outputs in a MediaLive channel so that ID3 metadata that is in a
source is automatically passed through to the output. Passthrough is supported in the
following types of output groups:

- Archive
- CMAF Ingest
- HLS TS
- HLS MP4
- MediaPackage
- UDP.
  Metadata is passed through according to the following rules about the source
  content.

| Type of frame     | Content of the source metadata                                           | Result                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Not PRIV and TDRL | Any content                                                              | Pass through in enabled outputs.                                                                                       |
| PRIV and TDRL     | The frame doesn't have "Elemental Technologies" included in the wording. | Pass through in enabled outputs.                                                                                       |
| PRIV and TDRL     | The frame does have "Elemental Technologies" included in the wording.    | Don't pass through. MediaLive assumes that the timestamp for this metadata has<br>passed, so the metadata isn't valid. |

###### Note

All the following procedures assume that you are familiar with creating or editing a
channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

## Passing through ID3 metadata in Archive

outputs

You must configure each output where you want the ID3 metadata to appear.

1. Display the **Create channel** or **Edit channel**
   page, then select the **Archive** output group.
2. Select the output where you want to include ID3 metadata. Select **Container
   Settings**, then **PID Settings**.
3. Complete the following fields:
   - **Timed Metadata Behavior**: Select
     **PASSTHROUGH**.
   - **Timed Metadata PIDs**: Enter the PID where you want to insert
     the ID3 metadata in this output. Or leave empty to use the default, which is PID
   502.

## Passing through ID3 metadata in CMAF Ingest

outputs

You must configure each output group where you want the ID3 metadata to appear.

1. Display the **Create channel** or **Edit channel**
   page and select the CMAF Ingest output group that you want to set up.
2. Set **ID3 Behavior**: Select **ENABLED**.
3. Go to **Additional Settings**. Set the following field:
   - **Timed Metadata Behavior**: Set to
     **ENABLED**.

## Passing through ID3 metadata in HLS TS

outputs

Follow this procedure for an HLS output that is set up with a standard container, which
holds a transport stream. You must configure each output where you want the ID3 metadata to
appear.

1. Display the **Create channel** or **Edit channel**
   page, then select the **HLS** output group.
2. Select the output where you want to include ID3 metadata. Go to **Container
   Settings**, then **PID Settings**.
3. Complete the following fields:
   - **Timed Metadata Behavior**: Select
     **PASSTHROUGH**.
   - **Timed Metadata PIDs**: Enter the PID where you want to insert
     the ID3 metadata in this output. Or leave empty to use the default, which is PID
   502.

## Passing through ID3 metadata in HLS MP4

outputs

Follow this procedure for an HLS output that is set up with an fMP4container. You must
configure each output where you want the ID3 metadata to appear. The metadata will be
included in the emsg event.

1. Display the **Create channel** or **Edit channel**
   page, then select the **HLS** output group.
2. Select the output where you want to include ID3 metadata. Set the following
   field:
   - **Timed Metadata Behavior**: Select
     **PASSTHROUGH**.

## Passing through ID3 metadata in

MediaPackage outputs

You don't have to perform any setup in MediaPackage outputs. These outputs are
automatically set up to pass through any ID3 metadata that is present in the source.

## Passing through ID3 metadata in UDP outputs

You must configure each output where you want the ID3 metadata to appear.

1. Display the **Create channel** or **Edit channel**
   page, then select the **UDP** output group.
2. Select the output where you want to include ID3 metadata. Go to **Network
   Settings**, then **PID Settings**.
3. Complete the following fields:
   - **Timed Metadata Behavior**: Select
     **PASSTHROUGH**.
   - **Timed Metadata PIDs**: Enter the PID where you want to insert
     the ID3 metadata in this output. Or leave empty to use the default, which is PID
   502.
