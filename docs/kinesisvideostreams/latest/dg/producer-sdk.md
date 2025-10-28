# Upload to Kinesis Video Streams

The Amazon Kinesis Video Streams producer libraries are a set of libraries in the Kinesis Video Streams producer SDK. The
client uses the libraries and SDK to build the on-device application for securely connecting
to Kinesis Video Streams, and streaming media data to view in the console or client applications in real
time.

Media data can be streamed in the following ways:

- In real time
- After buffering it for a few seconds
- After the media uploads
  After you create a Kinesis Video Streams stream, you can start sending data to it. You can use the SDK to
  create application code that extracts the video data, known as frames, from the media source
  and uploads it to Kinesis Video Streams. These applications are also referred to as
  _producer_ applications.

The producer libraries contain the following components:

- [Kinesis Video Streams producer client](#producer-sdk-client "#producer-sdk-client")
- [Kinesis Video Streams producer library](#producer-sdk-library "#producer-sdk-library")

## Kinesis Video Streams producer client

The Kinesis Video Streams producer client includes a single `KinesisVideoClient` class.
This class manages media sources, receives data from the sources, and manages the stream
lifecycle as data flows from a media source to Kinesis Video Streams. It also provides a
`MediaSource` interface for defining the interaction between Kinesis Video Streams and
your proprietary hardware and software.

A media source can be almost anything. For example, you can use a camera media source
or a microphone media source. Media sources are not limited to audio and video sources
only. For example, data logs might be text files, but they can still be sent as a stream
of data. You could also have multiple cameras on your phone that stream data
simultaneously.

To get data from any of these sources, you can implement the `MediaSource`
interface. This interface enables additional scenarios for which we don’t provide
built-in support. For example, you might choose to send the following to Kinesis Video Streams:

- A diagnostic data stream (for example, application logs and events)
- Data from infrared cameras, RADARs, or depth cameras

Kinesis Video Streams doesn't provide built-in implementations for media-producing devices such as cameras. To extract
data from these devices, you must implement code, thus creating your own custom media source implementation. You
can then explicitly register your custom media sources with `KinesisVideoClient`, which uploads the
data to Kinesis Video Streams.

The Kinesis Video Streams producer client is available for Java and Android applications. For more
information, see [Use the Java producer library](producer-sdk-javaapi.md "producer-sdk-javaapi.md") and [Use the Android producer library](producer-sdk-android.md "producer-sdk-android.md").

## Kinesis Video Streams producer library

The Kinesis Video Streams producer library is contained within the Kinesis Video Streams producer client. The
library is also available to use directly for those who want a deeper integration with
Kinesis Video Streams. It enables integration from devices with proprietary operating systems, network
stacks, or limited on-device resources.

The Kinesis Video Streams producer library implements the state machine for streaming to Kinesis Video Streams. It
provides callback hooks, which require that you provide your own transport
implementation and explicitly handle each message going to and from the service.

You might choose to use the Kinesis Video Streams producer library directly for the following
reasons:

- The device on which you want to run the application doesn't have a Java
  virtual machine.
- You want to write application code in languages other than Java.
- You want to reduce the amount of overhead in your code and limit it to the bare minimum level of
  abstraction, due to limitations like memory and processing power.

Currently, the Kinesis Video Streams producer library is available for Android, C, C++ and Java
applications. For more information, see the supported languages in the following
_Related
Topics_.

## Understand what producer libraries

are

[Use the Java producer library](producer-sdk-javaapi.md "producer-sdk-javaapi.md")

[Use the Android producer library](producer-sdk-android.md "producer-sdk-android.md")

[Use the C++ producer library](producer-sdk-cpp.md "producer-sdk-cpp.md")

[Use the C producer library](producer-sdk-c-api.md "producer-sdk-c-api.md")

[Use the C++ producer SDK on Raspberry Pi](producersdk-cpp-rpi.md "producersdk-cpp-rpi.md")
