This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Encoding – Rate Control Tuning

## Description

Following are encoding settings that can be used to provide additional tuning of video
quality.

- **Passes**: When this field is set to 2-pass and **Rate Control Mode** is set to CBR, VBR, or ABR, the system analyzes the
  entire source video stream before encoding in order to better distribute bits to more- or
  less-complex portions of the video. The tradeoff is that encoding time is increased as the
  system needs to decode/analyze the source stream prior to starting the encode process.
- **Lookahead**: This setting indicates the system should
  analyze a few frames in the future of the currently encoded frame (higher values mean more
  frames) and allow the encoder to take future frame data into account during rate control
  logic.

For example, if future frames are more complex, the encoder can allocate fewer bits to
encode the current frame to allow those bits to be used to encode those future frames. The
tradeoff is that processing and latency are increased slightly to allow those future frames
to be analyzed by the encoding engine.

## Recommendations

- Use 2-pass encoding for VOD unless minimize encoding time is critical.
- Set **Lookahead** to "medium" for use with 1-pass encoding
  unless latency is critical.

## Location of Fields

| Location of Field on Web Interface     | Location of Tag in XML                                                                                                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Streams – Video > Advanced > Passes    | stream_assembly/video_description/`codec`/passes where `codec` is one of the following: <br>• `h264_settings` <br>• `vc1_settings` <br>• `mpeg2_settings` <br>• `h265_settings`                  |
| Streams – Video > Advanced > Lookahead | stream_assembly/video_description/`codec`/look_ahead_rate_control where `codec` is one of the following: <br>• `h264_settings` <br>• `vc1_settings` <br>• `mpeg2_settings` <br>• `h265_settings` |
