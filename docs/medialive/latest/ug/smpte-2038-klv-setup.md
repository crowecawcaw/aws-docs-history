

# Configuring outputs for KLV metadata
<a name="smpte-2038-klv-setup"></a>

You can choose to pass through the KLV metadata in specific types of output groups. You can pass through the data in one or more the output groups.

**Note**  
The information in this section assumes that you are familiar with the general steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md).

**Topics**
+ [Archive](#smpte-2038-klv-setup-archive)
+ [MediaPackage](#smpte-2038-klv-setup-emp)
+ [HLS](#smpte-2038-klv-setup-hls)
+ [UDP/TS](#smpte-2038-klv-setup-udp)

## Archive
<a name="smpte-2038-klv-setup-archive"></a>

1. On the **Create channel** page, in the **Output groups** section, in the **Archive** group, choose the output. 

1. In **Output settings**, select **Container settings**, then select **PID settings**.

1. Set these fields:
   + **KLV**: Choose **PASSTHROUGH**
   + **KLV data PIDs**: Enter the PID where you want the KLV metadata.

## MediaPackage
<a name="smpte-2038-klv-setup-emp"></a>

MediaPackage outputs are automatically set up for passthrough. If MediaLive finds KLV metadata in an input, it passes it through in a MediaPackage output, in PID 501.

## HLS
<a name="smpte-2038-klv-setup-hls"></a>

You can pass through KLV metadata in any output that has a standard HLS container (a TS container).

1. On the **Create channel** page, in the **Output groups** section, in the **HLS** group, choose the output. 

1. In **Output settings**, make sure that **HLS settings** specifies **Standard HLS**.

1. In **HLS settings**, select **PID settings**.

1. Set these fields:
   + **KLV**: Choose **PASSTHROUGH**
   + **KLV data PIDs**: Enter the PID where you want the KLV metadata.

## UDP/TS
<a name="smpte-2038-klv-setup-udp"></a>

1. On the **Create channel** page, in the **Output groups** section, in the **UDP** group, choose the output. 

1. In **Output settings**, select **Network settings**, then select **PID Settings**.

1. Set these fields:
   + **KLV**: Choose **PASSTHROUGH**
   + **KLV data PID**: Enter the PID where you want the KLV metadata.