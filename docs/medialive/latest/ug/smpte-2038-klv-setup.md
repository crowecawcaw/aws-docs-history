# Configuring outputs for KLV metadata

You can choose to pass through the KLV metadata in specific types of output
groups. You can pass through the data in one or more the output groups.

###### Note

The information in this section assumes that you are familiar
with the general steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

###### Topics

- [Archive](#smpte-2038-klv-setup-archive "#smpte-2038-klv-setup-archive")
- [MediaPackage](#smpte-2038-klv-setup-emp "#smpte-2038-klv-setup-emp")
- [HLS](#smpte-2038-klv-setup-hls "#smpte-2038-klv-setup-hls")
- [UDP/TS](#smpte-2038-klv-setup-udp "#smpte-2038-klv-setup-udp")

## Archive

1. On the **Create channel** page, in the
   **Output groups** section, in the
   **Archive** group, choose the output.
2. In **Output settings**, select
   **Container settings**, then select
   **PID settings**.
3. Set these fields:
   - **KLV**: Choose
     **PASSTHROUGH**
   - **KLV data PIDs**: Enter the PID
     where you want the KLV metadata.

## MediaPackage

MediaPackage outputs are automatically set up for passthrough. If
MediaLive finds KLV metadata in an input, it passes it through in a
MediaPackage output, in PID 501.

## HLS

You can pass through KLV metadata in any output that has a
standard HLS container (a TS container).

1. On the **Create channel** page, in the
   **Output groups** section, in the
   **HLS** group, choose the output.
2. In **Output settings**, make sure that
   **HLS settings** specifies
   **Standard HLS**.
3. In **HLS settings**, select **PID
   settings**.
4. Set these fields:
   - **KLV**: Choose
     **PASSTHROUGH**
   - **KLV data PIDs**: Enter the PID
     where you want the KLV metadata.

## UDP/TS

1. On the **Create channel** page, in the
   **Output groups** section, in the
   **UDP** group, choose the output.
2. In **Output settings**, select
   **Network settings**, then select
   **PID Settings**.
3. Set these fields:
   - **KLV**: Choose
     **PASSTHROUGH**
   - **KLV data PID**: Enter the PID
     where you want the KLV metadata.
