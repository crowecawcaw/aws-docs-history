

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Image Processing – framerate Conversion
<a name="vq-framerate-conversion"></a>

## Description
<a name="description-vq-framerate"></a>

framerate conversion is typically used when producing content for devices that use different standards (e.g. NTSC vs. PAL) or different content playback scenarios (e.g. film at 24 fps vs. television at 25 fps or 29.97 fps). There are a few different encoding settings that can be adjusted when performing framerate conversion:
+  **framerate**: Defines the framerate of the output. The AWS Elemental system has some common built-in settings, but you can define custom settings. 
+ **Interpolated**: If Interpolated is disabled, the AWS Elemental engine drops or repeats frames as needed. This results in sharp individual frames. If Interpolated is enabled, a weighted average is applied between frames when “new” frames need to be added. This results in smoother motion. For example, when converting from a 24 fps input to 29.97 fps output, the AWS Elemental system uses an algorithm to average the 4th and 5th frames of the source content to produce the additional frame needed in the output. 
+ **Slow PAL**: This field appears only when framerate specifies 25 and applies when you are converting content from 23.976 fps to 25 fps frame rates. Slow PAL may be used to re-label the content as 25 fps and speed up the audio to compensate for the slower playback. 

## Recommendations
<a name="vq-framerate-conversion-recommendations"></a>
+ If possible, try to avoid framerate conversion if you want to provide the best video quality. However, given workflow requirements or playback devices, it may not always be possible to avoid framerate conversion. 
+ Enable **Interpolation** if input and output frame rates are close (e.g. 24 fps inputs to 25 fps outputs). 

## Location of Fields
<a name="vq-framerate-conversion-api"></a>


| Location of Field on Web Interface | Location of Tag in XML | 
| --- | --- | 
| Stream – Video > Advanced > Framerate | stream\_assembly/video\_description/{{codec}}/framerate\_numerator<br />stream\_assembly/video\_description/{{codec}}/framerate\_denominator<br />where {{codec}} is one of the following:+ **h264\_settings**<br />+ **vc1\_settings**<br />+ **mpeg2\_settings**<br />+ **h265\_settings**<br />+ **prores\_settings** | 
| Stream – Video > Advanced > Interpolated | stream\_assembly/video\_description/{{codec}}/interpolate\_frc<br />where {{codec}} is:+ **h264\_settings**<br />+ **vc1\_settings**<br />+ **mpeg2\_settings**<br />+  **h265\_settings**<br />+  **prores\_settings** | 
| Stream – Video > Advanced > Slow PAL | stream\_assembly/video\_description/{{codec}}/slow\_pal<br />where {{codec}} is:+ **h264\_settings**<br />+  **vc1\_settings**<br />+ **mpeg2\_settings**<br />+ **h265\_settings**<br />+ **prores\_settings** | 