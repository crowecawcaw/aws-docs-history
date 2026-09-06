

# Setting up for locking
<a name="pipeline-locking-set-up"></a>

Pipeline locking is enabled by default in a standard channel. You can disable it. If you decide to keep it enabled, you should configure the mode to use in a specific channel. And you should configure the output groups to ensure that MediaLive can successfully lock the pipelines.

**Note**  
All the procedures in this section assume that you are familiar with the general steps for creating a channel, as described [Creating a channel from scratch](creating-channel-scratch.md).

## Configuring output locking and setting the mode
<a name="pipeline-locking-mode"></a>

You can configure the channel as follows:
+ Locking disabled
+ Locking enabled in pipeline locking mode: lock the two pipelines to each other
+ Locking enabled in epoch locking mode: lock the pipelines using the Unix epoch as the reference.

**Configure the pipeline locking mode and method**

1. In the channel that you are creating or editing, in the navigation pane, choose **General settings**. Then choose **Global configuration**.

1. Choose **Enable global configuration**.

1. In **Output locking mode**, choose **DISABLED**. Or choose the mode—**PIPELINE\_LOCKING** or **EPOCH\_LOCKING**. For details about the options, choose the **Info** link next to the field. 

1. To configure the pipeline locking method (available only with **PIPELINE\_LOCKING** mode), expand **Additional settings**.

1. In **Output locking settings**, locate the **Pipeline locking method** field and choose the method for synchronization:
   + **SOURCE\_TIMECODE** (default): Uses embedded timecodes from the input source. Requires inputs with reliable embedded timecodes. See [Embedded timecode requirements (source timecode method)](pipeline-locking-verify-input.md#pipeline-locking-embedded-tcode).
   + **VIDEO\_ALIGNMENT**: Uses visual signature comparison between encoders. Does not require embedded timecodes. See [Requirements for video aligned locking](pipeline-locking-verify-input.md#pipeline-locking-video-alignment-inputs) for input compatibility.

1. (Optional) For CMAF Ingest and MediaPackage V2 output groups, you can configure a custom epoch. Expand **Additional settings**, then in **Output locking settings**, locate the **Custom epoch** field and enter a custom epoch time.

## Setting up an HLS, MediaPackage, or Microsoft Smooth output group
<a name="pipeline-locking-outputgroups"></a>

In an HLS output group or Microsoft Smooth output group, you must set up the framerate for each video encode. 

**Set up for pipeline locking**

1. In the channel that you are creating, in the navigation pane, choose the HLS or Microsoft Smooth output group. If necessary, create the outputs and video encodes in each output.

1. In each output that contains a video encode, choose the video encode. In the **Codec settings** field, choose the codec. More fields appear.

1. Choose the **Frame rate ** section and set the following fields:
   + **Framerate control**: We recommend you choose **Specified**. The option **Initialize\_from\_source** doesn't work well with pipeline locking.
   + **Framerate numerator** and **Framerate denominator**: Set the desired resolution for the output. Make sure that the conversion from input framerate to output framerate meets [the requirements](pipeline-locking-verify-input.md).

1. Repeat, to setup of the frame rate in the video encode in every output.

## Setting up a UDP output group
<a name="pipeline-locking-udp"></a>

In a UDP output group, you must obtain information about segmentation markers, and set up the segmentation markers for framerate for each video encode.

**Set up for pipeline locking**

1. You need information about the how to configure segmentation in the outputs. This information is contained in fields on the **Create channel** page on the console. To display the fields, in the navigation pane choose **Archive group**. Then choose an output and choose **Network settings**. Choose the **Info** link next to each of the following fields: 
   + **Segmentation markers**
   + **Segmentation time**
   + **EBP lookahead msec**
   + **Fragment time**
   + **Segmentation style**
   + **EBP placement**
   + **EBP audio interval**

1. Speak to your contact at the downstream system to obtain recommended values for these fields. 

1. In the channel that you are creating, in the navigation pane, choose the Archive output group. If necessary, create the outputs. Then in the **Output settings**, choose **Network settings**. More fields appear.

1. Choose **Container settings** and set values for the segmentation fields listed in step 1. It's possible that some of the fields don't apply to the segmentation markers you choose.

1. If necessary, create the video encode in the output, then choose the video encode. In the **Codec settings** field, choose the codec. More fields appear.

1. Choose the **Frame rate ** section and set the following fields:
   + **Framerate control**: We recommend you choose **Specified**. The option **Initialize\_from\_source** doesn't work well with pipeline locking.
   + **Framerate numerator** and **Framerate denominator**: Set the desired framerate for the output. Make sure that the conversion from input framerate to output framerate meets [the requirements](pipeline-locking-verify-input.md).