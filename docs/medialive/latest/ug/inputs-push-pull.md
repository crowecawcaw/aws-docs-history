# Push and pull AWS Cloud inputs

When an input is being [deployed in the AWS Cloud](inputs-emla.md "inputs-emla.md"),
it is categorized in terms of how MediaLive and the upstream system negotiate
delivery:

- Push input with handshake.
- Push input without handshake.
- Pull input.
  There are different [limits](eml-limitations-and-rules.md#limits-inputs "eml-limitations-and-rules.md#limits-inputs") and [charges](pricing.md "pricing.md") for push inputs compared to pull inputs.

| MediaLive input type       | Category                 |
| -------------------------- | ------------------------ | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CDI                        | Push                     |      |
| HLS                        |                          | Pull |
| Link                       | Push                     |      |
| MediaConnect               | Push                     |      |
| MP4                        |                          | Pull |
| RTMP Pull                  |                          | Pull |
| RTMP Push                  | Push. See the note below |      |
| RTP                        | Push                     |      |
| SRT caller                 |                          | Pull |
| Transport Stream (TS) file |                          | Pull | **Note about RTMP push inputs** An RTMP push input works as follows: The source attempts to deliver to an endpoint that is specified in the MediaLive input. There must be a handshake between the source and the MediaLive channel so that the source has information about the status of the input. When you start the channel that includes this input, MediaLive responds to the handshake message and ingests it. When the channel is not running, MediaLive does not react; the source goes into a paused state. |
