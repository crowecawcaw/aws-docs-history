This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Image Processing – framerate Conversion

## Description

framerate conversion is typically used when producing content for devices that use
different standards (e.g. NTSC vs. PAL) or different content playback scenarios (e.g. film at
24 fps vs. television at 25 fps or 29.97 fps). There are a few different encoding settings that
can be adjusted when performing framerate conversion:

- **framerate**: Defines the framerate of the output. The AWS Elemental system has some common built-in settings, but you can define custom settings.
- **Interpolated**: If Interpolated is disabled, the AWS Elemental engine drops or repeats frames as needed. This results in sharp individual frames.
  If Interpolated is enabled, a weighted average is applied between frames when “new” frames
  need to be added. This results in smoother motion. For example, when converting from a 24 fps
  input to 29.97 fps output, the AWS Elemental system uses an algorithm to average the 4th and
  5th frames of the source content to produce the additional frame needed in the output.
- **Slow PAL**: This field appears only when framerate
  specifies 25 and applies when you are converting content from 23.976 fps to 25 fps frame
  rates. Slow PAL may be used to re-label the content as 25 fps and speed up the audio to
  compensate for the slower playback.

## Recommendations

- If possible, try to avoid framerate conversion if you want to provide the best video
  quality. However, given workflow requirements or playback devices, it may not always be
  possible to avoid framerate conversion.
- Enable **Interpolation** if input and output frame rates
  are close (e.g. 24 fps inputs to 25 fps outputs).

## Location of Fields

| Location of Field on Web Interface       | Location of Tag in XML                                                                                                                                                                                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Stream – Video > Advanced > Framerate    | stream_assembly/video_description/`codec`/framerate_numerator stream_assembly/video_description/`codec`/framerate_denominator where `codec` is one of the following: <br>• `h264_settings` <br>• `vc1_settings` <br>• `mpeg2_settings` <br>• `h265_settings` <br>• `prores_settings` |
| Stream – Video > Advanced > Interpolated | stream_assembly/video_description/`codec`/interpolate_frc where `codec` is: <br>• `h264_settings` <br>• `vc1_settings` <br>• `mpeg2_settings` <br>• `h265_settings` <br>• `prores_settings`                                                                                          |
| Stream – Video > Advanced > Slow PAL     | stream_assembly/video_description/`codec`/slow_pal where `codec` is: <br>• `h264_settings` <br>• `vc1_settings` <br>• `mpeg2_settings` <br>• `h265_settings` <br>• `prores_settings`                                                                                                 |
