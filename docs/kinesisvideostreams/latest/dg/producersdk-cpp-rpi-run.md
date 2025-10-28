# Stream video to your Kinesis video stream

To run the sample application, you need the following information:

- The name of the stream you created in the [Prerequisites](producersdk-cpp-rpi-prerequisites.md "producersdk-cpp-rpi-prerequisites.md") section.
- The account credentials (access key ID and secret access key) that you created
  in [Create an IAM user with permission to write
  to Kinesis Video Streams](producersdk-cpp-rpi-iam.md "producersdk-cpp-rpi-iam.md").
- GStreamer is able to locate the `kvssink` plugin. See [Download and build the Kinesis Video Streams C++
  producer SDK](producersdk-cpp-rpi-download.md "producersdk-cpp-rpi-download.md") for more information.

1. Set the credentials and region.

```
export AWS_ACCESS_KEY_ID=`YourAccessKey`
export AWS_SECRET_ACCESS_KEY=`YourSecretKey`
export AWS_DEFAULT_REGION=`us-west-2`
```

For other authentication methods, see [Provide credentials to
kvssink](examples-gstreamer-plugin-parameters.md#credentials-to-kvssink "examples-gstreamer-plugin-parameters.md#credentials-to-kvssink").

###### Note

The C++ producer SDK uses the US West (Oregon) (`us-west-2`)
Region by default. To use the default AWS Region create your Kinesis video stream in
the US West (Oregon) Region.

To use a different Region for your Kinesis video stream, set the following
environment variable to your Region (for example,
`us-east-1`):

```
export AWS_DEFAULT_REGION=`us-east-1`
```

2. Depending on your input media, choose one of the following:

Sample GStreamer video
This GStreamer pipeline generates a live test video stream with a
standard test pattern that runs at 10 frames per second with a
resolution of 640x480 pixels. An overlay is added displaying the
current system time and date. The video is then encoded into H.264
format and keyframes are generated at most every 10 frames,
resulting in a fragment duration (also known as a group of pictures
(GoP) size) of 1 second. kvssink takes the H.264-encoded video
stream, packages it into the Matroska (MKV) container format, and
uploads it to your Kinesis video stream.

Run the following command:

```
gst-launch-1.0 -v videotestsrc is-live=true \
  ! video/x-raw,framerate=10/1,width=640,height=480 \
  ! clockoverlay time-format="%a %B %d, %Y %I:%M:%S %p" \
  ! x264enc bframes=0 key-int-max=10 \
  ! h264parse \
  ! kvssink stream-name="`YourStreamName`"
```

To stop the GStreamer pipeline, select the terminal window and
press **CTRL+C**.

The sample video GStreamer pipeline looks like this:

![Image of standard test pattern with overlayed date and time stamp.](images/sample-video.png)

USB web cam
Run the following command to have GStreamer auto-detect your USB
camera:

```
gst-launch-1.0 autovideosrc \
  ! videoconvert \
  ! video/x-raw,format=I420,width=640,height=480 \
  ! x264enc bframes=0 key-int-max=45 tune=zerolatency byte-stream=true speed-preset=ultrafast \
  ! h264parse \
  ! video/x-h264,stream-format=avc,alignment=au,profile=baseline \
  ! kvssink stream-name="`YourStreamname`"

```

To stop the GStreamer pipeline, select the terminal window and
press **CTRL+C**.

Rather than let GStreamer auto-detect, you can use
`v4l2src` with a specific device identifier. Run the
following command:

```
gst-device-monitor-1.0
```

In the output, you’ll see some devices and the start of a
GStreamer pipeline for how to use the device:

```
Device found:

    name  : H264 USB Camera: USB Camera
    class : Video/Source
    caps  : video/x-h264, stream-format=(string)byte-stream, alignment=(string)au, width=(int)1920, height=(int)1080, pixel-aspect-ratio=(fraction)1/1, colorimetry=(string){ 2:4:7:1 }, framerate=(fraction){ 30/1, 25/1, 15/1 };
            ...
    properties:
        device.path = /dev/video4
        udev-probed = false
        device.api = v4l2
        v4l2.device.driver = uvcvideo
        v4l2.device.card = "H264\ USB\ Camera:\ USB\ Camera"
        v4l2.device.bus_info = usb-3f980000.usb-1.3
        v4l2.device.version = 265767 (0x00040e27)
        v4l2.device.capabilities = 2216689665 (0x84200001)
        v4l2.device.device_caps = 69206017 (0x04200001)
    gst-launch-1.0 `v4l2src device=/dev/video4` ! ...
```

To stop the GStreamer pipeline, select the terminal window and
press **CTRL+C**.

Raspberry Pi camera module 1If you’re using the Pi camera module 1 or Pi camera module 2 with `bcm2835-v4l2`, use the following:

```
gst-launch-1.0 v4l2src device=/dev/video0 \
  ! videoconvert \
  ! video/x-raw,format=I420,width=640,height=480 \
  ! x264enc bframes=0 key-int-max=45 bitrate=500 tune=zerolatency \
  ! h264parse ! video/x-h264,stream-format=avc,alignment=au,profile=baseline \
  ! kvssink stream-name="`YourStreamname`"
```

To stop the GStreamer pipeline, select the terminal window and press **CTRL+C**.

Raspberry Pi camera module 2 or 3If you’re using the modern `libcamera` stack, use the following GStreamer pipeline:

```
gst-launch-1.0 libcamerasrc \
  ! video/x-raw,width=640,height=480,framerate=30/1,format=I420 \
  ! videoconvert \
  ! x264enc speed-preset=ultrafast tune=zerolatency byte-stream=true key-int-max=75 \
  ! video/x-h264,level='(string)4' \
  ! h264parse \
  ! video/x-h264,stream-format=avc,alignment=au,width=640,height=480,framerate=30/1 \
  ! kvssink stream-name="`YourStreamname`"
```

To stop the GStreamer pipeline, select the terminal window and press **CTRL+C**.

Sample RTSP camera
For this example, we use Gst-Rtsp-Server to locally host a demo RTSP camera feed. We then construct a GStreamer pipeline to upload that RTSP camera feed to the specified Kinesis video stream.

**To set up Gst-Rtsp-Server on your Raspberry Pi**

    1. Install the necessary dependency libraries to build the Gst-Rtsp-Server project. Make sure you have the software prerequisites installed as well. Type the following into your terminal:



    ```
    sudo apt-get update
    sudo apt-get install libgstrtspserver-1.0
    ```
    2. Download the 1.22 version of GStreamer on your Raspberry Pi.



    ```
    git clone https://gitlab.freedesktop.org/gstreamer/gstreamer.git --single-branch -b 1.22
    ```
    3. Change directories to the examples directory in the gst-rtsp-server.



    ```
    cd gstreamer
    cd subprojects
    cd gst-rtsp-server
    cd examples
    ```
    4. Compile the test-launch.c into an executable called test-launch using gcc.



    ```
    gcc -o test-launch test-launch.c `pkg-config --cflags --libs gstreamer-rtsp-server-1.0`
    ```
    5. Run the executable with the following arguments. Note: GStreamer might take some time to load for the first time.



    ```
    ./test-launch "videotestsrc is-live=true ! video/x-raw,height=480,width=640,framerate=10/1 ! videoconvert ! x264enc tune=zerolatency bitrate=512 key-int-max=25 bframes=0 ! h264parse ! rtph264pay ! name=pay0 pt=96"
    ```

    You should see the following output:



    ```
    stream ready at rtsp://127.0.0.1:8554/test
    ```
    6. Verify the RTSP video stream. You can use any RTSP viewer. For example, VLC media player. To use VLC media player to view your live stream, open a new terminal and type:



    ```
    sudo apt-get install vlc
    ```

    to install VLC media player. Then type:



    ```
    vlc rtsp://127.0.0.1:8554/test
    ```

    A VLC window should pop up with the live stream. If not, check that the test-launch executable is still running and check the output for any errors.


    Another way to verify the RTSP stream is by using the gst-discoverer-1.0 utility. Type:



    ```
    gst-discoverer-1.0 "rtsp://127.0.0.1:8554/test"
    ```

    The expected output looks like this:



    ```
    Analyzing rtsp://127.0.0.1:8554/test
    Done discovering rtsp://127.0.0.1:8554/test

    Properties:
      Duration: 99:99:99.999999999
      Seekable: no
      Live: yes
      unknown #0: application/x-rtp
        video #1: H.264 (Constrained Baseline Profile)
          Stream ID: 359314d7d4bba383223927d7e57d4244d0800e629c626be81c505055c62170e2/video:0:0:RTP:AVP:96
          Width: 640
          Height: 480
          Depth: 24
          Frame rate: 10/1
          Pixel aspect ratio: 1/1
          Interlaced: false
          Bitrate: 0
          Max bitrate: 0
    ```

**To send the RTSP feed to your Kinesis Video Stream using kvssink**

This GStreamer pipeline uses `rtspsrc` to connect to the RTSP server to fetch the RTP video stream. It passes the frames to the `rtph264depay`, which extracts the H.264-encoded video frames out of the RTP packets. `h264parse` groups the video frames into the format `kvssink` can understand. `kvssink` takes the H.264-encoded video stream, packages it into the Matroska (MKV) container format, and uploads it to your Kinesis video stream.

Run the following command:

```
gst-launch-1.0 -v rtspsrc location="rtsp://127.0.0.1:8554/test" short-header=true \
  ! rtph264depay \
  ! h264parse \
  ! video/x-h264,format=avc,alignment=au \
  ! kvssink stream-name="`YourStreamName`"
```

To stop the GStreamer pipeline, select the terminal window and press **CTRL+C**.

## Utilize hardware

Some Raspberry Pi models come with hardware-accelerated H.264 encoders. You can use
them in place of `x264enc`, which is a software encoder.

1. Make sure that the GStreamer plugins are installed:

```
sudo apt-get install gstreamer1.0-tools gstreamer1.0-plugins-bad
```

2. Type:

```
gst-inspect-1.0 | grep h264
```

Determine if the following elements are available:

    * omxh264enc
    * v4l2h264enc

If they're available, you can use them. Here are some pipeline examples using
those elements:

**`omxh264enc`:**

```
gst-launch-1.0 v4l2src device=/dev/video0 \
  ! videoconvert \
  ! video/x-raw,format=I420,width=640,height=480 \
  ! `omxh264enc` control-rate=2 target-bitrate=512000 periodicity-idr=45 inline-header=FALSE \
  ! h264parse ! video/x-h264,stream-format=avc,alignment=au,profile=baseline \
  ! kvssink stream-name="`raspberry`"
```

**`v4l2h264enc` and
`v4l2convert`:**

```
gst-launch-1.0 libcamerasrc \
  ! video/x-raw,width=640,height=480,framerate=30/1,format=I420 \
  ! `v4l2convert` \
  ! `v4l2h264enc` extra-controls="controls,repeat_sequence_header=1" \
  ! video/x-h264,level='(string)4' \
  ! h264parse \
  ! video/x-h264,stream-format=avc,alignment=au,width=640,height=480,framerate=30/1 \
  ! kvssink stream-name="`test-stream`"
```

## Runtime issues

The following are some frequently encountered runtime issues, and how to troubleshoot them.

### No such element "xxxxxxxxx"

If you receive an error like the following, it means you're missing a GStreamer
plugin:

```
WARNING: erroneous pipeline: no element "videoconvert"
```

**Resolution:**

Based on which element is missing, determine the appropriate action:

- `kvssink`: See [Download and build the Kinesis Video Streams C++
  producer SDK](producersdk-cpp-rpi-download.md "producersdk-cpp-rpi-download.md").
- `libcamerasrc`: See ["Buffer pool activation failed" error](#rpi-troubleshoot-buffer "#rpi-troubleshoot-buffer") to install the `libcamerasrc` GStreamer element.
- `omxh264enc` or `v4l2h264enc`:

Follow [Install software prerequisites](producersdk-cpp-rpi-software.md "producersdk-cpp-rpi-software.md") to install all the GStreamer libraries. If you’ve installed them all and these elements don’t show up, it
means that your Raspberry Pi doesn't have the hardware. Use the software encoder `x264enc` instead.

- Other: Follow [Install software prerequisites](producersdk-cpp-rpi-software.md "producersdk-cpp-rpi-software.md") to install all the GStreamer libraries. Different GStreamer elements are found in the various GStreamer plugin groups (good, bad, ugly), so make sure to install them all.

### "Buffer pool activation failed" error

If you receive an error like the following it means the pipeline being used is
using `v4l2src`, but it should use `libcamerasrc`
instead.

```
ERROR bufferpool gstbufferpool.c:572:gst_buffer_pool_set_active:source:pool0:src start failed
WARN v4l2src gstv4l2src.c:976:gst_v4l2src_decide_allocation: error: Failed to allocate required memory.
WARN v4l2src gstv4l2src.c:976:gst_v4l2src_decide_allocation: error: Buffer pool activation failed
WARN basesrc gstbasesrc.c:3352:gst_base_src_prepare_allocation: Subclass failed to decide allocation
Error received from element source: Failed to allocate required memory.
WARN basesrc gstbasesrc.c:3132:gst_base_src_loop: error: Internal data stream error.
Debugging information: ../sys/v4l2/gstv4l2src.c(976): gst_v4l2src_decide_allocation (): /GstPipeline:live-kinesis-pipeline/GstV4l2Src:source:
Buffer pool activation failed
WARN basesrc gstbasesrc.c:3132:gst_base_src_loop: error: streaming stopped, reason not-negotiated (-4)
```

For example, if you are using the following pipeline the with the camera
module 2 without `libcamerasrc` installed, you might encounter this
error when GStreamer is trying to auto-detect which elements to use.

```
gst-launch-1.0 autovideosrc ! videoconvert ! autovideosink
```

**Resolution:**

Make sure that `libcamerasrc` is installed and use it as the source
element, rather than `v4l2src`. Type the following to install the
`libcamerasrc` GStreamer element:

```
sudo apt-get update
sudo apt-get install gstreamer1.0-libcamera
```

Once `libcamerasrc` is installed, if you're using the
`autovideosrc` element, GStreamer should automatically switch to use
the correct source `libcamerasrc` instead of `v4l2src`.

### Bus error

If you receive a Bus error shortly after starting `kvssink` (typically,
around the time the HTTP call for `PutMedia` completes), it means your
Raspberry Pi doesn't support unaligned memory access. The logs will look like the
following:

```
INFO Camera camera.cpp:1197 configuring streams: (0) 640x480-YUV420
INFO RPI pisp.cpp:1450 Sensor: /base/axi/pcie@120000/rp1/i2c@88000/imx708@1a - Selected sensor format: 1536x864-SBGGR10_1X10 - Selected CFE format: 1536x864-PC1B
[INFO ] kinesisVideoStreamFormatChanged(): Stream format changed.
[DEBUG] setRequestHeader(): Appending header to request: user-agent -> AWS-SDK-KVS-CPP-CLIENT/3.4.2/1.5.3 GCC/12.2.0 Linux/6.6.51+rpt-rpi-v8 aarch64 CPPSDK
[DEBUG] setRequestHeader(): Appending header to request: x-amzn-stream-name -> demo-stream
[DEBUG] setRequestHeader(): Appending header to request: x-amzn-producer-start-timestamp -> 1732012345.678
[DEBUG] setRequestHeader(): Appending header to request: x-amzn-fragment-acknowledgment-required -> 1
[DEBUG] setRequestHeader(): Appending header to request: x-amzn-fragment-timecode-type -> ABSOLUTE
[DEBUG] setRequestHeader(): Appending header to request: transfer-encoding -> chunked
[DEBUG] setRequestHeader(): Appending header to request: connection -> keep-alive
[INFO ] putStreamResultEvent(): Put stream result event. New upload handle 0
[WARN ] notifyDataAvailable(): [demo-stream] Failed to un-pause curl with error: 43. Curl object 0xe2f6f418
Bus error
```

Kinesis Video Streams PIC uses unaligned memory access to optimize memory usage, which isn't supported by all devices.

**Resolution:**

To use the SDK in aligned memory access mode, you need to explicitly set the
`ALIGNED_MEMORY_MODEL` CMake flag to `ON` when compiling
`kvssink`, since it defaults to `OFF`. See [Download and build the Kinesis Video Streams C++
producer SDK](producersdk-cpp-rpi-download.md "producersdk-cpp-rpi-download.md") for more detailed instructions.

### Timestamp freezes and the pipeline stalls

When using `x264enc` in a GStreamer pipeline, you may encounter
situations where the pipeline's timeline slows down significantly or completely
stalls within a few seconds.

This occurs because the `x264enc` default settings can introduce high
encoding latency, which exceeds the capacity of the default input buffer. As a
result, the input buffer fills up, causing upstream elements to block and the
pipeline to stall.

For more information, see the [GStreamer documentation](https://gstreamer.freedesktop.org/documentation/x264/index.html?gi-language=c "https://gstreamer.freedesktop.org/documentation/x264/index.html?gi-language=c").

**Resolution:**

Configure `x264enc` with the `zerolatency` tuning option.
This significantly reduces encoding latency by optimizing for real-time scenarios,
ensuring frames are processed and output more quickly.

Example configuration:

```
... ! x264enc `tune=zerolatency` byte-stream=true speed-preset=ultrafast bframes=0 key-int-max=60 ! ...
```

###### Note

While this solution effectively prevents pipeline stalling, it may impact encoding efficiency
and quality. For scenarios requiring both low latency and high quality,
consider alternative approaches, such as using hardware optimizations or
finding a web cam that outputs H.264 directly, skipping this encoding
step.

For more information, see [Utilize hardware](#producersdk-cpp-rpi-utilize "#producersdk-cpp-rpi-utilize").

### Can’t run multiple pipelines from the same `v4l2` device at the same time

Devices such as `/dev/video0` can only be accessed by one process at a time. If multiple processes try to access it at the same time, the second one waits until the first one completes.

**Resolution:**

Create a loopback device, allowing multiple processes to use the loopback interface at the same time. For more information, see
[Stack Exchange](https://raspberrypi.stackexchange.com/questions/19630/take-picam-image-while-motion-is-running/19897#19897 "https://raspberrypi.stackexchange.com/questions/19630/take-picam-image-while-motion-is-running/19897#19897").

### Internal data stream error

When you create a GStreamer pipeline, you connect elements by linking the source
pad of one element to the sink pad of another element. This linking process allows
the flow of data from the source element to the sink element, forming a data
pipeline.

The error message "Pad link failed" in the log indicates that GStreamer
encountered an issue when trying to establish a connection (link) between the pads
of two elements in your pipeline.

```
Pad link failed
Error received from element udpsrc0: Internal data stream error.
```

**Resolution:**

Determine which elements are failing to link with each other. To narrow down the
pipeline scope, remove elements from the pipeline. Replace the right-most element
with `fakesink` and remove elements one at a time.

You may need to adjust [capsfilter](https://gstreamer.freedesktop.org/documentation/coreelements/capsfilter.html?gi-language=c "https://gstreamer.freedesktop.org/documentation/coreelements/capsfilter.html?gi-language=c") elements, and/or change which elements your pipeline
uses.

Common cases are asking for a `framerate` or
`resolution` that the camera does not support. Use
`gst-device-monitor-1.0` in the terminal to obtain the supported
`framerates`, `resolutions`, and `formats`.
You can use the [videoscale](https://gstreamer.freedesktop.org/documentation/videoconvertscale/videoscale.html?gi-language=c "https://gstreamer.freedesktop.org/documentation/videoconvertscale/videoscale.html?gi-language=c") GStreamer element to adjust the video resolution, and
[videorate](https://gstreamer.freedesktop.org/documentation/videorate/?gi-language=c "https://gstreamer.freedesktop.org/documentation/videorate/?gi-language=c") to adjust the video frame rate.

To inspect the supported formats for an individual GStreamer element, type
`gst-inspect-1.0 element-name` in the terminal.
