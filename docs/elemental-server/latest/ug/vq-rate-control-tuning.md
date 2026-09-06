

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Encoding – Rate Control Tuning
<a name="vq-rate-control-tuning"></a>

## Description
<a name="description-vq-rc-tuning"></a>

 Following are encoding settings that can be used to provide additional tuning of video quality. 
+  **Passes**: When this field is set to 2-pass and **Rate Control Mode** is set to CBR, VBR, or ABR, the system analyzes the entire source video stream before encoding in order to better distribute bits to more- or less-complex portions of the video. The tradeoff is that encoding time is increased as the system needs to decode/analyze the source stream prior to starting the encode process. 
+ **Lookahead**: This setting indicates the system should analyze a few frames in the future of the currently encoded frame (higher values mean more frames) and allow the encoder to take future frame data into account during rate control logic. 

  For example, if future frames are more complex, the encoder can allocate fewer bits to encode the current frame to allow those bits to be used to encode those future frames. The tradeoff is that processing and latency are increased slightly to allow those future frames to be analyzed by the encoding engine. 

## Recommendations
<a name="vq-rc-tuning-recommendations"></a>
+ Use 2-pass encoding for VOD unless minimize encoding time is critical. 
+ Set **Lookahead** to "medium" for use with 1-pass encoding unless latency is critical. 

## Location of Fields
<a name="vq-rc-tuning-api"></a>


| Location of Field on Web Interface | Location of Tag in XML | 
| --- | --- | 
| Streams – Video > Advanced > Passes | stream\_assembly/video\_description/{{codec}}/passes<br />where {{codec}} is one of the following:+  **h264\_settings** <br />+  **vc1\_settings** <br />+  **mpeg2\_settings** <br />+  **h265\_settings**  | 
| Streams – Video > Advanced > Lookahead | stream\_assembly/video\_description/{{codec}}/look\_ahead\_rate\_control<br />where {{codec}} is one of the following:+  **h264\_settings** <br />+  **vc1\_settings** <br />+  **mpeg2\_settings** <br />+  **h265\_settings**  | 