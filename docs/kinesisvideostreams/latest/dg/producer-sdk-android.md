# Use the Android producer library

You can use the Amazon Kinesis Video Streams provided Android producer library to write application code,
with minimal configuration, to send media data from an Android device to a Kinesis video stream.

Perform the following steps to integrate your code with Kinesis Video Streams so that your application can start streaming
data to your Kinesis video stream:

1. Create an instance of the `KinesisVideoClient` object.
2. Create a `MediaSource` object by providing media source information.
   For example, when creating a camera media source, you provide information such as
   identifying the camera and specifying the encoding the camera uses.

When you want to start streaming, you must create a custom media source.

## Procedure: Use the Android producer

SDK

This procedure demonstrates how to use the Kinesis Video Streams Android producer client in your
Android application to send data to your Kinesis video stream.

The procedure includes the following steps:

- [Prerequisites](producersdk-android-prerequisites.md "producersdk-android-prerequisites.md")
- [Download and configure the Android
  producer library code](producersdk-android-downloadcode.md "producersdk-android-downloadcode.md")
- [Examine the code](producersdk-android-writecode.md "producersdk-android-writecode.md")
- [Run and verify the code](producersdk-android-reviewcode.md "producersdk-android-reviewcode.md")
