# Use the Java producer library

You can use the Amazon Kinesis Video Streams provided Java producer library to write application code with
minimal configuration, to send media data from a device to a Kinesis video stream.

Perform the following steps to integrate your code with Kinesis Video Streams so that your application can start streaming
data to your Kinesis video stream:

1. Create an instance of the `KinesisVideoClient` object.
2. Create a `MediaSource` object by providing media source information.
   For example, when creating a camera media source, you provide information such as
   identifying the camera and specifying the encoding the camera uses.

When you want to start streaming, you must create a custom media source. 3. Register the media source with `KinesisVideoClient`.

After you register the media source with `KinesisVideoClient`, whenever
the data becomes available with the media source, it calls
`KinesisVideoClient` with the data.

## Procedure: Use the Java producer SDK

This procedure demonstrates how to use the Kinesis Video Streams Java producer client in your Java
application to send data to your Kinesis video stream.

These steps don't require you to have a media source, such as a camera or microphone.
Instead, for testing purposes, the code generates sample frames that consist of a series
of bytes. You can use the same coding pattern when you send media data from real sources
such as cameras and microphones.

The procedure includes the following steps:

- [Download and
  configure the code](producersdk-javaapi-downloadcode.md "producersdk-javaapi-downloadcode.md")
- [Write and
  examine the code](producersdk-javaapi-writecode.md "producersdk-javaapi-writecode.md")
- [Run and verify
  the code](producersdk-javaapi-reviewcode.md "producersdk-javaapi-reviewcode.md")
