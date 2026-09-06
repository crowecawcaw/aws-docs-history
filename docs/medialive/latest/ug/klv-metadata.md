

# Working with KLV metadata
<a name="klv-metadata"></a>

You can configure MediaLive to pass through KLV metadata in TS outputs. The metadata must be compliant with SMPTE 336M-2007.

In an input, KLV metadata might be contained in a SMPTE 2038 stream or in a PID in a transport stream:
+ If the KLV metadata is in a SMPTE 2038 stream in a specific input, you must configure the input to extract it. See [Handling SMPTE 2038 metadata](smpte-2038.md).
+ If the KLV metadata is in a PID, read the topics that follow.

Note that if an AWS Elemental Link device is the input, the KLV metadata is always in a SMPTE 2038 stream. Therefore, read the [SMPTE 2038 section.](smpte-2038.md) 

**Topics**
+ [Configuring inputs](#klv-metadata-input)
+ [Configuring outputs](#klv-metadata-setup)

## Configuring inputs
<a name="klv-metadata-input"></a>

When MediaLive ingests an input that contains a TS source, it automatically extracts KLV metadata that it finds. You don't need to configure the input.

## Configuring outputs
<a name="klv-metadata-setup"></a>

You can choose to pass through the KLV metadata in one or more of the following output groups.

**Note**  
The information in this section assumes that you are familiar with the general steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md).

### Archive
<a name="klv-metadata-setup-archive"></a>

1. On the **Create channel** page, in the **Output groups** section, in the **Archive** group, choose the output. 

1. In **Output settings**, select **Container settings**, then select **PID settings**.

1. Set these fields:
   + **KLV**: Choose **PASSTHROUGH**
   + **KLV data PIDs**: Enter the PID where you want the KLV metadata.

### MediaPackage
<a name="klv-metadata-setup-emp"></a>

MediaPackage outputs are automatically set up for passthrough. If MediaLive finds KLV metadata in an input, it passes it through in a MediaPackage output, in PID 501.

### HLS
<a name="klv-metadata-setup-hls"></a>

You can pass through KLV metadata in any output that has a standard HLS container (a TS container).

1. On the **Create channel** page, in the **Output groups** section, in the **HLS** group, choose the output. 

1. In **Output settings**, make sure that **HLS settings** specifies **Standard HLS**.

1. In **HLS settings**, select **PID settings**.

1. Set these fields:
   + **KLV**: Choose **PASSTHROUGH**
   + **KLV data PIDs**: Enter the PID where you want the KLV metadata.

### UDP/TS
<a name="klv-metadata-setup-udp"></a>

1. On the **Create channel** page, in the **Output groups** section, in the **UDP** group, choose the output. 

1. In **Output settings**, select **Network settings**, then select **PID Settings**.

1. Set these fields:
   + **KLV**: Choose **PASSTHROUGH**
   + **KLV data PID**: Enter the PID where you want the KLV metadata.