

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Encoding – Rate Control
<a name="vq-rate-control"></a>

## Description
<a name="description-vq-rate-control"></a>

 For AWS Elemental encoding, a buffer model (such as VBV or HRD) is used to manage rate control. The buffer model is a conceptual model for specifying both short-term and long-term constraints on encoding stream bitrates. The concept is that bits flow into the buffer at a fixed rate and picture are extracted instantaneously. In a "compliant" stream, the buffer cannot overflow or underflow. The following are several settings that allow the user to adjust the rate control settings tied to this buffer model: 
+ ** Bitrate**: Defines the long-term average bitrate, in bits/second. This field does not appear when Rate Control Mode is set to CQ. 
+ **Buffer Size**: Defines the total buffer size in bits. 
+ **Max Bitrate**: Defines the buffer fill rate, in bits/second. This field appears only when Rate Control Mode is set to VBR or Statmux.
+ **Initial Buffer Fill**: Defines the percentage of the buffer filled with bits before the decode begins. 

These fields work with the Rate Control Mode field, which is discussed in [Encoding – Rate Control Modes](vq-rate-control-modes.md).

## Recommendations
<a name="vq-rate-control-recommendations"></a>
+  For **Bitrate**, more is better. The value used will depend more on other workflow constraints and will likely be different for each application. 
+ In general, **Buffer Size **is commonly set to 1x to 2x the bitrate (again, more is typically better). 
+ **Max Bitrate** is commonly set to 1x to 2x the bitrate. Although more is typically better, this value must also fit within the other encoding requirements of your specific application. 
+ For **Initial Buffer Fill**, the default value (90%) typically provides the best video quality, so leave it blank to use the default. 

## Location of Fields
<a name="vq-rate-control-api"></a>


| Location of Field on Web Interface | Location of Tag in XML | 
| --- | --- | 
| Streams – Video > Advanced > Bitrate | stream\_assembly/video\_description/{{codec}}/bitrate<br />where {{codec}} is one of the following:+  **h264\_settings** <br />+  **vc1\_settings** <br />+  **mpeg2\_settings** <br />+  **h265\_settings**  | 
|  <br />Streams – Video > Advanced > Buffer Size | stream\_assembly/video\_description/{{codec}}/buf\_size<br />where {{codec}} is one of the following:+  **h264\_settings** <br />+  **vc1\_settings** <br />+  **mpeg2\_settings** <br />+  **h265\_settings**  | 
| Streams – Video > Advanced > Max Bitrate | stream\_assembly/video\_description/{{codec}}/max\_bitrate<br />where {{codec}} is one of the following:+  **h264\_settings** <br />+  **vc1\_settings** <br />+  **mpeg2\_settings** <br />+  **h265\_settings**  | 
| Streams – Video > Advanced > Initial Buffer Fill | stream\_assembly/video\_description/{{codec}}/buf\_fill\_pct<br />where {{codec}} is one of the following:+  **h264\_settings** <br />+  **vc1\_settings** <br />+  **mpeg2\_settings** <br />+  **h265\_settings**  | 