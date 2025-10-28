# Setup: Creating inputs

This section describes how to create inputs for the content sources for an AWS Elemental MediaLive
channel. You must create these inputs before you start to create the channel.

To create an input, you must perform these steps:

- You must arrange for the operator at the upstream system to perform some
  setup.
- You must create inputs in MediaLive.
  These two steps create a connection between an address on the upstream system and an
  address on MediaLive. The source content moves from the specified address on the upstream system
  to the specified address on MediaLive as either a _push_ by the
  upstream system or a _pull_ by MediaLive. The connection
  information is contained in the input that you create.

The setup you perform is different for each combination of upstream system (format and
delivery protocol) and input type. If you haven't already done so, you must identify the
upstream system and input type for each content source. See [Assess the upstream system](evaluate-upstream-system.md "evaluate-upstream-system.md") .

###### Topics

- [Getting ready](input-create-getready.md "input-create-getready.md")
- [CDI input](input-create-cdi-push.md "input-create-cdi-push.md")
- [CDI input – Partner CDI input](input-create-cdi-partners.md "input-create-cdi-partners.md")
- [Elemental Link input](input-create-link-device.md "input-create-link-device.md")
- [HLS input](input-create-hls-pull.md "input-create-hls-pull.md")
- [MediaConnect input](input-create-push-mediaconnect.md "input-create-push-mediaconnect.md")
- [MP4 input](mp4-pull-input.md "mp4-pull-input.md")
- [RTMP pull input](input-create-rtmp-pull.md "input-create-rtmp-pull.md")
- [RTMP push input](input-create-rtmp-push.md "input-create-rtmp-push.md")
- [RTMP VPC input](rtmp-push-vpc-input.md "rtmp-push-vpc-input.md")
- [RTP push input](input-create-rtp-push.md "input-create-rtp-push.md")
- [RTP VPC input](rtp-push-vpc-input.md "rtp-push-vpc-input.md")
- [SMPTE 2110 input](input-create-s2110.md "input-create-s2110.md")
- [SRT input](input-caller-srt.md "input-caller-srt.md")
- [TS file input](ts-file-input.md "ts-file-input.md")
- [Next steps](input-create-nextsteps.md "input-create-nextsteps.md")
