# Supported input class

In MediaLive there are two kinds of class for inputs — standard class inputs and
single-class inputs. Some inputs can be set up as either input class. Some inputs can be
set up only as single-class inputs.

When you have a choice, the type to use depends on whether you want to create a
standard channel, in order to implement pipeline resiliency. For more information, see
[Choosing the channel class and input
class](class-channel-input.md "class-channel-input.md").

| MediaLive input type       | Supported classes   |
| -------------------------- | ------------------- |
| CDI                        | Standard-class only |
| HLS                        | Both                |
| Link                       | Both                |
| MediaConnect               | Both                |
| MediaConnect Router        | Both                |
| MP4                        | Both                |
| RTMP Pull                  | Both                |
| RTMP Push                  | Both                |
| RTP                        | Standard-class only |
| SMPTE 2110                 | Single-class only   |
| SRT Caller                 | Both                |
| SRT Listener               | Both                |
| Transport Stream (TS) file | Both                |
