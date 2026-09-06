

# Fields for other Microsoft Smooth features
<a name="mss-other-fields"></a>

## Fields for resiliency
<a name="smooth-resiliency"></a>

The following field relates to implementing resiliency in a Microsoft Smooth output. 
+ **Microsoft Smooth output group** – **Microsoft Smooth Settings** section – **General configuration** section – **Input loss action**

Optionally change the value of **Input loss action**. 

Choose the **Info** link in the MediaLive console to decide which option to choose. For more information, see [Handling loss of video input](feature-input-loss.md).

## Fields for timecode
<a name="smooth-timecode"></a>

The following fields relate to configuring the timecode and timestamp in all the outputs in the output group. 
+ **Microsoft Smooth output group** – **Timecode Configuration** section 

For details about a field, choose the **Info** link next to the field in the MediaLive console.

## Fields for SCTE-35
<a name="smooth-s35"></a>

The following fields relate to configuring the timecode and timestamp in all the outputs in the output group. 
+ **Microsoft Smooth output group** – **Timecode Configuration** section 

If you want all the outputs in this output group to include the SCTE-35 messages that are already present in the input, choose **Sparse track**. The messages will be included in a sparse track. For more information, see [Processing SCTE 35 messages](scte-35-message-processing.md) and specifically [Enabling decoration – Microsoft Smooth](procedure-to-enable-decoration-ms-smooth.md).