# Collect information about the source content

After you have assessed the source content and have identified suitable video, audio, and
captions assets in that content, you must obtain information about those assets. The information
you need is different for each type of source.

You don't need this information to [create the input](medialive-inputs.md "medialive-inputs.md")
in MediaLive. But you will need this information when you [attach the input](creating-a-channel-step2.md "creating-a-channel-step2.md") to the channel in MediaLive.

###### Result of this step

After you have performed the procedures in this step, you should have source content
information that looks like this example.

| Example           | Information       | Format                      | Characteristics    | Identifiers |
| ----------------- | ----------------- | --------------------------- | ------------------ | ----------- |
| Upstream System   | RTP               | with FEC                    |                    |
| Selected video    | HEVC              | 1920x1080<br>5 Mbps maximum | PID 600            |
| Selected audio    | Dolby Digital 5.1 |                             | Spanish in PID 720 |
| AAC 2.0           |                   | Spanish in PID 746          |
| AAC 2.0           |                   | French in PID 747           |
| AAC 2.0           |                   | English in PID 759          |
| Selected captions | Embedded          |                             | C1 = Spanish       |
| C2 = French       |
| C4 = English      |
| Teletext          | 10 languages      | PID 815                     |

###### Topics

- [Identifying content in a CDI source](extract-contents-cdi.md "extract-contents-cdi.md")
- [Identifying content in an AWS Elemental Link source](extract-contents-link.md "extract-contents-link.md")
- [Identifying content in an HLS source](extract-contents-hls.md "extract-contents-hls.md")
- [Identifying content in a MediaConnect source](extract-content-emx.md "extract-content-emx.md")
- [Identifying content in an MP4 source](extract-contents-mp4.md "extract-contents-mp4.md")
- [Identifying content in an RTMP source](extract-contents-rtmp.md "extract-contents-rtmp.md")
- [Identifying content in an RTP source](extract-contents-rtp.md "extract-contents-rtp.md")
- [Identifying content in a
  SMPTE 2110 source](extract-contents-s2110.md "extract-contents-s2110.md")
- [Identifying content in an SRT source](extract-contents-srt.md "extract-contents-srt.md")
