

# Monitoring Amazon IVS Real-Time Streaming
<a name="stage-health"></a>

This document provides details about options available for monitoring your IVS real-time streaming application.

## What is a Stage Session?
<a name="stage-health-session"></a>

A stage *session* begins when the first participant joins a stage and ends a few minutes after the last participant stops publishing to the stage. Stage sessions help with debugging long-lived stages by separating out events and participants into short-lived sessions.

## View Stage Sessions and Participants
<a name="stage-health-view-sessions-participants"></a>

### Console Instructions
<a name="stage-health-view-sessions-participants-console"></a>

1. Open the[ Amazon IVS console](https://console.aws.amazon.com/ivs).

   (You also can access the Amazon IVS console through the [AWS Management Console](https://console.aws.amazon.com).)

1. On the navigation pane, choose **Stages**. (If the nav pane is collapsed, first open it by choosing the hamburger icon.)

1. Choose the stage to go to its details page.

1. Scroll down the page until you see the **Stage sessions** section, then select a stage session to view its details page.

1. To view participants in the session, scroll down until you see the **Participants** section, then select a participant to view its details page, including charts for Amazon CloudWatch metrics.

## View Events for a Participant
<a name="stage-health-view-participant-events"></a>

Events are sent when a participant’s status in a stage changes, such as joining a stage or encountering an error trying to publish to a stage. Not all errors cause events; e.g., client-side network errors and token-signature errors are not sent as events. To handle these errors in your client application, use the [IVS broadcast SDKs](broadcast.md).

### Console Instructions
<a name="stage-health-view-participant-events-console"></a>

1. Navigate to the participant details page as instructed above.

1. Scroll down until you see the **Events** section. This displays an ordered list of participant events. See [Using Amazon EventBridge with Amazon IVS](eventbridge.md) for details on events that are emitted for participants.

### CLI Instructions
<a name="stage-health-view-participant-events-cli"></a>

Accessing stage-session events with the AWS CLI is an advanced option and requires that you first download and configure the CLI on your machine. For details, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).

1. List stage sessions to find a stage session:

   ```
   aws ivs-realtime list-stage-sessions --stage-arn <arn>
   ```

1. List participants for a stage session to find a participant:

   ```
   aws ivs-realtime list-participants --stage-arn <arn> –session-id <sessionId>
   ```

1. List events for a stage session and participant:

   ```
   aws ivs-realtime list-participant-events --stage-arn <arn> --session-id <sessionId> –-participant-id <participantId>
   ```

Here is a sample response to the `list-participant-events` call: 

```
{
    "events": [
        {
            "eventTime": "2023-04-04T22:48:41+00:00",
            "name": "JOINED",
            "participantId": "AdRezBl021t0"
        },
        {
            "eventTime": "2023-04-04T22:48:41+00:00",
            "name": "SUBSCRIBE_STARTED",
            "participantId": "AdRezBl021t0",
            "remoteParticipantId": "Ou5b5n5XLMdC"
        },
        {
            "eventTime": "2023-04-04T22:49:45+00:00",
            "name": "SUBSCRIBE_STOPPED",
            "participantId": "AdRezBl021t0",
            "remoteParticipantId": "Ou5b5n5XLMdC"
        },
        {
            "eventTime": "2023-04-04T22:49:45+00:00",
            "name": "LEFT",
            "participantId": "AdRezBl021t0"
        }
    ]
}
```

## Access CloudWatch Metrics
<a name="stage-health-access-cloudwatch-metrics"></a>

For CloudWatch metrics to be available, the following IVS Broadcast SDK versions are required: Web 1.5.0 or later, Android 1.12.0 or later, or iOS 1.12.0 or later.

### CloudWatch Console Instructions
<a name="stage-health-access-cloudwatch-metrics-console"></a>

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the side navigation, expand the **Metrics** dropdown, then select **All metrics**.

1. On the **Browse** tab, using the unlabeled dropdown at the left, select your “home” region, where your channel(s) was(were) created. For more on regions, see [Global Solution, Regional Control](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/what-is.html#what-is-aws). For a list of supported regions, see the [Amazon IVS page](https://docs.aws.amazon.com/general/latest/gr/ivs.html) in the *AWS General Reference*.

1. At the bottom of the **Browse** tab, select the **IVSRealTime** namespace.

1. Do one of the following:

   1. In the search bar, enter your resource ID (part of the ARN, `arn:::ivs:stage/<resource id>`).

      Then select **IVSRealTime > Stage Metrics**.

   1. If **IVSRealTime** appears as a selectable service under **AWS Namespaces**, select it. It will be listed if you use Amazon IVS Real-Time Streaming and it is sending metrics to Amazon CloudWatch. (If **IVSRealTime** is not listed, you do not have any Amazon IVS metrics.)

      Then choose a *dimension* grouping as desired; available dimensions are listed in [CloudWatch Metrics](#stage-health-cloudwatch-metrics) below.

1. Choose metrics to add to the graph. Available metrics are listed in [CloudWatch Metrics](#stage-health-cloudwatch-metrics) below.

You also can access your stream session’s CloudWatch chart from the stream session’s details page, by selecting the **View in CloudWatch** button.

### CLI Instructions
<a name="stage-health-access-cloudwatch-metrics-cli"></a>

You also can access the metrics using the AWS CLI. This requires that you first download and configure the CLI on your machine. For details, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).

Then, to access Amazon IVS real-time streaming metrics using the AWS CLI:
+ At a command prompt, run:

  ```
  aws cloudwatch list-metrics --namespace AWS/IVSRealTime
  ```

For more information, see [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) in the *Amazon CloudWatch User Guide*.

## CloudWatch Metrics: IVS Real-Time Streaming
<a name="stage-health-cloudwatch-metrics"></a>

Amazon IVS provides the following metrics in the **AWS/IVSRealTime** namespace.

For CloudWatch metrics to be available, Web Broadcast SDK 1.5.2 or later must be used.

The dimension can have the following valid values:
+ The `Stage` dimension is a resource ID (part of the ARN, `arn:::stage/<resource id>`).
+ The `Participant` dimension is a `participantID`.
+ The `SimulcastLayer` is "hi", "mid", "low", or "none" for a `MediaType` of "video", or "none" for a `MediaType` of "audio." This value also can be empty.
+ The `MediaType` dimension is "video" or "audio" (string).

In the case of participant replication, for the destination stage, existing stage-health metrics include all replicated participants (publishers in the source stage who are replica participants in the destination stage).


| Metric | Dimensions | Description | 
| --- | --- | --- | 
| `ConcurrentPublishers` | — | Number of participants publishing across all stages in an AWS Region.<br />Unit: Count<br />Valid statistics: Average, Maximum, Minimum | 
| `ConcurrentSubscriptions` | — | Number of simultaneous publisher-to-subscriber connections across all stages in an AWS Region.<br />Unit: Count<br />Valid statistics: Average, Maximum, Minimum | 
| `DownloadPacketLoss` | — | Percentage of packets that were lost while downloading from the IVS server by subscribers.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of packet loss over the configured interval | 
| `DownloadPacketLoss` | `Platform` | Filters `DownloadPacketLoss` by subscriber platform.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of packet loss over the configured interval | 
| `DownloadPacketLoss` | `Platform, SDKVersion` | Filters `DownloadPacketLoss` by subscriber platform and SDK version.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of packet loss over the configured interval | 
| `DownloadPacketLoss` | `Stage` | Filters `DownloadPacketLoss` by subscriber stage.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of packet loss over the configured interval | 
| `DownloadPacketLoss` | `Stage, Participant` | Filters `DownloadPacketLoss` by participant, for subscribers who are also publishers. Samples represent the percentage of packets that were lost by the subscriber while downloading from the IVS server. Samples are emitted only when the participant is also a publisher.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of dropped frames over the configured interval | 
| `DownloadPacketLoss` | `Stage, Platform` | Filters `DownloadPacketLoss` by subscriber stage and platform.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of packet loss over the configured interval | 
| `DownloadPacketLoss` | `Stage, Platform, SDKVersion` | Filters `DownloadPacketLoss` by subscriber stage, platform, and SDK version.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of packet loss over the configured interval | 
| `DownloadPacketLoss` | `Stage, SubscriberCountryCode` | Filters `DownloadPacketLoss` by subscriber stage and country code (ISO 3166).<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of packet loss over the configured interval | 
| `DownloadPacketLoss` | `SubscriberCountryCode` | Filters `DownloadPacketLoss` by subscriber country code (ISO 3166).<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of packet loss over the configured interval | 
| `DroppedFrames` | `—` | For subscribers: the percentage of video frames dropped, calculated by aggregating frames received and frames dropped across all publishers the subscriber is subscribed to.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of dropped frames over the configured interval | 
| `DroppedFrames` | `Platform` | Filters `DroppedFrames` by subscriber’s platform.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of dropped frames over the configured interval | 
| `DroppedFrames` | `Platform, SDKVersion` | Filters `DroppedFrames` by subscriber’s platform and SDK version.<br />Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of dropped frames over the configured interval | 
| `DroppedFrames` | `Stage` | Filters `DroppedFrames` by stage.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of dropped frames over the configured interval | 
| `DroppedFrames` | `Stage, Participant` | Filters `DroppedFrames` by stage and participant. Only emitted for subscribers who are also publishers.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of dropped frames over the configured interval | 
| `DroppedFrames` | `Stage, Platform` | Filters `DroppedFrames` by stage and subscriber’s platform.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of dropped frames over the configured interval | 
| `DroppedFrames` | `Stage, Platform, SDKVersion` | Filters `DroppedFrames` by stage and subscriber’s platform and SDK version.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of dropped frames over the configured interval | 
| `DroppedFrames` | `Stage, SubscriberCountryCode` | Filters `DroppedFrames` by stage and subscriber’s country.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of dropped frames over the configured interval  | 
| `DroppedFrames` | `SubscriberCountryCode` | Filters `DroppedFrames` by subscriber’s country.<br />Unit: Percent<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of dropped frames over the configured interval | 
| `PublishBitrate` | `—` | The total rate at which a publisher is sending both video and audio data (summed across all simulcast layers). This includes retransmitted data. The bitrate can be inflated by upload packet loss and retransmissions, since it reflects what the publisher sends and may not match what IVS receives or delivers to subscribers.<br />Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `PublishBitrate` | `Platform` | Filters `PublishBitrate` by publisher’s platform.<br />Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `PublishBitrate` | `Stage` | Filters `PublishBitrate` by stage.<br />Unit: Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `PublishBitrate` | `Stage, Participant, SimulcastLayer, MediaType` | Filters `PublishBitrate` by stage, participant, simulcast layer, and media type. The simulcast layer ID is set by the broadcast SDK. When simulcast is disabled, this layer ID will be set to "disabled". The media type is either "video" or "audio".<br />Unit: Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `Publishers` | `Stage` | Number of participants publishing to the stage.<br />Unit: Count<br />Valid statistics: Average, Maximum, Minimum | 
| `PublishFramerate` | `Stage, Participant` | How often video frames are received from a given publisher. This metric is available only for participants publishing over RTMP.<br />Unit: Count/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of framerate over the configured interval | 
| `PublishFramerate` | `Stage, Participant, SimulcastLayer, MediaType` | How often video frames are received from a given publisher. This metric is available only for participants publishing over RTMP.<br />Unit: Count/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of framerate over the configured interval | 
| `PublishResolution` | `Stage, Participant, SimulcastLayer, MediaType` | Number of pixels across the smaller of the width or height of the frame. For example, for a landscape frame of size 1920x1080, the PublishResolution is 1080. For a portrait frame of size 720x1280, the PublishResolution is 720.<br />Unit: Count<br />Valid statistics: Average, Maximum, Minimum | 
| `SubscribeBitrate` | `—` | The total rate at which a subscriber is receiving both video and audio data<br />Unit: Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `SubscribeBitrate` | `Platform` | Filters `SubscribeBitrate` by subscriber’s platform.<br />Unit: Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval  | 
| `SubscribeBitrate` | `Platform, SDKVersion` | Filters `SubscribeBitrate` by subscriber’s platform and SDK version.<br />Unit: Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `SubscribeBitrate` | `Stage` | Filters `SubscribeBitrate` by stage.<br />Unit: Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `SubscribeBitrate` | `Stage, Participant, MediaType` | Filters `SubscribeBitrate` by stage, participant, and media type. The media type is either "video" or "audio". This metric is emitted only while the subscribing participant is also publishing.<br />Unit: Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `SubscribeBitrate` | `Stage, Platform` | Filters `SubscribeBitrate` by stage and subscriber’s platform.<br />Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `SubscribeBitrate` | `Stage, Platform, SDKVersion` | Filters `SubscribeBitrate` by stage and subscriber’s platform and SDK version.<br />Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `SubscribeBitrate` | `Stage, SubscriberCountryCode` | Filters `SubscribeBitrate` by stage and subscriber’s country code.<br />Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval | 
| `SubscribeBitrate` | `SubscriberCountryCode` | Filters `SubscribeBitrate` by subscriber’s country code (ISO 3166-1 alpha-2).<br />Bits/second<br />Valid statistics: Average, Maximum, Minimum — Average number, largest number, or smallest number (respectively) of bitrate over the configured interval  | 
| `Subscribers` | `Stage` | Number of participants subscribed to the stage. Note that participants that are actively publishing and subscribing are counted as both publishers and subscribers.<br />Unit: Count<br />Valid statistics: Average, Maximum, Minimum | 