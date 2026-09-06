

# Clipping video using AWS Elemental Inference
<a name="elemental-inference-event-clip"></a>

**Note**  
The information in this section assumes that you are familiar with the general steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md). 

In an AWS Elemental MediaLive channel, you can enable the event clipping feature in order to generate metadata that identifies interesting events in the stream. You can then use an application of your choice to use the metadata to make a clip.

MediaLive uses AWS Elemental Inference for this feature. 
+ When a channel with event clipping is also running (active), MediaLive delivers the source stream to Elemental Inference. 
+ Elemental Inference uses foundational models to continually analyze the content to detect events of interest. For each event, Elemental Inference generates metadata that identifies the start and finish of the event. Elemental Inference sends the metadata for each event to EventBridge. 

Note that MediaLive delivers the source stream to Elemental Inference, and then its involvement in event clipping stops.

You can subscribe to EventBridge for these events, then use a third-party application to create a video clip. 

**Important**  
Currently, MediaLive supports event clipping with video for soccer games and basketball games. 

**Topics**
+ [Get Ready](event-clip-getready.md)
+ [Setting up event clipping](event-clip-procedure-console.md)
+ [Viewing the event clipping setup](event-clip-view-console.md)
+ [Viewing the setup on the Elemental Inference console](#event-clip-inference-view)
+ [Modifying the event clipping configuration](event-clip-modify.md)
+ [Disabling event clipping](event-clip-disable.md)
+ [Monitoring event clipping activity](event-clip-monitor.md)

## Viewing the setup on the Elemental Inference console
<a name="event-clip-inference-view"></a>

To view information for a feed on the Elemental Inference console, see [ Creating an Elemental Inference workflow](https://docs.aws.amazon.com/elemental-inference/latest/userguide/monitoring-inference-via-console) in the *AWS Elemental Inference user guide*.