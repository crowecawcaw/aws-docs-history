

# Create an RTMP output group
<a name="creating-rtmp-output-group"></a>

When you [planned the workflow for your channel](identify-downstream-system.md), you might have determined that you want to include an RTMP output group.

1. On the **Create channel** page, under **Output groups**, choose **Add**. 

1. In the **Add output group** section, choose **RTMP**, and then choose **Confirm**. More sections appear: 
   + **RTMP settings** – This section contains fields for the [connection configuration](rtmp-connection.md), for [resiliency](rtmp-other.md), and for [captions](rtmp-other.md). 
   + **RTMP outputs** – This section shows the single output that is added by default. An RTMP output can contain only one output, so don't click **Add output**. 

1. In **RTMP outputs**, choose the **Settings** link to view the sections for the output:
   + **RTMP destination** – This section contains fields for the [output destination](rtmp-destinations.md). 
   + **Output settings** – This section contains fields for the [connection configuration](rtmp-connection.md). 
   + **Stream settings** – This section contains fields for the [output streams](rtmp-streams.md) (the video, audio, and captions).

1. (Optional) Enter names for the output group and the output:
   + In **RTMP settings**, for **Name**, enter a name for the output group. This name is internal to MediaLive; it doesn't appear in the output. For example, **Sports Game**.
   + In **RTMP output**, in **Output settings**, for **Output name**, enter a name for the output. This name is internal to MediaLive; it doesn't appear in the output.

1. To complete the other fields, see the topics listed after this procedure.

1. After you have finished setting up this output group and its single output, you can create another output group (of any type), if your plan requires it. Otherwise, go to [Save the channel](creating-a-channel-step9.md).

**Topics**
+ [Fields for the output destination](rtmp-destinations.md)
+ [Fields for the RTMP connection](rtmp-connection.md)
+ [Fields for the video, Audio, and captions streams (encodes)](rtmp-streams.md)
+ [Other fields](rtmp-other.md)