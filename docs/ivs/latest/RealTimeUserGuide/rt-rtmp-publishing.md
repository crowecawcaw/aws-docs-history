

# IVS RTMP Publishing \| Real-Time Streaming
<a name="rt-rtmp-publishing"></a>

This document outlines the process of publishing to an IVS stage using RTMP. For additional details on various ingest options, refer to the [Stream Ingest](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html) documentation

## Prerequisites
<a name="rtmp-prerequisites"></a>

### Create a Stage
<a name="rtmp-create-stage"></a>

To create a stage, use the following command:

`aws ivs-realtime create-stage --name "test-stage"`

See [CreateStage](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateStage.html) for details, including the response.

**Important:** In the response, note the `endpoints` field, which lists both RTMP and RTMPS endpoints. These are required for setting up your RTMP encoder.

### Create an Ingest Configuration
<a name="rtmp-create-an-ingest-configuration"></a>

To publish to a stage using RTMPS, you must first create an ingest configuration and associate it with your stage. When you publish to the stage (using the stream key from the ingest configuration and the RTMP endpoint from the stage), the media will be published to the stage as a participant. You have the option to specify a `userId` and custom `attributes`, which will be associated with the [participant](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_Participant.html) that connects to the stage.

```
aws ivs-realtime create-ingest-configuration \
  --name 'test' \
  --stage-arn arn:aws:ivs:us-east-1:123456789012:stage/8faHz1SQp0ik \
  --user-id '123' \
  --ingest-protocol 'RTMPS'
```

See [CreateIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateIngestConfiguration.html) for details, including the response.

When creating an ingest configuration, you can associate it with a specific stage ARN up front. Without this association, the stream key is unusable. Also, ingest configurations (including the `stageArn` field) can be updated via the [UpdateIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_UpdateIngestConfiguration.html) operation, allowing you to reuse the same configuration for different stages.

**Note:** The ingest configuration `insecureIngest` field defaults to `false`, requiring the use of RTMPS. RTMP connections will be rejected. If you must use RTMP, set `insecureIngest` to `true`. We recommend using RTMPS unless you have specific and verified use cases that require RTMP.

## RTMP Single-Track Video
<a name="rtmp-singletrack"></a>

Below we describe how to use OBS Studio; however, you can use any RTMP encoder that meets the IVS [media specifications](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html#supported-media-specifications).

### OBS Guide
<a name="rtmp-singletrack-obs"></a>

1. Download and install the software: [https://obsproject.com/download](https://obsproject.com/download).

1. Click **Settings**. In the **Stream** section of the **Settings** panel, select **Custom** from the **Service** dropdown.

1. For the **Server**, enter the RTMP or RTMPS endpoint from the stage.

1. For the **Stream Key**, enter the `streamKey` from the ingest configuration.

1. Configure your video settings as you normally would, with a few restrictions:

   1. IVS real-time streaming supports input up to 720p at 8.5 Mbps. If you exceed either of these limits, your stream will be disconnected.

   1. We recommend setting your **Keyframe Interval** in the **Output** panel to 1s or 2s. A low keyframe interval allows video playback to start more quickly for viewers. We also recommend setting **CPU Usage Preset** to **veryfast** and **Tune** to **zerolatency**, to enable the lowest latency.

   1. Because OBS does not support simulcast, we recommend keeping your bitrate below 2.5 Mbps. This enables viewers on lower-bandwidth connections to watch.

   1. Disable B-frames, as streams with B-frames will be automatically disconnected. Do one of the following:
      + In x264 options, enter `bframes=0 sliced-threads=0`.
      + Set B-frames to 0 if it is an option (e.g., for NVENC).

   Note: RTMP streams must include both audio and video tracks, or they will be disconnected.

1. Select **Start Streaming**

**Important:** If your encoder’s maximum bitrate is set to 8.5 Mbps, the publisher occasionally disappears from the session. This is because the maximum bitrate setting is only a target, and encoders occasionally go over the target. To prevent this, set your encoder’s maximum bitrate lower; e.g. to 6 Mbps.

## E-RTMP Multitrack Video
<a name="rtmp-multitrack"></a>

IVS supports the multitrack video capability of E-RTMP (Enhanced Real-Time Messaging Protocol), which allows you to publish multiple video qualities in a single RTMP stream to your IVS stage. This enables adaptive bitrate streaming, so subscribers can automatically watch in the best quality for their network connection.

Once ingested, the different video qualities are delivered to subscribers as simulcast layers. To configure which layers are received by subscribers, see the "Layered Encoding with Simulcast" sections in the real-time streaming broadcast SDK guides: [Android](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-android.html), [iOS](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-ios.html), and [Web](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/broadcast-web.html).

For sample code, see [aws-samples/sample-amazon-ivs-multitrack-video](https://github.com/aws-samples/sample-amazon-ivs-multitrack-video) on GitHub.

This diagram illustrates how publishing with multitrack video works:

![Publishing multitrack video to a stage."](http://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/images/E-RTMP.png)


### OBS Guide
<a name="rtmp-multitrack-obs"></a>

1. Download and install OBS Studio:

   1. Windows: Multitrack video is supported starting in OBS Studio 30.2.

   1. macOS: Multitrack video is supported starting in OBS Studio 31.1 Beta (Apple Silicon only).

   1. Download at: [https://obsproject.com/download](https://obsproject.com/download).

1. Click **Settings**. In the **Stream** section of the **Settings** panel, select **Amazon IVS** from the **Service** dropdown.

1. For the **Server**, leave the setting as **Auto**.

1. For the **Stream Key**, enter the `streamKey` from the ingest configuration.

1. Under the **Multitrack Video** section, check **Enable Multitrack Video**.

1. In the **Video** panel, set the desired **Base (Canvas Resolution)** and **Output (Scaled) Resolution**. IVS real-time streaming supports input up to 720p. If you exceed this limit, your stream will be disconnected.

   When multitrack video is enabled, settings such as the number of video tracks, their bitrates, and the keyframe interval are automatically configured based on the device’s capabilities.

1. Select **Start Streaming**.

### Publishing with FFmpeg
<a name="rtmp-multitrack-ffmpeg"></a>

You can use FFmpeg to publish live video and audio to IVS real-time streaming over RTMP. FFmpeg is a free, open-source project comprising a comprehensive suite of software libraries and tools for processing video, audio, and other multimedia content.

The following example command publishes a stream that includes a color pattern and a tone:

```
ffmpeg \
 -re \
 -f lavfi -i testsrc=d=300:s=1280x720:r=60,format=yuv420p \
 -f lavfi -i sine=f=440:b=4:d=300 \
 -c:v libx264 \
 -b:v 2500k \
 -g 60 -bf 0 \
 -profile:v baseline \
 -preset veryfast \
 -tune zerolatency \
 -x264opts sliced-threads=0 \
 -c:a aac \
 -ac 2 \
 -b:a 160k \
 -ar 48000 \
 -f flv \
 rtmps://$INGEST_ENDPOINT/app/$STREAM_KEY
```

In the example, replace `$INGEST_ENDPOINT` and `$STREAM_KEY` with your own values from the IVS console or API.

This configuration meets the [Supported Media Specifications](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html#supported-media-specifications) for IVS real-time streaming, including H.264 video (baseline profile, no B-frames, no sliced threads) and AAC audio.

## Private Ingest to Stages
<a name="private-ingest-stages"></a>

You can publish RTMP(S) and E-RTMP(S) streams to a stage from resources inside your Amazon VPC or from Direct Connect, by using an interface VPC endpoint. This enables a private connection between your VPC and IVS, keeping ingest traffic within the AWS network. To set up and configure an interface VPC endpoint for IVS, see [IVS Private Ingest](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-ingest-ll.html) in the *IVS Low-Latency Streaming User Guide*. 

## Redundant Ingest
<a name="redundant-ingest"></a>

Redundant ingest enables streaming from two separate encoders simultaneously to a single stage, with automated failover for the same source media. This helps protect against source encoder failures and first-mile network issues. Redundant ingest is supported for RTMP(S) and E-RTMP(S) streams.

To enable redundant ingest, set `redundantIngest` to `true` when creating your ingest configuration via [CreateIngestConfiguration](https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateIngestConfiguration.html). IVS provides two RTMP stream keys. Configure two separate encoders using the same ingest endpoint with their respective stream keys.

Each physical stream appears as a separate participant in participant APIs (e.g., ListParticipants). However, subscribers can subscribe to only one virtual participant, identified by the top-level `participantId` in the ingest configuration. IVS automatically controls which physical stream is used for the virtual participant. If you enable individual participant recording, each physical participant is recorded separately. If you enable server-side composition, only the virtual participant appears in the composition.

Redundant ingest also enables continuous 24/7 streaming. IVS limits individual publishers to 24 hours, but with redundant ingest, IVS staggers the connection timeouts between the two physical streams and automatically switches which stream is used for the virtual participant, allowing subscribers to experience uninterrupted 24/7 streaming.

### Requirements
<a name="redundant-ingest-requirements"></a>
+ Streams must be genlocked and must maintain matching encoding parameters (including resolution and frame rate) to ensure uninterrupted switchover.

### Recommendations
<a name="redundant-ingest-recommendations"></a>
+ Use independent network connections with diverse network paths (e.g., different ISPs) for each encoder, to maximize protection against first-mile network issues and avoid single points of failure.
+ Maintain active streams from both encoders.
+ Test failover scenarios before production use.