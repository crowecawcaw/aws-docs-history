# Miscellaneous video tuning

parameters

## Description

This section describes individual encoding parameters that provide let
you tune the video quality.

- **CABAC**: Applies only to H.264, and
  only when the **Profile** parameter is set to
  **Main** or **High**. This parameter
  enables arithmetic coding and can compress the same data with
  approximately 15% fewer bits. As a result, encoding is more efficient.
  There is no impact on video quality.

Recommendation: Always enable this parameter unless the intended
decoder or playback device doesn't support it.

- **Density vs Quality**: Applies only to
  H.264 and H.265. This parameter sets the balance between density on the
  appliance and video quality.

      + A value above **0** favors density over quality.
       This means that as you add more events to the appliance, the point will
       be reached where the encoder automatically starts to lower the video
       quality in any events that has this parameter set above 0.
      + A value below **0** favors quality over
       density.

  Note that this parameter controls density and quality, even though
  the parameter name in the XML is **svq** (speed vs
  quality).

Recommendation: On newer appliance models (L8xx and later), we
recommend that you leave the default. On older appliance models, a
different value might change the balance. However, never use
**-2** or **-3** with H.265.

- **Lookahead**: Lookahead indicates that
  the encoder should analyze a few frames into the future of the currently
  encoded frame, to allow the encoder to take future frame data into account
  during rate control logic. For example, if future frames are more complex,
  the encoder can allocate fewer bits to encode the current frame. In this
  way, the unused bits can be used to encode those future frames.

The tradeoff of a higher lookahead is that processing and latency
increase slightly, to allow the encoder to analyze those future
frames.

Recommendation: Set to **Medium** unless latency is
critical.

- **Profile**: Applies only to H.264 and
  H.265. For H.264, the profile affects video quality. For H.265, the
  profile sets various characteristics of the video.

Recommendation: With H.264, use **High
Profile** to achieve higher video quality.

- **Slices**: Applies only to H.264 and
  H.265. This parameter improves speed of encoding. Using a higher number of
  slices can improve speed optimization. However, this results in slightly
  lower video quality.

Recommendation:

Set to **Auto** so that the encoder uses a value
appropriate to the image height (resolution). The following table
specifies which value the encoder will assign when you choose
**Auto**, based on the image height.

| Height (pixels)                            | Recommendation for H.264                                                                                                                                                    | Recommendation for H.265 |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Less than 720                              | 1                                                                                                                                                                           | 1                        |
| Greater than or equal to 720               | 2                                                                                                                                                                           | 4                        |
| Greater than or equal to 1080              | 4                                                                                                                                                                           | 4                        |
| Greater than or equal to 2160              | 8                                                                                                                                                                           | 8                        | ## Location of parameters This table shows where the parameters mentioned in this section are located. The first column shows the location on the web interface. The second column shows the location in the event XML. |
| Location of parameter on web interface     | Location of tag in XML                                                                                                                                                      |                          | ---                                                                                                                                                                                                                     | ---                                                                                                                             |
| **Streams – Video > Advanced > Lookahead** | stream_assembly/video_description/`codec`/look_ahead_rate_control where `codec` is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings` |                          | **Streams – Video > Advanced > Profile**                                                                                                                                                                                | stream_assembly/video_description/h264_settings>/profile                                                                        |
| **Streams – Video > Advanced > Level**     | stream_assembly/video_description/h264_settings>/level                                                                                                                      |                          | **Streams – Video > Advanced > CABAC**                                                                                                                                                                                  | stream_assembly/video_description/h264_settings>/cabac                                                                          |
| **Streams – Video > Advanced > Slices**    | stream_assembly/video_description/`codec`/sliceswhere `codec` is one of the following: <br>• `h264_settings` <br>• `h265_settings`                                          |                          | **Streams – Video > Advanced > Density vs Quality**                                                                                                                                                                     | stream_assembly/video_description/`codec`/svqwhere `codec` is one of the following: <br>• `h264_settings` <br>• `h265_settings` |

|
