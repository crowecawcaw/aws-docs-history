# Monitoring Amazon IVS Low-Latency Streaming

You can monitor Amazon Interactive Video Service (IVS) resources using Amazon CloudWatch.
CloudWatch collects and processes raw data from Amazon IVS into readable, near real-time
metrics. These statistics are kept for 15 months, so you can gain a historical perspective
on how your web application or service performs. You can set alarms for certain thresholds
and send notifications or take actions when those thresholds are met. For details, see the
[CloudWatch User
Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

The timestamp on a metric represents the start of the period during which metric data is
accumulated. For example, suppose you get a per-minute `LiveDeliveredTime` metric
sum of 300 seconds at 01:02:00. This would mean that 5 minutes’ worth of video was served to
viewers during the 1-minute period from 01:02:00 to 01:02:59.

For metrics designated as high resolution, the first data point appears several seconds
after stream start. We recommend you specify a 5-second period when making the metric
requests. (See [Resolution](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Resolution_definition "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Resolution_definition") in the Amazon CloudWatch User Guide.) For other metrics, data is
emitted within 1 minute of the timestamp to which it refers.

The high-resolution metrics are rolled up over time. Resolution effectively decreases as
the metrics age. Here is the schedule:

- 1-second metrics are available for 3 hours.
- 60-second metrics are available for 15 days.
- 5-minute metrics are available for 63 days.
- 1-hour metrics are available for 455 days (15 months).
  For current information on data retention, search for "retention period" in [Amazon CloudWatch FAQs](https://aws.amazon.com/cloudwatch/faqs/ "https://aws.amazon.com/cloudwatch/faqs/").

## Prerequisites

- You must have an AWS account with sufficient IAM permissions to interface with
  the Stream Health APIs and CloudWatch metrics. For specific steps, see [Getting Started with IVS Low-Latency
  Streaming](getting-started.md "getting-started.md").
- You must create a channel and start a stream. Relevant information is in the
  [IVS Low-Latency Streaming User Guide](what-is.md "what-is.md"):
  - For instructions on creating a channel, see [Create a Channel](getting-started-create-channel.md "getting-started-create-channel.md") in
    _Getting Started with IVS Low-Latency
    Streaming_.
  - For instructions on starting a stream, see [Set Up Streaming Software](getting-started-set-up-streaming.md "getting-started-set-up-streaming.md") in _Getting Started with IVS Low-Latency Streaming_.
  - For encoder-configuration details, see [Amazon
    IVS Streaming Configuration](streaming-config.md "streaming-config.md").

## Access Stream Session Data

Using the `listStreamSessions` operation, you can access a list of streams
that a channel has had for up to 60 days. This list may include a live stream session
(denoted by an empty `endTime`).

You can get the session data for a specific stream through the
`getStreamSession` operation. If you do not specify the
`streamId` parameter, the operation returns the latest session. In
addition, you can periodically call the operation to get your stream’s latest events (up
to the most recent 500).

### Console Instructions

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").

(You also can access the Amazon IVS console through the [AWS Management
Console](https://console.aws.amazon.com "https://console.aws.amazon.com").) 2. On the navigation pane, choose **Channels**.
(If the nav pane is collapsed, first open it by choosing the hamburger
icon.) 3. Choose the channel to go to its details page. 4. Scroll down the page until you see the **Stream
sessions** section. 5. Select the Stream ID of the session you want to access to view its session
details, including charts for the Amazon CloudWatch high-resolution
metrics.

Alternatively, if one or more channels are already live:

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").
2. On the navigation pane, choose **Live
   channels**. (If the nav pane is collapsed, first open it by
   choosing the hamburger icon.)
3. Select a live channel from the list to access its session details inside a
   split view.

### AWS SDK Instructions

Accessing stream-session data with the AWS SDK is an advanced option and requires
that you first download and configure the SDK on your application. Below are
instructions for the AWS SDK using JavaScript.

**Prerequisite**: To use the code sample below, you
need to load the AWS JavaScript SDK into your application. For details, see [Getting started with the AWS SDK for JavaScript](../../../sdk-for-javascript/v3/developer-guide/getting-started.md "../../../sdk-for-javascript/v3/developer-guide/getting-started.md").

```
// This first call lists up to 50 stream sessions for a given channel.
const AWS = require("aws-sdk");
const REGION = 'us-west-2';
let channelArn = USE_YOUR_CHANNEL_ARN_HERE;

AWS.config.getCredentials(function(err) {
  if (err) console.log(err.stack);
  // credentials not loaded
  else {
    console.log("Access key:", AWS.config.credentials.accessKeyId);
  }
});

AWS.config.update({region: REGION});
var ivs = new AWS.IVS();

// List Stream Sessions
async function listSessions(arn) {
  const result = await ivs.listStreamSessions({"channelArn": arn}).promise();
  console.log(result.streamSessions);
}
listSessions(channelArn);

// Get Stream Session
async function getSession(arn, id) {
  const result = await ivs.getStreamSession({"channelArn": arn, "streamId": id}).promise();
  console.log(result);

  // This function polls every 3 seconds and prints the latest IVS stream events.
  setInterval(function(){
    console.log(result.streamSession.truncatedEvents);
  }, 3000);
}
getSession(channelArn);
```

### CLI Instructions

Accessing stream-session data with the AWS CLI is an advanced option and requires
that you first download and configure the CLI on your machine. For details, see the
[AWS
Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

1. List streams sessions:

```
aws ivs list-stream-sessions --channel-arn <arn>
```

2. Get stream session data for a specific stream using its
   `streamId`:

```
aws ivs get-stream-session --channel-arn <arn> --stream-id <streamId>
```

Here is a sample response to the `get-stream-session` call:

```
{
    "streamSession": {
        "startTime": "2021-10-22T00:03:57+00:00",
        "streamId": "st-1FQzeLONMT9XTKI43leLSo1",
        "truncatedEvents": [
            {
                "eventTime": "2021-10-22T00:09:30+00:00",
                "name": "Session Ended",
                "type": "IVS Stream State Change"
        	},
            {
                "eventTime": "2021-10-22T00:09:30+00:00",
                "name": "Stream End",
                "type": "IVS Stream State Change"
        	},
        	{
                "eventTime": "2021-10-22T00:03:57+00:00",
                "name": "Stream Start",
                "type": "IVS Stream State Change"
        	},
        	{
                "eventTime": "2021-10-22T00:03:50+00:00",
                "name": "Session Created",
                "type": "IVS Stream State Change"
        	}
        ],
        "endTime": "2021-10-22T00:09:31+00:00",
        "ingestConfiguration": {
            "audio": {
                "channels": 2,
                "codec": "mp4a.40.2",
                "sampleRate": 48000,
                "targetBitrate": 160000
        	},
            "video": {
                "avcLevel": "4.0",
                "avcProfile": "Baseline",
                "codec": "avc1.42C028",
                "encoder": "obs-output module (libobs version 27.0.1)",
                "targetBitrate": 3500000,
                "targetFramerate": 30,
                "videoHeight": 1080,
                "videoWidth": 1920
            }
        },
        "channel": {
            "name": "",
            "ingestEndpoint": "3f234d592b38.global-contribute.live-video.net",
            "authorized": false,
            "latencyMode": "LOW",
            "recordingConfigurationArn": "",
            "type": "STANDARD",
            "playbackUrl": "https://3f234d592b38.us-west-2.playback.live-video.net/api/video/v1/us-west-2.991729659840.channel.dY7LsluQX1gV.m3u8",
            "arn": "arn:aws:ivs:us-west-2:991729659840:channel/dY7LsluQX1gV"
        }
    }
}
```

## Filter Streams by Health

To easily find which streams are experiencing issues, you can use
`listStreams` to filter live streams by “health.”

### Console Instructions

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").

(You also can access the Amazon IVS console through the [AWS Management
Console](https://console.aws.amazon.com "https://console.aws.amazon.com").) 2. On the navigation pane, choose **Live
channels**. (If the nav pane is collapsed, first open it by
choosing the hamburger icon.) 3. Select the search field for **Filter by
health**. 4. In the drop-down list, select filtering by **Health =
STARVING**.

After filtering, you can go to a channel’s details page and select the channel’s
live-stream session, to access input-configuration details and stream events.

### CLI Instructions

Using the AWS CLI is an advanced option and requires that you first download and
configure the CLI on your machine. For details, see the [AWS
Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

To filter streams by health (e.g. `STARVING`):

```
aws ivs list-streams --filter-by health=STARVING
```

### CloudWatch Health

Dimension for ConcurrentStreams

You can filter `ConcurrentStreams` by a specific `Health`.
See [CloudWatch Metrics: IVS Low-Latency Streaming](#stream-health-cloudwatch-metrics-low-latency-streaming "#stream-health-cloudwatch-metrics-low-latency-streaming").

## Access CloudWatch Metrics

Amazon CloudWatch collects and processes raw data from Amazon IVS into readable,
near-real-time metrics. These statistics are kept for 15 months, so you can gain a
historical perspective on how your web application or service performs. You can set
alarms for certain thresholds and send notifications or take actions when those
thresholds are met. For details, see the [CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").

Note that CloudWatch metrics are rolled up over time. Resolution effectively decreases
as the metrics age. Here is the schedule:

- 1-second metrics are available for 3 hours.
- 60-second metrics are available for 15 days.
- 5-minute metrics are available for 63 days.
- 1-hour metrics are available for 455 days (15 months).

When you call `getMetricData` you can specify a period of 1, 5
(recommended), 10, 30 or any multiple of 60 seconds for high-resolution metrics.

### CloudWatch Console

Instructions

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the side navigation, expand the **Metrics** dropdown, then select **All
   metrics**.
3. On the **Browse** tab, using the unlabeled
   dropdown at the left, select your “home” region, where your channel(s)
   was(were) created. For more on regions, see [Global
   Solution, Regional Control](what-is.md#what-is-aws "what-is.md#what-is-aws"). For a list of supported regions, see
   the [Amazon IVS page](../../../general/latest/gr/ivs.md "../../../general/latest/gr/ivs.md") in the _AWS General
   Reference_.
4. At the bottom of the **Browse** tab, select
   the **IVS** namespace.
5. Do one of the following:
   1. In the search bar, enter your resource ID (part of the ARN,
      `arn:::ivs:channel/<resource id>`).

   Then select **IVS > By
   Channel**. 2. If **IVS** appears as a selectable
   service under **AWS Namespaces**,
   select it. It will be listed if you use Amazon IVS and it is sending
   metrics to Amazon CloudWatch. (If **IVS** is not listed, you do not have any Amazon IVS
   metrics.)

   Then choose a _dimension_
   grouping as desired; available dimensions are listed in [CloudWatch Metrics](#stream-health-cloudwatch-metrics-low-latency-streaming "#stream-health-cloudwatch-metrics-low-latency-streaming") below.

6. Choose metrics to add to the graph. Available metrics are listed in [CloudWatch Metrics](#stream-health-cloudwatch-metrics-low-latency-streaming "#stream-health-cloudwatch-metrics-low-latency-streaming") below.

You also can access your stream session’s CloudWatch chart from the stream
session’s details page, by selecting the **View in
CloudWatch** button.

### CLI Instructions

You also can access the metrics using the AWS CLI. This requires that you first
download and configure the CLI on your machine. For details, see the [AWS
Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

Then, to access Amazon IVS low-latency streaming metrics using the AWS CLI:

- At a command prompt, run:

```
aws cloudwatch list-metrics --namespace AWS/IVS
```

For more information, see [Using Amazon
CloudWatch Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") in the _Amazon CloudWatch User
Guide_.

## CloudWatch

Metrics: IVS Low-Latency Streaming

Amazon IVS provides the following metrics in the **AWS/IVS** namespace.

| Metric               | Dimensions                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ConcurrentViews`    | —                              | A count of concurrent views across all your live channels. A<br>\*view<br>• is a unique viewing<br>session which is actively downloading or playing video. (For a more<br>detailed definition, see the [IVS Glossary](ivs-glossary.md "ivs-glossary.md").) If channels are live but in<br>aggregate have no views, the value of this metric is 0. If no<br>channels are live, the metric has no data points.<br>Unit: Count<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of concurrent<br>views over the configured interval.                                         |
| `ConcurrentViews`    | `Channel`                      | Filters `ConcurrentViews` by channel ARN. If a channel<br>is live but has no views, the value of this metric is 0. If a<br>channel is not live, the metric has no data points.<br>This metric provides data for a channel, not a stream. To see<br>concurrent views for a particular streaming session on a given<br>channel, evaluate the `ConcurrentViews` metric for that<br>channel between the start and end times of the streaming<br>session.<br>Unit: Count<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of concurrent<br>views over the configured interval. |
| `ConcurrentStreams`  | —                              | A count of your channels which are streaming live. If no channels<br>are live, this metric has no data points.<br>Unit: Count<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of concurrent<br>streams over the configured interval.                                                                                                                                                                                                                                                                                                                                     |
| `ConcurrentStreams`  | `Health`                       | Filters `ConcurrentStreams` by channel health. If no<br>channels are live, this metric has no data points.<br>Unit: Count<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of concurrent<br>streams for a specific `Health` over the configured<br>interval.                                                                                                                                                                                                                                                                                                              |
| `IngestAudioBitrate` | `Channel`                      | \*_(High-resolution metric)_<br>• The<br>amount of audio data Amazon IVS receives when you stream. A higher<br>bitrate takes up more of your available internet bandwidth.<br>Unit: Bits/second<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of ingest audio<br>bitrates over the configured interval                                                                                                                                                                                                                                                                 |
| `IngestAudioBitrate` | `Channel, Track`               | \*_(High-resolution metric)_<br>• The<br>amount of audio data Amazon IVS receives when you stream. A higher<br>bitrate takes up more of your available internet bandwidth.<br>Unit: Bits/second<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of ingest audio<br>bitrates over the configured interval                                                                                                                                                                                                                                                                 |
| `IngestBitrate`      | —                              | \*_(High-resolution metric)_<br>• The<br>amount of video, audio and metadata (summed over all tracks) Amazon<br>IVS receives when you stream. A higher bitrate takes up more of your<br>available internet bandwidth.<br>Unit: Bits/second<br>Average, Maximum, Minimum — Average number, largest number, or<br>smallest number (respectively) of ingest bitrates over the<br>configured interval                                                                                                                                                                                                                                              |
| `IngestBitrate`      | `Channel`                      | \*_(High-resolution metric)_<br>• The<br>amount of video, audio and metadata (summed over all tracks) Amazon<br>IVS receives when you stream. A higher bitrate takes up more of your<br>available internet bandwidth.<br>Unit: Bits/second<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of ingest bitrates<br>over the configured interval                                                                                                                                                                                                                            |
| `IngestFramerate`    | —                              | \*_(High-resolution metric)_<br>• How<br>often video frames are received by Amazon IVS when you<br>stream.<br>Unit: Count/second<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of ingest<br>framerates over the configured interval                                                                                                                                                                                                                                                                                                                                    |
| `IngestFramerate`    | `Channel`                      | \*_(High-resolution metric)_<br>• How<br>often video frames are received by Amazon IVS when you<br>stream.<br>Unit: Count/second<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of ingest<br>framerates over the configured interval                                                                                                                                                                                                                                                                                                                                    |
| `IngestFramerate`    | `Channel, Track`               | \*_(High-resolution metric)_<br>• How<br>often video frames are received by Amazon IVS when you<br>stream.<br>Unit: Count/second<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of ingest<br>framerates over the configured interval                                                                                                                                                                                                                                                                                                                                    |
| `IngestVideoBitrate` | `Channel`                      | \*_(High-resolution metric)_<br>• The<br>amount of video data Amazon IVS receives when you stream. A higher<br>bitrate takes up more of your available internet bandwidth. Higher<br>bitrate can improve video quality, but only up to a certain<br>point.<br>Unit: Bits/second<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of ingest video<br>bitrates over the configured interval                                                                                                                                                                                 |
| `IngestVideoBitrate` | `Channel, Track`               | \*_(High-resolution metric)_<br>• The<br>amount of video data Amazon IVS receives when you stream. A higher<br>bitrate takes up more of your available internet bandwidth. Higher<br>bitrate can improve video quality, but only up to a certain<br>point.<br>Unit: Bits/second<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of ingest video<br>bitrates over the configured interval                                                                                                                                                                                 |
| `KeyframeInterval`   | `Channel`                      | \*_(High-resolution metric)_<br>• The<br>point in the video stream where the entire frame is sent instead of<br>just the differences from the previous frame.<br>Unit: Seconds<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of keyframe<br>intervals over the configured interval                                                                                                                                                                                                                                                                                     |
| `KeyframeInterval`   | `Channel, Track`               | \*_(High-resolution metric)_<br>• The<br>point in the video stream where the entire frame is sent instead of<br>just the differences from the previous frame.<br>Unit: Seconds<br>Valid statistics: Average, Maximum, Minimum — Average number,<br>largest number, or smallest number (respectively) of keyframe<br>intervals over the configured interval                                                                                                                                                                                                                                                                                     |
| `LiveDeliveredTime`  | —                              | Total real-time duration of video served to all viewers.<br>Unit: Seconds<br>Valid statistic: Sum                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `LiveDeliveredTime`  | `Channel`                      | Filters `LiveDeliveredTime` by channel. Channel<br>values are the channel's `resource-id`, which is the last<br>part of an [ARN](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md").<br>Unit: Seconds<br>Valid statistic: Sum                                                                                                                                                                                                                                                                                                                                                                  |
| `LiveDeliveredTime`  | `Channel`, `ViewerCountryCode` | Filters `LiveDeliveredTime` by channel and viewer’s<br>country code. Channel values are the channel's<br>`resource-id`, which is the last part of an [ARN](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). Country values are two-character ISO 3166-1<br>country codes. This allows you to answer the question: where are my<br>viewers watching from? If the viewer’s country cannot be determined,<br>it is shown as `UNKNOWN`.<br>Unit: Seconds<br>Valid statistic: Sum                                                                                                                |
| `LiveInputTime`      | —                              | Real-time duration of video stream.<br>Unit: Seconds<br>Valid statistic: Sum                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `LiveInputTime`      | `Channel`                      | Filters `LiveInputTime` by channel. Channel values<br>are the channel's `resource-id`, which is the last part<br>of an [ARN](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md").<br>Unit: Seconds<br>Valid statistic: Sum                                                                                                                                                                                                                                                                                                                                                                      |
| `RecordedTime`       | —                              | Real-time duration of recorded video.<br>Unit: Seconds<br>Valid statistic: Sum                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `RecordedTime`       | `Channel`                      | Filters `RecordedTime` by channel. Channel values<br>are the channel's `resource-id`, which is the last part<br>of an [ARN](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md").<br>Unit: Seconds<br>Valid statistic: Sum                                                                                                                                                                                                                                                                                                                                                                       |
