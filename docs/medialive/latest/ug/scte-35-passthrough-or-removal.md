

# Enabling SCTE 35 passthrough or removal
<a name="scte-35-passthrough-or-removal"></a>

You can set up the MediaLive channel so that SCTE 35 messages from the input are passed through (included) in the data stream for the following outputs:
+ Outputs in an Archive output group.
+ Outputs in an HLS output group.
+ Outputs in a MediaPackage output group. For these types of output groups, passthrough is always enabled. You can't disable it.
+ Outputs in a Multiplex output group. For Multiplex output groups, SCTE 35 passthrough is enabled by default.
+ Outputs in an SRT caller output group.
+ Outputs in a UDP output group.

**Alignment with video**

The PTS of the SCTE 35 message is adjusted to match the PTS of the corresponding video frame. 

**Passthrough is at the output level**

SCTE 35 passthrough or removal applies at the output level. The messages are passed through or removed only in a specific output. For most outputs, the default behavior (if you do not change the configuration fields) is to remove the messages. For MediaPackage outputs, the default behavior is to pass through the messages; you can't change this behavior.

**Packet identifier (PID) selection from the input**

If your source contains multiple SCTE 35 PIDs, you might want to select a specific PID to pass through to the output. By default, MediaLive will select the first SCTE 35 PID that is present on the input. This can be changed by selecting a specific PID value from the **General input settings** section of the **Input attachment**. If the PID value selected is not present in the input, no SCTE 35 PID will be passed from input and an alert will be triggered.

**Topics**
+ [Enabling passthrough for Archive outputs](#procedure-to-enable-passthrough-archive)
+ [Enabling passthrough for CMAF Ingest outputs](#procedure-to-enable-passthrough-cmafi)
+ [Enabling passthrough for HLS outputs](#procedure-to-enable-passthrough-hls)
+ [Enabling passthrough for SRT caller outputs](#procedure-to-enable-passthrough-srt)
+ [Enabling passthrough for UDP outputs](#procedure-to-enable-passthrough-udp)

## Enabling passthrough for Archive outputs
<a name="procedure-to-enable-passthrough-archive"></a>

Follow this procedure if you want to enable or disable passthrough of SCTE 35 message for MediaLive Archive outputs.

**To enable passthrough**

1. In the channel that you are creating, find the **Archive** output group that contains the output that you want to set up.

1. Choose that output.

1. In **PID settings**, complete the following fields:
   + **SCTE 35 control**: Set to **Passthrough**.
   + **SCTE 35 PID**: Leave the default PID or enter the PID where you want the SCTE 35 messages to go. 

1. If appropriate, repeat for other outputs in this or other **Archive** output groups.

All SCTE 35 messages from the input are included in the data stream of the outputs that you have set up.

## Enabling passthrough for CMAF Ingest outputs
<a name="procedure-to-enable-passthrough-cmafi"></a>

Follow this procedure if you want to enable or disable passthrough of SCTE 35 message for MediaLive CMAF Ingest outputs.

**To enable passthrough**

1. In the **Create channel** or **Edit channel** page for the channel, in the **Channel** panel, find the **CMAF Ingest** output group that you want to set up. Select the output group by its name. The details appear in the right panel.

1. In **CMAF Ingest settings** section, set **SCTE35 type** to the appropriate value:
   + **NONE**: Omits the SCTE 35 messages from the output group.
   + **SCTE\_35\_WITHOUT\_SEGMENTATION**: Includes (passes through) the SCTE 35 messages in the output group.

     Each SCTE 35 message inserted will result in a new IDR in the video, but it won't result in a new segment. Note that CMAF Ingest doesn't require that SCTE 35 messages force a new segment. 

## Enabling passthrough for HLS outputs
<a name="procedure-to-enable-passthrough-hls"></a>

Follow this procedure if you want to enable or disable passthrough of SCTE 35 message for MediaLive HLS outputs.

**To enable passthrough**

1. In the channel that you are creating, find the HLS output group that contains the output that you want to set up. 

1. Choose that output.

1. In **PID settings**, complete the following fields:
   + **SCTE 35 behavior**: Set to **Passthrough**.
   + **SCTE 35 PID**: Leave the default PID or enter the PID where you want the SCTE 35 messages to go. 

1. If appropriate, repeat for other outputs in this or other HLS output groups.

All SCTE 35 messages from the input will be included in the data stream of the outputs that you have set up.

## Enabling passthrough for SRT caller outputs
<a name="procedure-to-enable-passthrough-srt"></a>

Follow this procedure if you want to enable or disable passthrough of SCTE 35 message for MediaLive SRT caller outputs.

**To enable passthrough**

1. In the channel that you are creating, find the SRT caller output group that contains the output that you want to set up. 

1. Choose that output.

1. In **PID settings**, complete the following fields:
   + **SCTE 35 control**: Set to **Passthrough**.
   + **SCTE 35 PID**: Leave the default PID or enter the PID where you want the SCTE 35 messages to go. 

All SCTE 35 messages from the input will be included in the data stream of the outputs that you have set up.

## Enabling passthrough for UDP outputs
<a name="procedure-to-enable-passthrough-udp"></a>

Follow this procedure if you want to enable or disable passthrough of SCTE 35 message for MediaLive UDP outputs.

**To enable passthrough**

1. In the channel that you are creating, find the UDP output group that contains the output that you want to set up. 

1. Choose that output.

1. In **PID settings**, complete the following fields:
   + **SCTE 35 control**: Set to **Passthrough**.
   + **SCTE 35 PID**: Leave the default PID or enter the PID where you want the SCTE 35 messages to go. 

1. If appropriate, repeat for other outputs in this or other UDP output groups.

All SCTE 35 messages from the input will be included in the data stream of the outputs that you have set up.