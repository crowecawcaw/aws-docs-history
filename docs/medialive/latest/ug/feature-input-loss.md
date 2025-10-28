# Handling loss of video input

You can customize the way that MediaLive handles media when the video input
into the channel is lost.

###### Topics

- [How MediaLive handles video input
  loss](#feature-input-loss-overview "#feature-input-loss-overview")
- [Configuring the
  replacement content](#feature-input-loss-customize-replacement "#feature-input-loss-customize-replacement")
- [Customizing
  delivery](#feature-input-loss-customize-delivery "#feature-input-loss-customize-delivery")

## How MediaLive handles video input

loss

When MediaLive is ingesting an input, it might detect that the video source
has been lost. This loss causes MediaLive to start to follow the _input loss behavior_ handling. MediaLive starts to
encode _replacement content_ (fill frames)
on the output side. This handling ensures that the channel can continue to
encode video content. (A key rule of MediaLive is that a running channel must
always be encoding content.)

The channel follows the input loss handling until it recovers and goes
back to normal encoding. The way that the channel recovers depends on whether
you implement automatic input failover:

- If you implement [automatic
  input failover](automatic-input-failover.md "automatic-input-failover.md"), the input loss handling will continue until the
  video black failover condition triggers the switch to another input (or
  until the input recovers.) If the second input fails, input loss handling
  will restart and continue until you have fixed the problem with both of the
  inputs.
- If you don't implement automatic input failover, the input loss
  handling will continue until the input recovers or until you resolve the
  problem with the input.

The two features complement each other but work on different
timing:

- Input loss handling occurs as soon as an expected frame fails to
  arrive. For example, if the framerate of the input is 60 FPS, the handling
  will be triggered if a frame does not arrive within 17 Msecs of the
  previous frame. (17 Msecs is approximately 1 second divided by 60.)
- The trigger for automatic input failover is longer and is
  configurable. A typical trigger is 1000 Msecs.

**Input loss compared to input probing
failure**

Input loss handling occurs only after a previously healthy input becomes
unhealthy.

It is also possible for an input to fail before that. When a channel
starts and MediaLive begins to ingest the first input, it _probes_ for the input—it attempts to detect the input and the
sources. If the detection fails, then the input and the chanel fails
immediately. You must resolve the problem and restart the channel. The
problem might be that the input isn't present (this problem applies mostly to
RTMP inputs), or the input exceeds the [current channel specifications](input-specification.md "input-specification.md"), or the [input settings are wrong](create-input.md "create-input.md").

**Default behaviour input loss
handling**

The default for input loss handling is the following:

- Encoding the replacement content: Repeat and encode the last valid
  frame that was received. Repeat for 1000 Msecs. Then encode black frames
  for 1000 Msecs. Then encode a black slate indefinitely.
- Delivering the content: The default handling is to emit (deliver) the
  encoded replacement content.

**Customizing input loss handling**

- You can customize the timing of the replacement content, and you can
  customize the content of the slate..
- In some output group types, you can change the delivery so that the
  encoded content isn't delivered.

## Configuring the

replacement content

You can customize the duration of the replacement content, and you can
customize the image or color used for the slate. For example, you can change
the slate to an image (such as _Please stand
by_).

###### Note

This section assumes that you are familiar with creating or editing a
channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

1. On the **Create** channel page of the MediaLive
   console, choose **General settings**. Expand
   **Global configuration**. Choose **Enable global
   configuration**, if necessary.
2. In **Input loss behavior**, choose **Input
   loss Behavior**. More fields appear. These fields control the
   replacement content, as follows:
   - Encode the last valid frame for the time specified in
     **Repeat Frame Msec**. Zero means disabled (skip the
     repeat frame and go to the black frame). The value 1,000,000 means repeat
     the previous forever.
   - When **Repeat Frame Msec** expires, encode a black
     frame for the time specified in **Black Frame Msec**.
     Zero means disabled (skip the black frame and go to the slate). The value
     1,000,000 means repeat black frames forever.
   - When **Black Frame Msec** expires, switch to
     sending a specified slate or color, as specified in **Input Loss
     Image Type** and then **Input Loss Image
     Color** or **Input Loss Image Slate**.

3. Complete one or more fields to customize the behavior.
   For details about a field on the MediaLive console, choose the **Info** link next to the field.

## Customizing

delivery

You can change the default handling of the replacement content so that
instead of delivering the encoded output, MediaLivediscards it. You can change
the handling in the following types of output groups:

- HLS
- Microsoft Smooth
- RTMP
- UDP/TS

For all other types of output groups except MediaPackage, MediaLive always
delivers the content. For a MediaPackage output group, MediaLive always [pauses delivery](mediapackage-create-result.md "mediapackage-create-result.md").

###### Note

This section assumes that you are familiar with creating or editing a
channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

1. On the **Create** channel page of the MediaLive
   console, choose the output group in the left navigation bar.
2. In the **Settings** section for the output group,
   find the **Input Loss Action** field for that output
   group. Choose the option you want for all the outputs (including outputs
   that don't include video) in this output group. See the table after this
   step.

This table lists the delivery options for the output groups. Read across
each row.

| Type of output group      | Field        | Description                                                                                                                                                                                                                                                                                                      |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HLS Microsoft Smooth RTMP | EMIT_OUTPUT  | Deliver the replacement content.This is the default for these output groups.                                                                                                                                                                                                                                     |
| HLS Microsoft Smooth RTMP | PAUSE_OUTPUT | Encode only the repeat frames, if the [channel is configured](#feature-input-loss-customize-replacement "#feature-input-loss-customize-replacement") to process them. After that content ends, stop delivery for all outputs in this output group.Note that MediaLive keeps the underlying RTMP connection open. |
| UDPSRT                    | EMIT_PROGRAM | Encode the replacement content, and deliver the program and all the tables for this output group. This is the default for UDP.                                                                                                                                                                                   |
| UDPSRT                    | DROP_TS      | Stop delivery of the entire transport stream in this output group.                                                                                                                                                                                                                                               |
| UDPSRT                    | DROP_PROGRAM | Drop the program from the transport stream. MediaLive replaces the program with null packets, in order to meet the TS bitrate requirement. Deliver the null packets and all the tables for this output group.                                                                                                    | **Recommendation** You should make sure that the delivery meets the expectations of the downstream system. For example, if the channel is a standard channel (with two redundant pipelines), the downstream system might be set up to switch to the output from the second pipeline. In this case, it's best if you set up the output to stop emitting the output. As another example, the channel might have only one pipeline. Furthermore, the downstream system might not behave well if it loses delivery from MediaLive. Therefore, it's best for you to set up to emit the output. The downstream system will remain stable, and you could set up MediaLive with a "Please stand by" slate to improve the experience for the person watching the video. |
