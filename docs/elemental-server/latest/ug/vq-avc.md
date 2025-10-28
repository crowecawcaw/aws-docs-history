This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Encoding – MPEG-4 AVC (H.264) Controls

## Description

A few h.264-specific controls are available on AWS Elemental systems that affect video
quality:

- **CABAC**: This control enables arithmetic coding and can
  compress the same data with ~15% fewer bits.
- **Slices**: This control improves speed of encoding. Using
  a higher number of slices can improve speed optimization but results in slightly less
  quality.
- **Flicker Reduction**: This control reduces flicker in the
  video. It enables an additional encoding algorithm that compensates for visual differences
  when I-frames have occurred (often referred to as I-frame "pop"). The AWS Elemental system
  uses this approach to encode I-frames as if they were P-frames (thus creating a "PI"-frame),
  identify macroblocks that are prone to flicker, merge pixels from the PI-frame for the
  flicker-prone MBs into the I-frame, and then encode the PI-frame. This method carries some of
  the visual quality from the end of one GOP to the start of the next GOP, preventing the
  abrupt change in detail that gives the effect of a flicker in the video.
- **Reference Frames**: This control defines the number of
  frames that can be used to define B- and P- frames.

## Recommendations

- Use **High Profile** with H.264 to improve quality over
  Baseline Profile and Main Profile.
- Always enable **CABAC** unless the intended decoder or
  playback device doesn't support it.
- Set **Slices** to 2 (or higher) for all HD resolution
  outputs or high bitrate outputs. (AWS Elemental presets typically use 2 slices for 720p
  content and 4 slices for 1080p content.) For resolutions below 720p, set **Slices** to 1.
- Set **Flicker Reduction** to "high" for low-motion content.
  Disable it for high-motion content.
- Set **Reference Frames** to 2 or more for flash
  compensation.

## Location of Fields

| Location of Field on Web Interface             | Location of Tag in XML                                            |
| ---------------------------------------------- | ----------------------------------------------------------------- |
| Streams – Video > Advanced > Profile           | stream_assembly/video_description/h264_settings>/cabac            |
| Streams – Video > Advanced > Level             | stream_assembly/video_description/h264_settings>/level            |
| Streams – Video > Advanced > CABAC             | stream_assembly/video_description/h264_settings>/cabac            |
| Streams – Video > Advanced > Slices            | stream_assembly/video_description/h264_settings/slices            |
| Streams – Video > Advanced > Flicker Reduction | stream_assembly/video_description/h264_settings/flicker_reduction |
