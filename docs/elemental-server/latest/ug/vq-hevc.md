

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Encoding – HEVC (H.265) Controls
<a name="vq-hevc"></a>

## Description
<a name="description-hevc"></a>

The following HEVC-specific control can affect video quality:
+ **Slices**: This control improves speed of encoding. Using a higher number of slices can improve speed optimization but results in slightly less quality. 

## Recommendations
<a name="vq-hevc-recommendations"></a>

The AWS Elemental HEVC encoder performance is less sensitive to changes in slices than the MPEG-4 AVC encoder ([Encoding – MPEG-4 AVC (H.264) Controls](vq-avc.md)), so the benefit of using more slices is reduced and having more slices reduces video quality. For these reasons, the recommendation is to use half as many slices with HEVC as with MPEG-4 AVC for the same resolution. In other words, set **Slices** to 2 (or higher) for all 1080p (or above) resolution outputs or high bitrate outputs. Set Slices to 1 for Resolutions below 1080p . 

## Location of Fields
<a name="vq-hevc-api"></a>


| Location of Field on Web Interface | Location of Tag in XML | 
| --- | --- | 
| Streams – Video > Advanced > Profile | stream\_assembly/video\_description/h265\_settings>/cabac | 
| Streams – Video > Advanced > Slices | stream\_assembly/video\_description/h265\_settings/slices | 