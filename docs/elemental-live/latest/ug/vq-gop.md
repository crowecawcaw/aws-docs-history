# Group of pictures (GOP) configuration

## Description

GOP parameters define the basic pattern of the video stream in terms of
how the encoder uses I-, P-, and B- frames.

The parameters that control the GOP structure are the following:

- **GOP Mode**: Choose
  **Fixed**.

Recommendation: Always choose **Fixed**. The
**Follow** mode is obsolete and is not recommended.

- **GOP Size**: Defines the interval
  between I-frames.

Recommendation: When using MPEG-2, the recommended GOP size is up to 30. A size of 15 is also common.

For H.264, the recommendation is to make the GOP size as large as
possible while still meeting other encoding requirements. For example, for
adaptive bitrate delivery in which a segment size of 6 seconds is used for
29.97 fps outputs, the largest GOP size should be 180 frames.

- **B-Frames**: Defines the maximum run of
  B-frames. Note that the encoder might sometimes decide to use a smaller
  run of B- frames within the GOP. It usually does this to produce higher
  video quality.

Recommendation: When using H.264 or H.265, enable **GOP Reference B-Frame** to obtain the best quality
and set B-frames to a value from 3 to 5 (3 is recommended).

For other codecs, there is no quality benefit to setting the B-frames
to more than 2. For high-motion content, use 0 or 1 to produce the best
quality.

- **Closed GOP Cadence**: Defines the
  number of GOPs across which P- or B-frames are allowed to predict for
  encoding purposes.

Recommendation: Set the parameter to **1** for
segmented outputs such as adaptive bitrate content in HLS or DASH
outputs,

Set the parameter to **0** for non-segmented
outputs, to allow for an open GOP.

- **GOP Reference B-Frame** (H.264 and
  H.265 only): Enables the use of reference B-frames for GOP structures that
  have B- frames greater than 1.
- **Min I-interval**: Specifies a minimum
  number of frames between I-frames for GOP cadence and I-frames for scene
  change detection. I-frames require more bits than P- or B-frames, so
  encoding two in quick succession can hurt quality, particularly with small
  buffer sizes. The encoder enforces the minimum I-interval by shifting the
  GOP cadence.

Recommendation: For segmented outputs that require a fixed cadence of
I-frames, set this parameter to 0, in order to disable it.

- **Reference Frames**: Applies only to
  H.265. This parameter defines the number of frames that can be used to
  define B- and P- frames.

Recommendation: We recommend that you set this parameter to 3.

- **Scene Change Detect**: Enables an
  algorithm that determines when a scene change occurs. The encoder inserts
  an I-frame at each scene change.

Recommendation: Always enable this detection for the best video
quality. The only scenario where you might disable this detection is to
accommodate the rare case that a set-top box or playback device can't
accommodate an additional I-frame within the normal GOP pattern.

Some service providers, encoding vendors, or manufacturers might
state that scene change detection should be disabled during encoding of
content. Typically, they make this recommendation because their systems
require a consistent GOP structure. They assume that the encoder resets
the GOP structure when an I-frame is inserted for a scene change, which
disrupts the GOP structure.

However, the encoder doesn't disrupt the GOP structure in this way.
Instead, the encoder inserts an additional I-frame on a scene change.
With this approach, the adaptive bitrate outputs are always GOP-aligned.
This alignment has the side effect of allowing for compatibility with
these third-party systems, even when scene change detection is
enabled.

## Location of parameters

This table shows where the parameters mentioned in this section are
located. The first column shows the location on the web interface. The
second column shows the location in the event XML.

| Location of parameter on web interface                 | Location of tag in XML                                                                                                                                                    |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Streams – Video > Advanced > GOP Size**              | stream_assembly/video_description/`codec`/gop_size where codec is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings`                |
| **Streams – Video > Advanced > B Frames**              | stream_assembly/video_description/`codec`/ gop_num_b_frames where `codec` is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings`     |
| **Streams – Video > Advanced > Closed GOP Cadence**    | stream_assembly/video_description/`codec`/ gop_closed_cadence where `codec` is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings`   |
| **Streams – Video > Advanced > Reference Frames**      | stream_assembly/video_description/h265_settings/num_ref_frames                                                                                                            |
| **Streams – Video > Advanced > Scene Change Detect**   | stream_assembly/video_description/`codec`/ transition_detection where `codec` is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings` |
| **Streams – Video > Advanced > Min I-interval**        | stream_assembly/video_description/`codec`/ min_i_interval where `codec` is one of the following: <br>• `h264_settings` <br>• `mpeg2_settings` <br>• `h265_settings`       |
| **Streams – Video > Advanced > GOP Reference B-Frame** | stream_assembly/video_description/`codec`/ gop_b_reference where `codec` is one of the following: <br>• `h264_settings` <br>• `h265_settings`                             |
