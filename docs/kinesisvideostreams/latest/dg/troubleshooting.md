# Troubleshooting Kinesis Video Streams

Use the following information to troubleshoot common issues encountered with
Amazon Kinesis Video Streams.

###### Topics

- [General issues](#troubleshooting-general "#troubleshooting-general")
- [API issues](#troubleshooting-api "#troubleshooting-api")
- [HLS issues](#troubleshooting-hls "#troubleshooting-hls")
- [Java issues](#troubleshooting-java "#troubleshooting-java")
- [Producer library issues](#troubleshooting-producer "#troubleshooting-producer")
- [Stream parser library issues](#troubleshooting-parser "#troubleshooting-parser")
- [Network issues](#troubleshooting-network "#troubleshooting-network")

## General issues

This section describes general issues that you might encounter when working with
Kinesis Video Streams.

###### Issues

- [Latency too high](#troubleshooting-general-latency "#troubleshooting-general-latency")

### Latency too high

Latency might be caused by the duration of fragments that are sent to the Kinesis Video Streams
service. One way to reduce the latency between the producer and the service is to
configure the media pipeline to produce shorter fragment durations.

To reduce the number of frames sent in each fragment, reduce the following value in
`kinesis_video_gstreamer_sample_app.cpp`:

```
g_object_set(G_OBJECT (data.encoder), "bframes", 0, "key-int-max", `45`, "bitrate", 512, NULL);
```

###### Note

Latencies are higher in the Mozilla Firefox browser due to the internal
implementation of video rendering.

## API issues

This section describes API issues that you might encounter when working with
Kinesis Video Streams.

###### Issues

- [Error: "Unknown options"](#troubleshooting-api-unknown-options "#troubleshooting-api-unknown-options")
- [Error: "Unable to determine
  service/operation name to be authorized"](#troubleshooting-api-name-auth "#troubleshooting-api-name-auth")
- [Error: "Failed to put a frame in the
  stream"](#troubleshooting-api-putframe "#troubleshooting-api-putframe")
- [Error: "Service closed
  connection before final AckEvent was received"](#troubleshooting-api-closeconnection "#troubleshooting-api-closeconnection")
- [Error:
  "STATUS_STORE_OUT_OF_MEMORY"](#troubleshooting-api-storeoutofmemory "#troubleshooting-api-storeoutofmemory")
- [Error: "Credential should be scoped to a valid region."](#troubleshoot-api-credential "#troubleshoot-api-credential")

### Error: "Unknown options"

`GetMedia` and `GetMediaForFragmentList` can fail with the
following error:

```
Unknown options: <filename>.mkv
```

This error occurs if you configured the AWS CLI with an `output` type of
`json`. Reconfigure the AWS CLI with the default output type
(`none`). For information about configuring the AWS CLI, see [configure](../../../cli/latest/reference/configure.md "../../../cli/latest/reference/configure.md") in the
_AWS CLI Command Reference_.

### Error: "Unable to determine

service/operation name to be authorized"

`GetMedia` can fail with the following error:

```
Unable to determine service/operation name to be authorized
```

This error might occur if the endpoint is not properly specified. When you're getting the endpoint, be
sure to include the following parameter in the `GetDataEndpoint` call, depending on the API to be
called:

```
--api-name GET_MEDIA
--api-name PUT_MEDIA
--api-name GET_MEDIA_FOR_FRAGMENT_LIST
--api-name LIST_FRAGMENTS
```

### Error: "Failed to put a frame in the

stream"

`PutMedia` can fail with the following error:

```
Failed to put a frame in the stream
```

This error might occur if connectivity or permissions are not available to the
service. Run the following in the AWS CLI, and verify that the stream information can
be retrieved:

```
aws kinesisvideo describe-stream --stream-name `StreamName` --endpoint `https://ServiceEndpoint.kinesisvideo.region.amazonaws.com`
```

If the call fails, see [Troubleshooting AWS CLI Errors](../../../cli/latest/userguide/troubleshooting.md "../../../cli/latest/userguide/troubleshooting.md") for more information.

### Error: "Service closed

connection before final AckEvent was received"

`PutMedia` can fail with the following error:

```
com.amazonaws.SdkClientException: Service closed connection before final AckEvent was received
```

This error might occur if `PushbackInputStream` is improperly implemented. Verify that the
`unread()` methods are correctly implemented.

### Error:

"STATUS_STORE_OUT_OF_MEMORY"

`PutMedia` can fail with the following error:

```
The content store is out of memory.
```

This error occurs when the content store is not allocated with sufficient size. To
increase the size of the content store, increase the value of
`StorageInfo.storageSize`. For more information, see [StorageInfo](producer-reference-structures-producer.md#producer-reference-structures-producer-storageinfo "producer-reference-structures-producer.md#producer-reference-structures-producer-storageinfo").

### Error: "Credential should be scoped to a valid region."

This error occurs if the signing region doesn't match the endpoint region.

For example, if you specify `us-west-2` as your signing region, but
try to connect to the `kinesisvideo.us-east-1.amazonaws.com`
(`us-east-1`) endpoint, you'll receive this error.

In some applications, like [kvssink](examples-gstreamer-plugin.md "examples-gstreamer-plugin.md"), the region fallback chain defaults to `us-west-2`. Verify you set your region correctly according to the application you're using.

## HLS issues

If your video stream doesn't play back correctly, see [Troubleshooting HLS issues](hls-playback.md#how-hls-ex1-ts "hls-playback.md#how-hls-ex1-ts").

## Java issues

This section describes how to troubleshoot common Java issues encountered when working
with Kinesis Video Streams.

###### Issues

- [Enabling Java logs](#troubleshooting-java-log "#troubleshooting-java-log")

### Enabling Java logs

To troubleshoot issues with Java samples and libraries, it's helpful to enable and examine the debug
logs. To enable debug logs, do the following:

1. Add `log4j` to the `pom.xml` file, in
   the `dependencies` node:

```
<dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.17</version>
</dependency>

```

2. In the `target/classes` directory, create a file named
   `log4j.properties` with the following
   contents:

```
# Root logger option
log4j.rootLogger=DEBUG, stdout

# Redirect log messages to console
log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.Target=System.out
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n

log4j.logger.org.apache.http.wire=DEBUG

```

The debug logs then print to the IDE console.

## Producer library issues

This section describes issues that you might encounter when using the [Upload to Kinesis Video Streams](producer-sdk.md "producer-sdk.md").

###### Issues

- [Cannot compile the producer SDK](#troubleshooting-producer-compile "#troubleshooting-producer-compile")
- [Video stream does not appear in the
  console](#troubleshooting-producer-console "#troubleshooting-producer-console")
- [Error: "Security
  token included in the request is invalid" when streaming data using the
  GStreamer demo application](#troubleshooting-producer-general-securitytoken "#troubleshooting-producer-general-securitytoken")
- [Error: "Failed to
  submit frame to Kinesis Video client"](#troubleshooting-producer-failed-frame-client "#troubleshooting-producer-failed-frame-client")
- [GStreamer application
  stops with "streaming stopped, reason not-negotiated" message on OS X](#troubleshooting-producer-failed-stream-osx "#troubleshooting-producer-failed-stream-osx")
- [Error: "Failed to
  allocate heap" when creating Kinesis Video Client in GStreamer demo on Raspberry
  Pi](#troubleshooting-producer-raspberrypi-heap "#troubleshooting-producer-raspberrypi-heap")
- [Error:
  "Illegal Instruction" when running GStreamer demo on Raspberry Pi](#troubleshooting-producer-raspberrypi-illegalinstruction "#troubleshooting-producer-raspberrypi-illegalinstruction")
- [Camera fails to load
  on Raspberry Pi](#troubleshooting-producer-raspberrypi-camera "#troubleshooting-producer-raspberrypi-camera")
- [Camera can't be found on
  macOS High Sierra](#troubleshooting-producer-sierra-camera "#troubleshooting-producer-sierra-camera")
- [jni.h file not found when
  compiling on macOS High Sierra](#troubleshooting-producer-sierra-compile "#troubleshooting-producer-sierra-compile")
- [Curl errors when running the
  GStreamer demo application](#troubleshooting-producer-curl "#troubleshooting-producer-curl")
- [Timestamp/range assertion at runtime on Raspberry Pi](#troubleshooting-producer-raspberrypi-timestamp-assert "#troubleshooting-producer-raspberrypi-timestamp-assert")
- [Assertion on
  gst_value_set_fraction_range_full on Raspberry Pi](#troubleshooting-producer-raspberrypi-gst-assert "#troubleshooting-producer-raspberrypi-gst-assert")
- [STATUS_MKV_INVALID_ANNEXB_NALU_IN_FRAME_DATA (0x3200000d) error on
  Android](#troubleshooting-producer-android-invalid-annexb "#troubleshooting-producer-android-invalid-annexb")
- [Maximum fragment duration was reached error](#troubleshooting-producer-maxfragmentduration "#troubleshooting-producer-maxfragmentduration")
- ["Invalid thing name passed" error
  when using IoT authorization](#troubleshooting-producer-thingname "#troubleshooting-producer-thingname")

### Cannot compile the producer SDK

Verify that the required libraries are in your path. To verify this, use the
following command:

```
env | grep LD_LIBRARY_PATH
LD_LIBRARY_PATH=/home/local/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/kinesis-video-native-build/downloads/local/lib
```

### Video stream does not appear in the

console

To display your video stream in the console, it must be encoded using H.264 in
AvCC format. If your stream is not displayed, verify the following:

- Your [NAL adaptation flags](producer-reference-nal.md "producer-reference-nal.md") are set to
  `NAL_ADAPTATION_ANNEXB_NALS | NAL_ADAPTATION_ANNEXB_CPD_NALS`
  if the original stream is in Annex-B format. This is the default value in
  the `StreamDefinition` constructor.
- You are providing the codec private data correctly. For H.264, this is the
  sequence parameter set (SPS) and picture parameter set (PPS). Depending on
  your media source, this data may be retrieved from the media source
  separately or encoded into the frame.

Many elementary streams are in the following format, where `Ab`
is the Annex-B start code (001 or 0001):

```
Ab(Sps)Ab(Pps)Ab(I-frame)Ab(P/B-frame) Ab(P/B-frame)…. Ab(Sps)Ab(Pps)Ab(I-frame)Ab(P/B-frame) Ab(P/B-frame)
```

The CPD (Codec Private Data), if H.264 is in the stream as SPS and PPS, can be adapted to the
AvCC format. Unless the media pipeline gives the CPD separately, the application can extract the CPD from
the frame by looking for the first Idr frame (which should contain the SPS and PPS), extract the two NALUs
(which will be Ab(Sps)Ab(Pps)) and set it in the CPD in `StreamDefinition`.

### Error: "Security

token included in the request is invalid" when streaming data using the
GStreamer demo application

If this error occurs, there is an issue with your credentials. Verify the
following:

- If you are using temporary credentials, you must specify the session
  token.
- Verify that your temporary credentials are not expired.
- Verify that you have the proper rights set up.
- On macOS, verify that you do not have credentials cached in
  Keychain.

### Error: "Failed to

submit frame to Kinesis Video client"

If this error occurs, the timestamps are not properly set in the source stream.
Try the following:

- Use the latest SDK sample, which might have an update that fixes your
  issue.
- Set the high-quality stream to a higher bitrate, and fix any jitter in the source stream if
  the camera supports doing so.

### GStreamer application

stops with "streaming stopped, reason not-negotiated" message on OS X

Streaming may stop on OS X with the following message:

```
Debugging information: gstbasesrc.c(2939): void gst_base_src_loop(GstPad *) (): /GstPipeline:test-pipeline/GstAutoVideoSrc:source/GstAVFVideoSrc:source-actual-src-avfvide:
streaming stopped, reason not-negotiated (-4)
```

A possible workaround for this is to remove the frame rate parameters from the
`gst_caps_new_simple` call in `kinesis_video_gstreamer_sample_app.cpp`:

```
GstCaps *h264_caps = gst_caps_new_simple("video/x-h264",
                                             "profile", G_TYPE_STRING, "baseline",
                                             "stream-format", G_TYPE_STRING, "avc",
                                             "alignment", G_TYPE_STRING, "au",
                                             "width", GST_TYPE_INT_RANGE, 320, 1920,
                                             "height", GST_TYPE_INT_RANGE, 240, 1080,
                                             `"framerate", GST_TYPE_FRACTION_RANGE, 0, 1, 30, 1,`
                                             NULL);
```

### Error: "Failed to

allocate heap" when creating Kinesis Video Client in GStreamer demo on Raspberry
Pi

The GStreamer sample application tries to allocate 512 MB of RAM, which might not
be available on your system. You can reduce this allocation by reducing the
following value in `KinesisVideoProducer.cpp`:

```
device_info.storageInfo.storageSize = `512` * 1024 * 1024;
```

### Error:

"Illegal Instruction" when running GStreamer demo on Raspberry Pi

If you encounter the following error when running the GStreamer demo, verify that you have compiled
the application for the correct version of your device. (For example, verify that you're not compiling for
Raspberry Pi 3 when you're running on Raspberry Pi 2.)

```
INFO - Initializing curl.
Illegal instruction
```

### Camera fails to load

on Raspberry Pi

To check whether the camera is loaded, run the following:

```
ls /dev/video*
```

If nothing is found, run the following:

```
vcgencmd get_camera
```

The output should look similar to the following:

```
supported=1 detected=1
```

If the driver does not detect the camera, do the following:

1. Check the physical camera setup and verify that it's connected
   properly.
2. Run the following to upgrade the firmware:

```
sudo rpi-update
```

3. Restart the device.
4. Run the following to load the driver:

```
sudo modprobe bcm2835-v4l2
```

5. Verify that the camera was detected:

```
ls /dev/video*
```

### Camera can't be found on

macOS High Sierra

On macOS High Sierra, the demo application can't find the camera if more than one
camera is available.

### jni.h file not found when

compiling on macOS High Sierra

To resolve this error, update your installation of Xcode to the latest
version.

### Curl errors when running the

GStreamer demo application

To resolve curl errors when you run the GStreamer demo application, copy [this certificate
file](https://www.amazontrust.com/repository/SFSRootCAG2.pem "https://www.amazontrust.com/repository/SFSRootCAG2.pem") to `/etc/ssl/cert.pem`.

### Timestamp/range assertion at runtime on Raspberry Pi

If a timestamp range assertion occurs at runtime, update the firmware and restart
the device:

```
sudo rpi-update
$ sudo reboot
```

### Assertion on

gst_value_set_fraction_range_full on Raspberry Pi

The following assertion appears if the `uv4l` service is running:

```
gst_util_fraction_compare (numerator_start, denominator_start, numerator_end, denominator_end) < 0' failed
```

If this occurs, stop the `uv4l` service and restart the
application.

### STATUS_MKV_INVALID_ANNEXB_NALU_IN_FRAME_DATA (0x3200000d) error on

Android

The following error appears if the [NAL adaptation flags](producer-reference-nal.md "producer-reference-nal.md") are incorrect for the media
stream:

```
putKinesisVideoFrame(): Failed to put a frame with status code 0x3200000d
```

If this error occurs, provide the correct `.withNalAdaptationFlags`
flag for your media (for example, `NAL_ADAPTATION_ANNEXB_CPD_NALS`).
Provide this flag in the following line of the [Android](producer-sdk-android.md "producer-sdk-android.md"):

[https://github.com/awslabs/aws-sdk-android-samples/blob/master/AmazonKinesisVideoDemoApp/src/main/java/com/amazonaws/kinesisvideo/demoapp/fragment/StreamConfigurationFragment.java#L169](https://github.com/awslabs/aws-sdk-android-samples/blob/master/AmazonKinesisVideoDemoApp/src/main/java/com/amazonaws/kinesisvideo/demoapp/fragment/StreamConfigurationFragment.java#L169 "https://github.com/awslabs/aws-sdk-android-samples/blob/master/AmazonKinesisVideoDemoApp/src/main/java/com/amazonaws/kinesisvideo/demoapp/fragment/StreamConfigurationFragment.java#L169")

### Maximum fragment duration was reached error

This error occurs when a media fragment in a stream exceeds the maximum fragment
duration limit. See the maximum fragment duration limit in the [Media and archived-media API service quotas](limits.md#limits-akv-data "limits.md#limits-akv-data") section.

To resolve this issue, try the following:

- If you are using a webcam/USB camera, do one of the following:
  - If you're using key frame-based fragmentation, then set the encoder to provide key
    frames within 10 seconds.
  - If you're not using key frame-based fragmentation, then when defining the stream in
    [Write and examine the code](producersdk-cpp-write.md "producersdk-cpp-write.md"), set the maximum
    fragment duration limit to a value that's less than 10 seconds.
  - If you're using software encoders (like x264) in the GStreamer pipeline, you can set
    the key-int-max attribute to a value within 10 seconds. For example, set key-int-max to 60, with fps set
    to 30, to enable key frames every 2 seconds.

- If you're using an RPI camera, set the keyframe-interval attribute to be less than 10
  seconds.
- If you're using an IP (RTSP) camera, set the GOP size to 60.

### "Invalid thing name passed" error

when using IoT authorization

To avoid this error (`HTTP Error 403: Response: {"message":"Invalid thing name passed"}`)
when you're using IoT credentials for authorization, make sure that the value of `stream-name` (a
required parameter of the `kvssink` element) is identical to the value of `iot-thingname`.
For more information, see [GStreamer element parameter
reference](examples-gstreamer-plugin-parameters.md "examples-gstreamer-plugin-parameters.md").

## Stream parser library issues

This section describes issues that you might encounter when using the [Stream using parser library](parser-library.md "parser-library.md").

###### Issues

- [Cannot access a single frame from the
  stream](#troubleshooting-parser-frame "#troubleshooting-parser-frame")
- [Fragment decoding error](#troubleshooting-parser-fragment "#troubleshooting-parser-fragment")

### Cannot access a single frame from the

stream

To access a single frame from a streaming source in your consumer application, verify that your stream
contains the correct codec private data. For information about the format of the data in a stream, see [Data model](how-data.md "how-data.md").

To learn how to use codec private data to access a frame, see the following test
file on the GitHub website: [KinesisVideoRendererExampleTest.java](https://github.com/aws/amazon-kinesis-video-streams-parser-library/blob/master/src/test/java/com/amazonaws/kinesisvideo/parser/examples/KinesisVideoRendererExampleTest.java "https://github.com/aws/amazon-kinesis-video-streams-parser-library/blob/master/src/test/java/com/amazonaws/kinesisvideo/parser/examples/KinesisVideoRendererExampleTest.java")

### Fragment decoding error

If your fragments are not properly encoded in an H.264 format and level that the
browser supports, you might see the following error when playing your stream in the
console:

```
Fragment Decoding Error
There was an error decoding the video data. Verify that the stream contains valid H.264 content
```

If this occurs, verify the following:

- The resolution of the frames matches the resolution specified in the Codec
  Private Data.
- The H.264 profile and level of the encoded frames matches the profile and
  level specified in the Codec Private Data.
- The browser supports the profile/level combination. Most current browsers
  support all profile and level combinations.
- The timestamps are accurate and in the correct order, and no duplicate
  timestamps are being created.
- Your application is encoding the frame data using the H.264 format.

## Network issues

If you see connection errors, such as "Connection Timeout" or "Connection Failed",
when attempting to connect to Kinesis Video Streams, it may be due to IP address range restrictions in
your networking setup.

If your setup has IP address range restrictions for Kinesis Video Streams, update your network configuration to allowlist the Kinesis Video Streams [IP address ranges](https://ip-ranges.amazonaws.com/ip-ranges.json "https://ip-ranges.amazonaws.com/ip-ranges.json").

###### Important

The IP range list isn't an exhaustive list of Kinesis Video Streams IP addresses. Include the IP
address ranges you see and be aware that the IP addresses may change over
time.

For more information, see [AWS IP ranges](../../../vpc/latest/userguide/aws-ip-ranges.md "../../../vpc/latest/userguide/aws-ip-ranges.md"). To be
notified when IP ranges change, follow the [subscription
procedure](../../../vpc/latest/userguide/aws-ip-ranges.md#subscribe-notifications "../../../vpc/latest/userguide/aws-ip-ranges.md#subscribe-notifications").
