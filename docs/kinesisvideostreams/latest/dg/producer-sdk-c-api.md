# Use the C producer library

You can use the Amazon Kinesis Video Streams provided C producer library to write application code to send
media data from a device to a Kinesis video stream.

## Object model

The Kinesis Video Streams C producer library is based on a common component called Platform
Independent Codebase (PIC), which is available on GitHub at [https://github.com/awslabs/amazon-kinesis-video-streams-pic/](https://github.com/awslabs/amazon-kinesis-video-streams-pic/ "https://github.com/awslabs/amazon-kinesis-video-streams-pic/"). The PIC
contains platform-independent business logic for the foundational components. The Kinesis Video Streams
C producer library wraps PIC with additional layer of API that allows scenario-and
platform-specific callbacks and events. The Kinesis Video Streams C producer library has the following
components built on top of PIC:

- **Device info providers** – Exposes the
  `DeviceInfo` structure that can be directly supplied to the PIC API. You can configure a set of
  providers, including application scenario-optimized provider that can optimize the content store based on the
  number and types of streams that your application handles and the amount of required buffering configured
  based on the amount of available RAM.
- **Stream info provider** – Exposes the `StreamInfo`
  structure that can be directly supplied to the PIC API. There's a set of providers that are specific to the
  application types and the common types of streaming scenarios. These include providers such as video, audio,
  and audio and video multitrack. Each of these scenarios have defaults that you can customize according to your
  application's requirements.
- **Callback provider** – Exposes the
  `ClientCallbacks` structure that can be directly supplied to the PIC API. This includes a set of
  callback providers for networking (CURL-based API callbacks), authorization (AWS credentials API), and retry
  streaming on errors callbacks. The Callback Provider API takes a number of arguments to configure, such as the
  AWS Region and authorization information. This is done by using IoT certificates or by using AWS
  AccessKeyId, SecretKey, or SessionToken. You can enhance Callback Provider with custom callbacks if your
  application needs further processing of a particular callback to achieve some application-specific
  logic.
- **FrameOrderCoordinator** – Helps handle audio and video
  synchronization for multi-track scenarios. It has default behavior, which you can customize to handle your
  application's specific logic. It also streamlines the frame metadata packaging in PIC Frame structure before
  submitting it to the lower-layer PIC API. For non-multitrack scenarios, this component is a pass-through to
  PIC putFrame API.

The C library provides the following objects to manage sending data to a Kinesis video stream:

- **KinesisVideoClient** – Contains information about your
  device and maintains callbacks to report on Kinesis Video Streams events.
- **KinesisVideoStream** – Represents information about the
  video stream's parameters, such as name, data retention period, and media content type.

## Put media into the stream

You can use the C library provided methods (for example, `PutKinesisVideoFrame`) to put data
into the `KinesisVideoStream` object. The library then manages the internal state of the data, which
can include the following tasks:

- Performing authentication.
- Watching for network latency. If the latency is too high, the library might
  choose to drop frames.
- Tracking status of streaming in progress.

## Procedure: Use the C producer SDK

This procedure demonstrates how to use the Kinesis Video Streams client and media sources in a C
application to send H.264-encoded video frames to your Kinesis video stream.

The procedure includes the following steps:

- [Download the C producer library code](producersdk-c-download.md "producersdk-c-download.md")
- [Write and examine the code](producersdk-c-write.md "producersdk-c-write.md")
- [Run and verify the code](producersdk-c-test.md "producersdk-c-test.md")
