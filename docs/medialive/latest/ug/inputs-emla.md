# Input deployments: AWS Cloud and

MediaLive Anywhere

Inputs are categorized by the deployment mode of the channel that they are attached
to:

- AWS Cloud only. These inputs can be attached only to a channel that is
  running in the AWS Cloud.
- MediaLive Anywhere only. These inputs can be attached only to a channel that is running in
  a MediaLive Anywhere cluster.
- Both. These inputs can be used in both AWS Cloud amd MediaLive Anywhere deployments.

| MediaLive input type       | Supported deployments               |
| -------------------------- | ----------------------------------- |
| CDI                        | AWS Cloud deployments only          |
| HLS                        | Both                                |
| Link                       | AWS Cloud deployments only          |
| MediaConnect               | AWS Cloud deployments only          |
| MP4                        | Both                                |
| RTMP Pull                  | Both                                |
| RTMP Push                  | Both                                |
| RTP                        | Both                                |
| SMPTE 2110                 | MediaLive Anywhere deployments only |
| SRT caller                 | Both                                |
| Transport Stream (TS) file | Both                                |
