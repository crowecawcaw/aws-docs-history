

# Create an HLS output group
<a name="creating-hls-output-group"></a>

You create the output group and its outputs when you [create or edit a MediaLive channel](creating-a-channel-step4.md). 

## The procedure
<a name="hls-create-procedure"></a>

1. On the **Create channel** page, under **Output groups**, choose **Add**. 

1. In the **Add output group** section, choose **HLS**, and then choose **Confirm**. More sections appear:
   + **HLS group destination** – This section contains fields for the destination of the outputs. For more information see the section for the type of downstream system:
     + [Fields for the output destination – sending to Amazon S3](hls-destinations-s3.md)
     + [Fields for the output destination – sending to MediaStore](hls-destinations-ems.md)
     + [Fields for the output destination – sending to MediaPackage](hls-destinations-emp.md)
     + [Fields for the output destination – sending to an HTTP server](hls-destinations-http.md)
   + **HLS settings** – This section contains fields for the [destination of the outputs](hls-destinations-http.md), for [resiliency](hls-other-features.md#hls-resiliency), and for [captions](hls-other-features.md#hls-captions). 
   + **HLS outputs** – This section shows the single output that is added by default.
   + **Location** – This section contains fields for [customizing the paths inside the manifests](hls-manifest-paths.md).
   + **Manifest and segments** – This section contains fields for [configuring redundant manifests](hls-opg-redundant-manifest.md), for configuring the [manifest contents](hls-other-features.md#hls-manifest-contents), and for [configuring media segments](hls-other-features.md#hls-segment-fields).
   + **DRM** – This section contains fields for configuring [encryption of outputs](hls-other-features.md#hls-drm).
   + **Ad marker** – This section contains fields for setting up for [SCTE-35 ad avails](hls-other-features.md#hls-ad-markers).
   + **Captions** – This section contains fields for configuring [captions](hls-other-features.md#hls-captions).
   + **ID3** – This section contains fields for setting up for [ID3](hls-other-features.md#hls-id3).

1. If your plan includes more than one output in this output group, then in **HLS outputs**, choose **Add output** to add the appropriate number of outputs. 

1. In **HLS outputs**, choose the first **Settings** link to view the sections for the first output:
   + **Output settings** – This section contains fields for the destination of the outputs. See these sections:
     + [Fields for the output destination – sending to Amazon S3](hls-destinations-s3.md)
     + [Fields for the output destination – sending to MediaStore](hls-destinations-ems.md)
     + [Fields for the output destination – sending to MediaPackage](hls-destinations-emp.md)
     + [Fields for the output destination – sending to an HTTP server](hls-destinations-http.md)

     This section also contains fields for the [HLS container](hls-container.md).
   + **Stream settings** – This section contains fields for the [output streams](hls-streams-section.md) (the video, audio, and captions).

1. (Optional) Enter names for the output group and the outputs:
   + In **HLS settings**, for **Name**, enter a name for the output group. This name is internal to MediaLive; it doesn't appear in the output. For example, **Sports Curling**.
   + In the **HLS outputs** section for each output, for **Name**, enter a name for the output. This name is internal to MediaLive; it doesn't appear in the output. For example, **high resolution**.

1. To complete the other fields, see the topics listed after this procedure.

1. After you have finished setting up this output group and its outputs, you can create another output group (of any type), if your plan requires it. Otherwise, go to [Save the channel](creating-a-channel-step9.md).

**Topics**
+ [The procedure](#hls-create-procedure)
+ [Destination fields in an HLS output group](hls-destinations.md)
+ [Fields for the HLS container](hls-container.md)
+ [Fields for customizing the paths inside the manifests](hls-custom-manifests.md)
+ [Fields for redundant manifests](hls-opg-redundant-manifest.md)
+ [Fields for the video, audio, and captions streams (encodes)](hls-streams-section.md)
+ [Fields for other HLS features](hls-other-features.md)