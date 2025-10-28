# Frame rate conversion

## Description

Framerate conversion is typically used when producing content for
devices that use different standards (for example, NTSC vs. PAL), or
different content playback scenarios (for example, film at 24 fps vs.
television at 29.97 fps). You can set the frame rate for the video output to
a value that suits your workflow requirements. You can choose a standard
frame rate, such as 29.97. Or you can define a custom rate.

When you set the frame rate, consider the following related
parameters:

- The scan type for the output – interlaced or progressive. The choice
  of frame rate might be constrained by the scan type conversion you apply.
  For more information, see [Converting the scan type](vq-scan-type.md "vq-scan-type.md").
- Interpolation. The **Interpolated**
  parameter has values to favor sharpness or smoothness:

      + If **Interpolated** is disabled, the encoder
       drops or repeats frames, as needed. This results in sharp individual
       frames.
      + If **Interpolated** is enabled, a weighted average
       is applied between frames when new frames need to be added as part of
       the frame rate conversion. This results in smoother motion. For example,
       when converting from a 24 fps input to 29.97 fps output, the encoder
       uses an algorithm to average the 4th and 5th frames of the source
       content. this produces the additional frame that's needed in the output.

  Recommendation: Enable the **Interpolated** parameter if input and output frame rates are
  close. For example, 24 fps inputs to 25 fps outputs.

## Location of

parameters

This table shows where the parameters mentioned in this section are
located. The first column shows the location on the web interface. The
second column shows the location in the event XML.

| Location of parameter on web interface               | Location of tag in XML                                                                                                                                                                                                                                          |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stream – Video** > **Advanced** > **Framerate**    | stream_assembly/video_description/`codec`/framerate_numerator stream_assembly/video_description/`codec`/framerate_denominator where `codec` is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings` <br>• `prores_settings` |
| **Stream – Video** > **Advanced** > **Interpolated** | stream_assembly/video_description/`codec`/interpolate_frc where `codec` is: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings` <br>• `prores_settings`                                                                                          |
