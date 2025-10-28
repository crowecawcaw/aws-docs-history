# Send data to an Amazon Kinesis video stream

This section describes how to send media data from a camera to the Kinesis video stream that you
created in the previous section. This section uses the [Use the C++ producer library](producer-sdk-cpp.md "producer-sdk-cpp.md") as a [Example: Kinesis Video Streams producer SDK GStreamer
Plugin - kvssink](examples-gstreamer-plugin.md "examples-gstreamer-plugin.md") plugin.

To send media from a variety of devices on a variety of operating systems, this tutorial uses the Kinesis Video Streams
C++ producer library and [GStreamer](https://gstreamer.freedesktop.org/ "https://gstreamer.freedesktop.org/"), an open-source media
framework that standardizes access to cameras and other media sources.

###### Topics

- [Build the SDK and samples](#send-data-build-sdk "#send-data-build-sdk")
- [Run the samples to upload media to Kinesis Video Streams](#send-data-run-samples "#send-data-run-samples")
- [Review acknowledgement objects](#gs-review-acks "#gs-review-acks")

## Build the SDK and samples

You can build the SDK and samples on your computer or in AWS Cloud9. Follow the appropriate procedures below.

Build on your computer
Use the instructions in the [readme file](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp "https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp") to build the producer library and sample
application.

This includes:

- Installing dependencies
- Cloning the repository
- Using **CMake** to generate
  **makefiles**
- Building the binary files using **make**

Build in AWS Cloud9
Follow these procedures to upload to Kinesis Video Streams in AWS Cloud9. You won't need
to download anything to your computer.

1. In the AWS Management Console, open [AWS Cloud9](https://us-west-2.console.aws.amazon.com/cloud9control/home "https://us-west-2.console.aws.amazon.com/cloud9control/home").

Select **Create environment**. 2. On the **Create environment** screen,
complete the following:

    * **Name** - Type a name for your new
     environment.
    * **Platform** - Select
     **Ubuntu Server 22.04 LTS**.

You can leave the other fields with the default
selections. 3. When the environment has been created, select
**Open** in the **Cloud9
IDE** column.

In the lower-middle area of the screen, you see
`Admin:~/environment $`. This is the AWS Cloud9
(Amazon EC2) terminal.

###### Note

If you accidentally close the terminal, select
**Window**, **New
Terminal**.

Run the following commands in the terminal to change the
volume to 20 GiB.

    1. Download the script.



    ```
    wget https://awsj-iot-handson.s3-ap-northeast-1.amazonaws.com/kvs-workshop/resize_volume.sh
    ```
    2. Give the script execute permissions.



    ```
    chmod +x resize_volume.sh
    ```
    3. Run the script.



    ```
    ./resize_volume.sh
    ```

4. Fetch the latest information on all of the software you can
   install or update through the Advanced Packaging Tool (APT).

This command doesn't update the software itself, but makes
sure your system knows what the latest available versions
are.

```
sudo apt-get update
```

5. Install the C++ producer SDK dependencies.

```
sudo apt-get install -y cmake m4 git build-essential pkg-config libssl-dev libcurl4-openssl-dev \
liblog4cplus-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
gstreamer1.0-plugins-base-apps gstreamer1.0-plugins-bad gstreamer1.0-plugins-good \
gstreamer1.0-plugins-ugly gstreamer1.0-tools
```

6. Use git to clone the C++ producer SDK.

```
git clone https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp.git
```

7. Prepare a build directory.

```
cd amazon-kinesis-video-streams-producer-sdk-cpp
mkdir build
cd build
```

8. Use CMake to generate makefiles.

```
cmake .. -DBUILD_GSTREAMER_PLUGIN=TRUE -DBUILD_DEPENDENCIES=OFF
```

The end of the expected output looks like the
following:

```
-- Build files have been written to: /home/ubuntu/environment/amazon-kinesis-video-streams-producer-sdk-cpp/build
```

9. Use make to compile the SDK and sample applications, as well
   as build the final executables.

```
make
```

The end of the expected output looks like the
following:

```
[100%] Linking CXX executable kvs_gstreamer_file_uploader_sample
[100%] Built target kvs_gstreamer_file_uploader_sample
```

10. Confirm the sample files were built. List the files in the
    current directory:

```
ls
```

Confirm that the following files are present:

    * kvs\_gstreamer\_sample
    * libgstkvssink.so

11. (Optional) You can add setting the GST_PLUGIN_PATH environment
    variable to your shell's start-up script. This ensures
    GST_PLUGIN_PATH is set properly during a new terminal session.
    In AWS Cloud9, the shell's start-up script is:
    `~/.bashrc`.

Run the following command to append the command to the end of
the shell's start-up script.

```
echo "export GST_PLUGIN_PATH=~/environment/amazon-kinesis-video-streams-producer-sdk-cpp/build" >> ~/.bashrc
```

Type the following to run the shell's start-up script:

```
source ~/.bashrc
```

Confirm GST_PLUGIN_PATH is set.

```
echo $GST_PLUGIN_PATH
```

If you set the output correctly, you will see the following
output. If the output is blank, the environment variable is not
set properly.

```
/home/ubuntu/environment/amazon-kinesis-video-streams-producer-sdk-cpp/build
```

## Run the samples to upload media to Kinesis Video Streams

The sample application does not support IMDS credentials. In your terminal, export AWS credentials
for your IAM user or role and the region your stream is located in.

```
export AWS_ACCESS_KEY_ID=`YourAccessKey`
export AWS_SECRET_ACCESS_KEY=`YourSecretKey`
export AWS_DEFAULT_REGION=`YourAWSRegion`
```

If you're using temporary AWS credentials, also export your session
token:

```
export AWS_SESSION_TOKEN=`YourSessionToken`
```

.mp4 files
Download a sample .mp4 video to upload to Kinesis Video Streams.

```
wget https://awsj-iot-handson.s3-ap-northeast-1.amazonaws.com/kvs-workshop/sample.mp4
```

Video specifications:

- **Resolution** - 1280 x 720
  pixels
- **Frame rate** - 30 frames per
  second
- **Duration** - 14.0
  seconds
- **Video encoding** - H.264, in
  track 1
- **Keyframes** - Every 3 seconds,
  resulting in a fragment duration (also known as a group of
  pictures (GoP) size) of 3 seconds, with the final fragment being
  2 seconds long.

Run the following command with the name of the stream you previously
created. If you haven't created a stream yet, see [Create an Amazon Kinesis video stream](gs-createstream.md "gs-createstream.md").

```
./kvs_gstreamer_sample `YourStreamName` ./sample.mp4
```

Sample video from GStreamer
Use the following command to generate a video using GStreamer.

Tell GStreamer where to locate the `kvssink` GStreamer
plugin. In your build directory, specify the path to the folder
containing the `libgstkvssink.so` file.

From your build directory, run the following command:

```
export GST_PLUGIN_PATH=`pwd`
```

This GStreamer pipeline generates a live test video stream with a
standard test pattern that runs at 10 frames per second with a
resolution of 640x480 pixels. An overlay is added displaying the current
system time and date. The video is then encoded into H.264 format and
keyframes are generated at most every 10 frames, resulting in a fragment
duration (also known as a group of pictures (GoP) size) of 1 second.
`kvssink` takes the H.264-encoded video stream, packages
it into the Matroska (MKV) container format, and uploads it to your
Kinesis video stream.

Run the following command:

```
gst-launch-1.0 -v videotestsrc is-live=true \
  ! video/x-raw,framerate=10/1,width=640,height=480 \
  ! clockoverlay time-format="%a %B %d, %Y %I:%M:%S %p" \
  ! x264enc bframes=0 key-int-max=10 \
  ! h264parse \
  ! kvssink stream-name="`YourStreamName`"
```

To stop the GStreamer pipeline, select the terminal window and press
**CTRL+C**.

###### Note

For more information about using the GStreamer plugin to stream video
from an RTSP stream from a camera, or from a USB camera, see [Example: Kinesis Video Streams producer SDK GStreamer
Plugin - kvssink](examples-gstreamer-plugin.md "examples-gstreamer-plugin.md").

## Review acknowledgement objects

During upload, Kinesis Video Streams will send acknowledgement objects back to the client performing the upload. You should see these printed in the command output. An example looks like the following:

```
{"EventType":"PERSISTED","FragmentTimecode":`1711124585823`,"FragmentNumber":"`12345678901234567890123456789012345678901234567`"}
```

If the acknowledgement’s `EventType` is `PERSISTED`, it
means Kinesis Video Streams has durably stored and encrypted this chunk of media for retrieval,
analysis, and long-term storage.

For more information about acknowledgements, see [PutMedia](API_dataplane_PutMedia.md "API_dataplane_PutMedia.md").
