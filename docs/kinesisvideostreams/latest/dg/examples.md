

# Amazon Kinesis Video Streams examples
<a name="examples"></a>

The following code examples demonstrate how to work with the Kinesis Video Streams API:

## Examples: Sending data to Kinesis Video Streams
<a name="examples-toc-producer"></a>
+ [Example: Kinesis Video Streams producer SDK GStreamer Plugin - kvssink](examples-gstreamer-plugin.md): Shows how to build the Kinesis Video Streams producer SDK to use as a GStreamer destination.
+ [Run the GStreamer element in a Docker container](examples-gstreamer-plugin.md#examples-gstreamer-plugin-docker): Shows how to use a pre-built Docker image for sending Real-Time Streaming Protocol (RTSP) video from an IP camera to Kinesis Video Streams.
+ [Example: Streaming from an RTSP source](examples-rtsp.md): Shows how to build your own Docker image and send RTSP video from an IP camera to Kinesis Video Streams.
+ [Example: Sending data to Kinesis Video Streams using the PutMedia API](examples-putmedia.md): Shows how to use the [Use the Java producer library](producer-sdk-javaapi.md) to send data to Kinesis Video Streams that's already in a container format (MKV) using the [PutMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html) API.

## Examples: Retrieving data from Kinesis Video Streams
<a name="examples-toc-consumer"></a>
+ [KinesisVideoExample](parser-library-write.md#parser-library-write-example): Shows how to parse and log video fragments using the Kinesis Video Streams Parser Library.
+ [Example: Parsing and rendering Kinesis Video Streams fragments](examples-renderer.md): Shows how to parse and render Kinesis video stream fragments using [JCodec](http://jcodec.org/) and [JFrame](https://docs.oracle.com/javase/7/docs/api/javax/swing/JFrame.html).

## Examples: Playing back video data
<a name="examples-toc-playback"></a>
+ [Example: Use HLS in HTML and JavaScript](hls-playback.md#how-hls-ex1): Shows how to retrieve an HLS streaming session for a Kinesis video stream and play it back in a webpage.

## Prerequisites
<a name="examples-prerequisites"></a>
+ In the sample code, you provide credentials by specifying a profile that you set in your AWS credentials profile file, or by providing credentials in the Java system properties of your integrated development environment (IDE). If you haven't already done so, first set up your credentials. For more information, see [Set up AWS Credentials and Region for Development](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-credentials.html).
+ We recommend that you use a Java IDE to view and run the code, such as one of the following:
  + [Eclipse Java Neon](https://www.eclipse.org/downloads/packages/release/neon/3/eclipse-jee-neon-3)
  + [JetBrains IntelliJ IDEA](https://www.jetbrains.com/idea/)