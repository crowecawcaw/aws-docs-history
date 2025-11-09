# Step 5: Set Up Streaming

Software

You can stream (low-latency) to Amazon IVS with:

- The native [IVS broadcast SDKs](#broadcast-sdk "#broadcast-sdk"), which
  support RTMPS. We recommended this, especially for production scenarios.
- The [Amazon IVS console](#ivs-console "#ivs-console") — This is suitable
  for testing streams.
- Other streaming software and hardware encoders — You can use any streaming
  encoder that supports the RTMP, RTMPS, or SRT protocols. Several examples are
  described below, using Open Broadcast Software (OBS) and FFmpeg with RTMPS and
  SRT. RTMPS enables high security via use of an encrypted TLS stream.
  Key encoder settings are keyframe interval (2 seconds) and resolution/bitrate/frame
  rate (which are interrelated). For more detail on encoder settings, see:

- [Streaming Configuration](streaming-config.md "streaming-config.md") in
  the _Amazon IVS User Guide_
- This blog post: [Setting Up for Streaming with Amazon Interactive Video
  Service](https://aws.amazon.com/blogs/media/setting-up-for-streaming-with-amazon-ivs/ "https://aws.amazon.com/blogs/media/setting-up-for-streaming-with-amazon-ivs/")
  **Notes:**

- The maximum duration of Amazon IVS streams is 48 hours. After that, the stream
  is terminated and the streaming session is disconnected. A successful reconnect
  (automatically or manually) starts a new stream.
- If your encoder stops sending data (e.g., due to a temporary network issue),
  Amazon IVS waits for 30 seconds. If no broadcaster data is received during this
  time, Amazon IVS disconnects.

## Streaming with the Amazon IVS Broadcast SDK

To broadcast from your iOS or Android applications, you can use the Amazon IVS
broadcast SDK. The broadcast SDK leverages the Amazon IVS architecture and will see
continual improvement and new features, alongside Amazon IVS. As a native mobile
broadcast SDK, it is designed to minimize the performance impact on your application
and on the devices with which your users access your application.

| To broadcast from …              | You can use …                           | Notes                                                                                                                                                                           |
| -------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Your Android or iOS applications | Amazon IVS Android or iOS broadcast SDK | As a native mobile broadcast SDK, it is designed to minimize the<br>performance impact on your application and on the devices with which<br>your users access your application. |
| A web environment                | Amazon IVS Web broadcast SDK            | As a web broadcast SDK, the Amazon IVS Web Broadcast SDK allows<br>you to broadcast from web environments using WebRTC. It boasts<br>cross-browser and cross-platform support.  |

For details, see [IVS Broadcast SDK | Low-Latency Streaming](broadcast.md "broadcast.md").

## Streaming with the Amazon IVS Console

1. Open the [Amazon IVS
   console](https://console.aws.amazon.com/ivs "https://console.aws.amazon.com/ivs").

(You can also access the Amazon IVS console through the [AWS Management
Console](https://console.aws.amazon.com "https://console.aws.amazon.com").) 2. In the navigation pane, select **Channels**.
(If the nav pane is collapsed, expand it by selecting the hamburger
icon.) 3. Select the channel to which you want to broadcast, to go to its details
page. 4. Select the **Broadcast** tab. (Tabs are below
the **General Configuration** section.) 5. You will be prompted to grant the IVS console access to your camera and
microphone; **Allow** those permissions. 6. Toward the bottom of the **Broadcast** tab,
use the dropdown boxes to select input devices for the microphone and
camera. 7. To begin streaming, select **Start
broadcasting**. 8. To view the live stream, go to the **Playback** tab.

**Note**: After you start the stream, expect
a brief delay (usually under 30 seconds) before it is viewable in the
playback tab.

You can use this feature to simultaneously broadcast to multiple channels.

**Note**: Streaming from the console consumes
resources, and you will incur live-video input costs. To learn more, see [Live Video Input
Costs](https://aws.amazon.com/ivs/pricing/#Low-Latency_Streaming "https://aws.amazon.com/ivs/pricing/#Low-Latency_Streaming") on the IVS Pricing page.

## Streaming with OBS Studio using RTMPS

([OBS Studio](https://obsproject.com/ "https://obsproject.com/")) is a free, open-source
software suite for recording and live streaming. OBS provides real-time source and
device capture, scene composition, encoding, recording, and streaming.

Follow these steps to get up and running quickly with OBS Studio v30.2 or
later:

1. Download and install the software: [https://obsproject.com/download](https://obsproject.com/download "https://obsproject.com/download").
2. Run the OBS Studio **Auto-Configuration
   Wizard**, which appears when you load OBS Studio for the first
   time. Follow the steps and accept the defaults.
3. At **Stream Information**, choose **Amazon IVS** from the **Service** dropdown and enter the **Stream
   Key**.

If you created the channel with the Amazon IVS console, the **Stream Key** you enter in OBS is the **Stream key** from the console:
`sk_us-west-2_abcd1234efgh5678ijkl`

If you created the channel with the AWS CLI, the **Stream Key** you enter in OBS is the **streamKey value** from the CLI response
`sk_us-west-2_abcd1234efgh5678ijkl`

If your IVS channel is configured for multitrack video input, select
**Enable Multitrack Video**. Optionally,
configure the **Maximum Video Tracks** and
**Maximum Streaming Bandwidth** settings,
which are used to limit automatically configured stream settings. 4. For **Video Output Resolution** and **Bitrate**, refer to [Channel Types](streaming-config.md#streaming-config-settings-channel-types "streaming-config.md#streaming-config-settings-channel-types")
in _Amazon IVS Streaming Configuration_. If
either value chosen by the OBS wizard exceeds the values allowed by Amazon
IVS, you should manually adjust the values to avoid a failed connection to
Amazon IVS. After the wizard completes:

    1. To adjust video resolution, use **Settings >
     Video > Output (Scaled) Resolution**.
    2. To adjust video bitrate, use **Settings >
     Output > Streaming > Video Bitrate**.


    **Note:** This does not affect the
     live stream if you previously checked **Enable
     Multitrack Video**.

5. We recommend a 2-second **Keyframe Interval**
   to improve the stream stability and avoid buffering in the viewer playback.
   After the wizard completes, go to **Settings > Output >
   Output Mode**, select **Advanced**, and on the **Streaming**
   tab, ensure that **Keyframe Interval** is
6.

**Note:** Keyframe Interval is configured
automatically if you previously checked **Enable
Multitrack Video**. 6. In the OBS Studio main window, choose **Start
Streaming**.

For more on streaming with OBS Studio, see [OBS Studio
Quickstart](https://obsproject.com/wiki/OBS-Studio-Quickstart "https://obsproject.com/wiki/OBS-Studio-Quickstart").

You can modify your OBS settings manually later:

1. Choose **Settings > Stream**.
2. Choose **Amazon IVS** from the
   dropdown.
3. Paste in the **Stream Key**.

You can run the wizard again at any time: choose **Tools >
Auto-Configuration Wizard**.

Optionally, in **Settings > General**, enable local
recording to save your live stream for later use. As mentioned earlier, network
issues between the broadcast and AWS or within AWS could result in some data loss
while recording your stream. In these cases, Amazon IVS prioritizes the live stream
over the recording. Recording locally via your streaming tool provides
redundancy.

It’s advisable to check for OBS Studio updates regularly and update to the most
current version. (For instance, if you get a “Failed to connect to server” error,
you may be using an old version of OBS Studio that does not support RTMPS.)

## Streaming with OBS Studio using SRT

Follow these steps to get up and running quickly with the Secure Reliable
Transport protocol:

1. Download and install the software: [https://obsproject.com/download](https://obsproject.com/download "https://obsproject.com/download").
2. Run the OBS Studio **Auto-Configuration
   Wizard**, which appears when you load OBS Studio for the first
   time. Follow the steps and accept the defaults.
3. At **Stream Information**, choose **Custom...** from the **Service** dropdown and enter the **Server
   (Ingest server)** and **Stream
   Key**.

If you created the channel with the AWS CLI:

    * The **Server** you enter in OBS is a
     combination of five things:




    	+ An ingestion protocol: `srt://`
    	+ The **endpoint** from the
    	 `srt` struct in the CLI response:


    	`a1b2c3d4e5f6.srt.live-video.net`
    	+ A port: `9000`
    	+ A streamid, which is the **streamKey
    	 value** from the CLI response:


    	`sk_us-west-2_abcd1234efgh5678ijkl`
    	+ A passphrase, used to encrypt the content. Use this only
    	 if **insecure ingest** is not
    	 enabled.


    	`ZU5A3yrjGAkghUNDr0c5NXBhsPrjlmtcKMNBluh7oImwJQ3ijeyClvMKxlpPcGAMziICJ`
    The complete entry is:


    `srt://a1b2c3d4e5f6.srt.live-video.net:9000?streamid=sk_us-west-2_abcd1234efgh5678ijkl&passphrase=ZU5A3yrjGAkghUNDr0c5NXBhsPrjlmtcKMNBluh7oImwJQ3ijeyClvMKxlpPcGAMziICJ`
    * The **Stream Key** you enter in OBS
     will remain empty for the SRT protocol.

4. For **Video Output Resolution** and **Bitrate**, refer to [Channel Types](streaming-config.md#streaming-config-settings-channel-types "streaming-config.md#streaming-config-settings-channel-types")
   in _Amazon IVS Streaming Configuration_. If
   either value chosen by the OBS wizard exceeds the values allowed by Amazon
   IVS, you should manually adjust the values to avoid a failed connection to
   Amazon IVS. After the wizard completes:
   1. To adjust video resolution, use **Settings >
      Video > Output (Scaled) Resolution**.
   2. To adjust video bitrate, use **Settings >
      Output > Streaming > Video Bitrate**.

5. We recommend a 2-second **Keyframe Interval**
   to improve the stream stability and avoid buffering in the viewer playback.
   After the wizard completes, go to **Settings > Output >
   Output Mode**, select **Advanced**, and on the **Streaming**
   tab, ensure that **Keyframe Interval** is
6.
7. In the OBS Studio main window, choose **Start
   Streaming**.

You can modify your OBS settings manually later:

1. Choose **Settings > Stream**.
2. Choose **Custom** from the dropdown.
3. Paste in the **Server** and/or **Stream Key**.

You can run the wizard again at any time: choose **Tools >
Auto-Configuration Wizard**.

Optionally, in **Settings > General**, enable local
recording to save your live stream for later use. As mentioned earlier, network
issues between the broadcast and AWS or within AWS could result in some data loss
while recording your stream. In these cases, Amazon IVS prioritizes the live stream
over the recording. Recording locally via your streaming tool provides
redundancy.

It’s advisable to check for OBS Studio updates regularly and update to the most
current version. (For instance, if you get a "Failed to connect to server" error,
you may be using an old version of OBS Studio that does not support RTMPS.)

## Streaming a Recorded Video with FFmpeg using

RTMPS

Follow these steps:

1. Download and install FFmpeg: [https://www.ffmpeg.org/download.html](https://www.ffmpeg.org/download.html "https://www.ffmpeg.org/download.html").
2. Set `$VIDEO_FILEPATH` to the location of an MP4 video to
   stream:

```
VIDEO_FILEPATH=/home/test/my_video.mp4
```

3. Set `STREAM_KEY` to your StreamKey **value**:

```
STREAM_KEY=sk_us-west-2_abcd1234efgh5678ijkl
```

4. Set `INGEST_ENDPOINT` to your **ingestEndpoint** (from the AWS CLI):

```
INGEST_ENDPOINT=a1b2c3d4e5f6.global-contribute.live-video.net
```

5. Start streaming with the following terminal command (this is all one
   line):

```
ffmpeg -re -stream_loop -1 -i $VIDEO_FILEPATH -r 30 -c:v libx264 -pix_fmt yuv420p -profile:v main -preset veryfast -x264opts "nal-hrd=cbr:no-scenecut" -minrate 3000 -maxrate 3000 -g 60 -c:a aac -b:a 160k -ac 2 -ar 44100 -f flv rtmps://$INGEST_ENDPOINT:443/app/$STREAM_KEY
```

_Note, the above command is an example. For
production streaming, tune the parameters to your
needs._

## Streaming a Recorded Video with FFmpeg using

SRT

1. Download and install FFmpeg: [https://www.ffmpeg.org/download.html](https://www.ffmpeg.org/download.html "https://www.ffmpeg.org/download.html"). If you are using an
   old/compiled version of FFmpeg, build a new version with the
   `--enable-libsrt` flag.
2. Verify that SRT is available for use in FFmpeg: run the following command
   and ensure that `libsrt` is in the output. If `libsrt`
   is not there, rebuild or get a newer version of FFmpeg which supports
   SRT.

```
ffmpeg -version | grep enable-libsrt
```

3. Set `$VIDEO_FILEPATH` to the location of an MP4 video to
   stream:

```
VIDEO_FILEPATH=/home/test/my_video.mp4
```

4. Set `STREAM_KEY` to your StreamKey **value**:

```
STREAM_KEY=sk_us-west-2_abcd1234efgh5678ijkl
```

5. Set `INGEST_ENDPOINT` to your **endpoint** (from the AWS CLI under the `srt`
   object):

```
INGEST_ENDPOINT=a1b2c3d4e5f6.srt.live-video.net
```

6. Set `PASSPHRASE` to your **passphrase** (from the AWS CLI under the `srt`
   object). Use passphrase only if insecure ingest is not enabled for the
   channel.

```
PASSPHRASE=ZU5A3yrjGAkghUNDr0c5NXBhsPrjlmtcKMNBluh7oImwJQ3ijeyClvMKxlpPcGAMziICJ
```

7. Start streaming with the following terminal command (this is all one
   line):

```
ffmpeg -re -i $VIDEO_FILEPATH -c copy -f mpegts "srt://$INGEST_ENDPOINT:9000?streamid=$STREAM_KEY&passphrase=$PASSPHRASE”
```
