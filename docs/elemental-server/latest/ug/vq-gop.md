This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Encoding – Group of Pictures (GOP)

## Description

The Group of Pictures (GOP) settings define the basic pattern of the video stream itself
in terms of how the encoding engine uses I-, P-, and B- frames. A few encoding settings
control the GOP structure are as follows:

- **GOP Mode**: Select **Fixed**.
- **GOP Size**: Defines the interval between I-frames.
- **B-Frames**: Defines the maximum run of B-frames.
  (**Note:** The encoding engine may make the decision to use a
  smaller run of B- frames in specific instances within the GOP if it determines this will
  produce higher quality content.)
- **Closed GOP Cadence**: Defines the number of GOPs across
  which P- or B-frames are allowed to predict for encoding purposes.
- **Scene Change Detect**: Enables an algorithm that
  determines when a scene change occurs and inserts an I-frame.
- **Min I-interval**: Specifies a minimum number of frames
  between GOP Cadence I-frames and Scene Change Detect I-frames. I-frames require more bits
  than P- or B-frames, so encoding two in quick succession can hurt quality, particularly with
  small buffer sizes.
- **GOP Reference B-Frame** (H.264 and H.265 only): Enables
  the use of reference B-frames for GOP structures that have B- frames greater than 1.

## Recommendations

- **GOP Mode**: Always choose **Fixed**.The
  **Follow** mode is obsolete and not recommended.
- **GOP Size**: When using the MPEG-2 codec, the recommended
  **GOP Size** is up to 30 (15 is also very common). For H.264 or
  VC-1 codecs, our recommendation is to make this as large as possible while still meeting
  other encoding requirements.

For example, for adaptive bitrate delivery in which a segment size of 6 seconds is used
for 29.97 fps outputs, the largest GOP size should be 180 frames.

- **B Frames and GOP Reference B-Frames**: When using H.264
  or H.265, enable **GOP Reference B-Frame** to obtain the best
  quality and set B-frames to a value from 3 to 5 (3 is recommended). For other codecs, there
  is no quality benefit to setting the B-frames to more than 2. For high-motion content, use 0
  or 1 to produce the best quality.
- **Closed GOP Cadence**: For segmented outputs (e.g. for
  adaptive bitrate content, such as HLS, Smooth, HDS, DASH, etc.), set the **Closed GOP Cadence** to 1. For non-segmented outputs, this can be set to 0 to
  allow for an open GOP.
- **Scene Change Detect**; Always enable this for the best
  quality. The only scenario where this might be disabled is if a STB or playback device is
  unable to accommodate an additional I-frame within the normal GOP pattern. (This is rare.)

Some service providers, encoding vendors, or manufacturers may state that **Scene Change Detect** should be disabled during encoding of content.
This recommendation is typically based on the fact that these providers have systems that
require a consistent GOP structure and some encoders "reset" the GOP structure when an
I-frame is inserted for a scene change.

On AWS Elemental systems, **Scene Change Detect** can be
enabled in almost all cases as the default behavior is to simply insert an additional I-frame
on a scene change but not disrupt the normal GOP structure defined in the encoding settings.
The intent behind this approach is to ensure that adaptive bitrate outputs are always
GOP-aligned, and, as a side effect, allow for compatibility with these third-party systems
even with **Scene Change Detect** enabled.

- **Min I-interval** is enforced by shifting the GOP cadence;
  so, for segmented outputs that require a fixed cadence of I-frames, it cannot be used and
  should be set to 0. For non-segmented outputs, a Min I-Interval of 5 is recommended.

## Location of Fields

| Location of Field on Web Interface                 | Location of Tag in XML                                                                                                                                                                         |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Streams – Video > Advanced > GOP Size              | stream_assembly/video_description/`codec`/gop_size where codec is one of the following: <br>• `h264_settings` <br>• `vc1_settings` <br>• `mpeg2_settings` <br>• `h265_settings`                |
| Streams – Video > Advanced > B Frames              | stream_assembly/video_description/`codec`/ gop_num_b_frames where `codec` is one of the following: <br>• `h264_settings` <br>• `vc1_settings` <br>• `mpeg2_settings` <br>• `h265_settings`     |
| Streams – Video > Advanced > Closed GOP Cadence    | stream_assembly/video_description/`codec`/ gop_closed_cadence where `codec` is one of the following: <br>• `h264_settings` <br>• `vc1_settings` <br>• `mpeg2_settings` <br>• `h265_settings`   |
| Streams – Video > Advanced > Scene Change Detect   | stream_assembly/video_description/`codec`/ transition_detection where `codec` is one of the following: <br>• `h264_settings` <br>• `vc1_settings` <br>• `mpeg2_settings` <br>• `h265_settings` |
| Streams – Video > Advanced > Min I-interval        | stream_assembly/video_description/`codec`/ min_i_interval where `codec` is one of the following: <br>• `h264_settings` <br>• `vc1_settings` <br>• `mpeg2_settings` <br>• `h265_settings`       |
| Streams – Video > Advanced > GOP Reference B-Frame | stream_assembly/video_description/`codec`/ gop_b_reference where `codec` is one of the following: <br>• `h264_settings` <br>• `h265_settings`                                                  |
