# Clipping video using AWS Elemental Inference

###### Note

The information in this section assumes that you are familiar with the general steps
for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

In an AWS Elemental MediaLive channel, you can enable the event clipping feature in order to generate
metadata that identifies interesting events in the stream. You can then use an application
of your choice to use the metadata to make a clip.

MediaLive uses AWS Elemental Inference for this feature.

- When a channel that has event clipping enabled is running, MediaLive delivers the
  source stream to Elemental Inference.
- Elemental Inference uses foundational models to continually analyze the content to detect
  events of interest. For each event, Elemental Inference generates metadata that identifies the
  start and finish of the event. Elemental Inference sends the metadata for each event to EventBridge.
  Note that MediaLive delivers the source stream to Elemental Inference, and then its involvement in event
  clipping stops.

You can subscribe to EventBridge for these events, then use a third-party application to create a
video clip.

###### Important

Currently, MediaLive supports event clipping with video for soccer games and basketball
games.

###### Topics

- [Pricing](#event-clip-pricing "#event-clip-pricing")
- [Source requirements](#event-clip-source-requirements "#event-clip-source-requirements")
- [Setting up event clipping using the MediaLive console](#event-clip-procedure-console "#event-clip-procedure-console")
- [Modifying the event clipping configuration](#event-clip-modify "#event-clip-modify")
- [Disabling event clipping](#event-clip-disable "#event-clip-disable")

## Pricing

There is a charge for running a channel that has the event clipping feature enabled.
To stop this charge, you must disable the feature [Disabling event clipping](#event-clip-disable "#event-clip-disable").
For information on charges for using this feature, see [https://aws.amazon.com/elemental-inference/pricing/](https://aws.amazon.com/elemental-inference/pricing/ "https://aws.amazon.com/elemental-inference/pricing/").

###### Note

When you enable event clipping in a standard-class MediaLive channel, there is a
separate but identical charge for each pipeline in the channel.

## Source requirements

- Input type: All supported types. The _input_
  must be live input, not a file input.
- Input codec: All supported codecs
- Input resolution: All supported resolutions.
- Aspect ratio: Any aspect ratio
- Static image overlays and burned-in captions: We recommend that the source
  doesn’t include static image overlays or burned-in captions because the event
  clip might cut them off awkwardly.
- Event clipping is supported in channels that implement input switching and/or
  input failover.
- Event clipping isn't supported in MediaLive Anywhere channels.

## Setting up event clipping using the MediaLive console

###### Note

The information in this section assumes that you are familiar with the general
steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

### Enable event clipping

You must enable event clipping in the channel.

1. On the **Create channel** or **Edit channel
   page**, choose **AWS Elemental Inference
   settings**.
2. In **State**, choose **Enabled**.
   Sections for each Elemental Inference feature appear.
3. Expand the **Clip events** section. In
   **State**, choose **Enabled**.
4. In **Callback config**, enter a string that you want
   Elemental Inference to always include in the event clipping metadata for this output. In
   EventBridge, will be able to filter events using this string, to identify the
   events for one feed. The string might identify the sports event in the feed,
   for example.

## Modifying the event clipping configuration

You can modify the existing event clipping configuration in a channel as
follows:

1. On the **Create channel** or **Edit channel
   page**, choose **AWS Elemental Inference
   settings**. If necessary, expand the **Event
   clipping** section.
2. Change the value in **Callback config**.

## Disabling event clipping

You can disable event clipping in a channel as follows:

**To disable event clipping in the channel**

On the **Create channel** or **Edit channel page**,
choose **AWS Elemental Inference settings**. Choose the appropriate
action:

- To disable all Elemental Inference features, set the **State** field for
  Elemental Inference to **Disabled**.
- To disable only the event clipping feature, set the **State**
  field in **Event clipping** to
  **Disabled**.
